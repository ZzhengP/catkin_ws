// Generated by gencpp from file panda_mpc/UIRequest.msg
// DO NOT EDIT!


#ifndef PANDA_MPC_MESSAGE_UIREQUEST_H
#define PANDA_MPC_MESSAGE_UIREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Twist.h>

namespace panda_mpc
{
template <class ContainerAllocator>
struct UIRequest_
{
  typedef UIRequest_<ContainerAllocator> Type;

  UIRequest_()
    : play_traj(false)
    , jog_robot(false)
    , publish_traj(false)
    , build_traj(false)
    , positioning_(false)
    , p_gains_()
    , d_gains_()
    , move_signal_(false)
    , tune_gain(false)
    , amplitude(0.0)
    , axis(0)
    , exit_(false)
    , distance_to_contact_(0.0)
    , fake_distance_(false)  {
    }
  UIRequest_(const ContainerAllocator& _alloc)
    : play_traj(false)
    , jog_robot(false)
    , publish_traj(false)
    , build_traj(false)
    , positioning_(false)
    , p_gains_(_alloc)
    , d_gains_(_alloc)
    , move_signal_(false)
    , tune_gain(false)
    , amplitude(0.0)
    , axis(0)
    , exit_(false)
    , distance_to_contact_(0.0)
    , fake_distance_(false)  {
  (void)_alloc;
    }



   typedef uint8_t _play_traj_type;
  _play_traj_type play_traj;

   typedef uint8_t _jog_robot_type;
  _jog_robot_type jog_robot;

   typedef uint8_t _publish_traj_type;
  _publish_traj_type publish_traj;

   typedef uint8_t _build_traj_type;
  _build_traj_type build_traj;

   typedef uint8_t _positioning__type;
  _positioning__type positioning_;

   typedef  ::geometry_msgs::Twist_<ContainerAllocator>  _p_gains__type;
  _p_gains__type p_gains_;

   typedef  ::geometry_msgs::Twist_<ContainerAllocator>  _d_gains__type;
  _d_gains__type d_gains_;

   typedef uint8_t _move_signal__type;
  _move_signal__type move_signal_;

   typedef uint8_t _tune_gain_type;
  _tune_gain_type tune_gain;

   typedef double _amplitude_type;
  _amplitude_type amplitude;

   typedef int64_t _axis_type;
  _axis_type axis;

   typedef uint8_t _exit__type;
  _exit__type exit_;

   typedef double _distance_to_contact__type;
  _distance_to_contact__type distance_to_contact_;

   typedef uint8_t _fake_distance__type;
  _fake_distance__type fake_distance_;





  typedef boost::shared_ptr< ::panda_mpc::UIRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::panda_mpc::UIRequest_<ContainerAllocator> const> ConstPtr;

}; // struct UIRequest_

typedef ::panda_mpc::UIRequest_<std::allocator<void> > UIRequest;

typedef boost::shared_ptr< ::panda_mpc::UIRequest > UIRequestPtr;
typedef boost::shared_ptr< ::panda_mpc::UIRequest const> UIRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::panda_mpc::UIRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::panda_mpc::UIRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::panda_mpc::UIRequest_<ContainerAllocator1> & lhs, const ::panda_mpc::UIRequest_<ContainerAllocator2> & rhs)
{
  return lhs.play_traj == rhs.play_traj &&
    lhs.jog_robot == rhs.jog_robot &&
    lhs.publish_traj == rhs.publish_traj &&
    lhs.build_traj == rhs.build_traj &&
    lhs.positioning_ == rhs.positioning_ &&
    lhs.p_gains_ == rhs.p_gains_ &&
    lhs.d_gains_ == rhs.d_gains_ &&
    lhs.move_signal_ == rhs.move_signal_ &&
    lhs.tune_gain == rhs.tune_gain &&
    lhs.amplitude == rhs.amplitude &&
    lhs.axis == rhs.axis &&
    lhs.exit_ == rhs.exit_ &&
    lhs.distance_to_contact_ == rhs.distance_to_contact_ &&
    lhs.fake_distance_ == rhs.fake_distance_;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::panda_mpc::UIRequest_<ContainerAllocator1> & lhs, const ::panda_mpc::UIRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace panda_mpc

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::panda_mpc::UIRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::panda_mpc::UIRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::panda_mpc::UIRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::panda_mpc::UIRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::panda_mpc::UIRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::panda_mpc::UIRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::panda_mpc::UIRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c014034d544e11b0948e3346a66ba7c7";
  }

  static const char* value(const ::panda_mpc::UIRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc014034d544e11b0ULL;
  static const uint64_t static_value2 = 0x948e3346a66ba7c7ULL;
};

template<class ContainerAllocator>
struct DataType< ::panda_mpc::UIRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "panda_mpc/UIRequest";
  }

  static const char* value(const ::panda_mpc::UIRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::panda_mpc::UIRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool play_traj\n"
"bool jog_robot\n"
"bool publish_traj \n"
"bool build_traj\n"
"bool positioning_\n"
"geometry_msgs/Twist p_gains_\n"
"geometry_msgs/Twist d_gains_\n"
"bool move_signal_\n"
"bool tune_gain\n"
"float64 amplitude\n"
"int64 axis\n"
"bool exit_\n"
"float64 distance_to_contact_\n"
"bool fake_distance_\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Twist\n"
"# This expresses velocity in free space broken into its linear and angular parts.\n"
"Vector3  linear\n"
"Vector3  angular\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::panda_mpc::UIRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::panda_mpc::UIRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.play_traj);
      stream.next(m.jog_robot);
      stream.next(m.publish_traj);
      stream.next(m.build_traj);
      stream.next(m.positioning_);
      stream.next(m.p_gains_);
      stream.next(m.d_gains_);
      stream.next(m.move_signal_);
      stream.next(m.tune_gain);
      stream.next(m.amplitude);
      stream.next(m.axis);
      stream.next(m.exit_);
      stream.next(m.distance_to_contact_);
      stream.next(m.fake_distance_);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct UIRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::panda_mpc::UIRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::panda_mpc::UIRequest_<ContainerAllocator>& v)
  {
    s << indent << "play_traj: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.play_traj);
    s << indent << "jog_robot: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.jog_robot);
    s << indent << "publish_traj: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.publish_traj);
    s << indent << "build_traj: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.build_traj);
    s << indent << "positioning_: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.positioning_);
    s << indent << "p_gains_: ";
    s << std::endl;
    Printer< ::geometry_msgs::Twist_<ContainerAllocator> >::stream(s, indent + "  ", v.p_gains_);
    s << indent << "d_gains_: ";
    s << std::endl;
    Printer< ::geometry_msgs::Twist_<ContainerAllocator> >::stream(s, indent + "  ", v.d_gains_);
    s << indent << "move_signal_: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.move_signal_);
    s << indent << "tune_gain: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.tune_gain);
    s << indent << "amplitude: ";
    Printer<double>::stream(s, indent + "  ", v.amplitude);
    s << indent << "axis: ";
    Printer<int64_t>::stream(s, indent + "  ", v.axis);
    s << indent << "exit_: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.exit_);
    s << indent << "distance_to_contact_: ";
    Printer<double>::stream(s, indent + "  ", v.distance_to_contact_);
    s << indent << "fake_distance_: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.fake_distance_);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PANDA_MPC_MESSAGE_UIREQUEST_H
