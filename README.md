ddsc-test-client
================

A client to test the socket

This client does a job to read a csv file line by line and in the mean time send them to the socket server. Thus, a csv file need to be prepared before we can use it. 

The csv file should be the same format as the csv contains the time series.

For the settings file.

host: 'xxx.xxx.xxx.xx',  # socket server host
port:
test_file_dst: '/home/user/testdata/socket/xxx.csv',
timeout: 200

