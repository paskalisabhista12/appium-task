import unittest
import time
import subprocess
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.example.crudapps',    
    appActivity='com.example.crudapps.MainActivity',
    language='en',
    locale='US'
    # app='/data/app/~~TzVD1aFvS1RD4b0xLZdUpg==/com.example.crudapps-_8AixjA6z7-3PszDfpAguQ==/base.apk'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_add_1(self) -> None:

        print()
        print("=============================================")
        print("[Test Scenario] Success adding book to collection")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/floatingActionButton"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        add_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/floatingActionButton")
        add_button.click()

        # wait until the form is loaded
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/urlkoverBuku"))
            )
        except:
            self.driver.quit()

        # fill url cover input
        url_cover_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/urlkoverBuku")
        url_cover_input.send_keys("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9tMOm_6CzKLtzb161QqKv7_C1wQKD91gfkQ&usqp=CAU")
            
        # fill book name input
        book_name_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/namaBukuEditTextAdd")
        book_name_input.send_keys("Nature Book")

        # fill author input
        author_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/penulisBukuEditTextAdd")
        author_input.send_keys("Author")

        # fill publication year input
        publication_year_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/tahunTerbitEditTextAdd")
        publication_year_input.send_keys("2023")

        # click on the category dropdown
        self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/katergoriAdd").click()
        self.driver.implicitly_wait(1)

        # choose the category
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()

        # click simpan button
        simpan_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/simpanButtonAdd")
        simpan_button.click()

        self.driver.implicitly_wait(2)

        # verify that user currently in the home page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()
        
        home_page_container = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView")
        assert home_page_container.is_displayed()
        
    def test_add_2(self) -> None:

        print()
        print("=============================================")
        print("[Test Scenario] Success adding book with invalid url to collection")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/floatingActionButton"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        add_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/floatingActionButton")
        add_button.click()

        # wait until the form is loaded
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/urlkoverBuku"))
            )
        except:
            self.driver.quit()

        # fill url cover input
        url_cover_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/urlkoverBuku")
        url_cover_input.send_keys("test")
            
        # fill book name input
        book_name_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/namaBukuEditTextAdd")
        book_name_input.send_keys("Number Book")

        # fill author input
        author_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/penulisBukuEditTextAdd")
        author_input.send_keys("Author")

        # fill publication year input
        publication_year_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/tahunTerbitEditTextAdd")
        publication_year_input.send_keys("2023")

        # click on the category dropdown
        self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/katergoriAdd").click()
        self.driver.implicitly_wait(1)

        # choose the category
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()

        # click simpan button
        simpan_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/simpanButtonAdd")
        simpan_button.click()

        self.driver.implicitly_wait(2)

        # verify that user currently in the home page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()
        
        home_page_container = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView")
        assert home_page_container.is_displayed()

    def test_add_3(self) -> None:

        print()
        print("=============================================")
        print("[Test Scenario] Failed to add book to the collection because missing input")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/floatingActionButton"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        add_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/floatingActionButton")
        add_button.click()

        # wait until the form is loaded
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/urlkoverBuku"))
            )
        except:
            self.driver.quit()

        # fill url cover input
        url_cover_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/urlkoverBuku")
        url_cover_input.send_keys("test")
            
        # fill book name input
        book_name_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/namaBukuEditTextAdd")
        book_name_input.send_keys("Number Book")

        # fill publication year input
        publication_year_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/tahunTerbitEditTextAdd")
        publication_year_input.send_keys("2023")

        # click on the category dropdown
        self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/katergoriAdd").click()
        self.driver.implicitly_wait(1)

        # choose the category
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()

        # click simpan button
        simpan_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/simpanButtonAdd")
        simpan_button.click()

        self.driver.implicitly_wait(2)

        # verify the toast message
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.Toast)[1]"))
            )
        except:
            self.driver.quit()
        
        toast = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Toast)[1]")
        assert "Semua data harus diisi" in toast.get_attribute("text")
        
    def test_view_book_info(self) -> None:

        print()
        print("=============================================")
        print("[Test Scenario] View book information")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        book_cards = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView").find_elements(AppiumBy.ID, "com.example.crudapps:id/activity_home")
        
        for card in book_cards:
            book_title = card.find_element(AppiumBy.ID, "com.example.crudapps:id/judulBuku").get_attribute("text")
            card.click()
            toast = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Toast)[1]")     
            assert book_title in toast.get_attribute("text")
            self.driver.implicitly_wait(1)
            self.driver.back()

    def test_update_1(self) -> None:
        print()
        print("=============================================")
        print("[Test Scenario] Success to edit book")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        card = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView").find_element(AppiumBy.ID, "com.example.crudapps:id/activity_home")
        card.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/btnUpadte"))
            )
        except:
            self.driver.quit()

        # click update button
        update_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/btnUpadte")
        update_button.click()

        # fill url cover input
        url_cover_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/urlCoverBukuUpdate")
        url_cover_input.clear()
        url_cover_input.send_keys("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Altja_j%C3%B5gi_Lahemaal.jpg/1200px-Altja_j%C3%B5gi_Lahemaal.jpg")
            
        # fill author input
        author_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/penulisBukuUpdate")
        author_input.clear()
        author_input.send_keys("Author 2")

        # fill publication year input
        publication_year_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/tahunTerbitUpdate")
        publication_year_input.clear()
        publication_year_input.send_keys("2023")

        # click on the category dropdown
        self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/katergoriUpdate").click()
        self.driver.implicitly_wait(1)

        # choose the category
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()

        # click simpan button
        simpan_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/simpanButtonUpdate")
        simpan_button.click()

        self.driver.implicitly_wait(2)

        # verify that user currently in the home page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/action_bar_root"))
            )
        except:
            self.driver.quit()
        
        detail_page_container = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/action_bar_root")
        assert detail_page_container.is_displayed()       

    def test_update_2(self) -> None:
        print()
        print("=============================================")
        print("[Test Scenario] Success to edit book with invalid url")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        card = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView").find_element(AppiumBy.ID, "com.example.crudapps:id/activity_home")
        card.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/btnUpadte"))
            )
        except:
            self.driver.quit()

        # click update button
        update_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/btnUpadte")
        update_button.click()

        # fill url cover input
        url_cover_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/urlCoverBukuUpdate")
        url_cover_input.clear()
        url_cover_input.send_keys("test")
            
        # fill author input
        author_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/penulisBukuUpdate")
        author_input.clear()
        author_input.send_keys("Author 2")

        # fill publication year input
        publication_year_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/tahunTerbitUpdate")
        publication_year_input.clear()
        publication_year_input.send_keys("2023")

        # click on the category dropdown
        self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/katergoriUpdate").click()
        self.driver.implicitly_wait(1)

        # choose the category
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()

        # click simpan button
        simpan_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/simpanButtonUpdate")
        simpan_button.click()

        self.driver.implicitly_wait(2)

        # verify that user currently in the home page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/action_bar_root"))
            )
        except:
            self.driver.quit()
        
        detail_page_container = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/action_bar_root")
        assert detail_page_container.is_displayed()

    def test_update_3(self) -> None:
        print()
        print("=============================================")
        print("[Test Scenario] Failed to edit book because missing input")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        card = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView").find_element(AppiumBy.ID, "com.example.crudapps:id/activity_home")
        card.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/btnUpadte"))
            )
        except:
            self.driver.quit()

        # click update button
        update_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/btnUpadte")
        update_button.click()

        # fill url cover input
        url_cover_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/urlCoverBukuUpdate")
        url_cover_input.clear()
        url_cover_input.send_keys("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Altja_j%C3%B5gi_Lahemaal.jpg/1200px-Altja_j%C3%B5gi_Lahemaal.jpg")

        
        # clear author input
        author_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/penulisBukuUpdate")
        author_input.clear()
        
        # fill publication year input
        publication_year_input = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/tahunTerbitUpdate")
        publication_year_input.clear()
        publication_year_input.send_keys("2023")

        # click on the category dropdown
        self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/katergoriUpdate").click()
        self.driver.implicitly_wait(1)

        # choose the category
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()

        # click simpan button
        simpan_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/simpanButtonUpdate")
        simpan_button.click()

        self.driver.implicitly_wait(2)

        # verify the toast message
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.Toast)[1]"))
            )
        except:
            self.driver.quit()
        
        toast = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Toast)[1]")
        assert "Semua data harus diisi" in toast.get_attribute("text")

    def test_delete(self) -> None:
        print()
        print("=============================================")
        print("[Test Scenario] Success delete book from the collection")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()

        self.driver.implicitly_wait(1)
        card = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView").find_element(AppiumBy.ID, "com.example.crudapps:id/activity_home")
        card.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/btnUpadte"))
            )
        except:
            self.driver.quit()

        # click delete button
        update_button = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/btnDelete")
        update_button.click()

        # verify that user currently in the home page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.example.crudapps:id/homeRecycleView"))
            )
        except:
            self.driver.quit()
        
        home_page_container = self.driver.find_element(AppiumBy.ID, "com.example.crudapps:id/homeRecycleView")
        assert home_page_container.is_displayed()
 

if __name__ == '__main__':
    unittest.main()