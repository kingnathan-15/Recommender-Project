import requests
anime_id = 32935
headers = {
    'X-MAL-CLIENT-ID': 'e863fdfe943adee262553933a60982f8',
}
response = requests.get(f'https://api.myanimelist.net/v2/anime/{anime_id}', headers=headers)
print(response.json())

