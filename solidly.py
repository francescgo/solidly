import requests
import time

token_gecko = ["velodrome-finance","aerodrome-finance","thena","ramses-exchange","equalizer-on-sonic","lynex","ocelex"]
token_llama = ["velodrome","aerodrome","thena","ramses-exchange","equalizer","lynex","ocelex"]
token = ["velodrome","aerodrome","thena","ramses","equalizer","lynex","ocelex"]
result = { }

#Getting Fully Diluted Value from Coingecko
def get_fully_diluted_value(token_input):
    url = "https://api.coingecko.com/api/v3/coins/"+token_input
    response = requests.get(url)
    data = response.json()
    fully_diluted_value = round(data["market_data"]["fully_diluted_valuation"]["usd"]/1000000,1)
    return fully_diluted_value

#Getting Total Value Locked from Defi Llama
def get_tvl(token_input):
    url = "https://api.llama.fi/tvl/"+token_input
    response = requests.get(url)
    data = response.json()
    tvl = round(data/1000000,1)
    return tvl

#Getting 7d Revenue from Defi Llama
def get_rev7d(token_input):
    url = "https://api.llama.fi/summary/fees/"+token_input
    response = requests.get(url)
    data = response.json()
    rev7d = data["total7d"]
    if rev7d == None:
        return 0
        pass
    else:
        rev7d = round(rev7d/1000000,3)
    return rev7d

#Getting Market Cap from Defi Llama
def get_mcap(token_input):
    url = "https://api.llama.fi/protocol/"+token_input
    response = requests.get(url)
    data = response.json()
    mcap = data["mcap"]
    if mcap==None:
        return 0
        pass
    else:
        mcap = round(mcap/1000000,1)
    return mcap

for x in range(7):
    result[token[x]] = {}
    if x<6: result[token[x]]['fdv'] = get_fully_diluted_value(token_gecko[x])
    else: result[token[x]]['fdv'] = 0
    result[token[x]]['tvl'] = get_tvl(token_llama[x])
    result[token[x]]['rev7d'] = get_rev7d(token_llama[x])
    result[token[x]]['mcap'] = get_mcap(token_llama[x])
    time.sleep(5)
    if result[token[x]]['rev7d'] != 0:
        result[token[x]]['per'] = result[token[x]]['mcap']/result[token[x]]['rev7d']/52
        result[token[x]]['fdper'] = result[token[x]]['fdv']/result[token[x]]['rev7d']/52
        pass
    else: result[token[x]]['per'] = 'N/A'
    pass

print(result)
