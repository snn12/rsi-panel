import urllib.request, json

def fetch(symbol="BTCUSDT", interval="60", limit=100, category="spot"):
    url = f"https://api.bybit.com/v5/market/kline?category={category}&symbol={symbol}&interval={interval}&limit={limit}"
    with urllib.request.urlopen(url, timeout=15) as r:
        data = json.loads(r.read().decode())
    lst = data["result"]["list"]
    # Bybit returns newest first -> reverse to oldest->newest
    lst = lst[::-1]
    closes = [float(x[4]) for x in lst]
    return closes, lst

def rsi_wilder(closes, period=14):
    if len(closes) < period+1:
        return None
    gains = []
    losses = []
    for i in range(1, len(closes)):
        ch = closes[i]-closes[i-1]
        gains.append(max(ch,0))
        losses.append(max(-ch,0))
    avg_g = sum(gains[:period])/period
    avg_l = sum(losses[:period])/period
    if avg_l == 0:
        return 100.0
    for i in range(period, len(gains)):
        avg_g = (avg_g*(period-1)+gains[i])/period
        avg_l = (avg_l*(period-1)+losses[i])/period
    if avg_l == 0:
        return 100.0
    rs = avg_g/avg_l
    return 100 - (100/(1+rs))

for label, interval in [("1H","60"),("4H","240"),("1D","D")]:
    try:
        closes, lst = fetch(interval=interval, limit=100)
        r = rsi_wilder(closes, 14)
        print(f"{label}: last_close={closes[-1]} RSI14={r:.2f} candles={len(closes)}")
    except Exception as e:
        print(f"{label} ERROR: {e}")
