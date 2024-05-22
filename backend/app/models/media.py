#!/usr/bin/python3

"""The Media model
holds all the images partaining to a  user"""

import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import BaseModel
from app import db


class Media(BaseModel, db.Model):
    """Defines the media"""

    __tablename__ = "media"

    file_name: so.Mapped[str] = so.mapped_column(sa.String(255))
    file_type: so.Mapped[str] = so.mapped_column(sa.String(255))

    family_id = so.mapped_column(sa.String(255), sa.ForeignKey("Family.id"))
    member_id = so.mapped_column(sa.String(255), sa.ForeignKey("Member.id"))
    user_id = so.mapped_column(sa.String(255), sa.ForeignKey("User.id"))
    family = so.relationship("Family", back_populates="media")
    # person = so.relationship("PersonInfo", back_populates="media")
