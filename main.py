import getpass
import password
import sys
import os
import re

from difflib import SequenceMatcher
from itertools import dropwhile
from pathlib import Path

from password import Password

p = Password()
# Бесконечный цикл для поддержания работы программы до тех пор, пока пользователь не решит выйти из нее.
while True:
    print("1. Регистрация")  # Ushka@666
    print("2. Логин")
    print("3. Выход")
    choice = input("Введите свой выбор: ")
    if choice == '1':  # Если пользователь хочет зарегистрироваться
        file = 'user_data.json'
        if os.path.exists(file) and os.path.getsize(file) != 0:
            print("\n[-] Главный пользователь уже существует!!")
            sys.exit()
        else:
            username = input("Введите свое имя пользователя: ")
            master_password = getpass.getpass("Введите свой мастер-пароль: ")
            while True:
                if (p.validate_by_regexp(master_password) == "Пароль имеет неправильный формат."):
                    print("Пароль имеет неправильный формат.")
                    master_password = getpass.getpass("Введите свой мастер-пароль: ")
                elif (p.validate_by_common_list(master_password) == "Не используйте такой распространенный пароль."):
                    print("Не используйте такой распространенный пароль.")
                    master_password = getpass.getpass("Введите свой мастер-пароль: ")
                elif (p.validate_by_similarity(master_password,
                                               username) == "Пароль слишком похож на пароль другого пользователя."):
                    print("Пароль слишком похож на пароль другого пользователя.")
                    master_password = getpass.getpass("Введите свой мастер-пароль: ")
                else:
                    p.register(username, master_password)
                    break
    elif choice == '2':  # Если пользователь хочет войти в систему
        file = 'user_data.json'
        if os.path.exists(file):
            username = input("Введите свое имя пользователя: ")
            master_password = getpass.getpass("Введите свой мастер-пароль ")
            p.login(username, master_password)
        else:
            print("\n[-] Вы не регистрировались. Пожалуйста, сделайте это.\n")
            sys.exit()
        # Различные опции после успешного входа в систему.
        while True:
            print("1. Добавить пароль")
            print("2. Получить пароль")
            print("3. Просмотр сохраненных веб-сайтов")
            print("4. Выход")
            password_choice = input("Введите свой выбор:")
            if password_choice == '1':  # Если пользователь хочет добавить пароль
                website = input("Войти на веб-сайт: ")
                password = getpass.getpass("Введите пароль: ")
                # Зашифруйте и добавьте пароль
                p.add_password(website, password)
                print("\n[+] Добавлен пароль!\n")
            elif password_choice == '2':  # Если пользователь хочет получить пароль
                website = input("Войти на веб-сайт: ")
                decrypted_password = p.get_password(website)
                if website and decrypted_password:
                    # Скопируйте пароль в буфер обмена для удобства
                    # pyperclip.copy(расшифрованный пароль)
                    print(f"\n[+] Password for {website}: {decrypted_password}\n")
                else:
                    print("\n[-] Пароль не найден! Вы сохранили пароль? "
                          "\n[-] Используйте вариант 3, чтобы просмотреть сохраненные вами веб-сайты. \n")
            elif password_choice == '3':  # Если пользователь хочет просмотреть сохраненные веб-сайты
                p.view_websites()
            elif password_choice == '4':  # Если пользователь хочет выйти из менеджера паролей
                break
    elif choice == '3':  # Если пользователь хочет выйти из программы
        break