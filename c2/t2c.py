from bs4 import BeautifulSoup

# reading from a saved html page
with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # to find a specific tag and print its first element found when using find or all elements when using find_all
    #courses_html_tags = soup.find_all('h5')

    # using loop to print each of all elements in a list
    #for course in courses_html_tags:
        #print(course.text)

    # use inspect in browser to research a webpage thoroughly like which header, tag, division, etc. to pick that contains required info
    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        course_name = course.h5.text

        #to pick last word or element and also starting from first bit by using split and -1 as index
        course_price = course.a.text.split()[-1]

        # to print a sentence using format below
        print(f'{course_name} costs {course_price}')