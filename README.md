# Particulate Matter Monitor

![Python application](https://github.com/AndrewJanuary/PM-Monitor/workflows/Python%20application/badge.svg?branch=main) ![Mutation](https://github.com/AndrewJanuary/PM-Monitor/workflows/Mutation/badge.svg?branch=main)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AndrewJanuary/PM-Monitor)

## Overview

An air quality monitoring app.

Reads data from an [SDS011 particulate matter sensor](https://www.hackair.eu/docs/sds011/) via a serial port and uploads it to an [Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io) account.

Inspired by an [article from HackSpace magazine issue 21](https://hackspace.raspberrypi.org/issues/21) (August 2019). 

### Disclaimer

There are probably much more comprehensive and robust implementations out there for reading from the SDS011 sensor. Don't rely on this app for accurate and reliable data.

## Why

Small particulate matter less than 10 microns in diameter (PM 10) is recognised [globally by health](https://www.who.int/health-topics/air-pollution) and [environmental organisations](https://www.eea.europa.eu/themes/air) as a common contributor to air pollution.

### Health Implications of PM

Exposure to particle matter less than 2.5 microns in diameter (PM 2.5) is known to cause and contribute to respiratory and cardiovascular illness.

There is [some evidence which suggests](https://www.theguardian.com/environment/2020/apr/24/coronavirus-detected-particles-air-pollution) that high levels of PM may contribute to the transmission and lethality of COVID-19.

## Recommended hardware

- Raspberry Pi (for convenience of placing the sensor)
- [SDS011 PM sensor](https://www.hackair.eu/docs/sds011/)
- Serial to USB adapter

## Install

A python virtual environment is recommended. You can easily create a new virtual environment using venv.

`python -m venv PM-App` 

Launch the virtual environment

E.g on a Unix/Linux OS run the execute the following from the root of the repo
`source PM-App/bin/activate`

Required dependencies are defined in [requirements.txt](https://github.com/AndrewJanuary/PM-Monitor/blob/main/requirements.txt).

You can install these using pip.

`Pip install -r requirements.txt`

## AdaFruit IO

An [Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io) account and API key are required in order to upload data.

## Setup

Run `python main.py setup` to launch the setup script.

This script will prompt for input and write the following values to the config.yml file:
- AIO username
- AIO API Key
- PM 2.5 feed name in AIO account
- PM 10 feed name in AIO account

Your AIO username and API key can be found on the AIO profile page, in the `My Key` tab.
See [the AIO API docs](https://io.adafruit.com/api/docs/#adafruit-io-http-api) for more details on creating and useing API keys 

Check that the feeds exist in your AIO account before proceeding to start the app. You may need to manually creat the feeds.
Check the contents of the `config.yml` file before proceeding to start the app.

## Usage

Ensure that the PM sensor unit is connected via a USB port to the device which will run the application
Check that the device has an active network connection
Run `python main.py start` to launch the app.

Check the temrinal output to confirm that the sensor is active and the application is correctly reading and logging values
Check the AIO feeds to confirm that the application is correctly sending data to the feeds


## Testing

Automated tests are implemented using the Pytest framework.

From the root directory of the repo run `python -m pytest` to execute tests.

This project uses cov for reporting test coverage

From the root directory of the repo run `python -m pytest --cov` to execute tests and generate a coverage report.

## Known Issues
