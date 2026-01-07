import json
from person import Person

class BMI_Calculate:

    def calculate_bmi(self, height, weight):
        
        BMI_value = (weight/(height**2))
        BMI_range = ""
        
        if BMI_value < 18.5:
            BMI_range = "Underweight"
        
        elif BMI_value < 25:
            BMI_range = "Normal Weight"
        
        elif BMI_value < 30:
            BMI_range = "Overweight"

        else:
            BMI_range = "Obese"

        return BMI_value, BMI_range



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
        data = [person.to_dict() for person in self.member_informations]
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


    
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
        
