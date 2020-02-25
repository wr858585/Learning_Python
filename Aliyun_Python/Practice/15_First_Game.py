
# Question: Create a game where player can play as hero fighting against Hybrid.

print('Choose your side:')
print('1. Order')
print('2. Chaos')
choice = input('I pick: ')
print()

if choice == '1':
    print('You have chosen Hero. HP = 2 Attack = 2')
elif choice == '2':
    print('Nah you are not playing Hybrid. You are human! HP = 2 Attack = 2')
else:
    print('You missed your choice and was allocated Hero. HP = 2 Attack = 2')
print('-' * 100)

hero_HP = 2
hero_Attack = 2
boss_HP = 50
boss_Attack = 50

narrative = str('''What is your plan?
1. Training
2. Fight
3. Escape
''')
flag = True

while flag:
    print(narrative)
    routine = input('I choose:')
    if routine == '1':
        # Infinite loop is needed here.
        hero_HP += 2
        hero_Attack += 5
        print('-' * 100)
        print(f'You are stronger now. HP = {hero_HP} Attack = {hero_Attack}')
        print('-' * 100)
    elif routine == '2':
        flag = False
        while hero_HP > 0:
            boss_HP -= hero_Attack
            while boss_HP > 0:
                hero_HP -= boss_Attack
                break
            else:
                print('You have defeated the boss. Congratulations you saved your world!')
                break
        else:
            print('You are defeated. Game over.')
    elif routine == '3':
        flag = False
        print('You quit. Game over.')
    else:
        print('Please enter a valid number.')

# Tip: Next time simply write 'While True:' on line 30 with 'break' on line 54 to exit. An equivalent universal\
# approach.
