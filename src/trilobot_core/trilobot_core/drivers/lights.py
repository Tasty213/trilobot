from trilobot import Trilobot
from trilobot_core.drivers.abstract_driver import StaticRobotService
from trilobot_interfaces.srv import (
    ClearUnderlight,
    ClearUnderlighting,
    DisableUnderlighting,
    FillUnderlighting,
    FillUnderlightingHex,
    FillUnderlightingHsv,
    SetUnderlight,
    SetUnderlightHex,
    SetUnderlightHsv,
    SetUnderlights,
    SetUnderlightsHex,
    SetUnderlightsHsv,
    ShowUnderlighting,
)


def _light_index(light):
    return light.index


def _light_indices(lights):
    return [_light_index(light) for light in lights]


class SetUnderlightService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_underlight"

    @classmethod
    def service_type(cls) -> type[SetUnderlight]:
        return SetUnderlight

    @staticmethod
    def execute(
        request: SetUnderlight.Request,
        response: SetUnderlight.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_underlight(
            request.light.index,
            request.colour.red,
            request.colour.green,
            request.colour.blue,
            show=request.show,
        )
        response.success = True
        return response


class SetUnderlightHsvService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_underlight_hsv"

    @classmethod
    def service_type(cls) -> type[SetUnderlightHsv]:
        return SetUnderlightHsv

    @staticmethod
    def execute(
        request: SetUnderlightHsv.Request,
        response: SetUnderlightHsv.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_underlight_hsv(
            request.light.index,
            request.colour.hue,
            request.colour.saturation,
            request.colour.value,
            show=request.show,
        )
        response.success = True
        return response


class SetUnderlightHexService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_underlight_hex"

    @classmethod
    def service_type(cls) -> type[SetUnderlightHex]:
        return SetUnderlightHex

    @staticmethod
    def execute(
        request: SetUnderlightHex.Request,
        response: SetUnderlightHex.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_underlight(
            request.light.index, request.colour.code, show=request.show
        )
        response.success = True
        return response


class SetUnderlightsService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_underlights"

    @classmethod
    def service_type(cls) -> type[SetUnderlights]:
        return SetUnderlights

    @staticmethod
    def execute(
        request: SetUnderlights.Request,
        response: SetUnderlights.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_underlights(
            _light_indices(request.lights),
            request.colour.red,
            request.colour.green,
            request.colour.blue,
            show=request.show,
        )
        response.success = True
        return response


class SetUnderlightsHsvService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_underlights_hsv"

    @classmethod
    def service_type(cls) -> type[SetUnderlightsHsv]:
        return SetUnderlightsHsv

    @staticmethod
    def execute(
        request: SetUnderlightsHsv.Request,
        response: SetUnderlightsHsv.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_underlights_hsv(
            _light_indices(request.lights),
            request.colour.hue,
            request.colour.saturation,
            request.colour.value,
            show=request.show,
        )
        response.success = True
        return response


class SetUnderlightsHexService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_underlights_hex"

    @classmethod
    def service_type(cls) -> type[SetUnderlightsHex]:
        return SetUnderlightsHex

    @staticmethod
    def execute(
        request: SetUnderlightsHex.Request,
        response: SetUnderlightsHex.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_underlights(
            _light_indices(request.lights), request.colour.code, show=request.show
        )
        response.success = True
        return response


class FillUnderlightingService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "fill_underlighting"

    @classmethod
    def service_type(cls) -> type[FillUnderlighting]:
        return FillUnderlighting

    @staticmethod
    def execute(
        request: FillUnderlighting.Request,
        response: FillUnderlighting.Response,
        trilobot: Trilobot,
    ):
        trilobot.fill_underlighting(
            request.colour.red,
            request.colour.green,
            request.colour.blue,
            show=request.show,
        )
        response.success = True
        return response


class FillUnderlightingHsvService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "fill_underlighting_hsv"

    @classmethod
    def service_type(cls) -> type[FillUnderlightingHsv]:
        return FillUnderlightingHsv

    @staticmethod
    def execute(
        request: FillUnderlightingHsv.Request,
        response: FillUnderlightingHsv.Response,
        trilobot: Trilobot,
    ):
        trilobot.fill_underlighting_hsv(
            request.colour.hue,
            request.colour.saturation,
            request.colour.value,
            show=request.show,
        )
        response.success = True
        return response


class FillUnderlightingHexService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "fill_underlighting_hex"

    @classmethod
    def service_type(cls) -> type[FillUnderlightingHex]:
        return FillUnderlightingHex

    @staticmethod
    def execute(
        request: FillUnderlightingHex.Request,
        response: FillUnderlightingHex.Response,
        trilobot: Trilobot,
    ):
        trilobot.fill_underlighting(request.colour.code, show=request.show)
        response.success = True
        return response


class ClearUnderlightService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "clear_underlight"

    @classmethod
    def service_type(cls) -> type[ClearUnderlight]:
        return ClearUnderlight

    @staticmethod
    def execute(
        request: ClearUnderlight.Request,
        response: ClearUnderlight.Response,
        trilobot: Trilobot,
    ):
        trilobot.clear_underlight(request.light.index, show=request.show)
        response.success = True
        return response


class ClearUnderlightingService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "clear_underlighting"

    @classmethod
    def service_type(cls) -> type[ClearUnderlighting]:
        return ClearUnderlighting

    @staticmethod
    def execute(
        request: ClearUnderlighting.Request,
        response: ClearUnderlighting.Response,
        trilobot: Trilobot,
    ):
        trilobot.clear_underlighting(show=request.show)
        response.success = True
        return response


class ShowUnderlightingService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "show_underlighting"

    @classmethod
    def service_type(cls) -> type[ShowUnderlighting]:
        return ShowUnderlighting

    @staticmethod
    def execute(
        request: ShowUnderlighting.Request,
        response: ShowUnderlighting.Response,
        trilobot: Trilobot,
    ):
        trilobot.show_underlighting()
        response.success = True
        return response


class DisableUnderlightingService(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "disable_underlighting"

    @classmethod
    def service_type(cls) -> type[DisableUnderlighting]:
        return DisableUnderlighting

    @staticmethod
    def execute(
        request: DisableUnderlighting.Request,
        response: DisableUnderlighting.Response,
        trilobot: Trilobot,
    ):
        trilobot.disable_underlighting()
        response.success = True
        return response
