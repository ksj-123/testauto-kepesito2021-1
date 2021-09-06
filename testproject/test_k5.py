## 5 Feladat: Bingo
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Bingo app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Bingoapp tesztelését.
# Az applikáció indulo bingo táblája minden frissítésnél véletlenszerűen változik!
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"
driver.get(URL)
time.sleep(5)

def find_loc(id):
    element = driver.find_element_by_id(id)
    return element


def find_res(xpath):
    elemenx = driver.find_element_by_xpath(xpath)
    return elemenx


# teszt adatok
data_in = ["abcd1234", "teszt233@", "abcd"]
data_out = ["", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]


# * Az applikáció helyesen megjelenik:
#     * A bingo tábla 25 darab cellát tartalmaz
#     * A számlista 75 számot tartalmaz
def test_true():
    find_loc("title").send_keys(data_in[0])



# * Bingo számok ellenőzrzése:
#     * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
#     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki
def test_bingo():
    find_loc("init").click()
    find_loc("spin").click()



# Új játékot tudunk indítani
#     * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#     * új bingo szelvényt kapunk más számokkal.
def test_new():
