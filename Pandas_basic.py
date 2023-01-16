# 판다스

# 판다스 데이터 구조
# - 시리즈 : Series
# - 데이터 프레임 : DataFrame
# - 패널 : Panel

import pandas as pd

# Series
sr = pd.Series(data=[1, 2, 3, 4], index=['A', 'B', 'C', 'D'])

# DataFrame
# - list 방식
value = [[10, 50], [100, 500]]
index = ['1','2']
columes = ['종류', '원']

test = pd.DataFrame(data=value, index=index, columns=columes)

# - dic 방식
value = {
    '학생' : ['가', '나', '다', '라'],
    '학년' : [1, 2, 3, 2]
}

test = pd.DataFrame(value, index=list(range(1,5)))

# - dic 방식으로 test 데이터프레임 설정
value = {
    '이름' : ['김김김', '이이이', '박박박', '문문문', '손손손', '최최최'],
    '나이' : [22, 23, 24, 25, 24, 23],
    '참석' : ['O', 'O', 'O', 'X', 'X', 'O'],
    '학년' : [1, 3, 3, 2, 1, 1]
}

test = pd.DataFrame(value)

test = test.set_index('참석')
# 인덱스 지정하기
# set_index(column, drop=True, append=False, inplace=False)
# column -> 컬럼명(복수 사용시 리스트형태로 지정)
# drop -> 기존 컬럼 버릴것인지
# append -> 기존 인덱스에 원하는 컬럼 추가할것인지
# inplace -> 원본 덮어쓰기
test = test.loc['X']

# test = test.reset_index(drop=False, inplace=True)

test = pd.DataFrame(value)
test = test.set_index(['학년', '참석'])
test = test.sort_index()
# 데이터 프레임 정렬하기 
# sort_index(ascending = True)
# true(default) -> 오름차순

# 결과
# ------------------
#         이름  나이
# 학년 참석
# 1  O   김김김  22
#    O   최최최  23
#    X   손손손  24
# 2  X   문문문  25
# 3  O   이이이  23
#    O   박박박  24
# ------------------

# 조건을 넣어서 조회
test[test['나이'] >= 24]
#         이름  나이
# 학년 참석
# 1  X   손손손  24
# 2  X   문문문  25
# 3  O   박박박  24


#  위 형태에서 index 값 추출
test = test.index.values
# [(1, 'O') (1, 'O') (1, 'X') (2, 'X') (3, 'O') (3, 'O')]
# ↑
# 특정 값 뽑아낼땐 슬라이싱 가능.
 
# print(test)
