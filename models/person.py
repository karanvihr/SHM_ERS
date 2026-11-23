
class Person:

    


    def __init__(self,id,name,age,phone,email,address):

        self.id = id 
        self.fullname = name
        self.age = age
        self.phone_no = phone
        self.email = email
        self.address = address

    def update_phone_no(self,new_phone):
        if len(str(new_phone)) == 10: 
            self.phone_no = new_phone
            return "Changed successfully."   

    def update_email(self,new_email):
        self.email = new_email

    def update_age(self,new_age):
        if new_age < 0 or new_age > 120:
            return "Invalid age."
        self.age = new_age

    def update_address(self,new_address):
        self.address = new_address
         
    def  get_details(self):
        return {
            "user_id":self.id,
            "name":self.fullname,
            "age":self.age,
            "phone_no":self.phone_no,
            "email":self.email,
            "address":self.address
        }