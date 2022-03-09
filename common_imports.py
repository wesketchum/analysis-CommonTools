#!/usr/bin/env python3

#imports
import uproot
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *
import scipy as sp
import scipy.stats
import scipy.optimize
import glob
import time

try:
    import numba
    from numba import jit, int32, float32
    import numba_scipy
except:
    print("Cannot find numba. Don't use numba here!")

