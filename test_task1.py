import pytest
from Netology_test_task1 import find_sort_unique_names, find_top3_names, find_max_and_min_durations_courses

data1 = [
    ['Иван Иванов', 'Петр Петров'],
    ['Сергей Козлов', 'Илья Глинников', 'Кирилл Топорков'],
    ['Сергей Котов', 'Иван Овечкин', 'Сергей Пускепалис'],
    ['Кирилл Сарычев', 'Иван Янковский', 'Иван Киров']
]
result1 = 'Уникальные имена преподавателей: Иван, Илья, Кирилл, Петр, Сергей'
result1_2 = 'Иван: 4 раз(а), Сергей: 3 раз(а), Кирилл: 2 раз(а)'
data2 = [
    ['Иван Иванов', 'Петр Петров', ],
    [],
    ['Олег Колотвин', 'Александр Пушкин'],
    ['Олег Ветров', 'Александр Петров'],
    ['Иван Логинов', 'Иван Коробков']
]
result2 = 'Уникальные имена преподавателей: Александр, Иван, Олег, Петр'
result2_2 = 'Иван: 3 раз(а), Александр: 2 раз(а), Олег: 2 раз(а)'

courses1 = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля"]
durations1 = [20, 20, 1]
result_test3 = ('Самый короткий курс(ы): Python-разработчик с нуля - 1 месяца(ев)',
                'Самый длинный курс(ы): Java-разработчик с нуля, Fullstack-разработчик на Python - 20 месяца(ев)')

courses2 = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
            "Frontend-разработчик с нуля"]
durations2 = [1, 2, 3, 4]
result_test3_2 = ('Самый короткий курс(ы): Java-разработчик с нуля - 1 месяца(ев)',
                  'Самый длинный курс(ы): Frontend-разработчик с нуля - 4 месяца(ев)')


# Test_func1
class Test_find_sort_unique_names:

    def test_empty_list(self):
        with pytest.raises(ValueError):
            find_sort_unique_names([])

    def test_incorrect_data(self):
        with pytest.raises(ValueError):
            find_sort_unique_names([['Иван Иванов', 'Петр Петров'], 'daffdsfd', ['Илья Серебров']])

    @pytest.mark.parametrize('lst, result', (
            [data1, result1], [data2, result2]))
    def test_not_empty_list(self, lst, result):
        assert find_sort_unique_names(lst) == result


# Test_func_2
class Test_find_top3_names:

    def test_empty_list(self):
        with pytest.raises(ValueError):
            find_top3_names([])

    def test_incorrect_data(self):
        with pytest.raises(ValueError):
            find_top3_names([['Иван Иванов', 'Петр Петров'], 'daffdsfd', ['Илья Серебров']])

    @pytest.mark.parametrize('lst, result', (
            [data1, result1_2], [data2, result2_2]))
    def test_not_empty_list(self, lst, result):
        assert find_top3_names(lst) == result


# Test_func3
class Test_find_max_and_min_durations_course:
    def test_empty_course(self):
        with pytest.raises(ValueError):
            find_max_and_min_durations_courses([], [12, 13, 6])

    def test_empty_durations(self):
        with pytest.raises(ValueError):
            find_max_and_min_durations_courses(["Java-разработчик с нуля",
                                                "Fullstack-разработчик на Python", "Python-разработчик с нуля"], [])

    def test_equal_durations(self):
        with pytest.raises(ValueError):
            find_max_and_min_durations_courses(["Java-разработчик с нуля",
                                                "Fullstack-разработчик на Python", "Python-разработчик с нуля"],
                                               [10, 10, 10])

    def test_incorrect_data(self):
        with pytest.raises(ValueError):
            find_max_and_min_durations_courses(["Java-разработчик с нуля",
                                                "Fullstack-разработчик на Python", "Python-разработчик с нуля"],
                                               [12, 13])
            find_max_and_min_durations_courses(["Java-разработчик с нуля",
                                                "Fullstack-разработчик на Python", "Python-разработчик с нуля"],
                                               [12, 13, 14, 15])

    @pytest.mark.parametrize('courses, durations, result',
                             ([courses1, durations1, result_test3],
                              [courses2, durations2, result_test3_2]
                              ))
    def test_correct_data(self, courses, durations, result):
        assert find_max_and_min_durations_courses(courses, durations) == result
