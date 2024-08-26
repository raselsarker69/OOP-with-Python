student_scores={
    "Rasel":10,
    "Rayad":20,
    "Rahat":30,
    "Reyashad":40,
    "Rouf":50,
}

name=input("student name:")
student_score=int(input("student score:"))

student_scores[name]=student_score

for name,score in student_scores.items():
    print(name, ":", score)