import time
import sys
# util.py
import random

dadjokes =[
    'Hva spiser frukter på ferie, Pæreis',
    'Høne med slips',
    'Jeg er redd for kalenderen, dens dager er talte.',
    'En blind mann går inn i en bar, og et bord og en stol.'
]

work_locations =[
    'Pizza leveranse',
    'Foodora',
    'Mega',
    'McDonalds',
    'Circle K'
]

def get_dadjoke() -> str:
    """Returns a random dad joke"""
    return random.choice(dadjokes)

def add_dadjoke(joke: str) -> None:
    dadjokes.append(joke)

def load_jokes():
    dadjokes = 'lastet inn'

def save_jokes():
    dadjokes = 'lagret'

balance = int(100)
not_work = True
player_icon = ' '
winning_icon = ' '
dize_bet = 0
icon = 0
work_location = ' '

#dize ikoner
dize_icons = [
                    '⚀',
                    '⚁',
                    '⚂',
                    '⚃',
                    '⚄',
                    '⚅'
                ]

#valga man har i rpsls
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

#alle de forskjellige joksa.
kommandoer = {
    "?joke": "Jeg forteller en dårlig dad-joke.",
    "?gay": "Jeg vil fortelle deg hvor gay du er",
    '?balance': 'Sjekke hvor mye du har i banken.',
    '?work' : 'Finn deg en jobb, eller jobb på jobben du har.',
    '?quit job' : 'Du vil slutte i jobben din.',
    '?lucky dice' : 'Gamble pengene dine i et spill av lucky dice.',
    '?rpsls' : 'Spill et spill med rock, paper, scissors, lizard and spock.',
    "quit": "Avslutt samtale."
}


#onbording
navn = input('Hva heter du?')
if not navn:
    raise ValueError
print(f'Hei, {navn} ')
alder = input('Hvor gammer er du? ')

