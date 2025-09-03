import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    student_subjects = students.merge(subjects, how='cross')
    
    # agg beofre LEFT JOIN
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
    # LEFT JOIN
    result = student_subjects.merge(
        exam_counts,
        on=['student_id', 'subject_name'],
        how='left'
    )
    
    # attended_exams = 0 when NA
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    
    result = result.sort_values(by=['student_id', 'subject_name'])
    
    return result