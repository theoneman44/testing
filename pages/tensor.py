from pages.baseapp import BasePage


class TensorLocators:
    locator_people_power = ('xpath', "//div[contains(@class, 'tensor_ru-Index__block4-content')]")
    locator_link_about = ('xpath', "//div[contains(@class, 'tensor_ru-Index__block4-content')]//a")
    locator_text_work = ('xpath', "//h2[text()='Работаем']")
    locator_image_about = ('xpath', "//div[contains(@class, 'tensor_ru-About__block3-image-wrapper')]//img")


class TensorElementSearch(BasePage):
    def find_people_power(self):
        return self.find_element(TensorLocators.locator_people_power)

    def click_on_the_link_about(self):
        return self.find_element(TensorLocators.locator_link_about).click()

    def find_block_working(self):
        return self.find_element(TensorLocators.locator_text_work)

    def find_grid_of_images(self):
        return self.find_elements(TensorLocators.locator_image_about)
