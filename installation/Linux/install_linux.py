from installation.Linux.create_directories import create_directories
from installation.Linux.create_logging_files import create_logging_files
from installation.Linux.create_storage_files import create_storage_files

def main():
    create_directories()
    create_logging_files()
    create_storage_files()

