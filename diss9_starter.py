from bs4 import BeautifulSoup
import requests
import unittest

# Task 2: Get the URL that links to list of American universities with Olympic medal wins. 
# The clickable link can be found near the end of the introduction of the University of Michigan page.
def get_link(soup):
    # YOUR CODE HERE

    # HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
    pass

# Task 3: Get the details of the table 
# in the section titled "Organization and administration" in the University of Michigan Wikipedia page. 
# Get all the college/school names and the year they were founded 
# and organize that information into key-value pairs of a dictionary.
def get_school_founded_year(soup):
    # YOUR CODE HERE
    pass



def main():
    # Task 1: Create a BeautifulSoup object. Refer to discussion slides or lecture slides to complete this

    # YOUR CODE HERE

    # print(get_link(soup))
    # print(get_school_founded_year(soup))
    pass

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_get_link(self):
        self.assertEqual(get_link(self.soup), 'https://en.wikipedia.org/wiki/List_of_American_universities_with_Olympic_medals')

    def test_get_school_founded_year(self):
        self.assertEqual(get_school_founded_year(self.soup)['Information'], "1969")

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)