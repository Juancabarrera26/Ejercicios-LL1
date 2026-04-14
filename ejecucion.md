# Ejecucion de los ejercicios

Este documento explica como ejecutar cada uno de los ejercicios y que entrada debe usar para probarlos.

Todos los programas estan hechos en Python y se ejecutan desde consola.

---

# Forma de ejecucion

Cada ejercicio se ejecuta asi:

```
python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
```

Luego el programa pedira:
```
ingrese tokens:
```

Se deben ingresar palabras separadas por espacio.

---

# Ejercicio 1

## Tokens validos

```
uno dos tres cuatro cinco seis
```


## Ejemplos para probar

### Ejemplo valido 1
```
dos tres
```

### Ejemplo valido 2
```
uno tres
```

### Ejemplo valido 3
```
dos cuatro cinco tres
```

### Ejemplo invalido
```
dos cinco
```

## Resultado esperado

- Si la cadena es correcta:
```
cadena valida
```

- Si la cadena es incorrecta:
```
error
```

# Ejercicio 2

## Nota importante

Esta gramatica no es LL(1), por lo tanto el parser puede no ser completamente confiable.

## Tokens validos
```
uno dos tres cuatro cinco seis siete
```

## Ejemplos para probar

### Ejemplo valido
```
dos siete
```

### Ejemplo invalido
```
uno
```

## Resultado esperado

- Puede aceptar o rechazar cadenas debido a conflictos
- Si falla:
```
error
```

---

# Ejercicio 3

## Tokens validos
```
uno dos tres cuatro
```

## Ejemplos para probar

### Ejemplo valido 1
```
dos
```

### Ejemplo valido 2
```
dos cuatro tres
```

### Ejemplo valido 3
```
dos cuatro tres uno uno
```

### Ejemplo invalido
```
cuatro
```

## Resultado esperado

- Si la cadena es correcta:
```
error
```

---

# Observaciones

- Las palabras deben escribirse exactamente como aparecen
- Separadas por espacios
- No usar comas ni simbolos

Ejemplo correcto:
```
dos cuatro cinco tres
```

Ejemplo incorrecto:
```
dos, cuatro, cinco, tres
```
---

