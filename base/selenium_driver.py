from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
       
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getTableList(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            size = len(elementList)
            self.log.info("Element found with locator: " + locator +
                      " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                      " and  locatorType: " + locatorType)

        return len(elementList)

    def clearFIeld(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            element.clear()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()


    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def elementClear(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("cleared text field with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear text field with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element" + locator)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_located((byType, locator )))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def get_title(self, title):
        try:
            self.driver.title == title
            self.log.info("PASS: Title was found!")
        except:
            self.log.info("FAIL: Title was not found!")
        return True


    def switch_focus(self):
        try:
            self.driver.SwitchTo().Window(self.driver.WindowHandles.Last())
            self.log.info("Focus window has changed")
        except:
            self.log.info("Element is not in page")

    def messageText(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            text = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                      " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                      " and  locatorType: " + locatorType)
        return text.text

    def getValue(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            text = self.driver.find_element(byType, locator)
            my_text = text.text
            self.log.info("Element found with locator: " + locator +
                      " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                      " and  locatorType: " + locatorType)
        return int("".join(filter(str.isdigit,my_text)))



