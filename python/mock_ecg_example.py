"""
HealthData Labeling System
==========================

module: mock ECG example
"""


# Imports from standard library
from json import dumps
from random import choice, uniform
from time import sleep, time

# Project level imports
from enum_label_types import LabelTypes
from enum_measures import Measures
from enum_origins import Origins
from hdls_data_object import HDLSDataObject
from raw_collector import RawCollector
from raw_data import RawData


# In our example we model an ECG bracelet which has the following workflow
#   - It measure blood pressure with unknown frequency and sends two packages
#     of data in every minute.
#   - Packages contian 3 strings and 3 floats in the order of str, float, str,
#     float, str, float where str is the sensor ID, and float is the value that
#     belongs to the given sensor.
#   - Blood pressure sensros sends mean of blood pressure by the given tack
#     state.
#   - Heart rare sensros sends mean of heart rate.
#   - Tack sensro sends the value 1.0 if blood pressure data is the lowest
#      value at the beginning of an increasing period and 0.0 if blood pressure
#      data is the highest value at the beginning of a decreasing period.


# Device related constants
BLOOD_PRESSURE_SENSROR_ID = 'bps001'
DEVICE_ID = 'mybracelet'
HEARTH_RATE_SENSOR_ID = 'hrs001'
TACK_SENSOR_ID = 'tcks001'

# Test related constants
TEST_DURATION = 100
TEST_PACKAGES_PER_UNIT = 2 # If the reason is not clear, see descripiton above.
TEST_SAMPLE_LABELED = 5


# Mock ECG bracelet device
class ECGBracelet:
    """
    Provide mock ECG bracelet
    =========================
    """


    def __init__(self):
        """
        Initialize the object
        =====================
        """

        self.__first_in_minute = True
        self.__timestamp = int(time()) - 86400 # one day backward from now
        self.__tack_state = 0.0


    def get_package(self) -> tuple:
        """
        Mock packages from bracelet
        ===========================

        Returns
        -------
        tuple(int, tuple(str, float), tuple(str, float), tuple(str, float))
            Package data.
        """

        timestamp = self.__timestamp
        if self.__first_in_minute:
            self.__first_in_minute = False
            self.__tack_state = choice([0.0, 1.0])
        else:
            self.__first_in_minute = True
            self.__tack_state = 0.0 if self.__tack_state == 1.0 else 1.0
            self.__timestamp += 60
        hearth_rate = uniform(50.0, 110.0)
        if self.__tack_state == 0.0:
            blood_pressure = uniform(105.0, 125.0)
        else:
            blood_pressure = uniform(75.0, 85.0)
        return (timestamp, (BLOOD_PRESSURE_SENSROR_ID, blood_pressure),
                           (HEARTH_RATE_SENSOR_ID, hearth_rate),
                           (TACK_SENSOR_ID, self.__tack_state))


# Simple HealthData Labeling System collector to the mock device
class MyCollector(RawCollector):
    """
    Proved ECG bracelet raw data collector
    ======================================
    """

    def collect(self, device_id : any, source_id : any, data : any,
                timestamp : int = 0, time_section : int = 0):
        """
        Collect data from device

        Parameters
        ----------
        device_id : any (in fact str)
            Device ID of the signaling device.
        source_id : any (in fact str)
            Source ID of the signal. (Source ID relaitve to the device.)
        data : any (in fact float)
            Data of the signal.
        timestamp : int, optional (0 if omitted)
            Timestamp of the registration of the signal. If 0 is given, the
            signal gets registered to the call of the function. Timestamp is
            second precision value.
        time_section int, optional (0 if omitted)
            Time section of the signal. This value can be used to add
            millisencond precision to timestamp or to mark various series of
            data at the same time.

        Notes
        -----
        I.
            Expected worklof of this functiun is to convert parameters into
            RawData object and add RawData object to the end of the container
            self.__content.
        II.
            To fit the requirements of HealthData Labeling System device_id,
            source_id and data parameters should be converted to string.
        III.
            Tha final content of data must be a JSON compatible string to
            provide flexible usability. In most cases this means the use of
            dumps() function from the json standard library but unique solutions
            also can be reasonable.
        """

        self._content.append(RawData(device_id, source_id, str(data),
                                     timestamp, time_section))


# Instantiate device and collector
my_bracelet = ECGBracelet()
my_collector = MyCollector()


# Collect some data
print('\n\n\n#########################')
print('# Collecting test data. #')
print('#########################\n\n\n')
sleep(0.1)

for i in range(TEST_DURATION):
    for j in range(TEST_PACKAGES_PER_UNIT):
        package = my_bracelet.get_package()
        _timestamp = package[0]
        for k in range(1, 4): # Tuple elements 1-3 contains sensros data
            my_collector.collect(DEVICE_ID, *package[k], _timestamp, j)
        if i % 25 == 24:
            print('Sampling at test measure {}:'.format(i + 1))
            sleep(0.05)
            print('--- Data #1: {}'.format(my_collector.get_by_id(-3)))
            sleep(0.05)
            print('--- Data #2: {}'.format(my_collector.get_by_id(-2)))
            sleep(0.05)
            print('--- Data #3: {}'.format(my_collector.get_by_id(-1)))
            sleep(0.1)


