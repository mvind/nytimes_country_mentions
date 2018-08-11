from bs4 import BeautifulSoup
from fetchCountries import getCountries
import requests

countries = []

def main():
    # Request
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    # Parsing
    soup = BeautifulSoup(r_html, 'html.parser') # Create nested html object
    headlines = soup.find_all('h2','story-heading')

    # Get the text from each tag.
    results = {}
    for line in headlines:
        line = (line.text).strip()
        res = titlecountryscan(line, countries)
        results[res] = results.get(res,0) +1

    # Remove no hits
    del results['x']
    print(results)




def titlecountryscan(title, countries):
    "Determines wether a country is in a title"
    match = 0.75
    # Clean up title
    title = title.upper()
    title = title.replace(',', '')
    title = title.replace('\’', '')
    title = title.replace('.', '')
    title = title.replace('?', '')

    for country in countries:
        res = {}
        w = country.upper()
        if containword(title,w):
            return w

    return 'x'

def containword(s,w):
    "Checkes wether a string determines a word"
    return f' {w} '  in f' {s} '


if __name__ == '__main__':
    countries = getCountries() # Import all the countries in the world in a list

    main()
