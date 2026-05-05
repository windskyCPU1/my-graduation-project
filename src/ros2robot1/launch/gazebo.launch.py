import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    robot_name_in_model1 =" "
    urdf_tutorial_path = get_package_share_directory('ros2robot1')
    default_model_path1 = urdf_tutorial_path + '/urdf/ros2robot1.urdf.xacro'
    default_world_path = urdf_tutorial_path + '/world/custom_room.world'
# 声明 use_sim_time 参数
    use_sim_time_arg = launch.actions.DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )
    action_declare_arg_mode_path1 = launch.actions.DeclareLaunchArgument(
        name='model1', default_value=str(default_model_path1),
        description='URDF 的绝对路径')
    robot_description1 = launch_ros.parameter_descriptions.ParameterValue(
        launch.substitutions.Command(
            ['xacro ', launch.substitutions.LaunchConfiguration('model1')]),
        value_type=str)
    robot_state_publisher_node1 = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        # namespace=robot_name_in_model1,
        #name='my_robot_state_publisher', 
        parameters=[
            {'robot_description': robot_description1 },
            # {'frame_prefix': f"{robot_name_in_model1}/"},
            {'use_sim_time': LaunchConfiguration('use_sim_time')}
        ]
    )
    launch_gazebo = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory(
            'gazebo_ros'), '/launch', '/gazebo.launch.py']),
        launch_arguments=[('world', default_world_path), ('verbose', 'true')]
    )
    # 请求 Gazebo 加载机器人
    spawn_entity_node1 = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        # namespace=robot_name_in_model1,
        
        arguments=['-topic', 'robot_description',
                    '-entity', 'robot1',
                #     '-robot_namespace', f'/{robot_name_in_model1}',
                    '-x', '0.0', '-y', '0.0', '-z', '0.0']
    )
    # spawn_entity_node3 = launch_ros.actions.Node(
    # package='gazebo_ros',
    # executable='spawn_entity.py',
    # namespace=robot_name_in_model1,
    # arguments=['-param', 'robot_description',   # 这里必须用 -param
    #            '-entity', robot_name_in_model1,
    #            '-robot_namespace', robot_name_in_model1,   # 不要斜杠，例如 fishbot1
    #            '-x', '1.0', '-y', '2.0', '-z', '0.0']
    # )
    # controller_manager1 = launch_ros.actions.Node(
    #     package="controller_manager",
    #     executable="controller_manager",
    #     # namespace=robot_name_in_model1,
    #     parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
    #     arguments=["--ros-args", "--log-level", "info"],
    #     output="screen",
    # )

    joint_state_control_node1 = launch_ros.actions.Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "controller_manager"],
        #namespace=robot_name_in_model1,
        output="both",
    )
    diff_drive_control_node1 = launch_ros.actions.Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_drive_controller", "--controller-manager", "controller_manager"],
        #namespace=robot_name_in_model1,
        output="both",
    )
    return launch.LaunchDescription([
        use_sim_time_arg,
        action_declare_arg_mode_path1,
        launch_gazebo,
        robot_state_publisher_node1,
        #robot_state_publisher_node2,
        #robot_state_publisher_node3,
        spawn_entity_node1,
        
        #spawn_entity_node3,
        
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=spawn_entity_node1,
                on_exit=[joint_state_control_node1]
            )
        ),
        
        
        launch.actions.RegisterEventHandler(
           event_handler=launch.event_handlers.OnProcessExit(
               target_action=joint_state_control_node1,
               on_exit=[diff_drive_control_node1]
           )
        ),
        
        
        
        
    ])