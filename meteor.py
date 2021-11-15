from PIL import Image

img = Image.open("meteor_challenge_01.png")
size = w,h = img.size
data = img.load()

# Returns the number of stars and meteors in the sky
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

# Returns the number of meteors that will fall on water
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
            
print(sky_couting(data))
print(meteor_on_water(data))
