#!/usr/bin/python3

"""Defines the base Model"""
from datetime import datetime, timezone
import uuid
import sqlalchemy as sa
import sqlalchemy.orm as so


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    id: so.Mapped[str] = so.mapped_column(sa.String(255), primary_key=True)
    created_at: so.Mapped[datetime] = sa.Column(
        sa.DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: so.Mapped[datetime] = sa.Column(
        sa.DateTime, default=datetime.now(timezone.utc)
    )

    def __init__(self, *args, **kwargs):
        """Defines the model initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)

            else:
                self.created_at = datetime.now(timezone.utc)
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of BaseModel"""
        return "[{:s}]({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    # def to_dict(self):
    #     """returns a dictionary containing the key value pairs"""
    #     new_dict = self.__dict__.copy()
    #     if "created_at" in new_dict:
    #         new_dict["created_at"] = new_dict["created_at"].strftime(time)

    #     if "updated_at" in new_dict:
    #         new_dict["updated_at"] = new_dict["updated_at"].strftime(time)

    #     new_dict["__class__"] = self.__class__.__name__

    #     if "_sa_instance_state" in new_dict:
    #         del new_dict["_sa_instance_state"]
    #     if "passwrod_hash" in new_dict:
    #         del new_dict["password_hash"]
    #     return new_dict

    def to_dict(self):
        """returns a dictionary containing all SQLAlchemy columns"""
        class_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        if "password_hash" in class_dict:
            del class_dict["password_hash"]
        return class_dict

    def basic_info_dict(self):
        """returns a dictionary containing basic details"""

        basic_details = [
            "id",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "username",
            "email",
        ]
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
            if c.name in basic_details
        }

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)
