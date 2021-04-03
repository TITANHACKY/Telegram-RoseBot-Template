######################################################### https://t.me/TITANHACKY #########################################################


#Messages
import userDetails
import chatDetails
import config
import requests

#Sending Message
def sendMessage(text, chatId):
    text = text.replace("#", "%23")
    text = text.replace("_", "\_")
    text = text.replace("*", "\*")
    text = text.replace("`", "\`")
    url =f"{config.BotToken()}/sendMessage?chat_id={chatId}&text={text}&parse_mode=Markdown&disable_web_page_preview=True"
    requests.get(url)

#Sending Message With Buttons
def sendMessageWithButton(text, chatId, button):
    text = text.replace("#", "%23")
    text = text.replace("_", "\_")
    text = text.replace("*", "\*")
    text = text.replace("`", "\`")
    reply = '{"inline_keyboard":[[{"text":"Add Me To Your Group","url":"https://telegram.me/TheCarbonShBot?startgroup=true"}]]}'
    url = f"{config.BotToken()}/sendMessage?chat_id={chatId}&text={text}&parse_mode=Markdown&disable_web_page_preview=True&reply_markup={button}"
    print(url)
    requests.get(url)

#Editing Message With Buttons
def editMessageWithButton(text, chatId, messageId, button):
    text = text.replace("#", "%23")
    text = text.replace("_", "\_")
    text = text.replace("*", "\*")
    text = text.replace("`", "\`")
    url =f"{config.BotToken()}/editMessageText?chat_id={chatId}&message_id={messageId}&text={text}&parse_mode=Markdown&disable_web_page_preview=True&reply_markup={button}"
    print(url)
    requests.get(url)

#Setting Commands
def Messages(result):
    userId = userDetails.UserId(result)
    userName = userDetails.UserName(result)
    userFirstName = userDetails.UserFirstName(result)
    userLastName = userDetails.UserLastName(result)
    chatType = chatDetails.Type(result)
    chatId = chatDetails.ChatId(result)
    chatTitle = chatDetails.ChatTitle(result)
    chatUsername = chatDetails.ChatUserName(result)
    try:
        text = userDetails.Text(result)
        if('/start' in text):
            text = '''Hey there! My name is Rose - I'm here to help you manage your groups! Hit /help to find out more about how to use me to my full potential.

Join my news [channel](http://t.me/thePegion) to get information on all the latest updates.'''
            button = '{"inline_keyboard":[[{"text":"Add me to your chat","url":"https://telegram.me/Carbonise_Bot?startgroup=true"}]]}'
            sendMessageWithButton(text, userId, button)

        elif('/help' in text):
            text = '''Help
            
Hey! My name is Rose. I am a group management bot, here to help you get around and keep the order in your groups!
I have lots of handy features, such as flood control, a warning system, a note keeping system, and even predetermined replies on certain keywords.

Helpful commands1:
- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!
- /donate: Gives you info on how to support me and my creator.

If you have any bugs or questions on how to use me, have a look at my [website](https://missrose.org/), or head to @thePegionDiscussion.
 All commands can be used with the following: / !'''
            buttons = '{"inline_keyboard":[[{"text":"Admin","callback_data":"admin"},{"text":"Antiflood","callback_data":"antiflood"},{"text":"Approval","callback_data":"approval"}],' \
                      '[{"text":"Bans","callback_data":"bans"},{"text":"Blocklist","callback_data":"blocklist"},{"text":"CAPTCHA","callback_data":"captcha"}],' \
                      '[{"text":"Connections","callback_data":"connections"},{"text":"Disabling","callback_data":"disabling"},{"text":"Federations","callback_data":"federations"}],' \
                      '[{"text":"Filters","callback_data":"filters"},{"text":"Formatting","callback_data":"formatting"},{"text":"Greetings","callback_data":"greetings"}],' \
                      '[{"text":"Import/Export","callback_data":"importorExport"},{"text":"Languages","callback_data":"languages"},{"text":"Locks","callback_data":"locks"}],' \
                      '[{"text":"Log Channels","callback_data":"logchannels"},{"text":"Misc","callback_data":"misc"},{"text":"Notes","callback_data":"notes"}],' \
                      '[{"text":"Pin","callback_data":"pin"},{"text":"Purges","callback_data":"purges"},{"text":"Reports","callback_data":"reports"}],' \
                      '[{"text":"Rules","callback_data":"rules"},{"text":"Warnings","callback_data":"warnings"}]]}'
            sendMessageWithButton(text,userId,buttons)

    except:
        pass


######################################################### https://t.me/TITANHACKY #########################################################