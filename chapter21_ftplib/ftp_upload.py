import ftplib

def ftp_upload(ftp_obj, path, ftype='TXT'):
    """
    A function for uploading files to an FTP server
    @param ftp_obj: The file transfer protocol object
    @param path: The path to the file to upload
    """
    if ftype == 'TXT':
        with open(path) as fobj:
            ftp.storlines('STOR ' + path, fobj)
    else:
        with open(path, 'rb') as fobj:
            ftp.storbinary('STOR ' + path, fobj, 1024)

if __name__ == '__main__':
    ftp = ftplib.FTP('host', 'username', 'password')
    ftp.login()

    path = '/path/to/something.txt'
    ftp_upload(ftp, path)

    pdf_path = '/path/to/something.pdf'
    ftp_upload(ftp, pdf_path, ftype='PDF')

    ftp.quit()