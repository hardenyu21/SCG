import collections
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        return None

    # Initialize a defaultdict to store total scores and counts for each student
    student_scores = collections.defaultdict(lambda: {'total': 0, 'count': 0})

    # Iterate over each dictionary in the list
    for student_dict in data:
        for student, score in student_dict.items():
            if score is not None:
                if score < 0:
                    raise ValueError("Negative score encountered for student: {}".format(student))
                student_scores[student]['total'] += score
                student_scores[student]['count'] += 1

    # Calculate average scores
    average_scores = {}
    for student, scores in student_scores.items():
        if scores['count'] > 0:
            average_scores[student] = scores['total'] / scores['count']

    # Prepare data for plotting
    students = list(average_scores.keys())
    averages = list(average_scores.values())

    # Plotting
    fig, ax = plt.subplots()
    ax.bar(students, averages, color=['red', 'yellow', 'green', 'blue', 'purple'][:len(students)])
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Student Scores')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return ax