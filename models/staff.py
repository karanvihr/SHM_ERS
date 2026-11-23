from models.person import Person

class Staff(Person):

    def __init__(self,user_id,name,age,phone,email,address,shift,on_duty,department):

        super().__init__(user_id,name,age,phone,email,address)
        self.on_duty = on_duty 
        self.shift = shift
        self.department = department


        