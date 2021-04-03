######################################################### https://t.me/TITANHACKY #########################################################


#User Details

#User Id
def UserId(result):
    try:
        userId = result['message']['from']['id']
    except:
        userId = result['callback_query']['message']['from']['id']
    return userId

#User Name
def UserName(result):
    try:
        userName = result['message']['from']['username']
    except:
        userName = ''
    return userName

#User First Name
def UserFirstName(result):
    try:
        userFirstName = result['message']['from']['first_name']
    except:
        userFirstName = ''
    return userFirstName

#User Last Name
def UserLastName(result):
    try:
        userLastName = result['message']['from']['last_name']
    except:
        userLastName = ''
    return userLastName

#The User Is Bot Or Not
def IsBot(result):
    isBot = result['message']['from']['is_bot']
    return isBot

#Message Id
def MessageId(result):
    try:
        messageId = result['message']['message_id']
    except:
        messageId = result['callback_query']['message']['message_id']
    return messageId

#Text
def Text(result):
    try:
        text = result['message']['text']
    except:
        text = ''
    return text

#photo
def Photo(result):
    try:
        photo = result['message']['photo']['0']['file_id']
    except:
        photo = ''
    return photo

#video
def Video(result):
    try:
        video = result['message']['video']['file_id']
    except:
        video = ''
    return video

#Document
def Document(result):
    try:
        document = result['message']['document']['file_id']
    except:
        document = ''
    return document

#callback_query
def CallBackQuery(result):
    try:
        callBackQuery = result['callback_query']['data']
    except:
        callBackQuery = ''
    return callBackQuery


######################################################### https://t.me/TITANHACKY #########################################################