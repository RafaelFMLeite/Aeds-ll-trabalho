<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk, messagebox
from operacoes.ordenacao import ordenar_dados
=======
import tkinter as tk  # criar a interface gráfica.
from tkinter import messagebox  # mostrar mensagens de erro e sucesso.
from operacoes.ordenacao import merge_sort
>>>>>>> development
from operacoes.persistencia import carregar_dados, salvar_dados
import datetime  # manipular data e hora.

def log_message(message):
    with open('dados/log.txt', 'a') as log_file:  # log.txt.
        log_file.write(f"{datetime.datetime.now()}: {message}\n")

def ordenar_entidade(arquivo, chave):
    dados = carregar_dados(arquivo)

    log_message(f"Dados carregados antes da ordenação ({arquivo}): {[getattr(d, chave, '') for d in dados]}")
    
    if not dados:  # verifica se os dados estão vazios.
        messagebox.showerror("Erro", f"Nenhum dado encontrado para ordenar ({arquivo})")
        log_message(f"Erro: Nenhum dado encontrado para ordenar ({arquivo})")  
        return  

    try:
        merge_sort(dados, chave)  # ordenar os dados com base na chave especificada usando merge_sort.

        log_message(f"Dados depois da ordenação ({arquivo}): {[getattr(d, chave) for d in dados]}")
        
        salvar_dados(dados, arquivo)
        messagebox.showinfo("Sucesso", f"Dados ordenados com sucesso ({arquivo})!")  
        log_message(f"Sucesso: Dados ordenados ({arquivo})")  
    except AttributeError as e:  # exceções do tipo AttributeError (erro relacionado à chave não encontrada nos dados).
        messagebox.showerror("Erro", f"Erro ao ordenar {arquivo}: {e}") 
        log_message(f"Erro: {e} ao ordenar {arquivo}")  
    except Exception as e:  # qualquer outra exceção que possa ocorrer.
        messagebox.showerror("Erro", f"Erro ao ordenar {arquivo}: {e}")  
        log_message(f"Erro: {e} ao ordenar {arquivo}")  

def ordenar_dados_interface():
<<<<<<< HEAD
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
=======
    root = tk.Tk()  # cria uma instância
    root.title("Ordenar Dados")

    tk.Button(root, text="Ordenar Usuários", command=lambda: ordenar_entidade('dados/usuarios.pkl', 'nome')).pack(pady=5) 
    tk.Button(root, text="Ordenar Convidados", command=lambda: ordenar_entidade('dados/convidados.pkl', 'nome')).pack(pady=5)  
    tk.Button(root, text="Ordenar Comidas", command=lambda: ordenar_entidade('dados/comidas.pkl', 'nome')).pack(pady=5) 
    tk.Button(root, text="Ordenar Bebidas", command=lambda: ordenar_entidade('dados/bebidas.pkl', 'nome')).pack(pady=5) 
    tk.Button(root, text="Ordenar Eventos", command=lambda: ordenar_entidade('dados/eventos.pkl', 'nome')).pack(pady=5) 
>>>>>>> development

    root.mainloop()
