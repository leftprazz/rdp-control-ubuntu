#!/usr/bin/env python3
import subprocess

def disable_rdp_and_gui():
    # Stop XRDP service
    subprocess.run(["sudo", "systemctl", "stop", "xrdp"])

    # Stop GUI (GDM3) service
    subprocess.run(["sudo", "systemctl", "stop", "gdm3"])

def enable_rdp_and_gui():
    # Start XRDP service
    subprocess.run(["sudo", "systemctl", "start", "xrdp"])

    # Start GUI (GDM3) service
    subprocess.run(["sudo", "systemctl", "start", "gdm3"])

if __name__ == "__main__":
    print("1. Disable RDP and GUI")
    print("2. Enable RDP and GUI")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        disable_rdp_and_gui()
        print("RDP and GUI have been disabled.")
    elif choice == "2":
        enable_rdp_and_gui()
        print("RDP and GUI have been enabled.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
