import random 
import time

def natural_numbers():
    n = 1 
    yield n
    n += 1

returned_values = list(natural_numbers())

seats = [1,2,3]
left_seat_numbers = ' '.join(map(str, seats))
print("Welcome to Ehsan Gamenet!")
name = input("What's your name? ")
answer = input("What are you doing?(Leaving/entering)")
if answer.lower() == "leaving": 
    print("Goodbye! See you then!")
    quit()

if answer.lower() == "entering": 
        def seat_choosing_verification(seat_number):
            while True: 
                try:
                    seat_number = input(f"Please choose your seat number({left_seat_numbers}))")
                    if seat_number in left_seat_numbers:
                        print("You'll go there pal!")
                        seats.remove(seat_number)
                    else: 
                        pass  # Complete the else block, even if you don't want to do anything
                except ValueError:
                    seat_number = input(f"Please choose your seat number({left_seat_numbers}))")


def time_to_stay(staying_time):
    while True:
        try: 
            staying_time = int(input("How long are you going to be here?(in minutes please!)"))
            if staying_time  in returned_values:
                staying_time_seconds = staying_time*60 

                while staying_time_seconds>0: 
                    time.sleep(staying_time_seconds)
                    staying_time_seconds -= 1 
                print(f"It's time to go{name}!")
            
            
                 
            elif staying_time > 120: 
                staying_time = int(input("You can't be here this much! Enter another period of time: )"))

                
                 

            elif staying_time not in returned_values:
                staying_time = int(input("Your staying time must be a number!)"))
        except ValueError:
                        staying_time = int(input("How long are you going to be here?(in minutes please!)"))


            
        
        
    

