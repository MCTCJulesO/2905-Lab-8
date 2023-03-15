import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    bitcoin = get_bitcoin_amount()
    dollars = convert_bitcoin_to_dollars(bitcoin)
    display_results(bitcoin, dollars)


def get_bitcoin_amount():
    while True:
        try:
            bitcoin = float(input('Enter the number of bitcoin: '))
            if bitcoin >= 0:
                return bitcoin
            else:
                print(' Please enter a number greater than 0')
        except ValueError:
            print('Enter a positive number.')


def convert_bitcoin_to_dollars(bitcoin):
    rate_json = get_bitcoin_data()   
    exchange_rate = extract_rate(rate_json)
    
    bitcoin = exchange_rate * bitcoin
    return bitcoin


# this function will be mocked
def get_bitcoin_data():
    return requests.get(url).json()
    

def extract_rate(rate_json):
    return rate_json['bpi']['USD']['rate_float']
    

def display_results(bitcoin, dollars):
    print(f'{bitcoin} bitcoin is equal to ${dollars}')


if __name__ == '__main__':
    main()