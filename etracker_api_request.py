import requests

headers = {'X-ET-email':'YOUR_EMAIL',
           'X-ET-developerToken':'YOUR_TOKEN',
           'X-ET-accountId':'YOUR_ID', 
           'X-ET-password':'YOUR_PASSWORD'}
           
url = 'https://ws.etracker.com/api/rest/v2/report/VisitorPerDay/data?limit=40&offset=0&startDate=2015-10-01&endDate=2015-10-30&sortOrder=desc'
r = requests.get(url, headers=headers)

r.json()
