def grayscale(red, green, blue):
    la = red + green + blue
    lb = la / 3
    return lb

def to_hex(red, green, blue):
    la = "%02x" % red
    lb = "%02x" % green
    lc = "%02x" % blue
    return "#" + la + lb + lc
