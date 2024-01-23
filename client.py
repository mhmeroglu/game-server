import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8888))

    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print(data)

        if "Congratulations" in data or "Sorry" in data:
            break 
        else:
            response = input("Your answer: ").strip()
            client.send(response.encode())

        if not response: 
            print("Data didn’t come!!!")
            break

    client.close()

if __name__ == '__main__':
    main()
