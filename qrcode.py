import pyqrcode
import png
from pyqrcode import QRCode
  
input_string=str(input("Enter Text or link:- "))   #taking input link or text

file_name=str(input("Enter the name of image you want to use:- "))  #entering name of output of qrcode

if (len(input_string) != 0):                                        #checking if there is actual text or not

    
    url = pyqrcode.create(input_string)                             #creating qr code

    name_svg=file_name+".svg"                                       #nameing of svg
    name=file_name+".png"                                           #nameing of png

    url.svg(name_svg, scale = 8)                                    #creating svg of qr code
    url.png(name, scale = 6)                                        #creating png of qr code
else:
    print("Check if you have given correct input.")