#5.3.4 => 5.3.3 업그레이드
#한국어 연습 프로그램

#-Learning Korean-
#1. 연습할 한국어가 담긴 리스트를 만든다
#2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
#3. 프로그램 사용자는 단어를 그대로 입력하고,
#4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료.

#전체 문제 개수 : 표시
#맞힌 문제 개수 : 표시
#틀린 문제 개수 : 표시

korean_list = ["안녕","한글","겨울","눈사람","행복"]
correct = 0
wrong = 0

print("Let's Learning Korean")
print("보여지는 한글을 따라 입력해주세요")

for list in korean_list:
    print(list)
    answer = input()
    if answer == list:
        correct += 1
    else:
        wrong += 1

    if list == korean_list[-1]:
        print("전체 문제 개수 :",len(korean_list),"개")
        print("맞힌 문제 개수 :",correct,"개")
        print("틀린 문제 개수 :",wrong,"개") #len(korean_list) - correct
        
    