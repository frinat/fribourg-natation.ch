#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frinat.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Config')

    from configurations.management import execute_from_command_line
    execute_from_command_line(sys.argv)
