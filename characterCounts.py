import string

sentence = input("Enter a sentence:")
length = len(sentence)
upper_total = len(''.join([u for u in sentence if u.isupper()]))
lower_total = len(''.join([l for l in sentence if l.islower()]))
digits_total = len(''.join([d for d in sentence if d.isdigit()]))
is_space = len(''.join([s for s in sentence if s.isspace()]))
p_total = length - digits_total - upper_total - lower_total - is_space

print( '{:>{width}s}'.format("Upper case",width=15), '{:>{width}d}'.format(upper_total,width=5) ) 
print( '{:>{width}s}'.format("Lower case",width=15), '{:>{width}d}'.format(lower_total,width=5) ) 
print( '{:>{width}s}'.format("Digits",width=15), '{:>{width}d}'.format(digits_total,width=5) ) 
print( '{:>{width}s}'.format("Punctuation",width=15), '{:>{width}d}'.format(p_total,width=5) )




