# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from panda_mpc/PandaRunMsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class PandaRunMsg(genpy.Message):
  _md5sum = "978d838c2f0b7635c26f79d5649e9439"
  _type = "panda_mpc/PandaRunMsg"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
float64 vmax_ec # [m/s]
float64 t_traj_curr
geometry_msgs/Twist Xd_traj
geometry_msgs/Twist Xdd_traj
geometry_msgs/Twist X_err
geometry_msgs/Twist Xd_control
sensor_msgs/JointState qd_des
bool play_traj_
bool positioning_
bool tune_gains_
float64 distance_to_contact_
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort
"""
  __slots__ = ['header','vmax_ec','t_traj_curr','Xd_traj','Xdd_traj','X_err','Xd_control','qd_des','play_traj_','positioning_','tune_gains_','distance_to_contact_']
  _slot_types = ['std_msgs/Header','float64','float64','geometry_msgs/Twist','geometry_msgs/Twist','geometry_msgs/Twist','geometry_msgs/Twist','sensor_msgs/JointState','bool','bool','bool','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,vmax_ec,t_traj_curr,Xd_traj,Xdd_traj,X_err,Xd_control,qd_des,play_traj_,positioning_,tune_gains_,distance_to_contact_

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PandaRunMsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.vmax_ec is None:
        self.vmax_ec = 0.
      if self.t_traj_curr is None:
        self.t_traj_curr = 0.
      if self.Xd_traj is None:
        self.Xd_traj = geometry_msgs.msg.Twist()
      if self.Xdd_traj is None:
        self.Xdd_traj = geometry_msgs.msg.Twist()
      if self.X_err is None:
        self.X_err = geometry_msgs.msg.Twist()
      if self.Xd_control is None:
        self.Xd_control = geometry_msgs.msg.Twist()
      if self.qd_des is None:
        self.qd_des = sensor_msgs.msg.JointState()
      if self.play_traj_ is None:
        self.play_traj_ = False
      if self.positioning_ is None:
        self.positioning_ = False
      if self.tune_gains_ is None:
        self.tune_gains_ = False
      if self.distance_to_contact_ is None:
        self.distance_to_contact_ = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.vmax_ec = 0.
      self.t_traj_curr = 0.
      self.Xd_traj = geometry_msgs.msg.Twist()
      self.Xdd_traj = geometry_msgs.msg.Twist()
      self.X_err = geometry_msgs.msg.Twist()
      self.Xd_control = geometry_msgs.msg.Twist()
      self.qd_des = sensor_msgs.msg.JointState()
      self.play_traj_ = False
      self.positioning_ = False
      self.tune_gains_ = False
      self.distance_to_contact_ = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_26d3I().pack(_x.vmax_ec, _x.t_traj_curr, _x.Xd_traj.linear.x, _x.Xd_traj.linear.y, _x.Xd_traj.linear.z, _x.Xd_traj.angular.x, _x.Xd_traj.angular.y, _x.Xd_traj.angular.z, _x.Xdd_traj.linear.x, _x.Xdd_traj.linear.y, _x.Xdd_traj.linear.z, _x.Xdd_traj.angular.x, _x.Xdd_traj.angular.y, _x.Xdd_traj.angular.z, _x.X_err.linear.x, _x.X_err.linear.y, _x.X_err.linear.z, _x.X_err.angular.x, _x.X_err.angular.y, _x.X_err.angular.z, _x.Xd_control.linear.x, _x.Xd_control.linear.y, _x.Xd_control.linear.z, _x.Xd_control.angular.x, _x.Xd_control.angular.y, _x.Xd_control.angular.z, _x.qd_des.header.seq, _x.qd_des.header.stamp.secs, _x.qd_des.header.stamp.nsecs))
      _x = self.qd_des.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.qd_des.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.qd_des.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.qd_des.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_des.position))
      length = len(self.qd_des.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_des.velocity))
      length = len(self.qd_des.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_des.effort))
      _x = self
      buff.write(_get_struct_3Bd().pack(_x.play_traj_, _x.positioning_, _x.tune_gains_, _x.distance_to_contact_))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Xd_traj is None:
        self.Xd_traj = geometry_msgs.msg.Twist()
      if self.Xdd_traj is None:
        self.Xdd_traj = geometry_msgs.msg.Twist()
      if self.X_err is None:
        self.X_err = geometry_msgs.msg.Twist()
      if self.Xd_control is None:
        self.Xd_control = geometry_msgs.msg.Twist()
      if self.qd_des is None:
        self.qd_des = sensor_msgs.msg.JointState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 220
      (_x.vmax_ec, _x.t_traj_curr, _x.Xd_traj.linear.x, _x.Xd_traj.linear.y, _x.Xd_traj.linear.z, _x.Xd_traj.angular.x, _x.Xd_traj.angular.y, _x.Xd_traj.angular.z, _x.Xdd_traj.linear.x, _x.Xdd_traj.linear.y, _x.Xdd_traj.linear.z, _x.Xdd_traj.angular.x, _x.Xdd_traj.angular.y, _x.Xdd_traj.angular.z, _x.X_err.linear.x, _x.X_err.linear.y, _x.X_err.linear.z, _x.X_err.angular.x, _x.X_err.angular.y, _x.X_err.angular.z, _x.Xd_control.linear.x, _x.Xd_control.linear.y, _x.Xd_control.linear.z, _x.Xd_control.angular.x, _x.Xd_control.angular.y, _x.Xd_control.angular.z, _x.qd_des.header.seq, _x.qd_des.header.stamp.secs, _x.qd_des.header.stamp.nsecs,) = _get_struct_26d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.qd_des.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.qd_des.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.qd_des.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.qd_des.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_des.position = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_des.velocity = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_des.effort = s.unpack(str[start:end])
      _x = self
      start = end
      end += 11
      (_x.play_traj_, _x.positioning_, _x.tune_gains_, _x.distance_to_contact_,) = _get_struct_3Bd().unpack(str[start:end])
      self.play_traj_ = bool(self.play_traj_)
      self.positioning_ = bool(self.positioning_)
      self.tune_gains_ = bool(self.tune_gains_)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_26d3I().pack(_x.vmax_ec, _x.t_traj_curr, _x.Xd_traj.linear.x, _x.Xd_traj.linear.y, _x.Xd_traj.linear.z, _x.Xd_traj.angular.x, _x.Xd_traj.angular.y, _x.Xd_traj.angular.z, _x.Xdd_traj.linear.x, _x.Xdd_traj.linear.y, _x.Xdd_traj.linear.z, _x.Xdd_traj.angular.x, _x.Xdd_traj.angular.y, _x.Xdd_traj.angular.z, _x.X_err.linear.x, _x.X_err.linear.y, _x.X_err.linear.z, _x.X_err.angular.x, _x.X_err.angular.y, _x.X_err.angular.z, _x.Xd_control.linear.x, _x.Xd_control.linear.y, _x.Xd_control.linear.z, _x.Xd_control.angular.x, _x.Xd_control.angular.y, _x.Xd_control.angular.z, _x.qd_des.header.seq, _x.qd_des.header.stamp.secs, _x.qd_des.header.stamp.nsecs))
      _x = self.qd_des.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.qd_des.name)
      buff.write(_struct_I.pack(length))
      for val1 in self.qd_des.name:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.qd_des.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_des.position.tostring())
      length = len(self.qd_des.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_des.velocity.tostring())
      length = len(self.qd_des.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_des.effort.tostring())
      _x = self
      buff.write(_get_struct_3Bd().pack(_x.play_traj_, _x.positioning_, _x.tune_gains_, _x.distance_to_contact_))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Xd_traj is None:
        self.Xd_traj = geometry_msgs.msg.Twist()
      if self.Xdd_traj is None:
        self.Xdd_traj = geometry_msgs.msg.Twist()
      if self.X_err is None:
        self.X_err = geometry_msgs.msg.Twist()
      if self.Xd_control is None:
        self.Xd_control = geometry_msgs.msg.Twist()
      if self.qd_des is None:
        self.qd_des = sensor_msgs.msg.JointState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 220
      (_x.vmax_ec, _x.t_traj_curr, _x.Xd_traj.linear.x, _x.Xd_traj.linear.y, _x.Xd_traj.linear.z, _x.Xd_traj.angular.x, _x.Xd_traj.angular.y, _x.Xd_traj.angular.z, _x.Xdd_traj.linear.x, _x.Xdd_traj.linear.y, _x.Xdd_traj.linear.z, _x.Xdd_traj.angular.x, _x.Xdd_traj.angular.y, _x.Xdd_traj.angular.z, _x.X_err.linear.x, _x.X_err.linear.y, _x.X_err.linear.z, _x.X_err.angular.x, _x.X_err.angular.y, _x.X_err.angular.z, _x.Xd_control.linear.x, _x.Xd_control.linear.y, _x.Xd_control.linear.z, _x.Xd_control.angular.x, _x.Xd_control.angular.y, _x.Xd_control.angular.z, _x.qd_des.header.seq, _x.qd_des.header.stamp.secs, _x.qd_des.header.stamp.nsecs,) = _get_struct_26d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.qd_des.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.qd_des.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.qd_des.name = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.qd_des.name.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_des.position = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_des.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_des.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 11
      (_x.play_traj_, _x.positioning_, _x.tune_gains_, _x.distance_to_contact_,) = _get_struct_3Bd().unpack(str[start:end])
      self.play_traj_ = bool(self.play_traj_)
      self.positioning_ = bool(self.positioning_)
      self.tune_gains_ = bool(self.tune_gains_)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_26d3I = None
def _get_struct_26d3I():
    global _struct_26d3I
    if _struct_26d3I is None:
        _struct_26d3I = struct.Struct("<26d3I")
    return _struct_26d3I
_struct_3Bd = None
def _get_struct_3Bd():
    global _struct_3Bd
    if _struct_3Bd is None:
        _struct_3Bd = struct.Struct("<3Bd")
    return _struct_3Bd
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
