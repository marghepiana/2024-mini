#!/usr/bin/env python3
"""
This program scans for Wifi signals.

https://docs.micropython.org/en/latest/library/network.WLAN.html
"""

import network
import binascii

# MicroPython doesn't have "enum", so we use a dict()

Security = {
    0: "open",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK",
    5: "WPA2-Enterprise",
    6: "WPA3-PSK",
}
# Security values taken from:
# https://github.com/micropython/micropython/issues/10017#issuecomment-2143903717

wlan = network.WLAN(network.STA_IF)
# network.STA_IF constant configures the WiFi interface as a station (client).

wlan.active(True)

aps: list[tuple[bytes, bytes, int, int, int, int]] = wlan.scan()
# https://docs.micropython.org/en/latest/library/network.WLAN.html#network.WLAN.scan
# the format is not well-documented and is distinct between different models of board.
# People have been trying to figure it out:
# https://github.com/micropython/micropython/issues/10017

# Data format

# sort on RSSI, which is the 3rd element of each tuple
aps.sort(key=lambda x: x[3], reverse=True)

for w in aps:
    ssid = w[0].decode()
    bssid = binascii.hexlify(w[1]).decode()
    channel = w[2]
    rssi = w[3]  # Received Signal Strength Indicator [dBm]
    print(f"{ssid:25} {bssid} {channel:3} {rssi:3} {Security.get(w[4], w[4]):15}")
