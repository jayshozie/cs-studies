# Solution

students_data = []
total_score = 0
student_count = 0

with open('scores.txt', 'r') as scores_file:
    for line in scores_file:
        line = line.strip()
        if not line:
            continue

        name, score_str = line.split(',')

        try:
            score = float(score_str)
            students_data.append((name, score))
            total_score += score
            student_count += 1
        except ValueError:
            print(f"Warning: Could not parse score for line: '{line}'. "
                  f"Skipping.")

    average_score = total_score / student_count if student_count > 0 else 0

with open('summary_report.txt', 'w') as report_file:
    report_file.write(f"Total Students: {student_count}\n")
    report_file.write(f"Average Score: {average_score:.2f}\n")
    report_file.write("Students Above Average:\n")
    for name, score in students_data:
        if score > average_score:
            report_file.write(f"{name}\n")
