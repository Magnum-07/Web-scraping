from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    content = file.read()
    data = BeautifulSoup(content, "lxml")
    course_cards = data.find_all("div", class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} :- {course_price}.")
