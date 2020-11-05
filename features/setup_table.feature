# file:features/tutorial06_step_setup_table.feature
Feature: Setup Department

   Scenario: Setup Table
     Given a set of specific users to "Silicon":
        | name      | department  |
        | Barry     | Beer Cans   |
        | Pudey     | Silly Walks |
        | Two-Lumps | Silly Walks |
    When we count the number of people in each department
    Then we will find two people in "Silly Walks"
     But we will find one person in "Beer Cans"
