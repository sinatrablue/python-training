from audioop import add
from multiprocessing.connection import Listener

addr = ('localhost', 6000)
listener = Listener(address=addr, authkey=b'rosalatortue')
conn = listener.accept()

print("Connection accepted from ", listener.last_accepted)

while True:
    msg = conn.recv()
    if msg == 'end':
        conn.close()
        break
    else :
        print("Received : ", msg)
listener.close()