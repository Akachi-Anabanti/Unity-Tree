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
