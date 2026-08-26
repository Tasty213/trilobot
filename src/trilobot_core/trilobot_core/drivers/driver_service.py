import trilobot_core.drivers.buttons as Buttons
import trilobot_core.drivers.lights as Lights
import trilobot_core.drivers.motors as Motors
from rclpy.node import Node
from std_msgs.msg import Float32
from trilobot import Trilobot
from trilobot_core.drivers.abstract_driver import StaticRobotService
from trilobot_interfaces.srv import GetButtonsState


import inspect

DISTANCE_PUBLISH_PERIOD = 0.1
BUTTON_STATES_PUBLISH_PERIOD = 0.1


class DriverService(Node):
    def __init__(self, trilobot: Trilobot):
        super().__init__("driver_service")
        self.logger = self.get_logger()
        self.logger.info("Preparing trilobot")
        self.tbot = trilobot

        self.motor_services = {}
        for driver_name, driver in inspect.getmembers(Motors, inspect.isclass):
            if driver.__module__ != Motors.__name__:
                break
            if driver is StaticRobotService:
                break
            if not issubclass(driver, StaticRobotService):
                raise ValueError(f"{driver} is not a subclass of {StaticRobotService}")
            self.logger.info(
                f"Creating service of type {driver.service_type()} with name {driver.service_name()} executed by {driver.execute}"
            )
            new_service = self.create_service(
                driver.service_type(), driver.service_name(), driver.execute  # type: ignore
            )
            self.motor_services[driver_name] = new_service

        self.button_services = {}
        for driver_name, driver in inspect.getmembers(Buttons, inspect.isclass):
            if driver.__module__ != Buttons.__name__:
                continue
            if driver is StaticRobotService:
                continue
            if not issubclass(driver, StaticRobotService):
                raise ValueError(f"{driver} is not a subclass of {StaticRobotService}")
            self.logger.info(
                f"Creating service of type {driver.service_type()} with name {driver.service_name()} executed by {driver.execute}"
            )
            new_service = self.create_service(
                driver.service_type(),
                driver.service_name(),
                lambda request, response, execute=driver.execute: execute(
                    request, response, self.tbot
                ),
            )
            self.button_services[driver_name] = new_service

        self.light_services = {}
        for driver_name, driver in inspect.getmembers(Lights, inspect.isclass):
            if driver.__module__ != Lights.__name__:
                continue
            if driver is StaticRobotService:
                continue
            if not issubclass(driver, StaticRobotService):
                raise ValueError(f"{driver} is not a subclass of {StaticRobotService}")
            self.logger.info(
                f"Creating service of type {driver.service_type()} with name {driver.service_name()} executed by {driver.execute}"
            )
            new_service = self.create_service(
                driver.service_type(),
                driver.service_name(),
                lambda request, response, execute=driver.execute: execute(
                    request, response, self.tbot
                ),
            )
            self.light_services[driver_name] = new_service

        self.distance_publisher = self.create_publisher(Float32, "distance", 10)
        self.distance_timer = self.create_timer(
            DISTANCE_PUBLISH_PERIOD, self.publish_distance
        )

        self.button_states_publisher = self.create_publisher(
            GetButtonsState.Response, "button_states", 10
        )
        self.button_states_timer = self.create_timer(
            BUTTON_STATES_PUBLISH_PERIOD, self.publish_button_states
        )

        self.logger.info(("Trilobot driver ready"))

    def publish_distance(self):
        msg = Float32()
        msg.data = self.tbot.read_distance()
        self.distance_publisher.publish(msg)

    def publish_button_states(self):
        msg = GetButtonsState.Response()
        msg.buttons = [self.tbot.read_button(i) for i in range(4)]
        self.button_states_publisher.publish(msg)
