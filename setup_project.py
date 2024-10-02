import os
import subprocess
import sys

# Step 1: Create a virtual environment
def create_virtualenv(venv_name):
    try:
        print(f"Creating virtual environment '{venv_name}'...")
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
        print(f"Virtual environment '{venv_name}' created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during virtualenv creation: {e}")
        sys.exit(1)

# Step 2: Activate the virtual environment
def activate_virtualenv(venv_name):
    venv_activate = None
    if os.name == "nt":  # Windows
        venv_activate = os.path.join(venv_name, "Scripts", "activate")
    else:  # macOS/Linux
        venv_activate = os.path.join(venv_name, "bin", "activate")
    
    print(f"To activate the virtual environment, run: source {venv_activate}")

# Step 3: Install langflow or requirements.txt
def install_packages(venv_name, requirements_file=None):
    try:
        pip_path = os.path.join(venv_name, "bin", "pip") if os.name != "nt" else os.path.join(venv_name, "Scripts", "pip")
        
        # Install langflow or requirements.txt
        if requirements_file:
            print(f"Installing packages from {requirements_file}...")
            subprocess.run([pip_path, "install", "-r", requirements_file], check=True)
        else:
            print("Installing langflow...")
            subprocess.run([pip_path, "install", "langflow"], check=True)

        print("Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during package installation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Virtual environment name
    venv_name = "my_venv"

    # Create virtual environment
    create_virtualenv(venv_name)

    # Activate virtual environment (manual step)
    activate_virtualenv(venv_name)

    # Install either langflow or a requirements.txt
    # To install from a requirements.txt, pass the path to the file as an argument
    requirements_file = "requirements.txt"  # Replace with the path to your requirements file, or set to None to install langflow
    install_packages(venv_name, requirements_file)
