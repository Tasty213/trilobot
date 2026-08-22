import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from trilobot_interfaces.srv import SetUnderlight


class LightsClientAsync(Node):

    def __init__(self):
        super().__init__('lights_client_async')
        self.logger = self.get_logger()
        self.cli = self.create_client(SetUnderlight, 'set_underlight')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetUnderlight.Request()
        self.logger.info("Client ready")

    def send_request(self, red: int, green: int, blue: int):
        self.req.colour.red = red
        self.req.colour.green = green
        self.req.colour.blue = blue
        self.logger.info("Prepared colour to send")
        return self.cli.call_async(self.req)

def send_colours(lights_client: LightsClientAsync):
    for colour in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
        future = lights_client.send_request(colour[0], colour[1], colour[2])
        rclpy.spin_until_future_complete(lights_client, future)
        lights_client.logger.info(f"Sent colour ({colour})")


def main(args=None):
    try:
        with rclpy.init(args=args):
            lights_client = LightsClientAsync()
            lights_client.logger.info("Begining loop")
            while True:
                send_colours(lights_client)
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
