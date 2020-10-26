@echo off
@REM activate
call :twitterFunc
:twitterFunc
py getTweets2.py
git add .
git commit -m "add tweets"
git push origin master
timeout 900
call :twitterFunc
EXIT /B 0
pause