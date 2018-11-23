#!/bin/bash
# sdds plotting stuff
sddsprintout align1.twi -parameters=*
#sddsprintout fodo.twi -columns='(ElementName,ElementType,s,beta?)'
#sddsplot -graphic=line,vary apsu.twi -columnNames=s,beta? -yScalesGroup=id=beta -columnNames=s,etax -yScalesGroup=id=eta -scales=0,10.54,0,00
sddsplot align1.twi "-title=toy fodo ring"  -legend -date \
-col=s,betax -graphic=line,type=1 \
-col=s,betay -graphic=line,type=2 \
-col=s,etax -yScalesGroup=id=eta -graphic=line,type=3 \
-col=s,Profile -graphic=line,type=0 fodo.mag

sddsplot align2.traj -col=s,x -split=page -graph=sym
sddsplot align2.traj -col=s,y -split=page -graph=sym

#sddsplot -column=x,y align2.los -split=page -graph=sym -samescales
#sddsplot -column=s,x align2.los -split=page -graph=sym -samescales

sddsplot -column=s,x align3.clo -split=page -graph=sym,type=2 -samescales
sddsplot -column=s,y align3.clo -split=page -graph=sym,type=2 -samescales

sddsplot align3.twi "-title=toy fodo ring"  -legend -date \
-col=s,betax -graphic=line,type=1 \
-col=s,betay -graphic=line,type=2 -split=page -samescales \
