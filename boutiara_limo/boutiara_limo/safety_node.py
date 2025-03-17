import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class SafetyNode(Node):
    def __init__(self):
        super().__init__('safety_node')
        
        
        self.scan_subscriber = self.create_subscription(LaserScan, 'scan', self.lidar_callback, 10)
        
        self.twist_subscriber = self.create_subscription(Twist,'cmd_pure', self.safety_callback,10)
        
        self.safety_publisher = self.create_publisher(Twist,'cmd_vel',10)

        self.data = None  
        self.data_list = [] 
        self.v_pure = 0.0   
        self.rot_pure = 0.0 

        self.get_logger().info('Safety node has started.')






    def lidar_callback(self, msg):
        self.data = msg
        self.data_list = []
        
        for i in range(30, 90):
            self.data_list.append(self.data.ranges[i])

        
    def safety_callback(self, msg):
        self.v_pure = msg.linear.x
        self.rot_pure = msg.angular.z

        twist = Twist()
        
        if min(self.data_list) < 0.3:
            twist.linear.x = -0.2
        elif min(self.data_list) < 0.5:
            twist.linear.x = 0
        else:
            twist.linear.x = self.v_pure
            
        twist.angular.z = self.rot_pure
        self.safety_publisher.publish(twist)




def main(args=None):
    rclpy.init(args=args)
    safety_node = SafetyNode()
    rclpy.spin(safety_node)
    safety_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
