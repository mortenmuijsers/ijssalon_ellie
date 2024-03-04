import subprocess
import sys

def install_scikit_learn():
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'scikit-learn'], check=True)
        print("scikit-learn has been successfully installed.")
    except subprocess.CalledProcessError as e:
        print("Error installing scikit-learn:", e)

if __name__ == "__main__":
    install_scikit_learn()
