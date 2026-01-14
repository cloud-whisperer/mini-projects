# MODULE: user_context.py
# Handles user identity and context

import os

#print("✅ user_context.py loaded")


def get_current_user():
    """
    Returns the current system user.
    """
    return os.getenv("USERNAME") or os.getenv("USER") or "unknown-user"


# print("✅ user_context.py loaded")