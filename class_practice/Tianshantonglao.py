# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-01   09:54
# 文件名称    : Tianshantonglao  PY
# 开发工具    : PyCharm

class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self, em_hp, em_power):
        self.hp /= 2
        self.power *= 10
        self.hp -= em_power
        em_hp -= self.power
        if self.hp > em_hp:
            print("天山童姥获胜！")
        elif self.hp < em_hp:
            print("敌人获胜！")
        else: print("平局")
if __name__ == "__main__":
    tstl = TongLao(1000, 300)
    tstl.see_people("无崖子")
    tstl.fight_zms(500, 400)

