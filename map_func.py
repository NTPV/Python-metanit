class furniture:
    def __init__(self, title, material, price):
        self.title = title
        self.material = material
        self.price = price
        self.description = None


def filldescription(furnitureobj):
    furnitureobj.description = f'Объект: {furnitureobj.title},материал: {furnitureobj.material}, цена: {furnitureobj.price}$'
    return furnitureobj


furniturelist = [furniture('chair','wood', 100),
                 furniture('table', 'wood', 250),
                 furniture('bed', 'textile', 300)]


result = map(filldescription, furniturelist)

for x in result:
    print(x.description)