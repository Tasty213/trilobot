from trilobot import Trilobot
from trilobot_core.drivers.abstract_driver import StaticRobotService
from trilobot_interfaces.srv import (
    GetButtonsState,
    SetButtonLed,
    SetButtonLedBrightness,
)


class GetButtonsStateService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "get_buttons_state"

    @classmethod
    def service_type(cls) -> type[GetButtonsState]:
        return GetButtonsState

    @staticmethod
    def execute(
        request: GetButtonsState.Request,
        response: GetButtonsState.Response,
        trilobot: Trilobot,
    ):
        response.buttons = [trilobot.read_button(i) for i in range(4)]
        return response


class SetButtonLedService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_button_led"

    @classmethod
    def service_type(cls) -> type[SetButtonLed]:
        return SetButtonLed

    @staticmethod
    def execute(
        request: SetButtonLed.Request,
        response: SetButtonLed.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_button_led(request.button, request.value)
        response.success = True
        return response


class SetButtonLedBrightnessService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_button_led_brightness"

    @classmethod
    def service_type(cls) -> type[SetButtonLedBrightness]:
        return SetButtonLedBrightness

    @staticmethod
    def execute(
        request: SetButtonLedBrightness.Request,
        response: SetButtonLedBrightness.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_button_led(request.button, request.brightness)
        response.success = True
        return response
