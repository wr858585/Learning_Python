
# Task: Help mother Lisa develop an automatic filter for selecting perspective husband for her daughter, Elsa.
# Selecting criteria are as follows:
#   1. He should be over 180cm in height.
#   2. He should have assets over 10 million dollars.
#   3. He should be good looking as well with over 500 'charming points'.
# As Elsa gets older, she still cannot marry a guy due to such picky and rigid criteria. Eventually, Lisa compromised
# and told Elsa that she could still marry someone who possesses at least one character mentioned above whilst the
# ideal husband have all three.

height = int(input('Height (in cm): '))
wealth = float(input('Assets (in millions): '))
charming_points = int(input('Charming Points: '))

if height >= 180 and wealth >= 10 and charming_points >= 500:
    print('You are the perfect one.')

elif height >= 180 or wealth >= 10 or charming_points >= 500:
    print('You are tolerably accepted.')

else:
    print('Sorry you are out.')
