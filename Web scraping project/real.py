from bs4 import BeautifulSoup
import requests

html_text = requests.get(url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
not_skill_known = "sql"
for job in jobs:
    job_published_date = job.find('span', class_="sim-posted").span.text
    if "few" in job_published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.strip()
        experience = job.find('ul', class_="top-jd-dtl clearfix").text
        location = experience.split()[-1]
        imp_data_2 = (experience.split()[2])
        imp_data_1 = (experience.split()[0].split('l')[-1])
        required_experience = f"{imp_data_1} - {imp_data_2} years"
        skills_required = job.find('span', class_="srp-skills").text.strip()
        more_info = job.header.h2.a["href"]
        print(more_info)
        # if not_skill_known not in skills_required:
        #     print(f"Company Name:- {company_name}\nExperience Required:- {required_experience}\nJob Location:- {location}\nSkills Required:- {skills_required}\n")