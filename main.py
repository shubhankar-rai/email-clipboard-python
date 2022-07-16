import re, pyperclip

# Create Regex for Email
emailRegex = re.compile(r'''
[a-zA-Z0-9._+]+    #name part
@                  #@ symbol
[a-zA-Z0-9._+]+    #domain part
''', re.VERBOSE)

# Get Text From Clipboard
text = pyperclip.paste()

# Extract Email From Clipboard
extractedEmail = emailRegex.findall(text)

# Copy Extracted Emails To Clipboard
result = "\n".join(extractedEmail)
pyperclip.copy(result)