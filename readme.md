### **project proposal**
My project idea is a to make a spiderman platformer game. My inspiration for this project is the 1992 NES game spiderman: return of the sinister 6. It is a game I've owned for a few years now and I have literally never even beat the 1st level. I think it is achievable to make at least the platforming part of a game. 

### **Challenges**
I am currently studying the p5play documentation and wokring on getting some objects movable with physics. I found a sprite sheet of spiderman i plan to use but i have yet to make use of it in animation. I have been researching how to use sprite sheets in p5play/p5js and it is rather complicated to get it working. I made the descision to use a different platform to create my project in. for my project I used pygame, which is a python library for making games. I ran into manu issues with my spritesheet as the individual spirtes were not spaced incrementally nor were they the same dimension. I ended up have to manually map the spritesheet, to create the animations of spiderman running. jumping, and idle. My main breakthrough in this area came from this video: https://www.youtube.com/watch?v=ePiMYe7JpJo&ab_channel=CDcodes. with this tutorial I was able to test where my sprite frame was and where i needed to adjust to get the correct individual sprite. During the game creation I ran into confusion with the jump physics and how to add a sense of gravity, for this i consulted ChatGPT for help. It helped me with the jump and the collisions of the player and the platform so that the player could jump through a platform but land on top of it.   

### **Development plan**
I plan to get the physics working with objects by the end of the week. Then I plan to get the sprite sheet to work in p5play. Ihen once I have both working pieces I will combine them to make the platformer. After spending the first week an a half I had no movement or physics functionality in p5 play so i switched to pygame which had a very lengthy documentation page: https://www.pygame.org/docs/. This was critical to my development of the movement and game design itself. I have also watched many youtube videos on how to do things in pygame and how to animate sprites.  

### **week 1:**
I have been able to create sprites using p5play and its functions but I can not seem to get the movement to work, I have tried a bunch a different ways to implement the movement based on the p5play documentation but I think it is a library issue with the web editor not referncing the p5play library. 

### **Week 2:**
I have moved to using pygame instead of p5.js/p5 play, so far I have movement of an object set up but my sprite animations do not work at all.

### **week 3:**
I figured out how to animate my sprites finally. my run and jump animation only face one way so if you move spiderman left he is bascially backpeddling. Unfortunately I dont have enough time to mirror the sprites and map the mirrored leftsided sprites.   

### **Hosting on a live link**
I have been working to host my pygame on itch.io which python has a library to help convert pygame games into web accessable code for hosting called pygbag. I have watched multiple tutorials on how to run pygbag and have followed through all the steps but on itch.io the game wont run. I watched some of these tutorials early on to see if it was possible to live host a pygame game and most of the tutorials were a 5-7 step process encompassed in a 7-10 minute video, so it should be relatively easy to run but either my program has an error that is thrown when attempting host or I am doing a step wrong.


Here is a screen recording of my game running locally:
https://github.com/user-attachments/assets/58308f90-603f-4355-a16e-af968fa8c432

