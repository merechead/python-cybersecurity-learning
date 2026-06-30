import socket
import getpass
import platform
import os


def get_host_information():
    hostname = socket.gethostname()
    current_user = getpass.getuser()
    operating_system = platform.system()
    os_version = platform.platform()
    machine = platform.machine()
    processor = platform.processor()
    python_version = platform.python_version()
    current_dir = os.getcwd()
    ip_address = socket.gethostbyname(hostname)

    host_info = {
        "hostname": hostname,
        "current_user": current_user,
        "operating_system": operating_system,
        "os_version": os_version,
        "machine": machine,
        "processor": processor,
        "python_version": python_version,
        "current_dir": current_dir,
        "ip_address": ip_address,
    }

    return host_info


host_info = get_host_information()
print('''
================================
      Host Information Tool
================================
''')
print("Host Name: " + host_info["hostname"])
print("Current User: " + host_info["current_user"])
print("Operating System: " + host_info["operating_system"])
print("OS Version: " + host_info["os_version"])
print("Machine: " + host_info["machine"])
print("Processor: " + host_info["processor"])
print("Python Version: " + host_info["python_version"])
print("Current Directory: " + host_info["current_dir"])
print("IP Address: " + host_info["ip_address"])
