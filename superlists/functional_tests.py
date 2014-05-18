from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def terDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mr. Badass has heard about a marvelous new online to-do app.
        # he go to check out its homepage
        self.browser.get('http://localhost:8000')

        #He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# He is invited to enter a to-do item straight away

# He type "Be a Badass" into a text box

# When he hits enter, the page updates, and now the page
#lists "1: Be a Badass" as an item in a to do list

 #There is still a text box inviting him to another item.
# He enters "Feed the kitten"

# The page updates again, and now shows both items on his lists

# Mr. Badass wonders whether the site will remember his list.
# Then he sees that the site has generated a unique URL for him

# He visits the URL - His badass to-do list is still there.

# Satisfied, He goes back to sleep
