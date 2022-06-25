class Profile:
    # Класс относится к M-составляющей паттерна модели VCM.
    # Класс содержит методы set_profile и get_profile для добавления и получения
    # пользователя в/из БД соответственно
    def __init__(self, login, password, surname, name, age, email, study_group, id_student):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.study_group = study_group
        self.id_student = id_student

    def set_profile(self, conn):
        with conn.cursor() as cur:
            while True:
                passw = input("Введите Ваш будущий пароль: ")
                passw0 = input("Повторите пароль: ")
                if passw == passw0:
                    break
                else:
                    print("Пароли не совпали")
                    continue
            cur.execute("""
                        UPDATE student
                        SET login = (%s), password = (%s)
                        WHERE id_student = (%s);""",
                        [self.login, passw, self.id_student])
            conn.commit()

    def get_profile(self, conn):
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM student WHERE login = (%s);", [self.login])
            lst = cur.fetchone()
            return lst

    def get_group_list(self, conn):
        with conn.cursor() as cur:
            cur.execute("""
                        select s.id_student, s."name" ,s.surname  
                        from student s , study_group sg
                        where s.study_group = sg.id_study_group
                        and s.login is null
                        and sg."name" = (%s);""",
                        [self.study_group])
            lst = cur.fetchall()
        return lst
