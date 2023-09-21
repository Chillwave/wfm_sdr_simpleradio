from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
import osmosdr
import threading

class MyTopBlock(gr.top_block):
    def __init__(self, frequency):
        gr.top_block.__init__(self)

        sample_rate = 1.024e6  # Sample rate
        audio_rate = 48e3  # Audio rate

        self.src = osmosdr.source("rtl_tcp=127.0.0.1:1234")
        self.src.set_sample_rate(sample_rate)
        self.src.set_center_freq(frequency)
        self.src.set_gain_mode(True, 0)

        self.demod = analog.wfm_rcv(
            quad_rate=sample_rate,
            audio_decimation=int(sample_rate / audio_rate),
        )

        self.audio_sink = audio.sink(int(audio_rate), "", True)

        self.connect(self.src, self.demod, self.audio_sink)

def keyboard_thread(tb, frequency):
    while True:
        key = input()
        if key == "a":
            frequency[0] -= 0.01 * 1e6  # Adjust frequency by -0.01 MHz
            print(f"Decreased frequency to {frequency[0] / 1e6} MHz")
            tb.src.set_center_freq(frequency[0])
        elif key == "d":
            frequency[0] += 0.01 * 1e6  # Adjust frequency by +0.01 MHz
            print(f"Increased frequency to {frequency[0] / 1e6} MHz")
            tb.src.set_center_freq(frequency[0])

if __name__ == "__main__":
    frequency_input = input("Please enter the frequency in MHz: ")
    frequency = [float(frequency_input) * 1e6]  # Convert MHz to Hz
    tb = MyTopBlock(frequency[0])
    tb.start()
    threading.Thread(target=keyboard_thread, args=(tb, frequency)).start()
