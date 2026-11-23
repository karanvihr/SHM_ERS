from database.connection import get_connection


def patient_register(cursor,patient):

  

        query = """
            INSERT INTO patients
            (user_id,blood_group,medical_history,status)
            VALUES (%s, %s, %s, %s )
            """

        values = (
            patient.user_id,
            patient.blood_group,
            patient.medical_history,
            patient.status
        )


        cursor.execute(query,values)


        return cursor.lastrowid





# -------------------------------------------------------------------------------------------------------------------

def load_patient(p_id):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT * FROM patients 
            WHERE p_id = %s
            """

        cursor.execute(query,(p_id,))

        patient = cursor.fetchone()
        return patient

    except Exception  as e:
        print("error loading patient:",e)
        return None

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()