from selenium import webdriver
import unittest
#测试类继承unittest.TestCase
class NewVisitorTest(unittest.TestCase):
    #测试之前运行
    def setUp(self):
        browser = webdriver.Firefox()

    #测试之后运行
    def tearDown(self):
        self.browser.quit()

    #测试主体，以test开头的任何方法都是测试方法
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        #无论如何都会失败，产生错误信息
        self.fail('Finish the test')
    
    #程序入口
    if __name__ == "__main__":
        unittest.main(warnings = 'ignore')