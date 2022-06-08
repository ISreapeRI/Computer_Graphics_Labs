from typing import Union

import numpy as np


class Transform3D:
    @staticmethod
    def GetRotateXMatrix(Angle: Union[float, int]):

        # Поворот по оси X

        AngleX = Angle / 180 * np.pi

        R = np.array([
            [1, 0, 0, 0],
            [0, np.cos(AngleX), np.sin(AngleX), 0],
            [0, -np.sin(AngleX), np.cos(AngleX), 0],
            [0, 0, 0, 1]
        ])

        return R

    @staticmethod
    def GetRotateYMatrix(Angle: Union[float, int]):

        # Поворот по оси y

        AngleY = Angle / 180 * np.pi

        R = np.array([
            [np.cos(AngleY), 0, -np.sin(AngleY), 0],
            [0, 1, 0, 0],
            [np.sin(AngleY), 0, np.cos(AngleY), 0],
            [0, 0, 0, 1]
        ])

        return R
