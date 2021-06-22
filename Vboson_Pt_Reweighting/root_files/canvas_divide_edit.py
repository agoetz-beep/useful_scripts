import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys

boson=sys.argv[1]
file_LO=ROOT.TFile.Open(sys.argv[2])
file_NLO=ROOT.TFile.Open(sys.argv[3])
file_factors=ROOT.TFile(boson + "_factors.root", "RECREATE")

canvas=ROOT.TCanvas("canvas", "canvas", 4000, 3000)
canvas_3D=ROOT.TCanvas("canvas_3D", "canvas_3D", 4500, 1700)

legend=ROOT.TLegend(0.15,0.15)
legend2=ROOT.TLegend(0.15,0.15)

##################################################################

hist=file_LO.Get(boson+"_boson_pt")
hist2=file_NLO.Get(boson+"_boson_pt")
hist4=file_LO.Get(boson + "_boson_pt_to1TeV")
hist5=file_NLO.Get(boson +"_boson_pt_to1TeV")
hist7=file_LO.Get(boson + "_boson_eta")
hist8=file_NLO.Get(boson + "_boson_eta")
hist10=file_LO.Get(boson + "_boson_phi")
hist11=file_NLO.Get(boson + "_boson_phi")
hist13=file_LO.Get(boson + "_jets_fuehrende_Ordnung_pt")
hist14=file_NLO.Get(boson + "_jets_fuehrende_Ordnung_pt")
hist16=file_LO.Get(boson + "_jets_fuehrende_Ordnung_eta")
hist17=file_NLO.Get(boson + "_jets_fuehrende_Ordnung_eta")
hist19=file_LO.Get(boson + "_jets_anzahl")
hist20=file_NLO.Get(boson + "_jets_anzahl")
hist22=file_LO.Get(boson + "_jets_HT")
hist23=file_NLO.Get(boson + "_jets_HT")
hist25=file_LO.Get(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi")
hist26=file_NLO.Get(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi")
hist28=file_LO.Get(boson + "_boson_transverse_mass")
hist29=file_NLO.Get(boson + "_boson_transverse_mass")
hist1_2D=file_LO.Get(boson + "_boson_jets_fuehrende_Ordnung_pt_2D")
hist2_2D=file_NLO.Get(boson + "_boson_jets_fuehrende_Ordnung_pt_2D")
hist4_2D=file_LO.Get(boson + "_boson_pt_DeltaPhi_2D")
hist5_2D=file_NLO.Get(boson + "_boson_pt_DeltaPhi_2D")
hist7_2D=file_LO.Get(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D")
hist8_2D=file_NLO.Get(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D")
hist10_2D=file_LO.Get(boson + "_jets_anzahl_HT_2D")
hist11_2D=file_NLO.Get(boson + "_jets_anzahl_HT_2D")
hist13_2D=file_LO.Get(boson + "_boson_transverse_mass_pt_2D")
hist14_2D=file_NLO.Get(boson + "_boson_transverse_mass_pt_2D")
hist16_2D=file_LO.Get(boson + "_boson_transverse_mass_phizwlundnu_2D")
hist17_2D=file_NLO.Get(boson + "_boson_transverse_mass_phizwlundnu_2D")

hist_ana=file_LO.Get(boson+"_boson_pt_ana")
hist2_ana=file_NLO.Get(boson+"_boson_pt_ana")
hist4_ana=file_LO.Get(boson + "_boson_pt_to1TeV_ana")
hist5_ana=file_NLO.Get(boson +"_boson_pt_to1TeV_ana")
hist7_ana=file_LO.Get(boson + "_boson_eta_ana")
hist8_ana=file_NLO.Get(boson + "_boson_eta_ana")
hist10_ana=file_LO.Get(boson + "_boson_phi_ana")
hist11_ana=file_NLO.Get(boson + "_boson_phi_ana")
hist13_ana=file_LO.Get(boson + "_jets_fuehrende_Ordnung_pt_ana")
hist14_ana=file_NLO.Get(boson + "_jets_fuehrende_Ordnung_pt_ana")
hist16_ana=file_LO.Get(boson + "_jets_fuehrende_Ordnung_eta_ana")
hist17_ana=file_NLO.Get(boson + "_jets_fuehrende_Ordnung_eta_ana")
hist19_ana=file_LO.Get(boson + "_jets_anzahl_ana")
hist20_ana=file_NLO.Get(boson + "_jets_anzahl_ana")
hist22_ana=file_LO.Get(boson + "_jets_HT_ana")
hist23_ana=file_NLO.Get(boson + "_jets_HT_ana")
hist25_ana=file_LO.Get(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana")
hist26_ana=file_NLO.Get(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana")
hist28_ana=file_LO.Get(boson + "_boson_transverse_mass_ana")
hist29_ana=file_NLO.Get(boson + "_boson_transverse_mass_ana")
hist1_2D_ana=file_LO.Get(boson + "_boson_jets_fuehrende_Ordnung_pt_2D_ana")
hist2_2D_ana=file_NLO.Get(boson + "_boson_jets_fuehrende_Ordnung_pt_2D_ana")
hist4_2D_ana=file_LO.Get(boson + "_boson_pt_DeltaPhi_2D_ana")
hist5_2D_ana=file_NLO.Get(boson + "_boson_pt_DeltaPhi_2D_ana")
hist7_2D_ana=file_LO.Get(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_ana")
hist8_2D_ana=file_NLO.Get(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_ana")
hist10_2D_ana=file_LO.Get(boson + "_jets_anzahl_HT_2D_ana")
hist11_2D_ana=file_NLO.Get(boson + "_jets_anzahl_HT_2D_ana")
hist13_2D_ana=file_LO.Get(boson + "_boson_transverse_mass_pt_2D_ana")
hist14_2D_ana=file_NLO.Get(boson + "_boson_transverse_mass_pt_2D_ana")
hist16_2D_ana=file_LO.Get(boson + "_boson_transverse_mass_phizwlundnu_2D_ana")
hist17_2D_ana=file_NLO.Get(boson + "_boson_transverse_mass_phizwlundnu_2D_ana")

#########################################################################################

hist3=hist2.Clone()
hist3.Divide(hist)
hist3.GetXaxis().SetRangeUser(30.0,1000.0)

hist6=hist5.Clone()
hist6.Divide(hist4)

hist9=hist8.Clone()
hist9.Divide(hist7)
hist7.GetYaxis().SetRangeUser(0,3000)

hist12=hist11.Clone()
hist12.Divide(hist10)
hist10.GetYaxis().SetRangeUser(950,1350.0)

hist15=hist14.Clone()
hist15.Divide(hist13)

hist18=hist17.Clone()
hist18.Divide(hist16)
hist16.GetYaxis().SetRangeUser(0,4000)
hist18.GetXaxis().SetRangeUser(-8,8)

hist21=hist20.Clone()
hist21.Divide(hist19)
hist21.GetXaxis().SetRangeUser(0,14)

hist24=hist23.Clone()
hist24.Divide(hist22)

hist27=hist26.Clone()
hist27.Divide(hist25)

hist30=hist29.Clone()
hist30.Divide(hist28)

hist3_2D=hist2_2D.Clone()
hist3_2D.Divide(hist1_2D)
hist1_2D.GetZaxis().SetRangeUser(0.01,100)
hist2_2D.GetZaxis().SetRangeUser(0.01,100)

hist6_2D=hist5_2D.Clone()
hist6_2D.Divide(hist4_2D)

hist9_2D=hist8_2D.Clone()
hist9_2D.Divide(hist7_2D)

hist12_2D=hist11_2D.Clone()
hist12_2D.Divide(hist10_2D)

hist15_2D=hist14_2D.Clone()
hist15_2D.Divide(hist13_2D)

hist18_2D=hist17_2D.Clone()
hist18_2D.Divide(hist16_2D)

hist3_ana=hist2_ana.Clone()
hist3_ana.Divide(hist_ana)
hist_ana.GetXaxis().SetRangeUser(250.0,1000.0)
hist3_ana.GetXaxis().SetRangeUser(250.0,1000.0)

hist6_ana=hist5_ana.Clone()
hist6_ana.Divide(hist4_ana)
hist4_ana.GetXaxis().SetRangeUser(250.0,1000.0)
hist6_ana.GetXaxis().SetRangeUser(250.0,1000.0)

hist9_ana=hist8_ana.Clone()
hist9_ana.Divide(hist7_ana)
hist7_ana.GetYaxis().SetRangeUser(0,3.5)
hist9_ana.GetXaxis().SetRangeUser(-3.14,3.14)

hist12_ana=hist11_ana.Clone()
hist12_ana.Divide(hist10_ana)
hist10_ana.GetYaxis().SetRangeUser(0.35,0.85)

hist15_ana=hist14_ana.Clone()
hist15_ana.Divide(hist13_ana)
hist13_ana.GetXaxis().SetRangeUser(100.0,1000.0)
hist15_ana.GetXaxis().SetRangeUser(100.0,1000.0)

hist18_ana=hist17_ana.Clone()
hist18_ana.Divide(hist16_ana)
hist16_ana.GetYaxis().SetRangeUser(0,4)
hist18_ana.GetXaxis().SetRangeUser(-2.4,2.4)

hist21_ana=hist20_ana.Clone()
hist21_ana.Divide(hist19_ana)
hist21_ana.GetXaxis().SetRangeUser(0.5,11.5)

hist24_ana=hist23_ana.Clone()
hist24_ana.Divide(hist22_ana)

hist27_ana=hist26_ana.Clone()
hist27_ana.Divide(hist25_ana)
hist27_ana.GetXaxis().SetRangeUser(1.57,3.14)

hist30_ana=hist29_ana.Clone()
hist30_ana.Divide(hist28_ana)

hist3_2D_ana=hist2_2D_ana.Clone()
hist3_2D_ana.Divide(hist1_2D_ana)
hist1_2D_ana.GetXaxis().SetRangeUser(250,1000)
hist1_2D_ana.GetYaxis().SetRangeUser(100,1000)
hist2_2D_ana.GetXaxis().SetRangeUser(250,1000)
hist2_2D_ana.GetYaxis().SetRangeUser(100,1000)
hist3_2D_ana.GetXaxis().SetRangeUser(250,1000)
hist3_2D_ana.GetYaxis().SetRangeUser(100,1000)
hist1_2D_ana.GetZaxis().SetRangeUser(0.01,100)
hist2_2D_ana.GetZaxis().SetRangeUser(0.01,100)

hist6_2D_ana=hist5_2D_ana.Clone()
hist6_2D_ana.Divide(hist4_2D_ana)
hist4_2D_ana.GetXaxis().SetRangeUser(250,1000)
hist5_2D_ana.GetXaxis().SetRangeUser(250,1000)
hist6_2D_ana.GetXaxis().SetRangeUser(250,1000)

hist9_2D_ana=hist8_2D_ana.Clone()
hist9_2D_ana.Divide(hist7_2D_ana)
hist7_2D_ana.GetXaxis().SetRangeUser(100,1000)
hist8_2D_ana.GetXaxis().SetRangeUser(100,1000)
hist9_2D_ana.GetXaxis().SetRangeUser(100,1000)
hist9_2D_ana.GetYaxis().SetRangeUser(1.57,3.14)

hist12_2D_ana=hist11_2D_ana.Clone()
hist12_2D_ana.Divide(hist10_2D_ana)
hist12_2D_ana.GetXaxis().SetRangeUser(-0.5,12.5)

hist15_2D_ana=hist14_2D_ana.Clone()
hist15_2D_ana.Divide(hist13_2D_ana)
hist13_2D_ana.GetYaxis().SetRangeUser(250,1000)
hist14_2D_ana.GetYaxis().SetRangeUser(250,1000)
hist15_2D_ana.GetYaxis().SetRangeUser(250,1000)

hist18_2D_ana=hist17_2D_ana.Clone()
hist18_2D_ana.Divide(hist16_2D_ana)

########################################################################################################

dictionary_drei={hist3,hist6,hist9,hist12,hist15,hist18,hist21,hist24,hist27,hist30,hist3_ana,hist6_ana,hist9_ana,hist12_ana,hist15_ana,hist18_ana,hist21_ana,hist24_ana,hist27_ana,hist30_ana}
for key in dictionary_drei:
    key.GetYaxis().SetRangeUser(0,2)
    
dictionary_drei_2D={hist3_2D,hist6_2D,hist9_2D,hist12_2D,hist15_2D,hist18_2D,hist3_2D_ana,hist6_2D_ana,hist9_2D_ana,hist12_2D_ana,hist15_2D_ana,hist18_2D_ana}
for key in dictionary_drei_2D:
    key.GetZaxis().SetRangeUser(0,2)

dictionary={}
dictionary_2D={}
dictionary[hist] ={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des "+ boson+ " Bosons", "Color":1 }
dictionary[hist2]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist3]={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist4] ={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des "+ boson+ " Bosons", "Color":1 }
dictionary[hist5]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist6]={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist7] ={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapiditaet des "+ boson+ " Bosons", "Color":1 }
dictionary[hist8]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist9]={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist10] ={"Xaxis": "Azimutalwinkel", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Azimutalwinkel des "+ boson+ " Bosons", "Color":1 }
dictionary[hist11]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist12]={"Xaxis": "Azimutalwinkel", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist13] ={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des fuehrenden Jets", "Color":1 }
dictionary[hist14]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist15]={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist16] ={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapiditaet des fuehrenden Jets", "Color":1 }
dictionary[hist17]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist18]={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist19] ={"Xaxis": "Anzahl der Jets", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4", "Color":1 }
dictionary[hist20]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist21]={"Xaxis": "Anzahl der Jets", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist22] ={"Xaxis": "Summe der Transversalimpulse aller Jets in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Summe der Transversalimpulse aller Jets mit pt>=30 GeV,|eta|<=2.4", "Color":1 }
dictionary[hist23]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist24]={"Xaxis": "Summe der Transversalimpulse aller Jets in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist25] ={"Xaxis": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und fuehrendem Jet", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und fuehrendem Jet", "Color":1 }
dictionary[hist26]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist27]={"Xaxis": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und fuehrendem Jet", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary[hist28] ={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversale Masse des W Bosons", "Color":1 }
dictionary[hist29]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 2 }
dictionary[hist30]={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 1 }

dictionary_2D[hist1_2D] ={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "transversaler Impuls des fuehrenden Jets in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO" }
dictionary_2D[hist2_2D]={"Xaxis":"transversaler Impuls des "+boson+" Bosons in GeV","Yaxis": "transversaler Impuls des fuehrenden Jets in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO" }
dictionary_2D[hist3_2D]={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "transversaler Impuls des fuehrenden Jets in GeV","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO" }

dictionary_2D[hist4_2D] ={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO" }
dictionary_2D[hist5_2D]={"Xaxis":"transversaler Impuls des "+boson+" Bosons in GeV","Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist6_2D]={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO" }

dictionary_2D[hist7_2D] ={"Xaxis": "transversaler Impuls des fuehrenden Jets in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO" }
dictionary_2D[hist8_2D]={"Xaxis":"transversaler Impuls des fuehrenden Jets in GeV","Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist9_2D]={"Xaxis": "transversaler Impuls des fuehrenden Jets in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO"}

dictionary_2D[hist10_2D] ={"Xaxis": "Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4", "Yaxis": "Summe der pt aller Jets in GeV mit pt>=30 GeV,|eta|<=2.4","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO"}
dictionary_2D[hist11_2D]={"Xaxis":"Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4","Yaxis": "Summe der pt aller Jets in GeV mit pt>=30 GeV,|eta|<=2.4","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO" }
dictionary_2D[hist12_2D]={"Xaxis": "Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4", "Yaxis": "Summe der pt aller Jets in GeV mit pt>=30 GeV,|eta|<=2.4","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO" }

dictionary_2D[hist13_2D] ={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "transversaler Impuls des W Bosons in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO"}
dictionary_2D[hist14_2D]={"Xaxis":"transversale Masse des W Bosons in GeV","Yaxis": "transversaler Impuls des W Bosons in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist15_2D]={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "transversaler Impuls des W Bosons in GeV","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO"}

dictionary_2D[hist16_2D] ={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen geladenem Lepton und Neutrino","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO"}
dictionary_2D[hist17_2D]={"Xaxis":"transversale Masse des W Bosons in GeV","Yaxis": "Azimutalwinkel zwischen geladenem Lepton und Neutrino","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist18_2D]={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen geladenem Lepton und Neutrino","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO"}

#Analysephasenraum###########################################################################
 
dictionary[hist_ana] ={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des "+ boson+ " Bosons", "Color":4 }
dictionary[hist2_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist3_ana]={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist4_ana] ={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des "+ boson+ " Bosons", "Color":4 }
dictionary[hist5_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist6_ana]={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist7_ana] ={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapiditaet des "+ boson+ " Bosons", "Color":4 }
dictionary[hist8_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist9_ana]={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist10_ana] ={"Xaxis": "Azimutalwinkel", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Azimutalwinkel des "+ boson+ " Bosons", "Color":4 }
dictionary[hist11_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist12_ana]={"Xaxis": "Azimutalwinkel", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist13_ana] ={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des fuehrenden Jets", "Color":4 }
dictionary[hist14_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist15_ana]={"Xaxis": "transversaler Impuls in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist16_ana] ={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapiditaet des fuehrenden Jets", "Color":4 }
dictionary[hist17_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist18_ana]={"Xaxis": "Pseudorapiditaet", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist19_ana] ={"Xaxis": "Anzahl der Jets", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4", "Color":4 }
dictionary[hist20_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color":6 }
dictionary[hist21_ana]={"Xaxis": "Anzahl der Jets", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist22_ana] ={"Xaxis": "Summe der Transversalimpulse aller Jets in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Summe der Transversalimpulse aller Jets mit pt>=30 GeV,|eta|<=2.4", "Color":4}
dictionary[hist23_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist24_ana]={"Xaxis": "Summe der Transversalimpulse aller Jets in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist25_ana] ={"Xaxis": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und fuehrendem Jet", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und fuehrendem Jet", "Color":4 }
dictionary[hist26_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6}
dictionary[hist27_ana]={"Xaxis": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und fuehrendem Jet", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary[hist28_ana] ={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversale Masse des W Bosons", "Color":4}
dictionary[hist29_ana]={"Xaxis":" ","Yaxis": " ", "Title": " ", "Color": 6 }
dictionary[hist30_ana]={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": " ", "Color": 2 }

dictionary_2D[hist1_2D_ana] ={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "transversaler Impuls des fuehrenden Jets in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO" }
dictionary_2D[hist2_2D_ana]={"Xaxis":"transversaler Impuls des "+boson+" Bosons in GeV","Yaxis": "transversaler Impuls des fuehrenden Jets in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO" }
dictionary_2D[hist3_2D_ana]={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "transversaler Impuls des fuehrenden Jets in GeV","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO" }

dictionary_2D[hist4_2D_ana] ={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO" }
dictionary_2D[hist5_2D_ana]={"Xaxis":"transversaler Impuls des "+boson+" Bosons in GeV","Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist6_2D_ana]={"Xaxis": "transversaler Impuls des "+boson+" Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO" }

dictionary_2D[hist7_2D_ana] ={"Xaxis": "transversaler Impuls des fuehrenden Jets in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO" }
dictionary_2D[hist8_2D_ana]={"Xaxis":"transversaler Impuls des fuehrenden Jets in GeV","Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist9_2D_ana]={"Xaxis": "transversaler Impuls des fuehrenden Jets in GeV", "Yaxis": "Azimutalwinkel zwischen "+boson+" Boson und fuehrendem Jet","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO"}

dictionary_2D[hist10_2D_ana] ={"Xaxis": "Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4", "Yaxis": "Summe der pt aller Jets in GeV mit pt>=30 GeV,|eta|<=2.4","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO"}
dictionary_2D[hist11_2D_ana]={"Xaxis":"Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4","Yaxis": "Summe der pt aller Jets in GeV mit pt>=30 GeV,|eta|<=2.4","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO" }
dictionary_2D[hist12_2D_ana]={"Xaxis": "Anzahl der Jets mit pt>=30 GeV,|eta|<=2.4", "Yaxis": "Summe der pt aller Jets in GeV mit pt>=30 GeV,|eta|<=2.4","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO" }

dictionary_2D[hist13_2D_ana] ={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "transversaler Impuls des W Bosons in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO"}
dictionary_2D[hist14_2D_ana]={"Xaxis":"transversale Masse des W Bosons in GeV","Yaxis": "transversaler Impuls des W Bosons in GeV","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist15_2D_ana]={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "transversaler Impuls des W Bosons in GeV","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO"}

dictionary_2D[hist16_2D_ana] ={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen geladenem Lepton und Neutrino","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "LO"}
dictionary_2D[hist17_2D_ana]={"Xaxis":"transversale Masse des W Bosons in GeV","Yaxis": "Azimutalwinkel zwischen geladenem Lepton und Neutrino","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "NLO"}
dictionary_2D[hist18_2D_ana]={"Xaxis": "transversale Masse des W Bosons in GeV", "Yaxis": "Azimutalwinkel zwischen geladenem Lepton und Neutrino","Zaxis": "Wirkungsquerschnittsverhaeltnis NLO/LO","Title": "Verhaeltnis NLO zu LO"}

for key in dictionary:
    key.SetTitle(dictionary[key]["Title"])
    key.GetXaxis().SetTitle(dictionary[key]["Xaxis"])
    key.GetYaxis().SetTitle(dictionary[key]["Yaxis"])
    key.GetXaxis().CenterTitle()
    key.GetYaxis().CenterTitle()
    key.SetLineColor(dictionary[key]["Color"])

for key in dictionary_2D:
    key.SetTitle(dictionary_2D[key]["Title"])
    key.GetXaxis().SetTitle(dictionary_2D[key]["Xaxis"])
    key.GetYaxis().SetTitle(dictionary_2D[key]["Yaxis"])
    key.GetZaxis().SetTitle(dictionary_2D[key]["Zaxis"])
    key.GetXaxis().CenterTitle()
    key.GetYaxis().CenterTitle()
    key.GetZaxis().CenterTitle()
    
hist3.SetName(boson + "_boson_pt_theory_binning_factors")
file_factors.WriteTObject(hist3)
hist6.SetName(boson + "_boson_pt_to1TeV_factors")
file_factors.WriteTObject(hist6)
hist9.SetName(boson + "_boson_eta_factors")
file_factors.WriteTObject(hist9)
hist12.SetName(boson + "_boson_phi_factors")
file_factors.WriteTObject(hist12)
hist15.SetName(boson + "_jets_fuehrende_Ordnung_pt_factors")
file_factors.WriteTObject(hist15)
hist18.SetName(boson + "_jets_fuehrende_Ordnung_eta_factors")
file_factors.WriteTObject(hist18)
hist21.SetName(boson + "_jets_anzahl_factors")
file_factors.WriteTObject(hist21)
hist24.SetName(boson + "_jets_HT_factors")
file_factors.WriteTObject(hist24)
hist27.SetName(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_factors")
file_factors.WriteTObject(hist27)
hist30.SetName(boson + "_boson_transverse_mass_factors")
file_factors.WriteTObject(hist30)
hist3_2D.SetName(boson + "_boson_jets_fuehrende_Ordnung_pt_2D_factors")
file_factors.WriteTObject(hist3_2D)
hist6_2D.SetName(boson + "_boson_pt_DeltaPhi_2D_factors")
file_factors.WriteTObject(hist6_2D)
hist9_2D.SetName(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_factors")
file_factors.WriteTObject(hist9_2D)
hist12_2D.SetName(boson + "_jets_anzahl_HT_2D_factors")
file_factors.WriteTObject(hist12_2D)
hist15_2D.SetName(boson + "_boson_transverse_mass_pt_2D_factors")
file_factors.WriteTObject(hist15_2D)
hist18_2D.SetName(boson + "_boson_transverse_mass_phizwlundnu_2D_factors")
file_factors.WriteTObject(hist18_2D)

hist3_ana.SetName(boson + "_boson_pt_theory_binning_ana_factors")
file_factors.WriteTObject(hist3_ana)
hist6_ana.SetName(boson + "_boson_pt_to1TeV_ana_factors")
file_factors.WriteTObject(hist6_ana)
hist9_ana.SetName(boson + "_boson_eta_ana_factors")
file_factors.WriteTObject(hist9_ana)
hist12_ana.SetName(boson + "_boson_phi_ana_factors")
file_factors.WriteTObject(hist12_ana)
hist15_ana.SetName(boson + "_jets_fuehrende_Ordnung_pt_ana_factors")
file_factors.WriteTObject(hist15_ana)
hist18_ana.SetName(boson + "_jets_fuehrende_Ordnung_eta_ana_factors")
file_factors.WriteTObject(hist18_ana)
hist21_ana.SetName(boson + "_jets_anzahl_ana_factors")
file_factors.WriteTObject(hist21_ana)
hist24_ana.SetName(boson + "_jets_HT_ana_factors")
file_factors.WriteTObject(hist24_ana)
hist27_ana.SetName(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana_factors")
file_factors.WriteTObject(hist27_ana)
hist30_ana.SetName(boson + "_boson_transverse_mass_ana_factors")
file_factors.WriteTObject(hist30_ana)
hist3_2D_ana.SetName(boson + "_boson_jets_fuehrende_Ordnung_pt_2D_ana_factors")
file_factors.WriteTObject(hist3_2D_ana)
hist6_2D_ana.SetName(boson + "_boson_pt_DeltaPhi_2D_ana_factors")
file_factors.WriteTObject(hist6_2D_ana)
hist9_2D_ana.SetName(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_ana_factors")
file_factors.WriteTObject(hist9_2D_ana)
hist12_2D_ana.SetName(boson + "_jets_anzahl_HT_2D_ana_factors")
file_factors.WriteTObject(hist12_2D_ana)
hist15_2D_ana.SetName(boson + "_boson_transverse_mass_pt_2D_ana_factors")
file_factors.WriteTObject(hist15_2D_ana)
hist18_2D_ana.SetName(boson + "_boson_transverse_mass_phizwlundnu_2D_ana_factors")
file_factors.WriteTObject(hist18_2D_ana)



################################################################################################

#inklusives sample

################################################################################################
legend.AddEntry(hist, "LO", "l")
legend.AddEntry(hist2, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist.Draw("histe")
hist2.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist3.Draw("histe")
canvas.Print(boson + "_boson_pt.png")
#canvas.Print(boson + "_boson_pt.pdf")
canvas.Clear()
legend.Clear()
#########################################
legend.AddEntry(hist4, "LO", "l")
legend.AddEntry(hist5, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist4.Draw("histe")
hist5.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist6.Draw("histe")
canvas.Print(boson + "_boson_pt_to1TeV.png")
#canvas.Print(boson + "_boson_pt_to1TeV.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist7, "LO", "l")
legend.AddEntry(hist8, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist7.Draw("histe")
hist8.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist9.Draw("histe")
canvas.Print(boson + "_boson_eta.png")
#canvas.Print(boson + "_boson_eta.pdf")
canvas.Clear()
legend.Clear()
################################################
legend.AddEntry(hist10, "LO", "l")
legend.AddEntry(hist11, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist10.Draw("histe")
hist11.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist12.Draw("histe")
canvas.Print(boson + "_boson_phi.png")
#canvas.Print(boson + "_boson_phi.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist13, "LO", "l")
legend.AddEntry(hist14, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist13.Draw("histe")
hist14.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist15.Draw("histe")
canvas.Print(boson + "_jets_fuehrende_Ordnung_pt.png")
#canvas.Print(boson + "_jets_fuehrende_Ordnung_pt.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist16, "LO", "l")
legend.AddEntry(hist17, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist16.Draw("histe")
hist17.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist18.Draw("histe")
canvas.Print(boson + "_jets_fuehrende_Ordnung_eta.png")
#canvas.Print(boson + "_jets_fuehrende_Ordnung_eta.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist19, "LO", "l")
legend.AddEntry(hist20, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
canvas.cd(1).SetLogy(1)
hist19.Draw("histe")
hist20.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist21.Draw("histe")
canvas.Print(boson + "_jets_anzahl.png")
#canvas.Print(boson + "_jets_anzahl.pdf")
canvas.Clear()
legend.Clear()
##############################################
legend.AddEntry(hist22, "LO", "l")
legend.AddEntry(hist23, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist22.Draw("histe")
hist23.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist24.Draw("histe")
canvas.Print(boson + "_jets_HT.png")
#canvas.Print(boson + "_jets_HT.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist25, "LO", "l")
legend.AddEntry(hist26, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist25.Draw("histe")
hist26.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist27.Draw("histe")
canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi.png")
#canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist28, "LO", "l")
legend.AddEntry(hist29, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist28.Draw("histe")
hist29.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist30.Draw("histe")
canvas.Print(boson + "_boson_transverse_mass.png")
#canvas.Print(boson + "_boson_transverse_mass.pdf")
canvas.Clear()
legend.Clear()
##########################################
legend.AddEntry(hist1_2D, "LO", "f")
legend.AddEntry(hist2_2D, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist1_2D.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist2_2D.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist3_2D.Draw("colz")
canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_pt_2D.png")
#canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_pt_2D.pdf")
canvas.Clear()
legend.Clear()
###############################################
legend.AddEntry(hist4_2D, "LO", "f")
legend.AddEntry(hist5_2D, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist4_2D.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist5_2D.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist6_2D.Draw("colz")
canvas.Print(boson + "_boson_pt_DeltaPhi_2D.png")
#canvas.Print(boson + "_boson_pt_DeltaPhi_2D.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist7_2D, "LO", "f")
legend.AddEntry(hist8_2D, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist7_2D.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist8_2D.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist9_2D.Draw("colz")
canvas.Print(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D.png")
#canvas.Print(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist10_2D, "LO", "f")
legend.AddEntry(hist11_2D, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist10_2D.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist11_2D.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist12_2D.Draw("colz")
canvas.Print(boson + "_jets_anzahl_HT_2D.png")
#canvas.Print(boson + "_jets_anzahl_HT_2D.pdf")
canvas.Clear()
legend.Clear()
##########################################
legend.AddEntry(hist13_2D, "LO", "f")
legend.AddEntry(hist14_2D, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist13_2D.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist14_2D.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist15_2D.Draw("colz")
canvas.Print(boson + "_boson_transverse_mass_pt_2D.png")
#canvas.Print(boson + "_boson_transverse_mass_pt_2D.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist16_2D, "LO", "l")
legend.AddEntry(hist17_2D, "NLO", "l")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist16_2D.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist17_2D.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist18_2D.Draw("colz")
canvas.Print(boson + "_boson_transverse_mass_phizwlundnu_2D.png")
#canvas.Print(boson + "_boson_transverse_mass_phizwlundnu_2D.pdf")
canvas.Clear()
legend.Clear()
#########################################################################################

#inklusiver Raum und Analysephasenraum

#########################################################################################

hist7.GetYaxis().SetRangeUser(0.1,10000)

hist10.GetYaxis().SetRangeUser(0.1,10000)

hist16.GetYaxis().SetRangeUser(0.01,10000)

hist22.GetYaxis().SetRangeUser(0.01,10000)

hist25.GetYaxis().SetRangeUser(0.01,10000)

hist28.GetYaxis().SetRangeUser(0.01,10000)

##############################################################################

legend.AddEntry(hist, "LO", "l")
legend.AddEntry(hist2, "NLO", "l")
legend.AddEntry(hist_ana, "LO_ana", "l")
legend.AddEntry(hist2_ana, "NLO_ana", "l")
legend2.AddEntry(hist3, "inklusives sample", "l")
legend2.AddEntry(hist3_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist.Draw("histe")
hist2.Draw("histesame")
hist_ana.Draw("histesame")
hist2_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist3.Draw("histe")
hist3_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_boson_pt_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist4, "LO", "l")
legend.AddEntry(hist5, "NLO", "l")
legend.AddEntry(hist4_ana, "LO_ana", "l")
legend.AddEntry(hist5_ana, "NLO_ana", "l")
legend2.AddEntry(hist6, "inklusives sample", "l")
legend2.AddEntry(hist6_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist4.Draw("histe")
hist5.Draw("histesame")
hist4_ana.Draw("histesame")
hist5_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist6.Draw("histe")
hist6_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_boson_pt_to1TeV_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist7, "LO", "l")
legend.AddEntry(hist8, "NLO", "l")
legend.AddEntry(hist7_ana, "LO_ana", "l")
legend.AddEntry(hist8_ana, "NLO_ana", "l")
legend2.AddEntry(hist9, "inklusives sample", "l")
legend2.AddEntry(hist9_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist7.Draw("histe")
hist8.Draw("histesame")
hist7_ana.Draw("histesame")
hist8_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist9.Draw("histe")
hist9_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_boson_eta_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist10, "LO", "l")
legend.AddEntry(hist11, "NLO", "l")
legend.AddEntry(hist10_ana, "LO_ana", "l")
legend.AddEntry(hist11_ana, "NLO_ana", "l")
legend2.AddEntry(hist12, "inklusives sample", "l")
legend2.AddEntry(hist12_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist10.Draw("histe")
hist11.Draw("histesame")
hist10_ana.Draw("histesame")
hist11_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist12.Draw("histe")
hist12_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_boson_phi_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()


legend.AddEntry(hist13, "LO", "l")
legend.AddEntry(hist14, "NLO", "l")
legend.AddEntry(hist13_ana, "LO_ana", "l")
legend.AddEntry(hist14_ana, "NLO_ana", "l")
legend2.AddEntry(hist15, "inklusives sample", "l")
legend2.AddEntry(hist15_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist13.Draw("histe")
hist14.Draw("histesame")
hist13_ana.Draw("histesame")
hist14_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist15.Draw("histe")
hist15_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_jets_fuehrende_Ordnung_pt_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist16, "LO", "l")
legend.AddEntry(hist17, "NLO", "l")
legend.AddEntry(hist16_ana, "LO_ana", "l")
legend.AddEntry(hist17_ana, "NLO_ana", "l")
legend2.AddEntry(hist18, "inklusives sample", "l")
legend2.AddEntry(hist18_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist16.Draw("histe")
hist17.Draw("histesame")
hist16_ana.Draw("histesame")
hist17_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist18.Draw("histe")
hist18_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_jets_fuehrende_Ordnung_eta_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist19, "LO", "l")
legend.AddEntry(hist20, "NLO", "l")
legend.AddEntry(hist19_ana, "LO_ana", "l")
legend.AddEntry(hist20_ana, "NLO_ana", "l")
legend2.AddEntry(hist21, "inklusives sample", "l")
legend2.AddEntry(hist21_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist19.Draw("histe")
hist20.Draw("histesame")
hist19_ana.Draw("histesame")
hist20_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist21.Draw("histe")
hist21_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_jets_anzahl_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist22, "LO", "l")
legend.AddEntry(hist23, "NLO", "l")
legend.AddEntry(hist22_ana, "LO_ana", "l")
legend.AddEntry(hist23_ana, "NLO_ana", "l")
legend2.AddEntry(hist24, "inklusives sample", "l")
legend2.AddEntry(hist24_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist22.Draw("histe")
hist23.Draw("histesame")
hist22_ana.Draw("histesame")
hist23_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist24.Draw("histe")
hist24_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_jets_HT_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist25, "LO", "l")
legend.AddEntry(hist26, "NLO", "l")
legend.AddEntry(hist25_ana, "LO_ana", "l")
legend.AddEntry(hist26_ana, "NLO_ana", "l")
legend2.AddEntry(hist27, "inklusives sample", "l")
legend2.AddEntry(hist27_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist25.Draw("histe")
hist26.Draw("histesame")
hist25_ana.Draw("histesame")
hist26_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist27.Draw("histe")
hist27_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

legend.AddEntry(hist28, "LO", "l")
legend.AddEntry(hist29, "NLO", "l")
legend.AddEntry(hist28_ana, "LO_ana", "l")
legend.AddEntry(hist29_ana, "NLO_ana", "l")
legend2.AddEntry(hist30, "inklusives sample", "l")
legend2.AddEntry(hist30_ana, "Analysephasenraum", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist28.Draw("histe")
hist29.Draw("histesame")
hist28_ana.Draw("histesame")
hist29_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist30.Draw("histe")
hist30_ana.Draw("histesame")
legend2.Draw("same")
canvas.Print(boson + "_boson_transverse_mass_ana_inkl.png")
#canvas.Print(boson + "_boson_pt_ana_inkl.pdf")
canvas.Clear()
legend.Clear()
legend2.Clear()

######################################################################################

#Analysephasenraum

######################################################################################

legend.AddEntry(hist_ana, "LO", "l")
legend.AddEntry(hist2_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist_ana.Draw("histe")
hist2_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist3_ana.Draw("histe")
canvas.Print(boson + "_boson_pt_ana.png")
#canvas.Print(boson + "_boson_pt.pdf")
canvas.Clear()
legend.Clear()
#########################################
legend.AddEntry(hist4_ana, "LO", "l")
legend.AddEntry(hist5_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist4_ana.Draw("histe")
hist5_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist6_ana.Draw("histe")
canvas.Print(boson + "_boson_pt_to1TeV_ana.png")
#canvas.Print(boson + "_boson_pt_to1TeV.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist7_ana, "LO", "l")
legend.AddEntry(hist8_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist7_ana.Draw("histe")
hist8_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist9_ana.Draw("histe")
canvas.Print(boson + "_boson_eta_ana.png")
#canvas.Print(boson + "_boson_eta.pdf")
canvas.Clear()
legend.Clear()
################################################
legend.AddEntry(hist10_ana, "LO", "l")
legend.AddEntry(hist11_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist10_ana.Draw("histe")
hist11_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist12_ana.Draw("histe")
canvas.Print(boson + "_boson_phi_ana.png")
#canvas.Print(boson + "_boson_phi.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist13_ana, "LO", "l")
legend.AddEntry(hist14_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist13_ana.Draw("histe")
hist14_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist15_ana.Draw("histe")
canvas.Print(boson + "_jets_fuehrende_Ordnung_pt_ana.png")
#canvas.Print(boson + "_jets_fuehrende_Ordnung_pt.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist16_ana, "LO", "l")
legend.AddEntry(hist17_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist16_ana.Draw("histe")
hist17_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist18_ana.Draw("histe")
canvas.Print(boson + "_jets_fuehrende_Ordnung_eta_ana.png")
#canvas.Print(boson + "_jets_fuehrende_Ordnung_eta.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist19_ana, "LO", "l")
legend.AddEntry(hist20_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
canvas.cd(1).SetLogy(1)
hist19_ana.Draw("histe")
hist20_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist21_ana.Draw("histe")
canvas.Print(boson + "_jets_anzahl_ana.png")
#canvas.Print(boson + "_jets_anzahl.pdf")
canvas.Clear()
legend.Clear()
##############################################
legend.AddEntry(hist22_ana, "LO", "l")
legend.AddEntry(hist23_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist22_ana.Draw("histe")
hist23_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist24_ana.Draw("histe")
canvas.Print(boson + "_jets_HT_ana.png")
#canvas.Print(boson + "_jets_HT.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist25_ana, "LO", "l")
legend.AddEntry(hist26_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1)
hist25_ana.Draw("histe")
hist26_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist27_ana.Draw("histe")
canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana.png")
#canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist28_ana, "LO", "l")
legend.AddEntry(hist29_ana, "NLO", "l")
canvas.Divide(1,2)
canvas.cd(1).SetLogy(1)
canvas.cd(1)
hist28_ana.Draw("histe")
hist29_ana.Draw("histesame")
legend.Draw("same")
canvas.cd(2)
hist30_ana.Draw("histe")
canvas.Print(boson + "_boson_transverse_mass_ana.png")
#canvas.Print(boson + "_boson_transverse_mass.pdf")
canvas.Clear()
legend.Clear()
##########################################
legend.AddEntry(hist1_2D_ana, "LO", "f")
legend.AddEntry(hist2_2D_ana, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist1_2D_ana.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist2_2D_ana.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist3_2D_ana.Draw("colz")
canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_pt_2D_ana.png")
#canvas.Print(boson + "_boson_jets_fuehrende_Ordnung_pt_2D.pdf")
canvas.Clear()
legend.Clear()
###############################################
legend.AddEntry(hist4_2D_ana, "LO", "f")
legend.AddEntry(hist5_2D_ana, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist4_2D_ana.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist5_2D_ana.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist6_2D_ana.Draw("colz")
canvas.Print(boson + "_boson_pt_DeltaPhi_2D_ana.png")
#canvas.Print(boson + "_boson_pt_DeltaPhi_2D.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist7_2D_ana, "LO", "f")
legend.AddEntry(hist8_2D_ana, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist7_2D_ana.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist8_2D_ana.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist9_2D_ana.Draw("colz")
canvas.Print(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_ana.png")
#canvas.Print(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D.pdf")
canvas.Clear()
legend.Clear()
############################################
legend.AddEntry(hist10_2D_ana, "LO", "f")
legend.AddEntry(hist11_2D_ana, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist10_2D_ana.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist11_2D_ana.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist12_2D_ana.Draw("colz")
canvas.Print(boson + "_jets_anzahl_HT_2D_ana.png")
#canvas.Print(boson + "_jets_anzahl_HT_2D.pdf")
canvas.Clear()
legend.Clear()
##########################################
legend.AddEntry(hist13_2D_ana, "LO", "f")
legend.AddEntry(hist14_2D_ana, "NLO", "f")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist13_2D_ana.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist14_2D_ana.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist15_2D_ana.Draw("colz")
canvas.Print(boson + "_boson_transverse_mass_pt_2D_ana.png")
#canvas.Print(boson + "_boson_transverse_mass_pt_2D.pdf")
canvas.Clear()
legend.Clear()
###########################################
legend.AddEntry(hist16_2D_ana, "LO", "l")
legend.AddEntry(hist17_2D_ana, "NLO", "l")
canvas.Divide(1,3)
canvas.cd(1).SetLogz(1)
canvas.cd(1)
ROOT.gPad.SetRightMargin(0.2)
hist16_2D_ana.Draw("colz")
canvas.cd(2)
ROOT.gPad.SetRightMargin(0.2)
hist17_2D_ana.Draw("colz")
canvas.cd(2).SetLogz(1)
canvas.cd(3)
ROOT.gPad.SetRightMargin(0.2)
hist18_2D_ana.Draw("colz")
canvas.Print(boson + "_boson_transverse_mass_phizwlundnu_2D_ana.png")
#canvas.Print(boson + "_boson_transverse_mass_phizwlundnu_2D.pdf")
canvas.Clear()
legend.Clear()
################################################
file_factors.Close()
file_LO.Close()
file_NLO.Close()

print("finished")
