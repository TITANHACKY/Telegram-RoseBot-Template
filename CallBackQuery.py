######################################################### https://t.me/TITANHACKY #########################################################


#Call Back Query
import userDetails
import chatDetails
import Messages

#Call Back Query Commands
def CallBackQuery(result):
    userId = userDetails.UserId(result)
    chatId = chatDetails.ChatId(result)
    messageId = userDetails.MessageId(result)
    try:
        callBackQuery = userDetails.CallBackQuery(result)

########################################################## HELP ##########################################################

        if('help' in callBackQuery):
            text = '''Help

Hey! My name is Rose. I am a group management bot, here to help you get around and keep the order in your groups!
I have lots of handy features, such as flood control, a warning system, a note keeping system, and even predetermined replies on certain keywords.

Helpful commands1:
- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!
- /donate: Gives you info on how to support me and my creator.

If you have any bugs or questions on how to use me, have a look at my [website](https://missrose.org/), or head to @RoseSupportChannel.
 All commands can be used with the following: / !'''
            buttons = '{"inline_keyboard":[[{"text":"Admin","callback_data":"admin"},{"text":"Antiflood","callback_data":"antiflood"},{"text":"Approval","callback_data":"approval"}],' \
                      '[{"text":"Bans","callback_data":"bans"},{"text":"Blocklist","callback_data":"blocklist"},{"text":"CAPTCHA","callback_data":"captcha"}],' \
                      '[{"text":"Connections","callback_data":"connections"},{"text":"Disabling","callback_data":"disabling"},{"text":"Federations","callback_data":"frderations"}],' \
                      '[{"text":"Filters","callback_data":"filters"},{"text":"Formatting","callback_data":"formatting"},{"text":"Greetings","callback_data":"greetings"}],' \
                      '[{"text":"Import/Export","callback_data":"importorexport"},{"text":"Languages","callback_data":"languages"},{"text":"Locks","callback_data":"locks"}],' \
                      '[{"text":"Log Channels","callback_data":"logchannel"},{"text":"Misc","callback_data":"misc"},{"text":"Notes","callback_data":"notes"}],' \
                      '[{"text":"Pin","callback_data":"pin"},{"text":"Purges","callback_data":"purges"},{"text":"Reports","callback_data":"reports"}],' \
                      '[{"text":"Rules","callback_data":"rules"},{"text":"Warnings","callback_data":"warnings"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, buttons)

########################################################## ADMIN ##########################################################

        elif('admin' in callBackQuery):
            text = '''Admin

Make it easy to promote and demote users with the admin module!

Admin commands:
- /promote <reply/username/mention/userid>: Promote a user.
- /demote <reply/username/mention/userid>: Demote a user.
- /adminlist: List the admins in the current chat
- /admincache: Update the admin cache, to take into account new admins/admin permissions.
- /anonadmin <yes/no/on/off>: Allow anonymous admins to use all commands without checking their permissions. Not recommended.

Sometimes, you promote or demote an admin manually, and Rose doesn't realise it immediately. This is because to avoid spamming telegram servers, admin status is cached locally.
This means that you sometimes have to wait a few minutes for admin rights to update. If you want to update them immediately, you can use the /admincache command; that'll force Rose to check who the admins are again.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## ANTIFLOOD ##########################################################

        elif('antiflood' in callBackQuery):
            text = '''Antiflood

You know how sometimes, people join, send 100 messages, and ruin your chat? With antiflood, that happens no more!

Antiflood allows you to take action on users that send more than x messages in a row. Actions are: ban/kick/mute/tban/tmute

Admin commands:
- /flood: Get the current antiflood settings
- /setflood <number/off/no>: Set the number of messages after which to take action on a user. Set to '0', 'off', or 'no' to disable.
- /setfloodmode <action type>: Choose which action to take on a user who has been flooding. Options: ban/kick/mute/tban/tmute'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## APPROVAL ##########################################################

        elif ('approval' in callBackQuery):
            text = '''Approval

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.

That's what approvals are for - approve of trustworthy users to allow them to send 

Admin commands:
- /approval: Check a user's approval status in this chat.

Admin commands:
- /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
- /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
- /approved: List all approved users.
- /unapproveall: Unapprove ALL users in a chat. This cannot be undone.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## BANS ##########################################################

        elif ('bans' in callBackQuery):
            text = '''Bans

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

