# Generate video for a program. Make sure you have the executable open
import sys
sys.path.append('../simulation/')
from unity_simulator.comm_unity import UnityCommunication
#script = ['<char0> [Walk] <towel> (1)', '<char0> [Grab] <towel> (1)','<char0> [Wipe] <towel> (1)'] # Add here your script
#script = ['<char0> [Walk] <towel> (1)', '<char0> [Grab] <towel> (1)'] # Add here your script
#script = ['<char0> [Walk] <Bathroom_counter> (1)'] # Add here your script
script = ['<char0> [Walk] <tv> (1)', '<char0> [switchon] <tv> (1)']
print('Starting Unity...')
comm = UnityCommunication()
print('Starting scene...')
message = comm.reset()
print(message)
comm.add_character('Chars/Female1')
print('Generating video...')
s = comm.render_script(script, recording=True, find_solution=True, frame_rate=15)
print(s)
#print(environment_graph)
su, graph = comm.environment_graph()
print(su)
print(graph)
print('Generated, find video in simulation/unity_simulator/output/')
