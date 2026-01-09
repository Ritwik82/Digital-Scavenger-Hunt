Digital Scavenger Hunt 🕵️‍♂️

Welcome to the Digital Scavenger Hunt. This is a entry-level forensic challenge designed to test your knowledge of file structures, hex data, and data recovery.


The Scenario
A critical data packet has been intercepted, but it appears to be corrupted during transmission. Our automated systems cannot recognize the file format, and the data remains locked behind a damaged layer.

Your mission is to manually repair the file, extract the hidden information, and authenticate through the recovery portal.


Challenge Setup
1.Download the Repository: Clone this repo or download the ZIP to your local machine.

2.Start the Node: To ensure the recovery portal functions correctly, run a local server within the directory: "python -m http.server 8000"

3.Access the Portal: Open your browser and navigate to http://localhost:8000.


Objective
1.Identify why the provided challenge.png will not open.

2.Recover the integrity of the file using forensic tools.

3.Extract the hidden sequence within the image using the ZXing library or a compatible decoder.

4.Submit the final flag into the portal to complete the hunt.


Technical Details
1.Category: Forensics / File Carving

2.Difficulty: Easy / Medium

3.Required Tools: * A Hex Editor (e.g., HxD or Hexed.it)

4.ZXing Decoder (Online or Library)
