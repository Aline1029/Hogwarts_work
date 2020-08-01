# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-01   09:55
# 文件名称    : Xuzhu  PY
# 开发工具    : PyCharm

# 模块化思想，从隔壁模块中导入类
from class_practice.Tianshantonglao import TongLao

# 构造Xuzhu类，继承自TongLao
class Xuzhu(TongLao):
    # 添加独有的念经方法
    def read(self):
        print("罪过罪过")

# 实例化
if __name__ == "__main__":
    xuzhu = Xuzhu(100, 50)
    xuzhu.read()
