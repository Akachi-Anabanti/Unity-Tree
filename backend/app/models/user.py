#!/usr/bin/python3

""" The user model defines the user model"""
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import BaseModel


from werkzeug.security import generate_password_hash, check_password_hash


class PersonInfoMixin:

    @so.declared_attr
    def img(cls):
        return so.mapped_column(sa.String(255), nullable=True)

    @so.declared_attr
    def first_name(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def last_name(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def date_of_birth(cls):
        return sa.Column(sa.DATE, nullable=True)

    @so.declared_attr
    def height(cls):
        return so.mapped_column(sa.String(60), nullable=True)

    @so.declared_attr
    def hobbies(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def marital_status(cls):
        return so.mapped_column(sa.Boolean, default=False)

    @so.declared_attr
    def ethnicity(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def race(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def state_of_origin(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def nationality(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def occupation(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def nickname(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def genotype(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def blood_group(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def title(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def skin_color(cls):
        return so.mapped_column(sa.String(120), nullable=True)

    @so.declared_attr
    def gender(cls):
        return so.mapped_column(sa.String(120), nullable=True)


class User(PersonInfoMixin, BaseModel, db.Model):
    __tablename__ = "User"
    username: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120))
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    member = so.relationship(
        "Member", uselist=False, back_populates="user", viewonly=True
    )

    families_created = so.relationship("Family", back_populates="creator", lazy=True)

    @classmethod
    def create_user(cls, username, email, password):

        new_user = cls.query.filter_by(email=email).one_or_none()
        if new_user:
            return None
        new_user = cls(username=username, email=email)
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
    families = so.relationship(
        "FamilyMember", back_populates="member", cascade="all, delete-orphan"
    )

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

    def get_decendants(self, level):
        decendants = []
        nodes = [(self, 0)]
        while nodes:
            current_node, current_level = nodes.pop(0)
            if current_level < level:
                children = [
                    family_member.member
                    for family_member in current_node.families
                    if family_member.role == "child"
                ]

                decendants.extend(children)
                nodes.extend((child, current_level + 1) for child in children)
        return [decendant.to_dict() for decendant in decendants]

    def get_siblings(self):
        siblings = []
        for family_member in self.families:
            if family_member.role == "child":
                for sibling in family_member.family.members:
                    if sibling.role == "child" and sibling.member_id != self.id:
                        siblings.append(sibling.member)
        return siblings
