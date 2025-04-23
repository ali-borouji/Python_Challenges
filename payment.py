print('Hello Dear')
print('Hopefully this payment method seems fair enough!')
print('Please use ONLY numbers for the following questions.')
h = input('Please Enter The Hours Wasted This Month!:')
r = input('How much do you charge your boss per hour? :D')
try:
    h = float(h)
    r = float(r)
except:
    h <= 0
    print('Think again! looks like you owe us something!')
print('OK')
if h <= 160:
  print('You really care about the Life-Work balance, huh?')
  pay = (h * r)
  print('This is what you get $', pay)
  yn = input('Is it worth it?!')
  print('Oh I forgot to mention. This is your gross payment!')
else:
  h > 160
  print('you work so hard!')
  oh = h - 160
  pay = ((160 * r) + oh * r * 1.5)
  print('$', pay)
  yn = input('Is it worth it?!')
  print('Oh I forgot to mention. This is your gross payment!')
if int(pay) > 40000:
    taxp = pay - (pay * 0.4)
    print('This is what you really get $', taxp)
else:
    taxp = pay - (pay * 0.3)
    print('This is what you really get $', taxp)
