#Common Sequence Operations
#Общие последовательные операции

string = 'abcqwerty123qs45q3'

a = ('qwe' in string) #True
a = ('qwe' not in string) #False
a  = 'hi ' + string # 'hi abcqwerty123qs45q3'

a = string[2] # 'c " (индекс с номером 2)
a = string[0] # 'a' (индекс с номером 0)
a = string[-0] # 'a' (индекс с номером 0 так же)
a = string[-2] # 'q' (второй элемент с конца
a = string[-5] # 's'

# Нарезка
a = string[3:9] # 'qwerty'
#Нарезка с шагом (2 и 3)
a = string[3:9:2] # 'qet'
a = string[3:9:3] # 'qr'
a = string[3:-0] # ''
a = string[3:0] # ''
a = string[3:-1] # 'qwerty123qs45q'
a = string[-5:-3] # 's4'


a = len(string) # 18
a = min(string) # '1'
a = max(string) # 'y'

# s.index(x[, i[, j]])
# индекс первого вхождения x в s
# (или после индекса i и до индекса j)
a = string.index('ty') # 7
a = string.index('q') # 3
a = string.index('q', 5) # 12 (первое вхождение начиная от 5го индекса)
a = string.index('q', 14, 17) # 16 (первое вхождение на отрезке от 14 до 17 индекса)
a = string.count('q') # 3

a = string * 3 # 'abcqwerty123qs45q3abcqwerty123qs45q3abcqwerty123qs45q3'
