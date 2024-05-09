#!/usr/bin/python3
"""Represents the Family model"""

import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import BaseModel
from app import db


class Family(BaseModel, db.Model):
    __tablename__ = "Family"
    name: so.Mapped[str] = so.mapped_column(sa.String(125))
    members = so.relationship("FamilyMember", back_populates="family")
    media = so.relationship("Media", back_populates="family")
    creator_id = so.mapped_column(
        sa.String(255), sa.ForeignKey("User.id", name="fk_creator_id"), nullable=False
    )

    creator = db.relationship("User", back_populates="families_created")

    @classmethod
    def get_family_members(cls, family_id):
        family = cls.query.filter_by(id=family_id).one_or_none()

        if family:
            children = []
            parents = {}
            for member in family.members:
                if member.Role == "father" or member.Role == "mother":

                    parents[member.Role] = (
                        member.member.basic_info_dict()
                    )  # calls the member models basic_info_dict
                else:
                    children.append(member.member.basic_info_dict())
                    # calls the member models basic_info_dict
            members_dict = parents.copy()
            members_dict["children"] = children
            return members_dict
        # return [assoc.members for assoc in family.members]
        return None

    @classmethod
    def create_family(cls, name, creator_id):
        new_family = cls(name=name, creator_id=creator_id)
        return new_family

    def update_family(self, **kwargs):
        self.update(**kwargs)
        return self
