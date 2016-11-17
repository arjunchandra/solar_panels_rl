#!/usr/bin/env python
'''
Code for running RL + solar tracking experiments.

Author: Emily Reif + David Abel
'''

# Python imports.
import time, argparse, os, sys, copy
from collections import defaultdict

# simple_rl imports.
from simple_rl.utils.run_experiments import run_agents_on_mdp
from simple_rl.experiments import Experiment
from simple_rl.agents import RandomAgent, FixedPolicyAgent, QLearnerAgent, LinearApproxQLearnerAgent

# Local imports.
from solarOOMDP.SolarOOMDPClass import SolarOOMDP
import tracking_baselines as tb

def main():
    # Setup MDP.
    solar_mdp = SolarOOMDP()
    actions = solar_mdp.get_actions()
    gamma = solar_mdp.get_gamma()

    # Setup fixed agents.
    baseline_policy = tb.policy_from_simple_tracker
    baseline_tracker = FixedPolicyAgent(baseline_policy)

    # Setup RL agents.
    random_agent = RandomAgent(actions)
    qlearner_agent = QLearnerAgent(actions, gamma=gamma, explore="uniform")
    lin_approx_agent = LinearApproxQLearnerAgent(actions, gamma=gamma)

    agents = [baseline_tracker, qlearner_agent, random_agent]
    

    # Run experiments.
    run_agents_on_mdp(agents, solar_mdp)

if __name__ == "__main__":
    main()