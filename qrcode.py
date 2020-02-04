# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# Take the string which we want to convert into the QR code
s = input("Enter the link or text you want to generate qrcode for: ")
  
# Generate QR code 
url = pyqrcode.create(s) 

#Take the name of the file with which you want to save it
name=input("Enter the name of the qrcode file: ")
name=name+".svg"
  
# Create and save the file
url.svg(name, scale = 10) 