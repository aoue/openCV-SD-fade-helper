@echo off
cd "C:\Users\Aaja\Documents\openCV-SD-face-helper"

echo Running SD cleaning for txt2img
python openCVHelper.py 1

echo Running SD cleaning for img2img
python openCVHelper.py 2

pause