import cv2
import numpy as np
import sys
import time
img_path = './project_video/dataset0.jpg'

# 흑백 동영상
video_path = './project_video.mp4'
video = cv2.VideoCapture(video_path, cv2.IMREAD_GRAYSCALE)
video_w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))              # 비디오 Width
video_h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))             # 비디오 Height
video_count = video.get(cv2.CAP_PROP_FRAME_COUNT)               # 총 프레임 개수

# mask 
black_mask = np.zeros(shape=(video_h, video_w, 3), dtype=np.uint8)   # 0일때는 black, 255일때는 흰색

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print('이미지 불러오기 실패')
    sys.exit()
else:
    print('이미지 불러오기 성공')


# 마우스 이벤트
point = []
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 클릭 다운 좌표 : ', x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        point.append([x, y])
    elif event == cv2.EVENT_RBUTTONUP:
        # cv2.destroyWindow('canny')
        cv2.destroyAllWindows()
        print('마우스 종료')
        # return print(point)


# 원본
cv2.imshow('img', img)

# 윤곽선 도출 이미지
img_canny = cv2.Canny(img, 50, 700)
img_canny = cv2.imshow('canny', img_canny)
print('함수 사용')
cv2.setMouseCallback('canny', mouse_event)
cv2.waitKey()
cv2.destroyAllWindows()
# print(point)

# 좌표 찍은것을 이용해서 poly 적용하기
# print(point)
point_mask = np.array(point)
# print(point_mask)

mask = cv2.fillConvexPoly(black_mask, point_mask, color=(255, 255, 255))
cv2.imshow('mask', mask)
cv2.imwrite('./project_video/mask.png', mask)
cv2.waitKey()
cv2.destroyAllWindows()