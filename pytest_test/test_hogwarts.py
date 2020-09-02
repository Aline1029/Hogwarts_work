# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-19   15:59
# 文件名称    : test_hogwarts  PY
# 开发工具    : PyCharm
from selenium import webdriver
class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃滋测试学院").click()
        self.driver.