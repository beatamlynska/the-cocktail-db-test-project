import requests
from controllers.the_cocktail_db_controller import TheCocktailDbController
import pytest


class TestTheCocktailDbController:
    controller = TheCocktailDbController()

    # Positive case, drinks are returned
    def test_when_drink_for_given_letter_exists_then_return_list_of_drinks(self):
        response, drink_list = self.controller.get_a_list_of_cocktails_by_first_letter('a')

        # This condition is checking if all drinks started on 'a' letter
        for item in drink_list:
            drink_name = item['strDrink']
            assert drink_name[0].lower().startswith("a")

        # This condition is checking if response code is as expected
        assert response.status_code == 200

    # Positive Case, but empty response excepted
    def test_when_drink_for_given_letter_does_not_exist_then_return_null_in_drinks_list(self):
        response, drink_list = self.controller.get_a_list_of_cocktails_by_first_letter('x')

        # assertion for response: {"drinks":null}
        assert drink_list is None

        # This condition is checking if response code is as expected
        assert response.status_code == 200

    # Negative case, exception expected
    def test_when_get_drink_for_given_letter_with_incorrect_input_then_response_is_empty(self):
        response = self.controller.get_a_list_of_cocktails_by_first_letter('ax')

        # We excepting error here, because this response does not return any json object.
        with pytest.raises(requests.exceptions.JSONDecodeError):
            response.json()

        # This condition is checking if response code is as expected
        assert response.status_code == 200

