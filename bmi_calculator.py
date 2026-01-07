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