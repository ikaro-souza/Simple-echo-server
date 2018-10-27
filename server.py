import socket
from os import popen

ENCODING = 'utf-8'  # Define a codificação padrão do programa
HOST = 'localhost'  # Define que o servidor está na máquina onde o programa é rodado
PORT = 8800         # Define a porta que será usada
BUFFER_SIZE = 1024  # Define o tamanho máximo de dados que o socket irá receber de uma vez


# Cria um novo socket
def new_socket():
    # AF_INET informa que o socket usará IP versão 4
    # SOCK_STREAM que o socket usará o protocolo TCP
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def run(command):
    # Executa o comando e guarda a string que contém o resultado da execução
    output = popen(command).read()

    if output == '':
        output = 'Este comando é inválido.'

    # Retorna o resultado da execução
    return output


def main():
    server = new_socket()
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        print('Aguardando conexão com cliente.')
        print('-------------------------------')

        # Guarda o socket da conexão entre servidor e cliente e o endereço do cliente
        connection, address = server.accept()

        print('Conectado à', address)
        print('-------------------------------')
        print('Esperando mensagem do cliente.')
        print('-------------------------------')

        # Recebe o comando, decodificando em utf-8
        command = connection.recv(BUFFER_SIZE).decode(ENCODING)

        print('Executando comando.')
        print('-------------------------------')
        # Executa o comando e guarda o resultado na variavel output
        output = run(command)

        if output == 'Este comando é inválido.':
            print('Comando inválido.')
        else:
            print('Comando executado com sucesso.')

        print('-------------------------------')
        # Envia o resultado da execução do comando, codificando em utf-8
        connection.send(output.encode(ENCODING))
        # Encerra a conexão
        connection.close()


if __name__ == '__main__':
    main()
