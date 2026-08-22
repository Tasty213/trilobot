from trilobot_interfaces.msg import Colour
from trilobot_interfaces.srv import SetUnderlight
from trilobot import Trilobot

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

class DriverService(Node):

    def __init__(self):
        super().__init__('driver_service')
        self.logger = self.get_logger()
        self.logger.info("Preparing trilobot")
        self.tbot = Trilobot()
        self.srv = self.create_service(SetUnderlight, 'set_underlight', self.set_underlight_callback)
        self.logger.info(("Trilobot driver ready"))

    def set_underlight_callback(self, request: SetUnderlight.Request, response: SetUnderlight.Response):
        self.logger.info("Recieved set colour request")
        colour = (request.colour.red, request.colour.green, request.colour.blue)
        self.tbot.fill_underlighting(colour)
        response = True
        self.logger.info("Executed set colour request")
        return response


def main():
    try:
        with rclpy.init():
            driver_service = DriverService()

            rclpy.spin(driver_service)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
