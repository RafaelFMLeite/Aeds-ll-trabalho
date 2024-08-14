import tkinter as tk
from tkinter import ttk, messagebox
from operacoes.busca import busca_sequencial, busca_binaria
from operacoes.persistencia import carregar_dados

def buscar_evento_interface():
    def buscar_evento():
        metodo_busca = busca_var.get()
        nome_evento = nome_entry.get()
        eventos = carregar_dados('dados/eventos.pkl')

        evento_encontrado = None
        if metodo_busca == "Sequencial":
            evento_encontrado = busca_sequencial(eventos, 'nome', nome_evento)
        elif metodo_busca == "Binária":
            eventos_ordenados = sorted(eventos, key=lambda e: e.nome)
            evento_encontrado = busca_binaria(eventos_ordenados, 'nome', nome_evento)

        if evento_encontrado:
            messagebox.showinfo("Resultado", f"Evento encontrado: {evento_encontrado.nome}")
        else:
            messagebox.showerror("Erro", "Evento não encontrado")

    root = tk.Tk()
    root.title("Buscar Evento")

    tk.Label(root, text="Nome do Evento:").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack()

    tk.Label(root, text="Método de Busca:").pack()
    busca_var = tk.StringVar(value="Sequencial")
    ttk.Radiobutton(root, text="Sequencial", variable=busca_var, value="Sequencial").pack()
    ttk.Radiobutton(root, text="Binária", variable=busca_var, value="Binária").pack()

    tk.Button(root, text="Buscar", command=buscar_evento).pack(pady=10)

    root.mainloop()
