## 1 Feladat: Pitagorasz-tétel
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Pitagorasz-tétel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
driver.get(URL)
time.sleep(5)

# teszt adatok
data1 = [{"a": ""}, {"b": ""}]
data2 = [{"a": 2}, {"b": 3}, {"c": 10}]
data3 = [{"a": ""}, {"b": ""}, {"c": "NaN"}]


def find_loc(id):
    element = driver.find_element_by_id(id)
    return element


def find_res(xpath):
    elemenx = driver.find_element_by_xpath(xpath)
    return elemenx


# Helyesen jelenik meg az applikáció betöltéskor:
# *a: < üres >
# *b: < üres >
# *c: < nem látszik >
def test_input():
    assert find_loc("a").text == str(data1[0]["a"])
    assert find_loc("b").text == str(data1[1]["b"])
    assert not find_res('//*[@id="results"]/p').is_displayed()


# *Számítás helyes, megfelelő bemenettel
# *a: 2
# *b: 3
# *c: 10
def test_trueinput():
    find_loc("a").send_keys(data2[0]["a"])
    find_loc("b").send_keys(data2[1]["b"])
    find_loc("submit").click()
    time.sleep(10)
    assert find_loc("result").text == str(data2[2]["c"])


#
# # *Üres kitöltés:
# # *a: < üres >
# # *b: < üres >
# # *c: NaN
def test_nullinput():
    driver.get(URL)
    find_loc("submit").click()
    assert find_loc("result").text == data3[2]["c"]
