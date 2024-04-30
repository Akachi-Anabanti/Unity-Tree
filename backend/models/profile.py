#!/usr/bin/python3
"""The user profile information"""

from sqlalchemy import *


class Profile(Base):
    """The user profile information classs"""

    tablename = "profile"

    id = ""
    date_of_birth  = ""
    age = ""
    height = ""
    image = ""
    hobbies = []
    marital_status = ""
    ethnicity = ""
    race = ""
    state_of_origin = ""
    nationality = ""
    occupation = ""
    nickname = ""
    genotype = ""
    blood_group = ""
    title = ""

    user_id =  ""
