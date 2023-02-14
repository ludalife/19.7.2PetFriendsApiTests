from api import PetFriends
from settings import 'luda_deo@mail.ru', 'smoke112'
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email='luda_deo@mail.ru', password='smoke112'):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key('luda_deo@mail.ru', 'smoke112')

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    print(f'\n {email}, {password}, {status}, {result}')
    

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Вася', animal_type='дворняга',
                                     age='5', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

    # Test №1
def test_get_api_key_with_correct_mail_and_wrong_passwor('luda_deo@mail.ru', 'smoke'):
    """Проверяем запрос с правильным email и неправильным паролем.
    Проверяем нет ли ключа в ответе."""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print('ok')
    print(f'Статус {status} для теста с неправильным паролем')

# Test №2
def test_get_api_key_with_wrong_email_and_correct_password('luda_deo@mail...ru', 'smoke112'):
    """Проверяем запрос с невалидным email и с валидным паролем.
    Проверяем нет ли ключа в ответе."""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print('ok')
    print(f'Статус {status} для теста с неправильным email')
    
    # Test №3
def test_get_api_key_with_wrong_email_and_wrong_password('luda_deo@mail...ru', 'smoke1121111'):
    """Проверяем запрос с невалидным email и с невалидным паролем.
    Проверяем нет ли ключа в ответе."""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print('ok')
    print(f'Статус {status} для теста с неправильным email и паролем')
    
    # Test №4
def test_add_pet_with_valid_data_without_photo(name='Кот_без_фото', animal_type='Кот', age='2'):
    """Проверяем возможность добавления нового питомца без фото"""
    _, api_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    print('ok')
    print(f'добавлен {result}')
    
    # Test №5
def test_add_pet_with_variable_age_symble(name='Karlson', animal_type='Кот', pet_photo='images/cat.jpg'):
    """Добавления питомца с латиницей вместо цифр в поле возраста."""
    age = 'сто'
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    #age = float(result['age'])#.split()
    assert status == 200
    assert age, 'Возможен ввод букв в поле возраста'
    print(f'Возможен ввод букв в поле возраста\n м {age}')
    
    # Test №6
def test_add_pet_with_valid_data_empty_field():
    """Проверяем добавление питомца со всеми пустыми полями."""
    name = ''
    animal_type = ''
    age = ''
    _, api_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    print('ok')
    print(f'Сайт позволяет добавлять питомцев без заполнения полей {result}')
    
    
    # Test №7
def test_add_pet_with_a_lot_of_words_in_variable_name(animal_type='Кот', age='2', pet_photo='images/cat.jpg'):
    """ Добавление питомца с длинным именем."""

    name = 'СамыйДлинноИменныйКот на светеЭтоМой'

    _, api_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    list_name = result['name'].split()
    word_count = len(list_name)

    assert status == 200
    assert word_count > 10, 'Питомец с именем более 30 символов'
    print('ok')
    print(f'Имя питомца в 30 символов возможно. {word_count}')
    
    # Test №8
def test_add_pet_with_special_characters_in_variable_animal_type(name='Чибба', age='1', pet_photo='images/cat2.jpg'):
    """ Добавление питомца с использованием спецсимволов в поле "Порода"."""

    animal_type = '\.!_)%@'
    symbols = 'Ёё~#$%^&*{}|?/><
    symbol = []

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, api_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)

    assert status == 200
    for i in symbols:
        if i in result['animal_type']:
            symbol.append(i)
    assert symbol[0] in result['animal_type'], 'Питомец добавлен с недопустимыми спецсимволами.'
    print(f'\n Питомец с недопустимыми специальными символами добавляется. {symbols}')
    
    # Test №10
def test_successful_delete_notvalid_key_pet():
    """Проверяем возможность удаления питомца с использованием неверного auth_key"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    print()
    print(auth_key)
    # {'key': '6ecc18c80009355ae13ba9e44ac5ea152b80178ec7b755c3f57a5c91'}#правильный ключ
    auth_key = {'key': 'ecc18c60009357ae13ba9e44ac5ea152b80178ec7b755c3f57a5c91'} #не правильный ключ
    print(auth_key)

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    num = len(my_pets['pets'])
    print('ok')


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Китька', animal_type='Кот', age=2):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key('luda_deo@mail.ru', 'smoke112')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
