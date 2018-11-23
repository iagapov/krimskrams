# adapted from nsls2 script
# seems to weird to use for alignment assignment use only to merge files
# outut -- number of pages same as number of seeds
# align1.param contains misalignment for various seeds
#!/bin/bash

sddsprocess align1.param -pipe=out \
-match=column,ElementGroup=GIRDER* \
-match=column,ElementParameter=DX \
-define=column,PageP,i_page,type=long \
-define=parameter,PageP,i_page,type=long \
| sddsxref align1.twi -pipe -match=ElementName -take=s -reuse=page \
| sddsbreak -pipe -change=ElementGroup \
| sddsprocess -pipe \
-process=s,first,sMin -process=s,last,sMax \
-process=ParameterValue,first,Vo -process=ParameterValue,last,Vn \
"-define=parameter,sLength,sMax sMin -"  \
"-define=parameter,dxo,Vo"  \
"-define=parameter,dxp,Vn Vo - 1 /" \
"-define=column,dxGirdcor,dxo dxp s sMin - * +" \
"-define=column,dxGirdbeg,ParameterValue Vo == pop pop ? 0 : 1 $" \
"-define=column,dxGirdend,ParameterValue Vn == pop pop ? 0 : 1 $" \
"-define=column,dx,ParameterValue" \
| sddscombine -pipe=in align1.dx -merge=PageP
