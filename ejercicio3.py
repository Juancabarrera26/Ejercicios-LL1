tokens = []
pos = 0

def actual():
    if pos < len(tokens):
        return tokens[pos]
    return None

def match(t):
    global pos
    if actual() == t:
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
    if actual() == "uno":
        match("uno")
        Sp()

def A():
    if actual() == "dos":
        match("dos")
        B()
        C()

def B():
    if actual() == "cuatro":
        C()
        match("tres")

def C():
    if actual() == "cuatro":
        match("cuatro")
        B()


# MAIN
tokens = input("ingrese tokens: ").split()
S()

if pos == len(tokens):
    print("cadena valida")
else:
    print("cadena invalida")
