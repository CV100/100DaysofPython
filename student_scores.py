#creating our own summatory and maximum number of a list function

student_scores = [124, 345, 264, 564, 545, 558]

score = 0
ultimate_score = score
for score in student_scores:
    ultimate_score += score
    last_score = score

print(ultimate_score)


the_max_score = 0
for score in student_scores:
    if score > the_max_score:
        the_max_score = score
print(the_max_score)