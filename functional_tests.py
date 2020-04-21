from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
#测试类继承unittest.TestCase
class NewVisitorTest(unittest.TestCase):
    #测试之前运行
    def setUp(self):
        self.browser = webdriver.Firefox()

    #测试之后运行
    def tearDown(self):
        self.browser.quit()

    #测试主体，以test开头的任何方法都是测试方法
    def test_can_start_a_list_and_retrieve_it_later(self):
        #check homepage
        self.browser.get('http://localhost:8000')

        #title and header  to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        self.assertIn(
            '2:use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        #无论如何都会失败，产生错误信息
        self.fail('Finish the test')
    
    #程序入口
if __name__ == "__main__":
    unittest.main(warnings = 'ignore')