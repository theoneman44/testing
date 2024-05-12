from pages.baseapp import BasePage


class SbisLocators:
    locator_sbis_contacts = ('class name', 'sbisru-Header__menu-item-1')
    locator_sbis_logo = ('class name', 'sbisru-Contacts__logo-tensor')
    locator_region = ('class name', 'sbis_ru-Region-Chooser__text')
    locator_contact_list = ('class name', 'sbisru-Contacts-List__name')
    locator_new_region = ('xpath', "//div[@name = 'dialog']//span[@title = 'Камчатский край']")
    locator_contacts_list_city = ('class name', 'sbisru-Contacts-List__city')
    locator_footer = ('class name', 'sbisru-Footer')
    locator_download = ('xpath', "//a[text() = 'Скачать локальные версии']")
    locator_sbis_plugin = ('xpath', "//div[@class='controls-tabButton__overlay']")
    locator_download_web_installer = ('xpath', "//a[text() = 'Скачать (Exe 7.12 МБ) ']")


class SbisElementSearch(BasePage):
    def click_on_the_contacts(self):
        return self.find_element(SbisLocators.locator_sbis_contacts).click()

    def click_on_the_logo(self):
        return self.find_element(SbisLocators.locator_sbis_logo).click()

    def go_to_site(self):
        return self.driver.get('https://sbis.ru/')

    def find_region_text(self):
        return self.find_element(SbisLocators.locator_region)

    def find_contact_list(self):
        return self.find_elements(SbisLocators.locator_contact_list)

    def click_region(self):
        return self.find_element(SbisLocators.locator_region).click()

    def click_new_region(self):
        return self.find_element(SbisLocators.locator_new_region).click()

    def find_contacts_list_city(self):
        return self.find_element(SbisLocators.locator_contacts_list_city)

    def find_footer(self):
        return self.find_element(SbisLocators.locator_footer)

    def click_on_download(self):
        return self.find_element(SbisLocators.locator_download).click()

    def find_sbis_plugin(self):
        return self.find_elements(SbisLocators.locator_sbis_plugin)

    def click_download_web_installer(self):
        return self.find_element(SbisLocators.locator_download_web_installer).click()
