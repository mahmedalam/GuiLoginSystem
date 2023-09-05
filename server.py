import sqlite3
import socket
import rsa
import hashlib

with open("private.pem", "rb") as f:
    privateKey = rsa.PrivateKey.load_pkcs1(f.read(), "PEM")

with open("public.pem", "rb") as f:
    publicKey = rsa.PublicKey.load_pkcs1(f.read(), "PEM")

db = sqlite3.connect("database.db")
cursor = db.cursor()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()


def login(username, password):
    username = rsa.decrypt(username, privateKey).decode()
    password = hashlib.sha256(rsa.decrypt(password, privateKey)).hexdigest()

    cursor.execute("SELECT * FROM Accounts WHERE username = ? AND password = ?", (username, password))

    if cursor.fetchone():
        return "Login Successful".encode()
    else:
        return "Login Failed".encode()


# noinspection PyBroadException
def signup(firstName, lastName, email, username, password):
    firstName = rsa.decrypt(firstName, privateKey).decode()
    print(firstName)
    lastName = rsa.decrypt(lastName, privateKey).decode()
    print(lastName)
    email = rsa.decrypt(email, privateKey).decode()
    print(email)
    username = rsa.decrypt(username, privateKey).decode()
    print(username)
    password = hashlib.sha256(rsa.decrypt(password, privateKey)).hexdigest()
    print(password)

    try:
        cursor.execute("INSERT INTO Accounts VALUES(?,?,?,?,?,?)",
                       (None, firstName, lastName, email, username, password))
        msg = "Signup Successful"
    except:
        msg = "Username Already Exists!"

    db.commit()

    return msg.encode()


def handleConnection(client):
    command = client.recv(1024).decode()

    if command == "login":
        username = client.recv(1024)
        password = client.recv(1024)
        msg = login(username, password)
        client.send(msg)

    else:
        firstName = client.recv(1024)
        lastName = client.recv(1024)
        email = client.recv(1024)
        username = client.recv(1024)
        password = client.recv(1024)
        msg = signup(firstName, lastName, email, username, password)
        client.send(msg)


client, address = server.accept()
handleConnection(client)
