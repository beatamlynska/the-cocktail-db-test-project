from typing import Optional

import requests


class TheCocktailDbController:
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self):
        self.base_url = 'https://www.thecocktaildb.com'
        self.get_a_list_of_cocktails_by_first_letter_url = self.base_url + "/api/json/v1/1/search.php?f={}"

    def get_response_from_get_a_list_of_cocktails_by_first_letter_endpoint(self, letter: str):
        response = requests.get(self.get_a_list_of_cocktails_by_first_letter_url.format(letter))
        return response

    def get_a_list_of_cocktails_by_first_letter(self, letter: str) -> Optional[dict]:
        response = self.get_response_from_get_a_list_of_cocktails_by_first_letter_endpoint(letter)
        response.raise_for_status()
        if response.status_code != 200:
            raise ValueError(f"Response status code other than 200!: {response.status_code}")
        drink_list = response.json()['drinks']
        return drink_list

