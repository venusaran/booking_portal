from booking import Booking

if __name__ == '__main__':
    # load data from csv
    Booking.instantiate_from_csv()

    print(
        '''
            ====================================================
            |                                                  |
            |                                                  |
            |                   Geek Hotel                     |
            |                     ******                       |
            |          Please Select the Operation Below       |
            |          1. CHECK-IN                             |
            |          2. CHECK-OUT                            |
            |          3. CLEAN ROOM                           |
            |          4. MAKE ROOM OUT OF SERVICE             |
            |          5. REPAIR                               | 
            |          6. CHECK ROOMS STATUS                   | 
            |          7. EXIT                                 | 
            |                                                  | 
            ====================================================
            '''
    )

    session = True
    num = 0
    while session:
        try:
            num = int(input("PLEASE ENTER YOUR COMMAND NUMBER> "))
        except ValueError:
            pass
        if num == 1:
            print("You have selected CHECK-IN, Please wait for results")
            room = Booking.assign_room()
            print(f"Room Assignment Results: {room}\n")
            continue
        elif num == 2:
            print("You have selected CHECK-OUT")
            room_no = input("PLEASE ENTER YOUR ROOM NUMBER TO CHECK-OUT: \n")
            Booking.checkout_room(room_no)
            continue
        elif num == 3:
            print("You have selected CLEAN ROOM")
            room_no = input("PLEASE ENTER YOUR ROOM NUMBER: \n")
            Booking.clean_room(room_no)
            continue
        elif num == 4:
            print("You have selected MAKE ROOM OUT OF SERVICE")
            room_no = input("PLEASE ENTER YOUR ROOM NUMBER: \n")
            Booking.out_of_service(room_no)
            continue
        elif num == 5:
            print("You have selected REPAIR")
            room_no = input("PLEASE ENTER YOUR ROOM NUMBER: \n")
            Booking.repair(room_no)
            continue
        elif num == 6:
            print("You have selected CHECK ROOMS STATUS\n")
            Booking.get_rooms_status()
            continue
        elif num == 7:
            print("You have selected EXIT...EXITING AND SAVING THE CURRENT STATE TO CSV FILE....\n")
            Booking.save_to_csv()
            session = False
            continue
        else:
            print("Invalid Entry...Try Again\n")
            continue
