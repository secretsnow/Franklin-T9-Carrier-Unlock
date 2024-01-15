@echo off
setlocal enabledelayedexpansion

set /p IMEI=Enter your IMEI: 
set "hashInput=%IMEI%simlock"

:: Calculate SHA-1 hash using CertUtil
for /f %%H in ('echo %hashInput% ^| certutil -hashfile -SHA1 -') do set "hashedValue=%%H"

:: Extract the first 8 characters
set "hashedValue=!hashedValue:~0,8!"
echo %hashedValue%

endlocal
