from trilobot_core.drivers.abstract_driver import StaticRobotService
from trilobot_interfaces.srv import SetUnderlight
from trilobot import Trilobot

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
import trilobot_core.drivers.motors as Motors


class DriverService(Node):
    motor_drivers = Motors.__dict__

    def __init__(self):
        super().__init__("driver_service")
        self.logger = self.get_logger()
        self.logger.info("Preparing trilobot")
        self.tbot = Trilobot()
        self.srv = self.create_service(
            SetUnderlight, "set_underlight", self.set_underlight_callback
        )

        self.motor_services = {}
        for driver_name, driver in self.motor_drivers.items():
            if not issubclass(driver, StaticRobotService):
                raise ValueError("")
            new_service = self.create_service(
                driver.service_type(), driver.service_name(), driver.execute  # type: ignore
            )
            self.motor_services[driver_name] = new_service

        self.logger.info(("Trilobot driver ready"))

    def set_underlight_callback(
        self, request: SetUnderlight.Request, response: SetUnderlight.Response
    ) -> SetUnderlight.Response:
        self.logger.info("Recieved set colour request")
        colour = (request.colour.red, request.colour.green, request.colour.blue)
        self.tbot.fill_underlighting(colour)
        response.success = True
        self.logger.info("Executed set colour request")
        return response

    def set_underlight():
        pass

    def set_underlight_hsv():
        pass

    def clear_underlight():
        pass

    def fill_underlighting():
        pass

    def fill_underlighting_hsv():
        pass

    def clear_underlighting():
        pass

    def set_underlights():
        pass

    def set_underlights_hsv():
        pass

    def clear_underlights():
        pass

    def show_underlighting():
        pass

    def disable_underlighting():
        pass

    def read_distance():
        pass

    def get_buttons_state():
        pass

    def set_button_led():
        pass

    def set_button_led_brightness():
        pass


def main():
    try:
        with rclpy.init():
            driver_service = DriverService()

            rclpy.spin(driver_service)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == "__main__":
    main()
