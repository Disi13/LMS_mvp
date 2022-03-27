class User:
    __us_id = 0  # для подсчета и установки id новым пользователям

    def __init__(self, name, surname):
        User.__us_id += 1
        self.__name = name
        self.__surname = surname
        self.__id = User.__us_id
        self.__courses = set()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    def __str__(self):
        return str(self.__id) + ". " + self.__name + " " + self.__surname + ", " + str(self.__courses)

    def add_course_in_user(self, course):
        if not course in self.__courses:
            self.__courses.add(course)
            course.add_user_on_courses(self)


class Course:
    __course_id = 0

    def __init__(self, course_name):
        Course.__course_id += 1
        self.__course_name = course_name
        self.__id = Course.__course_id
        self.__users = dict()

    @property
    def course_name(self):
        return self.__course_name

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return str(self.__course_id) + ". " + str(self.__course_name) + str(self.__users)

    def add_user_on_courses(self, user):
        if not user.id in self.__users:
            self.__users[user.id] = dict()
            self.__users[user.id]['User'] = user
            self.__users[user.id]['grade'] = 0
            user.add_course_in_user(self)


matesha = Course("Matan")
print(matesha)
rus_yaz = Course("Русския язык для начальной школы")
print(rus_yaz)
usr_1 = User('Michail', 'Timofeev')
print(usr_1)
matesha.add_user_on_courses(usr_1)
print(matesha)
usr_1.add_course_in_user(rus_yaz)
print(usr_1)