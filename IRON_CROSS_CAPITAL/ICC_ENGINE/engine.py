import socketio
import yfinance as yf
import time
import random

sio = socketio.Client()

# Tracking Forex Pairs
PAIRS = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "USDCAD=X"]
current = 0

@sio.event
def connect():
    print("🛡️ ICC ENGINE: Connected to Live Bridge")

def start_stream():
    global current
    while True:
        ticker_symbol = PAIRS[current]
        try:
            # Fetching live data from Yahoo Finance
            data = yf.Ticker(ticker_symbol).fast_info
            price = data.last_price
            
            # Formatting name (e.g., EURUSD=X to EUR/USD)
            display_name = ticker_symbol.replace("=X", "")
            display_name = f"{display_name[:3]}/{display_name[3:]}"

            payload = {
                "time": time.strftime("%H:%M:%S"),
                "asset": display_name,
                "price": round(float(price), 5),
                "vol": "{:,}".format(random.randint(1200, 5000)),
                "side": "BUY" if price > data.open else "SELL"
            }
            
            # Sending data to your Vercel Dashboard
            sio.emit('new_whale', payload)
            print(f"🔥 SENT TO LIVE: {payload['asset']} | {payload['price']}")
            
            # Move to next pair
            current = (current + 1) % len(PAIRS)
            
        except Exception as e:
            print(f"⚠️ Skip {ticker_symbol}: {e}")
            current = (current + 1) % len(PAIRS)
            
        time.sleep(3) 

if __name__ == '__main__':
    try:
        # REPLACE THE LINK BELOW WITH YOUR ACTUAL VERCEL URL
        sio.connect('https://your-project-name.vercel.app', transports=['websocket'])
        start_stream()
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        print("💡 Check your Vercel URL and make sure your internet is on!")