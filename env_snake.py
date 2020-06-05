#!/usr/bin

import gym
import time
import numpy as np
import time
from gym import utils, spaces

from gym.utils import seeding
from gym.envs.registration import register
from snake_rl import snakeconnection

# register the training environment in the gym as an available one
reg = register(
    id='Snake-v0',
    entry_point='env_snake:Env',
    max_episode_steps=100,
    )
# env = gym.make('QuadcopterLiveShow-v0')

class Env(gym.Env):

    def __init__(self):

        self.running_step = 0.3
        self.mode = ''
        # stablishes connection with simulator
        self.control_snake = snakeconnection()
        self.count =0
        class data():
            x = 0
            y = 0
        self.current_init_pose = data()
        self.data_pose = data()
        self.desired_pose=data()
        self.action_space = spaces.Discrete(4) #Forward,Left,Right,Down
        self.reward_range = (-np.inf, np.inf)
        self.seed()

    # A function to initialize the random generator
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
        
    # Resets the state of the environment and returns an initial observation.
    def _reset(self):
        self.control_snake.respawn()
        observation = np.array([self.data_pose.x,self.data_pose.y,self.calculate_dist_between_two_Points()])
        observation = np.float32(observation)
        return observation

    def _step(self, action):

        # Given the action selected by the learning algorithm,
        # we perform the corresponding movement of the robot
        
        # 1st, we decide which velocity command corresponds
        if action == 0: #FORWARD
            self.mode='up'
        elif action == 1: #down
            self.mode='down'
        elif action == 2: #RIGHT
            self.mode='right'
        elif action == 3: #left
            self.mode='left'

        
        # Then we send the command to the robot and let it go
        # for running_step second
        self.desired_pose.x,self.desired_pose.y,self.data_pose.x,self.data_pose.y,self.count=self.control_snake.snake(self.mode)
        
        #time.sleep(self.running_step)
        #self.take_observation()

        # finally we get an evaluation based on what happened in the sim
        reward,done = self.process_data(self)
        reward =(reward - 100)*2
        state = np.array([self.data_pose.x,self.data_pose.y,self.calculate_dist_between_two_Points()])
        state = np.float32(state)
        return state, reward, done, {}


    def calculate_dist_between_two_Points(self):
        s1x=self.data_pose.x
        s1y=self.data_pose.y
        p2x=self.desired_pose.x
        p2y=self.desired_pose.y
        a = np.array((s1x ,s1y))
        b = np.array((p2x ,p2y))
        
        dist = np.linalg.norm(a-b)  
        return dist


    def init_desired_pose(self):

        self.current_init_pose.x = self.data_pose.x
        self.current_init_pose.y = self.data_pose.y
    

    def improved_distance_reward(self,current_pose):

        current_dist = self.calculate_dist_between_two_Points()
        #rospy.loginfo("Calculated Distance = "+str(current_dist))

        reward = -1*current_dist + 500           
        return reward


    def process_data(self,data_position):

        done = False

        #  minimum number of colliding        
        #if self.count > 10 and self.prev_count!=self.count:                   
            #wall = True
           

        if  self.desired_pose.x-10<=self.data_pose.x<=self.desired_pose.x+10 and self.desired_pose.y-10 <=self.data_pose.y <=self.desired_pose.y+10:
            reward = 10000
        else:
            reward = self.improved_distance_reward(data_position)

        return reward,done