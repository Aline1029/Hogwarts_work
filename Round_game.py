# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-07-31   14:27
# 文件名称    : Round_game  PY
# 开发工具    : PyCharm

"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

def fight():
    player1_hp, player2_hp = 1000, 1000
    player1_power, player2_power = 200, 200
    while True:
        player1_hp -= player2_power
        player2_hp -= player1_power
        if player1_hp == 0:
            print("玩家1输了。")
            break
        if player2_hp == 0:
            print("玩家2输了。")
            break

fight()