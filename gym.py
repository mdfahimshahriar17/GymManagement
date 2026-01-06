class Person:
    def __init__(self, name, age, phone, height, weight, BMI = None):
        self.name = name
        self.age = age
        self.phone = phone
        self.height = height
        self.weight = weight
        self.BMI = BMI

    def __str__(self):
        return f"Name : {self.name}\nAge : {self.age}\nHeight : {self.height}\nWeight: {self.weight}\nBMI : {self.BMI}"

class BMI_Calculate:

    def calculate_bmi(self, height, weight):
        
        BMI = (weight/(height**2))
        bmi_range = ""
        
        if BMI < 18.5:
            bmi_range = "Underweight"
        
        elif BMI < 25:
            bmi_range = "Normal Weight"
        
        elif BMI < 30:
            bmi_range = "Overweight"

        else:
            bmi_range = "Obese"

        return (BMI, bmi_range)



class GYM:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.member_informations = []




    def add_member(self, name, age, phone, height, weight):
        bmi = BMI_Calculate().calculate_bmi(height=height, weight=weight)

        person = Person(name=name, age=age, phone=phone, height=height, weight=weight, BMI=bmi)
        
        self.member_informations.append(person)


gym = GYM("Gymnasium", "Hussaini Dalan")

gym.add_member("Fahim", 26, "012345821", 1.68, 85.5)
gym.add_member("Nahar", 26, "012615821", 1.23, 56)

print([str(member) for member in gym.member_informations])












# print("*********CALCULATE YOUR BMI (Body Mass Index)*********")