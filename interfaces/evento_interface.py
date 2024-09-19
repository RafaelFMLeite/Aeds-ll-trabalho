import tkinter as tk
import psutil
from tkinter import ttk, messagebox
from entidades.evento import Evento
from operacoes.persistencia import salvar_dados, carregar_dados, gerar_id
from operacoes.interacoes import adicionar_convidado_evento, adicionar_comida_evento, adicionar_bebida_evento
import logging
from operacoes.particoes import gerar_particoes_por_letra_com_log
from operacoes.intercalacao import arvore_vencedores, carregar_particoes

# Configuração do logging
logging.basicConfig(
    filename='dados/evento_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # Modo de escrita, substitui o conteúdo existente do log
)

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
        nome_evento = nome_entry.get().strip()
        nome_organizador = organizador_combo.get()
        organizador = next((u for u in usuarios if u.nome == nome_organizador), None)

        if organizador:
            eventos = carregar_dados('dados/eventos.pkl')

            evento_existente = next((e for e in eventos if e.nome == nome_evento), None)

            if evento_existente:
                messagebox.showerror("Erro", "Já existe um evento com esse nome. Escolha outro nome.")
                logging.warning(f"Tentativa de criar evento com nome duplicado: {nome_evento}")
            else:
                evento = Evento(gerar_id(), nome_evento, organizador.id_usuario)
                eventos.append(evento)
                salvar_dados(eventos, 'dados/eventos.pkl')
                messagebox.showinfo("Sucesso", "Evento criado com sucesso!")
                logging.info(f"Evento criado: {evento.nome} com ID: {evento.id_evento}")
        else:
            messagebox.showerror("Erro", "Organizador não encontrado")
            logging.error(f"Organizador {nome_organizador} não encontrado")

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
            comida = next((c for c in comidas if c.nome == nome_comida), None)
            if comida:
                adicionar_comida_evento(evento, comida)

            nome_bebida = bebida_combo.get()
            bebida = next((b for b in bebidas if b.nome == nome_bebida), None)
            if bebida:
                adicionar_bebida_evento(evento, bebida)

            nome_convidado = convidado_combo.get()
            convidado = next((c for c in convidados if c.nome == nome_convidado), None)
            if convidado:
                adicionar_convidado_evento(evento, convidado)

            salvar_dados(eventos, 'dados/eventos.pkl')
            messagebox.showinfo("Sucesso", "Itens adicionados ao evento com sucesso!")
            logging.info(f"Itens adicionados ao evento: {evento.nome}")
        else:
            messagebox.showerror("Erro", "Evento não encontrado")
            logging.error(f"Evento {nome_evento} não encontrado")

    tk.Button(root, text="Adicionar Itens", command=adicionar_itens).pack(pady=10)

    root.mainloop()

def gerar_particoes_por_letra_interface():
    # Carregar os dados dos eventos
    dados = carregar_dados('dados/eventos.pkl')
    if not dados:
        messagebox.showerror("Erro", "Nenhum dado encontrado")
        return

    # Gerar partições por letra inicial com log
    particoes = gerar_particoes_por_letra_com_log(dados)

    # Salvar as partições geradas
    salvar_dados(particoes, 'dados/particoes_eventos_por_letra.pkl')

    # Exibir mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Partições por letra geradas com sucesso! Total: {len(particoes)}")

def intercalar_particoes_arvore_vencedores_interface():
    try:
        # Carregar partições do arquivo
        particoes = carregar_particoes('dados/particoes_eventos_por_letra.pkl')
        
        if not particoes:
            raise ValueError("Nenhuma partição encontrada")

        resultado = arvore_vencedores(particoes)  # Intercala as partições
        salvar_dados(resultado, 'dados/eventos_intercalados.pkl')
        messagebox.showinfo("Sucesso", "Eventos intercalados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
