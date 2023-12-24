# Task_1

# Function №1
# На лекции мы работали с преподавателями. Давайте усложним задачу и поработаем только с их именами, без фамилий.
# У нас есть 4 курса Нетологии, на которых преподают 4 группы преподавателей.
# Ваша задача — отделить имена от фамилий и собрать все имена преподавателей со всех четырёх курсов.
# Имена ни в коем случае не должны повторяться. А чтобы всё было красиво, отсортируйте их в алфавитном порядке.

def find_sort_unique_names(lst: list) -> str:
    result = []
    if not lst:
        raise ValueError('Список не должен быть пустым')
    for cours_mentors_list in lst:
        if not isinstance(cours_mentors_list, list):
            raise ValueError('Внутри входного списка должны быть списки')
        if cours_mentors_list:
            result.extend([x.split()[0] for x in cours_mentors_list])
    result = sorted(set(result))
    return f"Уникальные имена преподавателей: {', '.join(result)}"


# Function №2
# У нас есть 4 курса Нетологии, на них обучают 4 группы преподавателей.
# Вам необходимо определить топ-3 популярных имён среди преподавателей.
def find_top3_names(lst: list) -> str:
    all_names_list = []
    if not lst:
        raise ValueError('Список не должен быть пустым')
    for cours_mentors_list in lst:
        if not isinstance(cours_mentors_list, list):
            raise ValueError('Внутри входного списка должны быть списки')
        if cours_mentors_list:
            all_names_list.extend([x.split()[0] for x in cours_mentors_list])
    unique_names = set(all_names_list)
    result = [[name, all_names_list.count(name)] for name in unique_names]
    result.sort(key=lambda x: (-x[1], x[0]))  # При равенстве популярности сортируем по алфавиту
    return (f'{result[0][0]}: {result[0][1]} раз(а), {result[1][0]}: {result[1][1]} раз(а), '
            f'{result[2][0]}: {result[2][1]} раз(а)')


# Function 3
# Напишите код, который создаст список курсов courses_list, где каждый курс —
# словарь с названием курса, длительностью и преподавателями.
# После этого выведите названия самого короткого и самого длинного курсов.

def find_max_and_min_durations_courses(courses: list, durations: list) -> tuple:
    if not courses or not durations:
        raise ValueError('Входные параметры не должны быть пустыми')
    if len(courses) != len(durations):
        raise ValueError('Длина входных списков должна быть равна')
    courses_list = [{'title': cours, 'duration': duration} for cours, duration in zip(courses, durations)]
    max_ = max(durations)
    min_ = min(durations)
    if max_ == min_:
        raise ValueError('Продолжительность всех курсов равна')
    maxes_course = [x['title'] for x in courses_list if x['duration'] == max_]
    minis_course = [x['title'] for x in courses_list if x['duration'] == min_]
    result1 = f'Самый короткий курс(ы): {", ".join(minis_course)} - {min_} месяца(ев)'
    result2 = f'Самый длинный курс(ы): {", ".join(maxes_course)} - {max_} месяца(ев)'
    return result1, result2