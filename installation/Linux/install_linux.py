from installation.Linux.create_directories import create_directories
from installation.Linux.create_logging_files import create_logging_files
from installation.Linux.create_storage_files import create_storage_files
from installation.Linux.create_modules import install_modules
from installation.Linux.create_bin import create_bin

def main():
    create_directories()
    create_logging_files()
    create_storage_files()
    install_modules()
    create_bin()

