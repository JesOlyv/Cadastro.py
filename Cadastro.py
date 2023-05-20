import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self, matricula, nome, nota1, nota2):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2) / 2
        self.aprovado = self.media >= 6.0

class CadastroAlunos:
    def __init__(self):
        self.alunos = []

        self.window = tk.Tk()
        self.window.title("Cadastro de Alunos")

        self.label_matricula = tk.Label(self.window, text="Matrícula:")
        self.label_matricula.pack()

        self.entry_matricula = tk.Entry(self.window)
        self.entry_matricula.pack()

        self.label_nome = tk.Label(self.window, text="Nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(self.window)
        self.entry_nome.pack()

        self.label_nota1 = tk.Label(self.window, text="Nota 1:")
        self.label_nota1.pack()

        self.entry_nota1 = tk.Entry(self.window)
        self.entry_nota1.pack()

        self.label_nota2 = tk.Label(self.window, text="Nota 2:")
        self.label_nota2.pack()

        self.entry_nota2 = tk.Entry(self.window)
        self.entry_nota2.pack()

        self.button_cadastrar = tk.Button(self.window, text="Cadastrar", command=self.cadastrar_aluno)
        self.button_cadastrar.pack()

        self.window.mainloop()

    def cadastrar_aluno(self):
        matricula = self.entry_matricula.get()
        nome = self.entry_nome.get()
        nota1 = float(self.entry_nota1.get())
        nota2 = float(self.entry_nota2.get())

        aluno = Aluno(matricula, nome, nota1, nota2)
        self.alunos.append(aluno)

        mensagem = f"Aluno {aluno.nome} cadastrado com sucesso.\nMatrícula: {aluno.matricula}\nMédia: {aluno.media:.2f}"

        if aluno.aprovado:
            mensagem += "\nSituação: Aprovado"
        else:
            mensagem += "\nSituação: Reprovado"

        messagebox.showinfo("Sucesso", mensagem)

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_matricula.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_nota1.delete(0, tk.END)
        self.entry_nota2.delete(0, tk.END)

CadastroAlunos()
