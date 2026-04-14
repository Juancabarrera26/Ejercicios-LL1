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
    if actual() in ["dos", "cuatro", "seis"]:
        A()
        B()
        C()
    else:
        D()
        E()

def A():
    if actual() == "dos":
        match("dos")
        B()
        match("tres")

def B():
    if actual() == "cuatro":
        Bp()

def Bp():
    if actual() == "cuatro":
        match("cuatro")
        C()
        match("cinco")
        Bp()

def C():
    if actual() == "seis":
        match("seis")
        A()
        B()

def D():
    if actual() == "uno":
        match("uno")
        A()
        E()
    else:
        B()

def E():
    if actual() == "tres":
        match("tres")
    else:
        print("error")
        exit()


# MAIN (esto SI es necesario)
tokens = input("ingrese tokens: ").split()
S()

if pos == len(tokens):
    print("cadena valida")
else:
    print("cadena invalida")
