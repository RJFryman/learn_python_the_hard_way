# Exercise 27. Memorizing Logic

list = ['and', 'or', 'not', '!=(not equal)', '==(equal)',
        '>=(greater-than-equal)', '<=(less-than-equal)', 'True', 'False']

print "These are the Truth Terms:"
for item in list:
  print "* %s" % item

print "\nNOT      True?"
not_list = {'not False': True, 'not True': False}
for key in not_list:
  print key, not_list[key]

print "\nOR            True?"
or_list = {'True or False': True, 'True or True': True, 'False or True': True,
            'False or False': False}
for key in or_list:
  print key, or_list[key]

print "\nAND            True?"
and_list = {'True and False': False, 'True and True': True,
            'False and True':False, 'False and False': False}
for key in and_list:
  print key, and_list[key]

print "\nNOT OR            True?"
not_or_list = {'not(True or False)': False, 'not(True or True)': False,
               'not(False or True)': False, 'not(False or False)': True}
for key in not_or_list:
  print key, not_or_list[key]

print "\nNOT AND            True?"
not_and_list = {'not(True and False)': True, 'not(True and True)': False,
                'not(False and True)': True, 'not(False and False)': True}
for key in not_and_list:
  print key, not_and_list[key]

print "\n!=     True?"
not_equal_list = {'1 != 0': True, '1 != 1': False, '0 != 1': True,
                  '0 != 0': False}
for key in not_equal_list:
  print key, not_equal_list[key]

print "\n==     True?"
equal_equal_list = {'1 == 0': False, '1 == 1': True, '0 == 1': False,
                    '0 == 0': True}
for key in equal_equal_list:
  print key, equal_equal_list[key]
