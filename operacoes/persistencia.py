import pickle

def salvar_dados(objeto, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(objeto, arquivo)

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None
