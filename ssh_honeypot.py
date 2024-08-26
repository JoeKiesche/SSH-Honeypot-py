# Libraries
import logging
from logging.handlers import RotatingFileHandler
import socket

#constants

#how we want the messages to be formatted in the log file
logging_format = logging.Formatter('%(message)s')


#loggers and logging files
funnle_logger = logging.getLogger('FunnleLogger')
funnle_logger.setLevel(logging.INFO)

#set the format and where it will be logged to 
funnel_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnle_logger.addHandler(funnel_handler)


#   THIS IS TO MONITOR CMDS -----------------------------------------------
creds_logger = logging.getLogger('FunnleLogger')
creds_logger.setLevel(logging.INFO)

#set the format and where it will be logged to 
creds_handler = RotatingFileHandler('cmd_audits.log', maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(funnel_handler)



#emaulted shell

def emualted_shell(channel, client_ip):
    channel.send(b'corporate-jumpbox2$ ')
    commmand = b""
    while True:
        char = channel.recv(1)
        channel.send(char)
        if not char:
            channel.close()

        command += char

        if char  == b'\r':
            if commmand.strip() == b'exit':
                response = b'\n Goodbye!\n'
                channel.close()

            elif commmand.strip() == b'pwd':
                response = b'\n' + '\\usr\local' + b'\r\n'
            
            elif command.strip() == b'whoami':
                response = b'\n' + b"corpuser1" + b'\r\n'

            elif command.strip() == b'ls':
                response = b'\n' + b"jumpbox.conf" + b'\r\n'  

            elif commmand.strip() == b'cat jumpbox.conf':
                response = b'\n' + b"Helloooooo" + b'\r\n' 

            else:
                response = b'\n' + bytes(command.strip()) + b"\r\n"


        channel.send(response)
        channel.send(b'corporate-jumpbox2$ ')
        commmand = b""


#ssh server + socket

#ptovsion ssh-based honeypoty