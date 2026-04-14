# Ejecucion de los ejercicios

Este documento explica como ejecutar cada uno de los ejercicios y que entrada debe usar el profesor para probarlos.

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


---

# Ejercicio 2

## Nota importante

Esta gramatica no es LL(1), por lo tanto el parser puede no ser completamente confiable.

## Tokens validos
```
uno dos tres cuatro cinco seis siete
```

