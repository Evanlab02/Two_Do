import platform

from installation.Linux.install_linux import main as start_linux_install

def main():
    my_system = get_platform_system()
    install_program(my_system)


def install_program(my_system):
    if my_system == "Linux":
        start_linux_install()


def get_platform_system():
    return platform.system()
