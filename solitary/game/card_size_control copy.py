from PIL import Image
import numpy as np

print("This is my Image work")

#image:

#cards
# A_Clover = Image.open("image/Clover/A_Clover.png")
# c2_Clover = Image.open("image/Clover/2_Clover.png")
# c3_Clover = Image.open("image/Clover/3_Clover.png")
# c4_Clover = Image.open("image/Clover/4_Clover.png")
# c5_Clover = Image.open("image/Clover/5_Clover.png")
# c6_Clover = Image.open("image/Clover/6_Clover.png") 
# c7_Clover = Image.open("image/Clover/7_Clover.png")
# c8_Clover = Image.open("image/Clover/8_Clover.png")
# c9_Clover = Image.open("image/Clover/9_Clover.png")
# c10_Clover = Image.open("image/Clover/10_Clover.png")
# cJ_Clover = Image.open("image/Clover/J_Clover.png")
# cQ_Clover = Image.open("image/Clover/Q_Clover.png")
# cK_Clover = Image.open("image/Clover/K_Clover.png")

# A_Heart = Image.open("image/Heart/A_Heart.png")
# c2_Heart = Image.open("image/Heart/2_Heart.png")
# c3_Heart = Image.open("image/Heart/3_Heart.png")
# c4_Heart = Image.open("image/Heart/4_Heart.png")
# c5_Heart = Image.open("image/Heart/5_Heart.png")
# c6_Heart = Image.open("image/Heart/6_Heart.png")
# c7_Heart = Image.open("image/Heart/7_Heart.png")
# c8_Heart = Image.open("image/Heart/8_Heart.png")
# c9_Heart = Image.open("image/Heart/9_Heart.png")
# c10_Heart = Image.open("image/Heart/10_Heart.png")
# cJ_Heart = Image.open("image/Heart/J_Heart.png")
# cQ_Heart = Image.open("image/Heart/Q_Heart.png")
# cK_Heart = Image.open("image/Heart/K_Heart.png")

# A_Diamond = Image.open("image/Diamond/A_Diamond.png")
# c2_Diamond = Image.open("image/Diamond/2_Diamond.png")
# c3_Diamond = Image.open("image/Diamond/3_Diamond.png")
# c4_Diamond = Image.open("image/Diamond/4_Diamond.png")
# c5_Diamond = Image.open("image/Diamond/5_Diamond.png")
# c6_Diamond = Image.open("image/Diamond/6_Diamond.png")
# c7_Diamond = Image.open("image/Diamond/7_Diamond.png")
# c8_Diamond = Image.open("image/Diamond/8_Diamond.png")
# c9_Diamond = Image.open("image/Diamond/9_Diamond.png")
# c10_Diamond = Image.open("image/Diamond/10_Diamond.png")
# cJ_Diamond = Image.open("image/Diamond/J__Diamond.png")
# cQ_Diamond = Image.open("image/Diamond/Q_Diamond.png")
# cK_Diamond = Image.open("image/Diamond/K_Diamond.png")

# A_Pica = Image.open("image/Pica/A_Pica.png")
# c2_Pica = Image.open("image/Pica/2_Pica.png")
# c3_Pica = Image.open("image/Pica/3_Pica.png")
# c4_Pica = Image.open("image/Pica/4_Pica.png")
# c5_Pica = Image.open("image/Pica/5_Pica.png")
# c6_Pica = Image.open("image/Pica/6_Pica.png")
# c7_Pica = Image.open("image/Pica/7_Pica.png")
# c8_Pica = Image.open("image/Pica/8_Pica.png")
# c9_Pica = Image.open("image/Pica/9_Pica.png")
# c10_Pica = Image.open("image/Pica/10_Pica.png")
# cJ_Pica = Image.open("image/Pica/J_Pica.png")
# cQ_Pica = Image.open("image/Pica/Q_Pica.png")
# cK_Pica = Image.open("image/Pica/K_Pica.png")

running = True
while running:
    st = "image/Card/"
    i =0
    while i < 52:
        # st3 =""
        # i2 = int(i%13)
        # i2+=1
        # print(i2, end="")
        # if i2 == 1:
        #     # print("\tA")
        #     st3 = "A"
        # elif i2 == 11:
        #     st3 ="J"
        #     # print("\tJ")
        # elif i2 == 12:
        #     st3 = "Q"
        #     # print("\tQ")
        # elif i2 == 13:
        #     st3 = "K"
        #     # print("\tK")
        # else:
        #     st3 = str(i2)
        #     # print()
        # if i ==0 or i==13 or i ==26 or i==39:
        #     print(st)
        # if i < 13:
        #     st2 = "Clover/"
        #     st4 = st+st2+st3+"_Clover.png"
        #     print("\t", st4)
        # elif i < 26:
        #     st2 = "Diamond/"
        #     st4 = st+st2+st3+"_Diamond.png"
        #     print("\t", st4)
        # elif i < 39:
        #     st2 = "Heart/"
        #     st4 = st+st2+st3+"_Heart.png"
        #     print("\t", st4)
        # else:
        #     st2 = "Pica/"
        #     st4 = st+st2+st3+"_Pica.png"
        #     print("\t", st4)
        i+=1
    if i == 99:
        running = False
        
    i+=1






