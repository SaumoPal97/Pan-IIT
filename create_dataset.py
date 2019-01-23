from __future__ import print_function
import pandas as pd
import shutil
import os


df = pd.read_csv('C:\\Users\\USER\\Pan-IIT\\training.5k\\training\\solution.csv')
print(df.groupby('category').count())

train_num = 4500
val_num = 500

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

for i in range(train_num):
    shutil.copy2("C:\\Users\\USER\\Pan-IIT\\training.5k\\training\\training\\"+str(df['id'][i])+".png","C:\\Users\\USER\\Pan-IIT\\data\\train\\"+str(df['category'][i]))

for i in range(train_num,train_num+val_num):
    shutil.copy2("C:\\Users\\USER\\Pan-IIT\\training.5k\\training\\training\\"+str(df['id'][i])+".png","C:\\Users\\USER\\Pan-IIT\\data\\val\\"+str(df['category'][i]))
