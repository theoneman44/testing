import time
from pages.sbis import SbisElementSearch


def test_tensor_change_region(browser):
    sbis_page = SbisElementSearch(browser)
    sbis_page.go_to_site()
    time.sleep(1)
    sbis_page.click_on_the_contacts()

    region = sbis_page.find_region_text()
    assert region.text == 'Омская обл.'  # Проверка домашнего региона(мой браузер из за провайдера думает что я в Омске)

    contact_list = sbis_page.find_contact_list()
    assert len(contact_list) > 0  # Проверка на присутствие списка партнеров

    sbis_page.click_region()
    time.sleep(1)

    sbis_page.click_new_region()
    time.sleep(1)
    assert region.text == 'Камчатский край'  # Проверка смены региона

    contact_list_city = sbis_page.find_contacts_list_city()
    assert contact_list_city.text == 'Петропавловск-Камчатский'  # Проверка смены региона
    assert '41-kamchatskij-kraj' in browser.current_url  # Проверка смены региона
    assert 'Камчатский край' in browser.title  # Проверка смены региона
