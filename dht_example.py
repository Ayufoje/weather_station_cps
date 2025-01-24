import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4)
 
while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature_c, humidity) 
    except RuntimeError as error:        
        print(error.args[0])
        time.sleep(1.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(1.0)