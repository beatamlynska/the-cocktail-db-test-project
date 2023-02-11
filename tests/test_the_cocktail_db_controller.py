import requests
from controllers.the_cocktail_db_controller import TheCocktailDbController
import pytest


class TestTheCocktailDbController:
    controller = TheCocktailDbController()

    # Positive case - drinks are returned
    def test_when_drink_for_given_letter_exists_then_returns_only_list_of_drinks_start_with_this_letter(self):
        drink_list = self.controller.get_a_list_of_cocktails_by_first_letter('a')

        for item in drink_list:
            drink_name = item['strDrink']
            assert drink_name[0].lower().startswith("a")

    # Positive case - empty response excepted
    def test_when_drink_for_given_letter_does_not_exist_then_return_null_in_drinks_list(self):
        drink_list = self.controller.get_a_list_of_cocktails_by_first_letter('x')

        assert drink_list is None

    # Negative case - exception expected, status code should not be 200.
    def test_when_get_drink_for_given_letter_with_incorrect_input_then_response_is_empty(self):
        response = self.controller.get_response_from_get_a_list_of_cocktails_by_first_letter_endpoint('ax')

        # This assertion make sense only if we expecting no json in response. This should be clarified.
        with pytest.raises(requests.exceptions.JSONDecodeError):
            response.json()

        # In this assertion, we expecting that response code for incorrect input should not be 200.
        assert response.status_code is not 200

