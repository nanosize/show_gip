import sys
from cx_Freeze import setup, Executable
 
base = None
 
if sys.platform == 'win32': base = 'Win32GUI'

# exeにするソースファイルを指定
exe = Executable(script = "show-gip.py", base= base)

additional_modules = ['requests']

setup(name = 'show-gip', #ファイルの名前
    version = '0.1',     #バージョン表記
    description = 'グローバルIPを表示する', #アプリケーションの説明
    executables = [exe])  #実行ファイルの形式