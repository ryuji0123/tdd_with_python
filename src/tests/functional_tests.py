import os
import unittest
from logging import basicConfig, getLogger, INFO

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('django', self.browser.title)


if __name__ == '__main__':
    basicConfig()
    logger = getLogger(__name__)
    logger.setLevel(INFO)

    unittest.main(warnings='ignore')
    
    # if 'Django' in browser.title:
    #     logger.info('ok')
    # else:
    #     logger.info('oh...')
