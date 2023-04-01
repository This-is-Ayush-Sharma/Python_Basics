class Fruit_Info:
    fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    fruit_prize_list = [ 200, 80, 70, 110, 60]

    def get_fruit_price(self,fruit_name):
        if(fruit_name not in Fruit_Info.fruit_name_list):
            return -1
        else:
            return Fruit_Info.fruit_prize_list[Fruit_Info.fruit_name_list.index(Fruit_Info.fruit_name_list[fruit_name])]


class Purchase(Fruit_Info):
    counter = 101
    def __init__(self, fruit_Name):
        self.fruit_name = fruit_Name

    def calculate_price(self):
        pass
    