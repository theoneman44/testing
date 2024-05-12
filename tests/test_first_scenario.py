import time
from pages.sbis import SbisElementSearch
from pages.tensor import TensorElementSearch
from selenium.webdriver.common.action_chains import ActionChains


def test_tensor_pages(browser):
    sbis_page = SbisElementSearch(browser)
    sbis_page.go_to_site()
    time.sleep(1)
    sbis_page.click_on_the_contacts()
    sbis_page.click_on_the_logo()
    time.sleep(1)
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])

    tensor_page = TensorElementSearch(browser)
    people_power = tensor_page.find_people_power()
    assert 'Сила в людях' in people_power.text  # Проверка что есть блок сила в людях

    ActionChains(browser).scroll_to_element(people_power).perform()
    time.sleep(1)
    tensor_page.click_on_the_link_about()

    block_working = tensor_page.find_block_working()
    ActionChains(browser).scroll_to_element(block_working).perform()
    time.sleep(1)
    grid = tensor_page.find_grid_of_images()
    grid_width = grid[0].get_attribute('width')
    count = 1
    for g in range(1, len(grid)):
        grid_width = grid[0].get_attribute('width')
        grid_height = grid[0].get_attribute('height')
        if grid[g].get_attribute('width') == grid_width and grid[g].get_attribute('height') == grid_height:
            count += 1
    assert browser.current_url == 'https://tensor.ru/about'  # Проверка открытия нужной страницы
    assert count == len(grid)  # Проверка на одинаковые размеры фото
