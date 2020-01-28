def grade(score):
    if 100 >= score >= 90:
        return "A"
    elif 89 >= score >= 80:
        return "B"
    elif 79 >= score >= 70:
        return "C"
    elif 69 >= score >= 60:
        return "D"
    elif score <= 59:
        return "F"
