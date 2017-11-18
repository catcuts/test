# avaliable
# import os, subprocess, signal, time
# proc = subprocess.Popen('ffmpeg -re -stream_loop -1 \
#     -i "D:\\Documents\\catcuts\\big_buck_bunny_480p_h264.mov" \
#     -vcodec copy -acodec copy \
#     -f flv rtmp://192.168.116.32/live/big_buck_bunny', shell=True)
# print proc.pid
# time.sleep(10)
# print 'time up!'
# subprocess.Popen('taskkill /T /F /PID '+str(proc.pid), shell=True)

# not-avaliable 
# start cmd /c <command> first open cmd then open subprocess to exec command and then the first cmd is gone so that the proc.pid is not found
# import os, subprocess, signal, time
# proc = subprocess.Popen('start cmd /c ffmpeg -re -stream_loop -1 \
#     -i "D:\\Documents\\catcuts\\big_buck_bunny_480p_h264.mov" \
#     -vcodec copy -acodec copy \
#     -f flv rtmp://192.168.116.32/live/big_buck_bunny', shell=True)
# print proc.pid
# time.sleep(10)
# print 'time up!'
# subprocess.Popen('taskkill /T /F /PID '+str(proc.pid), shell=True)

# testing
import os, subprocess, signal, time
proc = subprocess.Popen('ffmpeg -re -stream_loop -1 \
    -i "D:\\Documents\\catcuts\\big_buck_bunny_480p_h264.mov" \
    -vcodec copy -acodec copy \
    -f flv rtmp://192.168.116.32/live/big_buck_bunny -loglevel quiet', shell=True)
print proc.pid
time.sleep(10)
print 'time up!'
subprocess.Popen('taskkill /T /F /PID '+str(proc.pid), shell=True)