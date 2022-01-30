import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(request):
    print("initiating firefox driver")
    #firefox_profile = webdriver.FirefoxProfile()
    #firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    driver = webdriver.Firefox()
    session = request.node

    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("http://128.232.222.153:8080/")


    yield driver
    driver.close()
