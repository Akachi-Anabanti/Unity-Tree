from datetime import datetime
from app import models, db
from app.api.errors import bad_request, not_found


def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None


def fetch_family_by_member_id(_id):
    return models.FamilyMember.get_family_by_member_id(_id)


def fetch_family_by_fam_id(_id):
    return models.Family.query.get(_id)


def fetch_family_members(family_id):
    return models.Family.get_family_members(family_id)


def fetch_member(member_id):
    return models.Member.query.get(member_id)


def fetch_user(member_id):
    return models.User.query.get(member_id)


def fetch_ancestors(member_id, level):
    member = models.Member.query.get(member_id)
    if not member:
        return None
    return member.get_ancestors(level)


def fetch_descendants(member_id, level):
    member = models.Member.query.get(member_id)
    if not member:
        return None
    return member.get_descendants(level)


def fetch_family_owner(family_id):
    return models.Family.query.get(family_id)


def create_family(creator_id, family_data):
    family = models.Family.create_family(creator_id=creator_id, **family_data)
    db.session.add(family)
    db.session.commit()
    return family


def create_family_member(family_id, member_data):
    first_name = member_data.get("firstName")
    last_name = member_data.get("lastName")
    role = member_data.get("role")
    date_string = member_data.get("dateOfBirth")

    date_of_birth = parse_date(date_string=date_string)
    family = models.Family.query.get(family_id)
    if not family:
        return None

    new_member = models.Member(
        first_name=first_name, last_name=last_name, date_of_birth=date_of_birth
    )
    new_member.last_name = family.name

    db.session.add(new_member)
    fam_member = models.FamilyMember().create_family_member(
        family_id, new_member.id, role
    )
    db.session.add(fam_member)
    db.session.commit()
    return new_member


def update_family(family_id, family_data):
    family = models.Family.query.get(family_id)
    if not family:
        return None
    family.update_family(**family_data)
    db.session.commit()
    return family


def update_family_member(member, member_data):
    marital_status = member_data.get("marital_status", None)
    if marital_status is not None and type(marital_status) == str:
        marital_status = bool(marital_status.lower() == "true")
        member_data["marital_status"] = marital_status

    date_of_birth = member_data.get("date_of_birth", None)
    if date_of_birth is not None:
        date_object = parse_date(date_of_birth)
        member_data["date_of_birth"] = date_object

    member.update_member(**member_data)
    db.session.commit()
    return member


def delete_family(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        return None
    family_dict = family.to_dict()
    db.session.delete(family)
    db.session.commit()
    return family_dict


def delete_family_member(family_id, member_id):
    member = models.FamilyMember.delete_family_member(family_id, member_id)
    if not member:
        return None
    member_dict = member.to_dict()
    db.session.delete(member)
    db.session.commit()
    return member_dict


def delete_family_members(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        return None
    family_members = models.FamilyMember.delete_family_members(family_id)
    for member in family_members:
        db.session.delete(member)
    db.session.commit()
    return family_members
