import socket
import rsa


class Client:
    def client(self):
        with open("public.pem", "rb") as f:
            self.publicKey = rsa.PublicKey.load_pkcs1(f.read(), "PEM")

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("localhost", 9999))

    def login(self, username, password):
        self.client.send("login".encode())

        username = rsa.encrypt(username.encode(), self.publicKey)
        password = rsa.encrypt(password.encode(), self.publicKey)

        self.client.send(username)
        self.client.send(password)

        self.loginMsg = self.client.recv(1024)

    def signup(self, firstName, lastName, email, username, password):
        self.client.send("signup".encode())

        firstName = rsa.encrypt(firstName.encode(), self.publicKey)
        lastName = rsa.encrypt(lastName.encode(), self.publicKey)
        email = rsa.encrypt(email.encode(), self.publicKey)
        username = rsa.encrypt(username.encode(), self.publicKey)
        password = rsa.encrypt(password.encode(), self.publicKey)

        self.client.send(firstName)
        self.client.send(lastName)
        self.client.send(email)
        self.client.send(username)
        self.client.send(password)

        self.signupMsg = self.client.recv(1024)
