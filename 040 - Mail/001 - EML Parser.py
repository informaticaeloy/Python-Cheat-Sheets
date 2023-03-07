### Based on NAMECHEAP repository
### https://github.com/namecheap/fast_mail_parser

import sys
import colors
from fast_mail_parser import parse_email, ParseError

with open('easy_mail.eml', 'r') as f:
    message_payload = f.read()

try:
    email = parse_email(message_payload)
except ParseError as e:
    print("Failed to parse email: ", e)
    sys.exit(1)

print(colors.bcolors.OKBLUE + 'SUBJECT: \t' + colors.bcolors.ENDC, end='')
print(email.subject)

print(colors.bcolors.OKBLUE + 'DATE: \t' + colors.bcolors.ENDC, end='')
print(email.date)

print(colors.bcolors.OKGREEN + '\tHEADER -> MIME-Version: \t' + colors.bcolors.ENDC, end='')
print(email.headers['MIME-Version'])

print(colors.bcolors.OKGREEN + '\tHEADER -> Date: \t' + colors.bcolors.ENDC, end='')
print(email.headers['Date'])

print(colors.bcolors.OKGREEN + '\tHEADER -> Message-ID: \t' + colors.bcolors.ENDC, end='')
print(email.headers['Message-ID'])

print(colors.bcolors.OKGREEN + '\tHEADER -> Subject: \t' + colors.bcolors.ENDC, end='')
print(email.headers['Subject'])

print(colors.bcolors.OKGREEN + '\tHEADER -> From: \t' + colors.bcolors.ENDC, end='')
print(email.headers['From'])

print(colors.bcolors.OKGREEN + '\tHEADER -> Content-Type: \t' + colors.bcolors.ENDC, end='')
print(email.headers['Content-Type'])

print(colors.bcolors.OKGREEN + '\tHEADER -> To: \t' + colors.bcolors.ENDC, end='')
print(email.headers['To'])


print(colors.bcolors.FAIL + "HEADERS" + colors.bcolors.ENDC)
print(colors.bcolors.FAIL + "-------" + colors.bcolors.ENDC)
print(email.headers)

print(colors.bcolors.FAIL + "EMAIL.TEXT_PLAIN" + colors.bcolors.ENDC)
print(colors.bcolors.FAIL + "----------------" + colors.bcolors.ENDC)
print(email.text_plain)

print(colors.bcolors.FAIL + "EMAIL.TEXT_HTML" + colors.bcolors.ENDC)
print(colors.bcolors.FAIL + "---------------" + colors.bcolors.ENDC)
print(email.text_html)

print(colors.bcolors.FAIL + "ATTACHMENTS" + colors.bcolors.ENDC)
print(colors.bcolors.FAIL + "----------->>>>" + colors.bcolors.ENDC)

i = 0
for attachment in email.attachments:
    print(colors.bcolors.WARNING + "\tATTACHMENT Nº" + str(i) + colors.bcolors.ENDC)
    i += 1
    print("\t",end='')
    print(attachment.mimetype)
    print("\t",end='')
    print(attachment.content)
    print("\t",end='')
    print(attachment.filename)
