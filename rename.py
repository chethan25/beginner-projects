# Rename files of different extensions in bulk.
import os 
import sys
# Files path are accepted from command line arguments

path = sys.argv[1]
a = 1

for filename in os.listdir(path):
    src = path + filename
    d = 'IMG' + '_' + str(a)
    djpg = path + d + '.jpg'
    dpng = path + d + '.png'
    djpeg = path + d + '.jpeg'
    djfif = path + d + '.jfif'
    dmp4 = path + d + '.mp4'
    dgif = path + d + '.gif'
    dJPG = path + d + '.JPG'
    # Renaming files based on extensions
    
    if filename[-3:] == 'jpg':
        os.rename(src, djpg)
        a+=1

    if filename[-3:] == 'png':
        os.rename(src, dpng)
        a+=1

    if filename[-4:] == 'jpeg':
        os.rename(src, djpeg)
        a+=1
        
    if filename[-4:] == 'jfif':
        os.rename(src, djfif)
        a+=1
        
    if filename[-3:] == 'mp4':
        os.rename(src, dmp4)
        a+=1

    if filename[-3:] == 'gif':
        os.rename(src, dgif)
        a+=1
        
    if filename[-3:] == 'JPG':
        os.rename(src, dJPG)
        a+=1
