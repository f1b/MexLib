from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards import ButtonColor


# Основное меню
def keyboard_menu():
    kb = Keyboard(one_time=False)
    kb.add_text_button("Список доступных документов", ButtonColor.PRIMARY)
    kb.add_row()
    kb.add_text_button("Изменить курс", ButtonColor.POSITIVE)
    kb.add_text_button("Админ-панель", ButtonColor.NEGATIVE)
    kb.add_row()
    kb.add_text_button("О боте", ButtonColor.SECONDARY)
    kb.add_text_button("Помощь", ButtonColor.SECONDARY)
    return kb.get_keyboard()


# Генератор списка документов
def keyboard_generator_old(buttons_list, buttons_per_page=4):
    result_keyboards_list = []
    kb = Keyboard(one_time=False)
    amount_of_added_buttons = 0
    count_of_pages = 1
    potential_pages = len(buttons_list) / buttons_per_page
    if ((len(buttons_list) % buttons_per_page) != 0):
        potential_pages += 1
        for i in range(len(buttons_list)):
            kb.add_text_button(buttons_list[i], ButtonColor.SECONDARY)
            kb.add_row()
            amount_of_added_buttons += 1
            middle_buttons_trigger += 1
            if ((amount_of_added_buttons == buttons_per_page) | (i == (len(buttons_list) - 1))):
                amount_of_added_buttons = 0
                if (count_of_pages == 1):
                    kb.add_text_button("Вперед", ButtonColor.POSITIVE)
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                elif ((count_of_pages > 1) & ((count_of_pages + 1) < potential_pages)):
                    kb.add_text_button("Назад", ButtonColor.POSITIVE)
                    kb.add_text_button("Вперед", ButtonColor.POSITIVE)
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
                elif ((len(buttons_list) - i) == 1):
                    kb.add_text_button("Назад", ButtonColor.POSITIVE)
                    kb.add_row()
                    kb.add_text_button("В меню", ButtonColor.PRIMARY)
                    count_of_pages += 1
                    result_keyboards_list.append(kb.get_keyboard())
                    kb = Keyboard(one_time=False)
    return result_keyboards_list


# Админ меню
def keyboard_admin():
    kb = Keyboard(one_time=False)
    kb.add_text_button("Список всех документов", ButtonColor.PRIMARY)
    kb.add_row()
    kb.add_text_button("Добавить документ", ButtonColor.POSITIVE)
    kb.add_text_button("Удалить документ", ButtonColor.NEGATIVE)
    kb.add_row()
    kb.add_text_button("Добавить модератора", ButtonColor.SECONDARY)
    kb.add_row()
    kb.add_text_button("В меню", ButtonColor.PRIMARY)
    return kb.get_keyboard()

