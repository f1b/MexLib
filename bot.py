from vkwave.bots import SimpleLongPollUserBot
from vkwave.bots import SimpleLongPollBot
from config import USER_TOKEN, BOT_TOKEN, GROUP_ID
from vkwave.bots import Keyboard, ButtonColor
import classes
import re
import keyboards

bot = SimpleLongPollUserBot(
    tokens=USER_TOKEN)
bot_group = SimpleLongPollBot(
    tokens=BOT_TOKEN, group_id=GROUP_ID)

clients = classes.Clients()
docswork = classes.DocsWork()


def TupleToList(tuple):
    zlist = []
    tupls = tuple
    for tup in tupls:
        t = str(tup).replace("('", "").replace("',)", "")
        zlist.append(t)
    return zlist


def GetDocsLinksByUserAllow(user_id):
    user_info = clients.FindByid(user_id)
    user_group = user_info[0][0]
    user_course = user_info[0][1]
    if user_course == 1:
        get_docs_course = 'is_1course'
    elif user_course == 2:
        get_docs_course = 'is_2course'
    elif user_course == 3:
        get_docs_course = 'is_3course'
    elif user_course == 4:
        get_docs_course = 'is_4course'

    if user_group == 7:
        get_docs_group = 'is_7group'
    elif user_group == 8:
        get_docs_group = 'is_8group'
    elif user_group == 9:
        get_docs_group = 'is_9group'
    elif user_group == 10:
        get_docs_group = 'is_10group'
    elif user_group == 11:
        get_docs_group = 'is_11group'

    docs_list = docswork.FindDocsByCourseAndGroup(get_docs_course, get_docs_group)
    if len(docs_list) > 0:
        return docs_list
    else:
        return False


def GetDocsLinksByAdminAllow():
    docs_list = docswork.FindDocsForAdmin()
    if len(docs_list) > 0:
        return docs_list
    else:
        return False


def GetDocsNamesByIDs(list_of_ids):
    res = []
    real_list_of_ids = TupleToList(list_of_ids)
    for x in real_list_of_ids:
        t = docswork.GetDocName(str(x))
        res.append(t)
    return (res)


def isDocInBase(doc_id, doc_name):
    try:
        if (docswork.IsInBase(doc_id)):
            print(doc_id)
            print(docswork.IsInBase(doc_id))
            return True
        elif (docswork.IsInBase(docswork.FindIDByName(doc_name)[0])):
            print(doc_name)
            print(docswork.FindIDByName(doc_name)[0])
            return True
        else:
            print(doc_id)
            print(doc_name)
            print(docswork.IsInBase(doc_id))
            print(docswork.FindIDByName(doc_name)[0])
            return False
    except Exception as ex:
        return False


