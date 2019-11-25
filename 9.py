def score(mark:float):
    if mark >= 0.9:
        print("A")
    elif mark >= 0.8:
        print("B")
    elif mark >= 0.7:
        print("C")
    elif mark >= 0.6:
        print("D")
    elif mark < 0.6:
        print("F")
    elif mark > 1:
        print("error")

score(0.89)