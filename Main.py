import paramiko

# Connect to the remote machine
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.113', username='phoenix', password='1122')

# Run the command
stdin, stdout, stderr = ssh.exec_command('ls -l')

# Capture the output
output = stdout.read().decode()
print(output)
# Save the output to a file
with open('output.txt', 'w') as file:
    file.write(output)

# Close the connection
ssh.close()
