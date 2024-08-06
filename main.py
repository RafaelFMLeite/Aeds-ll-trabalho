import random
import string
import os

from entidades.usuario import Usuario
from entidades.evento import Evento
from entidades.convidado import Convidado
from entidades.comida import Comida
from entidades.bebida import Bebida

from operacoes.ordenacao import merge_sort
from operacoes.interacoes import adicionar_convidado_evento, listar_convidados_evento
from operacoes.persistencia import salvar_dados, carregar_dados
from operacoes.busca import busca_sequencial, busca_binaria

def gerar_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Definindo nomes dos arquivos para persistência
arquivo_usuarios = 'dados/usuarios.pkl'
arquivo_eventos = 'dados/eventos.pkl'
arquivo_convidados = 'dados/convidados.pkl'
arquivo_comidas = 'dados/comidas.pkl'
arquivo_bebidas = 'dados/bebidas.pkl'

# Criando diretório de dados se não existir
os.makedirs('dados', exist_ok=True)

# Carregando bases de dados se existirem, senão gerando novas
usuarios = carregar_dados(arquivo_usuarios) or [Usuario(gerar_id(), f"Usuario_{i}") for i in range(10)]
eventos = carregar_dados(arquivo_eventos) or [Evento(gerar_id(), f"Evento_{i}", random.choice(usuarios).id_usuario) for i in range(5)]
convidados = carregar_dados(arquivo_convidados) or [Convidado(gerar_id(), f"Convidado_{i}", random.choice([True, False])) for i in range(20)]
comidas = carregar_dados(arquivo_comidas) or [Comida(gerar_id(), f"Comida_{i}") for i in range(10)]
bebidas = carregar_dados(arquivo_bebidas) or [Bebida(gerar_id(), f"Bebida_{i}") for i in range(10)]

# Ordenando a base de dados de usuários pelo nome
merge_sort(usuarios, 'nome')

# Exemplo de uso
evento_id = eventos[0].id_evento
convidado_id = convidados[0].id_convidado

adicionar_convidado_evento(eventos, convidados, evento_id, convidado_id)
print(listar_convidados_evento(eventos, evento_id))

# Exemplo de busca sequencial e binária
# Buscando um usuário pelo nome
nome_usuario_procurado = "Usuario_5"
usuario_encontrado_sequencial = busca_sequencial(usuarios, nome_usuario_procurado, 'nome')
usuario_encontrado_binaria = busca_binaria(usuarios, nome_usuario_procurado, 'nome')

print(f"Busca sequencial - Usuário encontrado: {usuario_encontrado_sequencial.nome if usuario_encontrado_sequencial else 'Não encontrado'}")
print(f"Busca binária - Usuário encontrado: {usuario_encontrado_binaria.nome if usuario_encontrado_binaria else 'Não encontrado'}")

# Buscando um usuário que não existe
nome_usuario_inexistente = "Usuario_Inexistente"
usuario_inexistente_sequencial = busca_sequencial(usuarios, nome_usuario_inexistente, 'nome')
usuario_inexistente_binaria = busca_binaria(usuarios, nome_usuario_inexistente, 'nome')

print(f"Busca sequencial - Usuário não encontrado: {'Usuário encontrado' if usuario_inexistente_sequencial else 'Não encontrado'}")
print(f"Busca binária - Usuário não encontrado: {'Usuário encontrado' if usuario_inexistente_binaria else 'Não encontrado'}")

# Buscando um evento pelo nome
nome_evento_procurado = "Evento_2"
evento_encontrado_sequencial = busca_sequencial(eventos, nome_evento_procurado, 'nome')
evento_encontrado_binaria = busca_binaria(eventos, nome_evento_procurado, 'nome')

print(f"Busca sequencial - Evento encontrado: {evento_encontrado_sequencial.nome if evento_encontrado_sequencial else 'Não encontrado'}")
print(f"Busca binária - Evento encontrado: {evento_encontrado_binaria.nome if evento_encontrado_binaria else 'Não encontrado'}")

# Buscando um convidado pelo nome
nome_convidado_procurado = "Convidado_10"
convidado_encontrado_sequencial = busca_sequencial(convidados, nome_convidado_procurado, 'nome')
convidado_encontrado_binaria = busca_binaria(convidados, nome_convidado_procurado, 'nome')

print(f"Busca sequencial - Convidado encontrado: {convidado_encontrado_sequencial.nome if convidado_encontrado_sequencial else 'Não encontrado'}")
print(f"Busca binária - Convidado encontrado: {convidado_encontrado_binaria.nome if convidado_encontrado_binaria else 'Não encontrado'}")

# Salvando bases de dados
salvar_dados(usuarios, arquivo_usuarios)
salvar_dados(eventos, arquivo_eventos)
salvar_dados(convidados, arquivo_convidados)
salvar_dados(comidas, arquivo_comidas)
salvar_dados(bebidas, arquivo_bebidas)