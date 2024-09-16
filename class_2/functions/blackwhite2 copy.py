from cs1media import *

def luma(p):
    r,g,b = p
    return int(0.299*r + 0.587*g + 0.114*b)
    # return int(r + g + b)


white = (255,255,255)
black = (0,0,0)

def black_white(img,threshold):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            v = luma(img.get(x,y))
            if v > threshold:
                img.set(x,y,white)
            else:
                img.set(x,y,black)

pic = load_picture("../photos/yuna1.jpg")
black_white(pic,111)
pic.show()


