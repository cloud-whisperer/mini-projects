# MODULE: main.py
# Entry point for the Secure Task Logger

from task_input import collect_tasks
from logger import write_logs

from user_context import get_current_user
print("👤 Current user:", get_current_user())


def main():
    print("🔐 Secure Task Logger v1.0\n")

    tasks = collect_tasks()
    write_logs(tasks)

    if tasks:
        print(f"\n📊 Total secure events logged: {len(tasks)}")
    else:
        print("\n⚠️  No events recorded.")

    print("\n✅ Session complete. Stay secure.")


if __name__ == "__main__":
    main()
