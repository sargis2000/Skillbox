data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print(f'data keys = {data.keys()}\ndata values = {data.values()}') #ex.1
#------------------------------------------------------------------------------------
data['ETH']['total_diff'] = 100  #EX.2
#----------------------------------------------------------------------
data['tokens'][0]['fst_token_info']['name'] = 'doge' #EX3
#-----------------------------------------------------------------------
for i in range(2):  #EX.4
    total_out = data['tokens'][i].pop('total_out')
    data['ETH'][total_out] = total_out
#---------------------------------------------------------------------------------
val = data['tokens'][1]['sec_token_info'].pop('price')#EX.5
data['tokens'][1]['sec_token_info']['total_price'] = val

print(data)
# TODO здесь писать код
