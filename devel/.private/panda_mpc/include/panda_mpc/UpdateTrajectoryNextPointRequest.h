// Generated by gencpp from file panda_mpc/UpdateTrajectoryNextPointRequest.msg
// DO NOT EDIT!


#ifndef PANDA_MPC_MESSAGE_UPDATETRAJECTORYNEXTPOINTREQUEST_H
#define PANDA_MPC_MESSAGE_UPDATETRAJECTORYNEXTPOINTREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Twist.h>

namespace panda_mpc
{
template <class ContainerAllocator>
struct UpdateTrajectoryNextPointRequest_
{
  typedef UpdateTrajectoryNextPointRequest_<ContainerAllocator> Type;

  UpdateTrajectoryNextPointRequest_()
    : next_point()
    , next_vel()  {
    }
  UpdateTrajectoryNextPointRequest_(const ContainerAllocator& _alloc)
    : next_point(_alloc)
    , next_vel(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _next_point_type;
  _next_point_type next_point;

   typedef  ::geometry_msgs::Twist_<ContainerAllocator>  _next_vel_type;
  _next_vel_type next_vel;





  typedef boost::shared_ptr< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> const> ConstPtr;

}; // struct UpdateTrajectoryNextPointRequest_

typedef ::panda_mpc::UpdateTrajectoryNextPointRequest_<std::allocator<void> > UpdateTrajectoryNextPointRequest;

typedef boost::shared_ptr< ::panda_mpc::UpdateTrajectoryNextPointRequest > UpdateTrajectoryNextPointRequestPtr;
typedef boost::shared_ptr< ::panda_mpc::UpdateTrajectoryNextPointRequest const> UpdateTrajectoryNextPointRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator1> & lhs, const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator2> & rhs)
{
  return lhs.next_point == rhs.next_point &&
    lhs.next_vel == rhs.next_vel;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator1> & lhs, const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace panda_mpc

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2685428bccce90adb95a24e6e6228b8f";
  }

  static const char* value(const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2685428bccce90adULL;
  static const uint64_t static_value2 = 0xb95a24e6e6228b8fULL;
};

template<class ContainerAllocator>
struct DataType< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "panda_mpc/UpdateTrajectoryNextPointRequest";
  }

  static const char* value(const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Vector3 next_point\n"
"geometry_msgs/Twist next_vel\n"
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
"================================================================================\n"
"MSG: geometry_msgs/Twist\n"
"# This expresses velocity in free space broken into its linear and angular parts.\n"
"Vector3  linear\n"
"Vector3  angular\n"
;
  }

  static const char* value(const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.next_point);
      stream.next(m.next_vel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct UpdateTrajectoryNextPointRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::panda_mpc::UpdateTrajectoryNextPointRequest_<ContainerAllocator>& v)
  {
    s << indent << "next_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.next_point);
    s << indent << "next_vel: ";
    s << std::endl;
    Printer< ::geometry_msgs::Twist_<ContainerAllocator> >::stream(s, indent + "  ", v.next_vel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PANDA_MPC_MESSAGE_UPDATETRAJECTORYNEXTPOINTREQUEST_H
