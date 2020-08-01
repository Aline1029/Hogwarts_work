# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-01   09:55
# 文件名称    : Xuzhu  PY
# 开发工具    : PyCharm

from class_practice.Tianshantonglao import TongLao


class Xuzhu(TongLao):
    def read(self):
        print("罪过罪过")


if __name__ == "__main__":
    xuzhu = Xuzhu(100, 50)
    xuzhu.read()
