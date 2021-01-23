from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://timesofindia.indiatimes.com/india').text
soup = BeautifulSoup(html_text, "lxml")
links = soup.find_all("span", class_="w_tle")
# print(link)
for link in links:
    site_link = link.a["href"]
    print(site_link)
    if site_link.split("/")[0] == "" and site_link.split("/")[1] == "india" and not link.a.i:
        full_link = f"https://timesofindia.indiatimes.com/{site_link}"
        another_html_req = requests.get(f'{full_link}').text
        another_soup = BeautifulSoup(another_html_req, "lxml")
        content = another_soup.find("div", class_="_2NFXP")
        title = content.h1.text
        date_and_time = content.find("div", class_="_3Mkg- byline").text.split("|")[1]
        para_content = another_soup.find("div", class_="ga-headlines").text.split(".")
        edited_para_content = '.\n'.join(para_content)
        # print(edited_para_content)
        # print(f"\nTITLE:-\n{title}.\n\nLINK:-\n{full_link}\n\nDATE&TIME:-\n{date_and_time}\n\nTEXT:-\n{para_content}")

        with open("content.txt", "a") as file:
            file.write(f"\nTITLE:\n{title}\n\nLINK:\n{full_link}\n\nDATE&TIME:\n{date_and_time}\n\nTEXT:\n{edited_para_content}\n\n")
