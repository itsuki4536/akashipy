
import requests

print("検索したいキーワード")

keyword = input()

r = requests.get('http://connpass.com/api/v1/event/?keyword={0}'.format(keyword))
print(r.status_code, r.headers['content-type'])

for event in r.json()['events']:
    print(event['title'], event['started_at'])