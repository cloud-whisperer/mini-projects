# MODULE: logger.py
# Handles secure log storage

LOG_FILE = "secure_tasks.log"


def write_logs(entries):
    """
    Writes log entries to an append-only log file.
    """
    if not entries:
        return

    with open(LOG_FILE, "a") as file:
        for entry in entries:
            file.write(entry + "\n")
