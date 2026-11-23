from models.staff import Staff

class Nurse(Staff):

    def __init__(self, user_id,n_id, name, age, phone, email, address,qualification, shift, on_duty, department,experience):
        super().__init__(user_id, name, age, phone, email, address, shift, on_duty, department)
        self.n_id = n_id
        self.qualification = qualification
        self.experience = experience

        