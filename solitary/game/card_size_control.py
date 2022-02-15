from PIL import Image
import numpy as np

print("This is my Image work")

#image:

#cards
# A_Clover = Image.open("image/Card/Clover/A_Clover.png")
# c2_Clover = Image.open("image/Card/Clover/2_Clover.png")
# c3_Clover = Image.open("image/Card/Clover/3_Clover.png")
# c4_Clover = Image.open("image/Card/Clover/4_Clover.png")
# c5_Clover = Image.open("image/Card/Clover/5_Clover.png")
# c6_Clover = Image.open("image/Card/Clover/6_Clover.png") 
# c7_Clover = Image.open("image/Card/Clover/7_Clover.png")
# c8_Clover = Image.open("image/Card/Clover/8_Clover.png")
# c9_Clover = Image.open("image/Card/Clover/9_Clover.png")
# c10_Clover = Image.open("image/Card/Clover/10_Clover.png")
# cJ_Clover = Image.open("image/Card/Clover/J_Clover.png")
# cQ_Clover = Image.open("image/Card/Clover/Q_Clover.png")
# cK_Clover = Image.open("image/Card/Clover/K_Clover.png")

# A_Heart = Image.open("image/Card/Heart/A_Heart.png")
# c2_Heart = Image.open("image/Card/Heart/2_Heart.png")
# c3_Heart = Image.open("image/Card/Heart/3_Heart.png")
# c4_Heart = Image.open("image/Card/Heart/4_Heart.png")
# c5_Heart = Image.open("image/Card/Heart/5_Heart.png")
# c6_Heart = Image.open("image/Card/Heart/6_Heart.png")
# c7_Heart = Image.open("image/Card/Heart/7_Heart.png")
# c8_Heart = Image.open("image/Card/Heart/8_Heart.png")
# c9_Heart = Image.open("image/Card/Heart/9_Heart.png")
# c10_Heart = Image.open("image/Card/Heart/10_Heart.png")
# cJ_Heart = Image.open("image/Card/Heart/J_Heart.png")
# cQ_Heart = Image.open("image/Card/Heart/Q_Heart.png")
# cK_Heart = Image.open("image/Card/Heart/K_Heart.png")

# A_Diamond = Image.open("image/Card/Diamond/A_Diamond.png")
# c2_Diamond = Image.open("image/Card/Diamond/2_Diamond.png")
# c3_Diamond = Image.open("image/Card/Diamond/3_Diamond.png")
# c4_Diamond = Image.open("image/Card/Diamond/4_Diamond.png")
# c5_Diamond = Image.open("image/Card/Diamond/5_Diamond.png")
# c6_Diamond = Image.open("image/Card/Diamond/6_Diamond.png")
# c7_Diamond = Image.open("image/Card/Diamond/7_Diamond.png")
# c8_Diamond = Image.open("image/Card/Diamond/8_Diamond.png")
# c9_Diamond = Image.open("image/Card/Diamond/9_Diamond.png")
# c10_Diamond = Image.open("image/Card/Diamond/10_Diamond.png")
# cJ_Diamond = Image.open("image/Card/Diamond/J__Diamond.png")
# cQ_Diamond = Image.open("image/Card/Diamond/Q_Diamond.png")
# cK_Diamond = Image.open("image/Card/Diamond/K_Diamond.png")

# A_Pica = Image.open("image/Card/Pica/A_Pica.png")
# c2_Pica = Image.open("image/Card/Pica/2_Pica.png")
# c3_Pica = Image.open("image/Card/Pica/3_Pica.png")
# c4_Pica = Image.open("image/Card/Pica/4_Pica.png")
# c5_Pica = Image.open("image/Card/Pica/5_Pica.png")
# c6_Pica = Image.open("image/Card/Pica/6_Pica.png")
# c7_Pica = Image.open("image/Card/Pica/7_Pica.png")
# c8_Pica = Image.open("image/Card/Pica/8_Pica.png")
# c9_Pica = Image.open("image/Card/Pica/9_Pica.png")
# c10_Pica = Image.open("image/Card/Pica/10_Pica.png")
# cJ_Pica = Image.open("image/Card/Pica/J_Pica.png")
# cQ_Pica = Image.open("image/Card/Pica/Q_Pica.png")
# cK_Pica = Image.open("image/Card/Pica/K_Pica.png")

running = True
while running:
    st = "image/Card/"
    stX = "image/Card_resize/"
    i =0
    while i < 52:
        st3 =""
        i2 = int(i%13)
        i2+=1
        if i2 == 1:
            # print("\tA")
            st3 = "A"
        elif i2 == 11:
            st3 ="J"
            # print("\tJ")
        elif i2 == 12:
            st3 = "Q"
            # print("\tQ")
        elif i2 == 13:
            st3 = "K"
            # print("\tK")
        else:
            st3 = str(i2)
            # print()
        if i ==0 or i==13 or i ==26 or i==39:
            print(" == ", st , "XXX")
        print(i2, end="")
        if i < 13:
            st2 = "Clover/"
            st4 = st+st2+st3+"_Clover.png"
            st5 = stX +st2+st3+"_Clover.png"
            print("\t", st4)
            print("\t", st5)
        elif i < 26:
            st2 = "Diamond/"
            st4 = st+st2+st3+"_Diamond.png"
            st5 = stX+st2+st3+"_Diamond.png"
            print("\t", st4)
            print("\t", st5)
        elif i < 39:
            st2 = "Heart/"
            st4 = st+st2+st3+"_Heart.png"
            st5 = stX+st2+st3+"_Heart.png"
            print("\t", st4)
            print("\t", st5)
        else:
            st2 = "Pica/"
            st4 = st+st2+st3+"_Pica.png"
            st5 = stX+st2+st3+"_Pica.png"
            print("\t", st4)
            print("\t", st5)
            
        
        # gthis section isto resize and reallocate
        basewidth = 80
        imageS = st4
        img = Image.open(imageS)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(st5)
            
            
        i+=1
        
    # if i == 99:
    running = False
        
    i+=1
    






