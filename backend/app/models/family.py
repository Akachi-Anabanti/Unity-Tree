#!/usr/bin/python3
"""Represents the Family model"""

import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import BaseModel
from app import db


class Family(BaseModel, db.Model):
    __tablename__ = "Family"
    name: so.Mapped[str] = so.mapped_column(sa.String(125))
    country: so.Mapped[str] = so.mapped_column(
        sa.String(125), nullable=True, index=True
    )
    state: so.Mapped[str] = so.mapped_column(sa.String(125), nullable=True, index=True)
    city: so.Mapped[str] = so.mapped_column(sa.String(125), nullable=True, index=True)
    lga: so.Mapped[str] = so.mapped_column(sa.String(125), nullable=True, index=True)
    community: so.Mapped[str] = so.mapped_column(
        sa.String(125), nullable=True, index=True
    )

    members = so.relationship(
        "FamilyMember", back_populates="family", cascade="all, delete"
    )
    media = so.relationship("Media", back_populates="family", cascade="all,delete")

    creator_id = so.mapped_column(
        sa.String(255), sa.ForeignKey("User.id", name="fk_creator_id"), nullable=False
    )

    creator = db.relationship("User", back_populates="families_created")

    @classmethod
    def get_family_members(cls, family_id):
        family = cls.query.filter_by(id=family_id).one_or_none()

        if family and len(family.members) > 0:
            children = []
            members_dict = {}
            for assoc in family.members:
                if assoc.role == "father" or assoc.role == "mother":

                    members_dict[assoc.role] = assoc.member.to_dict(
                        family_id
                    )  # calls the member models basic_info_dict
                else:
                    children.append(assoc.member.to_dict(family_id))
                    # calls the member models basic_info_dict
            members_dict["children"] = children
            return members_dict
            # print(family.members)
            # return [assoc.member.basic_info_dict() for assoc in family.members]
        return None

    @classmethod
    def create_family(cls, creator_id, **kwargs):
        new_family = cls(creator_id=creator_id, **kwargs)
        return new_family

    def update_family(self, **kwargs):
        self.update(**kwargs)
        return self
