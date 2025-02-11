#Dev by Vitor Nunciatelli - nunciatelli54@gmail.com - 2023
import socket

# Configuração do servidor
host = 'localhost'
port = 12345

# Inicialização do servidor TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Aguardando conexão em {host}:{port}")
client_socket, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

# Recebendo dados do dispositivo IoT
data = client_socket.recv(1024)
print(f"Dados recebidos: {data.decode()}")

# Fechando a conexão
client_socket.close()
server_socket.close()
