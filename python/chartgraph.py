import matplotlib.pyplot as plt
import numpy as np
import asyncio
from bleak import discover
from bleak import BleakScanner, BleakClient

async def scan_devices():
    global selected_device_address
    print('Searching for the nearest Bluetooth devices....\n')
    devices = await BleakScanner.discover()

    # Print a numbered list of the discovered devices
    print("Discovered devices:")
    for i, device in enumerate(devices):
        print(f"{i+1}. {device.name} ({device.address})")

    # Prompt the user to select a device
    while True:
        selection = input("Select a device (1-%d): " % len(devices) +'\n')
        try:
            index = int(selection) - 1
            if index >= 0 and index < len(devices):
                device = devices[index]
                break
        except ValueError:
            pass
        print("Invalid selection, try again.")
    selected_device_address = device.address
    print(f"Selected device: {device.name} ({selected_device_address})" +'\n')
    
    try:
        print(f"Connecting to {selected_device_address}...")
        client = BleakClient(selected_device_address)
        await client.connect(timeout=timeout)
        connected = True
        print("Connected!")
        uuid = "14839ac4-7d7e-415c-9a42-167340cf2339"
        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2)
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        xdata, ydata = [], []
        def update_line(data):
            x, y = data
            xdata.append(x)
            ydata.append(y)
            line.set_data(xdata, ydata)
            ax.relim()
            ax.autoscale_view(True, True, True)
            plt.draw()
            plt.pause(0.01)
        print("Reading data...")
        while connected:
            try:
                await client.start_notify(uuid, lambda sender, data: update_line((len(data_array), int.from_bytes(data, byteorder='little', signed=False))))
                await asyncio.sleep(5)
                await client.stop_notify(uuid)
            except Exception as e:
                print("Error: " + str(e))
                connected = False
        print("Displaying line graph...")
        plt.show()
    except:
        print("Connection error. Retrying...")
        await asyncio.sleep(1)

def on_disconnect(client):
    global connected
    connected = False
    print("Disconnected!")
    asyncio.get_event_loop().stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    selected_device_address = ""
    connected = False
    timeout = 30.0
    try:
        loop.run_until_complete(scan_devices())
    finally:
        loop.close()
