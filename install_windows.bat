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
echo * You must run this script using cmd.exe
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
  echo This script can automatically download Python 3.8 installer for Windows 10 PC.
  echo Do you prefer to download and run the installer?
  echo (Install manually if your Windows version is lower than 10)
  :WrongInputError2
  echo.
  echo [1] Download and run Python 3.8 installer.
  echo [2] Do not download. I will install it manually by myself.
  set /p isDownloadInstaller="Enter a #: "
  set isWrongInput2=false
  if "%isDownloadInstaller%" == "" set isWrongInput2=true
  if not "%isDownloadInstaller%" == "1" (
    if not "%isDownloadInstaller%" == "2" (
      set isWrongInput2=true
    )
  )
  if "%isWrongInput2%" == "true" (
    echo [ERROR] Please enter 1 or 2
    goto WrongInputError2
  )

  set installerURLamd64=https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe
  set installerURLx86=https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe

  if "%isDownloadInstaller%" == "1" (
    set isAMD64=false
    for /f "tokens=1,2 delims==" %%a in ('set pro') do (
      if "%%a" == "PROCESSOR_ARCHITECTURE" (
        if "%%b" == "AMD64" (
          set isAMD64=true
        )
      )
    )
    for /f %%v in ('powershell -c "[guid]::NewGuid().ToString().ToUpper()"') do set NEWGUID=%%v
    set installerEXE=__temp_python3.8_installer_%NEWGUID%__.exe
    if "%isAMD64%" == "true" (
      curl -o %installerEXE% %installerURLamd64%
    ) else (
      curl -o %installerEXE% %installerURLx86%
    )
    start /wait %installerEXE%
    del %installerEXE%
    echo.
    echo Now run this script again to install packages or re-install Python 3.8
    echo.
  )
  if "%isDownloadInstaller%" == "2" (
    echo.
    echo Install Python 3.8 or higher version and then run this script again.
    echo.
    echo You can download Python 3.8 executable installer at following links:
    echo For 32bit: %installerURLx86%
    echo For 64bit: %installerURLamd64%
    echo.
  )
)

