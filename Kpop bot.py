print('***Hello welcome to K-bot***')
name = input('Before we start, may I ask for your name: ').capitalize()

print('Thank you for using K-bot', name, 'remember to give us a rating according to your experiencing in using the bot')
print('I figure you are a big kpop fan if you are here, Welcome to the fandom', name)
print('K-bot makes it easy for users to prepare for kpop concerts and notifies you for a nearby'
      'kpop concert and gives you a safe space for talking about kpop')
continent = input('So which continent are you from: ').capitalize()

answer = ['America', 'Asia', 'Europe', 'Australia', 'Africa', 'Antarctica']

for i in range(3):
    if continent == 'America' or continent == 'Asia' or continent == 'Europe' or continent == 'Australia':
        print('you are in luck, We have alot of kpop groups coming to perform for the next three weeks in', continent)
        kpop_group = int(input('So how many kpop groups do you like (number): '))
        break

    elif continent == 'Africa' or continent == 'Antarctica':
        print('Oh', continent, '? Sorry I dont think there is any kpop group scheduled to perform')
        print('but if we see one we will let you know')
        kpop_group = int(input('so how many kpop groups do you like (number): '))
        break
    else:
        continent = input('Please enter a continent: ')

if continent not in answer:
    print('I am sorry we cant seem to know the continent. Go back to school and learn about your Geography')
    print('Seems like you are the flat earthers HA HA HA HA')
    exit(None)

if kpop_group >= 20:
    print('Wow you are an OG kpop fan')

elif kpop_group >= 10:
    print('Wow you know alot of groups, you are a fan')

elif kpop_group >= 3:
    print('you must be a newbie in the fandom, welcome', name)

else:
    print('OMG what are you doing here if you only know', kpop_group, 'group(s)')
    print('Enda tu youtube najua unajifanya kuwa fan **rolling eyes**')
    exit(None)

company = input("We all have a fav group which company does your group belong to: ").upper()

if company == 'JYP' or company == 'HYBE' or company == 'YG' or company == 'SM TOWN':
    print("oooooooh that's nice....I believe it is a popular group if it is in", company)
    group = input("so what is your favorite group: ")
    if continent == 'America' or continent == 'Asia' or continent == 'Europe' or continent == 'Australia':
        print('Wow you are in luck', group, 'is coming to perform in', continent)
        print('so let me help you to prepare for the concert')
    else:
        print('We are sorry but', group, 'has not scheduled any performance in the next month in', continent)
        print('But we have exciting news....', group, 'will come next year in', continent)
        print('so let me help you to prepare for the concert')
else:
    print("Sorry but I do not know the company")
    group = input("so what is your favorite group: ")
    if continent == 'America' or continent == 'Asia' or continent == 'Europe' or continent == 'Australia':
        print('Wow you are in luck', group, 'is coming to perform in', continent)
        print('so let me help you to prepare for the concert')
    else:
        print('We are sorry but', group, 'has not scheduled any performance in the next month in', continent)
        print('But we have exciting news....', group, 'will come next year in', continent)
        print('so let me help you to prepare for the concert')

print('we need to make sure you have', group, 'merchandise')
merch = input('Do you have any merchandise? ').capitalize()

if merch == 'Yes':
    print('Wow that is great, all you need to do is carry it to the concert.')
    thing = input('Give me one fav merch: ')
    print('That is nice, idols love to see their fans with', thing)
else:
    print('That is okay, I understand kama unapelekwa na economy vibaya HAHAHA')
    print('Ive got recommendations where you can get cheap merchandise')
    interest = input('Are you interested? ').capitalize()

    if interest == 'Yes':
        print('There are a lot of affordable merch in GoTo Store. Dont waste time they have a 50% off discount rn')
    else:
        print('Its okay fashionable clothes can still work')

