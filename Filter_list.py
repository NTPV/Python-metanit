# Фильтрация списка

class car:
    def __init__(self, model, ls):
        self.model = model
        self.ls = ls

carlist = [car('ford', 155), car('kia', 140), car('wolkswagen', 144)]

result = filter(lambda carobj: carobj.ls > 142, carlist)

for x in result:
    print(x.model)
