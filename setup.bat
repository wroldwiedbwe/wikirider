@echo off

::check for python installation
call python --version>NUL || (goto noPythonInstalled)
pip --version>NUL || (goto noPipInstalled)

::Install virtual env, set up environment, install requirements
(
pip install virtualenv

virtualenv .env


cd .env/Scripts/
call activate.bat

pip install -r ../../requirements.txt
call deactivate
) || (goto installFailed)
cd ../..
echo.
echo|set /p=" Install Successful! To run wikirider, do 'call .env/Scripts/activate.bat & python wikirun.py <starting url> <depth>'"

goto:eof

::errors
:noPythonInstalled
echo.
echo Error: No python installation found under python command
goto:eof

:noPipInstalled
echo.
echo Error: No pip installation found under pip command
goto:eof

:installFailed
echo.
echo Error: install failed. Look uo to see what went wrong.
goto:eof