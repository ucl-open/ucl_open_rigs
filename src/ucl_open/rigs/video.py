from typing import Union
from pydantic import Field
from swc.aeon.rigs.video import SpinnakerCamera
from ucl_open.rigs.base import BaseSchema

class CameraModule(BaseSchema) : 
    Union[SpinnakerCamera]

class CameraAcquisition(BaseSchema):
    """Represents the CameraAcquisition workflow module, with or without a trigger subject input."""

    camera: CameraModule = Field(description="Configuration for the camera used by the CameraAcquisition workflow.")
