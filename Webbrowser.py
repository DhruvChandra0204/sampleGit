from selenium import webdriver

class myclass:
    def func(self):
        Address = r'C:\Users\Dhruv\Documents\chromedriver_win32\chromedriver.exe'

        driver = webdriver.Chrome(executable_path=Address)
        driver.get("https://www.facebook.com")

obj = myclass()
obj.func()








