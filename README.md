
# Python-PLC Diagnostics

## General Description

The **AD S7 Diagnostics** is a Python application designed to connect to a Siemens PLC (Programmable Logic Controller) using the Snap7 library and PySimpleGUI for the user interface. This script allows for quick diagnostics of a machine connected to a Siemens PLC by providing an intuitive interface to monitor and interact with various PLC variables.

## Purpose

The primary purpose of this script is to simplify the diagnostic process for machines controlled by Siemens PLCs. It provides a user-friendly interface that allows users to read and write boolean values, integer values, and strings within the PLC's data block. When configured correctly, this script can offer a faster and more convenient alternative to using Siemens TIA Portal for basic diagnostic tasks.

## How It Works

1.  **Initial Connection**:
    
    -   The script starts by creating a connection window where the user can input the IP address and connection details of the Siemens PLC. It validates the IP address and attempts to establish a connection to the PLC.
    - 
2.  **Main Interface**:
    
    -   Once the connection is established, the main diagnostic interface is displayed.
    -   The interface allows the user to monitor and modify boolean values, integer values, and a string within the PLC's data block provided as Lib with this script. **NOTE: When using provided DB, please remember that DB optimization must be disabled**
    -   The "PLC to PC" section displays the current state of boolean values and integer values received configured to be used by PLC for diagnostics.
    -   The "PC to PLC" section allowes to edit values configured in PLC as needed by programmer.
   
3.  **Variable types**:
    
    -   Boolean Values: Users can toggle boolean values in the interface, and changes can be sent back to the PLC.
    -   Integer Values: Users can input integer values, validate them, and send them to the PLC.
    -   String Value: Users can input strings within a specified length limit and send them to the PLC.
    - 
4.  **Connection Monitoring**:
    -   The script continuously monitors the PLC connection status. If the connection is lost, it provides a notification.
    
5.  **Exiting the Script**:
    
    -   Users can close the script window by clicking the "Cancel" button or the window's close button (X).

## To Do

Possible future enhancements or changes to consider:

-   Adding a logging feature to record interactions during diagnostics

## Note

This script is intended for basic diagnostic purposes. It was made to help me with my work. It is faster to use it than Tia Portal in some specific situations that I encountered. It can be use as basis to make some very basic MES I suppose. 

## License

[MIT License](https://opensource.org/licenses/MIT)