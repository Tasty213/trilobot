from abc import ABC, abstractmethod
from trilobot import Trilobot
from rosidl_pycommon.interface_base_classes import BaseMessage


class StaticRobotService(ABC):
    """Contract for a stateless Trilobot ROS service."""

    @classmethod
    @abstractmethod
    def service_name(cls) -> str:
        """Return the ROS service name."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def service_type(cls) -> type:
        """Return the generated ROS service type."""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def execute(
        request,
        response,
        trilobot: Trilobot,
    ) -> BaseMessage:
        """Execute the service operation."""
        raise NotImplementedError
