from audioop import add
from multiprocessing.connection import Client
import time

addr = ('localhost', 6000)
client_conn = Client(address=addr, authkey=b'rosalatortue')

client_conn.send("Rosa")
time.sleep(2)
client_conn.send("La")
time.sleep(2)
client_conn.send("Tortue")
time.sleep(2)
client_conn.send("Hautaine")
time.sleep(2)
client_conn.send("end")

client_conn.close()