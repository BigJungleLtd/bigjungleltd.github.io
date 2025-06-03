---
layout: post
title: "Raspberry Pi FTDI Shim"
date: 2015-08-20 15:30:00 +0000
author: "Jeremy Poulter"
categories: ["Hardware", "Raspberry Pi"]
tags: ["raspberry-pi", "ftdi", "hardware", "serial"]
original_url: "/blog/2015/8/20/raspberry-pi-ftdi-shim"
---

When working with embedded systems and IoT projects, having reliable serial communication is essential. The Raspberry Pi's GPIO header provides UART functionality, but sometimes you need the convenience and isolation of an FTDI USB-to-serial adapter.

## The Problem

While the Raspberry Pi has built-in UART pins on the GPIO header, there are several scenarios where an external FTDI adapter is preferable:

- **Isolation**: Protecting your Pi from potential voltage issues
- **Convenience**: Easy plug-and-play serial access
- **Multiple Connections**: Using the Pi's UART for other purposes
- **Development**: Easier debugging and logging during development

## The Solution: FTDI Shim

An FTDI shim is a small adapter board that bridges the gap between standard FTDI breakout boards and the Raspberry Pi GPIO header. This simple but effective solution provides:

### Key Features

- **Direct GPIO Connection**: Plugs directly into the Pi's GPIO header
- **Standard FTDI Pinout**: Compatible with common FTDI breakout boards
- **Power Options**: Can provide 3.3V or 5V power to connected devices
- **Compact Design**: Minimal footprint and low profile
- **Easy Access**: Other GPIO pins remain accessible

### Pinout Mapping

The shim typically maps the following connections:

| FTDI Pin | Pi GPIO Pin | Function |
|----------|-------------|----------|
| GND      | GND         | Ground   |
| VCC      | 3.3V/5V     | Power    |
| RX       | GPIO 14     | TX       |
| TX       | GPIO 15     | RX       |
| DTR      | Not used    | -        |
| CTS/RTS  | Optional    | Flow Control |

## Use Cases

This setup is particularly useful for:

### OpenTRV Development
When working with OpenTRV thermostatic radiator valves, the FTDI connection provides:
- Easy firmware flashing
- Real-time status monitoring  
- Debug output capture
- Configuration updates

### Arduino Communication
For projects involving Arduino boards:
- Programming ATmega microcontrollers
- Serial debugging and monitoring
- Data logging from sensors
- Bootloader installation

### General Serial Devices
Any device requiring serial communication:
- GPS modules
- Sensor networks
- Display modules
- Custom embedded projects

## Assembly and Installation

The FTDI shim is typically a simple PCB that requires minimal assembly:

1. **Solder Headers**: Attach male pins for GPIO connection and female socket for FTDI board
2. **Check Connections**: Verify pinout matches your specific FTDI breakout
3. **Power Selection**: Ensure voltage levels match your target device
4. **Install**: Plug into Pi GPIO header and connect FTDI board

## Software Configuration

To use the FTDI connection with your Raspberry Pi:

```bash
# Check for USB serial device
lsusb | grep FTDI

# List serial devices
ls /dev/ttyUSB*

# Connect using screen
screen /dev/ttyUSB0 9600

# Or use minicom
minicom -D /dev/ttyUSB0 -b 9600
```

## Benefits

The FTDI shim approach offers several advantages:

- **Flexibility**: Easy to connect/disconnect serial devices
- **Reliability**: Proven FTDI chips provide stable communication
- **Debugging**: Excellent for development and troubleshooting
- **Isolation**: Protects Pi from electrical issues
- **Portability**: FTDI connection works with any computer

## Conclusion

The Raspberry Pi FTDI shim is a simple but valuable tool for anyone working with serial communication in IoT and embedded projects. Its ease of use and reliability make it an essential component in the embedded developer's toolkit.

Whether you're flashing firmware, debugging sensor networks, or monitoring data streams, this small adapter can significantly improve your development workflow and system reliability.
