import pygame
import socket
import _thread
from player import Player


ThreadCount = 0
def run_host():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Multiplayer Test")

    hostPlayer = Player(15, 15, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
        
        pygame.time.Clock().tick(60)

        screen.fill((0, 0, 0))

        hostPlayer.move_player()
        hostPlayer.draw_player()
        pygame.display.flip()

def disconnect_client():
    global ThreadCount
    ThreadCount -= 1

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        try:
            data = connection.recv(1024)
            response = 'Server message: ' + data.decode('utf-8')
            if not data:
                disconnect_client()
                break
            connection.sendall(str.encode(response))
        except Exception as e:
            disconnect_client()
            print(e)
            print("Player disconnected")
            break
    connection.close()

def run_server():
    global ThreadCount
    # Begin by creating the server, then loading the game
    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    port = 3000

    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening..')
    ServerSideSocket.listen(5) # Start listening for clients, then run the game for the host
    _thread.start_new_thread(run_host, ())
    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        _thread.start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()



if __name__ == "__main__":
    run_server()