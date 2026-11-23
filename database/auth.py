import bcrypt
from database.connection import get_connection
from database.patient_db import patient_register
from database.doctor_db import doctor_register
from database.nurse_db import nurse_register
from models.patient import Patient
from models.doctor import Doctor
from models.nurse import Nurse


def login_user(email,password):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT user_id, role, full_name, age, phone, email, address, password_hash
            FROM users
            WHERE email = %s
            """

        cursor.execute(query,(email,))
        user = cursor.fetchone()

        # check whether the email exists 
        if user is None:
            return False,"Invalid email or password.",None

        # compare the entered password with the stored bcrypt hash
        password_is_valid = bcrypt.checkpw(
            password.encode("utf-8"),
            user["password_hash"].encode("utf-8")
        )

        if not password_is_valid:
            return False,"Invalid email or password",None

        # Do not return the password hash to the UI 
        user.pop("password_hash",None)

        return True,"Login Successful.",user

    except Exception:
        return False,"Unable to log in right now. Please try again.",None


    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()






# ---------------------------------------------------------------------------------------------------------------------------------------------

def register_user(password,person):

    
    conn = None
    cursor = None

    if isinstance(person,Patient) and not person.blood_group:
        return False, "Blood group is required."

    elif isinstance(person,Doctor) and not person.specialization:
        return False, "Specialization is required."

    elif isinstance(person,Nurse) and not person.qualification:
        return False, "Qualification is required."

    elif isinstance(person,Nurse) and not person.department:
        return False, "Department is required."


     # convert the password into a secure hash
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
        )
    

    try:
        conn = get_connection()
        cursor = conn.cursor()

        user_query = """
            INSERT INTO users
            (role,full_name,age,phone,email,address,password_hash)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            """

        values = (
            person.role,
            person.full_name,
            person.age,
            person.phone,
            person.email,
            person.address,
            password_hash.decode("utf-8"),
        )

        cursor.execute(user_query,values)

        # Get automatically generated user_id
        user_id = cursor.lastrowid
        person.user_id = user_id


        # create patient profile
        if isinstance(person,Patient):
            patient_register(cursor,person)
            


        elif isinstance(person,Doctor):
            doctor_register(cursor,person)
            

        elif isinstance(person,Nurse):
            nurse_register(cursor,person)


        conn.commit()

        return True,"Account registered successfully."
        

    except Exception as e:

        if conn is not None:
            conn.rollback()

        # mysql error 1062 means a duplicate unique values
        if getattr(e,"errno",None) == 1062:
            return False, "An account with this email already exists."

        return False, f"Registration Failed: {e}"

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()
            
