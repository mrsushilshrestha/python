import winrm

# Target machine details
hostname = "http://192.168.1.65:5985/wsman"  # Target IP and port for WinRM
username = "admin"  # Administrator username (replace with the actual username)
password = "password"  # Administrator password (replace with the actual password)

# Create a session with the remote machine
session = winrm.Session(hostname, auth=(username, password))

# Command to shut down the target machine
shutdown_command = "shutdown /s /f /t 0"  # Force shutdown immediately

# Execute the shutdown command
result = session.run_cmd(shutdown_command)

# Print the result
print(result.std_out.decode())  # Output from the remote machine
print(result.std_err.decode())  # Any errors (if there are any)
