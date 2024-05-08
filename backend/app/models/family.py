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

    @classmethod
    def get_family_members(cls, family_id):
        family = cls.query.filter_by(id=family_id).one_or_none()

        if family is None:
            return None

        members = [assoc.members for assoc in family.members]
        children = []
        parents = {}

        for member in members:
            if member.Role == "father" or member.Role == "mother":
                parents[member.Role] = member.to_dict()
            else:
                children.append(member.to_dict())

        members_dict = parents.copy()
        members_dict["children"] = children
        return members_dict
