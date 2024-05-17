#!/usr/bin/python3

""" The user model defines the user model"""
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import BaseModel
from .mixins import PersonInfoMixin

from werkzeug.security import generate_password_hash, check_password_hash


class User(PersonInfoMixin, BaseModel, db.Model):
    __tablename__ = "User"
    username: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    member = so.relationship(
        "Member", uselist=False, back_populates="user", viewonly=True
    )

    families_created = so.relationship("Family", back_populates="creator", lazy=True)

    @classmethod
    def create_user(cls, username, email, first_name, last_name, password):

        new_user = cls.query.filter_by(email=email).one_or_none()
        if new_user:
            return None
        new_user = cls(
            username=username, email=email, first_name=first_name, last_name=last_name
        )
        new_user.set_password(password)
        return new_user

    def update_user(self, **kwargs):
        self.update(**kwargs)
        return self

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_families_created(self):
        return [family.to_dict() for family in self.families_created]


class Member(PersonInfoMixin, BaseModel, db.Model):
    __tablename__ = "Member"
    registered = so.mapped_column(sa.BOOLEAN, default=False)
    user_id: so.Mapped[str] = so.mapped_column(
        sa.String(255), sa.ForeignKey("User.id"), nullable=True
    )
    user = so.relationship("User", backref="related_member")
    families = so.relationship("FamilyMember", back_populates="member")

    def update_member(self, **kwargs):
        self.update(**kwargs)
        return self

    @classmethod
    def get_family(cls, member_id):
        member = cls.query.get(member_id)
        if member:
            return [family.family for family in member.families]
        return None

    def get_parent(self, role):
        for family_member in self.families:
            if family_member.role == role:
                return family_member.member
        return None

    def get_ancestors(self, level):
        ancestors = []
        current_member = self

        for _ in range(level):
            father = current_member.get_parent("father")
            mother = current_member.get_parent("mother")

            if father:
                ancestors.append(father)
            if mother:
                ancestors.append(mother)

            current_member = father if father else mother

        return ancestors

    def get_siblings(self):
        siblings = []
        for family_member in self.families:
            if family_member.role == "child":
                for sibling in family_member.family.members:
                    if sibling.role == "child" and sibling.member_id != self.id:
                        siblings.append(sibling.member.to_dict())
        return siblings

    def to_dict(self, family_id=None):
        data = super().to_dict()

        if family_id:
            family_member = next(
                (fm for fm in self.families if fm.family_id == family_id), None
            )
            if family_member:
                data["role"] = family_member.role
        return data

    def get_decendants(self, level, current_level=0):
        decendants = []
        if current_level < level:
            # Get the families where the member's role is either "mother" or "father"
            parent_families = [
                fm for fm in self.families if fm.role in ["mother", "father"]
            ]

            for family_member in parent_families:
                # Get the children of the member in the current family
                children = [
                    fm.member
                    for fm in family_member.family.members
                    if fm.role == "child"
                ]

                for child in children:
                    decendants.append(child.to_dict())
                    # Recursively get the descendants of the child
                    decendants.extend(child.get_decendants(level, current_level + 1))

        return decendants
