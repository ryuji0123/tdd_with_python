import os
from logging import basicConfig, getLogger, INFO

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


if __name__ == '__main__':
    basicConfig()
    logger = getLogger(__name__)
    logger.setLevel(INFO)
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')
    
    if 'Django' in browser.title:
        logger.info('ok')
    else:
        logger.info('oh...')
