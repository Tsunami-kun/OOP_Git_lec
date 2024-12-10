class Student:

    def __init__(self, age: int, name: str, school_name: str, vocal: bool, instrument: str):
        self.age = age
        self.name = name
        self.school_name = school_name
        self.vocal = vocal
        self.instrument = instrument
    def self_introduction(self):
        print(f"大家好，我的名字是 {self.name}，今年 {self.age} 岁，我在 {self.school_name} 学习。")
    def sing(self):
        if self.vocal == True:
            print(f"{self.name} 担任主唱。")
        else:
            pass
    def monologue(self):
        raise NotImplementedError
    def talk(self):
        raise NotImplementedError
    def run(self):
        raise NotImplementedError
    def yell(self):
        raise NotImplementedError
    def play(self):
        print(f"{self.name} 正在用 {self.instrument} 演奏音乐。")

Tomori = Student(age = 16, name = "Takamatsu Tomori", school_name = "羽丘女子学園")
Lena = Student()
Sakiko = Student()
Soyo = Student() 

print(Tomori)
#  <__main__.Student object at 0x00000197797E9040>

Tomori.self_introduction()
# 大家好，我的名字是 Takamatsu Tomori，今年 16 岁，我在 羽丘女子学園 学习。

class mygo_member(Student):
    def is_from_羽丘女子学園(self):
        print(self.school_name=="羽丘女子学園")
class pre_crychic_member(Student):
    def is_from_羽丘女子学園(self):
        print(self.school_name=="羽丘女子学園")

Tomori = mygo_member(age = 16, name = "Takamatsu Tomori", school_name = "羽丘女子学園")
Tomori.is_from_羽丘女子学園()
# True

Tomori = mygo_member(age = 16, name = "Takamatsu Tomori", school_name = "羽丘女子学園", instrument = "Angle iron")
Mutsumi = pre_crychic_member(age = 16, name = "Wakaba Mutsumi", school_name = "月之森女子學園", instrument = "Guitar")

def let_play(student):
    student.play()

let_play(Tomori)
# Takamatsu Tomori 正在用 Angle iron 演奏音乐。
let_play(Mutsumi)
# Wakaba Mutsumi 正在用 Guitar 演奏音乐。


# Tomori.play()
# Takamatsu Tomori 正在用 Angle iron 演奏音乐。
# Mutsumi.play()
# Wakaba Mutsumi 正在用 Guitar 演奏音乐。


# class crychic_member(Student):


Tomori.monologue()
Lena.play()
Sakiko.run()
Soyo.yell()