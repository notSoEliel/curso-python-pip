import requests

api_url_categories = "https://api.escuelajs.co/api/v1/categories"

def get_categories():
    r = requests.get(api_url_categories)
    print(f'Status code: {r.status_code}')
    print(f'Text: {r.text}')
    print(f'Type: {type(r.text)}')
    categories = r.json() # convert from string to json format (in python a list of dictionaries)
    for category in categories:
        print(category['name'])