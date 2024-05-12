import time
import os
from pages.sbis import SbisElementSearch
from selenium.webdriver.common.action_chains import ActionChains


def test_download_sbis_plugin(browser):
    sbis_page = SbisElementSearch(browser)
    sbis_page.go_to_site()

    footer = sbis_page.find_footer()
    ActionChains(browser).scroll_to_element(footer).perform()

    sbis_page.click_on_download()

    download_list = sbis_page.find_sbis_plugin()
    time.sleep(1)
    download_list[1].click()

    sbis_page.click_download_web_installer()
    time.sleep(5)

    file_plugin_size = os.path.getsize('tests/sbisplugin-setup-web.exe')
    assert file_plugin_size == 7462040  # Проверка размера скачанного файла на соответствие заявленному
