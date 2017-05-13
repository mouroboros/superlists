from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os, unittest

class NewVisitorTest (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new to-do app she goes to check out
        # the webpage
        
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #enter to do list straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        
        #she types "buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        # when she hits enter, the page updates
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        
        #still text box for new items
        self.fail('Finish the test!')
        #site has generated unique url
        #url has persistance
        #satisfied she goes to sleep

if __name__ == '__main__':
    unittest.main()
