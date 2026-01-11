#Скалярное произведение векторов a (a1, a2, a3, ...aN) и b (b1, b2, b3, ...bN) определяется с помощью формулы:
#(a,b) = a1*b1 + a2*b2 + a3*b3 + .... aN*bN
#Напишите функцию, которая принимает два вектора - два списка чисел и возвращает скалярное произведение векторов переданных списков.

def scal(vect1, vect2):
    scproduct = 0
    zipobj = zip(vect1, vect2)
    for x in zipobj:
        scproduct = scproduct + x[0]*x[1]
    return scproduct

spis1 = [1, 2, 3, 4]
spis2 = [5, 6, 7, 8]

print(scal(spis1, spis2))