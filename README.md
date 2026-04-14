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

## Conclusion

La gramatica SI es LL(1).

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

## Conclusion

La gramatica NO es LL(1) debido a conflictos en prediccion.

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

## Conclusion

La gramatica SI es LL(1).

---

# Resumen de ejercicios

- Ejercicio 1: LL(1)
- Ejercicio 2: NO LL(1)
- Ejercicio 3: LL(1)
