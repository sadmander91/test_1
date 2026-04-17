class ParentProcessor:
    def __init__(self, num_list):
        self.num_list = num_list

    def get_positive_numbers(self):
        pass  # list comprehension 사용

    def get_even_squares(self):
        pass  # list comprehension 사용

    def summary(self):
        pass  # count & mean dict 형태 반환

# ===== 테스트 코드 =====
num_list = [1, -2, 3, 4, -5]

parent = ParentProcessor(num_list)

print("Parent Positive Numbers:", parent.get_positive_numbers())    # 양수인 숫자만 반환
print("Parent Even Squares:", parent.get_even_squares())    # 각 값을 제곱한 값중 2의 배수만 반환
print("Parent Summary:", parent.summary())    # 개수와 평균을 딕셔너리로 반환
