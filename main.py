from gym import GYM

def functionalities_choice():
    print("*********THE GYMNASIUM*********")
    print("TYPE (1) TO ADD MEMBER")
    print("TYPE (2) TO SEE MEMBERS")
    print("TYPE (3) TO Add MEMBERSHIP")
    print("TYPE (0) TO CLOSE")

    

def main():
    gym = GYM("Gymnasium", "Hussaini Dalan")

    while True:
        functionalities_choice()

        try:
            choice = int(input())
    
        except ValueError:
            print("Enter the right value")
            continue

        

        if choice == 1:
            try:
                name = input("Enter Name : ")
                age = int(input("Enter Age : "))
                phone = input("Enter Phone : ")
                height = float(input("Enter Height in Meter : "))
                weight = float(input("Enter Weight : "))
            
                gym.add_member(name=name, age=age, phone=phone, height=height, weight=weight)
                print("Member added!")

            except ValueError:
                print("Something you have written!")
            
        
        elif choice == 2:
            
            if gym.member_informations:
                for member in gym.member_informations:
                    print(member)
                    print("-" * 30)
            
            else:
                print("MEMBER LIST IS EMPTY!")
        
        
        elif choice == 3:
            phone = int(input("Enter Phone Number : "))
            if gym.member_informations:
                for member in gym.member_informations:
                    if member.phone == "570752":
                        print("Got it")
                    
            
            else:
                print("MEMBER LIST IS EMPTY!")
            # find_member =



        elif choice == 0:
            print("Closed")
            break


        else:
            print("Wrong Choice!")

            continue
            

if __name__ == "__main__":
    main()
