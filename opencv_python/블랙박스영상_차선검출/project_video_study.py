import cv2
import numpy as np

videoFile = 'project_video.mp4'
# 비디오 영상 가져오기
cap = cv2.VideoCapture(videoFile)

# 비디오 영상 크기 확인하기
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_size =', frame_size)
print('frame count=', frame_count)

def on_mouse(event, x, y, flags, param):
    print("x={}, y={}".format(x,y))


def region_of_interest(img, vertices):
    # Define a blank matrix that matches the image height/width.
    mask = np.zeros_like(img)
    # Retrieve the number of color channels of the image.
    channel_count = img.shape[2]
    # Create a match color with the same color channel counts.
    match_mask_color = (255,) * channel_count
      
    # Fill inside the polygon
    cv2.fillPoly(mask, vertices, match_mask_color)
    
    # Returning the image only where mask pixels match
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

# 207,675, 521,476 803,476, 1120, 675

ROI_vertices = [
    (207, 675),
    (521,476),
    (803,476),
    (1120,675)
]

# main
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', on_mouse)
# 마스크를 생성하고,
# while문으로 반복하면서 영상 한 프레임씩 가져오기
# 마스크를 적용해서 마스크 부분만 영상 가져오기(copyTo)
# 영상 출력(imshow)
while True:   
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break
    masked_img = region_of_interest(frame, np.array([ROI_vertices], np.int32))
    img_HSV = cv2.cvtColor(masked_img, cv2.COLOR_BGR2HSV)
    cLine_img = cv2.inRange(img_HSV, (18, 150, 0), (24, 255, 255))
    rLine_img = cv2.inRange(img_HSV, (0, 0, 135), (179, 24, 255))
    cv2.imshow('frame',frame)
    cv2.imshow('result',masked_img)
    cv2.imshow('cLine',cLine_img)
    cv2.imshow('rLine',rLine_img)

    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
