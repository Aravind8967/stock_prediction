import requests

def test(c_name):
    api_url = f'http://localhost:80/price_range/{c_name}'
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    return data

if __name__ == '__main__':
    name = 'ITC'
    print(test(name))