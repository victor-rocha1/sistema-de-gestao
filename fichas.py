import tkinter as tk

# Função para abrir a nova janela e ocultar a janela anterior
def abrir_janela_fichas(janela_anterior, geometry):
    # Cria uma nova janela com as mesmas dimensões e posição
    fichas = tk.Toplevel()
    fichas.title("Fichas do Usuário")
    fichas.geometry(geometry)  # Aplica a mesma geometria da janela anterior
    fichas.configure(bg="#f0f0f0")

    # Adiciona conteúdo à nova janela
    label = tk.Label(fichas, text="Veja aqui as suas fichas", font=("Arial", 14), bg="#f0f0f0")
    label.pack(pady=20)

    # Botão para voltar ao painel
    button_voltar = tk.Button(fichas, text="Voltar a Página Principal", command=lambda: voltar_para_painel(fichas, janela_anterior), bg="#4CAF50", fg="white", width=25)
    button_voltar.pack(pady=10)

# Função para voltar ao painel e ocultar as fichas
def voltar_para_painel(fichas, janela_anterior):
    fichas.destroy()  # Fecha a janela atual
    janela_anterior.deiconify()  # Mostra novamente o painel
