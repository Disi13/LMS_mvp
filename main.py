import lms_mvp as lms


matesha = lms.Course("Matan")
print(matesha)
rus_yaz = lms.Course("Русския язык для начальной школы")
print(rus_yaz)
usr_1 = lms.User('Michail', 'Timofeev')
print(usr_1)
matesha.add_user_on_courses(usr_1)
print(matesha)
usr_1.add_course_in_user(rus_yaz)
print(usr_1)