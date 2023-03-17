class Table:
    def __init__(self):
        self.no_of_legs = 4
        self.glass_top = None
        self.wooden_top = None

dTable = Table()
back_table = Table()

font_table = dTable
back_table = back_table

print(dTable,
      back_table,font_table,back_table)