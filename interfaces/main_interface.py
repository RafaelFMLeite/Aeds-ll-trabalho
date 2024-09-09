import tkinter as tk  # criar a interface gráfica.

# Importa funções de outros módulos que criam interfaces específicas para diferentes funcionalidades.
from interfaces.busca_interface import buscar_evento_interface
from interfaces.evento_interface import (
    gerar_particoes_selecao_substituicao_interface, 
    intercalar_particoes_arvore_vencedores_interface,
    criar_evento_interface,
    adicionar_itens_evento_interface
)
from interfaces.ordenar_dados_interface import ordenar_dados_interface


def iniciar_interface():
    # cria a janela principal da interface gráfica.
    root = tk.Tk()
    root.title("Gerenciador de Eventos")

    # cria botões na janela principal
    tk.Button(root, text="Criar Evento", command=criar_evento_interface).pack(pady=10)
    tk.Button(root, text="Buscar Evento", command=buscar_evento_interface).pack(pady=10)
    tk.Button(root, text="Adicionar Itens ao Evento", command=adicionar_itens_evento_interface).pack(pady=10)
    tk.Button(root, text="Ordenar Dados", command=ordenar_dados_interface).pack(pady=10)
    tk.Button(root, text="Gerar Partições (Seleção por Substituição)", command=gerar_particoes_selecao_substituicao_interface).pack(pady=10)
    tk.Button(root, text="Intercalar Partições (Árvore de Vencedores)", command=intercalar_particoes_arvore_vencedores_interface).pack(pady=10)

    # loop
    root.mainloop()
