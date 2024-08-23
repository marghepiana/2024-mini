# Exercise 03: applications of analog input

Connect the photocell using the 10k ohm resistor as a voltage divider
[circuit](../doc/photocell.md).
The 10k ohm resistor connects to "3V3" and to ADC2.
The photocell connects to the ADC2 and to AGND.
Polarity is not important for this resistor and photocell.

The MicroPython
[machine.ADC](https://docs.micropython.org/en/latest/library/machine.ADC.html)
class is used to read the analog voltage from the photocell.
The `machine.ADC(id)` value corresponds to the "GP" pin number.
On the Pico W, GP28 is ADC2, accessed with `machine.ADC(28)`.

## Questions

Let's "calibrate" the light sensor to be meaningful.
These values will change with room illumination and the specific photocell you have.
We are just getting rough estimates, something other than the default values I used.
Experiment to find approximate max_bright and min_bright values that:

* max_bright: make the LED duty cycle about 100% when in bright light (sunlight, room light)
* min_bright: make the LED duty cycle about 0% when in very dim light (dark room, covered with hand)

Please put these values in the exercise03.json file and read them with your own version of exercise03.py.
This exercise03.json and exercise03.py should be in your own Git repo, and are the "answers" for Exercise 03.

## Notes

Pico MicroPython time.sleep() doesn't error for negative values even though such are obviously incorrect--it is undefined for a system to sleep for negative time.
Duty cycle greater than 1 is undefined, so we clip the duty cycle to the range [0, 1].
