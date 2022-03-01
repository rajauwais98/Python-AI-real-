import pyperclip
import re

emailRegex = re.compile(r'''(
([a-zA-Z0–9_\-\.]) +
@tm.com.my
)''', re.VERBOSE)
#emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

text = str(pyperclip.paste())
matches = []
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to Clipboard:')
    print('\n'.join(matches))
else:
    print('no emails found')