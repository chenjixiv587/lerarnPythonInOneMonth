studentInfo = [{
    "name": "chen",
    "age": 12,
    "score": 23,
}, {
    "name": "li",
    "age": 21,
    "score": 673,
}, {
    "name": "fen",
    "age": 42,
    "score": 233,
}]

# def dependentOnWhat(aList):
#     return aList["score"]


newStudentInfo = sorted(studentInfo, key=lambda x: x["age"], reverse=True)
print(newStudentInfo)
