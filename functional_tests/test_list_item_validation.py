from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Manuel goes to the home page and accidentally tries to submit
        # an empty list item. He hits Enter on the empty input box
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # The home page refershes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
            ))

        # She tries again with some text for the item, which works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversely, he now decides to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # He recieves a similir warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
            ))

        # And he can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')