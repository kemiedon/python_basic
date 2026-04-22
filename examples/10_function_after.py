# 學生資料列表，包含姓名和分數
students = [
    {"name": "Alice", "scores": [80, 90, 70]},
    {"name": "Bob", "scores": [60, 75, 85]},
    {"name": "Cathy", "scores": [95, 88, 92]},
]
def calculate_average(scores):
    """計算分數的平均值"""
    total = 0
    for score in scores:
        total += score
    return total / len(scores)
def get_grade(avg):
    """根據平均分數判斷等第"""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
def print_student_result(student):
    """印出學生的平均分數和等第"""
    avg = calculate_average(student["scores"])
    grade = get_grade(avg)
    print(f'{student["name"]} 的平均分數是 {avg}，等第是 {grade}')


def main():
    """主程式：遍歷所有學生並印出結果"""
    for student in students:
        print_student_result(student)


# 執行主程式
main()
