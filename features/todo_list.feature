Feature: To-Do List Management

  Scenario: Add a new task to the to-do list
    Given I have an empty to-do list
    When I add a new task with description "Buy groceries" and due date "2024-08-01"
    Then the to-do list should contain 1 task
    And the task should have description "Buy groceries" and due date "2024-08-01"
    And the task should be marked as not completed

  Scenario: List all the tasks in the to-do list
    Given I have a to-do list with tasks
    When I list all the tasks
    Then I should see the following tasks:
      | description      | due_date   | completed |
      | Buy groceries    | 2024-08-01 | False     |
      | Read a book      | 2024-08-02 | False     |

  Scenario: Mark a task as completed
    Given I have a to-do list with tasks
    When I mark the task with ID 1 as completed
    Then the task with ID 1 should be marked as completed

  Scenario: Clear the entire to-do list
    Given I have a to-do list with tasks
    When I clear the entire to-do list
    Then the to-do list should be empty
