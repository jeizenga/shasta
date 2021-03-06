#!/usr/bin/python3

import shasta
import GetConfig
import sys
 
# Read the config file.
config = GetConfig.getConfig()

# Initialize the assembler and access what we need.
a = shasta.Assembler()
a.accessKmers()
a.accessReadsReadOnly()
a.accessMarkers()
a.accessOverlaps()
a.accessAlignmentData()

# Do the computation.
a.computeReadGraphComponents(
    minComponentSize = int(config['ReadGraph']['minComponentSize']),
    minAlignedMarkerCount = int(config['Align']['minAlignedMarkerCount']),
    maxTrim = int(config['Align']['maxTrim'])
    )

