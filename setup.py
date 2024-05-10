from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['requests'], 'excludes': []}

base = 'gui'

executables = [
    Executable('main.py', base=base, target_name = 'Show-Gip',icon= 'icons/gip_icon.ico')
]

setup(name='Show-Gip',
      version = '1.0',
      description = 'Show your global IP address.',
      options = {'build_exe': build_options},
      executables = executables)