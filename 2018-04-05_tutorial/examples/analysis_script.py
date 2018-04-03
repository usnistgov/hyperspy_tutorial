# -*- coding: utf-8 -*-
"""
analysis_script.py

This is an example hyperspy script that loads an example EDS spectrum and then 
prints some very basic statistics about it.
"""

import hyperspy.api as hs

sig = hs.datasets.example_signals.EDS_SEM_Spectrum()

print(sig.metadata)

sig.print_summary_statistics()
