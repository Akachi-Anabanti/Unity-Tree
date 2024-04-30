#!/usr/bin/python3

""" The user model defines the user model"""

from sqlachemy import Column, Integer


relationship =  'self-refrencing many to many relationship'


class User(Base):
    """The user class"""
    tablename = "user"

    id = ""
    first_name = ""
    last_name = ""
    email = ""
    created_at = ""
    updated_at = ""


    def __repr__(self):
        return "User(" + self.first_name + " " \
                + self.last_name + ")"

