# run.py
import os
import sys
import subprocess

def install_dependencies():
    print("Installing required Python packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_isha():
    print("Starting ISHA Assistant...")
    os.system("python isha.py")

if __name__ == "__main__":
    # Check if dependencies are installed
    try:
        import pyttsx3
    except ImportError:
        install_dependencies()
    run_isha()
