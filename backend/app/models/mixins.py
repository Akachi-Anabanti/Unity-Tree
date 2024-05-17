import sqlalchemy as sa
import sqlalchemy.orm as so


class PersonInfoMixin:
    """Personal Information on user/members"""

    @so.declared_attr
    def img(cls):
        return so.mapped_column(sa.String(255), nullable=True)

    @so.declared_attr
    def first_name(cls):
        return so.mapped_column(sa.String(120), nullable=False)

    @so.declared_attr
    def last_name(cls):
        return so.mapped_column(sa.String(120), nullable=False)

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


class EducationInfoMixin:
    """Information about the persons Education"""

    name_of_school = ""
    start_date = ""
    end_date = ""
    state = ""
    country = ""
    degree = ""
    user_id = ""


class SearchableMixin:
    """defines the abstract searchables for a class"""

    pass
