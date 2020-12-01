from vkwave.bots import SimpleLongPollUserBot
from vkwave.bots import SimpleLongPollBot
from config import USER_TOKEN, BOT_TOKEN, GROUP_ID
import re
import keyboards

bot = SimpleLongPollUserBot(
    tokens=USER_TOKEN)
bot_group = SimpleLongPollBot(
    tokens=BOT_TOKEN, group_id=GROUP_ID)
doc_page = 0
menu_flag = True
docs_flag = False

# 
# Да, тут много костылей, но по итогу весь функционал будет переделываться под работу с БД
# Из-за её отсутствия, например, пришлось выносить выдачу каждого документа в отдельный хэндлер, когда по-хорошему ему бы передавать массив имен документов и уже по имени искать ID документа в базе
# Мы всего лишь хотим показать как должен работать MexLib со стороны обычного студента, который хочет иметь удобный доступ к учебникам. На данный момент студенты 1 курса ФИИТа могут пользоваться без проблем
# Остальное скажем в презентации, наверно
# 

@bot_group.message_handler(bot_group.text_filter(("список доступных документов"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    model_of_docs = (await bot.api_context.docs.get()).response
    name_of_docs = []
    list_of_docs = []

    for i in range(model_of_docs.count):
        list_of_docs.append(model_of_docs.items[i].title.title())

    list_of_docs.sort()
    global docs_flag
    global menu_flag
    
    doc_page = 0

    for i in range(model_of_docs.count):
        match = re.search(r'(.+)\.', list_of_docs[i])
        print(f"{i + 1}. {str(match[1])[0:30]}\n")
        name_of_docs.append(f"{str(match[1])[0:30]}\n")
        
    text_ans = ''
    for i in range(4):
        if ((4 * doc_page + i) < len(name_of_docs)):
            text_ans = text_ans + '├─ ' + name_of_docs[4 * doc_page + i]
    if (doc_page == 0):
        text_ans = text_ans + '\n├─ Вперед \n \n├─ В меню'
    if ((doc_page > 0) & (doc_page < (len(name_of_docs) / 4 - 1))):
        text_ans = text_ans + '\n├─ Вперед \n├─ Назад \n \n├─ В меню'
    if (doc_page >= (len(name_of_docs) / 4 - 1)):
        text_ans = text_ans + '\n├─ Назад \n \n├─ В меню'
    
        
    if menu_flag:
        await event.answer(text_ans, keyboard=keyboards.keyboard_generator_old(name_of_docs)[doc_page])
        docs_flag = True
        menu_flag = False
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot_group.text_filter(("назад"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    model_of_docs = (await bot.api_context.docs.get()).response
    name_of_docs = []
    list_of_docs = []

    for i in range(model_of_docs.count):
        list_of_docs.append(model_of_docs.items[i].title.title())

    list_of_docs.sort()
    global docs_flag
    global menu_flag

    for i in range(model_of_docs.count):
        match = re.search(r'(.+)\.', list_of_docs[i])
        name_of_docs.append(f"{str(match[1])[0:35]}\n")
        
    if docs_flag:
        global doc_page
        doc_page -= 1
        text_ans = ''
        for i in range(4):
            if ((4 * doc_page + i) < len(name_of_docs)):
                text_ans = text_ans + '├─ ' + name_of_docs[4 * doc_page + i]
        if (doc_page == 0):
            text_ans = text_ans + '\n├─ Вперед \n \n├─ В меню'
        if ((doc_page > 0) & (doc_page < (len(name_of_docs) / 4 - 1))):
            text_ans = text_ans + '\n├─ Вперед \n├─ Назад \n \n├─ В меню'
        if (doc_page >= (len(name_of_docs) / 4 - 1)):
            text_ans = text_ans + '\n├─ Назад \n \n├─ В меню'
        
        if ((doc_page >= 0) & (doc_page <= len(name_of_docs))):
            await event.answer(text_ans, keyboard=keyboards.keyboard_generator_old(name_of_docs)[doc_page])
        else:
            await event.answer('Конец списка!', keyboard=keyboards.keyboard_menu())
            await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
            doc_page = 0
            docs_flag = False
            menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot_group.text_filter(("вперед"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    model_of_docs = (await bot.api_context.docs.get()).response
    name_of_docs = []
    list_of_docs = []

    for i in range(model_of_docs.count):
        list_of_docs.append(model_of_docs.items[i].title.title())

    list_of_docs.sort()
    global docs_flag
    global menu_flag

    for i in range(model_of_docs.count):
        match = re.search(r'(.+)\.', list_of_docs[i])
        name_of_docs.append(f"{str(match[1])[0:35]}\n")
        
    if docs_flag:
        global doc_page
        doc_page += 1
        text_ans = ''
        for i in range(4):
            if ((4 * doc_page + i) < len(name_of_docs)):
                text_ans = text_ans + '├─ ' + name_of_docs[4 * doc_page + i]
        if (doc_page == 0):
            text_ans = text_ans + '\n├─ Вперед \n \n├─ В меню'
        if ((doc_page > 0) & (doc_page < (len(name_of_docs) / 4 - 1))):
            text_ans = text_ans + '\n├─ Вперед \n├─ Назад \n \n├─ В меню'
        if (doc_page >= (len(name_of_docs) / 4 - 1)):
            text_ans = text_ans + '\n├─ Назад \n \n├─ В меню'
        
        if ((doc_page >= 0) & (doc_page <= (len(name_of_docs) / 4))):
            await event.answer(text_ans, keyboard=keyboards.keyboard_generator_old(name_of_docs)[doc_page])
        else:
            await event.answer('Конец списка!', keyboard=keyboards.keyboard_menu())
            await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
            doc_page = 0
            docs_flag = False
            menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot_group.text_filter(("начать", "в меню"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global doc_page
    doc_page = 0
    await event.answer('Главное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
    global docs_flag
    global menu_flag
    docs_flag = False
    menu_flag = True

@bot_group.message_handler(bot.text_filter(("о боте"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(
            f"И снова привет! \nЯ все еще не очень умный помощник для работы с учебными книгами и документами, который делают крутые ребята с ФИИТа, а именно... \n \n Олег Авдеев (@forib) \n Альберт Нойман (@okrieso) \n Фёдор Лагутин (@federiton_san) \n Симеон Загайнов (@yaprogromist) \n Максим Стребежев (@mapsalpon) \n \n  ... в качестве проектной деятельности 2020-2021. Сейчас во мне почти нет никакого полезного функционала, но увидешь - к концу я стану гораздо лучше и буду помогать тебе в обучении!",
            keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False



@bot_group.message_handler(bot.text_filter(("помощь"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(
            f"Если у тебя возникли проблемы или какие-либо вопросы - пиши в личные сообщения @forib, и наша команда постарается помочь.",
            keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("изменить курс"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(f"Функция еще недоступна", keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("админ-панель"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer('Панель модератора:\n \n├─ Список всех документов \n├─ Добавить документ \n├─ Удалить документ \n├─ Добавить модератора \n \n├─ В меню', keyboard=keyboards.keyboard_admin())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("добавить документ"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(f"Функция еще недоступна", keyboard=keyboards.keyboard_admin())
        await event.answer('Панель модератора:\n \n├─ Список всех документов \n├─ Добавить документ \n├─ Удалить документ \n├─ Добавить модератора \n \n├─ В меню', keyboard=keyboards.keyboard_admin())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("удалить документ"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(f"Функция еще недоступна", keyboard=keyboards.keyboard_admin())
        await event.answer('Панель модератора:\n \n├─ Список всех документов \n├─ Добавить документ \n├─ Удалить документ \n├─ Добавить модератора \n \n├─ В меню', keyboard=keyboards.keyboard_admin())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("добавить модератора"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(f"Функция еще недоступна", keyboard=keyboards.keyboard_admin())
        await event.answer('Панель модератора:\n \n├─ Список всех документов \n├─ Добавить документ \n├─ Удалить документ \n├─ Добавить модератора \n \n├─ В меню', keyboard=keyboards.keyboard_admin())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("список всех документов"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if menu_flag:
        await event.answer(f"Функция еще недоступна", keyboard=keyboards.keyboard_admin())
        await event.answer('Панель модератора:\n \n├─ Список всех документов \n├─ Добавить документ \n├─ Удалить документ \n├─ Добавить модератора \n \n├─ В меню', keyboard=keyboards.keyboard_admin())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати.', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False
        

@bot_group.message_handler(bot.text_filter(("аиг бахвалов"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519046"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False


@bot_group.message_handler(bot.text_filter(("аиг ерусалимский 1сем и 2сем"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519085"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("аиг ерусалимский 2сем(fix)"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519217"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("аиг кряквин"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519234"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("аиг курош"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519270"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("аиг проскуряков"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519286"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("аиг фадеев и соминский"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519309"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("дискретка ерусалимский v1"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519568"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("дискретка ерусалимский v2"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519587"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("дискретка ерусалимский v3"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519603"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра абрамян"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519329"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра демидович v1"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519347"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра демидович v2"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519361"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра матвеев"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519381"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра пилиди интегралы-ряды"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519449"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра пилиди"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519496"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler(bot.text_filter(("непра филипов"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):

    global docs_flag
    global menu_flag
    if docs_flag:
        await event.answer("Держи!", attachment=["doc213720008_579519538"], keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь", keyboard=keyboards.keyboard_menu())
        docs_flag = False
        menu_flag = True
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню. \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь', keyboard=keyboards.keyboard_menu())
        menu_flag = True
        docs_flag = False

@bot_group.message_handler()
async def sender(event: bot.SimpleBotEvent):
    await event.answer(f"Прости, я не понял, что ты хочешь, но на всякий случай перекину тебя в меню \n \nГлавное меню:\n \n├─ Список доступных документов \n├─ Изменить курс \n├─ Админ-панель \n├─ О боте \n├─ Помощь",
                       keyboard=keyboards.keyboard_menu())
    global docs_flag
    global menu_flag
    docs_flag = False
    menu_flag = True

bot_group.run_forever()
bot.run_forever()
