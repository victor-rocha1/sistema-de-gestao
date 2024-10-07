import tkinter as tk
import fichas

# Função para abrir o painel do usuário
def abrir_painel(janela_login, username):
    painel = tk.Toplevel()
    painel.title("Painel do Usuário")
    painel.geometry(janela_login.geometry())  # Define as mesmas dimensões da janela de login
    painel.configure(bg="#f0f0f0")
    painel.attributes('-topmost', True)  # Faz a janela ficar ativa

    # Label de boas-vindas
    label_bem_vindo = tk.Label(painel, text=f"Bem-vindo a Modular Life, {username}!", font=("Arial", 14), bg="#f0f0f0")
    label_bem_vindo.pack(pady=20)

    # Botão para abrir nova janela
    button_nova_janela = tk.Button(painel, text="Ver suas fichas", command=lambda: abrir_nova(janela_login, painel), bg="#4CAF50", fg="white", width=15)
    button_nova_janela.pack(pady=10)

    # Botão para sair e voltar à tela de login
    button_sair = tk.Button(painel, text="Sair", command=lambda: sair(painel, janela_login), bg="#FF5722", fg="white", width=10)
    button_sair.pack(pady=10)

# Função para abrir a nova janela e ocultar o painel
def abrir_nova(janela_login, painel):
    geometry = painel.geometry()  # Pega a posição e dimensões da janela atual
    painel.withdraw()  # Oculta o painel
    fichas.abrir_janela_fichas(painel, geometry)  # Chama a função que abre a nova janela

# Função para sair e voltar à tela de login
def sair(painel, janela_login):
    painel.destroy()  # Fecha o painel
    janela_login.deiconify()  # Mostra a janela de login novamente