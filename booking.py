import csv


class Booking:
    all_rooms = []

    def __init__(self, room_id: str, distance: int, status: str):
        # run validations
        assert distance > 0, f"distance {distance} should be greater than zero"

        # assign self object
        self.__room_id = room_id.lower()
        self.__distance = distance
        self.__status = status.lower()

        # actions to execute
        Booking.all_rooms.append([self.__room_id, self.__distance, self.__status])

    @classmethod
    def instantiate_from_csv(cls):
        with open('rooms.csv', 'r') as f:
            reader = csv.DictReader(f)
            rooms = list(reader)

        for room in rooms:
            Booking(
                room_id=room.get('id'),
                distance=int(room.get('distance')),
                status=room.get('status'),
            )

    @classmethod
    def save_to_csv(cls):
        # field names
        fields = ['id', 'distance', 'status']

        # truncate mode
        with open('rooms.csv', 'w+') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(Booking.all_rooms)
            f.close()

    @property
    def room_id(self):
        return self.__room_id

    @property
    def distance(self):
        return self.__distance

    @property
    def status(self):
        return self.__status

    @room_id.setter
    def room_id(self, value):
        self.__room_id = value

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @status.setter
    def status(self, value):
        self.__status = value

    def __repr__(self):
        return self.room_id + " >> " + self.status

    @staticmethod
    def assign_room():
        allocated_room = ""
        sorted_rooms = sorted(filter(lambda x: x[2] == "available", Booking.all_rooms), key=lambda x: x[1])
        if len(sorted_rooms) > 0:
            allocated_room = sorted_rooms[0][0].upper()
            # update room status
            sorted_rooms[0][2] = "occupied"
        else:
            allocated_room = "No Rooms Found"

        return allocated_room

    @staticmethod
    def checkout_room(room_no):
        checkout = False
        for room in Booking.all_rooms:
            if room[0] == room_no.lower() and room[2] == "occupied":
                checkout = True
                room[2] = "vacant"
                print(f"room {room[0].upper()} checked out successfully\n")
                break
        if not checkout:
            print(f"invalid room number {room_no.upper()} provided for checkout\n")

    @staticmethod
    def clean_room(room_no):
        cleaned = False
        for room in Booking.all_rooms:
            if room[0] == room_no.lower() and room[2] == "vacant":
                cleaned = True
                room[2] = "available"
                print(f"room {room[0].upper()} cleaned successfully\n")
                break
        if not cleaned:
            print(f"invalid room number {room_no.upper()} provided for cleaning\n")

    @staticmethod
    def out_of_service(room_no):
        marked_for_repair = False
        for room in Booking.all_rooms:
            if room[0] == room_no.lower() and room[2] == "vacant":
                marked_for_repair = True
                room[2] = "repair"
                print(f"room {room[0].upper()} marked for repair successfully\n")
                break
        if not marked_for_repair:
            print(f"invalid room number {room_no.upper()} provided for repair marking\n")

    @staticmethod
    def repair(room_no):
        repaired = False
        for room in Booking.all_rooms:
            if room[0] == room_no.lower() and room[2] == "repair":
                repaired = True
                room[2] = "vacant"
                print(f"room {room[0].upper()} repaired successfully\n")
                break
        if not repaired:
            print(f"invalid room number {room_no.upper()} provided for repairing\n")

    @staticmethod
    def get_rooms_status():
        for room in Booking.all_rooms:
            print(room[0].upper() + " >> " + room[2])
