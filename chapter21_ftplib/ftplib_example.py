import ftplib
import os

ftp = ftplib.FTP('ftp.debian.org')
ftp.login()
ftp.cwd('debian')
filenames = ftp.nlst()

for filename in filenames:
    host_file = os.path.join(
        '/home/mike/Desktop/ftp_test', filename)
    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
    except ftplib.error_perm:
        pass

ftp.quit()