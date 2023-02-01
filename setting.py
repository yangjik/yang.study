# 아나콘다 가상환경 설정(아나콘다에서 exe파일 다운)

# 가상환경 만들기
# conda create -n 가상환경이름
# conda create -name 가상환경이름
#  'y' 입력

# 가상환경 삭제


# 가상환경
# - 활성화
# conda activate 가상환경이름
# - 비활성화
# conda deactivate

# 패키지 설치
# conda install 패키지명
# ex) conda install matplotlib


# 현재 설치된 라이브러리
# conda install requests
# conda install numpy
# conda install scipy
# conda install scikit-learn
# conda install matplotlib

# 패키지 관리
# - pip freeze 로 현재 내가 설치한 라이브러리 확인
# - txt파일로 저장은 pip freeze > requirements.txt

# txt파일 기준으로 라이브러리 설치는
# - pip install -r requirements.txt 