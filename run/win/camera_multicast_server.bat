cd %~dp0
cd ../../capture
python camera_multicast_server.py picture 1920 1080 30 30
rem python filename mode frame_width frame_height frame_fps frame_brightness 
start .\capture
pause