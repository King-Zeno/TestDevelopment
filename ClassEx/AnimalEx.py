import yaml


class Animal:
    name: str = "default"
    color: str = "default"
    age: int = 20
    gender: str = "default"

    def __init__(self, name, gender, age, color):
        # print("start init")
        self.name = name
        self.gender = gender
        self.age = age
        self.color = color
        # print("end init")

    def cry(self):
        print(f"{self.name} could crying")

    def run(self):
        print(f"{self.name} could running")


class Cat(Animal):
    def __init__(self, name, gender, age, color, hair='short hair'):
        # print("start init")
        self.name = name
        self.gender = gender
        self.age = age
        self.color = color
        self.hair = hair

    def catch_mouse(self):
        print(f"Cat {self.name} could catching mouse")

    def cry(self):
        print(f"{self.name} is crying 喵喵叫")


class Dog(Animal):
    def __init__(self, name, gender, age, color, hair='long hair'):
        # print("start init")
        self.name = name
        self.gender = gender
        self.age = age
        self.color = color
        self.hair = hair

    def watch_home(self):
        print(f"Dog {self.name} could watching home")

    def cry(self):
        print(f"{self.name} is crying 汪汪叫")


if __name__ == '__main__':
    with open("Animal.yml") as fc:
        datas = yaml.safe_load(fc)
    cat1 = datas['Cat']
    cat_name = cat1['name']
    cat_gender = cat1['gender']
    cat_age = cat1['age']
    cat_color = cat1['color']
    cat_hair = cat1['hair']
    cat = Cat(cat_name, cat_gender, cat_age, cat_color, cat_hair)
    print(f"{cat.name, cat.color, cat.age, cat.gender, cat.hair} catch mouse successfully")

    with open("Animal.yml") as fd:
        datas = yaml.safe_load(fd)
    dog1 = datas['Dog']
    dog_name = dog1['name']
    dog_gender = dog1['gender']
    dog_age = dog1['age']
    dog_color = dog1['color']
    dog_hair = dog1['hair']
    dog = Dog(dog_name, dog_gender, dog_age, dog_color, dog_hair)
    print(f"{dog.name, dog.color, dog.age, dog.gender, dog.hair}")
# cat = Cat("Tom", "male", 3, "blue", 'short hair')
# cat.catch_mouse()
# print(f"{cat.name, cat.color, cat.age, cat.gender, cat.hair} catch mouse successfully")
#
# dog = Dog("James", "female", 2, "yellow", 'long hair')
# dog.watch_home()
# print(f"{dog.name, dog.color, dog.age, dog.gender, dog.hair}")
