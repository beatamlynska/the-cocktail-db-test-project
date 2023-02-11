import requests


class TheCocktailDbController:
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self):
        self.base_url = 'https://www.thecocktaildb.com'
        self.get_a_list_of_cocktails_by_first_letter_url = self.base_url + "/api/json/v1/1/search.php?f={}"

    def get_response_from_get_a_list_of_cocktails_by_first_letter_endpoint(self, letter: str):
        response = requests.get(self.get_a_list_of_cocktails_by_first_letter_url.format(letter))
        return response

    def get_a_list_of_cocktails_by_first_letter(self, letter: str) -> dict:
        response = self.get_response_from_get_a_list_of_cocktails_by_first_letter_endpoint(letter)
        if response.status_code == 200:
            drink_list = response.json()['drinks']
            return drink_list
        else:
            print("Something went wrong!")

