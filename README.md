# Particulate Matter Monitor

## Overview
An air quality monitoring app.

Reads data from a SDS011 particulate matter sensor via a serial port and uploads it to a 

Inspired by tutorial from Raspberry Pi magazine issue

### Disclaimer

There are probably much more comprehensive and robust implementations out there for reading from the SDS011 sensor. Don't rely on this app for accurate and reliable data.

## Why

Small particulate matter less than 10 microns in diameter (PM 10) is recognised globally by health and environmental organisations as a common contributor to air pollution.

### Health Implications of PM

Exposure to particle matter less than 2.5 microns in diameter (PM 2.5) is known to cause respiratory and cardiovascular illness.

There is some evidence which suggests that high levels of PM may contribute to the transmission and lethality of COVID-19.

## Recommended hardware

Raspberry Pi
SDS011
Serial to USB adapter

## Install

Required dependencies are defined in requirements.txt

Pip install -r requirements.txt

## Ada FruitIO

An Ada FruitIO account and API key is required in order to upload data

## Setup

Run setup.py

Enter 

## Usage

A python virtual environment is recommended

Run python main.py start

Offline mode

## Testing

Automated tests use the Pytest framework

From the root directory of the repo run python -m pytest

This project uses cov for reporting test coverage

From the root directory of the repo run python -m pytest --cov

## Known Issues