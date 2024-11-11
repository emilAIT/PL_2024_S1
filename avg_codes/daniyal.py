
from csv import reader

with open('exam_final.csv') as f:
    filename = list(reader(f))[1:]

my_name = 'Daniyal Va-akhunov'
from csv import reader
def get_average_score(filename):
    with open(filename) as fid:
        r = reader(fid)
        results = []
    for i in exam:
        midterm = int(i[1]) if i[1] and i[1].isdigit() else 0  # Устанавливаем промежуточный экзамен
        quizzes = []

        # Считываем контрольные работы, пропуская индексы 1, 4 и 9
        for j in range(len(i)):
            if j in [1, 4, 9]:  # Индексы для пропуска
                continue
            
            score = i[j]
            if score == 'absent':
                quizzes.append(0)  # При отсутствии добавляем 0
            elif score:
                try:
                    quizzes.append(float(score))  # Преобразуем в число
                except ValueError:
                    continue  # Игнорируем некорректные значения

        # Сортируем и выбираем 7 наибольших оценок
        sorted_quizzes = sorted(quizzes, reverse=True)[:7]
        sum_quizzes = sum(sorted_quizzes)
        avg_quizzes = sum_quizzes / len(sorted_quizzes) if sorted_quizzes else 0

        # Рассчитываем итоговое среднее значение
        avg_sum = (avg_quizzes * 0.7) + (midterm * 0.075)

        results.append(f'Студент: {i[9]} - Средний балл: {avg_sum:.3f}')  # Форматируем результат

    return results
from csv import reader, writer
scores = get_average_score("exam4.csv")
d = {name:score for name, score in scores}
out = []
with open('result.csv') as fid:
    r = reader(fid)
    out.append(list(next(r)) + [my_name])
    for i in r:
        res = i + [d.get(i[0],'')]
        out.append(res)
with open('result.csv', 'w', newline='') as fid:
    w = writer(fid)
    w.writerows(out)