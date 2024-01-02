Astrophotography can be fun, but the file management can be cumbersome.

I decided to write a little utility that mirrors the process that eventually evolved from my months of iterations.

My folder structure is quite simple, I have a main Astrophotography folder, inside which I have a folder for calibration frames (dark flats and flats), I copy them and use that location as a symbolic link inside each project folder.

Calibration Frames contains the images stored in a naming convention of "night_date" for example, images I took on 23 December 2023 would be listed as: night_20231223

This naming convention keeps things organized and allows the use of PixInsight's keywords to help sort things out to ensure image stacking is done on a nightly basis.

_I'll eventually add more detail here if there's an interest_