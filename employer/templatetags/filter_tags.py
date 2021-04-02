from django import template

register = template.Library()

@register.filter(name='in_user_category')
def in_user_category(objects, category):
    return objects.filter(user=category)

# как вариант регистрации без декоратора
# register.filter('in_user_category', in_user_category)

@register.filter(name='in_company_category')
def in_company_category(objects, category):
    return objects.filter(company=category)