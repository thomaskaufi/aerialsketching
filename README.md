# Making Motion GitHub Repo!
This GitHub contains all software sketches and technical documentation for Final Master Project: Making Motion.
The project takes shape through Aerial Sketching - a kinetic installation allowing to design kinetic expressivity of suspended fabrics through embodied interaction.
Aerial Sketching consists of three [kinetic winches by Wahlberg Motion Design](https://wahlberg.dk/products/winch-3). Interaction is driven by [Google Mediapipe Hand Detection](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker). All data handling and interaction is facilitated with TouchDesigner. The installation allows to create visual representation of interaction (Kinetic Captures) which are printed with a Dymo Labelprinter through a custom python-script.

Thomas Kaufmanas, Eindhoven, 2025

## Contents
- MakingMotion.toe: Main Touchdesigner script for running Aerial Sketching
- print_watcher.py: Script for printing kinetic captures with dymo label printer
- /Sketches: Earlier iterations
- /Documentation: Photos and strucutal plans


Version History:
- Sketch 01: Track XY of index finger tips
- Sketch 02: Track pinchpoints (thumb/indx finger), export XY
- Sketch 03: Link pinchpoints to winch, add smoothing
- Sketch 04: Map to three winches (left/right average)
- Sketch 05: Cursor-style pinchpoints 
- Sketch 06: Added cases (0, 1 or 2 hands present)
- Sketch 07: Added GUI
- Sketch 10: Rebuild data-path of landmarks
- Sketch 11: Added mid-winch tilt (wrist-index finger distance)
- Sketch 12: Added Smoothing (liveliness) from hand distance
- Sketch 13: Added Sampling. Rebuild GUI for perform-mode
- Sketch 14: Remove hand-distance smoothing. Rebuild mid-winch tilt (from z-distance),
- Sketch 15: Update Indexing sampler through range slider
- Sketch 16: Added point cloud from sample data
- Sketch 17: Update point cloud (kinetic capture)
- Sketch 18: Added label export + full res export
- Sketch 19: Update label pipeline
- Sketch 20: Script optimization and general cleanup
