import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print("✅ SUCCESS: Connected to the Dashboard!")

@sio.event
def disconnect():
    print("❌ Disconnected from server.")

try:
    sio.connect('http://localhost:5173')
    
    # This loop keeps it running so it doesn't just "exit"
    while True:
        test_data = {
            "time": time.strftime("%H:%M:%S"),
            "price": "67420.00",
            "size": "999.9", # Big number so you can't miss it
            "side": "BUY"
        }
        sio.emit('whale_data', test_data)
        print(f"🚀 [SENT] {test_data['time']} - 999.9 BTC BUY")
        time.sleep(5) # Wait 5 seconds before sending again
        
except Exception as e:
    print(f"🚨 ERROR: {e}")