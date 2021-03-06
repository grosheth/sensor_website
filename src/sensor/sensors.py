# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht


def main():
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        

        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        print(error.args[0])
        return
    except Exception as error:
        dhtDevice.exit()
        raise error
        return

    return temperature_c, humidity

if __name__ == '__main__':
    main()