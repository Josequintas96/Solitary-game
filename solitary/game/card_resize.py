from PIL import Image

basewidth = 80
imageS = "image/card_empty.png"
img = Image.open(imageS)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('image/special_R/card_emptyR.png')