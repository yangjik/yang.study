import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 동영상에서 한 프레임 이미지 가져오기
# 2. 차선 부분만 보기 위해 마스크를 생성
# 3. 차선 부분만 이미지에서 보기
# 4. 차선의 황색 실선과 흰색 점선만 추출하기

# 동영상 불러오기
video_path = './project_video.mp4'

# 컬러 동영상
# video = cv2.VideoCapture(video_path)

# 흑백 동영상
video = cv2.VideoCapture(video_path, cv2.IMREAD_GRAYSCALE)

video_w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))              # 비디오 Width
video_h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))             # 비디오 Height
video_count = video.get(cv2.CAP_PROP_FRAME_COUNT)               # 총 프레임 개수


# 프레임별 이미지 생성.
data_path = './project_video/'
os.makedirs(data_path, exist_ok=True)

# mask 
black_mask = np.zeros(shape=(video_h, video_w, 3), dtype=np.uint8)   # 0일때는 black, 255일때는 흰색

frameNum = 0
while True:   
    retval, frame = video.read() # 프레임 캡처    # retval <- 동영상이 있는가. true / false      frame <- 이미지의 rgb컬러

    if not retval:
        break

    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(25)       # 위 작업 실행하는데 시간이 걸리기 때문에(메모리 처리 시간)
    if key == 27: # Esc
        break

    if frameNum%30 == 0:  # 30프레임 마다 이미지 생성
        # 파일 명 - dataset + frameNum.jpg
        file_name = os.path.join(data_path, 'dataset'+str(frameNum)+'.jpg')
        # print(file_name) 

        cv2.imwrite(filename=file_name,  img=frame, params=[cv2.IMWRITE_JPEG_QUALITY, 90])
    frameNum += 1


if video.isOpened():
    video.release()

cv2.destroyAllWindows()