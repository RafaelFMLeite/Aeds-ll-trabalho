import tkinter as tk
from tkinter import ttk, messagebox
from operacoes.ordenacao import ordenar_dados
from operacoes.persistencia import carregar_dados, salvar_dados

def ordenar_dados_interface():
    def atualizar_entidade(event):
        entidade = entidade_combo.get().strip()
        entidade_var.set(entidade)
        print(f"Entidade selecionada: '{entidade}'")  # Verificação de valor selecionado

    def ordenar_dados_evento():
        entidade = entidade_var.get().strip()
        
        arquivos = {
            "Usuários": 'dados/usuarios.pkl',
            "Convidados": 'dados/convidados.pkl',
            "Comidas": 'dados/comidas.pkl',
            "Bebidas": 'dados/bebidas.pkl'
        }

        if entidade not in arquivos:
            messagebox.showerror("Erro", "Entidade desconhecida")
            return
        
        dados = carregar_dados(arquivos[entidade])
        
        if dados is None or not dados:
            messagebox.showerror("Erro", "Nenhum dado encontrado para ordenar")
            return

        try:
            dados_ordenados = ordenar_dados(dados)
            salvar_dados(dados_ordenados, arquivos[entidade])
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
    
    # Associe a mudança de seleção ao evento de atualização da entidade
    entidade_combo.bind("<<ComboboxSelected>>", atualizar_entidade)

    tk.Button(root, text="Ordenar por ID", command=ordenar_dados_evento).pack(pady=10)

    root.mainloop()
