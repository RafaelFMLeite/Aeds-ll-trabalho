import tkinter as tk
from tkinter import ttk, messagebox
from operacoes.busca import busca_sequencial, busca_binaria  
from operacoes.persistencia import carregar_dados

def buscar_evento_interface():
    def buscar_evento():
        metodo_busca = busca_var.get()  # obtém o método de busca selecionado.
        nome_evento = nome_entry.get()  # obtém o nome do evento inserido pelo usuário.
        eventos = carregar_dados('dados/eventos.pkl')  # carrega a lista de eventos do arquivo.

        evento_encontrado = None
        if metodo_busca == "Sequencial":
            evento_encontrado = busca_sequencial(eventos, 'nome', nome_evento)
        elif metodo_busca == "Binária":
            # eventos_ordenados = sorted(eventos, key=lambda e: e.nome)  # ordena eventos por nome.
            evento_encontrado = busca_binaria(eventos, 'nome', nome_evento)

        if evento_encontrado:
            # mensagem com os detalhes do evento encontrado.
            detalhes_evento = f"Evento encontrado: {evento_encontrado.nome}\n\n"

            if hasattr(evento_encontrado, 'comidas') and evento_encontrado.comidas:
                detalhes_evento += "Comidas:\n" + "\n".join([comida.nome for comida in evento_encontrado.comidas]) + "\n\n"
            if hasattr(evento_encontrado, 'bebidas') and evento_encontrado.bebidas:
                detalhes_evento += "Bebidas:\n" + "\n".join([bebida.nome for bebida in evento_encontrado.bebidas]) + "\n\n"
            if hasattr(evento_encontrado, 'convidados') and evento_encontrado.convidados:
                detalhes_evento += "Convidados:\n" + "\n".join([convidado.nome for convidado in evento_encontrado.convidados]) + "\n\n"

            messagebox.showinfo("Resultado", detalhes_evento)  # detalhes do evento.
        else:
            messagebox.showerror("Erro", "Evento não encontrado")

    root = tk.Tk()  
    root.title("Buscar Evento")

    tk.Label(root, text="Nome do Evento:").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack()

    tk.Label(root, text="Método de Busca:").pack()
    busca_var = tk.StringVar(value="Sequencial")  # variável para armazenar o método de busca selecionado.
    ttk.Radiobutton(root, text="Sequencial", variable=busca_var, value="Sequencial").pack()
    ttk.Radiobutton(root, text="Binária", variable=busca_var, value="Binária").pack()

    tk.Button(root, text="Buscar", command=buscar_evento).pack(pady=10)

    root.mainloop()
