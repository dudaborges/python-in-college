import turtle as t

t.speed(13)
t.ht()
nome = t.textinput("Nome", "Digite o seu nome")
sobrenome = t.textinput("Sobrenome", "Digite seu sobrenome")
t.write("Olá, " + nome + " " + sobrenome + "!")

t.mainloop()


