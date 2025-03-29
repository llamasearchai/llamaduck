# Documentation Images

This directory contains images used in the LlamaDuck Pro documentation.

## Creating a Demo GIF

To create a new demo GIF:

1. Install [asciinema](https://asciinema.org/) and [asciicast2gif](https://github.com/asciinema/asciicast2gif)

2. Record a terminal session:
   ```bash
   asciinema rec llamaduck-demo.cast
   ```

3. During the recording, demonstrate the LlamaDuck Pro features:
   ```bash
   llamaduck --help
   llamaduck search "python best practices"
   llamaduck chat "Tell me about llamas"
   ```

4. Convert the recording to a GIF:
   ```bash
   asciicast2gif llamaduck-demo.cast llamaduck-demo.gif
   ```

5. Optimize the GIF (optional):
   ```bash
   gifsicle -O3 llamaduck-demo.gif -o llamaduck-demo.gif
   ```

6. Place the resulting GIF in this directory as `llamaduck-demo.gif` 