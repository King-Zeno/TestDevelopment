class Person:
    name: str = "default"
    gender: str = "default"
    age: int = 20
    __money: float = 1000

    # def set_name(self, name):
    #     self.name = name
    def __init__(self, name, gender, age, money):
        # print("start init")
        self.name = name
        self.gender = gender
        self.age = age
        self.money = money
        # print("end init")

    @classmethod
    def classmethod(cls):
        pass

    # 调用私有变量
    def get_money(self):
        return self.__money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

    # 私有方法
    def __make_money(self):
        print(f"{self.name} could make money")


class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is very funney")


class SingerMan(Person):
    def make_money(self, moneynum: str):
        print((f"{self.name} could make money {moneynum}"))


class Chengxuyuan(Person):
    def write_code(a):
        print(f"{a.name} could write code")

    @classmethod
    def zhengshu(self):
        print("我有证书")


gezishan = Chengxuyuan('tom', '男', 30, 100000)
gezishan.write_code()
# gezishan.zhengshu()
Chengxuyuan.zhengshu()

# singer = SingerMan('jerry', '男', 28, 1000)
# singer.make_money('10W')

# funneyman = FunnyMan('st', "男", 30, 20000)
# print(funneyman.name)
# funneyman.eat()
# funneyman.fun()
#
# p = Person("lili", "女", 18, 1000)
# print(p.name)
# p.eat()
# p.make_money()
# print(p.get_money())
# p._Person__make_money()
# print(p._Person__money)
# print(dir(p))
