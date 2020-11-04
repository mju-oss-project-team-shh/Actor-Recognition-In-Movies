@echo off

echo *****************************************************
echo *****************************************************
echo ***             Installer for Windows             ***
echo *****************************************************
echo *****************************************************
echo. 
echo =====================================================
echo *****                  WARNING                  *****
echo =====================================================
echo * Python 3.8 or higher version must be installed
echo * If your Python version is lower than 3.8, do not run this script
:WrongInputError
echo. 
echo [1] My Python version is 3.8 or higher than 3.8
echo [2] My Python version is lower than 3.8
set /p isPythonInstalled="Enter a #: "
set isWrongInput=false
if "%isPythonInstalled%" == "" set isWrongInput=true
if not "%isPythonInstalled%" == "1" (
  if not "%isPythonInstalled%" == "2" (
    set isWrongInput=true
  )
)
if "%isWrongInput%" == "true"  (
  echo [ERROR] Please enter 1 or 2
  goto WrongInputError
)
if "%isPythonInstalled%" == "1" (
  echo.
  echo =====================================================
  echo *****      Install packages in virtualenv       *****
  echo =====================================================
  pip install virtualenv
  virtualenv venv-windows
  venv-windows\Scripts\activate
  pip install cmake numpy==1.19.3
  pip install dlib pyqt5
  pip install imutils jupyter scipy pandas opencv-python face-recognition sklearn numpy progressbar
  deactivate
  echo.
  echo "DONE. Run venv-windows\Scripts\activate to activate virtualenv."
  echo.
)
if "%isPythonInstalled%" == "2" (
  echo.
  echo Install Python 3.8 or higher version and then run this script
  echo You can download Python 3.8 executable installer at following links:
  echo For 32bit: https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe
  echo For 64bit: https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe
  echo.
)

