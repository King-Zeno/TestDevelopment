

class Bycycle:
    def run(self, km):
        print(f"骑行的里程数为: {km} km")

class EBicycle(Bycycle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        print(f"充电:{vol}")

    def run(self, km):
        max_mile = self.battery_level * 10
        level_mile = km -max_mile

        if level_mile > 0:
            print(f"已经使用电量骑行的里程数:{max_mile} km")
            super().run(level_mile)

        else:
            print(f"骑行的里程数：{km}")

myebycile = EBicycle(20)
myebycile.run(300)