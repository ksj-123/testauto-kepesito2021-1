## 3 Feladat: Alfanumerikus mező
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Alfanumerikus mezőapp-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Alfanumerikus mező app tesztelését.
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
driver.get(URL)
time.sleep(5)


def find_loc(id):
    element = driver.find_element_by_id(id)
    return element


def find_span(tagname):
    elemens = driver.find_element_by_tag_name(tagname)
    return elemens


# teszt adatok
data_in = ["abcd1234", "teszt233@", "abcd"]
data_out = ["", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]


# * Helyes kitöltés esete:
#     * title: abcd1234
#     * Nincs validációs hibazüzenet
def test_true():
    find_loc("title").send_keys(data_in[0])
    assert find_span("span").text == data_out[0]


# * Illegális karakterek esete:
#     * title: teszt233@
#     * Only a-z and 0-9 characters allowed.
def test_ill():
    find_loc("title").clear()
    find_loc("title").send_keys(data_in[1])
    assert find_span("span").text == data_out[1]


# * Tul rövid bemenet esete:
#     * title: abcd
#     * Title should be at least 8 characters; you entered 4.
def test_short():
    find_loc("title").clear()
    find_loc("title").send_keys(data_in[2])
    assert find_span("span").text == data_out[2]
