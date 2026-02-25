import os
import tempfile
import pytest

from app.db import init_db
from app.task_manager import add_task, list_tasks, complete_task, delete_task


@pytest.fixture
def test_db():
    # Create temporary database file
    db_fd, db_path = tempfile.mkstemp()
    os.environ["DB_PATH"] = db_path

    init_db()

    yield db_path

    os.close(db_fd)
    os.remove(db_path)


def test_add_task(test_db):
    add_task("Test Task", "Testing add")
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0][1] == "Test Task"


def test_complete_task(test_db):
    add_task("Complete Me")
    complete_task(1)
    tasks = list_tasks()
    assert tasks[0][2] == "completed"


def test_delete_task(test_db):
    add_task("Delete Me")
    delete_task(1)
    tasks = list_tasks()
    assert len(tasks) == 0
