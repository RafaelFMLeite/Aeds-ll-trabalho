import tkinter as tk  # criar a interface gráfica.

# Importa funções de outros módulos que criam interfaces específicas para diferentes funcionalidades.
from interfaces.busca_interface import buscar_evento_interface
from interfaces.evento_interface import criar_evento_interface, adicionar_itens_evento_interface
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

    # loop
    root.mainloop()
