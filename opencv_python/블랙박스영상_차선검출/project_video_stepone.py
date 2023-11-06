import cv2
import sys

# 1. 동영상에서 한 프레임 이미지 가져오기
# 2. 차선 부분만 보기 위해 마스크를 생성
# 3. 차선 부분만 이미지에서 보기
# 4. 차선의 황색 실선과 흰색 점선만 추출하기

# 동영상 불러오기
video_path = './project_video.mp4'

video = cv2.VideoCapture(video_path)

if video is None:
    print("동영상 불러오지 못했습니다.")
    sys.exit()
else:
    print('불러오기 성공')


while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('video', frame)

    key = cv2.waitKey(25)   # 위 작업시간
    if key == 27:           # esc
        break

if video.isOpened():
    video.release()

cv2.destroyAllWindows()
