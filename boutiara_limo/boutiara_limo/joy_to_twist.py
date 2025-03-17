import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class JoyToTwist(Node):
    def __init__(self):
        super().__init__('joy_to_twist')


        # Subscriber to the joystick topic
        self.joy_subscriber = self.create_subscription(Joy, 'joy', self.joy_callback, 10)
        
        # Publisher to the robot's velocity topic
        self.twist_publisher = self.create_publisher(Twist,'cmd_vel',10)

        self.get_logger().info('JoyToTwist node has started.')

        



    def joy_callback(self, msg: Joy):
        
        # Create a Twist message
            twist = Twist()
            
            # Map joystick axes to linear and angular velocities
            
            twist.linear.x = msg.axes[1] * 0.5
            twist.angular.z = msg.axes[3] * 1
            
            # Publish the Twist message to control the robot
            self.twist_publisher.publish(twist)

            

def main(args=None):
    rclpy.init(args=args)
    joy_to_twist = JoyToTwist()
    rclpy.spin(joy_to_twist)
    joy_to_twist.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

