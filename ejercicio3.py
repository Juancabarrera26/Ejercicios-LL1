tokens = []
pos = 0

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        print("error")
        exit()

def S():
    A()
    B()
    C()
    Sp()

def Sp():
    if pos < len(tokens) and tokens[pos] == "uno":
        match("uno")
        Sp()
    else:
        pass

def A():
    if tokens[pos] == "dos":
        match("dos")
        B()
        C()
    else:
        pass

def B():
    if tokens[pos] == "cuatro":
        C()
        match("tres")
    else:
        pass

def C():
    if tokens[pos] == "cuatro":
        match("cuatro")
        B()
    else:
        pass


# prueba
tokens = input("ingrese tokens: ").split()
S()

if pos == len(tokens):
    print("cadena valida")
else:
    print("cadena invalida")
