def grayscale(red, green, blue):
    sum = red + green + blue
    average = sum / 3
    return average

def to_hex(red, green, blue):
    red_str = "%02x" % red
    green_str = "%02x" % green
    blue_str = "%02x" % blue
    return "#" + red_str + green_str + blue_str
