import socket

# ip da máquina vizinha
# HOST = '10.0.4.178'
HOST = '127.0.0.1'
PORT = 5010

servidor = (HOST, PORT)

print('=== Cliente ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def menu():
    print("""\nMenu:
      1 - Mostrar conteúdo do diretório
      2 - Criar diretório
      3 - Excluir diretório
      4 - Mostrar arquivo\n""")


def trata_opcoes(opcao_digitada):
    # 1 /tmp
    valores = opcao_digitada.split()
    opcao = valores[0]
    caminho = valores[1]

    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt

    msg = ''

    # Realiza a ação correspondente à opção do usuário
    # Mostra o conteúdo do diretório atual
    if opcao == "1":
        msg = 'LERDIR:' + caminho

    # Cria um novo diretório
    elif opcao == "2":
        msg = 'CRIARDIR:' + caminho

    # Exclui um diretório
    elif opcao == "3":
        msg = 'EXCLUIRDIR:' + caminho

    # Mostra o conteúdo de um arquivo
    elif opcao == "4":
        msg = 'MOSTRAR:' + caminho

    return msg


while True:
    menu()
    opcao = input('')
    msg = trata_opcoes(opcao)
    udp.sendto(msg.encode(encoding="utf-8"), servidor)
    resposta_servidor, s = udp.recvfrom(1024)
    print(resposta_servidor.decode(encoding='utf-8', errors='backslashreplace'))
