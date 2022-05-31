import pybullet as p
import time
import pybullet_data
from math import sin, cos, pi
import numpy as np

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version p.GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())
print(pybullet_data.getDataPath())
p.setGravity(0,0,-9.81)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])
myRobot = p.loadURDF("/home/xingshengwei/LarvaBotSim/urdf/LarvaBotSim.urdf",startPos, startOrientation)
#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
p.changeDynamics(bodyUniqueId=myRobot,linkIndex=4,lateralFriction=0.99)
p.changeDynamics(bodyUniqueId=myRobot,linkIndex=9,lateralFriction=0.99)

step = 0
t = 0

while True:
    p.stepSimulation()
    time.sleep(1./240.)
    #maxForce = 1
    nJoint = p.getNumJoints(myRobot)
    jointIndex = [0,1,2,3,4,5,6,7,8,9]
    omega = 5
    prisMove = -0.015-0.015*sin(omega*t)
    endMove = 0.5*cos(omega*t)
    
    pos = [prisMove,0,0,prisMove,endMove,prisMove,0,0,prisMove,-endMove]
    p.setJointMotorControlArray(myRobot,jointIndex,p.POSITION_CONTROL,pos)

    step += 1
    t = step/240

    if (step%120 == 0):
        #cubePos, cubeOrn = p.getBasePositionAndOrientation(myRobot)
        #print(cubePos,cubeOrn)
        
        #print('nJoint: ');print(nJoint)
        #print('step: ');print(step)
        #print('jointIndex: ');print(jointIndex)
        #print('pos: ');print(pos)
        print('t: ');print(t)
        ##[j0,j1,j2,j3] = p.getJointStates(myRobot,jointIndex)
        #[fp,fv,ff,ft] = j1
        #print(fp)


p.disconnect()
