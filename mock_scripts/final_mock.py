"""
HealthData Labeling System
==========================

Mockup for final presentation

To better understand what's going on here, please see our video on youtube.
"""


from __future__ import annotations
from multiprocessing import Pipe, Process
from time import sleep

from design_tools import colored
from raw_data import RawData


def main():
    """
    Provide main functionality
    ==========================
    """

    # pylint: disable=import-outside-toplevel
    #         Function level import is the only way in Python to be resource
    #         effective while multiprocessing.

    from time import strftime

    def timeprint(text : str):
        """
        Print text with a leading timestamp

        Parameters
        ----------
        text : str
            Text to print.
        """

        print('{} {}'.format(strftime('%Y-%m-%d %H:%M:%S'), text))


    print('-' * 43)
    print('{} mockup workflow'.format(colored('HealthData Labelling System',
                                              'cyan')))
    print('-' * 43)
    request_receiver, request_sender = Pipe()
    devices = Process(target=mock_devices, args=(request_sender, ))
    devices.start()
    print('HDLSServer is {}.'.format(colored('running', 'green')))
    keep_running = True
    while keep_running:
        hdls_requests = []
        while request_receiver.poll():
            hdls_requests.append(request_receiver.recv())
        for _request in hdls_requests:
            if _request['endpoint'] == 'register':
                timeprint('Registering {}'
                          .format(colored(_request['data']['product_type'],
                                          'white')))
                print(' ' * 20, end='')
                print('{} by {}'.format(colored(
                                        _request['data']['product_name'],
                                        'cyan'),
                                        colored(
                                        _request['data']['service_provider'],
                                        'yellow')))
                print(' ' * 20, end='')
                print('uses {} {} provides {}'
                      .format(colored(
                              _request['data']['hdls_platform'], 'yellow'),
                              colored('{}.{}.{}-{}'
                              .format(*_request['data']['hdls_version']),
                              'white'),
                              colored(' '.join(
                              _request['data']['hdls_data_types']), 'cyan')))
            elif _request['endpoint'] == 'store':
                timeprint('{} received {} elements as {} from {} to a user.'
                          .format(colored('<-', 'green'),
                          colored(len(_request['data']['datapoints']), 'cyan'),
                          colored(_request['data']['hdls_data_type'], 'white'),
                          colored(_request['data']['product_name'], 'yellow')))
            elif _request['endpoint'] == 'get':
                timeprint('{} sent {} elements to {} by request'
                          .format(colored('->', 'red'),
                          colored(_request['data']['amount'], 'yellow'),
                          colored(_request['data']['product_name'], 'cyan')))
            elif _request['endpoint'] == 'stop':
                keep_running = False
                sleep(0.5)
                print('HDLSServer is {}.'.format(colored('stopping', 'red')))
                print('Demo finished. Bye.')
                sleep(0.1)
            else:
                timeprint('Invalid endpoint "{}"!'
                          .format(colored(_request['endpoint'], 'red')))


