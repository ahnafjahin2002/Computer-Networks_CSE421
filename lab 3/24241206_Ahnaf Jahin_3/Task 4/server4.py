import socket

port = 5050

data = 16
format = "utf-8"
disconnected_msg = "End"

hostname = socket.gethostname()

host_addr = socket.gethostbyname(hostname)

server_socket_address = (host_addr, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)

server.listen()

print("Our server is listening now")

while True:
    conn, addr = server.accept()
    print("Connected to", addr)
    connected = True

    while connected:
        initial = conn.recv(data).decode(format)
        print("Length of the msg to be sent", initial)

        if initial:
            msg_length = int(initial)
            msg = conn.recv(msg_length).decode(format)

            if msg == disconnected_msg:
                print("Terminating connection with", addr)
                conn.send("Nice to meet you".encode(format))
                connected = False

            else:
                hours = int(msg)

                if hours <= 40:
                    salary = hours * 200
                else:
                    salary = 8000 + (hours - 40) * 300

                conn.send(f"Salary is Tk {salary}".encode(format))

    conn.close()
    print("Connection closed with", addr)