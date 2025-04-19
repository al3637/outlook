import win32com.client
import time
import datetime

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

def delete(email, userFolder, sender, loop):
    if loop == 'y':
        interval = int(input('How long would you like the interval to be (Enter a time in seconds): '))
        print('\n')
        print('Keep the terminal and the Outlook Application open while the program is running.')

    folderList = userFolder.split('::')
    folderCount = 0

    for j in folderList:
        folderCount += 1
    
    emailList = sender.split('::')
    emailCount = 0

    if 'bot' in sender:
        emailList.extend(['example email', 'example email', 'example email', 'example email', 'example email',
                          'example email'])
        emailList.remove('bot')
    elif 'where' in sender:
        emailList.extend(['example email', 'example email', 'example email'])
    elif 'normal' in sender:
        emailList.extend(['example email', 'example email', 'example email', 'example email', 'example email', 'example email',
                          'example email', 'example email', 'example email', 'example email', 'example email', 'example email'])
        emailList.remove('normal')
    elif 'team' in sender:
        emailList.extend(['example email', 'example email', 'example email', 'example email', 'example email', 'example email',
                        'example email', 'example email', 'example email', 'example email', 'example email'])
    
    for a in emailList:
        emailCount += 1
    
    totalEmails = 0

    while True:
        beginTime = datetime.datetime.now()
        print(f'\nStarted: {beginTime}')
        for i in folderList:

            totalTimeBegin = datetime.datetime.now()

            if i == 'Inbox':
                folder = outlook.GetDefaultFolder(6)
            elif i == 'Deleted Items':
                folder = outlook.GetDefaultFolder(3)
            else:
                folder = outlook.Stores.Item(email).GetRootFolder().Folders.Item("Inbox").Folders.Item(i)

            for l in emailList:

                deleteCount = 0
                count = 0
                begin = datetime.datetime.now()

                while True:
                    for message in folder.items:
                        if message.SenderName == l:
                            deleteCount += 1
                            count += 1
                
                while True:
                    for message in folder.Items:
                        if message.SenderName == l:
                            message.Delete()
                            count -=1
                            totalEmails += 1
                    if count == 0:
                        break
                end = datetime.datetime.now()
                break

                totalTime = end - begin

                if deleteCount != 0:
                    print('\n')
                    print(f'Inbox: {i}')
                    print(f'Number of emails deleted from {l}: {deleteCount}')
                    print(f'Time Taken: {totalTime}')
                
                emailCount -= 1

                if emailCount == 0:
                    totalTimeEnd = datetime.datetime.now()
                    print(f'\nTotal Emails Deleted: {totalEmails}')
                    print(f'Total Time Taken: {totalTimeEnd - totalTimeBegin}')
                
            folderCount -= 1

            if loop =='n':
                if folderCount == 0:
                    endTime = datetime.datetime.now()
                    print(f'Ended: {endTime}')
                    print(f'Total Time: {endTime - beginTime}')
                    break
            else:
                time.sleep(interval)

# Make it so the count can do multiple emails
# Add sending capabilities
# Also add reading optinos for inboxes and all new emails
# Make it so that it displays all hte emials from a certain person/people in any amount of folders
# Something ot mark everthing in an inbox as read everything

# Delete emails after a certain date/time