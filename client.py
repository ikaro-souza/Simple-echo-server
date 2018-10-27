import socket
from tkinter import *

ENCODING = 'utf-8'
HOST = 'localhost'
PORT = 8800
BUFFER_SIZE = 1024


class ClientGUI:
    def __init__(self, root=None):
        if root is None:
            self.root = Tk()
        else:
            self.root = root

        # Comando que o cliente digitou
        self.command = ''
        # Resultado da execução do comando
        self.command_output = ''

        # Frame onde ficará o formulário
        self.form_frame = Frame(self.root, height=80)
        # Frame onde ficará o resultado da execução do comando
        self.output_frame = Frame(self.root, height=100, bg='black')

        # Label do comando
        self.command_label = Label(self.form_frame, text='Comando')
        # Entry do comando
        self.command_entry = Entry(self.form_frame, width=30)
        # faz a entry executar a função run_command quando a tecla Enter for pressionada
        self.command_entry.bind('<Return>', self.run_command)
        # Button do comando, que executa a função run_commando quando pressionado
        self.command_button = Button(self.form_frame, text='Enviar', command=self.run_command)
        # Label que exibe o valor de command_output
        self.output_label = Label(self.output_frame, justify=LEFT, width=30, bg='black', fg='white')

    # Exibe a interface do programa
    def show(self):
        # Define o tamanho da tela em 500 pixels de largura e 200 de altura
        self.root.geometry('500x300')
        # Define o nome da tela
        self.root.title('Cliente')
        # Permite que apenas a altura da tela seja reajustável
        self.root.resizable(False, True)
        # Executa a função pack_widgets
        self.pack_widgets()
        # Executa o mainloop
        self.root.mainloop()

    # Posiciona todos os widgets na interface
    def pack_widgets(self):
        self.form_frame.pack(side=TOP, fill=BOTH)
        self.output_frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        self.command_label.grid(row=0, column=0, padx=33, pady=5, sticky=W)
        self.command_entry.grid(row=0, column=1, padx=33, pady=5)
        self.command_button.grid(row=0, column=2, padx=33, pady=5, sticky=E)
        self.output_label.pack(padx=5, pady=5, fill=BOTH)

    # Executa o comando digitado pelo cliente e exibe o resultado da execução
    def run_command(self, event=None):
        # Cria o socket do cliente
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta o socket
        client_socket.connect((HOST, PORT))
        # Guarda o texto que está na entry e o codifica em utf-8
        self.command = self.command_entry.get().encode(ENCODING)
        # Envia o comando para o servidor
        client_socket.send(self.command)
        # Recebe o retorno do comando executado, decondando em utf-8
        self.command_output = client_socket.recv(BUFFER_SIZE).decode(ENCODING)
        # Muda o texto na label que mostra o resultado da execução do comando
        self.output_label.configure(text=self.command_output)
        # Apaga o texto na entry
        self.command_entry.delete(0, 'end')
        # Fecha o socket
        client_socket.close()


if __name__ == '__main__':
    # Cria a inteface do cliente
    client_interface = ClientGUI()
    # Exibe a interface do cliente
    client_interface.show()
