import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Decorator for all tests.
@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    '''
    Provide a selenium webdriver    
    '''
    options = Options()
    # Display test logs?
    options.headless = False
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()