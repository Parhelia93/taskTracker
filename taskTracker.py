import datetime

while True:
    inputStr = input('What is your current task? ')
    
    if inputStr == 'exit':
        break
    else:
        startTaskTime = datetime.datetime.now()
        endTaskTime = None
        strTmp_ = f'\nTask name: "{inputStr}". Date: {startTaskTime.strftime("%Y-%m-%d")}'
        try:
            with open('taskRes.txt','a') as file:
                file.write(strTmp_)
        except:
            print('Error work with file')


        while True:
            inputTask = input('For compliting task tap "done": ')
            if inputTask == 'done':
                endTaskTime = datetime.datetime.now()
                break
        seconds = (endTaskTime - startTaskTime).total_seconds()
        minutes = (seconds % 3600) // 60
        hours = seconds // 3600
        strTmp = f' Spending time: {str(hours)} hours, {str(minutes)} minutes'
        try:
            with open('taskRes.txt','a') as file:
                file.write(strTmp)
        except:
            print('Error work with file')
