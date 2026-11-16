#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# one line short cut for git: 

# git add . && git commit -m "  " && git push

# # 1. Make changes to your code

# # 2. Check which files changed
# git status

# # 3. Stage changes
# git add .

# # 4. Commit changes
# git commit -m "Describe what you changed"

# # 5. Upload changes to GitHub
# git push


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
