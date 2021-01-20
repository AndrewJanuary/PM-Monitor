# Particulate Matter Monitor

## Overview

An air quality monitoring app.

Reads data from an [SDS011 particulate matter sensor](https://www.hackair.eu/docs/sds011/) via a serial port and uploads it to an [Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io) account.

Inspired by tutorial from Raspberry Pi magazine issue

### Disclaimer

There are probably much more comprehensive and robust implementations out there for reading from the SDS011 sensor. Don't rely on this app for accurate and reliable data.

## Why

Small particulate matter less than 10 microns in diameter (PM 10) is recognised globally by health and environmental organisations as a common contributor to air pollution.

### Health Implications of PM

Exposure to particle matter less than 2.5 microns in diameter (PM 2.5) is known to cause and contribute to respiratory and cardiovascular illness.

There is some evidence which suggests that high levels of PM may contribute to the transmission and lethality of COVID-19.

## Recommended hardware

Raspberry Pi (for convenience of placing the sensor)
[SDS011 PM sensor](https://www.hackair.eu/docs/sds011/)
Serial to USB adapter

## Install

A python virtual environment is recommended. You can easily create a new virtual environment using venv.

python -m venv venv

Required dependencies are defined in requirements.txt. You can install these using pip.

Pip install -r requirements.txt

## AdaFruit IO

An [Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io) account and API key are required in order to upload data.

## Setup


## Usage


## Testing

Automated tests use the Pytest framework

From the root directory of the repo run python -m pytest

This project uses cov for reporting test coverage

From the root directory of the repo run python -m pytest --cov

## Known Issues