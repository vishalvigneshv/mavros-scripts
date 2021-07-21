# mavros-scripts

## Setup
1. run ```roscore```.
2. run ```sim_vehicle.py -v ArduCopter -f gazebo-iris -m --mav10 --map --console -I0``` to set up the simulator. I chose Arducoptor as vehicle and iris drone. It also opens up     mavproxy console and a map.
3. run ```gazebo --verbose iris_ardupilot.world``` to set up the physical environment (Gazebo) in which the simulator works.
4. run ```roslaunch mavros apm.launch fcu_url:="udp://127.0.0.1:14551@14555"``` to start MAVROS.

## deploying Scripts
1. open up QGroundControl and takeoff to hold position. 
2. run the .py executable
