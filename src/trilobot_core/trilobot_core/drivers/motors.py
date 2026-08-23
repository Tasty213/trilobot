from trilobot import Trilobot
from trilobot_core.drivers.abstract_driver import StaticRobotService
from trilobot_interfaces.srv._single_speed import SingleSpeed
from trilobot_interfaces.srv._twin_speed import TwinSpeed
from trilobot_interfaces.srv._motor_speed import MotorSpeed
from std_srvs.srv import Trigger


class Forward(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "forward"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.forward(request.speed.speed)
        response.success = True
        return response


class Backward(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "backward"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.backward(request.speed.speed)
        response.success = True
        return response


class TurnLeft(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "turn_left"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.turn_left(request.speed.speed)
        response.success = True
        return response


class TurnRight(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "turn_right"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.turn_right(request.speed.speed)
        response.success = True
        return response


class CurveForwardLeft(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "curve_forward_left"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.curve_forward_left(request.speed.speed)
        response.success = True
        return response


class CurveForwardRight(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "curve_forward_right"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.curve_forward_right(request.speed.speed)
        response.success = True
        return response


class CurveBackwardLeft(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "curve_backward_left"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.curve_backward_left(request.speed.speed)
        response.success = True
        return response


class CurveBackwardRight(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "curve_backward_right"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.curve_backward_right(request.speed.speed)
        response.success = True
        return response


class Stop(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "stop"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.stop()
        response.success = True
        return response


class Coast(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "coast"

    @classmethod
    def service_type(cls) -> type[Trigger]:
        return Trigger

    @staticmethod
    def execute(
        request: Trigger.Request,
        response: Trigger.Response,
        trilobot: Trilobot,
    ):
        trilobot.coast()
        response.success = True
        return response


class SetLeftSpeed(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_left_speed"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_left_speed(request.speed.speed)
        response.success = True
        return response


class SetRightSpeed(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_right_speed"

    @classmethod
    def service_type(cls) -> type[SingleSpeed]:
        return SingleSpeed

    @staticmethod
    def execute(
        request: SingleSpeed.Request,
        response: SingleSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_right_speed(request.speed.speed)
        response.success = True
        return response


class SetMotorSpeeds(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_motor_speeds"

    @classmethod
    def service_type(cls) -> type[TwinSpeed]:
        return TwinSpeed

    @staticmethod
    def execute(
        request: TwinSpeed.Request,
        response: TwinSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_motor_speeds(request.speed_left.speed, request.speed_right.speed)
        response.success = True
        return response


class SetMotorSpeed(StaticRobotService):
    @classmethod
    def service_name(cls) -> str:
        return "set_motor_speeds"

    @classmethod
    def service_type(cls) -> type[MotorSpeed]:
        return MotorSpeed

    @staticmethod
    def execute(
        request: MotorSpeed.Request,
        response: MotorSpeed.Response,
        trilobot: Trilobot,
    ):
        trilobot.set_motor_speed(request.motor, request.speed.speed)
        response.success = True
        return response
