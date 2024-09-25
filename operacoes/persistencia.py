import os
import pickle
import random
from entidades.evento import Evento
from entidades.comida import Comida
from entidades.bebida import Bebida
from entidades.convidado import Convidado
from entidades.usuario import Usuario


def SalvarDados(obj, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'wb') as f:  
        pickle.dump(obj, f)

def CarregarDados(filename):
    try:
        with open(filename, 'rb') as f:  
            return pickle.load(f)  
    except FileNotFoundError:  
        return []

def SalvarDadosTxt(objetos, filename):
    """Função para salvar os dados de uma lista de objetos em um arquivo .txt"""
    os.makedirs(os.path.dirname(filename), exist_ok=True) 
    with open(f"{filename}.txt", 'w') as f:
        for obj in objetos:
            f.write(f"{str(obj)}\n")  

def AdicionandoDados(NumeroDeEntidades, Classe, filename):
    listaDeObjeto = []
    contain = set()

    for _ in range(NumeroDeEntidades):
        rand = random.randint(0, NumeroDeEntidades - 1)
        
        while rand in contain:
            rand = random.randint(0, NumeroDeEntidades - 1)
        
        contain.add(rand)
        # Instancia a classe correta
        objeto = Classe(rand, f"{Classe.__name__}{rand}")
        listaDeObjeto.append(objeto)
    
    # Salva os dados em arquivo pickle
    SalvarDados(listaDeObjeto, f"dados/{filename}.pkl")
    return listaDeObjeto
    
def InicializandoBase(NumeroDeEntidades):
    # Carregar dados previamente salvos, se existirem
    usuarios = CarregarDados("dados/usuarios.pkl")
    comidas = CarregarDados("dados/comidas.pkl")
    bebidas = CarregarDados("dados/bebidas.pkl")
    convidados = CarregarDados("dados/convidados.pkl")
    eventos = CarregarDados("dados/eventos.pkl")

    # Adiciona dados e salva em txt se necessário
    if not usuarios:
        usuarios = AdicionandoDados(NumeroDeEntidades, Usuario, "usuarios")
    SalvarDadosTxt(usuarios, "dados/usuarios")

    if not comidas:
        comidas = AdicionandoDados(NumeroDeEntidades, Comida, "comidas")
    SalvarDadosTxt(comidas, "dados/comidas")

    if not convidados:
        convidados = AdicionandoDados(NumeroDeEntidades, Convidado, "convidados")
    SalvarDadosTxt(convidados, "dados/convidados")
    
    if not bebidas:
        bebidas = AdicionandoDados(NumeroDeEntidades, Bebida, "bebidas")
    SalvarDadosTxt(bebidas, "dados/bebidas")
        
    if not eventos:
        listaDeEventos = []
        contain = set()
        
        for _ in range(NumeroDeEntidades):
            organizador = random.choice(usuarios) if usuarios else Usuario(0, "Usuario0")
            rand = random.randint(0, NumeroDeEntidades - 1)
           
            while rand in contain:
                 rand = random.randint(0, NumeroDeEntidades - 1)

            contain.add(rand)
            evento = Evento(rand, f"Evento{rand}", organizador.id_usuario)
            listaDeEventos.append(evento)

        SalvarDados(listaDeEventos, "dados/eventos.pkl")
        eventos = listaDeEventos
        
    # Salvar dados dos eventos em arquivo txt
    SalvarDadosTxt(eventos, "dados/eventos")
