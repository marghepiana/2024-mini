#!/usr/bin/env python3
"""
This program scans for Bluetooth signals using the micropython standard library.

https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble#passive-scan-for-nearby-devices-for-5-seconds-observer
"""

import asyncio
import aioble


async def ble_scan():
    async with aioble.scan(duration_ms=5000) as scanner:
        async for result in scanner:
            name = result.name()
            print(name, result.rssi, end=" ")
            #            for m in result.manufacturer():
            #                print(m, end=" ")
            for s in result.services():
                print(s)


try:
    asyncio.run(ble_scan())
finally:
    aioble.stop()
