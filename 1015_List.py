#List 만들기와 확인하기
a = [10, 20, 30, 40, 50]
print(a)

#빈 리스트 만들기
a = []
print(a)

#List의 주요 메소드
append() = 리스트 마지막에 element 추가
insert() = 지정한 index 위치에 element를 추가
remove() = 지정한 element 리스트에서 제거
del = 리시트에서 삭제하고 싶은 항목의 index number를 알고 있는 경우 del 사용
pop() = 리스트에서 마지막 항목을 삭제하거나, 괄호 안에 인덱스를 입력하여 특정 항목 삭제
len() = 리스트에 포함된 element의 갯수 표시

#메소드 example
방문하고 싶은 장소의 "bucketList"를 만들고 아래 문제에 답하시오.
bucketList = ['서울', '대구', '부산']

adding 제주 the end of the List = bucketList.append('제주')
printing the length of List = len(bucketList)
adding 대전 in the index 1 = bucketList.insert(1, '대전')
removing 서울 in the List = bucketList.remove('서울') or del bucketList[0]
removing the last element in the List = bucketList.pop()
clear every element in the List = bucketList.clear()

#slice
slice = 분할 영억의 시작 index, 종료 index, 간격 지정할 수 있음
example = Listname[0,6,2] = 0 (시작), 6 (끝), 2 (간격(증가, 감소))

bucketList = ['김가천', '22', '서울', '속초', '부산', '제주']
bucketList [0:6:2]
['김가천', '서울','부산']
bucketList[2:6] = print index 2 to index 5
bucketList[3:] = print indext 3 to the end
bucketList[:3] = print indext 0 to index 2

#Negative indexing
음수 인덱싱 = python sequence 자료 끝에서 시작하는 목록 element에 대한 액세스 사용
- index -1 = access of the last element in the List. my_list[-1]
- index -2 = access of the second element from the bottom of the List. my_list[-2]

#문자열 slice
a = "Life is too short, you need python"

a[0] = L, a[1] = i, a[2] = f, a[3] = e
a[0:4] =Life

a[-6:] = 뒤에서 6번쩨, 즉 p부터 끝까지 = python

#리스트 연산
연결 (Concentration): '+' 연산자를 사용하여 두 리스트를 병합
반복 (Repetition): '*' 연산자를 사용하여 지정된 횟수 만크 리스트 요소 반복

연결 및 반복 예시: 
goodplace = ['Rome', 'Seoul']
city = ['Tokyo', 'Beijing']

goodplace + city = ['Rome', 'Seoul', 'Tokyo', 'Beijing'] = 연결
city*3 = ['Tokyo', 'Beijing', 'Tokyo', 'Beijing', 'Tokyo', 'Beijing'] = 반복


