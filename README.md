# wallpyper

Wallpyper is a python script that aims towards extracting the bing spotlight pictures on windows 10.

Every day.

To do this, it is armed with configuration files, logs and blacklists.

Upon running it, it will compare new pictures with current ones and only copy the ones that are missing.
It is fine-tuned to have a threshold for file size so cached ad thumbnails are filtered.

## Configuration
Configuring wallpyper is done through the command line or direct editing of the `pyper_conf.json` file, 
which is in the same directory as the script itself.

By default, all extracted pictures are to be found in the Pictures directory of the user, in a folder called `Spotlight`

### Syntax

The syntax for commandline usage is the following:
```
usage: wallpyper.exe [-h] [-c] [-t DIRECTORY] [-b FILE]

Flip a switch by setting a flag

optional arguments:
  -h, --help                              show this help message and exit
  -t DIRECTORY, --target DIRECTORY        set the directory to where the wallpapers get extracted to.
  -b FILE, --blacklist FILE               add a file to the backlist
  -c, --clean                             deletes duplicate, blacklisted and invalid files in the output directory and renames files
```
### Blacklist

I provide a premade blacklist to filter known ad thumbnails. It can be pasted directly into the configuration file.
```
"82727b41ac0fd92db411cbf08a4da37c",
"760ac5d4780e4cd4c747eabd1f986ab7",
"f4fc747e9e360de8ec5ec11c96536675",
"4b3abf5c64a50ae41da09f5aafbe68a4",
"24b4ea55f27a187892d39d4b8faf8725",
"d3610c50453ad4065493b40a995a757a",
"3dff2e9113007d23e84870b20a5ae8fd",
"1e273d97c8f548d764d1e0faafea2d46",
"99fa40c982082f56c322a6700eab3753",
"feb0b0575c6083800ddb68958825356e",
"23109eb71dfc7e0a6b11f92d6de228d1",
```
### Autorun

Wallpyper will not run by itself; You will have to link it in the autostart or make an entry in the task scheduler.

## Installation
Compiled binary-versions of the script are provided on the releases page.

If you want to compile it for yourself, run 
```
pip -r requirements.txt
``` 
in the root directory of the project to install the dependencies and after that compile it with
```
python make.py
```