print('Skriv ?hjelp for å komme i gang.')
#start robot
while True:
    match input('$: '):
        case '?hjelp':
            print('Jeg kan følgende kommandoer.')
            for kommando in kommandoer:
                print(f'{kommando} - {kommandoer[kommando]}')
            # for cmd, val in kommandoer.items():
            #   print('f'{cmd} - {val}')
        case '?joke':
            print(get_dadjoke())
        case '?gay':
            #valger et random tall mellom 1 og 100
            print(f'{navn} er {random.randint(0, 99)}% gay.')
        case '?balance':
            #sjekker hvor mye du har i banken
            print(f'Du har {balance} i banken.')
        case '?work':
            #sjekker om du har en jobb
            if not_work == True:
                #hvis du ikke har en kan du velge en jobb
                print('Er du litt fattig, du kan jobbe hos en av våre gode jobbpartner.')
                print('1 - Foodora')
                print('2 - Mega')
                print('3 - McDonalds')
                print('4 - Circle K')
                work = input('$: ')
                if work == '1':
                    work_location = 'Foodora'
                    print(f'Nå jobber du på {work_location}.')
                    not_work = False
                elif work == '2':
                    work_location = 'Mega'
                    print(f'Nå jobber du på {work_location}.')
                    not_work = False
                elif work == '3':
                    work_location = 'McDonalds'
                    print(f'Nå jobber du på {work_location}.')
                    not_work = False
                elif work == '4':
                    work_location = 'Circle K'
                    print(f'Nå jobber du på {work_location}.')
                    not_work = False
                else:
                    print('Velg mellom de 4 valgene')
            else:
                #hvis du har en jobb kan du velge hvor lenge du vil jobbe
                print('Hvor lenge vil du jobbe?')
                work_balance = 0
                robbed = False
                timer = int(input('$: '))
                for i in range(timer):
                    # 8 prosent sjans for at dette skjer
                    if random.randint(0,100) < 8:
                        robbed = True
                    if robbed == False:
                        #hvis du ikke blir robbet tjener du mellom 20-150
                        work_balance = work_balance + 1 * random.randint (20,150)
                    else:
                        #du tjener ingenting på heile skiftet ditt ( dette gjør at man ikke bare kan skrive 5000 timer.
                        work_balance = 0
                #legger det du tjente inn i banken
                balance = balance + work_balance
                if robbed == True:
                    print('Du ble robbet under skift og tjente ingenting denne dagen. ')
                else:
                    print(f'Du tjente {work_balance} i dag.')
        case '?quit job':
            #sjekker om du har en jobb
            if not_work == False:
                #du slutter hos jobben din og ?work vil gi deg en ny en
                not_work = True
                print(f'Du har nå sluttet hos {work_location}')
            else:
                #Du har ingen jobb å slutte fra
                print('Du har ingen jobb, skriv ?work for å finne deg en. ')

        case '?lucky dice':
            print('Hvor mye vil du vedde?')
            bet = int(input('$ '))
            #sjekker om du har pengene i banken
            if (bet -1) >= balance:
                print(f'Du har ikke {bet} i banken')
            else:
                print(f'Du vedder {bet}')
                balance = balance - bet
                winnings = 0
                print(f'Velg et symbol mellom 1 - 6. ')

                svar = input(f'$: ')
                #gjør nummeret ditt om til et symbol
                if svar == '1':
                    player_icon = '⚀'
                elif svar == '2':
                    player_icon = '⚁'
                elif svar == '3':
                    player_icon = '⚂'
                elif svar == '4':
                    player_icon = '⚃'
                elif svar == '5':
                    player_icon = '⚄'
                elif svar == '6':
                    player_icon = '⚅'
                else:
                    print('Feil! Velg mellom 1 - 6')

                #gjør det 3 ganger
                for i in range(0, 3):
                    #bytter på terningen random 15 ganger
                    for x in range(0, 15):
                        sys.stdout.write('\r' + random.choice(dize_icons))
                        time.sleep(0.1)
                    #velger vinnertallet
                    winning_icon = random.choice(dize_icons)
                    sys.stdout.write('\r' + winning_icon)
                    print(' ')

                    #sjekker om spilleren veddet på det samme som vinnertalet
                    if winning_icon == player_icon:
                        #Hvis du veddet på det samme dobler den beten din
                        winnings = winnings + (bet * 2)

                    #Hvis ikke det var det samme blir winnings samme verdi
                    else:
                        winnings = winnings

                #sjekker om du vant noe
                if winnings == 0:
                    print('Dessvrere vant du ingenting denne gang. ')
                else:
                    print(f'Du vant {winnings}. ')
                    balance = balance + winnings

        #cheatcode hvis du trenger penger
        case 'apekatt':
            print("You're breaking the matrix. ")
            money = int(input('Hvor mye vil du ha?'))
            balance = balance + money

        case '?rpsls':
            print('Vil du spille med penger, Ja eller Nei')
            svar = input('$: ')
            #Sjekker om du vil spille med eller uten
            if (svar == 'Ja') or (svar == 'ja') or (svar == 'JA'):
                print('Hvor mye vil du vedde?')
                bet = int(input('$ '))
                #sjekker om du har beten i banken
                if (bet - 1) >= balance:
                    print(f'Du har ikke {bet} i banken')
                else:
                    print(f'Du vedder {bet}')
                    balance = balance - bet
                    #pcen velger et random valg
                    computer_choice = random.choice(choices)
                    #sier at du må velge mellom valgene
                    print('Velg mellom (rock/paper/scissors/lizard/spock)')
                    user_choice = input('$: ')

                    #sjekker om det du skreiv inn var et av valga
                    if user_choice not in choices:
                        print('Ikke gyldigt valg. Velg mellom rock, paper, scissors, lizard eller spock.')

                    #hvis det du valge og pcen valgte var det samme blir det uavgjort
                    if user_choice == computer_choice:
                        print(f'Det ble uavgjort. Jeg valgte{computer_choice} og. ')
                        balance = balance + bet
                    #sjekker om det du valgte slår det pcen valgte
                    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                            (user_choice == 'rock' and computer_choice == 'lizard') or \
                            (user_choice == 'paper' and computer_choice == 'rock') or \
                            (user_choice == 'paper' and computer_choice == 'spock') or \
                            (user_choice == 'scissors' and computer_choice == 'paper') or \
                            (user_choice == 'scissors' and computer_choice == 'lizard') or \
                            (user_choice == 'lizard' and computer_choice == 'paper') or \
                            (user_choice == 'lizard' and computer_choice == 'spock') or \
                            (user_choice == 'spock' and computer_choice == 'rock') or \
                            (user_choice == 'spock' and computer_choice == 'scissors'):
                        print(f'Du vant! Jeg valgte {computer_choice}')
                        balance = balance + bet*2
                    #hvis ikke du slo pcen slo den deg og du tapte
                    else:
                        print(f'Du tapte! Jeg valgte {computer_choice}')
                        balance = balance

            elif (svar == 'Nei') or (svar == 'nei') or (svar == 'NEI'):
                #Det samme igjen bare uten penger
                # pcen velger et random valg
                computer_choice = random.choice(choices)
                # sier at du må velge mellom valgene
                print('Velg mellom (rock/paper/scissors/lizard/spock)')
                user_choice = input('$: ')

                # sjekker om det du skreiv inn var et av valga
                if user_choice not in choices:
                    print('Ikke gyldigt valg. Velg mellom rock, paper, scissors, lizard eller spock.')

                # hvis det du valge og pcen valgte var det samme blir det uavgjort
                if user_choice == computer_choice:
                    print(f'Det ble uavgjort. Jeg valgte{computer_choice} og. ')
                # sjekker om det du valgte slår det pcen valgte
                elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                        (user_choice == 'rock' and computer_choice == 'lizard') or \
                        (user_choice == 'paper' and computer_choice == 'rock') or \
                        (user_choice == 'paper' and computer_choice == 'spock') or \
                        (user_choice == 'scissors' and computer_choice == 'paper') or \
                        (user_choice == 'scissors' and computer_choice == 'lizard') or \
                        (user_choice == 'lizard' and computer_choice == 'paper') or \
                        (user_choice == 'lizard' and computer_choice == 'spock') or \
                        (user_choice == 'spock' and computer_choice == 'rock') or \
                        (user_choice == 'spock' and computer_choice == 'scissors'):
                    print(f'Du vant! Jeg valgte {computer_choice}')
                # hvis ikke du slo pcen slo den deg og du tapte
                else:
                    print(f'Du tapte! Jeg valgte {computer_choice}')
        #stopper boten
        case 'quit':
             break

        #hvis du skriver inn noe som ikke er i valga over får du meldingen "invalid syntax"
        case _:
            print('invalid syntax')