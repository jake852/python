'''
    세개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오.

    예) 합계: 평균:
'''
# 설명문 (docstring) """ """
def print_sum_avg(x, y, z):
    """
    세개의 숫자를 받아 합계와 평균을 출력하는 함수
    :param s:
    :param y:
    :param z:
    :return:
    """
    sum = x + y + z
    avg = sum / 3
    print(f"합계: {sum} 평균:{avg} ");
print_sum_avg(10, 20, 30)
print_sum_avg(30, 40, 50)