import os
import shutil
import socket
from pathlib import Path

# ip da máquina que usei na sala de aula
# HOST = '10.0.4.72'
HOST = '127.0.0.1'
PORT = 5010

print('=== Servidor ===\n')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)


def trata_opcoes(msg):
    # 1 /tmp
    valores = msg.split(sep=':')
    operacao = valores[0]
    caminho = valores[1]

    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt

    folder = Path("./marcelo_folder/")

    # Cria um arquivo numa determinada pasta
    arquivo = folder / "arquivo.txt"

    msg = ''

    # Realiza a ação correspondente à opção do usuário
    # Exibe o conteúdo do diretório atual
    if operacao == "LERDIR":
        caminho = "./marcelo_folder"

        # Lista os arquivos da pasta e exibe os conteúdos existentes
        arquivos = os.listdir(caminho)
        conteudo = 'Conteúdo(s) existente(s) no diretório:\n '
        for palavra in arquivos:
            conteudo += "".join(palavra + ' ')

        udp.sendto(conteudo.encode(), cliente)

        print('\nLERDIR:' + caminho)

    # Cria um novo diretório, um arquivo e insere um texto dentro do mesmo
    elif operacao == "CRIARDIR":
        folder.mkdir()
        arquivo.touch()
        arquivo.write_text("S.O: Prática - Sockets", encoding="utf-8")
        print('CRIARDIR:' + caminho)

    # Exclui um diretório e seus arquivos, caso existam
    elif operacao == "EXCLUIRDIR":
        shutil.rmtree(folder)
        print('EXCLUIRDIR:' + caminho)

    # Exibe o conteúdo de um determinado arquivo
    elif operacao == "MOSTRAR":
        with open(f"{arquivo}", "r", encoding="utf-8") as file:
            conteudo = "Conteúdo do arquivo:\n" + file.read()
            udp.sendto(conteudo.encode(), cliente)
        print('MOSTRAR:' + caminho)

    return msg


while True:
    msg, cliente = udp.recvfrom(1024)
    trata_opcoes(msg.decode())
    print('Recebi de', cliente, 'a mensagem', msg.decode(encoding="utf-8"))

    resposta = 'Mensagem recebida com sucesso!'
    udp.sendto(resposta.encode(), cliente)
    print('Resposta enviada!\n')
