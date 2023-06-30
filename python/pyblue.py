# import bluetooth


# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print(nearby_devices)
# discovery = bluetooth.DeviceDiscoverer()

# print("Searching for nearby Bluetooth devices...")
# # devices = discovery.discover(10, True, True)

# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name))
# # for addr, name in discovery:#devices.items():
# #     print(f"Found device: {name} ({addr})")
# #     # print("  {} - {}".format(addr, name))


# import bluetooth, subprocess
# nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True, flush_cache=True, lookup_class=False)




# # To find the bluetooth device of near location  
# import bluetooth
# print( "performing inquiry...")
# devices = bluetooth.discover_devices(lookup_names=True)
# print(type(devices))
# print("Devices found: %s" % len(devices))
# for item in devices:
#     print(item)






# ## Important
# import asyncio
# from bleak import discover

# async def scan_devices():
#     devices = await discover()

#     for d in devices:
#          print(devices)


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(scan_devices())


#++++++++++++++++++++++++++++++++ Proper searching devices with Name +++++++++++++++++

    import asyncio
    from bleak import discover
    from bleak import BleakScanner

    async def scan_devices():
        print('Searching for the nearest bluetooth devices  ....... \n')
        devices = await BleakScanner.discover()

        for device in devices:
            print("Device Name  : ", device.name)
            print("Address      : ", device.address)
            print("Metadata     : ", device.metadata)
            print("RSSI         : ", device.rssi)
            print("")

    if __name__ == "__main__":
        # Create an event loop
        loop = asyncio.new_event_loop()

        # Set the event loop as the default event loop
        asyncio.set_event_loop(loop)

        # Run the async function in the event loop
        loop.run_until_complete(scan_devices())



