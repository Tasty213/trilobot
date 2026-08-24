import trilobot_core.drivers.lights as Lights
import trilobot_core.drivers.motors as Motors
from rclpy.node import Node
from trilobot import Trilobot
from trilobot_core.drivers.abstract_driver import StaticRobotService


import inspect


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

        self.logger.info(("Trilobot driver ready"))

    def read_distance():
        pass

    def get_buttons_state():
        pass

    def set_button_led():
        pass

    def set_button_led_brightness():
        pass
