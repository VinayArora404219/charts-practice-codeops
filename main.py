from pycoingecko import CoinGeckoAPI

from utils import draw_bar_chart, draw_pie_chart

if __name__ == '__main__':
    cg = CoinGeckoAPI()

    # getting list of names of first 5 coins from CoinGeckoAPI
    list_of_first_5_coins = cg.get_coins_list()[0: 5]

    # extracting list of names of first 5 coins
    names_list_of_first_5_coins = list(
        map(lambda x: x['name'], list_of_first_5_coins)
    )

    # getting list of price of first 5 coins from CoinGeckoAPI
    price_list_of_first_5_coins = list(
        map(lambda x: cg.get_price(ids=x['id'], vs_currencies='usd')[x['id']]['usd'], list_of_first_5_coins)
    )

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
            }

    draw_bar_chart(
        names_list_of_first_5_coins,
        price_list_of_first_5_coins,
        "Cryptocurrency names",
        "price(usd)",
        "Crytocurrency data",
        font=font
    )

    draw_pie_chart(
        names_list_of_first_5_coins,
        price_list_of_first_5_coins,
        'Cryptocurrency data'
    )







