import cv2
import numpy as np

def count_blobs(img):
    img = masked_image(img)
    img = cv2.bitwise_not(img)
    img = cv2.resize(img, dsize=(0,0), fx=2, fy=2)
    # cv2.imshow("blobbed image", img)
    # cv2.waitKey(0)
    print(img.dtype)
    img = cv2.normalize(img, dst=None, alpha=0, beta=255,
                        norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()

    # Detect blobs.
    keypoints = detector.detect(img)
    # print("Found {} blobs".format(str(len(keypoints))))
    return len(keypoints)


def masked_image(img):
    # img = cv2.imread(path_to_img)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    lower, upper = np.array([220, 220, 220]), np.array([255, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # print(result.shape)
    # cv2.imshow("masked image", result)
    # cv2.waitKey(0)
    return result