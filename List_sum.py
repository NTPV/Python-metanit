# Напишите функцию, которая принимает два списка и возвращает новый список, в котором каждый элемент представляет сумму соответствующих элементов обоих списков.
def sumlist(list1, list2):

    lsum = []
    zipped = zip(list1, list2)

    for x, y in zipped:
        lsum.append(x + y)

    return lsum

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

lsum = sumlist(list1, list2)
print(lsum)