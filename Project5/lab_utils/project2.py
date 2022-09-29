import rospy
# import tf
from nav_msgs.msg import Odometry
from scipy.spatial.transform import Rotation as R
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3


def publish_odom_tf(odom_pub, x, y, vlin, vang, yaw):
    time = rospy.Time.now()
    odom_frame = "odom"
    base_frame = "base_link"

    # Get pose and orientation
    pose = (x, y, 0)
    r = R.from_euler('xyz', [0, 0, yaw], degrees=False)
    orientation = r.as_quat()
    
    # Publish odometry message
    odom_msg = Odometry()
    odom_msg.header.frame_id = odom_frame
    odom_msg.header.stamp = time
    odom_msg.child_frame_id = base_frame
    odom_msg.pose.pose = Pose(Point(*pose), Quaternion(*orientation))
    odom_msg.twist.twist = Twist(Vector3(vlin, 0, 0), Vector3(0, 0, vang))
    odom_pub.publish(odom_msg)

    # Broadcast tf transform
    # br = tf.TransformBroadcaster()
    # br.sendTransform(pose, orientation, time, base_frame, odom_frame)

    return odom_msg

def get_heading_from_quaternion(q):
    r= R.from_quat([q.x, q.y, q.z, q.w])
    angles = r.as_euler('zyx', degrees=False)
    return angles[2]