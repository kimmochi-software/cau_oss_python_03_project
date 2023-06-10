import file_manager
import parking_spot_manager

def start_process(path):

    spots = []
    str_list = file_manager.read_file(path)  # 파일을 읽어와 문자열 리스트 반환
    spots = parking_spot_manager.str_list_to_class_list(str_list)  # parking_spot 객체 리스트 생성

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)  # 객체 리스트 출력
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword) # filter_by_name 호출
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword) # filter_by_city 호출
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword) # filter_by_district 호출
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword) # filter_by_ptype 호출
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations) # filter_by_location 호출
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit") # 4번을 선택하면 Exit을 출력하고 반복을 종료
            break
        else:
            print("invalid input")