#!/usr/bin/python3

""" The user model defines the user model"""
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import BaseModel
from typing import Optional
from datetime import date

from werkzeug.security import generate_password_hash, check_password_hash


class PersonInfoMixin:
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
    # media = so.relationship("Media", back_populates="user")

    # def __init__(self):
    #     self.set_password(self.password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


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
