import turtle as bob

nome = bob.textinput("Nome", "Digite o seu nome").upper()
sobrenome = bob.textinput("Sobrenome", "Digite seu sobrenome").upper()
nomeCompleto = nome + sobrenome
letras = list(nomeCompleto)

def desenhar_letras(letras):
    if("A" in letras):
            bob.delay(30)
            bob.lt(90)
            bob.rt(25)
            bob.fd(100)
            bob.rt(130)
            bob.fd(100)
            bob.rt(180)
            bob.fd(50)
            bob.lt(65)
            bob.fd(50)
            bob.clear()
            bob.reset()
    if("B" in letras):
        bob.delay(30)
        bob.rt(90)
        bob.fd(200)
        bob.lt(90)
        bob.fd(150)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(20)
        bob.lt(20)
        bob.fd(150)
        bob.rt(90)
        bob.fd(130)
        bob.rt(90)
        bob.fd(100)
        bob.rt(20)
        bob.fd(25)
        bob.rt(20)
        bob.fd(25)
        bob.rt(20)
        bob.fd(25)
        bob.rt(20)
        bob.fd(25)
        bob.rt(20)
        bob.fd(23)
        bob.rt(20)
        bob.fd(18)
        bob.rt(20)
        bob.fd(20)
        bob.rt(20)
        bob.fd(25)
        bob.rt(20)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("C" in letras):
        bob.delay(30)
        bob.lt(180)
        bob.fd(90)
        bob.lt(90)
        bob.fd(120)
        bob.lt(90)
        bob.fd(90)
        bob.clear()
        bob.reset()
    if("D" in letras):
        bob.delay(30)

        def tcircle(radius):
            c = 2 * 3.14 * radius
            n = 10 
            l = c / n
            regular_polygon(int(l), n)

        def regular_polygon(l, n):
            for _ in range(n):
                bob.forward(l)
                bob.left(200 / n)

        bob.ht()
        tcircle(40)
        bob.rt(-68)
        bob.fd(142)
        bob.clear()
        bob.reset()
        if("E" in letras):
            bob.delay(30)
            bob.lt(90)
            bob.fd(100)
            bob.rt(90)
            bob.fd(50)
            bob.bk(50)
            bob.rt(90)
            bob.fd(50)
            bob.lt(90)
            bob.fd(50)
            bob.bk(50)
            bob.rt(90)
            bob.fd(50)
            bob.lt(90)
            bob.fd(50)
            bob.clear()
            bob.reset()
    if("F" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(100)
        bob.rt(90)
        bob.fd(50)
        bob.lt(180)
        bob.fd(50)
        bob.lt(90)
        bob.fd(40)
        bob.lt(90)
        bob.fd(40)
        bob.lt(180)
        bob.fd(40)
        bob.clear()
        bob.reset()
    if("G" in letras):
        bob.delay(30)
        bob.rt(180)
        bob.fd(100)
        bob.lt(90)
        bob.fd(150)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(75)
        bob.lt(90)
        bob.fd(50)
        bob.clear()
        bob.reset()
    if("H" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(100)
        bob.lt(180)
        bob.fd(200)
        bob.lt(180)
        bob.fd(100)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(100)
        bob.lt(180)
        bob.fd(200)
        bob.clear()
        bob.reset()
    if("I" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("J" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(100)
        bob.rt(180)
        bob.forward(100)
        bob.forward(100)
        bob.lt(180)
        bob.fd(100)
        bob.lt(90)
        bob.fd(200)
        bob.rt(90)
        bob.fd(120)
        bob.rt(90)
        bob.fd(50)
        bob.clear()
        bob.reset()
    if("K" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(150)
        bob.lt(180)
        bob.fd(80)
        bob.lt(150)
        bob.fd(90)
        bob.lt(180)
        bob.fd(90)
        bob.lt(70)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("L" in letras):
        bob.delay(30)
        bob.rt(90)
        bob.fd(150)
        bob.lt(90)
        bob.fd(130)
        bob.clear()
        bob.reset()
    if("M" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(150)
        bob.rt(150)
        bob.fd(100)
        bob.lt(120)
        bob.fd(100)
        bob.rt(150)
        bob.fd(150)
        bob.clear()
        bob.reset()
    if("N" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(100)
        bob.rt(150)
        bob.fd(115)
        bob.lt(148)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("O" in letras):
        bob.delay(30)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.hideturtle()
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.fd(40)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.fd(40)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.lt(-5)
        bob.fd(5)
        bob.clear()
        bob.reset()
    if("P" in letras):
        bob.delay(30)
        bob.hideturtle()
        bob.lt(90)
        bob.fd(150)
        bob.rt(90)
        bob.fd(55)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(5)
        bob.rt(10)
        bob.fd(55)
        bob.clear()
        bob.reset()
    if("Q" in letras):
        bob.delay(30)
        bob.rt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(200)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(100)
        bob.lt(180)
        bob.fd(100)
        bob.lt(208)
        bob.fd(280)
        bob.clear()
        bob.reset()
    if("R" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(100)
        bob.rt(90)
        bob.fd(70)
        bob.rt(90)
        bob.fd(40)
        bob.rt(90)
        bob.fd(70)
        bob.lt(140)
        bob.fd(90)
        bob.clear()
        bob.reset()
    if("S" in letras):
        bob.delay(30)
        bob.fd(90)
        bob.rt(180)
        bob.fd(90)
        bob.lt(90)
        bob.fd(90)
        bob.lt(90)
        bob.fd(90)
        bob.lt(270)
        bob.fd(90)
        bob.lt(270)
        bob.fd(90)
        bob.clear()
        bob.reset()
    if("T" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(200)
        bob.rt(90)
        bob.fd(90)
        bob.back(180)
        bob.clear()
        bob.reset()
    if("U" in letras):
        bob.delay(30)
        bob.lt(90)
        bob.fd(200)
        bob.lt(180)
        bob.fd(200)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
        bob.fd(200)
        bob.clear()
        bob.reset()
    if("V" in letras):
        bob.delay(30)
        bob.lt(125)
        bob.fd(100)
        bob.lt(900)
        bob.fd(100)
        bob.right(600)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("W" in letras):
        bob.delay(30)
        bob.rt(70)
        bob.fd(100)
        bob.rt(220)
        bob.fd(100)
        bob.rt(140)
        bob.fd(100)
        bob.rt(220)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("X" in letras):
        bob.delay(30)
        bob.rt(70)
        bob.fd(100)
        bob.back(50)
        bob.rt(220)
        bob.fd(50)
        bob.back(100)
        bob.clear()
        bob.reset()
    if("Y" in letras):
        bob.delay(30)
        bob.rt(60)
        bob.fd(100)
        bob.lt(120)
        bob.fd(100)
        bob.rt(180)
        bob.fd(100)
        bob.lt(30)
        bob.fd(100)
        bob.clear()
        bob.reset()
    if("Z" in letras):
        bob.delay(30)
        bob.fd(90)
        bob.lt(240)
        bob.fd(180)
        bob.rt(240)
        bob.fd(90)
        bob.clear()
        bob.reset()

for letra in letras:
    desenhar_letras(letra)

bob.mainloop()