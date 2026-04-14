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
    if actual() == "dos":
        match("dos")
        C()
    elif actual() in ["cuatro", "siete"]:
        B()
        match("uno")
    else:
        pass

def A():
    if actual() == "cuatro":
        match("cuatro")
    elif actual() in ["dos", "siete"]:
        S()
        match("tres")
        B()
        C()

def B():
    if actual() in ["dos", "cuatro", "siete"]:
        A()
        match("cinco")
        C()
        match("seis")

def C():
    if actual() == "siete":
        match("siete")
        B()


# MAIN
tokens = input("ingrese tokens: ").split()
S()

if pos == len(tokens):
    print("cadena valida")
else:
    print("cadena invalida")
