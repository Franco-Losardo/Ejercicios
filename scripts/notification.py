# import os
#
# def notify(title, text, sound):
#     os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format(text, title, sound))
#
# notify("Hola!!", "Heres an alert", "default")


import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


# Calling the function
notify(title    = 'A Real Notification',
       subtitle = 'with python',
       message  = 'Hello, this is me, notifying you!!')
