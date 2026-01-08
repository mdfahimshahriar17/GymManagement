import json
from person import Person
from bmi_calculator import BMI_Calculate
from membership import Membership



class GYM:
    def __init__(self, name, address, file_name="member_data.json"):
        self.name = name
        self.address = address
        self.file_name = file_name
        self.member_informations = []
        self.load_members()


    def load_members(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.member_informations = [Person(**member_data) for member_data in data]

        except (FileNotFoundError, json.JSONDecodeError):
            self.member_informations = []


    def save_members(self):
        member_data = [person.to_dict() for person in self.member_informations]
        with open(self.file_name, "w") as f:
            json.dump(member_data, f, indent=2)

    
    def add_member(self, name, age, phone, height, weight):
        BMI_value, BMI_range = BMI_Calculate().calculate_bmi(height, weight)

        person = Person(
            name=name,
            age=age,
            phone=phone,
            height=height,
            weight=weight,
            BMI_value=BMI_value,
            BMI_range=BMI_range,
        )

        self.member_informations.append(person)
        self.save_members()


    def membership(self, member, membership_type):
        if membership_type == 1:
            membership, access = Membership().bronze()

        elif membership_type == 2:
            membership, access = Membership().silvar()

        elif membership_type == 3:
            membership, access = Membership().golden()

        else:
            print("Invalid membership type")
            return

    
        member.membership = membership
        member.access = access

        
        self.save_members()

        print(f"{member.name} successfully added to {membership} membership")
        
