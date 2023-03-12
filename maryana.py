import telebot
import openai

bot = telebot.TeleBot("5832104073:AAEpP3fc5IMv4Tm4G_cyt6P4XYdu9yUWSRI")
openai.api_key = "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"
 
# python maryana.py

@bot.message_handler(content_types=['text'])
def lalala(message):
    if "/start" in message.text.lower():
        bot.send_message(message.chat.id, "Привіт, запитай у мене що небудь")
    elif "путін" in message.text.lower():
        bot.send_message(message.chat.id, "цей гівнюк - XYйл0")
    elif "хто ти" in message.text.lower():
        bot.send_message(message.chat.id, "Я Мар'яна")
    elif "вова" in message.text.lower():
        bot.send_message(message.chat.id, "красавчик який написав цей код")
    elif "Маряна" in message.text.lower():
        bot.send_message(message.chat.id, "Кохана")
    elif "автор бот" in message.text.lower():
        bot.send_message(message.chat.id, "Слуценко Володимир Миколайович")
    elif "контакт автор" in message.text.lower():
        bot.send_message(message.chat.id, "http://citrus.infinityfreeapp.com/")
    else:
        print(message.chat.title, message.chat.username)
        #if message.chat.id == -1905120293:
        #print(message.text) 
        #if "Vova712" in message.chat.username:
        message.text = (message.text).replace("@MarSlu_bot ", "")
        print(message.text)
        response = openai.Completion.create(model="text-davinci-003", prompt=message.text, max_tokens=1000)
        full_response = response['choices'][0]['text']  # Use the text property of the first element of the choices list to access the full response
        lines = full_response.splitlines()  # Split the response into individual lines 
        for line in lines:  # Iterate over the lines
                try:
                    print(line)
                    bot.send_message(message.chat.id, line)  # Send each line back to the user as a separate message
                except Exception as e:
                    print(e)
    #else:
    #   bot.send_message(message.chat.id, "Вибачте, доступний тільки в группі https://t.me/+ncj0nXkZDCdhYjY6")
 
bot.polling(none_stop=True, interval=0)

# key_words = ["1111", "3333"]  # Вводимо ключові слова які будемо шукати в повідомленнях
 
# @client.on(events.NewMessage(chats=[-100*********, ************]))  
# # Запускаємо наш клієнт та сказуемо на які саме канали реагувати

# async def normal_handler(event):  # Обробляємо подію
#     for i in range(len(key_words)):  # Перебираємо всі ключові слова з нашого списку
#         if key_words[i] in event.message.message:  # Перевіряємо коне слово на наявність його в нашому повідомленні
#             print(event.message)
#             print(event.message.peer_id,
#                   event.message.message)  # Роздруковуемо в консоль id чату/групи та текст знайденного повідомлення (не обов'язково)
#             await client.send_message(target_can, event.message)  # Пересилаємо знайдене повідомлення
 
# client.start()  # Запускаємо кліент
# client.run_until_disconnected()  # Ставимо його в бескінечний цикл
