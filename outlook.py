from delete import *
from count import *
from send import *

if __name__ == "__main__":

    email = input('Enter your email: ')

    if email == 'morning':
        delete('example email', 'example folder', 'normal', 'n')
    elif email == 'bot':
        delete('example email', 'example folder', 'bot', 'n')
    elif email == 'team':
        delete('example email', 'example folder', 'purge', 'n')
    else:
        question = input('Would you like to count, delete, or send emails? ').lower()

        if question =='count':
            userFolder = input('Enter the folders for emails to be counted from (Seperate by:: no spaces on each side): ')
            folderList = userFolder.split('::')
            sender = input('Enter an email hwose emails will be counted: ')
            loop = input('Would you like this to run constantly? (Y/N)?').lower()
            emailCount(folderList, sender, loop)
        elif question == 'delete':
            userFolder = input('Enter the folders you would like emails deleted from (Seperated by :: with no spaces before and after the colons.: )')
            sender = input("Enter the names of the emails that are to be deleted (Sepererated by :: with no spaces before and after the colons.): ")
            loop = input('Would you like this to run constantly (Y/N)?').lower()
            delete(email, userfolder, sender, loop)
        elif question == 'send':
            carbon = input('Would you like to cc or bcc anyone (cc/bcc/Both/Neither) (Seperate by :: no spaces to either side of the colons): ')
            send()

# Use sys.argv to not have to even need the input for writing morning and all
# Write something to analyze the times taked for each email and see if it gets less the more emails are deleted (make graph?)