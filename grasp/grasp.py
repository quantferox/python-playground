# 🧩 Задача: GRASP — кто за что отвечает?
# Ты делаешь бэкенд для онлайн-курсов. Сейчас есть такой код:
class CoursePlatform:
    def __init__(self):
        self.users = []
        self.courses = []

    def register_user(self, name):
        user = {"name": name, "enrolled_courses": []}
        self.users.append(user)
        return user

    def create_course(self, title, description):
        course = {"title": title, "description": description}
        self.courses.append(course)
        return course

    def enroll_user(self, user, course):
        user["enrolled_courses"].append(course)
        print(f"{user['name']} enrolled in {course['title']}")


# ✅ Твоя задача:
# 🧠 Найди 2–3 шаблона GRASP, которые можно применить.
# ✏️ Перепиши код, перераспределив ответственность между классами согласно этим шаблонам.
class User:
    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course.title}")


class Course:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class CoursePlatform:
    def __init__(self):
        self.users = []
        self.courses = []

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def create_course(self, title, description):
        course = Course(title, description)
        self.courses.append(course)
        return course

    def enroll_user(self, user, course):
        user.enroll(course)
