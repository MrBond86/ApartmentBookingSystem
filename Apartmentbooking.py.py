'''
Name-Pramod Bhattarai
Student id- S4109474
Attempted all part 3 parts.
'''
import sys
guests = {
     'Arjun': 20,
     'Pramod':30
}
apartment ={
     'U12swan': {'rate':95.0,'capacity':2},
     'U209duck': {'rate':106.7,'capacity':2},
     'U49goose':{'rate':145.2,'capacity':2},
}
supplementary_item={
    'car_park': 25,
    'breakfast':21,
    'toothpaste':5.,
    'extra_bed':50
}
guest_booking={}
#function to validate non empty input
def non_empty(prompt):
     while True:
          user_input=input(prompt).strip()
          if user_input:
               return user_input
          else:
               print("Input cannot be empty. Please try again.")

def display_guests():
    if guests:
        print("Existing Guest and Reward points: ")
        for guest, reward_points in guests.items():
            print(f"Guest: {guest}, Reward point: {reward_points}")
    else:
         print("No guest found.")

def validate_apartment_id(apartment_id):
    if apartment_id.startswith('U') and apartment_id[1:].isalnum():
        return True
    return False

def display_apartment():
    if apartment:
        print("The apartment list are:")
        for apartment_id, details in apartment.items():
            print(f"Apartment Id: {apartment_id}, Rate: ${details['rate']:.2f}per nights, Capacity: {details['capacity']} beds ")

def display_supplimentary_items():
    print("The suppliementary items are:")   
    for items_id,price in supplementary_item.items():
        print(f"Item id: {items_id}, Price: ${price:.2f}")

#function to add or update apartment for part 2
def add_update_apartment():
    new_apartment=non_empty("Enter the apartment details (Id Rate Capacity)").split()
    if len(new_apartment)==3 and validate_apartment_id(new_apartment[0]):
        apartment_id = new_apartment[0]
        rate=float(new_apartment[1])
        capacity=int(new_apartment[2])
        apartment[apartment_id]={'rate':rate, 'capacity':capacity}
        print(f"Apartment {apartment_id} is updated with rate :${rate:.2f} and capacity :{capacity:.2f}")
    else:
        print("Invalid data. Please Try again. Apartment not updated")

#function to add supplementary items for part 2
def add_update_supplementary_items_part2():
    new_items=non_empty("Enter items in detail (ID Price)").split()
    if len(new_items)==2:
        item_id=new_items[0]
        price=float(new_items[1])
        supplementary_item[item_id]=price
        print("Supplementary items {item_id} is updated with price : ${price: .2f}")
    else:
        print("Invalid data.Item was not updated . ")

#function to add/update information of a supplementary items  for part 3
#reference of use of try and catch from canvas file
def add_update_supplementary_items():
    display_supplimentary_items
    while True:
        input_list=non_empty("Enter the list of supplementary items and prices: ").strip()
        datas= input_list.split(',')
        valid= True
        for data in datas:
            try:
                item, price = data.split()
                price = float(price)
                if price <=0:
                    print(f"Invalid price for {item}. Price must be positive")
                    valid=False
                    break
                supplementary_item[item] =price
            except ValueError:
                print("Invalid format or price.Please try again")
                value=False
                break
        if valid:
            print("Supplementary items are updated")
            break
# function to display guest booking or history for part 3
#Enumerate function is used  with start =1 as it allows  easy numbering of each booking starting from 1
#reference for enumerate is chatgpt
def display_guest_history():
    guest_name=non_empty("Enter the name of the guest:")
    if guest_name not in guest_booking:
        print("Invalid guest name. Please try again")
        return
    
    print(f"/n The booking and order history of {guest_name} :")
    print(f"{'List':<20} {'Total cost':<20} {'Earned Rewards:<20'}")
    for index, booking in enumerate(guest_booking[guest_name],1):
        apartment_info = f"{booking['nights']} x {booking['apartment_id']}"
        supplementary_info= f"{booking['supplementary_total']}" if booking['supplementary_total']>0 else""
        print(f"Order {index:<20} {apartment_info + supplementary_info:<20} {booking['total_cost']:<20.2f} {booking['reward_points']:<20}")
            
