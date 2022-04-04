import requests
from bs4 import BeautifulSoup

LIMIT = 50
SEARCH_CONDITION = "/jobs?q=python&limit="
INDEED_URL = "https://kr.indeed.com"

def get_last_page():
  result = requests.get(INDEED_URL + SEARCH_CONDITION + str(LIMIT))

  soup = BeautifulSoup(result.text, "html.parser")
  
  pagination = soup.find("div",{"class":"pagination"})
  
  links = pagination.find_all("a")
  pages = []

  for link in links[:-1]:
   pages.append(int(link.string))

  max_page = pages[-1]

  return max_page

def extract_job(html):
  
  title = html.find("h2",{"class":"jobTitle"}).find_all("span")[-1].string
  company_name = html.find("span",{"class":"companyName"}).string
  company_location = html.find("div",{"class":"companyLocation"}).string
  link = html['href']
  
  return {'title' : title, 'company_name' : company_name, 'company_location' : company_location, 'link' : INDEED_URL + link}
  

def extract_jobs(last_page):

  jobs = []
  
  for page in range(last_page):
    result = requests.get(f"{INDEED_URL}{SEARCH_CONDITION}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    htmls = soup.find("div", {"id":"mosaic-provider-jobcards"}).find_all("a")
    
    for html in htmls:
      try:
        jobs.append(extract_job(html))
      except:
        continue
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
  