User commands:
- /kickme: Users that use this, kick themselves.

Admin commands:
- /ban: Ban a user.
- /dban: Ban a user by reply, and delete their message.
- /sban: Silently ban a user, and delete your message.
- /tban: Temporarily ban a user.
- /unban: Unban a user.
- /mute: Mute a user.
- /dmute: Mute a user by reply, and delete their message.
- /smute: Silently mute a user, and delete your message.
- /tmute: Temporarily mute a user.
- /unmute: Unmute a user.
- /kick: Kick a user.
- /dkick: Kick a user by reply, and delete their message.
- /skick: Silently kick a user, and delete your message

Examples:
- Mute a user for two hours.
-> /tmute @username 2h'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## BLOCKLISTS ##########################################################

        elif (callBackQuery == 'blocklist'):
            text = '''Blocklists

Want to stop people asking stupid questions? or ban anyone saying censored words? Blocklists is the module for you!

From blocking rude words, filenames/extensions, to specific emoji, everything is possible.

Admin commands:
- /addblocklist <blocklist trigger> <reason>: Add a blocklist trigger. You can blocklist an entire sentence by putting it in "quotes".
- /rmblocklist <blocklist trigger>: Remove a blocklist trigger.
- /unblocklistall: Remove all blocklist triggers - chat creator only.
- /blocklist: List all blocklisted items.
- /blocklistmode <blocklist mode>: Set the desired action to take when someone says a blocklisted item. Available: nothing/ban/mute/kick/warn/tban/tmute.
- /blocklistdelete <yes/no/on/off>: Set whether blocklisted messages should be deleted. Default: (on)
- /setblocklistreason <reason>: Set the default blocklist reason to warn people with.
- /resetblocklistreason: Reset the default blocklist reason to default - nothing.

Top tip:
Blocklists allow you to use some modifiers to match "unknown" characters. For example, you can use the ? character to match a single occurrence of any non-whitespace character.
You could also use the * modifier, which matches any number of any character. If you want to blocklist urls, this will allow you to match the full thing. It matches every character except spaces. This is cool if you want to block, for example, url shorteners.'''
            button = '{"inline_keyboard":[[{"text":"Blocklist Command Examples","callback_data":"blocklistExamples"}],[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## BLOCKLIST EXAMPLES ##########################################################

        elif ('blocklistExamples' in callBackQuery):
            text = '''Blocklist Command Examples



Example blocklist commands:
- Automatically warn users who say blocklisted words.
-> /blocklistmode warn
- Override the blocklist mode for a single filter. Users that says 'boo' will get a muted for 6 hours, instead of the blocklist action.
-> /addblocklist boo Don't scare the ghosts! {tmute 6h}
- Add a full sentence to the blocklist. This would delete any message containing 'the admins suck'.
-> /addblocklist "the admins suck" Respect your admins!
- Stop any bit.ly links using the * shortcut to match any character.
-> /addblocklist "bit.ly/*" We dont like shorteners!
- Stop any bit.ly links followed by exactly three characters, to catch bit.ly/hey, but not bit.ly/abcd.
-> /addblocklist "bit.ly/???" We dont like 3 letter shorteners!
- Stop people sending zip files, by blocklisting *.zip
-> /addblocklist "*.zip" zip files are not allowed here.
- Stop any 🖕 emoji, or any stickers related to it.
-> /addblocklist 🖕 This emoji is not allowed here.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

######################################################### CAPTCHA ##########################################################

        elif ('captcha' in callBackQuery):
            text = '''CAPTCHA

Some chats get a lot of users joining just to spam. This could be because they're trolls, or part of a spam network.
To slow them down, you could try enabling CAPTCHAs. New users joining your chat will be required to complete a test to confirm that they're real people.'

Admin commands:
- /captcha <yes/no/on/off>: All users that join will need to solve a CAPTCHA. This proves they aren't a bot!
- /captchamode <button/math/text>: Choose which CAPTCHA type to use for your chat.
- /captchatime <Xw/d/h/m>: Unmute new users after X time. If a user hasn't solved the CAPTCHA yet, they get automatically unmuted after this period.
- /captchakick <yes/no/on/off>: Kick users that haven't solved the CAPTCHA.
- /captchakicktime <Xw/d/h/m>: Set the time after which to kick CAPTCHA'd users.
- /setcaptchatext <text>: Customise the CAPTCHA button.
- /resetcaptchatext: Reset the CAPTCHA button to the default text.

