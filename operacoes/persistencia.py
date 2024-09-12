import pickle  
import random  
import string  
from entidades.usuario import Usuario
from entidades.convidado import Convidado
from entidades.comida import Comida
from entidades.bebida import Bebida
from entidades.evento import Evento

def salvar_dados(obj, filename):
    with open(filename, 'wb') as f:  # Abre o arquivo no modo de escrita binária
        pickle.dump(obj, f)  # Usa pickle para salvar o objeto no arquivo

# Função para carregar dados de um arquivo usando pickle
def carregar_dados(filename):
    try:
        with open(filename, 'rb') as f:  # Abre o arquivo no modo de leitura binária
            return pickle.load(f)  # Carrega e retorna o objeto salvo
    except FileNotFoundError:  # Se o arquivo não for encontrado
        return []  # Retorna uma lista vazia

# Função para gerar um ID aleatório
def gerar_id():
<<<<<<< HEAD
    # ID é composto de 6 caracteres alfanuméricos, seguido de um sufixo numérico
    sufixo = f"_{random.randint(1, 999):03d}"
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + sufixo
=======
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))  # Gera um ID com 6 caracteres aleatórios
>>>>>>> development

# Função para gerar nomes de entidades, como "Usuario_a", "Usuario_b", etc.
def gerar_nome_entidade(entidade, index):
    letras = string.ascii_lowercase  # Usa letras minúsculas para gerar os nomes
    if index < len(letras):  # Se o índice estiver dentro do alfabeto
        return f"{entidade}_{letras[index]}"  # Retorna o nome da entidade com uma letra
    else:
        index -= len(letras)  # Ajusta o índice para nomes com duas letras
        primeiro_letra = letras[index // len(letras)]
        segunda_letra = letras[index % len(letras)]
        return f"{entidade}_{primeiro_letra}{segunda_letra}"  # Retorna o nome da entidade com duas letras

# Função para gerar dados de usuários, convidados, comidas, bebidas e eventos
def gerar_dados():
<<<<<<< HEAD
    usuarios = [Usuario(gerar_id(), f"Usuario_{gerar_id()}") for i in range(80)]
    convidados = [Convidado(gerar_id(), f"Convidado_{gerar_id()}", random.choice([True, False])) for i in range(80)]
    comidas = [Comida(gerar_id(), f"Comida_{gerar_id()}") for i in range(80)]
    bebidas = [Bebida(gerar_id(), f"Bebida_{gerar_id()}") for i in range(80)]
=======
    # Carrega dados existentes
    usuarios = carregar_dados('dados/usuarios.pkl')
    convidados = carregar_dados('dados/convidados.pkl')
    comidas = carregar_dados('dados/comidas.pkl')
    bebidas = carregar_dados('dados/bebidas.pkl')
    eventos = carregar_dados('dados/eventos.pkl')
>>>>>>> development

    # Se não houver usuários salvos, gera novos
    if not usuarios:
        usuarios = [Usuario(gerar_id(), gerar_nome_entidade("Usuario", i)) for i in range(80)]  # Gera 80 usuários
        random.shuffle(usuarios)  # Embaralha a lista de usuários
        salvar_dados(usuarios, 'dados/usuarios.pkl')  # Salva os usuários no arquivo

    # Se não houver convidados salvos, gera novos
    if not convidados:
        convidados = [Convidado(gerar_id(), gerar_nome_entidade("Convidado", i)) for i in range(80)]
        random.shuffle(convidados)  # Embaralha a lista de convidados
        salvar_dados(convidados, 'dados/convidados.pkl')  # Salva os convidados no arquivo

    # Se não houver comidas salvas, gera novas
    if not comidas:
        comidas = [Comida(gerar_id(), gerar_nome_entidade("Comida", i)) for i in range(80)]
        random.shuffle(comidas)  # Embaralha a lista de comidas
        salvar_dados(comidas, 'dados/comidas.pkl')  # Salva as comidas no arquivo

    # Se não houver bebidas salvas, gera novas
    if not bebidas:
        bebidas = [Bebida(gerar_id(), gerar_nome_entidade("Bebida", i)) for i in range(80)]
        random.shuffle(bebidas)  # Embaralha a lista de bebidas
        salvar_dados(bebidas, 'dados/bebidas.pkl')  # Salva as bebidas no arquivo

    # Se não houver eventos salvos, gera novos
    if not eventos:
        organizadores = [usuario.id_usuario for usuario in usuarios]  # Cria uma lista de IDs dos organizadores
        eventos = [Evento(gerar_id(), gerar_nome_entidade("Evento", i), random.choice(organizadores)) for i in range(80)]
        random.shuffle(eventos)  # Embaralha a lista de eventos
        salvar_dados(eventos, 'dados/eventos.pkl')  # Salva os eventos no arquivo
    else:
        # Embaralha eventos existentes
        eventos = carregar_dados('dados/eventos.pkl')  # Carrega os eventos do arquivo
        random.shuffle(eventos)  # Embaralha a lista de eventos
        salvar_dados(eventos, 'dados/eventos.pkl')  # Salva os eventos embaralhados
