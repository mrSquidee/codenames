import socket  
import numpy as np              

board = []

def generateGame():
   words = []

   with open('words.txt', 'r') as wordFile:
      for line in wordFile:
         words.append(line[:-1])
   
   board = np.random.choice(words, 25)

   teams = np.array([1]*9 + [-1]*8 + [0]*7 + [2])
   teams = {}
   for word in board:
      teams[word] = np.random.choice(teams, 1)
   
   
   print(board)
   print(teams)

s = socket.socket()          
port = 12345                
s.bind(('', port))         
print('socket binded to ' + str(port))
s.listen(5)      
  

generateGame()

while(True): 
  
   c, addr = s.accept()      
   print('Got connection from', addr)

   c.send('Thank you for connecting') 
  
   c.close() 


