# Taller - Procesadores de Lenguaje

Solucion de los ejercicios 1, 2 y 3 de la presentacion 7.

En cada ejercicio se realiza:

- Eliminacion de recursividad por la izquierda (si aplica)
- Calculo de conjuntos PRIMEROS
- Calculo de conjuntos SIGUIENTES
- Calculo de conjuntos de prediccion
- Verificacion si la gramatica es LL(1)

---

# Ejercicio 1

## Gramatica original

S -> A B C  
S -> D E  
A -> dos B tres | e  
B -> B cuatro C cinco | e  
C -> seis A B | e  
D -> uno A E | B  
E -> tres  

---

## Eliminacion de recursividad

La unica recursividad esta en B:

B -> B cuatro C cinco | e  

Se transforma en:

B -> e Bp  
Bp -> cuatro C cinco Bp | e  

---

## PRIMEROS

- FIRST(A) = { dos, e }
- FIRST(B) = { cuatro, e }
- FIRST(C) = { seis, e }
- FIRST(D) = { uno, cuatro, e }
- FIRST(E) = { tres }
- FIRST(S) = { dos, uno, cuatro, seis, tres, e }

---

## SIGUIENTES

- FOLLOW(S) = { $ }
- FOLLOW(A) = { cuatro, seis, tres, $ }
- FOLLOW(B) = { seis, tres, cinco, $ }
- FOLLOW(C) = { cinco, $ }
- FOLLOW(D) = { tres }
- FOLLOW(E) = { $ }

---

## Prediccion

No hay intersecciones entre reglas de un mismo no terminal.

---

## La gramatica SI es LL1.

Porque:

- Se elimino la recursividad por la izquierda en B.
- Los conjuntos FIRST de las producciones de un mismo no terminal no se intersectan.
- Cuando hay epsilon, los FOLLOW no generan conflictos.
- El parser puede decidir que produccion usar con un solo token.

## Conclusion:

La gramatica es LL1 porque no hay ambiguedad en la seleccion de producciones.

---

# Ejercicio 2

## Gramatica

S -> B uno | dos C | e  
A -> S tres B C | cuatro | e  
B -> A cinco C seis | e  
C -> siete B | e  

---

## PRIMEROS

- FIRST(S) = { dos, cuatro, siete, e }
- FIRST(A) = { dos, cuatro, siete, e }
- FIRST(B) = { dos, cuatro, siete, e }
- FIRST(C) = { siete, e }

---

## SIGUIENTES

- FOLLOW(S) = { $, tres }
- FOLLOW(A) = { cinco }
- FOLLOW(B) = { uno, seis }
- FOLLOW(C) = { seis, $ }

---

## Prediccion

Existen intersecciones en los conjuntos de prediccion.

---

## La gramatica NO es LL1.

Porque:

- Los conjuntos FIRST de varios no terminales son iguales o se intersectan.
- Existen muchas producciones con epsilon.
- Los conjuntos FOLLOW se cruzan con FIRST generando conflictos.
- No se puede decidir que produccion usar con un solo token.

## Conclusion:

La gramatica no es LL1 porque hay ambiguedad en la seleccion de producciones.

---

# Ejercicio 3

## Gramatica original

S -> A B C | S uno  
A -> dos B C | e  
B -> C tres | e  
C -> cuatro B | e  

---

## Eliminacion de recursividad

S -> A B C S'  
S' -> uno S' | e  

---

## PRIMEROS

- FIRST(A) = { dos, e }
- FIRST(B) = { cuatro, e }
- FIRST(C) = { cuatro, e }
- FIRST(S) = { dos, cuatro, e }

---

## SIGUIENTES

- FOLLOW(S) = { $ }
- FOLLOW(A) = { cuatro, $ }
- FOLLOW(B) = { cuatro, tres, $ }
- FOLLOW(C) = { tres, $ }

---

## Prediccion

No hay conflictos entre reglas.

---

La gramatica SI es LL1.

Porque:

- Se elimino la recursividad por la izquierda en S.
- Los conjuntos de prediccion no se intersectan.
- El manejo de epsilon no genera conflictos.
- Cada decision se puede tomar con un solo token.

## Conclusion:

La gramatica es LL1 porque no presenta conflictos en la prediccion.

# Resumen de ejercicios

- Ejercicio 1: LL(1)
- Ejercicio 2: NO LL(1)
- Ejercicio 3: LL(1)
