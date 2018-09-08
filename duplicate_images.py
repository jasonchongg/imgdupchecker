#imports

from PIL import Image
import imagehash
import os
import sys

print("\nImage Hash Comparison Starting...\n")

#---- FOLDER 1 SETUP ---

PATH_TO_FOLDER1_IMAGES_DIR = sys.argv[1]
folder1_image_nums = []

#creates list of file names

for filename in os.listdir(PATH_TO_FOLDER1_IMAGES_DIR):
  if filename.endswith(sys.argv[3]):
     filename=filename.replace(sys.argv[3], "")
     folder1_image_nums.append(str(filename))
  else:
    continue

#creates list of image paths in folder 1
FOLDER1_IMAGE_PATHS = [ os.path.join(PATH_TO_FOLDER1_IMAGES_DIR, '{}%s'.format(entry) %(sys.argv[3]) ) for entry in folder1_image_nums]


#calculates hash of images in folder 1
hash1 = []
for image_path in FOLDER1_IMAGE_PATHS:
  hash = imagehash.average_hash(Image.open(image_path))
  hash1.append(str(hash))

#---- FOLDER 2 SETUP ---

PATH_TO_FOLDER2_IMAGES_DIR = sys.argv[2]
folder2_image_nums = []

#creates list of file names

for filename in os.listdir(PATH_TO_FOLDER2_IMAGES_DIR):
  if filename.endswith(sys.argv[4]):
     filename=filename.replace(sys.argv[4], "")
     folder2_image_nums.append(str(filename))
  else:
    continue

#creates list of image paths in folder 2
FOLDER2_IMAGE_PATHS = [ os.path.join(PATH_TO_FOLDER2_IMAGES_DIR, '{}%s'.format(entry) %(sys.argv[4])) for entry in folder2_image_nums]


#calculates hash of images in folder 2
hash2 = []
for image_path in FOLDER2_IMAGE_PATHS:
  hash = imagehash.average_hash(Image.open(image_path))
  hash2.append(str(hash))


# ---- COMPARING FOLDER 1 TO FOLDER 2 ---


for i in range(len(hash1)):
    for j in range(len(hash2)):
        if hash1[i] == hash2[j]:
            print("\nduplicate")
            print(FOLDER1_IMAGE_PATHS[i])
            print(FOLDER2_IMAGE_PATHS[j])
        else:
            continue
