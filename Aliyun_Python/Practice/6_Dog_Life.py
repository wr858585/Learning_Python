# Background information: a dog's life can be calculated in a way which is equivalent to human's.
# Formula: dog's life = 10.5 * the first two years + 4 * the following years
# Question: Convert dog's life when user enters the number

life = int(input('Please enter your dog\'s life: '))

if life < 0:
    print('Please enter a valid number.')

elif life <= 2:
    print('Your dog\'s life is equivalent to %f years' % (2 * life))

else:
    print('Your dog\'s life is equivalent to %f years' % (2 * 10.5 + 4 * (life - 2)))
