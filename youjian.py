from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(inf):
    if 'email_key' in os.environ:
        try:
            from_addr,email_password,to_addr,smtp_server = os.environ['email_key'].split(',')
            msg = MIMEText(inf, 'plain', 'utf-8')
            msg['From'] = _format_addr('德玛西亚 <%s>' % from_addr)
            msg['To'] = _format_addr('艾欧尼亚 <%s>' % to_addr)
            msg['Subject'] = Header('From Github actions: SHU-selfreport', 'utf-8').encode()

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, email_password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
        except:
            print('email_key is right,but fail to send email')
    else:
        print('email_key is wrong')
