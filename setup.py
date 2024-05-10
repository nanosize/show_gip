from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    #'excludes': ['requests']
}

setup(
    name="Show-Gip",
    version="0.1",
      description = 'Show your global IP address.',
    options={"build_exe": build_exe_options},
    executables=[Executable("ShowGip.py", base="gui")]
)