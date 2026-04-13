import socketio
import yfinance as yf
import time
import random

sio = socketio.Client()

# This list ensures you track more than just EUR/USD
PAIRS = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "USDCAD=X"]
current = 0

@sio.event
def connect():
    print("🛡️ ICC ENGINE: Connected to Bridge")

def start_stream():
    global current
    while True:
        ticker_symbol = PAIRS[current]
        try:
            # Fetching the live data
            data = yf.Ticker(ticker_symbol).fast_info
            price = data.last_price
            
            # Formatting the name (e.g., GBPUSD=X to GBP/USD)
            display_name = ticker_symbol.replace("=X", "")
            display_name = f"{display_name[:3]}/{display_name[3:]}"

            payload = {
                "time": time.strftime("%H:%M:%S"),
                "asset": display_name,
                "price": round(float(price), 5),
                "vol": "{:,}".format(random.randint(1200, 5000)),
                "side": "BUY" if price > data.open else "SELL"
            }
            
            sio.emit('new_whale', payload)
            print(f"🔥 SENT: {payload['asset']} | {payload['price']}")
            
            # FORCE move to the next pair in the list
            current = (current + 1) % len(PAIRS)
            
        except Exception as e:
            print(f"⚠️ Skip {ticker_symbol}: {e}")
            current = (current + 1) % len(PAIRS)
            
        time.sleep(3) 

if __name__ == '__main__':
    try:
        sio.connect('https://my-terminal.vercel.app')
        start_stream()
    except:
        print("❌ Dashboard not found. Run 'npm run dev' first!")