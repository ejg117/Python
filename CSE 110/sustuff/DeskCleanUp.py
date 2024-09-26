import os
import subprocess
import psutil
import time

def open_all_executables():
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if file.endswith(".exe"):
                path = os.path.join(root, file)
                try:
                    subprocess.Popen(path)
                    print(f"Opened: {path}")
                except Exception as e:
                    print(f"Error opening {path}: {e}")

def close_all_executables():
    for proc in psutil.process_iter():
        try:
            if proc.name().endswith(".exe"):
                proc.kill()
                print(f"Closed: {proc.name()}")
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass

open_all_executables()
print("Waiting for 5 seconds before closing...")
time.sleep(1)  # Wait for 5 seconds
close_all_executables()