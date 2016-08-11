import subprocess

from threading import Timer

kill = lambda process: process.kill()
cmd = ['ping', 'www.google.com']
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_timer = Timer(5, kill, [ping])

try:
    my_timer.start()
    stdout, stderr = ping.communicate()
finally:
    my_timer.cancel()

print (str(stdout))