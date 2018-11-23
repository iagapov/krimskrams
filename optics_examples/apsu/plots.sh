#!/bin/bash
# sdds plotting stuff
sddsprintout apsu.twi -parameters=ex0
sddsprintout apsu.twi -columns='(s,beta?)'
#sddsplot -graphic=line,vary apsu.twi -columnNames=s,beta? -yScalesGroup=id=beta -columnNames=s,etax -yScalesGroup=id=eta -scales=0,10.54,0,00
sddsplot -graphic=line,vary apsu.twi -columnNames=s,beta? -yScalesGroup=id=beta -columnNames=s,etax -yScalesGroup=id=eta
