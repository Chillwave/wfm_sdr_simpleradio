# wfm_sdr_simpleradio

`wfm_sdr_simpleradio` is a software-defined radio (SDR) application designed to demodulate wideband FM (WFM) signals. It utilizes the GNURadio framework and the OsmoSDR source block in combination with the `rtl_tcp` utility to support a wide range of SDR devices, including the popular RTL-SDR dongles.

## Prerequisites

- Python 3
- GNURadio
- OsmoSDR
- rtl-sdr package
- An SDR device supported by OsmoSDR and rtl-sdr (e.g., RTL-SDR)

## Hardware

Popular options within the field, the entry tier is a great device to learn with. Here are some options on Amazon:

### Entry Tier (27MHz-1700MHz)

[NooElec NESDR Mini USB RTL-SDR & ADS-B Receiver Set](https://www.amazon.com/NooElec-NESDR-Mini-Compatible-Packages/dp/B009U7WZCA)

### Mid Tier (65MHz-2300MHz)

[NooElec NESDR Smart XTR SDR](https://www.amazon.com/NooElec-NESDR-Smart-XTR-SDR/dp/B06Y1HKLHY/)

### High Tier (1MHz to 6GHz)

[Software Defined Radio, 1MHz-6GHz SDR Platform Software Defined Radio Development Board](https://www.amazon.com/Software-1MHz-6GHz-Frequency-Bandwidth-Adapters/dp/B0BKH7Z2N)
## Usage

1. Run the `rtl_tcp` utility in a separate terminal to start the TCP server:

   ```sh
   rtl_tcp
   ```

2. Run the script with Python 3:

   ```sh
   python3 wfm_sdr_simpleradio.py
   ```

3. When prompted, enter the frequency of the FM station you want to listen to in MHz.

4. The script will start demodulating the FM signal and playing the audio.

5. You can adjust the frequency while the script is running by typing "a" to decrease the frequency by 0.01 MHz or "d" to increase the frequency by 0.01 MHz.

## How It Works

The script sets up a GNURadio flowgraph with the following blocks:

- An OsmoSDR source block that receives samples from the SDR device via the `rtl_tcp` server. This allows the SDR device to be used remotely over a network.
- A wideband FM receive (WFM RCVR) block that demodulates the FM signal.
- An audio sink block that plays the demodulated audio.

The OsmoSDR source block is configured to use automatic gain control and a sample rate of 1.024 MS/s. The WFM RCVR block is configured with a quadrature rate equal to the sample rate and an audio decimation factor that results in an audio rate of 48 kHz.

## Limitations and Future Work

This is a basic SDR application with limited features. Future work could include adding support for other modulation schemes, implementing a graphical user interface (GUI), improving the audio quality, and handling different types of SDR hardware. Additionally, better error handling and support for different network configurations could be added for the `rtl_tcp` server connection.
