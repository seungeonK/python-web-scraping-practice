import requests
from bs4 import BeautifulSoup as BS
import time

print('Put some skill that you are not familar with')

unfamiliar_skill = input('>')

print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BS(html_text, 'lxml')

    #find(), find_all()
    jobs = soup.find_all(
        name='li', 
        class_='clearfix job-bx wht-shd-bx'
    )
    for idx, job in enumerate(jobs):
        published_date = job.find(
            name = "span",
            class_ = "sim-posted"
        ).span.text
        
        if 'few' in published_date.lower():
            company_name = job.find(
                name = 'h3',
                class_ = 'joblist-comp-name',
            ).text.replace(' ', '')

            skills = job.find(
                name = 'span',
                class_ = 'srp-skills'
            ).text.replace(' ','')

            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{idx}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Requried Skills: {skills.strip()}\n')
                    f.write(f'More Info: {more_info}\n')
                print(f'File saved: {idx}.txt')


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        # 600 = 600/60 = 10mins
        time.sleep(time_wait * 60)