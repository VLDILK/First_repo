def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
            total_salary = 0
            for line in lines:
                total_salary += int(line.split(',')[1])
            avarage_salary = total_salary/len(lines)     
            return total_salary, avarage_salary
    except FileNotFoundError:
        print(f'файл {path} відсутній')
    except SyntaxError:
        print('помилка')
     
total, average = total_salary("D:\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

