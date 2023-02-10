import cv2
import sys
import os

def detect(filename : str) -> bool:
    cascade_1 = cv2.CascadeClassifier('lbpcascade_animeface.xml')
    cascade_2 = cv2.CascadeClassifier('haarcascade_eye.xml')

    image = cv2.imread(filename, cv2.IMREAD_COLOR)

    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.equalizeHist(gray)
    # cv2.imshow("gray ver", gray)

    if list(cascade_1.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5, minSize = (24, 24))) or list(cascade_2.detectMultiScale(image,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (24, 24))):
        """
        for (x, y, w, h) in faces1:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("faceDetect", image)
        cv2.waitKey(0)
        """
        return True
    else:
        """
        print("Couldn't detect a face.")
        cv2.waitKey(0)
        """
        return False

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception("Error: missing argument. Please input either '0'-dummy set, '1'-txt2img set, or '2'-img2img set.")
    
    arg = sys.argv[1]

    if arg == '0':
        path = 'C:\\ai\\stable-diffusion-webui\\outputs\\openCV-SD-face-helper\\train-backup'
    elif arg == '1':
        path = 'C:\\ai\\stable-diffusion-webui\\outputs\\txt2img-images'
    elif arg == '2':
        path = 'C:\\ai\\stable-diffusion-webui\\outputs\\img2img-images'
    else:
        raise Exception("Error: invalid argument. Please input either '0'-dummy set, '1'-txt2img set, or '2'-img2img set.")
    
    try:
        directory = os.fsencode(path)
    except:
        raise Exception("Error: could not find image directory.")

    total = len(os.listdir(directory))
    passed = 0
    for file in os.listdir(directory):
        filepath = path + '\\' + os.fsdecode(file)
        result = detect(filepath)

        if result:
            passed += 1
        else:
            # delete the failing image
            if arg != '0':
                os.remove(filepath)
            

    # deliver a final report
    print("Done: " + str(passed) + " / " + str(total) + " images made the cut.")