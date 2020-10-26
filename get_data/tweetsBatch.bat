@echo off
@REM activate
py getTweets2.py
git add . && git commit - m "add tweets" && git push origin master
pause