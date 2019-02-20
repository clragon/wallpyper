import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '--name=%s' % "wallpyper",
    '--onefile',
    '--distpath=./build/dist',
    '--workpath=./build/temp',
    '--noconfirm',
    '--icon=%s' % os.path.join('wallpyper', 'pyper.ico'),
    os.path.join('wallpyper', 'wallpyper.py'),
])