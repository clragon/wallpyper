:: ______________________________________________________________________________________________________________
:: 														
:: 	DISCLAIMER: I NOT do own this Disclaimer, it is orginally written by someone else			
:: 	DISCLAIMER: I NOT am responsible for any physical or emotional harm you get by reading this source code	
:: 	DISCLAIMER: I NOT will be responsible for any damage this code caused to anything			
:: 	DISCLAIMER: I NOT do even know if it will work how it it is intended/supposed				
:: ______________________________________________________________________________________________________________


@echo off
mode con cols=80 lines=25
setlocal enabledelayedexpansion enableextensions

set title=SpotLightXtract
set version=sfx_auto_fn 0.2
title %title% %version%


set "wrk=0"
set "nam=0"
set "num=0"
set "max=0"
set "paper=%appdata%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
set "wall=undefined"
if not exist "%paper%" ( goto swrong )
if "%wall%"=="undefined" cls & echo wall path not defined, please change settings. & pause>nul & exit
if not exist "%wall%" ( mkdir "%wall%" )





:start
echo ^>autoXtract running...
set "tempX=%temp%\Xtract_%random%"
md "%tempX%"

FOR /R "%paper%" %%a in (*.*) do (
	if %%~za GTR 100000 ( 
		copy %%a "%tempX%" >nul 2>&1
	)
)


FOR /R "%tempX%" %%a in (*.*) do (
	set /a "wrk+=1"
	rename "%%a" "workin_!wrk!.jpg" >nul 2>&1
)


FOR /R "%wall%" %%a in (*.*) do (
	set "reported="
	FOR /R "%tempX%" %%c in (*.*) do if not defined reported IF /i "%%~nxa" lss "%%~nxc" IF "%%~za"=="%%~zc" (
		FC /b "%%a" "%%c" >nul
		if not !errorlevel! EQU 1 (
			erase /F "%%c"
			set reported=Y
		)
	)
)


rd "%tempX%" || (

	FOR /R "%tempX%" %%a in (*.*) do (
		copy %%a "%wall%" >nul 2>&1
		set /a "num+=1"
	)

	FOR /R "%wall%" %%a in ("Spotlight (*).jpg") do (
		set "Com=%%~na"
		set "Com=!Com:(=!"
		set "Com=!Com:)=!"
		set "Com=!Com:Spotlight =!"
		set "Com=!Com: =!"
		if !Com! GTR !max! set "max=!Com!"
	)

	FOR /R "%wall%" %%a in ("workin_*.jpg") do (
		set /a "max+=1"
		rename "%%a" "Spotlight (!max!).jpg" >nul 2>&1
	)

)

rd /S /Q "%tempX%"


:close
cls
echo ________________________________________________________________________________
echo.
echo                            %title% %version%
echo.
echo                             grabbed !num! wallpapers
echo ________________________________________________________________________________
timeout /t 1 >nul
endlocal
exit


:swrong
cls
color 17
set erCode=%random%%random%%random%
set erCode=%erCode:~-3%
echo ________________________________________________________________________________
%loFix%
echo.
echo.
echo.
echo.
echo                                     WINDOWS
echo.
echo                 A fatal exception 0E has occured at 0028:CB4T%erCode%A1
echo                   STOP: 0x00000007 INVALID_SOFTWARE_INTERRUPT
echo                   The current application will be terminated
echo.
echo.
echo.
echo.
echo.
echo.
echo ________________________________________________________________________________
timeout /t 10 >nul
exit
