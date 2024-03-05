from PIL import Image
import sys

def Resize(img, scale):

    w, h = img.size

    (width, height) = (img.width // scale, img.height // scale)
    img = img.resize((width, height))
    w, h = img.size
    return img
def Gray(img):

    img = img.convert('1')
    return img


for infile in sys.argv[1:]:
    try:
        with Image.open('img/' + infile) as img:
            img_resized = Resize(img, 7)
            img_gray = Gray(img_resized)
            w, h = img_gray.size
            info = img_gray.load()

            with open('ascii.txt', 'w') as txt:

                for i in range(h):  
                    for j in range(w):  
                        if 0 <= j < w and 0 <= i < h:  
                            if info[j, i] == 255:
                                txt.write('.')
                            if info[j, i] == 0:
                                txt.write(' ')
                        else:
                            
                            txt.write('O')  

                    txt.write('\n')

    except OSError:
        print('Error trying to open the image')

    