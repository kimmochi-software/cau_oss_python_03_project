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

if __name__ == '__main__':
    print("Testing the module...")
    