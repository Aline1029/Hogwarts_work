# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-01   09:54
# 文件名称    : Tianshantonglao  PY
# 开发工具    : PyCharm

class TongLao:
    def __init__(self, hp, power):
        # 添加血量和攻击力属性
        self.hp = hp
        self.power = power
    # 喊人方法
    def see_people(self, name):
        # 喊不同的名字会有不同的执行
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
    # 天山折梅手
    def fight_zms(self, em_hp, em_power):
        # 血量减半， 攻击力提升10倍
        self.hp /= 2
        self.power *= 10
        # 一回合对打
        self.hp -= em_power
        em_hp -= self.power
        # 血量高的获胜， 血量相等平局
        if self.hp > em_hp:
            print("天山童姥获胜！")
        elif self.hp < em_hp:
            print("敌人获胜！")
        else: print("平局")
# 实例化
if __name__ == "__main__":
    tstl = TongLao(1000, 300)
    tstl.see_people("无崖子")
    tstl.fight_zms(500, 400)

