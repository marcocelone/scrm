from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.amazon.com"
        if self.browser == "chrome":
            # Set ie driver
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "safari":
            # Set chrome driver
            driver = webdriver.Safari()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver