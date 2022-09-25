from multiprocessing.connection import Client
import time
from equip import Equip

addr = ('localhost', 6000)
client_conn = Client(address=addr, authkey=b'rosalatortue')

my_team = Equip("Fansworth", "Emmy", 20)

client_conn.send("Rosa")
time.sleep(2)
client_conn.send("La")
time.sleep(2)
client_conn.send("Tortue")
time.sleep(2)
client_conn.send("Hautaine")
time.sleep(2)
client_conn.send(my_team.mb1)
time.sleep(2)
client_conn.send(my_team.totEff)
time.sleep(2)
client_conn.send("end")

client_conn.close()