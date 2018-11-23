#!/bin/bash
# sdds plotting stuff
sddsprintout first_turn.twi -parameters=*
#sddsprintout fodo.twi -columns='(ElementName,ElementType,s,beta?)'
#sddsplot -graphic=line,vary apsu.twi -columnNames=s,beta? -yScalesGroup=id=beta -columnNames=s,etax -yScalesGroup=id=eta -scales=0,10.54,0,00
sddsplot first_turn.twi "-title=toy fodo ring"  -legend -date \
-col=s,betax -graphic=line,type=1 \
-col=s,betay -graphic=line,type=2 \
-col=s,etax -yScalesGroup=id=eta -graphic=line,type=3 \
-col=s,Profile -graphic=line,type=0 fodo.mag

sddsplot -parameter=MALIN.DP,Transmission first_turn.fin -graph=sym

# -graph=line,type=0 fodo.mag -col=s,Profile -overlay=xmode=norm,yfact=0.05
#sddsplot -column=s,Cx errors.cen -graph=sym,fill
