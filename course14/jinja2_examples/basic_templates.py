# -*- coding: utf-8 -*-

from jinja2 import Template


def simple_hello_world():
    t = Template('Hello {{ something }}!')
    result = t.render(something='World')
    k = 'New'
    result_new = t.render(something=k)

    print(result, result_new)


def for_example(iterable=None):
    """ 'for' loop inside template
    """
    if iterable is None:
        iterable = range(1, 11)

    template_var = """
My favorite numbers:{% for n in my_list %} 
{{ n }}{% endfor %}
"""
    t = Template(template_var)

    result = t.render(my_list=iterable)
    print(result)


def if_example(value):
    """ 'if' condition inside template (condition can be with boolen operators)
    """
    t = Template("""
{% if value %}
True!
{% else %}
False.
{% endif %}
"""
    )

    result = t.render(value=value)
    print(result)


def f(foo = None):
    foo('1323')




f(foo=print)

if __name__ == '__main__':
    #simple_hello_world()
    #for_example()
    #
    #if_example(True)
    if_example('')
