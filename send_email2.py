# Sending mail using GMAIL

import yagmail
yag = yagmail.SMTP( "syed.atique@gmail.com" )

contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send("syed.atique@gmail.com", 'subject', contents)

yagmail.SMTP.quit()