@bot_group.message_handler(bot_group.text_filter(("testdocs"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    await event.answer(docswork.FindIDByName("АиГ Кряквин"))


@bot_group.message_handler(bot_group.text_filter(("начать", "в меню"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    if (clients.IsInBase(msg_user_id)):
        await event.answer(
            'Главное меню',
            keyboard=keyboards.keyboard_menu())
    else:
        await event.answer(clients.AddNewUser(msg_user_id))
        anskb = Keyboard()
        anskb.add_text_button(
            text="1 курс", color=ButtonColor.PRIMARY, payload={"command": "getcourse1"}
        )
        anskb.add_text_button(
            text="2 курс", color=ButtonColor.PRIMARY, payload={"command": "getcourse2"}
        )
        anskb.add_row()
        anskb.add_text_button(
            text="3 курс", color=ButtonColor.PRIMARY, payload={"command": "getcourse3"}
        )
        anskb.add_text_button(
            text="4 курс", color=ButtonColor.PRIMARY, payload={"command": "getcourse4"}
        )

        await event.answer(
            'Ты - новый пользователь, так что выбери номер своего курса',
            keyboard=anskb.get_keyboard())


@bot_group.message_handler(bot_group.payload_filter({"command": "getcourse1"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateCourse(msg_user_id, '1')
    anskb = Keyboard()
    anskb.add_text_button(
        text="7 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup7"}
    )
    anskb.add_text_button(
        text="8 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup8"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="9 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup9"}
    )
    anskb.add_text_button(
        text="10 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup10"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="11 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup11"}
    )
    await event.answer(
        'А теперь выбери свою группу',
        keyboard=anskb.get_keyboard())


@bot_group.message_handler(bot_group.payload_filter({"command": "getcourse2"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateCourse(msg_user_id, '2')
    anskb = Keyboard()
    anskb.add_text_button(
        text="7 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup7"}
    )
    anskb.add_text_button(
        text="8 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup8"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="9 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup9"}
    )
    anskb.add_text_button(
        text="10 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup10"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="11 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup11"}
    )
    await event.answer(
        'А теперь выбери свою группу',
        keyboard=anskb.get_keyboard())


@bot_group.message_handler(bot_group.payload_filter({"command": "getcourse3"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateCourse(msg_user_id, '3')
    anskb = Keyboard()
    anskb.add_text_button(
        text="7 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup7"}
    )
    anskb.add_text_button(
        text="8 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup8"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="9 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup9"}
    )
    anskb.add_text_button(
        text="10 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup10"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="11 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup11"}
    )
    await event.answer(
        'А теперь выбери свою группу',
        keyboard=anskb.get_keyboard())


@bot_group.message_handler(bot_group.payload_filter({"command": "getcourse4"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateCourse(msg_user_id, '4')
    anskb = Keyboard()
    anskb.add_text_button(
        text="7 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup7"}
    )
    anskb.add_text_button(
        text="8 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup8"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="9 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup9"}
    )
    anskb.add_text_button(
        text="10 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup10"}
    )
    anskb.add_row()
    anskb.add_text_button(
        text="11 группа", color=ButtonColor.PRIMARY, payload={"command": "getgroup11"}
    )
    await event.answer(
        'А теперь выбери свою группу',
        keyboard=anskb.get_keyboard())


@bot_group.message_handler(bot_group.payload_filter({"command": "getgroup7"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateGroup(msg_user_id, '7')
    await event.answer(
        'Спасибо, теперь ты можешь пользоваться ботом! \n \n Главное меню',
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getgroup8"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateGroup(msg_user_id, '8')
    await event.answer(
        'Спасибо, теперь ты можешь пользоваться ботом! \n \n Главное меню',
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getgroup9"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateGroup(msg_user_id, '9')
    await event.answer(
        'Спасибо, теперь ты можешь пользоваться ботом! \n \n Главное меню',
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getgroup10"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateGroup(msg_user_id, '10')
    await event.answer(
        'Спасибо, теперь ты можешь пользоваться ботом! \n \n Главное меню',
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getgroup11"}))
async def send_schedule(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    clients.UpdateGroup(msg_user_id, '11')
    await event.answer(
        'Спасибо, теперь ты можешь пользоваться ботом! \n \n Главное меню',
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "changeuserinfo"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    clients.DeleteFromTable(msg_user_id)
    anskb = Keyboard()
    anskb.add_text_button(
        text="Начать", color=ButtonColor.PRIMARY
    )
    await event.answer(
        'Хорошо, я удалил всю информацию о тебе. Нажми "Начать", чтобы снова указать курс и группу',
        keyboard=anskb.get_keyboard())


@bot_group.message_handler(bot_group.payload_filter({"command": "about"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    if clients.GetMenuFlag(msg_user_id):
        await event.answer(
            f"И снова привет! \n \nЯ умный(на уровне бордер-колли) помощник для работы с учебными книгами и документами, который сделали крутые ребята с ФИИТа, а именно... \n \n Олег Авдеев (@forib) \n Альберт Нойман (@okrieso) \n Фёдор Лагутин (@federiton_san) \n Симеон Загайнов (@yaprogromist) \n Максим Стребежев (@mapsalpon) \n \n  ... в качестве проектной деятельности 2020-2021.",
            keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "adminmenu"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    if clients.GetMenuFlag(msg_user_id):
        if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
            await event.answer('Добро пожаловать в меню администратора! \n \n Админ-меню',
                               keyboard=keyboards.keyboard_admin())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
        else:
            await event.answer('Ты не администратор! Возвращайся в меню')
            await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("getcode"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        clients.UpdateRole(msg_user_id, "student")
        await event.answer('Теперь ты студент!', keyboard=keyboards.keyboard_menu())
    else:
        clients.UpdateRole(msg_user_id, "admin")
        await event.answer('Теперь ты администратор!', keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "adddoc"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    if clients.GetMenuFlag(msg_user_id):
        if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
            await event.answer(
                'Хорошо! Пришли мне документ со словом "Добавить" \n \n Обязательные требования к документу: \n \n 1) Формат - только PDF или DOCX. Если старовер, то можешь загрузить DOC \n \n 1) Зайди в раздел "Файлы", найди там тот документ, который хочешь добавить, и поменяй его метку на "Учебный файл"(маленький карандаш справа от названия) \n \n 3) Само название должно быть не больше 30 символов в длину(будет больше - автоматически обрежется) и содержать в себе максимально краткое и понятное описание документа. ')
            clients.UpdateDocsFlag(msg_user_id, 1)
            clients.UpdateMenuFlag(msg_user_id, 0)
        else:
            await event.answer('Ты не администратор! Возвращайся в меню')
            await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("добавить"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (isDocInBase(doc_link, doc_title)):
                    await event.answer('Такой документ уже есть в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.AddNewDoc(doc_link):
                            docswork.UpdateDocName(doc_link, doc_title)
                            await event.answer(
                                "Добавил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "Просил же - PDF или DOCX. На крайний случай можно и DOC, старовер \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "deletedoc"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    if clients.GetMenuFlag(msg_user_id):
        if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
            await event.answer('Хорошо! Пришли мне документ, который хочешь удалить из библиотеки, со словом "Удалить"')
            clients.UpdateDocsFlag(msg_user_id, 1)
            clients.UpdateMenuFlag(msg_user_id, 0)
        else:
            await event.answer('Ты не администратор! Возвращайся в меню')
            await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("удалить"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.DeleteFromTable(docswork.FindIDByName(doc_title)[0]):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "addtags"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    if clients.GetMenuFlag(msg_user_id):
        if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
            await event.answer(
                'Хорошо! Пришли мне документ и сообщение "метка добавить" и саму метку (пример: метка добавить курс 2), которую хочешь поставить. Можно поставить одну метку за раз. \n \n Доступные метки: \n Курс 1 \n Курс 2 \n Курс 3 \n Курс 4 \n Группа 7 \n Группа 8 \n Группа 9 \n Группа 10 \n Группа 11 \n Для всех')
            clients.UpdateDocsFlag(msg_user_id, 1)
            clients.UpdateMenuFlag(msg_user_id, 0)
        else:
            await event.answer('Ты не администратор! Возвращайся в меню')
            await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить курс 1"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc1Course(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить курс 2"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc2Course(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить курс 3"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc3Course(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить курс 4"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc4Course(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить группа 7"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc7Group(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить группа 8"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc8Group(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить группа 9"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc9Group(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить группа 10"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc10Group(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить группа 11"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc11Group(docswork.FindIDByName(doc_title)[0], 1):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка добавить для всех"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if (docswork.SetDoc1Course(doc_link, 1) & docswork.SetDoc2Course(doc_link,
                                                                                         1) & docswork.SetDoc3Course(
                            doc_link, 1) & docswork.SetDoc4Course(doc_link, 1) & docswork.SetDoc7Group(doc_link,
                                                                                                       1) & docswork.SetDoc8Group(
                            doc_link, 1) & docswork.SetDoc9Group(doc_link, 1) & docswork.SetDoc10Group(doc_link,
                                                                                                       1) & docswork.SetDoc11Group(
                            doc_link, 1)):
                            await event.answer(
                                "Поставил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            print(ex)
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "deletetags"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    if clients.GetMenuFlag(msg_user_id):
        if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
            await event.answer(
                'Хорошо! Пришли мне документ и сообщение "метка удалить" и саму метку (пример: метка удалить курс 2), которую хочешь убрать. Можно убрать одну метку за раз. \n \n Доступные метки: \n Курс 1 \n Курс 2 \n Курс 3 \n Курс 4 \n Группа 7 \n Группа 8 \n Группа 9 \n Группа 10 \n Группа 11')
            clients.UpdateDocsFlag(msg_user_id, 1)
            clients.UpdateMenuFlag(msg_user_id, 0)
        else:
            await event.answer('Ты не администратор! Возвращайся в меню')
            await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить курс 1"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc1Course(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить курс 2"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc2Course(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить курс 3"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc3Course(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить курс 4"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc4Course(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить группа 7"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc7Group(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить группа 8"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc8Group(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить группа 9"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc9Group(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить группа 10"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc10Group(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot.text_filter(("метка удалить группа 11"), ignore_case=True))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    docflag = clients.GetDocsFlag(msg_user_id)
    if (clients.GetUserRole(msg_user_id)[0] == 'admin'):
        try:
            if (docflag):
                doc_owner_id = str(event.object.object.message.attachments[0].doc.owner_id)
                doc_id = str(event.object.object.message.attachments[0].doc.id)
                match = re.search(r'(.+?)\.', event.object.object.message.attachments[0].doc.title)
                temp_doc_title = match[1]
                if (len(temp_doc_title) < 30):
                    doc_title = f"{str(temp_doc_title)}"
                else:
                    doc_title = f"{str(temp_doc_title)[0:30]}" + "..."
                doc_link = "doc" + doc_owner_id + "_" + doc_id
                doc_type = str(event.object.object.message.attachments[0].doc.ext)
                if (not isDocInBase(doc_link, doc_title)):
                    await event.answer('Такого документа нет в библиотеке. Возвращаю в меню \n \n Главное меню',
                                       keyboard=keyboards.keyboard_menu())
                else:
                    if ((doc_type == "pdf" or doc_type == "doc" or doc_type == "docx") and docflag):
                        if docswork.SetDoc11Group(doc_link, 0):
                            await event.answer(
                                "Удалил! Возвращаю в меню \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                        else:
                            await event.answer(
                                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                                keyboard=keyboards.keyboard_menu())
                            clients.UpdateDocsFlag(msg_user_id, 0)
                            clients.UpdateMenuFlag(msg_user_id, 1)
                    else:
                        await event.answer(
                            "При удалении правила те же - только PDF, DOCX или DOC \n \n Главное меню",
                            keyboard=keyboards.keyboard_menu())
                        clients.UpdateDocsFlag(msg_user_id, 0)
                        clients.UpdateMenuFlag(msg_user_id, 1)
            else:
                await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
                await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
                clients.UpdateDocsFlag(msg_user_id, 0)
                clients.UpdateMenuFlag(msg_user_id, 1)
        except Exception as ex:
            await event.answer(
                "Произошла ошибка. Если ты уверен, что не виноват в ней, то напиши людям, упомянутым в разделе 'Помощь' \n \n Главное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не администратор! Возвращайся в меню')
        await event.answer("\n \nГлавное меню", keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "getadminsdocs"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    name_of_docs = TupleToList(GetDocsNamesByIDs(GetDocsLinksByAdminAllow()))

    clients.UpdateDocPage(msg_user_id, str(0))

    if clients.GetMenuFlag(msg_user_id):
        await event.answer('Список', keyboard=keyboards.keyboard_generator_admin(name_of_docs)[
            int(TupleToList(clients.GetDocPage(msg_user_id))[0])])
        clients.UpdateDocsFlag(msg_user_id, 1)
        clients.UpdateMenuFlag(msg_user_id, 0)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_admin())
        await event.answer(
            "\n \nАдмин-меню",
            keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "backwarddocsadmin"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    name_of_docs = TupleToList(GetDocsNamesByIDs(GetDocsLinksByAdminAllow()))

    if clients.GetDocsFlag(msg_user_id):
        old_doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
        clients.UpdateDocPage(msg_user_id, str(old_doc_page - 1))
        doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])

        if ((doc_page >= 0) & (doc_page <= len(name_of_docs))):
            await event.answer("Список", keyboard=keyboards.keyboard_generator_admin(name_of_docs)[doc_page])
        else:
            await event.answer('Конец списка!', keyboard=keyboards.keyboard_admin())
            await event.answer(
                "\n \nАдмин-меню",
                keyboard=keyboards.keyboard_admin())
            clients.UpdateDocPage(msg_user_id, 0)
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню', keyboard=keyboards.keyboard_admin())
        await event.answer(
            "\n \nАдмин-меню",
            keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "forwarddocsadmin"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    name_of_docs = TupleToList(GetDocsNamesByIDs(GetDocsLinksByAdminAllow()))

    if clients.GetDocsFlag(msg_user_id):
        old_doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
        clients.UpdateDocPage(msg_user_id, str(old_doc_page + 1))
        doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])

        if ((doc_page >= 0) & (doc_page <= (len(name_of_docs) / 4))):
            await event.answer("Список", keyboard=keyboards.keyboard_generator_admin(name_of_docs)[doc_page])
        else:
            await event.answer('Конец списка!', keyboard=keyboards.keyboard_admin())
            await event.answer(
                "\n \nАдмин-меню:",
                keyboard=keyboards.keyboard_admin())
            clients.UpdateDocPage(msg_user_id, 0)
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню', keyboard=keyboards.keyboard_admin())
        await event.answer(
            "\n \nАдмин-меню",
            keyboard=keyboards.keyboard_admin())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "getstudentdocs"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    name_of_docs = TupleToList(GetDocsNamesByIDs(GetDocsLinksByUserAllow(msg_user_id)))

    clients.UpdateDocPage(msg_user_id, str(0))

    if clients.GetMenuFlag(msg_user_id):
        await event.answer('Список', keyboard=keyboards.keyboard_generator(name_of_docs)[
            int(TupleToList(clients.GetDocPage(msg_user_id))[0])])
        clients.UpdateDocsFlag(msg_user_id, 1)
        clients.UpdateMenuFlag(msg_user_id, 0)
    else:
        await event.answer('Ты же не в меню! Вот оно, кстати', keyboard=keyboards.keyboard_menu())
        await event.answer(
            "\n \nГлавное меню",
            keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "backwarddocs"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    name_of_docs = TupleToList(GetDocsNamesByIDs(GetDocsLinksByUserAllow(msg_user_id)))

    if clients.GetDocsFlag(msg_user_id):
        old_doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
        clients.UpdateDocPage(msg_user_id, str(old_doc_page - 1))
        doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])

        if ((doc_page >= 0) & (doc_page <= len(name_of_docs))):
            await event.answer("Список", keyboard=keyboards.keyboard_generator(name_of_docs)[doc_page])
        else:
            await event.answer('Конец списка!', keyboard=keyboards.keyboard_menu())
            await event.answer(
                "\n \nГлавное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocPage(msg_user_id, 0)
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню', keyboard=keyboards.keyboard_menu())
        await event.answer(
            "\n \nГлавное меню",
            keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "forwarddocs"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    name_of_docs = TupleToList(GetDocsNamesByIDs(GetDocsLinksByUserAllow(msg_user_id)))

    if clients.GetDocsFlag(msg_user_id):
        old_doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
        clients.UpdateDocPage(msg_user_id, str(old_doc_page + 1))
        doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])

        if ((doc_page >= 0) & (doc_page <= (len(name_of_docs) / 4))):
            await event.answer("Список", keyboard=keyboards.keyboard_generator(name_of_docs)[doc_page])
        else:
            await event.answer('Конец списка!', keyboard=keyboards.keyboard_menu())
            await event.answer(
                "\n \nГлавное меню",
                keyboard=keyboards.keyboard_menu())
            clients.UpdateDocPage(msg_user_id, 0)
            clients.UpdateDocsFlag(msg_user_id, 0)
            clients.UpdateMenuFlag(msg_user_id, 1)
    else:
        await event.answer('Ты не в списке документов! Возвращаю в меню', keyboard=keyboards.keyboard_menu())
        await event.answer(
            "\n \nГлавное меню",
            keyboard=keyboards.keyboard_menu())
        clients.UpdateDocsFlag(msg_user_id, 0)
        clients.UpdateMenuFlag(msg_user_id, 1)


@bot_group.message_handler(bot_group.payload_filter({"command": "getdoc0"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByUserAllow(msg_user_id))
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 0
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdoc1"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByUserAllow(msg_user_id))
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 1
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdoc2"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByUserAllow(msg_user_id))
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 2
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdoc3"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByUserAllow(msg_user_id))
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 3
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdocadmin0"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByAdminAllow())
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 0
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdocadmin1"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByAdminAllow())
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 1
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdocadmin2"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByAdminAllow())
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 2
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "getdocadmin3"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    list_of_docs_ids = TupleToList(GetDocsLinksByAdminAllow())
    doc_page = int(TupleToList(clients.GetDocPage(msg_user_id))[0])
    current_pos_in_docs = 4 * doc_page + 3
    await event.answer("Держи! \n \nГлавное меню", attachment=[list_of_docs_ids[current_pos_in_docs]],
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "help"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id
    await event.answer(
        "FAQ:\n1) На запрос документа бот присылает пустое сообщение. Решение - у документа стоит метка \"Личный файл\", которую может снять только владелец файла. Свяжитесь с владельцем файла и попросите поставить метку \"Учебный файл\" \n2) На мой запрос бот выдает ошибку. Решение - перепроверьте свой запрос, убедитесь, что искомый вами документ существует и есть в базе. \n3) Я всё-всё точно проверил и перепроверил, но бот присылает сообщение о ошибке. Решение - напишите любому контакту, указанному в пункте \"О боте\", и мы постараемся решить проблему. \n \nГлавное меню",
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "aboutme"}))
async def sender(event: bot.SimpleBotEvent):
    msg_user_id = event.object.object.message.from_id

    user_info = TupleToList(clients.FindByid(msg_user_id)[0])
    temp_user_course = user_info[1]
    temp_user_group = user_info[0]
    temp_user_role = user_info[2]

    user_role = "No info"

    if (temp_user_role == "student"):
        user_role = "Студент"
    if (temp_user_role == "admin"):
        user_role = "Администратор"

    await event.answer(
        f"Твой курс: {temp_user_course} курс\nТвоя группа: {temp_user_group} группа\nТвоя роль: {user_role}",
        keyboard=keyboards.keyboard_menu())


@bot_group.message_handler(bot_group.payload_filter({"command": "checkhelp"}))
async def sender(event: bot.SimpleBotEvent):
    await event.answer("Для быстрой смены роли с администратора на студента и обратно используйте сообщение getcode",
                       keyboard=keyboards.keyboard_menu())


@bot_group.message_handler()
async def sender(event: bot.SimpleBotEvent):
    await event.answer("Я тебя не очень понял, так что добро пожаловать в...\n \nГлавное меню",
                       keyboard=keyboards.keyboard_menu())


bot_group.run_forever()
bot.run_forever()
