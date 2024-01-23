import socket

def handle_request(client_connection):
    
    questions = [
        "Which planet is closest to the Sun in our Solar System?\nA) Mars\nB) Venus\nC) Jupiter\nD) Uranus\n",
        "The highest mountain on Earth, located in the Himalayas, is how many meters tall?\nA) 7,201 meters\nB) 8,848 meters\nC) 6,962 meters\nD) 9,356 meters\n",
        "Which author is known for classic works such as 'Les Misérables' and 'The Hunchback of Notre-Dame'?\nA) Charles Dickens\nB) Jane Austen\nC) Victor Hugo\nD) Fyodor Dostoyevsky\n",
    ]
    
    correct_answers = ['B', 'B', 'C']
    
    score = 0

    for i, question in enumerate(questions):
        client_connection.send(question.encode())
        response = client_connection.recv(1024).decode().strip().upper()

        if not response:
            return  
        
        elif response == correct_answers[i]:
            score += 1

        else:
            client_connection.send("Sorry!!! You lost the competition".encode())
            return 
    if score == len(questions):
        client_connection.send("Congratulations!! You're a millionaire now".encode())
    else:
        client_connection.send("Sorry!!! You lost the competition".encode())

def serve_forever():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen(5)
    
    print("Server is listening on port 8888...")
    
    while True:
        client_connection, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        handle_request(client_connection)
        client_connection.close()

if __name__ == '__main__':
    serve_forever()
