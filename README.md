🕵️‍♂️ Digital Scavenger Hunt 
==========================

🧩 Overview
-------------
Welcome to the Digital Scavenger Hunt.
This is an entry-level forensic challenge designed to test your understanding of:
- File structures
- Hexadecimal data
- Manual data recovery techniques


📖 The Scenario
----------------
A critical data packet has been intercepted, but it appears to have been corrupted
during transmission. Our automated systems cannot recognize the file format, and
the data remains locked behind a damaged layer.

Your mission is to manually repair the file, extract the hidden information, and
authenticate through the recovery portal.


🗂️ Challenge Setup
-------------------
1. Download the Repository
   Clone this repository or download the ZIP file to your local machine.

2. Start the Local Node
   To ensure the recovery portal functions correctly, run a local server inside
   the project directory:

   python -m http.server 8000

3. Access the Portal
   Open your browser and navigate to:

   http://localhost:8000


🎯 Objective
-------------
1. Identify why the provided challenge.png will not open.
2. Recover the integrity of the file using forensic techniques.
3. Extract the hidden sequence within the image using the ZXing library or a
   compatible QR decoder.
4. Submit the final flag into the portal to complete the hunt.


⚙️ Technical Details
---------------------
Category: Forensics / File Carving
Difficulty: Easy / Medium
Required Tools:
- Hex Editor (HxD, Hexed.it)
- ZXing Decoder (Online or Library)



Good luck, investigator.
The truth is hidden in plain hex.

