import subprocess
import time
import sys
import itertools
import random
import winsound  # Only works on Windows
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

# List of packages to install
packages = [
    "Flask", "discord", "packaging", "requests", "colorama", "inputimeout",
    "init", "Fore", "Style", "fade", "whois"
]

# Spinning animation for waiting moments
spinner = itertools.cycle(['|', '/', '-', '\\'])

# Function to play a sound (beep) on package installation
def play_sound():
    frequency = 1000  # Set Frequency To 1000 Hertz
    duration = 200    # Set Duration To 200 ms == 0.2 second
    winsound.Beep(frequency, duration)

# Function to display a simple progress bar
def progress_bar(package_name, duration=3):
    bar_length = 30

    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "#" * i + "-" * (bar_length - i)
        sys.stdout.write(f"\rInstalling {Fore.GREEN}{package_name}{Fore.RESET}: [{bar}] {percent}% {next(spinner)}")
        sys.stdout.flush()
        time.sleep(duration / bar_length)

    play_sound()  # Play sound when installation is complete
    print()  # Move to the next line after progress bar completes

# Function to install a package quietly
def install_package(package_name):
    try:
        progress_bar(package_name)

        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print(Fore.LIGHTBLACK_EX + f"{package_name} installed successfully!")
        else:
            print(Fore.RED + f"Failed to install {package_name}")

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

# Display a simple title
def display_title():
    print(Fore.LIGHTCYAN_EX + "Installing Python Packages")
    time.sleep(1)

# Main script to install all packages
if __name__ == "__main__":
    display_title()

    for package in packages:
        install_package(package)

    print(Fore.GREEN + "All packages installed successfully!")
    play_sound()
