import win32com.client
import time

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

def emailCount(folderList, sender, loop):

    if loop == 'y':
        interval = int(input("How long would you like the interval to be (Enter a time in seconds): "))
        print("Keep the terminal and the Outlook Application open while the program is running.")
    
    while True:
        for f in folderList:
            folder = outlook.Stores.Item("example email").GetRootFolder().Folders.Item("Inbox").Folders.Item(f)
            count = 0
            for message in folder.Items:
                if message.SenderName == sender:
                    count += 1
            print(f"\nEmails from {sender} in {f}: {count}")
            
        if loop == 'n':
            break
        else:
            time.sleep(interval)