Examples:
- Enable captchas
-> /captcha on

NOTE:
For CAPTCHAs to be enabled, you MUST have enabled welcome messages. If you disable welcome messages, CAPTCHAs will also stop.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## CONNECTIONS ##########################################################

        elif ('connections' in callBackQuery):
            text = '''Connections

Sometimes, you just want to add some notes and filters to a group chat, but you don't want everyone to see; This is where connections come in...

This allows you to connect to a chat's database, and add things to it without the chat knowing about it! For obvious reasons, you need to be an admin to add things; but any member can view your data. (banned/kicked users can't!)

Admin commands:
- /connect <chatid/username>: Connect to the specified chat, allowing you to view/edit contents.
- /disconnect: Disconnect from the current chat.
- /reconnect: Reconnect to the previously connect chat
- /connection: See information about the currently connected chat.

You can retrieve the chat id by using the /id command in your chat. Don't be surprised if the id is negative; all super groups have negative ids.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## DISABLINGS ##########################################################

        elif ('disabling' in callBackQuery):
            text = '''Disabling

Not everyone wants every feature that Rose offers. Some commands are best left unused; to avoid spam and abuse.

This allows you to disable some commonly used commands, so noone can use them. It'll also allow you to autodelete them, stopping people from bluetexting.

Admin commands:
- /disable <commandname>: Stop users from using "commandname" in this group.
- /enable <item name>: Allow users from using "commandname" in this group.
- /disableable: List all disableable commands.
- /disabledel <yes/no/on/off>: Delete disabled commands when used by non-admins.
- /disabled: List the disabled commands in this chat.

Note:
When disabling a command, the command only gets disabled for non-admins. All admins can still use those commands.
Disabled commands are still accessible through the /connect feature. If you would be interested to see this disabled too, let me know in the support chat.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FEDERATIONS ##########################################################

        elif ('federations' in callBackQuery):
            text = '''Federations

Ah, group management. It's all fun and games, until you start getting spammers in, and you need to ban them. Then you need to start banning more, and more, and it gets painful.
But then you have multiple groups, and you don't want these spammers in any of your groups - how can you deal? Do you have to ban them manually, in all your groups?

No more! With federations, you can make a ban in one chat overlap to all your other chats.
You can even appoint federation admins, so that your trustworthiest admins can ban across all the chats that you want to protect.'''
            button = '{"inline_keyboard":[[{"text":"Admin Commamd","callback_data":"adminFederationCommand"},{"text":"Federation Owner Command","callback_data":"federationOwnerCommand"}],[{"text":"User Commands","callback_data":"userFederationCommand"}],[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FEDERATION COMMANDS FOR GROUP ADMINS ##########################################################

        elif ('adminFederationCommand' in callBackQuery):
            text = '''Admin Commands

The following is the list of all fed admin commands. To run these, you have to be a federation admin in the current federation.

Commands:
- /fban: Bans a user from the current chat's federation
- /unfban: Unbans a user from the current chat's federation
- /feddemoteme <fedID>: Demote yourself from a fed.
- /myfeds: List all feds you are an admin in.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"federations"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FEDERATION COMMANDS FOR FEDERATION OWNERS ##########################################################

        elif ('federationOwnerCommand' in callBackQuery):
            text = '''Federation Owner Commands

These are the list of available fed owner commands. To run these, you have to own the current federation.

