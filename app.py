import random
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def get_data():

    data = pd.read_csv('./data/quotes.csv', header=0)

    select = random.randint(0, 59)

    df_select = data[data.id == select]

    body = df_select.body.values[0]
    auth = df_select.author.values[0]

    return body, auth


@app.route('/')
def index():

    body, auth = get_data()

    return render_template('index.html', text1=body, text2=auth)


if __name__ == '__main__':

    app.run(debug=True)
