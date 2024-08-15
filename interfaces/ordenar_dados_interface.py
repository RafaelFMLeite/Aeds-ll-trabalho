import tkinter as tk
from tkinter import messagebox
from operacoes.ordenacao import merge_sort
from operacoes.persistencia import carregar_dados, salvar_dados
import datetime

def log_message(message):
    with open('dados/log.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")

def ordenar_entidade(arquivo, chave):
    # Carregar dados
    dados = carregar_dados(arquivo)
    
    log_message(f"Dados carregados antes da ordenação ({arquivo}): {[getattr(d, chave, '') for d in dados]}")
    
    if not dados:
        messagebox.showerror("Erro", f"Nenhum dado encontrado para ordenar ({arquivo})")
        log_message(f"Erro: Nenhum dado encontrado para ordenar ({arquivo})")
        return

    try:
        # Ordenar e salvar os dados
        merge_sort(dados, chave)
        
        log_message(f"Dados depois da ordenação ({arquivo}): {[getattr(d, chave) for d in dados]}")
        
        salvar_dados(dados, arquivo)
        messagebox.showinfo("Sucesso", f"Dados ordenados com sucesso ({arquivo})!")
        log_message(f"Sucesso: Dados ordenados ({arquivo})")
    except AttributeError as e:
        messagebox.showerror("Erro", f"Erro ao ordenar {arquivo}: {e}")
        log_message(f"Erro: {e} ao ordenar {arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ordenar {arquivo}: {e}")
        log_message(f"Erro: {e} ao ordenar {arquivo}")

def ordenar_dados_interface():
    root = tk.Tk()
    root.title("Ordenar Dados")

    tk.Button(root, text="Ordenar Usuários", command=lambda: ordenar_entidade('dados/usuarios.pkl', 'nome')).pack(pady=5)
    tk.Button(root, text="Ordenar Convidados", command=lambda: ordenar_entidade('dados/convidados.pkl', 'nome')).pack(pady=5)
    tk.Button(root, text="Ordenar Comidas", command=lambda: ordenar_entidade('dados/comidas.pkl', 'nome')).pack(pady=5)
    tk.Button(root, text="Ordenar Bebidas", command=lambda: ordenar_entidade('dados/bebidas.pkl', 'nome')).pack(pady=5)
    tk.Button(root, text="Ordenar Eventos", command=lambda: ordenar_entidade('dados/eventos.pkl', 'nome')).pack(pady=5)

    root.mainloop()
