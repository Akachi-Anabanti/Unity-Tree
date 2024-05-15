#!/usr/bin/python3

"""Defines Family and Member relationship"""
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import BaseModel


class FamilyMember(BaseModel, db.Model):
    """A table that expresses a two way relationship
    between family and member tables"""

    __tablename__ = "family_member"

    family_id = so.mapped_column(
        sa.String(255), sa.ForeignKey("Family.id"), primary_key=True
    )
    member_id = so.mapped_column(
        sa.String(255), sa.ForeignKey("Member.id"), primary_key=True
    )
    role: so.Mapped[str] = so.mapped_column(sa.String(60))
    family = so.relationship("Family", back_populates="members")
    member = so.relationship("Member", back_populates="families")

    @classmethod
    def create_family_member(cls, family_id, member_id, role):
        new_family_member = cls(family_id=family_id, member_id=member_id, role=role)
        return new_family_member

    @classmethod
    def get_family_member(cls, member_id):
        member = cls.query.filter_by(member_id=member_id).one_or_none()
        return member.member

    @classmethod
    def get_family_by_member_id(cls, member_id):
        family_member = cls.query.filter_by(member_id=member_id).one_or_none()
        if family_member:
            return family_member.family
        else:
            return None

    @classmethod
    def delete_family_member(cls, family_id, member_id):
        family_member = cls.query.filter_by(
            family_id=family_id, member_id=member_id
        ).first()
        if family_member:
            return family_member
        return None

    @classmethod
    def delete_family_members(cls, family_id):
        family_members = cls.query.filter_by(family_id=family_id).all()
        return family_members
