# -*- coding: utf-8 -*-

# print(1 / 0)  # this will raise an exception

# Basic try/except

try:
    print(1 / 0)
except:
    print('0!!')

try:
    print(1 / 0)
except Exception:  # it is almost the same as just `except:`
    print('0!!')






# Catching specific exceptions

try:
    print(1 / 0)
except ValueError:
    print('Exception!')







# Catching exception instance

try:
    print(1 / 0)
except ZeroDivisionError as some_var:
    print('Exception! Stop it!')
    some_var1 = some_var

print(some_var1)











# custom traceback print
try:
    print(1 / 0)
except ZeroDivisionError as some_var:
    import traceback
    print(traceback.format_exc())
    # import sys
    # print(sys.exc_info())







# Mismatched exception will not be captured

try:
    d = {'key': 23}
    print(d['does not exist'])
except ZeroDivisionError:
    print("This won't be called")














try:
    d = {'key': 23}
    print(d['does not exist'])
except KeyError as e:
    print("Got it", e)

# Raising exception

try:
    # .....
    raise ValueError('Custom message')
except ValueError as e:
    print('Message is', e)


# class CustomError(Exception):
#     pass
# Multiple except blocks

try:
    raise ZeroDivisionError()
except ZeroDivisionError:
    print('Divided by zero!')
except AttributeError:
    print('Key is missing!')
except Exception as ex:
    print("I don't know what's going on!")
    print(ex)
# try/except/else

try:
    print('Fine')
except KeyError:
    print('Nope.')
else:
    print('Else clause')

# try/except/finally

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0!')
finally:
    print('I will be called in the end!')



# All together





try:
    print('try')
except ValueError:
    pass  # You should never pass on exceptions!
else:
    print('else')
finally:
    print('finally')

try:
    raise ValueError()
finally:
    print('Finally!')



di = {'Please, input what is the name of the first President of Russia?': ('Boris','Elcin','Boris Elcin'),
      'Please, input how many 5 * 5?': ('25','twenty five','TWENTY FIVE'),
      'Please, input what is the main street in Moscow?': ('Tverskaia','Tverskaya','TVERSKAIA'),
      }



