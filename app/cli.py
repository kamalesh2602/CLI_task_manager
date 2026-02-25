import click
from app.db import init_db
from app.task_manager import (
    add_task,
    list_tasks,
    complete_task,
    delete_task,
)


@click.group()
def cli():
    """Simple CLI Task Manager"""
    init_db()  # Ensure DB + table exists


@cli.command()
@click.argument("title")
@click.option("--description", "-d", default=None, help="Task description")
def add(title, description):
    """Add a new task"""
    add_task(title, description)
    click.echo("Task added successfully!")


@cli.command()
def list():
    """List all tasks"""
    tasks = list_tasks()

    if not tasks:
        click.echo("No tasks found.")
        return

    for task in tasks:
        click.echo(
            f"ID: {task[0]} | Title: {task[1]} | Status: {task[2]} | Created: {task[3]}"
        )


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Mark task as completed"""
    complete_task(task_id)
    click.echo("Task marked as completed!")


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task"""
    delete_task(task_id)
    click.echo("Task deleted!")


if __name__ == "__main__":
    cli()
