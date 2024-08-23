# Exercise 02 - deterministic code

A common task in embedded systems is to repeat a task many times with a precise enough time interval.
Since we expect deterministic execution, there should be little variance in time to execute vs. what happens on a non-real-time system such as full Raspberry Pi with a non-real-time operating system or a laptop computer.
However, if the task is waiting on communication, IO or has random time delay, the execution time will vary.

## measuring elapsed time

The MicroPython
[time](https://docs.micropython.org/en/latest/library/time.html)
module has some missing and additional functions vs. the CPython
[time](https://docs.python.org/3/library/time.html)
module.
Many operations on microcontrollers concern time such as time delays or doing something on a strict periodic schedule, which is what utime can be used for.
Doing a periodic task with the highest precision can be done by specifying CPU ticks.
For tasks like flashing LEDs or sampling slowly updating sensors like photocells, CPU tick level precision is typically not needed.

For the variable "tic", in CPython on might be accustomed to using
[time.monotonic()](https://docs.python.org/3/library/time.html#time.monotonic)
but in current versions of MicroPython this function is not available.

Here we measure elapsed time with hardware in the loop.

Note: to transfer files such as
[exercise02.json](./exercise02.json)
to the Pico, use Thonny IDE "View - Files".
Then in the "Files" top window for "This Computer", navigate to the file to copy to the Pico.
Right click that file, and select "Upload to /" to copy the file to the Pico.

In this exercise, copy both "exercise02.py" and "exercise02.json" to the Pico so that the Pico can load the parameter file without relying on the computer.
Edit / run the exercise02.py script on the Pico -- with Thonny this is done from the Files tab by right-clicking exercise02.py and selecting "open in Thonny".
Thonny shows tab "[exercise02.py]" where the brackets `[]` indicate the file is remote on the Pico.

For future reference (not necessary for this specific exercise): to download a file that you've edited on the Pico back to your computer to upload to Git, in Thonny Files tab, right-click the file on the Pico and select "Download to ..." where "..." is the directory on your computer to save the file.

## Questions

### Question 01

Why do you think we would use a file (e.g. JSON file) for parameter storage instead of accepting the parameters as user `input()`, especially on an embedded system?

### Question 02

Why might we prefer to use a JSON file to store parameters instead of hard-coding values in the Python script?

### Question 03

Why is "time.ticks_diff(toc, tic)" used to determine elapsed time instead of "toc - tic"?
