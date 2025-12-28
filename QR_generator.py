import qrcode 
url = input("Enter the url for which you want the scanner: ")
filename = input("Name of the file you want to save the scanner into: ")
if not (filename.endswith('.png')):
    filename = filename + '.png'

scanner = qrcode.make(url)
scanner.save(filename)