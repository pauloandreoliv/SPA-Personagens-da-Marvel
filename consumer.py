import requests
import hashlib
import time
import math

private_key = "aee05529d16467018b061c20de02d8873daa6aa9"
public_key = "a85314be8d4d34bb6e28dc2224274c9b"
timestamp = str(time.time())

string = timestamp + private_key + public_key

md5 = hashlib.md5()
md5.update(string.encode('utf-8'))
md5_hash = md5.hexdigest()


def request(offset):
    request_url = f"https://gateway.marvel.com:443/v1/public/characters?limit=100&offset={offset}&apikey={public_key}&ts={timestamp}&hash={md5_hash}"
    request_return = requests.get(request_url)
    result = request_return.json()

    data_list = result["data"]

    return data_list


def listing(offset, past_requests, characters):
    data_list = request(offset)

    results_list = data_list["results"]
    total = data_list["total"]

    number_requests = total / 100
    number_requests = math.ceil(number_requests)

    past_requests = past_requests
    
    k = 0

    characters = characters
    
    while k < len(results_list) and past_requests < number_requests:
        name = results_list[k]["name"]
        description = results_list[k]["description"]
        path_thumbnail = results_list[k]["thumbnail"]["path"]
        extension_thumbnail = results_list[k]["thumbnail"]["extension"]
        thumbnail = path_thumbnail + "." + extension_thumbnail

        character = []
        character.append(name)
        character.append(description)
        character.append(thumbnail)

        characters.append(character)

        if k == 99:
            past_requests += 1
            offset = past_requests * 100
            listing(offset, past_requests, characters)
            
        k += 1
