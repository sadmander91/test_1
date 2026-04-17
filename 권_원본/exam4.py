# ===== 테스트용 데이터 =====
students_data = [
    {
        "student_id": 123456,
        "name": "John Doe",
        "courses": {
            "Math": {"grade": 3.8, "credits": 3},
            "Science": {"grade": 3.5, "credits": 4},
            "English": {"grade": 3.0, "credits": 3},
            "History": {"grade": 3.3, "credits": 3}
        }
    },
    {
        "student_id": 234567,
        "name": "Jane Smith",
        "courses": {
            "Math": {"grade": 4.0, "credits": 3},
            "Science": {"grade": 3.7, "credits": 4},
            "English": {"grade": 3.2, "credits": 3},
            "Art": {"grade": 3.9, "credits": 2}
        }
    },
    {
        "student_id": 345678,
        "name": "Emily Davis",
        "courses": {
            "Math": {"grade": 3.1, "credits": 3},
            "Science": {"grade": 2.9, "credits": 4},
            "English": {"grade": 3.4, "credits": 3},
            "History": {"grade": 3.6, "credits": 3},
            "Music": {"grade": 4.0, "credits": 2}
        }
    }
]

def calculate_gpa(student_data):
    # student_data 딕셔너리에서 grade, credits 정보를 사용하여
    # GPA 계산 후 반환 (총점: grade * credits의 합, GPA: 총점 / 총학점)
    pass  # 여기에 코드 작성


# ===== GPA 출력 테스트 =====
for student in students_data:
    gpa = calculate_gpa(student)
    print(f"Student: {student['name']}, GPA: {gpa}")