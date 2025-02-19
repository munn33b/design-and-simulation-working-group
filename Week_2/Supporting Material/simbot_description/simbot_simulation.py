import pybullet as p
import time
p.connect(p.GUI)
offset = [0,0,0]

turtle = p.loadURDF("urdf/simbot_description.urdf",offset)
plane = p.loadURDF("plane.urdf")
p.setRealTimeSimulation(1)


while (1):
	p.setGravity(0,0,-10)
	time.sleep(1./240.)
	keys = p.getKeyboardEvents()
	leftWheelVelocity=0
	rightWheelVelocity=0
	speed=10
	
	
