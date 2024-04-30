#!/usr/bin/python3

"""The Media model
holds all the images partaining to a  user"""


class Media(Base):

    tablename = "media"
    path = ""
    caption = ""
    uploaded_at = ""
    size = ""
    format = ""

    user_id = ""

