import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexão com o SQLite
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# Tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# Função para registrar usuário
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Entrada inválida", "Usuário e senha não podem estar vazios.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Registro bem-sucedido", f"Usuário {username} registrado com sucesso!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

# Função para login de usuário
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {username}!")
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos!")

# Interface Tkinter
janela = tk.Tk()
janela.title("Modular Life")
janela.geometry("300x250")  # Tamanho da janela

# Estilo básico
janela.configure(bg="#f0f0f0")  # Cor de fundo

# Label para título da tela
label_title = tk.Label(janela, text="Tela de Login", font=("Arial", 16), bg="#f0f0f0")
label_title.pack(pady=10)

# Labels e Entradas para o login
label_name = tk.Label(janela, text="Usuário:", bg="#f0f0f0")
label_name.pack(pady=5)

entry_username = tk.Entry(janela, width=30)
entry_username.pack(pady=5)

label_password = tk.Label(janela, text="Senha:", bg="#f0f0f0")
label_password.pack(pady=5)

entry_password = tk.Entry(janela, show="*", width=30)
entry_password.pack(pady=5)

# Botão de login
button_login = tk.Button(janela, text="Login", command=login_user, bg="#4CAF50", fg="white", width=10)
button_login.pack(pady=10)

# Botão de registrar
button_register = tk.Button(janela, text="Registrar", command=register_user, bg="#2196F3", fg="white", width=10)
button_register.pack(pady=10)

# Loop para rodar a interface
janela.mainloop()

# Fechar a conexão com o banco ao final
conn.close()