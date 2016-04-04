countries = {
    'Slovenia': 'Ljubljana',
    'Finland': 'Helsinki',
    'Uganda': 'Kampala',
    'Italy' : 'Rome',
    'Germany' : 'Berlin',
    'Myanmar' : 'Naypyidaw',
    'Vietnam' : 'Hanoi',
    'Canada' : 'Ottawa',
    'Brunei' : 'Bandar Seri Begawan',
    'Malaysia' : 'Kuala Lumpur'
}


def prestolnica(country_search):
    for country, capital in countries.iteritems():
        if country_search == country:
            return capital


def check(capital_search, country_search):
    if capital_search == prestolnica(country_search):
        print "Pravilno"
    else:
        print "Nepravilno"

country = raw_input("Type country: ").capitalize()
capital = raw_input("Type capital: ").capitalize()
check(capital, country)





