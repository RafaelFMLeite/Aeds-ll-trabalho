import tkinter as tk
from tkinter import ttk, messagebox
from entidades.evento import Evento
from operacoes.persistencia import salvar_dados, carregar_dados, gerar_id
from operacoes.interacoes import adicionar_convidado_evento, adicionar_comida_evento, adicionar_bebida_evento

def criar_evento_interface():
    root = tk.Tk()
    root.title("Criar Evento")

    tk.Label(root, text="Nome do Evento:").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack()

    usuarios = carregar_dados('dados/usuarios.pkl')
    tk.Label(root, text="Organizador:").pack()
    organizador_combo = ttk.Combobox(root, values=[u.nome for u in usuarios])
    organizador_combo.pack()

    def salvar_evento():
        nome_evento = nome_entry.get()
        nome_organizador = organizador_combo.get()
        organizador = next((u for u in usuarios if u.nome == nome_organizador), None)
        
        if organizador:
            eventos = carregar_dados('dados/eventos.pkl')
            
            # Verificar se já existe um evento com o mesmo nome e organizador
            evento_existente = next((e for e in eventos if e.nome == nome_evento and e.organizador_id == organizador.id_usuario), None)
            
            if evento_existente:
                messagebox.showerror("Erro", "Um evento com esse nome e organizador já existe.")
            else:
                evento = Evento(gerar_id(), nome_evento, organizador.id_usuario)
                eventos.append(evento)
                salvar_dados(eventos, 'dados/eventos.pkl')
                messagebox.showinfo("Sucesso", "Evento criado com sucesso!")
        else:
            messagebox.showerror("Erro", "Organizador não encontrado")

    tk.Button(root, text="Salvar Evento", command=salvar_evento).pack()

    root.mainloop()

def adicionar_itens_evento_interface():
    root = tk.Tk()
    root.title("Adicionar Itens ao Evento")

    eventos = carregar_dados('dados/eventos.pkl')
    tk.Label(root, text="Selecione o Evento:").pack()
    evento_combo = ttk.Combobox(root, values=[e.nome for e in eventos])
    evento_combo.pack()

    tk.Label(root, text="Adicionar Comida:").pack()
    comidas = carregar_dados('dados/comidas.pkl')
    comida_combo = ttk.Combobox(root, values=[c.nome for c in comidas])
    comida_combo.pack()

    tk.Label(root, text="Adicionar Bebida:").pack()
    bebidas = carregar_dados('dados/bebidas.pkl')
    bebida_combo = ttk.Combobox(root, values=[b.nome for b in bebidas])
    bebida_combo.pack()

    tk.Label(root, text="Adicionar Convidado:").pack()
    convidados = carregar_dados('dados/convidados.pkl')
    convidado_combo = ttk.Combobox(root, values=[c.nome for c in convidados])
    convidado_combo.pack()

    def adicionar_itens():
        nome_evento = evento_combo.get()
        evento = next((e for e in eventos if e.nome == nome_evento), None)

        if evento:
            nome_comida = comida_combo.get()
            nome_bebida = bebida_combo.get()
            nome_convidado = convidado_combo.get()

            comida = next((c for c in comidas if c.nome == nome_comida), None)
            bebida = next((b for b in bebidas if b.nome == nome_bebida), None)
            convidado = next((c for c in convidados if c.nome == nome_convidado), None)

            if comida:
                adicionar_comida_evento(evento, comida)
            if bebida:
                adicionar_bebida_evento(evento, bebida)
            if convidado:
                adicionar_convidado_evento(evento, convidado)

            salvar_dados(eventos, 'dados/eventos.pkl')
            messagebox.showinfo("Sucesso", "Itens adicionados com sucesso!")
        else:
            messagebox.showerror("Erro", "Evento não encontrado")

    tk.Button(root, text="Adicionar Itens", command=adicionar_itens).pack()

    root.mainloop()
