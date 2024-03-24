import sqlite3


class database:
    def __init__(self):
        conn = sqlite3.connect("SHOP.sqlite")
        cursor = conn.cursor()
        with open("database.sql", "r") as file:
            query = file.read()
            cursor.executescript(query)
        cursor.execute("SELECT Cassa_many FROM Cassa")
        info = cursor.fetchall()
        if info == []:
            cursor.execute("insert into Cassa(Cassa_many) values (0)")
            cursor.execute("insert into Karta(Karta_many) values (0)")
            cursor.execute("insert into Users(user_log_parol, user_rol) values ('Admin:1234','adm')")
        conn.commit()
        conn.close()




    def select_admin(self):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute("SELECT User_Log_parol FROM Users WHERE user_rol ='adm'")
            info = curs.fetchall()
            info = [item for sublist in info for item in sublist]


        conn.commit()
        conn.close()

        return info

    def select_jobs(self):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute("SELECT User_Log_parol FROM Users WHERE user_rol ='job'")
            info = curs.fetchall()
            info = [item for sublist in info for item in sublist]
        conn.commit()
        conn.close()
        return info


    def select_cassa(self):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute("SELECT Cassa_many FROM Cassa WHERE Cassa_id = 1")
            info = curs.fetchall()
            info = [item for sublist in info for item in sublist]
        conn.commit()
        conn.close()

        return info



    def update_cassa(self,couns):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"UPDATE Cassa set Cassa_many= {couns} where Cassa_id = 1")
        conn.commit()
        conn.close()

    def Add_admin(self,couns):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"insert into Users(user_log_parol, user_rol) values (?,?)",(couns,'adm',))
        conn.commit()
        conn.close()

    def Add_worker(self, couns):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"insert into Users(user_log_parol, user_rol) values (?,?)", (couns, 'job',))
        conn.commit()
        conn.close()

    def select_my_dolg(self):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute("SELECT My_dolg_id,names FROM My_dolg")
            info = curs.fetchall()
            info = [item for sublist in info for item in sublist]
        conn.commit()
        conn.close()
        result = ''
        # Разделение значений на пары по два элемента
        pairs = zip(info[::2], info[1::2])

        for id, name in pairs:
            result += f"{id} - {name}\n"
        return result

    def add_my_dolg(self, dolg):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"insert into My_dolg(names) values (?)", (dolg,))
        conn.commit()
        conn.close()

    def del_my_dolg(self, dolg):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"delete from My_dolg where My_dolg_id = {dolg}")
        conn.commit()
        conn.close()

    def select__dolg(self):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute("SELECT Dolg_id,names FROM Dolg")
            info = curs.fetchall()
            info = [item for sublist in info for item in sublist]
        conn.commit()
        conn.close()
        result = ''
        # Разделение значений на пары по два элемента
        pairs = zip(info[::2], info[1::2])

        for id, name in pairs:
            result += f"{id} - {name}\n"
        return result

    def add_dolg(self, dolg):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"insert into Dolg(names) values (?)", (dolg,))
        conn.commit()
        conn.close()

    def del_dolg(self, dolg):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"delete from Dolg where Dolg_id = {dolg}")
        conn.commit()
        conn.close()

    def update_Karta(self, couns):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute(f"UPDATE Karta set Karta_many= {couns} where Karta_id = 1")
        conn.commit()
        conn.close()

    def select_karta(self):
        with sqlite3.connect("SHOP.sqlite") as conn:
            curs = conn.cursor()
            curs.execute("SELECT Karta_many FROM Karta WHERE Karta_id = 1")
            info = curs.fetchall()
            info = [item for sublist in info for item in sublist]
        conn.commit()
        conn.close()
        return info[0]