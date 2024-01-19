import random

dadjokes = [
    "Hvorfor kunne ikke sykkelen holde seg oppreist selv? - Fordi den var to-tung.",
    "Hva sa den ene veggen til den andre veggen? - 'Jeg støtter deg.'",
    "Hva kalles en fiskegruppe som spiller musikk? - En orkester.",
    "Hvorfor tok sjøstjernen med seg et kompass til skolen? - Fordi den ville bli bedre på stjernefag.",
    "Hvordan får du en nese til å smile? - Kjøp den en genser.",
    "Hva gjorde den ene blyanten til den andre blyanten på skolen? - 'Du skriver meg feil.'",
    "Hvorfor kan ikke du gi Elsa en ballong? - Fordi hun vil la den gå.",
    "Hva sa det ene eplet til det andre eplet? - 'Slutt å dytt meg!'",
    "Hvorfor tok ikke solen noen venner med seg til festen? - Fordi den allerede hadde nok stråler.",
    "Hva kalles en haug med katter? - En miauskete."
  ]

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
        case ('?dadjoke'):
            print(random.choice(dadjokes))
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

        # Hidden commando
        case('?apekatt'):
            money = input('Hvor mye vil du ha? ')
            balance = balance + int(money)


        # stopper boten
        case  'quit':
            break

        # hvis du skriver inn noe som ikke er i valga over får du meldingen "invalid syntax"
        case _:
            print('invalid syntax')
