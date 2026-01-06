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

class Calculate_BMI:

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







# print("*********CALCULATE YOUR BMI (Body Mass Index)*********")