from models.staff import Staff

class Doctor(Staff):

    def __init__(self,user_id,d_id,name,age,phone,email,address,specialization,years_of_experience,consultation_fee,on_duty,shift,department,availability):
        super().__init__(
            user_id=user_id,
            name=name,
            age=age,
            phone=phone,
            email=email,
            address=address,
            on_duty=on_duty,
            shift=shift,
            department=department,
            )
        self.d_id = d_id
        self.specialization = specialization
        self.years_of_experience = years_of_experience
        self.consultation_fee = consultation_fee
        self.availability = availability
