
def doctor_register(cursor,doctor):



        query = """
        INSERT INTO doctors
        (user_id,s_id,specialization,on_duty,shift,department)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            doctor.user_id,
            doctor.s_id,
            doctor.specialization,
            doctor.on_duty,
            doctor.shift,
            doctor.department
        )


        cursor.execute(query,values)

        return cursor.lastrowid

