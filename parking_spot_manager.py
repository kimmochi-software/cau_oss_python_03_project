class parking_spot:
     
    def __init__(self, name, city, district, ptype, longitude, latitude): # 생성자
        self.__item = {
            'name': name,
            'city': city,
            'district': district,
            'ptype': ptype,
            'longitude': longitude,
            'latitude': latitude
        }

    def get(self, keyword='name'): # get 메서드
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s


def str_list_to_class_list(str_list): #
        class_list = []
        for item in str_list:
            data = item.split(',')
            name = data[1]
            city = data[2]
            district = data[3]
            ptype = data[4]
            longitude = data[5]
            latitude = data[6]
            spot = parking_spot(name, city, district, ptype, longitude, latitude)
            class_list.append(spot)
        return class_list


def print_spots(spots):
    length = len(spots)
    print(f"---print elements({length})---")
    for spot in spots:
        print(spot)

def filter_by_name(spots, name): # filter_by_name 함수
    return [spot for spot in spots if name.lower() in spot.get('name').lower()]

def filter_by_city(spots, city): # filter_by_city 함수
    return [spot for spot in spots if city.lower() in spot.get('city').lower()]

def filter_by_district(spots, district): # filter_by_district 함수
    return [spot for spot in spots if district.lower() in spot.get('district').lower()]

def filter_by_ptype(spots, ptype): # filter_by_ptype 함수
    return [spot for spot in spots if ptype.lower() in spot.get('ptype').lower()]

def filter_by_location(spots, locations): # filter_by_location 함수
    min_lat, max_lat, min_long, max_long = locations
    return [
        spot for spot in spots
        if float(min_lat) <= float(spot.get('latitude')) <= float(max_lat)
        and float(min_long) <= float(spot.get('longitude')) <= float(max_long)
    ]

def sort_by_keyword(spots, keyword): # filter_by_keyword 
    return sorted(spots, key=lambda spot: spot.get(keyword))

if __name__ == '__main__':
    print("Testing the module...")
    