"""Device handler for hivehome.com MOT003 sensors."""
import logging
from zigpy.profiles import zha
from zigpy.zcl.clusters.general import (
    Basic, Identify, PollControl, Ota, PowerConfiguration
)
from zigpy.zcl.clusters.security import IasZone
from zigpy.zcl.clusters.measurement import (
    TemperatureMeasurement, OccupancySensing
)
from zigpy.quirks import CustomDevice
from . import MotionCluster

_LOGGER = logging.getLogger(__name__)


class MOT003(CustomDevice):
    """hivehome.com MOT003."""

    signature = {
        #  <SimpleDescriptor endpoint=6 profile=260 device_type=1026
        # device_version=0
        # input_clusters=[0, 1, 3, 32, 1026, 1030, 1280]
        # output_clusters=[25]>
        6: {
            'manufacturer': 'HiveHome.com',
            'model': 'MOT003',
            'profile_id': zha.PROFILE_ID,
            'device_type': zha.DeviceType.IAS_ZONE,
            'input_clusters': [
                Basic.cluster_id,
                PowerConfiguration.cluster_id,
                Identify.cluster_id,
                PollControl.cluster_id,
                TemperatureMeasurement.cluster_id,
                OccupancySensing.cluster_id,
                IasZone.cluster_id,
            ],
            'output_clusters': [
                Ota.cluster_id
            ],
        }
    }

    replacement = {
        'endpoints': {
            6: {
                'input_clusters': [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    PollControl.cluster_id,
                    TemperatureMeasurement.cluster_id,
                    OccupancySensing.cluster_id,
                    MotionCluster,
                ],
                'output_clusters': [
                    Ota.cluster_id
                ],
            }
        },
    }