def mock_devices(data_pipe : multiprocessing.connection.PipeConnection):
    """
    Mock devices
    ============

    Parameters
    ----------
    data_pipe : multiprocessing.connection.PipeConnection
        Data stream input to send collected (mocked) data.
    """

    # pylint: disable=undefined-variable
    #         PyLint cannot understand to workflow of annotations from future.

    # pylint: disable=import-outside-toplevel
    #         Function level import is the only way in Python to be resource
    #         effective while multiprocessing.

    from random import choice, randint


    def get_some_data(entity : dict, amount : int, sleep_time : float):
        """
        Get som data for an entity
        ==========================

        Parameters
        ----------
        entity : dict
            The entity to get data for.
        amount : int
            Amount of elements to get.
        sleep_time : float, optional (0.2 if omitted)
            Sleep time after the process is sent in seconds.
        """

        package = {}
        package['endpoint'] = 'get'
        package['data'] = {'product_name' : entity['product_name'],
                           'amount' : amount}
        data_pipe.send(package)
        sleep(sleep_time)


    def loop(loop_count : int, sleep_time : float, consumers : list = None):
        """
        Make data loop
        ==============

        Parameters
        ----------
        loop_count : int
            Number of loops to make.
        sleep_time : float
            Number of seconds to sleep between events.
        consumers : list, optional (None if omitted)
            List of entities who can get random amount of data.
        """

        for i in range(loop_count):
            selected_device = choice(available_devices)
            datapoints = [RawData(smart_bracelet['device']['id'],
                                  'sensor', 'mock')
                          for e in range(randint(5, 50))]
            send_some_data(selected_device, datapoints,
                           choice(selected_device['hdls_data_types']),
                           sleep_time)
            if consumers is not None and choice([True, False]):
                get_some_data(choice(consumers), randint(5, 20), 0.0)


    def register(entity : dict, sleep_time : float = 0.2):
        """
        Register an entity
        ==================

        Parameters
        ----------
        entity : dict
            The entity to register.
        sleep_time : float, optional (0.2 if omitted)
            Sleep time after the registration in seconds.
        """

        package = {}
        package['endpoint'] = 'register'
        package['data'] = entity
        data_pipe.send(package)
        sleep(sleep_time)


    def register_and_loop(loop_count : int, sleep_time : float,
                          consumers : list = None):
        """
        Register new device and make data loop
        ======================================

        Parameters
        ----------
        loop_count : int
            Number of loops to make.
        sleep_time : float
            Number of seconds to sleep between events.
        consumers : list, optional (None if omitted)
            List of entities who can get random amount of data.
        """

        register(available_devices[-1])
        loop(loop_count, sleep_time, consumers)


    def send_some_data(entity : dict, data_points : list, data_type : string,
                       sleep_time : float = 0.2):
        """
        Send some data
        ==============

        Parameters
        ----------
        entity : dict
            The entity to get data for.
        data_points : list
            List of data points.
        data_type : string
            HDLS data type of the data points.
        sleep_time : float, optional (0.2 if omitted)
            Sleep time after the data is sent in seconds.
        """

        package = {}
        package['endpoint'] = 'store'
        package['data'] = {'datapoints' : data_points,
                           'hdls_data_type' : data_type,
                           'product_name' : entity['product_name'],
                           'user' : {}}
        data_pipe.send(package)
        sleep(sleep_time)

    smart_bracelet = {'product_name' : 'Smart Bracalet',
                      'product_type' : 'device',
                      'manufacturer' : 'EU Startup #1',
                      'service_provider' : 'EU Startup #1',
                      'hdls_platform' : 'C++',
                      'hdls_version' : [0, 0, 2, 'final'],
                      'hdls_data_types' : ['raw_data'],
                      'device' : {'id' : 'eusmblet_01234'}}
    smart_ring = {'product_name' : 'Smart Ring',
                  'product_type' : 'device',
                  'manufacturer' : 'EU Startup #2',
                  'service_provider' : 'EU Startup #2',
                  'hdls_platform' : 'Java',
                  'hdls_version' : [0, 0, 1, 'final'],
                  'hdls_data_types' : ['raw_data', 'foreign_data'],
                  'device' : {}}
    smart_service = {'product_name' : 'Gym Service',
                     'product_type' : 'service',
                     'manufacturer' : 'not_relevant',
                     'service_provider' : 'Challenge Sponsor',
                     'hdls_platform' : 'Python',
                     'hdls_version' : [0, 0, 3, 'alpha'],
                     'hdls_data_types' : ['foreign_data'],
                     'service' : {}}
    other_service = {'product_name' : 'Augmented Data in my Country',
                     'product_type' : 'service',
                     'manufacturer' : 'not_relevant',
                     'service_provider' : 'EU Startup #3',
                     'hdls_platform' : 'Python',
                     'hdls_version' : [0, 0, 2, 'final'],
                     'hdls_data_types' : ['labeled_data'],
                     'service' : {}}
    hospital_screening = {'product_name' : 'Foreign Country Screening',
                          'product_type' : 'service',
                          'manufacturer' : 'not_relevant',
                          'service_provider' : 'Foreign Country Hospital',
                          'hdls_platform' : 'Python',
                          'hdls_version' : [0, 0, 2, 'final'],
                          'hdls_data_types' : ['raw_data'],
                          'service' : {'id' : 'screening_1'}}
    hospital_ai = {'product_name' : 'Bone Fractures Hunter AI',
                   'product_type' : 'service',
                   'manufacturer' : 'not_relevant',
                   'service_provider' : 'European AI Provider',
                   'hdls_platform' : 'Python',
                   'hdls_version' : [0, 0, 2, 'final'],
                   'hdls_data_types' : ['foreign_data'],
                   'service' : {'model' : 'best_predictor'}}
    doctor_1 = {'product_name' : 'Dr. Bone',
                'product_type' : 'personal_service',
                'manufacturer' : 'not_relevant',
                'service_provider' : 'Dr. Bone\'s Surgery',
                'hdls_platform' : 'Java',
                'hdls_version' : [0, 0, 1, 'final'],
                'hdls_data_types' : ['foreign_data'],
                'service' : {'person' : 'Dr. Bone'}}
    doctor_2 = {'product_name' : 'Dr. Fracture',
                'product_type' : 'personal_service',
                'manufacturer' : 'not_relevant',
                'service_provider' : 'Dr. Fracture\'s Surgery',
                'hdls_platform' : 'Java',
                'hdls_version' : [0, 0, 1, 'final'],
                'hdls_data_types' : ['foreign_data'],
                'service' : {'person' : 'Dr. Fracture'}}
    doctor_3 = {'product_name' : 'Dr. Neuron',
                'product_type' : 'personal_service',
                'manufacturer' : 'not_relevant',
                'service_provider' : 'Dr. Neuron\'s Surgery',
                'hdls_platform' : 'Java',
                'hdls_version' : [0, 0, 1, 'final'],
                'hdls_data_types' : ['foreign_data'],
                'service' : {'person' : 'Dr. Neuron'}}
    available_devices = [smart_bracelet]
    register_and_loop(5, 1)
    available_devices.append(smart_ring)
    register_and_loop(10, 0.5)
    available_devices.append(smart_service)
    register_and_loop(10, 0.5)
    available_devices.append(other_service)
    data_consumers = [other_service]
    register_and_loop(10, 0.5, data_consumers)
    register(hospital_screening)
    send_some_data(hospital_screening, [
                   RawData(hospital_screening['service']['id'], 'prediction',
                   'mock')], 'foreign_data')
    available_devices.append(hospital_screening)
    register(hospital_ai)
    available_devices.append(hospital_ai)
    register(hospital_ai)
    register(doctor_1)
    register(doctor_2)
    register(doctor_3)
    get_some_data(hospital_ai, 1, 0.4)
    send_some_data(hospital_ai, [RawData(hospital_ai['service']['model'],
                                         'prediction', 'mock')], 'foreign_data')
    get_some_data(doctor_1, 1, 0.4)
    send_some_data(hospital_ai, [RawData(doctor_1['service']['person'],
                                         'opinion', 'mock')], 'foreign_data')
    get_some_data(doctor_2, 1, 0.4)
    send_some_data(hospital_ai, [RawData(doctor_2['service']['person'],
                                         'opinion', 'mock')], 'foreign_data')
    get_some_data(doctor_3, 2, 0.4)
    send_some_data(hospital_ai, [RawData(doctor_3['service']['person'],
                                         'opinion', 'mock')], 'foreign_data')
    loop(50, 0.25, data_consumers)
    package = {}
    package['endpoint'] = 'stop'
    data_pipe.send(package)


if __name__ == '__main__':
    main()
