from unittest.mock import Mock

import pytest


@pytest.fixture()
def sensor():
    cave = Mock()
    sensor=Sensor(8,7,cave)
    return sensor


def test_signal_part2(sensor):
    line = 10
    maxsize = 10
    sensor.distance =10
    a, b = sensor.signal_part2(line, maxsize)
    assert a == True and b == [1,10]

def test_signal_part4(sensor):
    line = 10
    maxsize = 10
    sensor.distance =20
    a, b = sensor.signal_part2(line, maxsize)
    assert a == True and b == [0,10]

def test_signal_part5(sensor):
    line = 10
    maxsize = 10
    sensor.distance =2
    a, b = sensor.signal_part2(line, maxsize)
    assert a == False and b == [0,0]

def test_signal_part3(sensor):
    beacon=Mock()
    beacon.coords={"x":20,"y":4}
    sensor.closest_beacon=beacon
    sensor.distances()
    distance=sensor.distance
    assert distance==15