Owner Commands:
- /newfed <fedname>: Creates a new federation with the given name. Only one federation per user.
- /renamefed <fedname>: Rename your federation.
- /delfed: Deletes your federation, and any information related to it. Will not unban any banned users.
- /fedtransfer <reply/username/mention/userid>: Transfer your federation to another user.
- /quietfed <yes/no/on/off>: Whether or not to send ban notifications when fedbanned users join the chat.
- /fedpromote: Promote a user to fedadmin in your fed. To avoid unwanted fedadmin, the user will get a message to confirm this.
- /feddemote: Demote a federation admin in your fed.
- /fednotif <yes/no/on/off>: Whether or not to receive PM notifications of every fed action.
- /fedreason <yes/no/on/off>: Whether or not fedbans should require a reason.
- /subfed <FedId>: Subscribe your federation to another. Users banned in the subscribed fed will also be banned in this one.
Note: This does not affect your banlist. You just inherit any bans.
- /unsubfed <FedId>: Unsubscribes your federation from another. Bans from the other fed will no longer take effect.
- /fedexport <csv/minicsv/json/human>: Get the list of currently banned users. Default output is CSV.
- /fedimport: Import a list of banned users.
- /setfedlog: Sets the current chat as the federation log. All federation events will be logged here.
- /unsetfedlog: Unset the federation log. Events will no longer be logged.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"federations"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FEDERATION COMMANDS FOR USERS ##########################################################

        elif ('userFederationCommand' in callBackQuery):
            text = '''User Commands

These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.

Commands:
- /fedinfo <FedID>: Information about a federation.
- /fedadmins <FedID>: List the admins in a federation.
- /fedsubs <FedID>: List all federations your federation is subscribed to.
- /joinfed <FedID>: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
- /leavefed: Leave the current federation. Only chat owners can do this.
- /fedstat: List all the federations you are banned in.
- /fedstat <user ID>: List all the federations a user has been banned in.
- /fedstat <user ID> <FedID>: Gives information about a user's ban in a federation.
- /chatfed: Information about the federation the current chat is in.
- /quietfed <yes/no/on/off>: Whether or not to send ban notifications when fedbanned users join the chat.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"federations"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FILTERS ##########################################################

        elif ('filters' in callBackQuery):
            text = '''Filters

Make your chat more lively with filters; The bot will reply to certain words!

Filters are case insensitive; every time someone says your trigger words, Rose will reply something else! can be used to create your own commands, if desired.

Commands:
- /filter <trigger> <reply>: Every time someone says "trigger", the bot will reply with "sentence". For multiple word filters, quote the trigger.
- /filters: List all chat filters.
- /stop <trigger>: Stop the bot from replying to "trigger".
- /stopall: Stop ALL filters in the current chat. This cannot be undone.

Examples:
- How to set a filter:[{"text":"Back","callback_data":"help"}]
-> /filter hello Hello there! How are you?
- How to set a multiword filter:
-> /filter "hello friend" Hello back! Long time no see!
- To save a file, image, gif, or any other attachment, simply reply to file with:
-> /filter trigger
- To get the unformatted version of a filter, to copy and edit it, simply say the trigger followed by the keyword "noformat":
-> trigger noformat'''
            button = '{"inline_keyboard":[[{"text":"Formatting","callback_data":"formatting"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FORMATTING ##########################################################

        elif ('formatting' in callBackQuery):
            text = '''Formatting

Rose supports a large number of formatting options to make your messages more expressive. Take a look!'''
            button = '{"inline_keyboard":[[{"text":"Markdown Formatting","callback_data":"markdownFormatting"},{"text":"Fillings","callback_data":"fillings"}],[{"text":"Random content","callback_data":"randomContent"}],[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

        elif ('markdownFormatting' in callBackQuery):
            text = '''Markdown Formatting

You can format your message using bold, italics, underline, and much more. Go ahead and experiment!

