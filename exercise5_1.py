count = 0
sum = 0
tempString = ''
while(tempString != 'done'):
    tempString = input('Enter a number:')
    try:
        sum += float(tempString)
        count += 1
    except:
        if(tempString != 'done'):
            print('bad data')

print(sum, count, sum / count )
