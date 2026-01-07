class Person:
    def __init__(self, name, age, phone, height, weight, BMI_value, BMI_range, membership=0):
        self.name = name
        self.age = age
        self.phone = phone
        self.height = height
        self.weight = weight
        self.BMI_value = BMI_value
        self.BMI_range = BMI_range
        self.membership = membership

    def __str__(self):
        bmi_text = f"{self.BMI_value:.2f} ({self.BMI_range})"
        membership_text =  f"You have '{self.membership}' Month Membership"

        return (
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Phone : {self.phone}\n"
            f"Height : {self.height}\n"
            f"Weight : {self.weight}\n"
            f"BMI : {bmi_text}\n"
            f"Membership : {membership_text}\n"
        )


    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "height": self.height,
            "weight": self.weight,
            "BMI_value": self.BMI_value,
            "BMI_range": self.BMI_range,
            "membership": self.membership
        }
 
