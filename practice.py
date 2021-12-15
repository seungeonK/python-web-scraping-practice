from bs4 import BeautifulSoup as bs


#open file and read the content
#file, mode
with open('index.html', 'r') as html_file:

    #read html
    content = html_file.read()

    soup  = bs(content, 'lxml')

    # grab some specific information(h5)
    # find_all() returns a list of all tags specified as parameter
    # courses_html_tags = soup.find_all('h5')

    # class(x), class_(O), class is built-in python keyword
    course_cards = soup.find_all('div', class_='card')
    
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')