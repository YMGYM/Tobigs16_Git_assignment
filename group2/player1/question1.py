# 간단한 파이썬 문제!
# 주어진 코드를 디버깅 해서 오류가 없게 바꿔 주세요!

def question():
    # 문제 : 리스트 안의 숫자들을 더해서 결과를 반환하겠습니다!
    target = [5, 10, -5, 6, 7, -1, 5, 1, 11, -5, 0, 1]
    sum = 0
    for i in range(len(target)):
        sum += target[i]

    assert sum == 35 # 합이 35가 맞는지 측정합니다. 이 줄은 수정하지 말아 주세요!
    
    if sum == 35:
        print('yes')
if __name__ == "__main__":
    question()

