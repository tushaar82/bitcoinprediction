import configparser
import pandas as pd
from ta.utils import dropna
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator

# Load datas
df = pd.read_csv('ETC-USD.csv', sep=',')
indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2,fillna=True)
rsi_21 = RSIIndicator(close = df['Close'], window = 21)
df['bb_bbm'] = indicator_bb.bollinger_mavg()
df['bb_bbh'] = indicator_bb.bollinger_hband()
df['bb_bbl'] = indicator_bb.bollinger_lband()
df["rsi_21"] = rsi_21.rsi()

df['pivot'] =( df['High'] + df['Low'] + df['Close']) /3

#Support 1 (S1)=(Pivot Point∗2)−Previous High
#Support 2 (S2)=Pivot Point−(Previous High−Previous Low)
#Support 3 = Pivot Point – (Resistance 2 – Support 2)
#Resistance 3 = (Pivot Point – Support 2) + Resistance 2

df['s1'] = (df['pivot']*2) - df['High']
df['s2'] = df['pivot'] - (df['High'] - df['Low'])
df['s3'] = df['pivot']

df['r1'] = (df['pivot']*2) + df['High']
df['r2'] = df['pivot'] + (df['High'] - df['Low'])

df['s3'] = df['pivot'] - (df['r2']-df['s2'])

df['r3'] = (df['pivot']-df['s2']) + df['r2']

bb_middle = round(df['bb_bbm'].tail(1).item(),2)
strbb_middle ="{}".format(bb_middle)

bb_high = round(df['bb_bbh'].tail(1).item(),2)
strbb_high ="{}".format(bb_high)

bb_low = round(df['bb_bbl'].tail(1).item(),2)
strbb_low ="{}".format(bb_low)

rsi =round( df['rsi_21'].tail(1).item(),2)
strrsi ="{}".format(rsi)

pivot = round(df['pivot'].tail(1).item(),2)
strpivot ="{}".format(pivot)

s1 = round(df['s1'].tail(1).item(),2)
strs1 ="{}".format(s1)
s2 = round(df['s2'].tail(1).item(),2)
strs2 ="{}".format(s2)
s3 = round(df['s3'].tail(1).item(),2)
strs3 ="{}".format(s3)

r1 = round(df['r1'].tail(1).item(),2)
strr1 ="{}".format(r1)
r2 = round(df['r2'].tail(1).item(),2)
strr2 ="{}".format(r2)
r3 = round(df['r3'].tail(1).item(),2)
strr3 ="{}".format(r3)

predicted_close = round(df['Close'].tail(1).item(),2)
strpredicted_close="{}".format(predicted_close)

yesterday_close = round(df['Close'].iloc[-2].item(),2)
stryesterday_close ="{}".format(yesterday_close)

todays_open = round(df['Open'].tail(1).item(),2)
strtodays_open ="{}".format(todays_open)


#print(strpredicted_close)
d1 = (2012, 7, 20)
d2 = (2012, 7, 21)
d3 = (2012, 7, 22)
d4 = (2012, 7, 23)
d5 = (2012, 7, 24)

v1 = 42
v2 = 49
v3 = 52
v4 = 40
v5 = 56

sd1 = strtodays_open ="{}".format(d1)
sd2 = strtodays_open ="{}".format(d2)
sd3 = strtodays_open ="{}".format(d3)
sd4 = strtodays_open ="{}".format(d4)
sd5 = strtodays_open ="{}".format(d5)

sv1 = strtodays_open ="{}".format(v1)
sv2 = strtodays_open ="{}".format(v2)
sv3 = strtodays_open ="{}".format(v3)
sv4 = strtodays_open ="{}".format(v4)
sv5 = strtodays_open ="{}".format(v5)

config = configparser.ConfigParser()
config.add_section("predicted")
config['predicted']['predicted_close']=strpredicted_close
config['predicted']['yesterday_close']=stryesterday_close
config['predicted']['rsi']=strrsi
config['predicted']['todays_open']=strtodays_open
config['predicted']['bb_up']=strbb_high
config['predicted']['bb_middle']=strbb_middle
config['predicted']['bb_lower']=strbb_low
config['predicted']['s3']=strs3
config['predicted']['s2']=strs2
config['predicted']['s1']=strs1
config['predicted']['pivot']=strpivot
config['predicted']['r3']=strr3
config['predicted']['r2']=strr2
config['predicted']['r1']=strr1
config['predicted'] ['d1'] = sd1
config['predicted'] ['d2'] = sd2
config['predicted'] ['d3'] = sd3
config['predicted'] ['d4'] = sd4
config['predicted'] ['d5'] = sd5
config['predicted'] ['v1'] = sv1
config['predicted'] ['v2'] = sv2
config['predicted'] ['v3'] = sv3
config['predicted'] ['v4'] = sv4
config['predicted'] ['v5'] = sv5

config.write(open("weth.ini","w"))
with open('weth.ini','w')as configfile:
    config.write(configfile)