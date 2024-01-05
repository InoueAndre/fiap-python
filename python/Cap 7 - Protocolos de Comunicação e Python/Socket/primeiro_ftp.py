from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.cwd('pub')

ftp.quit()