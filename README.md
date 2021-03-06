# RPC-FPGA-NETWORK
A TCP client-server implemenation in python.


## Purpose
The purpose of the TCP client-server is to transmit an adjacency matrix to the server, along with several updates corresponding to position changes in a distributed robotic system. The server communicates with the FPGA onboard the PYNQ board. 

## Usage
To run the server
`python server.py`

To run the client
`python client.py`