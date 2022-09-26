import socket   # simple socket this time

HOST, PORT = "localhost", 6666
data = "rosalatortue"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.connect((HOST, PORT))
    my_socket.sendall(bytes(data + "\n", "utf-8"))
    #data_rcv = str(my_socket.recv(1024), "utf-8")

print("Sent ::> {}".format(data))
#print("Received ::> {}".format(data_rcv))