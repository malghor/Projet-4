from PIL import Image, ImageDraw
from IPython.display import display
#===========================================================================
# Exercice 4

img1=Image.open("iguane.jpg")
display(img1)

largeur=img1.height
longueur=img1.width

definition=largeur*longueur
print(definition,"pixels")

#===========================================================================


x=300
y=140
couleur=img1.getpixel((x,y)) # couleur est un tuple

R,V,B=couleur
print("Les composantes R,V,B du pixel (x={},y={}) sont R={},V={} et B={}".format(x,y,R,V,B))

#===========================================================================
# Exercice 5

img2=Image.open("iguane2.jpg")
display(img2)
img3=img2.transpose(Image.FLIP_TOP_BOTTOM)
display(img3)

#==========================================================================
# Exercice 6

img3=Image.open("plane.jpg")
img3.show()

width,height=img3.size

TabPixel = img3.load()
for i in range(height):
  for j in range(width):
    pixel = TabPixel[j,i]
    gris = int((pixel[0] +pixel[1] +pixel[2])/3)
    p = (gris,gris,gris)
    TabPixel[j,i] = p
img3.show()

#==========================================================================
# Exercice 7

TabPixel = img1.load()
width,height=img1.size

for i in range(height):
  for j in range(width):
    pixel = TabPixel[j,i]
    p = (255-pixel[0],255-pixel[1],255-pixel[2])
    TabPixel[j,i] = p
img1.show()



