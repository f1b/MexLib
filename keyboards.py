from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards import ButtonColor


# Основное меню
def keyboard_menu():
    kb = Keyboard(one_time=False)
    kb.add_text_button("Список доступных документов", ButtonColor.PRIMARY, payload={"command": "getstudentdocs"})
    kb.add_row()
    kb.add_text_button("О боте", ButtonColor.SECONDARY, payload={"command": "about"})
    kb.add_text_button("Помощь", ButtonColor.SECONDARY, payload={"command": "help"})
    kb.add_text_button("О мне", ButtonColor.SECONDARY, payload={"command": "aboutme"})
    kb.add_row()
    kb.add_text_button("Настройки", ButtonColor.POSITIVE, payload={"command": "settings"})
    return kb.get_keyboard()

# Меню настроек
def settings_menu():
    kb = Keyboard(one_time=False)
    kb.add_text_button("Изменить курс", ButtonColor.POSITIVE, payload={"command": "changeuserinfo"})
    kb.add_text_button("Админ-панель", ButtonColor.NEGATIVE, payload={"command": "adminmenu"})
    kb.add_row()
    kb.add_text_button("В меню", ButtonColor.PRIMARY)
    return kb.get_keyboard()

# Генератор списка документов
def keyboard_generator(buttons_list, buttons_per_page=4):
    result_keyboards_list = []
    kb = Keyboard(one_time=False)
    amount_of_added_buttons = 0
    count_of_pages = 1
    potential_pages = len(buttons_list) / buttons_per_page
    if ((len(buttons_list) % buttons_per_page) >= 0):
        potential_pages += 1
        for i in range(len(buttons_list)):
            kb.add_text_button(buttons_list[i], ButtonColor.SECONDARY, payload={"command": "getdoc"+f"{i % 4}"})
            kb.add_row()
            amount_of_added_buttons += 1
            if ((amount_of_added_buttons == buttons_per_page) | (i == (len(buttons_list) - 1))):
                amount_of_added_buttons = 0
                if ((count_of_pages == 1) & (len(buttons_list) > 4)):
                    kb.add_text_button("Вперед", ButtonColor.POSITIVE, payload={"command": "forwarddocs"})
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                elif ((count_of_pages > 1) & ((count_of_pages + 1) < potential_pages)):
                    kb.add_text_button("Назад", ButtonColor.POSITIVE, payload={"command": "backwarddocs"})
                    kb.add_text_button("Вперед", ButtonColor.POSITIVE, payload={"command": "forwarddocs"})
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                elif (((len(buttons_list) - i) == 1) & (len(buttons_list) > 4)):
                    kb.add_text_button("Назад", ButtonColor.POSITIVE, payload={"command": "backwarddocs"})
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                else:
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
    return result_keyboards_list


# Админ меню
def keyboard_admin():
    kb = Keyboard(one_time=False)
    kb.add_text_button("Список всех документов", ButtonColor.PRIMARY, payload={"command": "getadminsdocs"})
    kb.add_row()
    kb.add_text_button("Добавить документ", ButtonColor.POSITIVE, payload={"command": "adddoc"})
    kb.add_text_button("Удалить документ", ButtonColor.NEGATIVE, payload={"command": "deletedoc"})
    kb.add_row()
    kb.add_text_button("Добавить теги", ButtonColor.SECONDARY, payload={"command": "addtags"})
    kb.add_text_button("Удалить теги", ButtonColor.SECONDARY, payload={"command": "deletetags"})
    kb.add_row()
    kb.add_text_button("Добавить администратора", ButtonColor.POSITIVE, payload={"command": "makeadmin"})
    kb.add_row()
    kb.add_text_button("В меню", ButtonColor.PRIMARY)
    return kb.get_keyboard()

# Генератор списка документов для админов
def keyboard_generator_admin(buttons_list, buttons_per_page=4):
    result_keyboards_list = []
    kb = Keyboard(one_time=False)
    amount_of_added_buttons = 0
    count_of_pages = 1
    potential_pages = len(buttons_list) / buttons_per_page
    if ((len(buttons_list) % buttons_per_page) >= 0):
        potential_pages += 1
        for i in range(len(buttons_list)):
            kb.add_text_button(buttons_list[i], ButtonColor.SECONDARY, payload={"command": "getdocadmin"+f"{i % 4}"})
            kb.add_row()
            amount_of_added_buttons += 1
            if ((amount_of_added_buttons == buttons_per_page) | (i == (len(buttons_list) - 1))):
                amount_of_added_buttons = 0
                if ((count_of_pages == 1) & (len(buttons_list) > 4)):
                    kb.add_text_button("Вперед", ButtonColor.POSITIVE, payload={"command": "forwarddocsadmin"})
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                elif ((count_of_pages > 1) & ((count_of_pages + 1) < potential_pages)):
                    kb.add_text_button("Назад", ButtonColor.POSITIVE, payload={"command": "backwarddocsadmin"})
                    kb.add_text_button("Вперед", ButtonColor.POSITIVE, payload={"command": "forwarddocsadmin"})
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                elif (((len(buttons_list) - i) == 1) & (len(buttons_list) > 4)):
                    kb.add_text_button("Назад", ButtonColor.POSITIVE, payload={"command": "backwarddocsadmin"})
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                else:
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
    return result_keyboards_list

