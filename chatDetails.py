######################################################### https://t.me/TITANHACKY #########################################################


#Chat Details

#Chat Id
def ChatId(result):
    try:
        chatId = result['message']['chat']['id']
    except:
        chatId = result['callback_query']['message']['chat']['id']
    return  chatId

#Chat User Name
def ChatUserName(result):
    try:
        chatUserName = result['message']['from']['username']
    except:
        chatUserName = ''
    return chatUserName

#Chat Title
def ChatTitle(result):
    try:
        userName = result['message']['chat']['title']
    except:
        userName = ''
    return userName

#Chat Type (Private or Group)
def Type(result):
    try:
        type = result['message']['chat']['type']
    except:
        type = ''
    return type

######################################################### https://t.me/TITANHACKY #########################################################