class parking_lot:
    def __init__(self):
        pass
    def create_parking_lot(self,size):
        
        for i in range(1,size+1):
            lot[i]=("empty slot".split())
        print("Created a parking lot with ", size, "slots")
    
    def park(self,vehicle_detail):
        for i in range(1,size+1):
            if lot[i]==['empty', 'slot']:
                lot[i]=vehicle_detail.split()
                print("Allocated slot number:",i)
                break
        else:
            print("Sorry, parking lot is full ")
        
    
    def leave(self,slot_no):
        for i in range(1,size+1):
            if i==slot_no:
                lot[i]=['empty', 'slot']
                print("Slot number", i, "is free ")
               #print(lot)
                break
    
    def status(self):
        print("Slot No. RegistrationNo Colour") 
        for i in range(1,size+1):
            print(i,lot[i][0],lot[i][1])

    def registration_numbers_for_cars_with_colour(self,colour):
        for i in range(1,size+1):
            if lot[i][1]==colour:
                print(lot[i][0],end=', ')
        print()

    def slot_numbers_for_cars_with_colour(self,colour):
        for i in range(1,size+1):
            if lot[i][1]==colour:
                print(i,end=', ') 
        print()
        
    def slot_number_for_registration_number(self,regist_no):
        for i in range(1,size+1):
            if lot[i][0]==regist_no:
                print(i)
                break
        else:
            print("Not found")


    def control(self,user_input):
        user_input=user_input.split()
        
        
        if "create_parking_lot" in user_input:
            
            global size
            size=int(user_input[-1])
            parking.create_parking_lot(size)
        
        
        if "park" in user_input:
            
            vehicle_detail= user_input[1]+" "+user_input[2]
            
            parking.park(vehicle_detail)


        if "leave" in user_input:
            
            slot_no = user_input[1]
            parking.leave(int(slot_no))

        
        if "status" in user_input:
            parking.status()

        
        if "registration_numbers_for_cars_with_colour" in user_input:
            colour= user_input[-1]
            parking.registration_numbers_for_cars_with_colour(colour)

        
        if "slot_numbers_for_cars_with_colour" in user_input:
            colour=user_input[-1]
            parking.slot_numbers_for_cars_with_colour(colour)


        if "slot_number_for_registration_number" in user_input:
            regist_no = user_input[-1]
            parking.slot_number_for_registration_number(regist_no)
            #print(parking.get_slot_number_for_registration_number(registration_number))


def main():
    global lot
    lot=dict()
    In=input("select the way to provide input: press 1 for interactive and 2 for  file :")
    if In=="1":
        print("enter the command")
        while True:
        
            user_input=input()
            if user_input=="exit":
                print("Thank for using service")
                break
            parking.control(user_input)

    if In=="2":
        with open("G:\prasad7/co.txt") as fil:
            for i in fil:
                parking.control(i)
                
if __name__ == "__main__":
    parking=parking_lot()
    main()
    



   
