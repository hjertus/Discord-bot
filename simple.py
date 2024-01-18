import random

kommandoer = {
    "?joke": "Jeg forteller en dårlig dad-joke.",
    '?balance': 'Sjekke hvor mye du har i banken.',
    '?gamble' : 'Gamble penger.',
    "quit": "Avslutt samtale."
}

balance = 100

print('Skriv ?hjelp for å komme i gang.')

#start robot
while True:
    match input('$: '):
        case '?hjelp':
            print('Jeg kan følgende kommandoer.')
            for kommando in kommandoer:
                print(f'{kommando} - {kommandoer[kommando]}')
        case '?balance':

            print(f'Du har {balance} på konto.')
        #Hidden command
        case ('?apekatt'):
            money = input('Hvor mye vil du ha? ')
            balance = balance + int(money)
        case ('?gamble'):
            money = input('Hvor mye vil du gamble? ')
            if random.randint(0, 2) == 1:
                print('Du vant')
                balance = balance + int(money)
                print(f'Du har nå {balance} på konto.')
            else:
                print('Du tapte')
                balance = balance - int(money)
                print(f'Du har nå {balance} på konto.')


        # stopper boten
        case  'quit':
            break

        # hvis du skriver inn noe som ikke er i valga over får du meldingen "invalid syntax"
        case _:
            print('invalid syntax')
