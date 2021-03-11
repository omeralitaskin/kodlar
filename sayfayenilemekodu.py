import time  #time kütüphanesini içer aktarıyoruz.

from selenium import webdriver #selenyum kütüphanesini içer aktarıyoruz.

driver = webdriver.Chrome()
driver.get("https://www.google.com.tr/") #sürekli yenilemek istediğimiz adresimizi buraya yazıyoruz.
while True:
    driver.refresh()
    time.sleep(10)   #Kaç saniye aralıkla yenilenmesi gerektiğini söylüyoruz.