import requests
import json
import dateutil


def process_job(jobdata):
    jobdata['_id'] = jobdata[u'DocumentID']
    jobdata['SalaryMin'] = float(jobdata['SalaryMin'][1:].replace(',',''))
    jobdata['SalaryMax'] = float(jobdata['SalaryMax'][1:].replace(',',''))
    return jobdata


def jobs_pager(url):

    current_page = 1
    while True:
        current_jobs_url = url + "&page=%s" % current_page
        response = requests.get(current_jobs_url)
        data = json.loads(response.text)
        if len(data['JobData']) > 0:
            for job in data['JobData']:
                yield process_job(job)

            current_page = current_page + 1

        else:
            break
        

def documents(name,**kwargs):
    return jobs_pager('https://data.usajobs.gov/api/jobs?series=2210')
