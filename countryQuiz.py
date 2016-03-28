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

score = 0

for key, value in countries.iteritems():
    print "Name the capital of", key + " here:  "
    capital = raw_input()
    if capital.capitalize() == value:
        score += 1
        print "Bravo! Now your score is ", score
    else:
        print "You dummy! The capital of", key, "is",value,"!"


print"Your final score is", score




