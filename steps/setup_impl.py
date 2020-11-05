from behave   import given, when, then
from hamcrest import assert_that, equal_to
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder
#
from tested_module.company_model import CompanyModel
from testutil import NamedNumber

@given('a set of specific users to "{company}"')
def step_impl(context, company):
    model = getattr(context, "model", None)
    if not model:
        context.model = CompanyModel(company)
    #
    for row in context.table:
        context.model.add_user(row["name"], deparment=row["department"])

@when('we count the number of people in each department')
def step_impl(context):
    context.model.count_persons_per_department()

@then('we will find {count} people in "{department}"')
def step_impl(context, count, department):
    count_ = NamedNumber.from_string(count)
    assert_that(count_, equal_to(context.model.get_headcount_for(department)))

@then('we will find one person in "{department}"')
def step_impl(context, department):
    assert_that(1, equal_to(context.model.get_headcount_for(department)))


@when('we remove "{user}" from "{department}" in "{company}"')
def step_impl(context, user, department, company):
    model = getattr(context, "model", None)
    if not model:
        context.model = CompanyModel(company)
    #
    obj = context.model.departments[department]
    print(obj)
    obj.remove_member(user)


    
@then('we will have the following people in "{department}"')
def step_impl(context, department):
    """
    Compares expected with actual persons in a department.
    NOTE: Unordered comparison (ordering is not important).
    """
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, "Department %s is unknown" % department)
    # -- NORMAl-CASE:
    expected_persons = [ row["name"]    for row in context.table ]
    actual_persons   = department_.members

    # -- UNORDERED TABLE-COMPARISON (using: pyhamcrest)
    assert_that(contains_inanyorder(*expected_persons), actual_persons)

@then('we will have at least the following people in "{department}"')
def step_impl(context, department):
    """
    Compares subset of persons with actual persons in a department.
    NOTE: Unordered subset comparison.
    """
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, "Department %s is unknown" % department)
    # -- NORMAl-CASE:
    expected_persons = [ row["name"]    for row in context.table ]
    actual_persons   = department_.members

    # -- TABLE-SUBSET-COMPARISON (using: pyhamcrest)
    assert_that(has_items(*expected_persons), actual_persons)