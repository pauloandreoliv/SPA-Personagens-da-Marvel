import requests
import hashlib
import time

private_key = "aee05529d16467018b061c20de02d8873daa6aa9"
public_key = "a85314be8d4d34bb6e28dc2224274c9b"
timestamp = str(time.time())

string = timestamp + private_key + public_key

md5 = hashlib.md5()
md5.update(string.encode('utf-8'))
md5_hash = md5.hexdigest()


def request(limit,offset):
    request_url = f"https://gateway.marvel.com:443/v1/public/characters?limit={limit}&offset={offset}&apikey={public_key}&ts={timestamp}&hash={md5_hash}"
    request_return = requests.get(request_url)
    result = request_return.json()

    results_list = result["data"]
    return results_list

def listing(limit,offset):
    results_list = request(limit,offset)
    k = 0
    while k < len(results_list):
        print(k["name"])
        k += 1
    if k == 99:
        k = 0
        listing(limit+100,offset+100)

listing(0,0)