# Labeling
#
# In the final code it will hava its own class but now it is just a proof of
# concept only.
print('\n\n\n#######################')
print('# Labeling test data. #')
print('#######################\n\n\n')
sleep(0.1)


# This whole stuff in that for loop could be made in the collection phase and
# it is much easier to make it there. We separated it for demonstrational use
# only.
fails = 0
labaled_datapoints = []
for i in range(TEST_DURATION):
    raw_datapoints = my_collector.get(i * 6, (i + 1) * 6)
    # Test timestamps
    if len(set([e.timestamp for e in raw_datapoints])) != 1:
        fails += 1
        continue
    _timestamp = raw_datapoints[0].timestamp
    # Separate systolic and diastolic data
    _tack_state_1 = None
    _blood_pressure_1 = None
    for j in range(3):
        if raw_datapoints[j].source_id == TACK_SENSOR_ID:
            _tack_state_1 = float(raw_datapoints[j].data)
        if raw_datapoints[j].source_id == BLOOD_PRESSURE_SENSROR_ID:
            _blood_pressure_1 = float(raw_datapoints[j].data)
    # Test tack data
    if _tack_state_1 is None:
        fails += 1
        continue
    if _blood_pressure_1 is None:
        fails += 1
        continue
    _tack_state_2 = None
    _blood_pressure_2 = None
    for j in range(3, 6):
        if raw_datapoints[j].source_id == TACK_SENSOR_ID:
            _tack_state_2 = float(raw_datapoints[j].data)
        if raw_datapoints[j].source_id == BLOOD_PRESSURE_SENSROR_ID:
            _blood_pressure_2 = float(raw_datapoints[j].data)
    # Test tack data
    if _tack_state_2 is None:
        fails += 1
        continue
    if _blood_pressure_2 is None:
        fails += 1
        continue
    if _tack_state_1 == _tack_state_2:
        fails += 1
        continue
    if _tack_state_1 == 0.0:
        _systolic_value = _blood_pressure_1
        _diastolic_value = _blood_pressure_2
    else:
        _systolic_value = _blood_pressure_2
        _diastolic_value = _blood_pressure_1
    # Test systolic diastolic values - IN REAL LIFE THIS TEST IS NOT VALID
    if _diastolic_value > _systolic_value:
        fails += 1
        continue
    # Get the mean of hearth rates
    _hearth_rate = 0.0
    _count = 0
    for datapoint in raw_datapoints:
        if datapoint.source_id == HEARTH_RATE_SENSOR_ID:
            _hearth_rate += float(datapoint.data)
            _count += 1
    # Test count of hearth rate sensor data
    if _count != 2:
        fails += 1
        continue
    _hearth_rate /= 2.0 # Simple mean.
    # If we are here we can start labeling
    # In this approach we use complex datapoint therefore we use Measures.DATA
    _data = {'systolic' : _systolic_value, 'diastolic' : _diastolic_value,
             'hearth rate' : _hearth_rate}
    _data_object = HDLSDataObject(name='mock_data_{:03d}'.format(i),
                                  measure=Measures.DATA, origin=Origins.RAW)
    _data_object.value = dumps(_data)
    # Let's add some labeling
    _data_object.add_label(name='received at', type=LabelTypes.TIME,
                           value=str(_timestamp))
    _data_object.add_label(name='data length', type=LabelTypes.DATA,
                           value=str(3))
    _data_object.add_label(name='data form', type=LabelTypes.DATA,
                           value='key value pairs')
    _data_object.add_label(name='produced by', type=LabelTypes.LIFECYCLE,
                           value='test auto-diagnosis from raw')
    _data_object.add_label(name='general', type=LabelTypes.CONTEXT,
                           value='bracelet mock')
    _auto_diagnosis_1 = 'normal'
    if _systolic_value > 120.0:
        _auto_diagnosis_1 = 'elevated'
    if _diastolic_value > 80.0:
        _auto_diagnosis_1 = 'high'
    _data_object.add_label(name='auto_diagnois.blood_pressure', type=LabelTypes.CONTEXT,
                           value=_auto_diagnosis_1)
    _auto_diagnosis_2 = 'normal'
    if _hearth_rate > 100.0:
        _auto_diagnosis_2 = 'high'
    _data_object.add_label(name='auto_diagnois.hearth_rate', type=LabelTypes.CONTEXT,
                           value=_auto_diagnosis_2)
    labaled_datapoints.append(_data_object)

print('Labeling finished with {} fails.'.format(fails))

# Sample labeled datapoints
print('\n\n\n###############################')
print('# Sampling labeled datapoints #')
print('###############################\n\n\n')
sleep(0.1)


for i in range(TEST_SAMPLE_LABELED):
    print('Sample #{}'.format(i + 1))
    datapoint = choice(labaled_datapoints)
    print(datapoint)
    sleep(0.1)
