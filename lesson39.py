import requests

res = requests.get("https://miro.medium.com/max/1050/1*1BUIofZgqVuR6nj8LbrRtQ.jpeg")
# print(res.status_code)
# print(res.text[:500])
# easy way to see if it's working
print(res.raise_for_status())
# returns none if all good
# can save web page but must do it with binary file (so wb instead of w)
testFile = open("testFile.jpg", "wb")
for chunk in res.iter_content(1000000):
    testFile.write(chunk)
testFile.close()