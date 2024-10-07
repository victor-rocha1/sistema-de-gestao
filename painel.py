import tkinter as tk

# Função para abrir o painel do usuário
def abrir_painel(janela_login, username):
    painel = tk.Toplevel()  # Cria uma nova janela
    painel.title("Painel do Usuário")
    painel.geometry("500x400")
    painel.configure(bg="#f0f0f0")
    painel.attributes('-topmost', True)  # Faz a janela ficar sempre no topo

    # Label de boas-vindas
    label_bem_vindo = tk.Label(painel, text=f"Bem-vindo a Modular Life, {username}!", font=("Arial", 14), bg="#f0f0f0")
    label_bem_vindo.pack(pady=20)

    # Botão para sair
    button_sair = tk.Button(painel, text="Sair", command=lambda: sair(painel, janela_login), bg="#FF5722", fg="white", width=10)
    button_sair.pack(pady=10)

# Função para sair e voltar à tela de login
def sair(painel, janela_login):
    painel.destroy()  # Fecha o painel
    janela_login.deiconify()  # Mostra a janela de login novamente
