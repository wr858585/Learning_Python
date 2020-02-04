"""
Placeholders are % signs followed by specific characters or marks that are replaced by corresponding contents later.

Some useful examples:
%s will be replaced by string
%d will be replaced by integer
%f will be replaced by float

Replacing starts after the second %
"""

a = int(input('a='))
b = int(input('b='))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# When run, there would be an issue on line 17 as the result is a float but the placeholder claims it is an integer.
# Solution: use %f instead on the right hand side of the equation

"""
Another hint: line 19 uses double dollar signs because system expects something follows the single % sign as 
placeholder. To simply display %, we need to tell system that the dollar sign here is not a placeholder. Rather, 
it means to display one. 
"""