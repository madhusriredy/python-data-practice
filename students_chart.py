import matplotlib.pyplot as plt

students = [
    {"name": "Asha", "score": 80},
    {"name": "Rahul", "score": 70},
    {"name": "Meena", "score": 90}
]

names = [s["name"] for s in students]
scores = [s["score"] for s in students]

average = sum(scores) / len(scores)
print("Average Score:", average)

plt.bar(names, scores)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.show()