Supported markdown:
- `code words`: Backticks are used for monospace fonts. Shows as: code words.
- _italic words_: Underscores are used for italic fonts. Shows as: italic words.
- *bold words*: Asterisks are used for bold fonts. Shows as: bold words.
- ~strikethrough~: Tildes are used for strikethrough. Shows as: strikethrough.
- __underline__: Double underscores are used for underlines. Shows as: underline. NOTE: Some clients try to be smart and interpret it as italic. In that case, try to use your app's built-in formatting.
- [hyperlink](missrose.org): This is the formatting used for hyperlinks. Shows as: hyperlink (http://missrose.org/).
- [My button](buttonurl://missrose.org): This is the formatting used for creating buttons. This example will create a button named "My button" which opens missrose.org when clicked.
If you would like to send buttons on the same row, use the :same formatting. EG:
[button 1](buttonurl://example.com)
[button 2](buttonurl://example.com:same)
[button 3](buttonurl://example.com)
This will show button 1 and 2 on the same line, with 3 underneath.
Alternatively, check out https://missrose.org/tools/buttons/ to generate the button syntax for you.
- [note button](buttonurl://#notename): This syntax will allow you to create a button which links to a note. When clicked, the user will be redirected to Rose's PM to see the note.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"formatting"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## FILLINGS ##########################################################

        elif ('fillings' in callBackQuery):
            text = '''Fillings

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the welcome message, or mention them in a filter!

Supported fillings:
- {first}: The user's first name.
- {last}: The user's last name.
- {fullname}: The user's full name.
- {username}: The user's username. If they don't have one, mentions the user instead.
- {mention}: Mentions the user with their firstname.
- {id}: The user's ID.
- {chatname}: The chat's name.
- {rules}: Create a button to the chat's rules.
- {preview}: Enables link previews for this message. Useful when using links to Instant View pages.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"formatting"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## RANDOM CONTENT ##########################################################

        elif ('randomContent' in callBackQuery):
            text = '''Random Content

Another thing that can be fun, is to randomise the contents of a message. Make things a little more personal by changing welcome messages, or changing notes!

How to use random contents:
- %%%: This separator can be used to add "random" replies to the bot.
For example:
hello
%%%
how are you
This will randomly choose between sending the first message, "hello", or the second message, "how are you". Use this to make Rose feel a bit more customised! (only works in notes/filters/greetings)

Example welcome message::
- Every time a new user joins, they'll be presented with one of the three messages shown here.
-> /setwelcome
hello there {first}!
%%%
Ooooh, {first} is in the house!
%%%
Welcome to the group, {first}!'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"formatting"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## GREETINGS ##########################################################

        elif ('greetings' in callBackQuery):
            text = '''Greetings

Give your members a warm welcome with the greetings module! Or a sad goodbye... Depends!

Admin commands:
- /welcome <yes/no/on/off>: Enable/disable welcomes messages.
- /goodbye <yes/no/on/off>: Enable/disable goodbye messages.
- /setwelcome <text>: Set a new welcome message. Supports markdown, buttons, and fillings.
- /resetwelcome: Reset the welcome message.
- /setgoodbye <text>: Set a new goodbye message. Supports markdown, buttons, and fillings.
- /resetgoodbye: Reset the goodbye message.
- /cleanservice <yes/no/on/off>: Delete all service messages. Those are the annoying 'x joined the group' notifications you see when people join.
- /cleanwelcome <yes/no/on/off>: Delete old welcome messages. When a new person joins, or after 5 minutes, the previous message will get deleted.

Examples:
- Get the welcome message without any formatting
-> /welcome noformat'''
            button = '{"inline_keyboard":[[{"text":"CAPTCHA","callback_data":"captcha"},{"text":"Formatting","callback_data":"formatting"}],[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## CHAT IMPORT OR EXPORT ##########################################################

        elif ('importExport' in callBackQuery):
            text = '''Import/Export

Some people just want to see the world burn. Others, just want to have a way of grouping their chat data in one place so they can export their configuration to other chats!

Rose allows you to import/export settings for chat, so you can quickly set up other chats using a preexisting template. Instead of setting the same settings over and over again in different chats, you can use this feature to copy the general configuration across groups.
The generated file is in standard JSON format, so if there are any settings you don't want to import to your other chats, just open the file and edit it before importing.
Exporting settings can be done by any administrator, but for security reasons, importing can only be done by the group creator.

The following modules will have their data exported:
- admin
- antiflood
- blocklists
- disabled
- federations
- filters
- greetings
- locks
- notes
- pins
- reports
- rules
- translations
- warns

Chat owner commands:
- /export: Generate a file containing all your chat data.
- /import: Import the settings in the replied to data file.

Examples:
- To export only specific categories, use:
-> /export notes filters
- Or, to import only specific categories from a file, use:
-> /import rules greetings

Note: To avoid abuse, this command is heavily rate limited; this is to make sure that people importing/exporting data don't slow down the bot.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## LANGUAGES ##########################################################

        elif ('languages' in callBackQuery):
            text = '''Languages

Not every group speaks fluent english; some groups would rather have Rose respond in their own language.

This is where translations come in; you can change the language of most replies to be in the language of your choice!

Available languages are:
- AR (العربية)
- CKB (کوردیی ناوەندی)
- DE (Deutsch)
- EN-GB (British English)
- ES (español)
- ES-AR (español)
- FA (فارسی)
- FR (français)
- HE (עברית)
- ID (Indonesia)
- IT (italiano)
- KM (ខ្មែរ)
- ML-IN (മലയാളം)
- NL (Nederlands)
- PA (ਪੰਜਾਬੀ)
- PL (polski)
- PT-BR (português)
- RU (русский)
- TA (தமிழ்)
- TR (Türkçe)
- UZ (o‘zbek)
- VI (Tiếng Việt)
- ZH-CN (中文)
- ZH-TW (繁體中文)


Admin commands:
- /setlang <language>: Set your preferred language.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## LOCKS ##########################################################

        elif ('locks' in callBackQuery):
            text = '''Locks

Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!

The locks module allows you to lock away some common items in the telegram world; the bot will automatically delete them!

Admin commands:
- /lock <item(s)>: Lock one or more items. Now, only admins can use this type!
- /unlock <item(s)>: Unlock one or more items. Everyone can use this type again!
- /locks: List currently locked items.
- /lockwarns <yes/no/on/off>: Enabled or disable whether a user should be warned when using a locked item.
- /locktypes: Show the list of all lockable items.
- /allowlist <url/id/@channelname(s)>: Allowlist a URL, group ID, channel @, or bot @ to stop them being deleted by URL, forward, invitelink, and inline locks. Separate with a space to add multiple items at once. If no arguments are given, returns the current allowlist.
- /rmallowlist <url/id/@channelname(s)>: Remove an item from the allowlist - url, invitelink, and forward locking will now take effect on messages containing it again. Separate with a space to remove multiple items.

Examples:
- Lock stickers with:
-> /lock sticker
- You can lock/unlock multiple items by chaining them:
-> /lock sticker photo gif video
- To allow forwards from a specific channel, eg @RoseSupport, you can allowlist it. You can also use the ID, or invitelink:
-> /allowlist @RoseSupport'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## LOG CHANNELS ##########################################################

        elif ('logchannels' in callBackQuery):
            text = '''Log Channels

Recent actions are nice, but they don't help you log every action taken by the bot. This is why you need log channels!

Log channels can help you keep track of exactly what the other admins are doing. Bans, Mutes, warns, notes - everything can be moderated.

Setting a log channel is done by the following steps:
 - Add Rose to your channel, as an admin. This is done via the "add administrators" tab.
 - Send /setlog to your channel.
 - Forward the /setlog command to the group you wish to be logged.
 - Congrats! all done :)

Admin commands:
- /logchannel: Get the name of the current log channel.
- /setlog: Set the log channel for the current chat.
- /unsetlog: Unset the log channel for the current chat.
- /log <category>: Enable a log category - actions of that type will now be logged.
- /nolog <category>: Disable a log category - actions of that type will no longer be logged.
- /logcategories: List all support categories, with information on what they refer to.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## MISC ##########################################################

        elif ('misc' in callBackQuery):
            text = '''Misc

An "odds and ends" module for small, simple commands which don't really fit anywhere.

Commands:
- /runs: Respond with a randomly generated "run away" string.
- /id: Get a user's ID.
- /info: Get a user's info.
- /donate: Donate to the bot creator.
- /markdownhelp: Information on how to use markdown with the bot. PM only.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## NOTES ##########################################################

        elif ('notes' in callBackQuery):
            text = '''Notes

Save data for future users with notes!

Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!

User commands:
- /get <notename>: Get a note.
- #notename: Same as /get.

Admin commands:
- /save <notename> <note text>: Save a new note called "word". Replying to a message will save that message. Even works on media!
- /clear <notename>: Delete the associated note.
- /notes: List all notes in the current chat.
- /saved: Same as /notes.
- /clearall: Delete ALL notes in a chat. This cannot be undone.
- /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM.'''
            button = '{"inline_keyboard":[[{"text":"Example Usage","callback_data":"notesExample"},{"text":"Formatting","callback_data":"formatting"}],[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## EXAMPLE FOR NOTES ##########################################################

        elif ('notesExample' in callBackQuery):
            text = '''Example Usage

Notes can seem quite complicated; so here are some examples, so you can get some inspiration.

Examples:
- Saving a note. Now, anyone using #test or /get test will see this message. To save an image, gif, sticker, or any other kind of data, simply reply to that message
-> /save test This is a fancy note!
- To retrieve a note without formatting, add noformat after the get command. This will retrieve the note with no formatting, allowing you to copy and edit it.
-> /get notename noformat
- You can also link notes through notebuttons. To do this, simply use the notename as the URL:
-> /save note This is a note [With a button](buttonurl://#anothernote)
- To send all notes to the user's PM:
-> /privatenotes on
- To send a single note to user's PM, add a {private} tag to your note:
-> /save test This is a note that always goes to PM {private}
- If you've enabled privatenotes, but have one note that you don't want to go to PM:
-> /save test This is a note that always goes to groups {noprivate}'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"notes"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## PIN ##########################################################

        elif ('pin' in callBackQuery):
            text = '''Pin

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

User commands:
- /pinned: Get the current pinned message.

Admin commands:
- /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
- /permapin <text>: Pin a custom message through the bot. This message can contain markdown, buttons, and all the other cool features.
- /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.
- /unpinall: Unpins all pinned messages.
- /antichannelpin <yes/no/on/off>: Don't let telegram auto-pin linked channels. If no arguments are given, shows current setting.
- /cleanlinked <yes/no/on/off>: Delete messages sent by the linked channel.

Note: When using antichannel pins, make sure to use the /unpin command, instead of doing it manually. Otherwise, the old message will get re-pinned when the channel sends any messages.'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## PURGES ##########################################################

        elif ('purges' in callBackQuery):
            text = '''Purges

Need to delete lots of messages? That's what purges are for!

Admin commands:
- /purge: Delete all messages from the replied to message, to the current message.
- /purge <X>: Delete the following X messages after the replied to message.
- /spurge: Same as purge, but doesnt send the final confirmation message.
- /del: Deletes the replied to message.
- /purgefrom: Reply to a message to mark the message as where to purge from - this should be used followed by a /purgeto.
- /purgeto: Delete all messages between the replied to message, and the message marked by the latest /purgefrom.

Examples:
- Delete all messages from the replied to message, until now.
-> /purge
- Mark the first message to purge from (as a reply).
-> /purgefrom
- Mark the message to purge to (as a reply). All messages between the previously marked /purgefrom and the newly marked /purgeto will be deleted.
-> /purgeto'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## REPORTS ##########################################################

        elif ('reports' in callBackQuery):
            text = '''Reports

We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?

Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.

User commands:
- /report: Reply to a message to report it for admins to review.
- admin: Same as /report

Admin commands:
- /reports <yes/no/on/off>: Enable/disable user reports.

To report a user, simply reply to his message with @admin or /report; Rose will then reply with a message stating that admins have been notified. This message tags all the chat admins; same as if they had been @'ed.

Note that the report commands do not work when admins use them; or when used to report an admin. Rose assumes that admins don't need to report, or be reported!'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## RULES ##########################################################

        elif ('rules' in callBackQuery):
            text = '''Rules

Every chat works with different rules; this module will help make those rules clearer!

User commands:
- /rules: Check the current chat rules.

Admin commands:
- /setrules <text>: Set the rules for this chat. Supports markdown, buttons, fillings, etc.
- /privaterules <yes/no/on/off>: Enable/disable whether the rules should be sent in private.
- /resetrules: Reset the chat rules to default.
- /setrulesbutton: Set the rules button name when using {rules}.
- /resetrulesbutton: Reset the rules button name from {rules} to default.'''
            button = '{"inline_keyboard":[[{"text":"Formatting","callback_data":"formatting"}],[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

########################################################## WARNINGS ##########################################################

        elif ('warnings' in callBackQuery):
            text = '''Warnings

Keep your members in check with warnings; stop them getting out of control!

If you're looking for automated warnings, go read about the blacklist module.

Admin commands:
- /warn <reason>: Warn a user.
- /dwarn <reason>: Warn a user by reply, and delete their message.
- /swarn <reason>: Silently warn a user, and delete your message.
- /warns: See a user's warnings.
- /rmwarn: Remove a user's latest warning.
- /resetwarn: Reset all of a user's warnings to 0.
- /resetallwarns: Delete all the warnings in a chat. All users return to 0 warns.
- /warnings: Get the chat's warning settings.
- /setwarnmode <ban/kick/mute/tban/tmute>: Set the chat's warn mode.
- /setwarnlimit <number>: Set the number of warnings before users are punished.
- /setwarntime <time>: Set how long warnings should last.Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.

Examples:
- Warn a user.
-> /warn @user For disobeying the rules'''
            button = '{"inline_keyboard":[[{"text":"Back","callback_data":"help"}]]}'
            Messages.editMessageWithButton(text, chatId, messageId, button)

    except:
        pass


######################################################### https://t.me/TITANHACKY #########################################################