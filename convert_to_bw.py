from PIL import Image
from os import listdir
from os.path import isfile, join

train_cat_1 = "C:\\Users\\USER\\Pan-IIT\\data\\train\\1"
train_cat_2 = "C:\\Users\\USER\\Pan-IIT\\data\\train\\2"
train_cat_3 = "C:\\Users\\USER\\Pan-IIT\\data\\train\\3"
train_cat_4 = "C:\\Users\\USER\\Pan-IIT\\data\\train\\4"
train_cat_5 = "C:\\Users\\USER\\Pan-IIT\\data\\train\\5"
train_cat_6 = "C:\\Users\\USER\\Pan-IIT\\data\\train\\6"

val_cat_1 = "C:\\Users\\USER\\Pan-IIT\\data\\val\\1"
val_cat_2 = "C:\\Users\\USER\\Pan-IIT\\data\\val\\2"
val_cat_3 = "C:\\Users\\USER\\Pan-IIT\\data\\val\\3"
val_cat_4 = "C:\\Users\\USER\\Pan-IIT\\data\\val\\4"
val_cat_5 = "C:\\Users\\USER\\Pan-IIT\\data\\val\\5"
val_cat_6 = "C:\\Users\\USER\\Pan-IIT\\data\\val\\6"

test_cat = "C:\\Users\\USER\\Pan-IIT\\testing"

#vars = [train_cat_1,train_cat_2,train_cat_3,train_cat_4,train_cat_5,train_cat_6,val_cat_1,val_cat_2,val_cat_3,val_cat_4,val_cat_5,val_cat_6,test_cat]
vars = [test_cat]

for v in vars:
    image_files = [f for f in listdir(v) if isfile(join(v, f))]

    for i in image_files:
        image_file = Image.open(join(v,i)) # open colour image
        image_file = image_file.convert('1') # convert image to black and white
        image_file.save(join(v,i))
