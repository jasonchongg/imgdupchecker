# Image Duplication Detection Script

## Purpose 

Needed a simple way to detect duplicate images when training computer vision models. Created a simple python script to do the job. 

## How it works

Calculates image hashes using the python imagehash library and iteratively compares across folders.

## How to Use

The script takes in two command line arguments which are folder 1 and folder 2 paths that you want to compare. 

Example: python duplicate_images.py ~/[folder_1] ~/[folder2]

## Future Upgrades

At the time, I had images in two folders but might be useful to allow image duplication comparison in a single folder. Also if needed, I will have duplicate images be deleted by means of a deletion flag.
