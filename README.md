# AHA_Lv1_CW
## Project Synopsis
This project is used for the AHA Foundations Level 1 course in cooporation with Iolani School's Robotics Team, Team 2438, Iobotics. This module includes coursework for teaching python as well as the IoT project that will be used as a base project while learning how to code. Students will utilize the monitoring project to monitor and grow plants on a rooftop garden. 

_Note: Slides and curriculum are in sepereate documents but can be found on goolge drive. Only code and test cases for students to test their code are in this repo._

For more information about this project or how to use it, contact Shane Matsushima at shanematsushima@gmail.com

### Getting Started
This section describes the materials and software needed to create the project portion of the course as well as the course work. 

#### Course work material
Visual Studio Code must be installed on student laptops as well as the recent version of Python. Windows OS is preffered as tests are ran through .bat files, but Mac OS will be incorporated in a later update.

#### Project material
These are the supplies needed to create the project:
* RPI (Model 3 B is being used in classes but any version above this will work)
* Breadboard (This will later be swapped with a PCB / RPI Shield for easier use)
* Jumper wires
* 4.7k Ohm resistor
* DS18B20 temperature sensor
* ADC ADS1115
* ME110 moisture sensor
* Housing material (Pelican case works)

#### Blynk accounts needed
For the IoT aspect of the project, a [Blynk](Blynk.io) accout must be created as this is the IoT interface the RPI communicates with. 

#### Github
Github accounts are not required but recommended as a mean to transfer project code from laptop to RPI. If a github account is not created for a student, students may use flash drives as a mean to transfer over code. 

#### Wiring schematics
Wiring schematics can be found with the curriculum lecture slides and curriculum overview. 

## Course Overview
This course will cover the following topics:
* Introduction to Python and VSCode
* Python Variables and Data Types
* Python Loops and Lists
* Python Functions
* Python Packages and Imports
* Introduction to API's
* Introduction to IoT

Course work that coinside with specific topics can be found in this repository. 

_NOTE: Not all topics have course work as some are mainly lecture topics._ 

### Completing and testing course work
Students will complete each python script in the course directories after the section lecture has been completed. Please refer back to the curriculum documentation for specific files students should be utilizing. 

Unit tests are incorporated into the coursework, allowing students to test their completed code for correctness. Based on the section being worked on, .bat files have been created for easier use. An example to run the test in "0 Intro" run the following code in the "0 Intro" directory:
'''
test_1
'''

_NOTE: All tests pass when the OK is printed in the terminal._

## IoT Project
The IoT project is a culmination of the course work. Students will create a temperature and moisture monitoring system that will be deployed on a rooftop garden. 

### Running and setting up RPI
First, one-wire and I2C must be enabled on the RPI.
Once the OS has been installed and a default user created, open the terminal and run the following steps:
1. `sudo raspi-config` to enable one-wire and I2C
2. Once the page is open, go to Interface and enable both one-wire and I2C. Click finish once complete, the RPI may reboot once done. 
3. `sudo apt-get update` to update the RPI's package list
4. `sudo apt-get install python3-pip` to install pip for python3

Once the configuration of the RPI is complete, use the cd command to traverse through the RPI to the working directory where the project code will be held. The following steps are for setting up and running the project: 
1. `python -m venv venv` to create a virtual environment for python.
2. `chmod +x venv_start.sh` to allow the RPI to run the shell script.
3. `chmod +x temp_sensor_setup.sh` to allow the RPI to run the shell script.
4. `chmod +x run.sh` to allow the RPI to run the shell script.
5. `venv_start.sh` to activate the virtual environment we created.
6. `pip install -r requirements.txt` to install required packages for the python project.
7. Once sensors are wired to the RPI, `temp_sensor_setup.sh` must be run in order to start logging temperature data from one-wire.
8. Once code has been corrected / implemented, `run.sh` will start the main program of the project.



