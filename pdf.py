import sys
import os
from wand.image import Image


def convertpdf_jpg(source, destfolder):
    for x in os.listdir(source):
        path = os.path.join(source, x)
        print(path)    
        with Image(filename=path) as img:
             img.save(filename=destfolder +"/"+ x.replace(".pdf" , ".jpg"))

if __name__ == '__main__':
    source_folder = os.getcwd() + '/' + sys.argv[1]

    if not os.path.exists(source_folder):
        raise ValueError('Pasta de entrada não existe')
 

    dest_folder = os.getcwd() + '/' + sys.argv[2]
    if not os.path.exists( dest_folder):
        print("Pasta de destino nao existe, criando a pasta "+ dest_folder)
        os.makedirs(os.getcwd() + '/' + dest_folder)
    
    convertpdf_jpg(source_folder, dest_folder)





    
