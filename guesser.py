import socket
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
board = data.decode('UTF-8')
print(board)

win = 0

while(win == 0):
    data = s.recv(1024)
    data.decode('UTF-8')

    if('win' in data):
        win = data[0]
        print(data)
    if('turn' in data):
        guess(data[0], data[8:-3], data[-1])

def guess(team, hint, num):
    guess = 0
    print(data)
    if(team == 1):
        guess = aiCode(hint)
    elif(team == -1):
        guess = input('\n> ')

    s.sendall(bytes(guess, 'UTF-8'))

    goAgain = s.recv(1024)
    if(goAgain and num >= 0):
        guess(team, hint, num-1)


def aiCode(hint):
    return 0