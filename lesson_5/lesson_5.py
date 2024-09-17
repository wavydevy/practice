import random
import os
from faker import Faker
import file_operations


def main():
    fake = Faker('ru_RU')
    alphabet = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
    }
    all_skills = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
    ]
    my_cwd = os.getcwd()
    os.makedirs('result', exist_ok=True)
    file_name = 'template.svg'
    path = os.path.join(my_cwd, file_name)

    for number in range(10):
        file_name_result = 'result_{file_number}.svg'.format(file_number=str(number + 1))
        path_result = os.path.join(my_cwd, 'result', file_name_result)

        all_skills_letter = [0] * len(all_skills)
        all_skills_runic = [0] * len(all_skills)
        for i in range(len(all_skills)):
            skill_runic = []
            all_skills_letter[i] = list(all_skills[i])
            for letter in all_skills_letter[i]:
                for key_alphabet, letter_alphabet in alphabet.items():
                    if letter == key_alphabet:
                        skill_runic.append(letter_alphabet)
                        all_skills_runic[i] = ''.join(skill_runic)
        skill = random.sample(all_skills_runic, 3)

        context = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'job': fake.job(),
            'town': fake.city(),
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'endurance': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'luck': random.randint(3, 18),
            'skill_1': skill[0],
            'skill_2': skill[1],
            'skill_3': skill[2]
        }
        file_operations.render_template(path, path_result, context)


if __name__ == '__main__':
    main()
