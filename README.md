# Meteor Challenge

Dependencies:

`python3 -m pip install --upgrade pip `<br />
`python3 -m pip install --upgrade Pillow`

I used the PIL library to manipulate the image.
```python
from PIL import Image

img = Image.open("meteor_challenge_01.png")
size = w,h = img.size
data = img.load()
```

![image](meteor_challenge_01.png)

# Question 1 and 2
 
Count the number of Stars and Meteors.

```python
def sky_couting(data):
    colors = []
    for x in range(w):
        for y in range(h):
            color = data[x,y]
            hex_color = '#' + ''.join([hex(c)[2:].rjust(2,'0') for c in color])
            if hex_color == '#ff0000ff':
                colors.append('Meteors')
            elif hex_color == "#ffffffff":
                colors.append('Stars')

    stars = colors.count('Stars')
    meteors = colors.count('Meteors')
    string1 = "There is " + str(stars) + " stars in the sky\n"
    string2 = "There is " + str(meteors) + " meteors in the sky"
    return string1 + string2
```
The function runs through the array of pixels, and when a pixel has a value of white ('Stars') or red ('Meteors') it is added to the 'colors' list.
Afterwards, the amount of 'Stars' and 'Meteors' is returned, through the count() function. </br>
NOTE: I preferred to work with the pixels in the Hexadecimal form, line 29.

# Question 3
 
Count the number of Meteors.
```python
def meteor_on_water(data):
    meteors_on_water = 0
    for x in range(w):
        meteors = 0
        for y in range(h):
            color = data[x,y]
            hex_color = '#' + ''.join([hex(c)[2:].rjust(2,'0') for c in color])
            if hex_color == '#ff0000ff':
                meteors += 1 
            elif hex_color == '#0000ffff':
                meteors_on_water += meteors
                break

    return str(meteors_on_water) + " meteors will fall in the water"
```

The matrix is traversed column by column, adding each meteor found in the variable 'meteors', if there is a pixel of water (#0000ffff) in the column, these meteors are added to the variable 'meteors_on_water', if there is no water, the value of meteors in the column is reset to 0.

# Output
```
There is 315 stars in the sky
There is 328 meteors in the sky
105 meteors will fall in the water
```
# Hidden Phrase

Without a doubt, it was the part that I thought about the most and racked my brain, in the end I couldn't find that phrase, but I'll leave the main attempts and patterns found here:

* All columns that have a star or a meteor, the same type is not repeated, so it is possible to do some sort of order.
* I tried to decode the message line by line/column by column, using binary, meteor = 0 or 1 star = 1 or 0, and then translate the binary value to ASCII, but no readable phrase was found. I decoded only the sections that had water underneath, but nothing either.
* I tried to access the address https://scipio.tech, but I couldn't find anything that would help me.
* Also, I manipulated the image in photoshop, with the intention of finding the message in a visual way, but I don't believe that's the way.
