import sys
from cx_Freeze import setup, Executable


# ----------------------------------------------------------------
# 基本情報
# ----------------------------------------------------------------
name = "Show-Gip"
version = "0.1"
description = "自分のグローバルIPを簡単に確認することができます"
author = "Nanosize"
license= 'MIT'
url = "https://netchira.github.io/"
icon = "icons/gip_icon.ico"

# アプリケーションの種別を選択
if sys.platform == "win32":
    base = "Win32GUI"

# UUIDは一度決めたら変更しない
upgrade_code = "{a2b30d2a-0e91-11ef-9e21-242fd016a5e8}"

# ----------------------------------------------------------------
# セットアップ処理
# ----------------------------------------------------------------
shortcut_table = [
    ('DesktopShortcut',          # Shortcut
     'DesktopFolder',            # Directory_
     "CompareTxt",               # Name
     'TARGETDIR',                # Component_
     '[TARGETDIR]CompareTxt.exe',# Target
     'license',                  # license
     None,                       # Description
     None,                       # Hotkey
     None,                       # Icon
     None,                       # IconIndex
     None,                       # ShowCmd
     'TARGETDIR',                # WkDir
    )
    ]

# Table dictionary
msi_data = {'Shortcut': shortcut_table}

# 追加モジュールで必要なものを packages に入れる
build_exe_options = {'packages': ['requests'],
                     'excludes': [],
                     'includes': [],
                     'include_files': ["icons/"]
}

bdist_msi_options = {'upgrade_code': upgrade_code,
                     'add_to_path': False,
                     'data': msi_data
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}


# セットアップ処理
setup(name=name,
      version=version,
      author=author,
      url=url,
      description=description,
      options=options,
      executables=[Executable(script="main.py",icon=icon)]
      )