import win32com

outlook = win32com.client.Dispatch("Outlook.Application") #.GetNamespace("MAPI")

olMailItem = 0x0
newMail = outlook.CreateItem(olMailItem)

def Send(carbon):

    newMail.To = input('Enter who you are sending the email to: ')
    newMail.Subject - input('Enter the subject line of the email: ')

    if carbon == 'cc':
        copyNames = input('Enter the emails to cc to (Seperate by :: no spaces on either side): ')
        copyList = copyNames.split('::')
        for name in copyList:
            newMail.CC = name
    elif carbon == 'bcc':
        copyList = copyNames.split('::')
        copyNames = input('Enter the emails to bcc to *Seperate by :: no spaces on either side): ')
    elif carbon == 'both':
        print('Test')
    else:
        print('Test for else.')
    
    newMail.body = input("Enter the body of the email: *Use '\\n' for new lines)")
    # attachQuestion = input('Would you like to add attachments (Y/N)? ')

    newMail.display()

    # able to send to multiple people