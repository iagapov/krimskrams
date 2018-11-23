SDDS1
&description text="Error log--input: errors.ele  lattice: fodo.lte", contents="error log, elegant output" &end
&associate filename="errors.ele", path="C:/workspace/misc/optics_examples/sandbox", contents="elegant input, parent" &end
&associate filename="fodo.lte", path="C:/workspace/misc/optics_examples/sandbox", contents="elegant lattice, parent" &end
&parameter name=Step, type=long, description="simulation step" &end
&parameter name=When, type=string, description="phase of simulation when errors were asserted" &end
&column name=ParameterValue, type=double, description="Perturbed value" &end
&column name=ParameterError, type=double, description="Perturbation value" &end
&column name=ElementParameter, type=string, description="Parameter name" &end
&column name=ElementName, type=string, description="Element name" &end
&column name=ElementOccurence, type=long, description="Element occurence" &end
&column name=ElementType, type=string, description="Element type" &end
&data mode=ascii, lines_per_row=1, no_row_counts=1 &end
0              ! simulation step
pre-correction
-6.412908274354552e-03 -6.412908274354552e-03         DX         QF 1       QUAD
3.534329734678947e-02 3.534329734678947e-02         DX         QF 2       QUAD
-2.820104675078300e-02 -2.820104675078300e-02         DX         QF 3       QUAD
-6.443310643423106e-02 -6.443310643423106e-02         DX         QF 4       QUAD
8.027278130105034e-02 8.027278130105034e-02         DX         QF 5       QUAD
-2.081579208586655e-02 -2.081579208586655e-02         DX         QF 6       QUAD
4.497360968193748e-02 4.497360968193748e-02         DX         QF 7       QUAD
-2.186500612739881e-02 -2.186500612739881e-02         DX         QF 8       QUAD
-3.691461886526888e-02 -3.691461886526888e-02         DX         QF 9       QUAD
3.032179701402678e-02 3.032179701402678e-02         DY         QD 1       QUAD
7.537710641587725e-02 7.537710641587725e-02         DY         QD 2       QUAD
2.097442644849893e-02 2.097442644849893e-02         DY         QD 3       QUAD
-1.906834617623292e-02 -1.906834617623292e-02         DY         QD 4       QUAD
-1.280425306042117e-02 -1.280425306042117e-02         DY         QD 5       QUAD
-8.088841675297069e-02 -8.088841675297069e-02         DY         QD 6       QUAD
-6.334509146050204e-03 -6.334509146050204e-03         DY         QD 7       QUAD
5.380917280065017e-02 5.380917280065017e-02         DY         QD 8       QUAD
-1.047514916855388e-02 -1.047514916855388e-02         DY         QD 9       QUAD
2.008932545687775e+00 8.932545687775181e-03         K1         QF 1       QUAD
2.004095595088486e+00 4.095595088486328e-03         K1         QF 2       QUAD
2.003166835435951e+00 3.166835435951016e-03         K1         QF 3       QUAD
1.994062488022594e+00 -5.937511977406393e-03         K1         QF 4       QUAD
1.993318107784263e+00 -6.681892215737296e-03         K1         QF 5       QUAD
1.991139618093083e+00 -8.860381906916551e-03         K1         QF 6       QUAD
2.010066343195456e+00 1.006634319545572e-02         K1         QF 7       QUAD
1.999507219647376e+00 -4.927803526240408e-04         K1         QF 8       QUAD
1.998909965625269e+00 -1.090034374731137e-03         K1         QF 9       QUAD
-1.995328226437834e+00 4.671773562165527e-03         K1         QD 1       QUAD
-1.992539762138537e+00 7.460237861462775e-03         K1         QD 2       QUAD
-2.017637949906886e+00 -1.763794990688569e-02         K1         QD 3       QUAD
-2.009446589739727e+00 -9.446589739727160e-03         K1         QD 4       QUAD
-1.996990981164715e+00 3.009018835284674e-03         K1         QD 5       QUAD
-2.011258320086666e+00 -1.125832008666648e-02         K1         QD 6       QUAD
-1.982286868237441e+00 1.771313176255896e-02         K1         QD 7       QUAD
-2.006096329646849e+00 -6.096329646849380e-03         K1         QD 8       QUAD
-1.996447729767381e+00 3.552270232619055e-03         K1         QD 9       QUAD

