class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)

        row = []
        for i in range(self.__rows):
            col = []
            for j in range(self.__cols):
                col.append(False)
            row.append(col)
        self.__seats.update({id: row})

    def book_seats(self, customerName, phoneNumber, id, desiredSeats):
        print("-"*80)
        is_show_exists = False
        is_seat_booked = True
        bookedSeat = []

        for show in self.__show_list:
            if id in show:
                is_show_exists = True

                AlreadyBookedSeat = []
                for row, col in desiredSeats:
                    # row, col = desiredSeat
                    if int(row) > int(self.__rows) - 1 or int(col) > int(self.__cols) - 1:
                        print(f'Invalid Seat Entry. Try Again\n')
                        print("-"*80, "\n")
                        return

                    if self.__seats[id][row][col] == True:
                        AlreadyBookedSeat.append(
                            f'{chr(int(row)+65)}{chr(int(col)+48)}')
                        is_seat_booked = False

                    else:
                        self.__seats[id][row][col] = True
                        bookedSeat.append(
                            f'{chr(int(row)+65)}{chr(int(col)+48)}')

                if is_seat_booked == False:
                    for bsa in AlreadyBookedSeat:
                        print(bsa, end=",")
                    print(
                        f' Seat Already Booked')

        if is_show_exists == True and is_seat_booked == True:
            print(
                f'Customer Name : {customerName} \nCustomer Phone Number : {phoneNumber}\n')
            for show in self.__show_list:
                if show[0] == id:
                    print(f'Movie Name : {show[1]}\t\tTime : {show[2]}')
            print(f'Hall : {self.__hall_no}\n')

            for bs in bookedSeat:
                print(bs, end=",")
            print(' Seat Booked Success\n')

        if is_show_exists == False:
            print("Show Doesn't Exist\n")
        print("-"*80, "\n")

    def view_show_list(self):
        print("-"*100, "\n")
        for show in self.__show_list:
            print(
                f'Movie Name: {show[1]}\t\t Show Id: {show[0]}\t\t Time: {show[2]}\n')
        print("-"*100, "\n")

    def view_available_seats(self, id):
        print("-"*70)
        is_Id_exsist = False
        for show in self.__show_list:
            if show[0] == id:
                is_Id_exsist = True
                print(
                    f'Movie Name: {show[1]}\t\tTime: {show[2]}\n')
                print("X for already booked seats")
                break

        if is_Id_exsist == False:
            print("Id Did't Match , Please Enter Correct Id")
            print("-"*70)

        if is_Id_exsist == True:
            print("-"*100)
            for i, row in enumerate(self.__seats[id]):
                print_str = ""
                for j, seat in enumerate(row):
                    if seat == True:
                        print_str += "X\t\t\t"
                    else:
                        print_str += f'{chr(int(i)+65)}{chr(int(j)+48)}\t\t\t'
                print(print_str)
            print("-"*100, "\n")


hall = Hall(4, 5, "nondita-01")
hall.entry_show("a11", "Avatar(The Way of water)", "Dec 10 2022 1:00 PM")
hall.entry_show("b12", "The Pale Blue Eye   ", "Dec 10 2022 4:00 PM")
hall.entry_show("c13", "A Man Called Otto   ", "Dec 10 2022 9:00 PM")

bool = True
while bool:
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")
    option = input("Enter option : ")

    if option == '1':
        hall.view_show_list()

    elif option == '2':
        show_id = input("Enter Show Id : ")
        hall.view_available_seats(show_id)

    elif option == "3":
        customerName = input("Customer Name : ")
        phoneNumber = input("Customer Phone No : ")
        showId = input("Show Id : ")
        totalTicket = int(input("How Many Tickets Do You Want? "))
        desiredSeats = []
        is_valid_seat = True
        for i in range(totalTicket):
            listInfo = input(f'Seat For Ticket Number {i+1} :')
            if len(listInfo) > 2:
                print("-"*40, "\n")
                print("Invalid Seat Entry. Try Again\n")
                is_valid_seat = False
                print("-"*40, "\n")
                break
            else:
                [row, column] = list(listInfo)
                seat = (ord(row)-65, ord(column)-48)
                desiredSeats.append(seat)
        if is_valid_seat == True:
            hall.book_seats(customerName, phoneNumber,
                            showId, desiredSeats)

    elif option == "4":
        bool = False

    else:
        print("\nInvalid Input, Please Enter Correct Input\n")
