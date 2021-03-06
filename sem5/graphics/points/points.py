import numpy as np
import cv2

def open_image(path):
    img = cv2.imread(path, 0)
    return img

def show_image(name, img):
    cv2.imshow(name, img)

def write_image(name, img):
    cv2.imwrite(name, img)
    show_image(name, img)

def wait_exit():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------------------------------------------------------

# http://stackoverflow.com/a/26227854
def drawMatches(img1, kp1, img2, kp2, matches):
    """
    My own implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0

    This function takes in two images with their associated 
    keypoints, as well as a list of DMatch data structure (matches) 
    that contains which keypoints matched in which images.

    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.

    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.

    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """

    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left
    out[:rows1,:cols1,:] = np.dstack([img1, img1, img1])

    # Place the next image to the right of it
    out[:rows2,cols1:cols1+cols2,:] = np.dstack([img2, img2, img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour blue
        # thickness = 1
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

        # Draw a line in between the two points
        # thickness = 1
        # colour blue
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)


    # Show the image
    cv2.imshow('Matched Features', out)

# ------------------------------------------------------------------

sift = cv2.SIFT()
def points(img):
    return sift.detectAndCompute(img, None)

def draw_points(img, kps):
    cpy = img.copy()
    return cv2.drawKeypoints(cpy, kps, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

def rns_matrix(img, angle, scale):
    rows, cols = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, scale)
    return M

def rotate_n_scale(img, M):
    cpy = img.copy()
    rns = cv2.warpAffine(cpy, M, cpy.shape)
    return rns

def points_of_match(match, kp1, kp2):
    img1_idx = match.queryIdx
    img2_idx = match.trainIdx
    (x1,y1) = kp1[img1_idx].pt
    (x2,y2) = kp2[img2_idx].pt
    p1 = (int(x1), int(y1))
    p2 = (int(x2), int(y2))
    return (p1, p2)

def mult((x, y), ((a00, a01, a02), (a10, a11, a12))):
    nx = x * a00 + y * a01+ a02
    ny = x * a10 + y * a11 + a12
    return (nx, ny)

def close_enough(d, (x1, y1), (x2, y2)):
    return d > np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def perfect_matches(iM, matches, kps1, kps2):

    coords = [points_of_match(m, kps1, kps2) for m in matches]
    original = [p1 for (p1, p2) in coords]
    changed  = [p2 for (p1, p2) in coords]
    recovered = [mult(p, iM) for p in changed]

    mcount = len(original)
    count = 0

    for i in xrange(mcount):
        if close_enough(3, original[i], recovered[i]):
            count += 1

    return int((float(count) / float(mcount)) * 100)


def main():
    img = open_image("mandril.bmp")
    M = rns_matrix(img, 45, 0.5)
    kps1, des1 = points(img)
    rns = rotate_n_scale(img, M)
    kps2, des2 = points(rns)

    show_image("Original - keypoints", draw_points(img, kps1))
    show_image('Rotated and scaled - keypoints', draw_points(rns, kps2))

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)
    matches = map(lambda (m, n): m if m.distance < 0.7 * n.distance else n, matches)
    matches = sorted(matches, key=lambda val: val.distance)
    
    iM = cv2.invertAffineTransform(M)
    percetage = perfect_matches(iM, matches, kps1, kps2)

    print str(percetage) + "%"

    drawMatches(img, kps1, rns, kps2, matches)
    
    wait_exit()

# -----------------------------------------------------------------

if __name__ == '__main__':
    main()


