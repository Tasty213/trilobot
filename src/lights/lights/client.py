import itertools
import time

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from trilobot_interfaces.srv import SetUnderlight


class LightsClientAsync(Node):
    COLOURS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    def __init__(self):
        super().__init__('lights_client_async')
        self.logger = self.get_logger()
        self.colour_cycle = itertools.cycle(self.COLOURS)
        self.timer_period = 0.3
        self.cli = self.create_client(SetUnderlight, 'set_underlight')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.timer = self.create_timer(self.timer_period, self.send_request)
        self.request = SetUnderlight.Request()
        self.logger.info("Client ready")

    def send_request(self):
        next_colour = next(self.colour_cycle)
        self.request.colour.red = next_colour.red
        self.request.colour.green = next_colour.green
        self.request.colour.blue = next_colour.blue
        self.logger.info(f"Prepared colour to send {self.request.colour}")
        return self.cli.call_async(self.request)

def main(args=None):
    try:
        with rclpy.init(args=args):
            lights_client = LightsClientAsync()
            rclpy.spin(lights_client)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()




# import time

# from trilobot import Trilobot

# """
# This example will demonstrate the RGB underlights of Trilobot,
# by making them flash in a red, green and blue sequence.
# """
# print("Trilobot Example: Flash Underlights\n")


# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# INTERVAL = 0.3  # Control the speed of the LED animation

# tbot = Trilobot()

# # Cycle R, G, B a set number of times
# while True:
#     tbot.fill_underlighting(RED)
#     time.sleep(INTERVAL)

#     tbot.fill_underlighting(GREEN)
#     time.sleep(INTERVAL)

#     tbot.fill_underlighting(BLUE)
#     time.sleep(INTERVAL)

# # Turn off underlighting
# tbot.clear_underlighting()

# print("Done")
