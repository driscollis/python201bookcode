import urllib.robotparser


robot = urllib.robotparser.RobotFileParser()
robot.set_url('http://arstechnica.com/robots.txt')
print(robot.read())
print(robot.can_fetch('*', 'http://arstechnica.com/'))
print(robot.can_fetch('*', 'http://arstechnica.com/cgi-bin/'))
