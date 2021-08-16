import pygatt
from binascii import hexlify

adapter = pygatt.GATTToolBackend()

sensor_ids = {
    "temp_data": "f000aa01-0451-4000-b000-000000000000",
    "humidity_data": "f000aa21-0451-4000-b000-000000000000",
    "lux_data": "f000aa71-0451-4000-b000-000000000000",
    "batt_lvl": "f0002a19-0451-4000-b000-000000000000"
}

try:
    adapter.start()
    device = adapter.connect('80:6F:B0:F0:2B:95')   # target MAC address
    while True:
        value = device.char_read(sensor_ids["lux_data"])
        # print(f"Received data: {hexlify(value)}")
        print(value)
finally:
    adapter.stop()
