import unittest

import qcodes
import qtt.data
import qtt.measurements.scans
import qtt.simulation.virtual_dot_array
from qtt.measurements.videomode_processor import DummyVideoModeProcessor
from qtt.measurements.videomode import VideoMode


class TestVideoModeProcessor(unittest.TestCase):


    def test_DummyVideoModeProcessor(self):
        station = qtt.simulation.virtual_dot_array.initialize()
        dummy_processor = DummyVideoModeProcessor(station)
        vm = VideoMode(station, Naverage=25, diff_dir=None, verbose=1,
                       nplots=1, dorun=False, videomode_processor=dummy_processor)
        vm.updatebg()
        datasets = vm.get_dataset()

        self.assertIsInstance(datasets[0], qcodes.DataSet)

