from app.models import User, Family, Member, FamilyMember
from app import db
from app.api.errors import bad_request


def get_user_info(user):
    return user.to_dict()


def get_families_created(user):
    return user.get_families_created()


def get_user_family(member):
    if member:
        family = FamilyMember.get_family_by_member_id(member.id)
        if family:
            return family.to_dict()
    return None


def delete_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    db.session.delete(user)
    db.session.commit()
    return {"msg": "successfully deleted"}


def update_user(user, user_data):
    if not user:
        return None
    user.update_user(**user_data)
    user.member.update(**user_data)
    db.session.commit()
    return user.to_dict()


def handle_existing_member(member, role, request):
    if role not in [family.role for family in member.families]:
        new_family = create_family(member, role, request=request)
        return new_family.to_dict(), 201
    else:
        return bad_request(f"You are already a {role} in a family!")


def handle_new_member(current_user, role, request):
    new_member = create_member(current_user)
    new_family = create_family(new_member, role, request=request)
    return new_family.to_dict(), 201


def create_member(current_user):
    new_member = Member(
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        date_of_birth=current_user.date_of_birth,
    )
    new_member.user_id = current_user.id
    new_member.registered = True
    db.session.add(new_member)
    return new_member


def create_family(member, role, request):
    new_family = Family.create_family(member.user_id, **request)
    fam_member = FamilyMember().create_family_member(
        new_family.id, member.id, role=role
    )
    db.session.add_all([new_family, fam_member])
    db.session.commit()
    return new_family
