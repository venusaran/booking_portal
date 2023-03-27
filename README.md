# booking_portal
Application to manage and modify the hotel booking stages based on the room availability

## Requirements
This module requires no modules outside Python3.

## Functionalities
1) Can import available rooms, distance from the entrance to the room and status of the room in a CSV file
2) Check-In a room(Rooms will be assigned by checking the availability and shortest distance from entrance)
3) Checkout a room by providing a room number
4) Clean a room by providing room number
5) Mark a room as OUT OF SERVICE by providing number
6) Repair a room by proving a room number
7) Check all rooms status as a list
8) Exit from the program
9) Save last state of the rooms in CSV when exiting the program via command 7, and load it again when program starts

## Validations
1) Commands should be integers from 1 to 7, any other inputs will be considered as invalid
2) Inputs are not case-sensitive( 1A and 1a will be considered as same)
3) If the execution of the program killed or interrupted, the last known state will be fetched from the csv

## Execute
cd /booking_portal

python main.py
