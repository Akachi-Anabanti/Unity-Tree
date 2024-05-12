#!/usr/bin/python3

"""Defines Family and Member relationship"""
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import BaseModel


class FamilyMember(BaseModel, db.Model):
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


# POSSIBLE QUERIES

# # get the member
# member = session.query(Member).filter(Member.MemberId == <member_id>).first()

# # get the associations where the member is a 'father'
# father_associations = session.query(FamilyMember).filter(FamilyMember.MemberId == member.MemberId, FamilyMember.role == 'father').all()

# # get the families where the member is a 'father'
# father_families = [assoc.family for assoc in father_associations]

# # get the associations where the member is a 'child'
# child_associations = session.query(FamilyMember).filter(FamilyMember.MemberId == member.MemberId, FamilyMember.role == 'child').all()

# # get the families where the member is a 'child'
# child_families = [assoc.family for assoc in child_associations]


# # get the family
# family = session.query(Family).filter(Family.FamilyId == <family_id>).first()

# # get the members of the family
# members = [assoc.member for assoc in family.members]


# # get the member
# member = session.query(Member).filter(Member.MemberId == <member_id>).first()

# # get the families where the member is a child
# child_families = session.query(FamilyMember).filter(FamilyMember.MemberId == member.MemberId, FamilyMember.role == 'child').all()

# # get the siblings and parents
# siblings = []
# parents = []
# for assoc in child_families:
#     family_members = [assoc.member for assoc in assoc.family.members]
#     for family_member in family_members:
#         if family_member.MemberId != member.MemberId:
#             if family_member.role in ['father', 'mother']:
#                 parents.append(family_member)
#             else:
#                 siblings.append(family_member)


# # get the member
# member = session.query(Member).filter(Member.MemberId == <member_id>).first()

# # get the families where the member is a father
# father_families = session.query(FamilyMember).filter(FamilyMember.MemberId == member.MemberId, FamilyMember.Role == 'father').all()

# # get the children and spouse
# children = []
# spouse = None
# for assoc in father_families:
#     family_members = [assoc.member for assoc in assoc.family.members]
#     for family_member in family_members:
#         if family_member.MemberId != member.MemberId:
#             if family_member.role == 'child':
#                 children.append(family_member)
#             elif family_member.role == 'mother':
#                 spouse = family_member


# DELETING A FAMILY

# When deleting a family:
# family = session.query(Family).filter(Family.FamilyId == <family_id>).first()
# for assoc in family.members:
#     if not assoc.member.registered:
#         session.delete(assoc.member)
# session.delete(family)
# session.commit()


# assoc = session.query(FamilyMember).filter(FamilyMember.FamilyId == <family_id>, FamilyMember.MemberId == <member_id>).first()
# session.delete(assoc)
# session.commit()
