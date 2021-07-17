from flask import Flask,render_template
import pandas as pd
import configparser
config = configparser.ConfigParser()


app=Flask(__name__)
@app.route('/')
def log():
    return render_template('login.html')


@app.route('/Bitchart')
def bitchart():
    config.read('wbtc.ini')

    predicted_close= config['predicted']['predicted_close']
    yesterdays_close=config['predicted']['yesterday_close']
    rsi_predicted=config['predicted']['rsi']
    todays_open=config['predicted']['todays_open']
    bb_up=config['predicted']['bb_up']
    bb_middle=config['predicted']['bb_middle']
    bb_lower=config['predicted']['bb_lower']
    ps3=config['predicted']['s3']
    ps2=config['predicted']['s2']
    ps1=config['predicted']['s1']
    pivot=config['predicted']['pivot']
    pr3=config['predicted']['r3']
    pr2=config['predicted']['r2']
    pr1=config['predicted']['r1']
    d1 = config['predicted']['d1']
    d2 = config['predicted']['d2']
    d3 = config['predicted']['d3']
    d4 = config['predicted']['d4']
    d5 = config['predicted']['d5']

    v1 = config['predicted']['v1']
    v2 = config['predicted']['v2']
    v3 = config['predicted']['v3']
    v4 = config['predicted']['v4']
    v5 = config['predicted']['v5']

    return render_template('Bitcoin-chart.html',
        d1=d1,
        d2=d2,
        d3=d3,
        d4=d4,
        d5=d5,
        v1=v1,
        v2=v2,
        v3=v3,
        v4=v4,
        v5=v5,
        predicted_close = predicted_close,
        yesterdays_close = yesterdays_close,
        rsi_predicted=rsi_predicted,
        todays_open=todays_open,
        bb_up=bb_up,
        bb_middle=bb_middle,
        bb_lower=bb_lower,
        ps3=ps3,
        ps2=ps2,
        ps1=ps1,
        pivot=pivot,
        pr3=pr3,
        pr2=pr2,
        pr1=pr1
        )


@app.route('/Litchart')
def litchart():
    config.read('wlit.ini')

    predicted_close= config['predicted']['predicted_close']
    yesterdays_close=config['predicted']['yesterday_close']
    rsi_predicted=config['predicted']['rsi']
    todays_open=config['predicted']['todays_open']
    bb_up=config['predicted']['bb_up']
    bb_middle=config['predicted']['bb_middle']
    bb_lower=config['predicted']['bb_lower']
    ps3=config['predicted']['s3']
    ps2=config['predicted']['s2']
    ps1=config['predicted']['s1']
    pivot=config['predicted']['pivot']
    pr3=config['predicted']['r3']
    pr2=config['predicted']['r2']
    pr1=config['predicted']['r1']
    d1 = config['predicted']['d1']
    d2 = config['predicted']['d2']
    d3 = config['predicted']['d3']
    d4 = config['predicted']['d4']
    d5 = config['predicted']['d5']

    v1 = config['predicted']['v1']
    v2 = config['predicted']['v2']
    v3 = config['predicted']['v3']
    v4 = config['predicted']['v4']
    v5 = config['predicted']['v5']

    return render_template('Litcoin-chart.html',
        d1=d1,
        d2=d2,
        d3=d3,
        d4=d4,
        d5=d5,
        v1=v1,
        v2=v2,
        v3=v3,
        v4=v4,
        v5=v5,
        predicted_close = predicted_close,
        yesterdays_close = yesterdays_close,
        rsi_predicted=rsi_predicted,
        todays_open=todays_open,
        bb_up=bb_up,
        bb_middle=bb_middle,
        bb_lower=bb_lower,
        ps3=ps3,
        ps2=ps2,
        ps1=ps1,
        pivot=pivot,
        pr3=pr3,
        pr2=pr2,
        pr1=pr1
        )

@app.route('/Ethchart')
def ethchart():
    config.read('weth.ini')

    predicted_close= config['predicted']['predicted_close']
    yesterdays_close=config['predicted']['yesterday_close']
    rsi_predicted=config['predicted']['rsi']
    todays_open=config['predicted']['todays_open']
    bb_up=config['predicted']['bb_up']
    bb_middle=config['predicted']['bb_middle']
    bb_lower=config['predicted']['bb_lower']
    ps3=config['predicted']['s3']
    ps2=config['predicted']['s2']
    ps1=config['predicted']['s1']
    pivot=config['predicted']['pivot']
    pr3=config['predicted']['r3']
    pr2=config['predicted']['r2']
    pr1=config['predicted']['r1']
    d1 = config['predicted']['d1']
    d2 = config['predicted']['d2']
    d3 = config['predicted']['d3']
    d4 = config['predicted']['d4']
    d5 = config['predicted']['d5']

    v1 = config['predicted']['v1']
    v2 = config['predicted']['v2']
    v3 = config['predicted']['v3']
    v4 = config['predicted']['v4']
    v5 = config['predicted']['v5']

    return render_template('Eth-chart.html',
        d1=d1,
        d2=d2,
        d3=d3,
        d4=d4,
        d5=d5,
        v1=v1,
        v2=v2,
        v3=v3,
        v4=v4,
        v5=v5,
        predicted_close = predicted_close,
        yesterdays_close = yesterdays_close,
        rsi_predicted=rsi_predicted,
        todays_open=todays_open,
        bb_up=bb_up,
        bb_middle=bb_middle,
        bb_lower=bb_lower,
        ps3=ps3,
        ps2=ps2,
        ps1=ps1,
        pivot=pivot,
        pr3=pr3,
        pr2=pr2,
        pr1=pr1
        )


if __name__=="main":
    app.run(debug=True)