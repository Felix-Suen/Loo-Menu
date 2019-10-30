from uwaterlooapi import UWaterlooAPI

if __name__ == '__main__':
    uw = UWaterlooAPI(api_key="7d0e829ff82a1aa902f44d6609a1cbb2")
    places = uw.menu()

    lunches = places['outlets'][0]['menu'][0]['meals']['lunch'][0]['product_name']
    print(lunches)

    lunch = places['outlets'][1]['menu'][0]['meals']['dinner'][0]['product_name']
    print(lunch)

    locations = places['outlets'][0]
    print("\n" + locations['outlet_name'] + ": ")
    dates = locations['menu']
    for date in dates:
        print(" - " + date['date'])
        if date['meals']['lunch']:
            lunches = date['meals']['lunch']
            for lunch in lunches:
                print('    + ' + lunch['product_name'])

    locations = places['outlets'][1]
    print("\n" + locations['outlet_name'] + ": ")
    dates = locations['menu']
    for date in dates:
        print(" - " + date['date'])
        dinners = date['meals']['dinner']
        for dinner in dinners:
            print('    + ' + dinner['product_name'])
