from django import template

register = template.Library()

def get_target_user(obj, user):
    return obj.get_target_user(user)

def get_target_image(obj, user):
    user = get_target_user(obj, user)
    return user.profile_image.url

def get_last_message(obj):
    last = obj.messages.all().last()
    if last:
        return last.content
    else:
        return "start Conversation !"

register.filter('target_user', get_target_user)
register.filter('target_image', get_target_image)
register.filter('last_message', get_last_message)