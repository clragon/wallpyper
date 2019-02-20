from win32com.shell import shell, shellcon
from collections import Counter
from shutil import copyfile
import multiprocessing
import argparse
import datetime
import hashlib
import imghdr
import json
import os


INPUT_DIR = os.environ['localappdata'] + "/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
SETTINGS_FILE = "pyper_conf.json"
LOG_FILE = "pyper.log"
NAME = "Spotlight"


def main():

    parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
    parser.add_argument('-c', '--clean', action='store_true', help="deletes duplicate, blacklisted and invalid files in the output directory and renames files")
    parser.add_argument('-t', '--target', dest='directory', help="set the directory to where the wallpapers get extracted to.")
    parser.add_argument('-b', '--blacklist', dest='file', help="add a file to the backlist")

    arg = parser.parse_args()
    if (arg.clean):

        clean()
    
    if (arg.directory):

        if (arg.directory is not None):

            set_output_dir(arg.directory)
            os.sys.exit()
        
        else:
            print("[{}] [Error] Directory does not exist: \"{}\"".format(datetime.datetime.now(), arg.directory))

    if (arg.file):

        if (arg.file is not None):
            
            add_to_blacklist(arg.file)
            os.sys.exit()
        
        else:
            print("[{}] [Error] File does not exist: \"{}\"".format(datetime.datetime.now(), arg.file))
    
    run()



def get_files(directory):
    for _, _, files in os.walk(directory):
        file_strings = files
    files = dict()
    for string in file_strings:
        hasher = hashlib.md5()
        hasher.update(open(os.path.join(directory, string), 'rb').read())
        files[string] = hasher.hexdigest()
    return files


def load_settings(file):
    # check if the file is existing
    if (os.path.isfile(file)):
        try:
            # and if so try to load it
            sets = settings()
            sets.__dict__ = settings.load(file)
        except:
            # if the file isnt able to be parsed, default.
            sets = settings()
    else:
        sets = settings()
    return sets

def clean_output(directory):

    delete = 0
    clean = get_files(directory)
    md5_counts = Counter(clean.values())
    for md5, count in md5_counts.items():
        if count > 1:
            keep_first = False
            for string, md5_2 in clean.items():
                if md5_2 == md5:
                    if (keep_first == True):
                        os.remove(os.path.join(directory, string))
                        delete += 1
                    else:
                        keep_first = True
    print("[{}] deleted {} duplicates".format(datetime.datetime.now(), delete))

    blacklist = 0
    clean = get_files(directory)
    for string, md5 in clean.items():
        if md5 in SETS.blacklist:
            os.remove(os.path.join(directory, string))
            blacklist += 1
    print("[{}] deleted {} blacklisted files".format(datetime.datetime.now(), blacklist))

    invalid = 0
    clean = get_files(directory)
    for string, md5 in clean.items():
        if (imghdr.what((os.path.join(directory, string))) == None):
            os.remove(os.path.join(directory, string))
            invalid += 1
    print("[{}] deleted {} invalid files".format(datetime.datetime.now(), invalid))

    for index, string in enumerate(get_files(directory)):
        # os.path.splitext(directory + string)[1])
        os.rename(os.path.join(directory, string), os.path.join(directory, "{} ({}){}".format("Temp", index + 1, ".png")))
    
    for index, string in enumerate(get_files(directory)):
        os.rename(os.path.join(directory, string), os.path.join(directory, "{} ({}){}".format(NAME, index + 1, os.path.splitext(directory + string)[1])))


def run():

    global SETS
    SETS = load_settings(SETTINGS_FILE)

    os.sys.stdout = open(LOG_FILE, 'a')

    os.makedirs(SETS.output_dir, exist_ok=True)
    
    papers = get_files(INPUT_DIR)
    walls = get_files(SETS.output_dir)

    transfer = dict()
    for string, md5 in papers.items():
        if md5 not in walls.values():
            if md5 not in SETS.blacklist:
                if (os.stat(os.path.join(INPUT_DIR, string)).st_size > 190000):
                    transfer[string] = md5

    index = len(walls)
    for string, md5 in transfer.items():
        index += 1
        copyfile(os.path.join(INPUT_DIR, string), os.path.join(SETS.output_dir, '{} ({}){}'.format(NAME, index, ".png")))
    print("[{}] fetched {} wallpapers".format(datetime.datetime.now(), len(transfer)))


def clean():

    SETS = load_settings(SETTINGS_FILE)

    os.sys.stdout = open(LOG_FILE, 'a')
    
    clean_output(SETS.output_dir)

def set_output_dir(directory):

    SETS = load_settings(SETTINGS_FILE)

    if (os.path.isdir(directory)):
        SETS.output_dir = directory
        SETS.save(SETTINGS_FILE)

def add_to_blacklist(file):

    SETS = load_settings(SETTINGS_FILE)

    if (os.path.isfile(arg.file)):
        hasher = hashlib.md5()
        hasher.update(open(arg.file, 'rb').read())
        SETS.blacklist.append(hasher.hexdigest())
        SETS.save(SETTINGS_FILE)


class settings:

    def __init__(self):
        self.blacklist = []
        self.output_dir = os.path.join(shell.SHGetFolderPath(0, shellcon.CSIDL_MYPICTURES, 0, 0), "Spotlight")

    def save(self, file):
        json.dump(self.__dict__, open(file, 'w'), indent=4)
    
    @staticmethod
    def load(file):
        return json.load(open(file, 'r'))

    output_dir = ""

    blacklist = list()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()