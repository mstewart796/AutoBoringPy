import smtplib

"""How to send emails"""

# Call server
conn = smtplib.SMTP('smtp.gmail.com', 587)
# Begin connection
conn.ehlo()
# Begin encryption
conn.starttls()
# Login
conn.login('YOUREMAIL@gmail.com', 'YOUR_PASSWORD')
# Send emails through the sendmail function
conn.sendmail('FROM_ADDRESS', 'TO_ADDRESS', 'Subject: EXAMPLE SUBJECT... \n\n'
                                            'SOME EXAMPLE TEXT\n\n NAME')

# Disconnect from server
conn.quit()