#booking function 
def booking():
    extra_beds= 0
     #1 name of guest
    guest_name = non_empty("Enter the Main guest name: ")
    if not  guest_name.isalpha():
          print("Invalid input. Guest name must be Alphabet characters.")
          return
    
     #2 number of guest
    while True:
          number_of_guest=non_empty("Enter the number of Guest: ")
          if  number_of_guest.isdigit():
           number_of_guest= int(number_of_guest)
           break
          else:
               print("Invalid input. Please enter numeric value")
               break
     
     #3 For aparment id
    while True:
          apartment_id=non_empty("Enter the apartment id(U12swan/U209duck/U49goose): ")
          if validate_apartment_id(apartment_id) and  apartment_id in  apartment:
              print(f"Apartmetment rate :${apartment[apartment_id]['rate']:.2f} per night")  #part 3 rate is automatically displayed
              break
          print("Invalid aparment id. Please enter again")
    #for part 3 validating the number of guest against the capacity of apartment
    apartment_capacity= apartment[apartment_id]['capacity']
    
    while number_of_guest > apartment_capacity + extra_beds *2:
        if extra_beds<2:
            print("Number of guest is more than capacity.Please consider ordering an extra bed")
            add_extra_beds=non_empty("Do you want to add any extra bed?(y/n):").lower()
            if add_extra_beds == 'y':
                extra_beds += 1
                print(f"Extra bed is added. Total capacity :{apartment_capacity + extra_beds * 2} guests.")
            else:
                print("Booking connot be  proceed. Exiting to main menu.")
                return
        else:
            print("Booking cannot be done with extra beds. Exiting to main menu.")
            return
        
     #4 getting check in dates
    check_in_date=non_empty("Enter the check in date (dd/mm/yyyy) ")

     #5getting check out dates
    check_out_date=non_empty("Enter the check out date (dd/mm/yyyy) ")

     #6 for length of stay
    while True:
          length_of_stay=non_empty("Enter the length of stay (Nights) : ")
          if  length_of_stay.isdigit():
               length_of_stay=int(length_of_stay)
               if length_of_stay > 0 and length_of_stay <= 7:
                    break
               else:
                print("Length of stay must be positive and between 1 and 7 days.")
          else:
           length_of_stay=print("Invalid input. Please enter a numeric values")
           break

    
     #7 For booking dates
    booking_date=non_empty("Enter the booking date (dd/mm/yyyy): ")

     #8calculating Cost
    apartment_rates = apartment[apartment_id]['rate']
    total_cost=apartment_rates * length_of_stay
    print(f"Apartment rate: ${apartment_rates:.2f} (AUD)")

     #9 for calcualating rewards
    reward_points=round(total_cost)

    #for part 3 checking does the guest already exist and have some rewards worth reducing or not
    if guest_name in guests: 
        current_rewards = guests[guest_name]
        if current_rewards >= 100:
            reward_choice = non_empty("Do you want to use your rewards point ?(y/n):")
            if reward_choice == 'y':
                reduce= (current_rewards// 100)*10
                total_cost -= reduce
                remaining_rewards= current_rewards *100
                guests[guest_name] = remaining_rewards + reward_points
                print(f"${reduce} deducted from total cost. New cost :${total_cost:.2f}")
            else:
                guests[guest_name] += reward_points
        else:
            guests[guest_name] += reward_points
    else:
       guests[guest_name] = reward_points 

    


     #for 12 and 13
    if guest_name in guests:
          guests[guest_name] += reward_points
    else:
          guests[guest_name] = reward_points
          
#for supplimentary items for part 2
    supplementary_total=0
    while True:
        supplementary_choice= non_empty("Do you want to order any suppliementary items:\n ").lower()
        if supplementary_choice =='n':
            break
        elif supplementary_choice == 'y':
            while True:
                display_supplimentary_items()
                item_id=non_empty("Enter the supplement item ID:")
                if item_id in supplementary_item:
                    price=supplementary_item[item_id]
                    print(f"Price: ${price:.2f}")   #part 3 displaying automatically the price of supllimentary item
                    quantity=non_empty("Enter the quantity")
                    if quantity.isdigit():
                        quantity= int(quantity)
                        if quantity > 0:
                            cost= price * quantity
                            print(f"Item: {item_id}, Quantity: {quantity}, Price: ${price}, Cost: {cost}")
                            confirm = non_empty("Please confirm order (y/n): ").lower()
                            if confirm == "y":
                                supplementary_total += cost
                                total_cost += cost
                                break
                            elif confirm == 'n':
                                print("Item cancelled")
                                break
                            else:
                                print("Invalid input. Please enter y/n:")
                        else:
                            print("Quantity must be positive")
                    else:
                        print("Invlaid quantity.Please Enter a number")
                else:
                    print("Invalid Item Id. Please enter again")
 
    #Storing the booking detail in guest booking
    if guest_name not in guest_booking:
        guest_booking[guest_name] = []
    guest_booking[guest_name].append({
        'apartment_id':apartment_id,
        'apartment_rates':apartment_rates,
        'nights':length_of_stay,
        'supplementary_total':supplementary_total,
        'total_cost':total_cost,
        'reward_points':reward_points,
        'check_in_date':check_in_date,
        'check_out_date':check_out_date
    })                  



    #printing all output
    print("\n---Booking Information---")
    print(f"Guest's Name:{guest_name}")
    print(f"Number of Guest:{number_of_guest}")
    print(f"Aparment ID:{apartment_id}")
    print(f"Apartment Rate: ${apartment_rates:.2f} per night")
    print(f"Check-in Date:{check_in_date}")
    print(f"Check-out Date:{check_out_date}")
    print(f"Length of Stay :{length_of_stay} nights")
    print(f"Booking Date :{booking_date}")
    if supplementary_total > 0:
        print("===================================================")
        print("Supplemenatry Items: \n")
        for item_id, price in supplementary_item.items():
            print(f"Item Id: {item_id}, Price: {price:.2f}")
    print(f"Sub_total :$({supplementary_total:.2f})")
    print("==================================================")


    print(f"Total Cost:${total_cost:.2f} (AUD)")
    print(f"Reward Point Earned:{reward_points} (points)")
    print("\nThank you for your booking! We hope you will have an enjoyable stay.")
    print("===================================================")

            
#for part 3 
def main():
    while True:
        print("\nMenu:")
        print("1.Display Guests")
        print("2.Display Apartments")
        print("3.Display supplemetary items")
        print("4.Make a booking")
        print("5.Add/update Information of Supplementary Items")
        print("6.Display Guest and order history")
        print("7.Exit")
        
        choose=non_empty("Choose an option:")
        if choose == '1':
          display_guests()
        elif choose=='2':
            display_apartment()
        elif choose=='3':
            display_supplimentary_items()
        elif choose=='4':
            booking()
        elif choose=='5':
            add_update_supplementary_items()
        elif choose =='6':
            display_guest_history()
        elif choose=='7':
            print("Program exiting. Thank you. Goodbye")
            sys.exit()
        else:
            print("Invalid choice.Please choose again")
        
main()


'''
For Designing anf writing this program , i have used data structures like dictionaries mainly for storing except for using 
list in guest booking to maintain the sequential history of booking for each guest. For all operation like input validation 
,displaying output, booking process , adding / updating data etc all are defined as a functions. For the flow control while loop is used
as we dont have any specification for the number of guests and if-else statement are used to ensure the input data are in correct format
 as well loops and if=else statements in nested form are also used to avoid the infinite loops.


 #for references

 -Python documentation and canvas material was used mostly for syntax references and built in functions
 -Stack overflow and w3wschools was also used to understand and write code
 -Some amount of chatgpt was also used for guidance on logic of code and for suggestion on refening the functions and loops
 used within the program
'''