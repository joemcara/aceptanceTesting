from behave import given, when, then
from datetime import datetime
from main import ToDoListManager, Task

@given('I have an empty to-do list')
def step_given_empty_todo_list(context):
    context.manager = ToDoListManager()

@when('I add a new task with description "{description}" and due date "{due_date}"')
def step_when_add_new_task(context, description, due_date):
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    task = Task(len(context.manager.tasks) + 1, description, due_date)
    context.manager.add_task(task)

@then('the to-do list should contain {count} task')
def step_then_todo_list_should_contain_tasks(context, count):
    assert len(context.manager.tasks) == int(count)

@then('the task should have description "{description}" and due date "{due_date}"')
def step_then_task_should_have_description_due_date(context, description, due_date):
    task = context.manager.tasks[0]
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    assert task.description == description
    assert task.due_date == due_date

@then('the task should be marked as not completed')
def step_then_task_should_be_not_completed(context):
    task = context.manager.tasks[0]
    assert not task.completed

@given('I have a to-do list with tasks')
def step_given_todo_list_with_tasks(context):
    context.manager = ToDoListManager()
    tasks = [
        Task(1, "Buy groceries", datetime.strptime("2024-08-01", "%Y-%m-%d")),
        Task(2, "Read a book", datetime.strptime("2024-08-02", "%Y-%m-%d"))
    ]
    for task in tasks:
        context.manager.add_task(task)

@when('I list all the tasks')
def step_when_list_all_tasks(context):
    context.tasks = context.manager.list_tasks()

@then('I should see the following tasks')
def step_then_should_see_following_tasks(context):
    expected_tasks = context.table
    for row in expected_tasks:
        task = next((task for task in context.manager.tasks if task.description == row['description']), None)
        assert task is not None
        assert task.due_date.strftime("%Y-%m-%d") == row['due_date']
        assert str(task.completed) == row['completed']

@when('I mark the task with ID {task_id:d} as completed')
def step_when_mark_task_as_completed(context, task_id):
    context.manager.mark_task_as_completed(task_id)

@then('the task with ID {task_id:d} should be marked as completed')
def step_then_task_should_be_marked_completed(context, task_id):
    task = next(task for task in context.manager.tasks if task.task_id == task_id)
    assert task.completed

@when('I clear the entire to-do list')
def step_when_clear_entire_todo_list(context):
    context.manager.clear_all_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert len(context.manager.tasks) == 0
