## 2 Feladat: Színes reakció
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Színes reakció app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
driver.get(URL)
time.sleep(5)


def find_loc(id):
    element = driver.find_element_by_id(id)
    return element


def st():
    find_loc("start").click()
    time.sleep(5)
    find_loc("stop").click()


rdmcolor = find_loc("randomColor")
testcolor = find_loc("testColor")


# * Helyesen jelenik meg az applikáció betöltéskor:
#  Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#  <szín neve> [     ] == [     ]
def test_start():
    assert rdmcolor.is_enabled()
    assert testcolor.text == '[     ]'


# * El lehet indítani a játékot a `start` gommbal.
#     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
def test_run():
    st()
    assert find_loc("start").is_enabled()
    assert find_loc("stop").is_enabled()


# * Eltaláltam, vagy nem találtam el.
# * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
# amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
# ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
def test_text():
    for i in range(20):
        st()
        if rdmcolor.text == testcolor.text:
            assert find_loc("result").text == "Incorrect!"
        else:
            assert find_loc("result").text == "Correct!"
