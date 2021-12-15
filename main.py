from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    cg = CoinGeckoAPI()
    list_of_first_5_coins = cg.get_coins_list()[0: 5]

    names_list_of_first_5_coins = list(map(lambda x: x['name'], list_of_first_5_coins))
    price_list_of_first_5_coins = list(
        map(lambda x: cg.get_price(ids=x['id'], vs_currencies='usd')[x['id']]['usd'], list_of_first_5_coins)
    )

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
            }

    X_axis = np.arange(len(names_list_of_first_5_coins))

    # for bar chart
    plt.bar(X_axis, price_list_of_first_5_coins, 0.4, label='Cryptocurrencies')
    plt.xticks(X_axis, names_list_of_first_5_coins)
    plt.xlabel("Cryptocurrency names", fontdict=font)
    plt.ylabel("price(usd)", fontdict=font)
    plt.title('Crytocurrency data')
    plt.legend()
    plt.show()

    # for pie chart
    plt.pie(price_list_of_first_5_coins, labels=names_list_of_first_5_coins, autopct='%1.2f%%')
    plt.title('Crytocurrency data')
    plt.show()







