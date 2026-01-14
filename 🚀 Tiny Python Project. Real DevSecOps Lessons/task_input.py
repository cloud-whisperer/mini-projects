# MODULE: task_input.py
# Handles task collection and validation

from datetime import datetime
from user_context import get_current_user
from security import hash_entry


def collect_tasks():
    """
    Collects tasks from user input and returns secure log entries.
    """
    tasks = []
    user = get_current_user()

    print("⚠️  This action is logged and monitored.")
    print("📝 Add a task (or type 'done' to finish):")

    while True:
        task_text = input("Enter a task: ").strip()

        if task_text.lower() == "done":
            break

        if task_text == "":
            print("⚠️  Empty task ignored.")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        base_entry = f"[{timestamp}] user={user} action={task_text}"
        hash_value = hash_entry(base_entry)

        secure_entry = f"{base_entry} hash={hash_value}"
        tasks.append(secure_entry)

    return tasks