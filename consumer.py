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


def request(offset,limit,name):
    request_url = f"https://gateway.marvel.com:443/v1/public/characters?limit={limit}&offset={offset}&apikey={public_key}&ts={timestamp}&hash={md5_hash}" + name
    request_return = requests.get(request_url)
    result = request_return.json()

    data_list = result["data"]
    return data_list


def listing_all(offset, past_requests, characters):
    data_list = request(offset,100,"")
    results_list = data_list["results"]
    total = data_list["total"]
    number_requests = math.ceil(total/100)

    cont = 0
    
    while cont < len(results_list) and past_requests < number_requests:
        name = results_list[cont]["name"]
        character = {"name": name}
        characters.append(character)

        if cont == 99:
            past_requests += 1
            
            if past_requests == (number_requests - 1):
                return characters
            
            offset = past_requests * 100
            return listing_all(offset, past_requests, characters)
            
        cont += 1


def listing(offset):
    characters = []
    
    data_list = request(offset,20,"")

    results_list = data_list["results"]

    cont = 0
    
    while cont < len(results_list):
        name = results_list[cont]["name"]
        description = results_list[cont]["description"]
        path_thumbnail = results_list[cont]["thumbnail"]["path"]
        extension_thumbnail = results_list[cont]["thumbnail"]["extension"]
        thumbnail = path_thumbnail + "." + extension_thumbnail
        
        if description == "":
            description = "Character has no description."
        
        character = {}
        character["name"] = name
        character["description"] = description
        character["thumbnail"] = thumbnail
        
        characters.append(character)

        if cont == 19:
            return characters
            
        cont += 1


def search(name):
    result = {}

    result["name"] = "Não foi possível encontrar"
    result["description"] = "Tente novamente"
    result["thumbnail"] = "https://i.imgur.com/QN8GUmf.jpg"
    result["comics"] = {"name": ""}
    
    if (name != ""):
        name = "&name=" + name
        
        data_list = request(0,1,name)

        total = data_list["total"]
        
        if total == 1:
            results_list = data_list["results"]
            
            name = results_list[0]["name"]
            description = results_list[0]["description"]
            path_thumbnail = results_list[0]["thumbnail"]["path"]
            extension_thumbnail = results_list[0]["thumbnail"]["extension"]
            thumbnail = path_thumbnail + "." + extension_thumbnail

            comics_list = results_list[0]["comics"]["items"]
            
            result["name"] = name
            result["description"] = description
            result["thumbnail"] = thumbnail
            result["comics"] = comics_list
    return result
