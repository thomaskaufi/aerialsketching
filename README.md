# Making Motion GitHub Repo!
This GitHub contains all software sketches and technical documentation for Final Master Project: Making Motion.
The project takes shape through Aerial Sketching - a kinetic installation allowing to design kinetic expressivity of suspended fabrics through embodied interaction.
Aerial Sketching consists of three [kinetic winches by Wahlberg Motion Design](https://wahlberg.dk/products/winch-3). Interaction is driven by [Google Mediapipe Hand Detection](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker). All data handling and interaction is facilitated with TouchDesigner. The installation allows to create visual representation of interaction (Kinetic Captures) which are printed with a Dymo Labelprinter through a custom python-script.

Thomas Kaufmanas, Eindhoven, 2025

## Contents
- MakingMotion.toe: Main Touchdesigner script for running Aerial Sketching
- print_watcher.py: Script for printing kinetic captures with dymo label printer
- /Documentation: Photos and strucutal plans

Version History:
- Sketch01.toe: Track XY of index finger tips
- Sketch02.toe: Track pinchpoints (thumb/indx finger), export XY
- Sketch03.toe: Link pinchpoints to winch, add smoothing
- Sketch04.toe: Map to three winches (left/right average)
- Sketch05.toe: Cursor-style pinchpoints 
- Sketch06.toe: Added cases (0, 1 or 2 hands present)
- Sketch07.toe: Added GUI
- Sketch10.toe: Rebuild data-path of landmarks
- Sketch11.toe: Added mid-winch tilt (wrist-index finger distance)
- Sketch12.toe: Added Smoothing (liveliness) from hand distance
- Sketch13.toe: Added Sampling. Rebuild GUI for perform-mode
- Sketch14.toe: Remove hand-distance smoothing. Rebuild mid-winch tilt (from z-distance),
- Sketch15.toe: Update Indexing sampler through range slider
- Sketch16.toe: Added point cloud from sample data
- Sketch17.toe: Update point cloud (kinetic capture)
- Sketch18.toe: Added label export + full res export
- Sketch19.toe: Update label pipeline
- MakingMotion.Toe: Script optimization and general cleanup

![Exposition Design](https://github.com/user-attachments/assets/5b1a6f08-eb2b-4cac-abf0-9e9dcc71bad4)

