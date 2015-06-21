
import requests

print("検索したいキーワード")

keyword = input()

r = requests.get('http://connpass.com/api/v1/event/?keyword={0}'.format(keyword))
print(r.status_code, r.headers['content-type'])

f = open("events.txt","w")
for event in r.json()['events']:
    s = "{0} {1}".format(event['title'], event['started_at'])
    print(s)
    f.write(s + "\n")

f.close()


