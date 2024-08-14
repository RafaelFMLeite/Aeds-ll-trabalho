import tkinter as tk
from tkinter import ttk, messagebox
from operacoes.ordenacao import merge_sort
from operacoes.persistencia import carregar_dados, salvar_dados

def ordenar_dados_interface():
    def ordenar_dados():
        entidade = entidade_var.get()
        
        # Mapeamento das entidades para os arquivos correspondentes
        arquivos = {
            "Usuários": 'dados/usuarios.pkl',
            "Convidados": 'dados/convidados.pkl',
            "Comidas": 'dados/comidas.pkl',
            "Bebidas": 'dados/bebidas.pkl'
        }

        if entidade not in arquivos:
            messagebox.showerror("Erro", "Entidade desconhecida")
            return
        
        # Carregar dados
        dados = carregar_dados(arquivos[entidade])
        
        if not dados:
            messagebox.showerror("Erro", "Nenhum dado encontrado para ordenar")
            return

        chave = "id"  # Ordenar por 'id'

        try:
            # Ordenar e salvar os dados
            merge_sort(dados, chave)
            salvar_dados(dados, arquivos[entidade])
            messagebox.showinfo("Sucesso", f"Dados de {entidade} ordenados com sucesso!")
        except AttributeError as e:
            messagebox.showerror("Erro", f"Erro ao ordenar {entidade}: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ordenar {entidade}: {e}")

    root = tk.Tk()
    root.title("Ordenar Dados")

    tk.Label(root, text="Escolha a Entidade:").pack(pady=5)
    entidade_var = tk.StringVar()
    entidade_combo = ttk.Combobox(root, textvariable=entidade_var, values=["Usuários", "Convidados", "Comidas", "Bebidas"])
    entidade_combo.pack(pady=5)
    
    tk.Button(root, text="Ordenar por ID", command=ordenar_dados).pack(pady=10)

    root.mainloop()
