import lms_mvp


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