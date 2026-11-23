

def nurse_register(cursor,nurse):




        query = """
                INSERT INTO nurses (user_id, qualification, shift, on_duty, department)
                VALUES (%s, %s, %s, %s, %s)
                """

        values = (
            nurse.user_id,
            nurse.qualification,
            nurse.shift, 
            nurse.on_duty, 
            nurse.department
        )
        
        cursor.execute(query,values)
        

        return cursor.lastrowid

    