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
    if tokens[pos] == "dos":
        match("dos")
        C()
    elif tokens[pos] in ["cuatro", "siete"]:
        B()
        match("uno")
    else:
        pass

def A():
    if tokens[pos] == "cuatro":
        match("cuatro")
    elif tokens[pos] in ["dos", "siete"]:
        S()
        match("tres")
        B()
        C()
    else:
        pass

def B():
    if tokens[pos] in ["dos", "cuatro", "siete"]:
        A()
        match("cinco")
        C()
        match("seis")
    else:
        pass

def C():
    if tokens[pos] == "siete":
        match("siete")
        B()
    else:
        pass


# prueba
tokens = input("ingrese tokens: ").split()
S()

if pos == len(tokens):
    print("cadena valida")
else:
    print("cadena invalida (gramatica no LL1)")
