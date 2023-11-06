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

# mask - 검은색 배경
black_mask = np.zeros(shape=(video_h, video_w, 3), dtype=np.uint8)   # 0일때는 black, 255일때는 흰색

# 동영상 추출된 이미지 -> 윤곽선 -> 마스크작업
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
cv2.imshow('video', img)

# 윤곽선 도출 이미지
img_canny = cv2.Canny(img, 50, 700)
img_canny = cv2.imshow('canny', img_canny)
print('함수 사용')
cv2.setMouseCallback('canny', mouse_event)
cv2.waitKey()
cv2.destroyAllWindows()

# 좌표 찍은것을 이용해서 poly 적용하기
point_mask = np.array(point)
mask = cv2.fillConvexPoly(black_mask, point_mask, color=(255, 255, 255))
cv2.imshow('mask', mask)
mask_path = './project_video/mask.png'
cv2.imwrite(mask_path, mask)
cv2.waitKey()


# 이미지 부터 작업시작! - 이미지에서 mask 적용
# mask_show = cv2.bitwise_and(img, mask)


# 동영상 작업 구역 - 동영상에서 mask 적용
if video.isOpened():
    while True:
        ret, img = video.read()     
        if ret:                 
            # 원본영상
            cv2.imshow('main', img)

            # 마스크 영상
            mask_show = cv2.copyTo(img, mask=mask)
            # cv2.imshow('mask', mask_show)

            # canny 적용 동영상
            mask_canny = cv2.Canny(mask_show, 50, 700)
            cv2.imshow('canny', mask_canny)

            # hsv 적용된것 이용하는거 -> 캐니, 마스크
            video_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            mask_show = cv2.copyTo(video_hsv, mask=mask)
            # cv2.imshow('mask', mask_show)
            
            mask_canny = cv2.Canny(mask_show, 200, 760)
            cv2.imshow('canny', mask_canny)
            
            # 각각 hsv 노란색, 흰색 선 검출
            w_line = cv2.inRange(mask_show, (18, 150, 0), (24, 255, 255))
            contours, hierarchy = cv2.findContours(w_line,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            w_line = cv2.drawContours(img, contours, -1, (0, 0, 255), 5)
                                                    # image:영상, countours:위에서 찾은 외곽선 좌표, contourldx:외곽선 인덱스 -1지정시 모든외곽선
                                                    # color:색상, thichness:외곽선두께 < 0 이면 내부를 채운다. lineType:LINE_4, LINE_8, LINE_AA 중 선택
                                                    # hierarchy:외곽선 계층정보, maxLevel: 최대 외곽선 레벨. 0이면 위에 지정된 좌표값만 그린다.
            cv2.imshow('w_line',w_line)

            r_line = cv2.inRange(mask_show, (0, 0, 135), (179, 24, 255))
            contours, hierarchy = cv2.findContours(r_line,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            r_line = cv2.drawContours(img, contours, -1, (0, 255, 0), 5)
            # cv2.imshow('r_line',r_line)

            # 위에서 만든 노란색, 흰색 선 합치기.
            # w_r_line = cv2.add(w_line, r_line)
            # cv2.imshow('result', w_r_line)
            result = cv2.addWeighted(w_line, 0.3, r_line, 0.7, 0)
            # result = cv2.cvtColor(w_r_line, cv2.COLOR_HSV2BGR)
            cv2.imshow('result', result)

            key = cv2.waitKey(25)   # 위 작업시간
            if key == 27:           # esc
                break
        else:                       
            break                   
else:
    print("can't open video.")      # 캡쳐 객체 초기화 실패
video.release()              

cv2.waitKey()
cv2.destroyAllWindows()