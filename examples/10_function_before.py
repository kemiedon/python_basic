students = [
    {"name": "Alice", "scores": [80, 90, 70]},
    {"name": "Bob", "scores": [60, 75, 85]},
    {"name": "Cathy", "scores": [95, 88, 92]},
]

for s in students:
    total = 0
    # 遍歷每個學生的分數後計算平均分數
    for sc in s["scores"]:
        total = total + sc
    avg = total / len(s["scores"])
    
    # 根據平均分數計算等第
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    print(s["name"] + " 的平均分數是 " + str(avg) + "，等第是 " + grade)
