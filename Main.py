import pexpect


def main():
    # Open an ssh connection to the remote machine
    ssh = pexpect.spawn("ssh root@remote_machine_ip")

    # Wait for the password prompt and send the password
    ssh.expect("Password:")
    ssh.sendline("your_password")

    # Wait for the command prompt and run the ls command
    ssh.expect("#")
    ssh.sendline("ls")

    # Save the output to a file
    with open("output.txt", "w") as f:
        f.write(ssh.before.decode("utf-8"))


if __name__ == "__main__":
    main()
