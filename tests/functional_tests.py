from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')
    
    assert 'Django' in browser.title
