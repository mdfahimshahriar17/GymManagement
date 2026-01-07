class Person:
    def __init__(self, name, age, phone, height, weight, BMI_value = None, BMI_range = None):
        self.name = name
        self.age = age
        self.phone = phone
        self.height = height
        self.weight = weight
        self.BMI_value = BMI_value
        self.BMI_range = BMI_range

    def __str__(self):
        bmi_text = "Not calculated"
        if self.BMI_value is not None and self.BMI_range is not None:
            bmi_text = f"{self.BMI_value:.2f} ({self.BMI_range})"

        return (
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Phone : {self.phone}\n"
            f"Height : {self.height}\n"
            f"Weight : {self.weight}\n"
            f"BMI : {bmi_text}"
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
        }
