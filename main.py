from dorna import Dorna
robot = Dorna()
# robot.update_firmware()
robot.connect()
cmd = {"command": "move", "prm": {"path": "joint", "movement": 0, "j0":0,"j1":0,
"j2":0, "j3":0, "j4":0}}
robot.play(cmd)