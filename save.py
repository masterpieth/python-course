import csv

def save_to_file(jobs):
  #파일을 생성
  file = open("jobs.csv", mode="w")
  #csv 내의 writer 객체 생성
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    #values 로만 하게 되면 type 이 dict_value 가 되어버린다.
    writer.writerow(list(job.values()))
  return