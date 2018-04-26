import os
from shutil import copyfile

original_root = '/home/jenno/Desktop/core50_128x128/'

train_root = '/home/jenno/Desktop/core50_static/train'
test_root = '/home/jenno/Desktop/core50_static/test'
train_session = ['s1','s2','s4','s5']
test_session = ['s3','s6']

#now begin copy training data
for s_current in train_session:
    print(s_current)
    session_folder = os.path.join(original_root,s_current)
    object_list = os.listdir(session_folder)
    for o_current in object_list:
        object_folder = os.path.join(session_folder,o_current)
        image_list = os.listdir(object_folder)
        #check if the object folder exists in training
        destination_root = os.path.join(train_root,o_current)
        if os.path.isdir(destination_root) is False:
            os.mkdir(destination_root)
        for image in image_list:
            src = os.path.join(object_folder,image)
            dst = os.path.join(destination_root,image)
            copyfile(src,dst)
            
            
#now begin copy testing data
for s_current in test_session:
    print(s_current)
    session_folder = os.path.join(original_root,s_current)
    object_list = os.listdir(session_folder)
    for o_current in object_list:
        object_folder = os.path.join(session_folder,o_current)
        image_list = os.listdir(object_folder)
        #check if the object folder exists in training
        destination_root = os.path.join(test_root,o_current)
        if os.path.isdir(destination_root) is False:
            os.mkdir(destination_root)
        for image in image_list:
            src = os.path.join(object_folder,image)
            dst = os.path.join(destination_root,image)
            copyfile(src,dst)