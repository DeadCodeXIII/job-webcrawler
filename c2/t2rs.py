from bs4 import BeautifulSoup
import requests
import time

print('Enter a skill to be included or excluded:')
ski = input('>')
print(f'Filtering {ski}...')
print(f'')

def job_search():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        posted_date = job.find('span', class_='sim-posted').text.strip()
        if 'today' in posted_date:
            soup.find('span', class_='comp-more').decompose()
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            if ski not in skills:
                with open(f'posts/job_list.txt','a') as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Skills Required: {skills}\n")
                    f.write(f"Day of Posting: {posted_date}\n")
                    f.write(f"More Info: {more_info}\n\n\n")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        job_search()
        minutes = 30
        print(f'')
        print(f'Rescanning again in {minutes} minutes...')
        time.sleep(minutes * 60)