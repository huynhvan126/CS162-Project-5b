# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/30/2024
# Description: Write a class named NobelData that read JSON file, and allows the user to search that data.
import json

class NobelData:
    """
    A class to handle data on Nobel Prize winners, allowing users to search for laureates by year and category.
    """
    def __init__(self):
        """
        Initialize the NobelData class.
        """
        with open('nobels.json', 'r') as file:
            self._data = json.load(file)

    def search_nobel(self, year: str, category: str) ->list:
        """
        Searching for Nobel Prize laureates by year and category, returning a sorted list of laureate surnames.
        """
        surnames = []
        for prize in self._data['prizes']:
            if prize['year'] == year and prize['category'] == category:
                for laureate in prize.get('laureates', []):
                    if 'surname' in laureate:
                        surnames.append(laureate['surname'])
                break
        return sorted(surnames)