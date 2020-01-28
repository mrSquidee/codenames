import socket  
import numpy as np    
import json          

board = []
words = []

with open('words.txt', 'r') as wordFile:
   for line in wordFile:
      words.append(line[:-1])

words = np.ndarray.tolist(np.random.choice(words, 25))
teams = [1]*9 + [-1]*8 + [0]*7 + [2]
np.random.shuffle(teams)
board = dict(zip(words, teams))

print(board)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        boardSend = bytes(str(words), 'UTF-8')
        conn.sendall(boardSend)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


