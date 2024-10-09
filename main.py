# main.py

from arvore_b import BTree
from evento import Evento

def carregar_eventos(nome_arquivo):
    eventos = []
    try:
        with open(nome_arquivo, 'r') as file:
            for linha in file:
                partes = linha.strip().split(',')
                if len(partes) != 4:
                    continue  # Ignora linhas invalidas
                evento_id, tipo, data, cliente = partes
                try:
                    evento_id = int(evento_id)
                except ValueError:
                    continue  # Ignora IDs que nao sao inteiros
                evento = Evento(evento_id, tipo, data, cliente)
                eventos.append(evento)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' nao encontrado.")
    return eventos

def main():
    grau = 3  # Grau minimo da Arvore B
    btree = BTree(grau)
    nome_arquivo = "eventos.txt"
    eventos = carregar_eventos(nome_arquivo)
    print(f"{len(eventos)} eventos carregados do arquivo '{nome_arquivo}'.")

    # Inserir os eventos carregados na arvore
    for evento in eventos:
        btree.insert(evento)
    
    # Registrar a estrutura inicial da arvore
    btree.log("\nEstrutura Inicial da Arvore B:")
    btree.print_tree(btree.root)

    while True:
        print("\nEscolha uma operacao:")
        print("1. Inserir Evento")
        print("2. Buscar Evento")
        print("3. Remover Evento")
        print("4. Visualizar Arvore")
        print("5. Sair")
        escolha = input("Digite o numero da operacao desejada: ")

        if escolha == '1':
            try:
                evento_id = int(input("Digite o ID do Evento: "))
                tipo = input("Digite o Tipo do Evento (Aniversario, Casamento, etc.): ")
                data = input("Digite a Data do Evento (DD/MM/AAAA): ")
                cliente = input("Digite o Nome do Cliente: ")
                evento = Evento(evento_id, tipo, data, cliente)
                btree.insert(evento)
                btree.log(f"Evento ID {evento_id} inserido com sucesso.")
                btree.log("Estrutura da Arvore B apos insercao:")
                btree.print_tree(btree.root)
            except ValueError:
                print("ID do Evento deve ser um numero inteiro.")
        elif escolha == '2':
            try:
                evento_id = int(input("Digite o ID do Evento a ser buscado: "))
                resultado = btree.search(btree.root, evento_id)
                if resultado:
                    print(f"Evento encontrado: {resultado}")
                else:
                    print(f"Evento ID {evento_id} nao encontrado.")
                btree.log("Estrutura da Arvore B apos busca:")
                btree.print_tree(btree.root)
            except ValueError:
                print("ID do Evento deve ser um numero inteiro.")
        elif escolha == '3':
            try:
                evento_id = int(input("Digite o ID do Evento a ser removido: "))
                btree.remove(evento_id)
                btree.log(f"Evento ID {evento_id} removido, se existia.")
                btree.log("Estrutura da Arvore B apos remocao:")
                btree.print_tree(btree.root)
            except ValueError:
                print("ID do Evento deve ser um numero inteiro.")
        elif escolha == '4':
            btree.log("Visualizando a Estrutura da Arvore B:")
            btree.print_tree(btree.root)
        elif escolha == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Escolha invalida. Tente novamente.")

if __name__ == "__main__":
    main()
