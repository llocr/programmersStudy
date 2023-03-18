# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000

def solution(array):
    
    array.sort()
    
    count = 1
    big = 1
    result = -1
    
    if len(array) == 1:
        result = array[0]
            
    elif len(array) > 1:
        for i in range (1, len(array), 1):
            if array[i-1] == array[i]:
                count += 1
            
                if big < count:
                    big = count
                    result = array[i]
                elif big == count:
                    result = -1
            
            elif array[i-1] != array[i]:
                count = 1

    return result