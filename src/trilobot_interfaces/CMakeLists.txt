cmake_minimum_required(VERSION 3.20)
project(trilobot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Colour.msg"
  "msg/ColourHex.msg"
  "msg/ColourHsv.msg"
  "msg/Motor.msg"
  "msg/Speed.msg"
  "msg/UnderLight.msg"
  "srv/Coast.srv"
  "srv/ClearUnderlight.srv"
  "srv/ClearUnderlighting.srv"
  "srv/DisableUnderlighting.srv"
  "srv/FillUnderlighting.srv"
  "srv/FillUnderlightingHex.srv"
  "srv/FillUnderlightingHsv.srv"
  "srv/MotorSpeed.srv"
  "srv/SetUnderlight.srv"
  "srv/SetUnderlightHex.srv"
  "srv/SetUnderlightHsv.srv"
  "srv/SetUnderlights.srv"
  "srv/SetUnderlightsHex.srv"
  "srv/SetUnderlightsHsv.srv"
  "srv/ShowUnderlighting.srv"
  "srv/SingleSpeed.srv"
  "srv/TwinSpeed.srv"
  "srv/GetButtonsState.srv"
  "srv/ReadDistance.srv"
  "srv/SetButtonLed.srv"
  "srv/SetButtonLedBrightness.srv"
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
