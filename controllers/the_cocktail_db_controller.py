import requests


class TheCocktailDbController:
    baseUrl = 'https://www.thecocktaildb.com/'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    def get_a_list_of_cocktails_by_first_letter(self, letter: str) -> (object, dict):
        try:
            url = self.baseUrl + f'api/json/v1/1/search.php?f={letter}'
            response = requests.get(url, headers=self.headers)
            drink_list = response.json()['drinks']
        except requests.exceptions.JSONDecodeError:
            return response
        return response, drink_list
