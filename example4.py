import numpy as np
from poliastro.bodies import Earth, Sun
from poliastro.constants import J2000
from poliastro.examples import churi, iss, molniya
from poliastro.plotting import OrbitPlotter3D
from poliastro.twobody import Orbit
# More info: https://plotly.com/python/renderers/
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook_connected"
churi.plot(interactive=True, use_3d=True)