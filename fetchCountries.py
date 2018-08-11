
countries = []

def getCountries():
    global countries

    with open('countries.txt', 'r') as f:
        for line in f:
            countries.append(line.replace('\n',''))
    return countries
