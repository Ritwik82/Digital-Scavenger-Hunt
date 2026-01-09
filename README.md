Digital Scavenger Hunt 🕵️‍♂️

Welcome to the Digital Scavenger Hunt. This is a entry-level forensic challenge designed to test your knowledge of file structures, hex data, and data recovery.

The Scenario
A critical data packet has been intercepted, but it appears to be corrupted during transmission. Our automated systems cannot recognize the file format, and the data remains locked behind a damaged layer.

Your mission is to manually repair the file, extract the hidden information, and authenticate through the recovery portal.

Challenge Setup
Download the Repository: Clone this repo or download the ZIP to your local machine.

Start the Node: To ensure the recovery portal functions correctly, run a local server within the directory:

Bash

python -m http.server 8000
Access the Portal: Open your browser and navigate to http://localhost:8000.

Objective
Identify why the provided challenge.png will not open.

Recover the integrity of the file using forensic tools.

Extract the hidden sequence within the image using the ZXing library or a compatible decoder.

Submit the final flag into the portal to complete the hunt.

Technical Details
Category: Forensics / File Carving

Difficulty: Easy / Medium

Required Tools: * A Hex Editor (e.g., HxD or Hexed.it)

ZXing Decoder (Online or Library)
