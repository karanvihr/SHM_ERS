from .person import Person

class Patient(Person):

    

    def __init__(self,user_id,p_id,name,age,phone,email,address,disease,blood_group,insurance_number,wallet_balance,medical_history=None,status='Registered',):

        super().__init__(user_id,name,age,email,phone,address)
        self.p_id = p_id
        self.disease = disease
        self.blood_group = blood_group
        self.__medical_history = medical_history
        self.status = status
        self.__insurance_number = insurance_number
        self.__wallet_balance = wallet_balance

    @property
    def medical_history(self):
        return self.__medical_history

    @medical_history.setter
    def medical_history(self,history):

        if not isinstance(history,str):
            raise ValueError("medical history must be a string.")

        self.__medical_history = history
        return "successfully updated medical history."

    @property
    def insurance_number(self):
        return self.__insurance_number

    @insurance_number.setter
    def insurance_number(self,number):

        if not isinstance(number,str):
            raise ValueError("insurance number must be a string.")

        self.__insurance_number = number
        return "successfully updated insurance number."
    

    @property
    def wallet_balance(self):
        return self.__wallet_balance

    def deposit(self,amount):
        if amount < 0 :
            raise ValueError("amount cannot be negative")
        self.__wallet_balance += amount 

    def withdraw(self,amount):
        if amount < self.__wallet_balance:
            raise ValueError("insufficient balance")
        self.__wallet_balance -= amount
        

    def update_blood_group(self,new_blood_group):
        self.blood_group = new_blood_group
        return "successfuly updated blood group."

    def get_details(self):
        patient_details = super().get_details()
        patient_details.update({'medical_history':self.medical_history,'blood_group':self.blood_group,'disease':self.disease,'wallet_balance':self.wallet_balance,'insurance_no.':self.insurance_number})
        return patient_details



p1 = Patient(1,1,'karan',22,333,'example@',1212,'fever','B+',123321,20000,'fever')


d = p1.get_details()
print(d.values())