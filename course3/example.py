try:
    print(1 / 0)
except ZeroDivisionError as some_var:
    import traceback
    print(traceback.format_exc())

print('After')
