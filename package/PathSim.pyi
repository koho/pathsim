from typing import Any

class PathSim:
    """
    FreeCAD python wrapper of CAMSimulator
    """

    def BeginSimulation(self, **kwargs) -> Any:
        """
        BeginSimulation(stock, resolution):

                  Start a simulation process on a box shape stock with given resolution"""
        ...

    def ResetSimulation(self) -> Any:
        """
        ResetSimulation():

                  Clear the simulation and all gcode commands"""
        ...

    def AddTool(self, **kwargs) -> Any:
        """
        AddTool(shape, toolnumber, diameter, resolution):

                  Set the shape of the tool to be used for simulation"""
        ...

    def SetBaseShape(self, **kwargs) -> Any:
        """
        SetBaseShape(shape, resolution):

                  Set the shape of the base object of the job"""
        ...

    def AddCommand(self, **kwargs) -> Any:
        """
        AddCommand(command):

                  Add a path command to the simulation."""
        ...

    def SetNumSamples(self, samples: int, /) -> Any:
        """
        SetNumSamples(samples):

                  Set the Anti-Aliasing modes of the rendered 3D scene."""
        ...
