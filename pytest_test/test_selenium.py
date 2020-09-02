# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-19   15:23
# 文件名称    : test_selenium  PY
# 开发工具    : PyCharm


from selenium import webdriver
def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")

if __name__ == "__main__":
    test_selenium()