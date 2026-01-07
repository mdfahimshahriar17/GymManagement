class Person:
    def __init__(self, name, age, phone, height, weight, BMI_value = None, BMI_range = None):
        self.name = name
        self.age = age
        self.phone = phone
        self.height = height
        self.weight = weight
        self.BMI_value = BMI_value
        self.BMI_range = BMI_range



    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "height": self.height,
            "weight": self.weight,
            "BMI_value": self.BMI_value,
            "BMI_range": self.BMI_range,
        }
