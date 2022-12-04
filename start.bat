@echo off
@title ChatMaskDump
call virtualPythonEnvironment\scripts\activate.bat

IF '%errorlevel%' NEQ '0' (
    echo Preparing environment
    py -m venv virtualPythonEnvironment
    call virtualPythonEnvironment\scripts\activate.bat
    call pip install -r requirements.txt -U
)

python fridahook.py