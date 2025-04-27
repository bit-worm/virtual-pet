from pet import Pet

print('Welcome...\n')
name = input('How would you like toname your pet: ')

pet = Pet(name)

print(f"Conratulations, you now own {name}\n")

choice = ' '

print(f'------------{pet.name}------------')
pet.get_status()

while choice != 'x':
    print('\nFeed(f) __ Sleep(s) __ Play(p) __ Info(i) __ Train(t) __ Tricks(j) __ Exit(x)')
    choice = input('->> ')

    if choice == 'f':
        pet.eat()
    elif choice == 's':
        pet.sleep()
    elif choice == 'p':
        pet.play()
    elif choice == 'i':
        pet.get_status()
    elif choice == 't':
        trick = input(f"What would you like to teach {pet.name}: ")
        pet.train(trick)
    elif choice == 'j':
        pet.show_tricks()
    elif choice == 'x':
        print(f"{pet.name} says goodbye...")
