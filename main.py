import json
import requests
import pandas as pd


def get_data(url):

    response = requests.get(url)

    data = json.loads(response.text)
    data = data['data']

    return data


def prcs_data(data):

    df_list = []
    for i in range(len(data)):
        dct = {k: [v] for k, v in data[i].items()}
        df = pd.DataFrame.from_dict(dct)
        df_list.append(df)

    merged = pd.concat(df_list, ignore_index=True, sort=False)

    return merged


def main():

    url1 = 'https://stoicquotesapi.com/v1/api/quotes'
    url2 = 'https://stoicquotesapi.com/v1/api/quotes?page=2'
    url3 = 'https://stoicquotesapi.com/v1/api/quotes?page=3'
    url4 = 'https://stoicquotesapi.com/v1/api/quotes?page=4'
    url5 = 'https://stoicquotesapi.com/v1/api/quotes?page=5'
    url6 = 'https://stoicquotesapi.com/v1/api/quotes?page=6'

    data1 = get_data(url1)
    data2 = get_data(url2)
    data3 = get_data(url3)
    data4 = get_data(url4)
    data5 = get_data(url5)
    data6 = get_data(url6)

    df1 = prcs_data(data1)
    df2 = prcs_data(data2)
    df3 = prcs_data(data3)
    df4 = prcs_data(data4)
    df5 = prcs_data(data5)
    df6 = prcs_data(data6)

    full_data = pd.concat([df1, df2, df3, df4, df5, df6],
                          ignore_index=True, sort=False)

    full_data.to_csv('./data/quotes.csv', index=False)


if __name__ == '__main__':

    main()
