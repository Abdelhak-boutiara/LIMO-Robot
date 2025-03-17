from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([  
        
        Node(
            package='joy',  
            executable='joy_node',
            name='joy_node',
            output='screen',
        ),       
        Node(
            package='boutiara_limo',  
            executable='joy_to_twist',
            name='joy_to_twist',
            output='screen',
        ),
        ])
