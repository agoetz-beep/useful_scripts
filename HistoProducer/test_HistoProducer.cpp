// compile with: `root-config --cxx --cflags --evelibs` -Wall -o test.exe *.cpp `root-config --cflags --evelibs`

#include "HistoProducer.hpp"

int  main() {

HistoProducer test;
test.AddVariable("Evt_Pt_MET");
test.AddVariable("Neutralino_Pt");
test.PrintVariables();
test.AddWeight("Weight_XS");
test.AddWeight("Weight_CSV");
test.PrintWeights();
test.AddUncertainty("Weight_CSVLF");
test.AddUncertainty("Weight_CSVHF");
test.PrintUncertainties();
return 0;

}
