## 4 Feladat: Műveletek karakterekkel
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Műveletek karakterekkel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Műveletek karakterekkel app tesztelését.
# Az applikáció minden frissítésnél véletlenszerűen változik!
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
driver.get(URL)
time.sleep(5)


def find_loc(id):
    element = driver.find_element_by_id(id)
    return element


def find_res(xpath):
    elemenx = driver.find_element_by_xpath(xpath)
    return elemenx


# teszt adatok
data1 = 'ascii'
data_op = ["+", "-"]


# * Helyesen betöltődik az applikáció:
#     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
def test_true():
    tt = find_res("/html/body/div/div/p[3]")
    assert tt.text == ord()


# * Megjelenik egy érvényes művelet:
#     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     * `op` mező vagy + vagy - karaktert tartlamaz
#     * `num` mező egy egész számot tartalamaz
def test_legal():
    assert find_loc("chr")
    if find_loc("op") == data_op[0]:
        assert find_loc("op") == "+"
    else:
        assert find_loc("op") == data_op[1]
    assert find_loc("num") == int


# * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
#     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
#     * A `num` mezőben megjelenő mennyiségű karaktert
#     * az `result` mező helyes karaktert fog mutatni
def test_button():
    find_loc("submit").click()

