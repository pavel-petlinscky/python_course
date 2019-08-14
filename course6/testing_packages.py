# -*- coding: utf-8 -*-



#from normal_package import MyClass

from normal_package.normal_file import \
    MyClass, my_function, GLOBAL_VAR, special_function


#from normal_package.__main__ import special_function as m_special_function
#from normal_package import __main__


my_function()
#my_special_function()


print("__name__ in testing_package.py", __name__)

try:
    from not_a_package.my_module import print_info

    # why does it happen:
    # http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
    print_info()
except ImportError as e:
    print(e)



