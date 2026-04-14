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
    if tokens[pos] in ["dos", "cuatro", "seis"]:
        A()
        B()
        C()
    else:
        D()
        E()

def A():
    if tokens[pos] == "dos":
        match("dos")
        B()
        match("tres")
    else:
        pass

def B():
    if tokens[pos] == "cuatro":
        Bp()
    else:
        pass

def Bp():
    if pos < len(tokens) and tokens[pos] == "cuatro":
        match("cuatro")
        C()
        match("cinco")
        Bp()
    else:
        pass

def C():
    if tokens[pos] == "seis":
        match("seis")
        A()
        B()
    else:
        pass

def D():
    if tokens[pos] == "uno":
        match("uno")
        A()
        E()
    else:
        B()

def E():
    match("tres")


# prueba
tokens = input("ingrese tokens: ").split()
S()

if pos == len(tokens):
    print("cadena valida")
else:
    print("cadena invalida")
