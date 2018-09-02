import csv
import ldap
import string
import random
import smtplib
import argparse
from ldap3 import Server, Connection, ALL, core

securedigits = ('@#$&*')

def password_generator(size=12, chars=string.ascii_letters + string.digits+securedigits):
    return ''.join(random.choice(chars) for i in range(size))

print password_generator()

#def ldapimport():
ldapnome=
ldapsobrenome =
ldaplogin=
ldapmail=     
    


def csvreader(ldapnome, ldapsobrenome, ldaplogin, ldapmail):
    with open('insertdata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        uid = 48059
        for row in readCSV:
            ldapnome = str(row[0])
            ldapsobrenome = str(row[1])
            ldaplogin = str(row[2])
            ldapmail = str(row[3])
            uid = uid + 1
            return ldapnome, ldapsobrenome, ldaplogin, ldapmail
        ldapimport()

print csvreader(ldapnome, ldapsobrenome, ldaplogin, ldapmail)

def sendmail(maildest, mailsubject, mailmsg ): 
    sender  = 'pytestcoding@gmail.com'
    senderpass  = 'pypypy666'
    to = maildest
    subject = mailsubject
    msg = mailmsg

    msg = '\r\n'.join([
    'From: %s' % to,
    'To: %s' % subject,
    'Subject: %s' % msg,
    '',
    '%s' % msg
    ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender,senderpass)
    server.sendmail(to, subject, msg)
    server.quit()

msg = 'seu login e: ',ldaplogin , 'e sua senha e : ', password_generator()
print msg
sendmail('fernando.wfvm@gmail.com', 'teste', msg)

 

print "All Done"