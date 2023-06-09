from abc import ABC, abstractmethod
from .wheels import SwedishWheel
from .platform import Platform
from numpy import array, cos, sin, pi, sqrt
import numpy as np


class OmniDirectinalRobot(Platform):
    """
    A class to represent an omnidirectional robot
    Each instance has 3 wheels, with 2*pi/3 radians apart

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, w_radii, first_wheel_position):
        """
        Parameters
        ----------
        first_wheel : str
            a wheel is fixed to the platforms by a polar coordinate" (l,alpha)
        w_radii : float or int
            The radii of all the wheels on the robot
        """
        wheels = []
        l, first_alpha = first_wheel_position
        for i in range(3):
            alpha = first_alpha + (2 * pi / 3) * i
            wheel = SwedishWheel(w_radii, (l, alpha))
            wheels.append(wheel)
        super().__init__(*wheels)

    @property
    def kinematics(self):
        J = []
        for wheel in self.wheels:
            J.append(wheel.J)
        J = array(J)
        return J


if __name__ == "__main__":
    pass
