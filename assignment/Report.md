

For the three assignments, the original codes provided were overwritten with our modified codes. 

Exercise 1:
The new values we found were a minimum of 14000 and a maximum of 55000. These were approximately the lowest and highest values the photocell read.
- [Link to video demo for exercise 1 showing the photocel readings and the light turning on and off based on the readings ](https://drive.google.com/file/d/1TNY0iuxiTV-cgtwoc1U1oIXnICd-V40Q/view?usp=sharing)


Exercise 2: In this exercise we changed the output of the speaker to play the theme song of Super Mario Bros. The notes and their durations were found at the following website: https://www.hackster.io/techarea98/super-mario-theme-song-with-piezo-buzzer-and-arduino-2cc461 
- [Link to the video demo for exercise 2 showing the Mario theme being played](https://drive.google.com/file/d/1TRnETztIHfEBiv2cLKIchmwxzG01nkb0/view?usp=sharing)


Exercise 3: 
In this exercise we created a game with our pico rasberry py and then we used firebase to upload the player's results. Every time the LED flashed the user had to press the button. We computed the average, minimum and maximum response time of the user for 10 flashes. We stored the result in a dictionary and we wrote them on a json file. Once we palyed the game and made sure everything was working we added the necessary lines to our code to uplaod the results to Firebase. To do so on our gmail email we made a firebase account and created a new project with a live database. We then connected our rasberry pi to the wifi, we then ran the code ans saw the results being uploaded in the live database

- [Link to video demo for exercise 3 showing game being played ](https://drive.google.com/file/d/1Ob-gdPL814_aEiASfZe3okjn7ZXL9xMf/view?usp=sharing).

- [Link to video demo for exercise 3 showing upload to firebase database](https://drive.google.com/file/d/1jrmWEuzFMgvX93u1EiXKI1lzVfm-9GVa/view?usp=share_link).

User Story: I first ran the code with the Raspberry Pi Pico plugged into my computer and played the button game, after seeing that my results were recorded on the pi pico, I logged into firebase with my email. I then went to the game project and then clicked the "Realtime Database" section where I saw that my results from the game were automatically uploaded to the cloud server.
