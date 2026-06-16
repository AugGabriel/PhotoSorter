import os
import re
import shutil
import datetime
import time

# Verificação de tamanho

PATH = r"C:\Users\gabri_06sjdhx\OneDrive\Imagens\Neural"
DIRS = os.scandir(PATH)

def main():
    try:
        open(PATH)
    except PermissionError as e:
        pass
    except Exception as e:
        print(e.args[1])
        return
    
    for d in range(datetime.datetime.now().year, older(DIRS) - 1, -1):
        print(d)


def older(dirs):
    minimum = min([get_archv_date(archive).year for archive in dirs])
    return minimum

    
def get_archv_date(archive: os.DirEntry):
    # Gets the creation date according to the operational system (which may not be the real one),
    # and tries to get the date in the name of the archive, which is usually the correct one

    t1 = time.localtime(os.path.getctime(archive))
    d1 = datetime.date(year=t1.tm_year, month=t1.tm_mon, day=t1.tm_mday)
    
    d2 = date_by_name(archive)

    return min(d1, d2) if d2 else d1


def date_by_name(archive):
    match = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', archive.name)
    if (match):
        m = (match.string)[0:10]
        d = datetime.date(year=int(m[0:4]), month=int(m[5:7]), day=int(m[8:10]))
        return d
    
    return






























def old():
    # for archive in DIRS:
        # print(archive)
        # date_format = r'[0-9]{4}\-[0-9]{2}\-[0-9]{2}'

        # print(archive, end='\t')
        # if re.match(date_format, archive.name):
        #     print(archive, end='\t')
        #     # year = re.findall(date_format, archive.name)[0][:4]
        #     # print(year)

        #     # try:
        #     #     os.mkdir(PATH + year)
        #     # except FileExistsError:
        #     #     pass
        #     # finally:
        #     #     shutil.copy2(PATH + archive.name, PATH + f'{year}')

        print()

if __name__ == '__main__':
    main()