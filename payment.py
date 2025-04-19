print('Hello Dear')
print('Hopefully this payment method seems fair enough!')
print('Please use ONLY numbers for the following questions.')
h = float(input('Please Enter The Hours Wasted This Month!:'))
r = float(input('How much do you charge your boss per hour? :D'))
if h <= 160:
  print('You really care about the Life-Work balance, huh?')
  pay = (h * r)
  print('This is what you get $', pay)
  yn = input('Is it worth it?!')
  print('Oh I forgot to mention. This is your gross payment! Good luck.')
else:
  h > 160
  print('you work so hard!')
  oh = h - 160
  pay = ((160 * r) + oh * r * 1.5)
  print('$', pay)
  yn = input('Is it worth it?!')
  print('Oh I forgot to mention. This is your gross payment! Good luck.')
print('And please do NOT take it personal, you know I love you <3')
