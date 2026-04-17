class ParentProcessor:
    def __init__(self, num_list):
        self.num_list = num_list

    def get_positive_numbers(self):
        pass  # list comprehension 사용

    def get_even_squares(self):
        pass  # list comprehension 사용

    def summary(self):
        pass  # count & mean dict 형태 반환
    

class ChildProcessor(ParentProcessor):
    def __init__(self, num_list, num_dict):
        pass # 이 코드도 작성해야 함
    
    def get_even_keys(self):
        pass  # dict comprehension 사용 가능

    def summary(self):
        pass  # dict 기반 summary (Overriding)


# ===== 테스트 코드 =====
num_list = [1, -2, 3, 4, -5]
num_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

parent = ParentProcessor(num_list)
child = ChildProcessor(num_list, num_dict)

print("Parent Positive Numbers:", parent.get_positive_numbers())
print("Parent Even Squares:", parent.get_even_squares())
print("Parent Summary:", parent.summary())

print("Child Even Keys:", child.get_even_keys())    # 짝수인 값만 반환
print("Child Summary (Overridden):", child.summary())