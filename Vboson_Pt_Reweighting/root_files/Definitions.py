from __future__ import print_function
import ROOT
import sys
from array import array

boson="W"

# binning according to https://arxiv.org/pdf/1705.04664.pdf
binning = [
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    200,
    250,
    300,
    350,
    400,
    450,
    500,
    550,
    600,
    650,
    700,
    750,
    800,
    850,
    900,
    950,
    1000,
    1100,
    1200,
    1300,
    1400,
    1600,
    1800,
    2000,
    2200,
    2400,
    2600,
    2800,
    3000,
    6500,
]

neue_bin_grenzen=[ 
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    200,
    250,
    300,
    350,
    400,
    500,
    650,
    1000]
neue_bins=array("d", neue_bin_grenzen)

var_info_dict = {

                         "boson_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_pt",   "boson_pt", 29, array("d", binning)) , "function" : "boson_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des "+ boson+ " Bosons"},
                         "boson_pt_to1TeV" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_pt_to1TeV",   "boson_pt_to1TeV",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "boson_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des "+ boson+ " Bosons"},
                         "boson_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_eta",   "boson_eta",20, -10, 10) , "function" : "boson_eta","Xaxis": "Pseudorapidit#ddot{a}t", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t des "+ boson+ " Bosons"},
                         "jets_fuehrende_Ordnung_pt": {"dim" : 1, "hist" : ROOT.TH1D(  "jets_fuehrende_Ordnung_pt",  "jets_fuehrende_Ordnung_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet0_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des f#ddot{u}hrenden Jets"},
                         "jets_fuehrende_Ordnung_eta": {"dim" : 1, "hist" : ROOT.TH1D(  "jets_fuehrende_Ordnung_eta",  "jets_fuehrende_Ordnung_eta", 20, -8,8) , "function" : "jet0_eta","Xaxis": "Pseudorapidit#ddot{a}t", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t des f#ddot{u}hrenden Jets"},
                         "jets_anzahl" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_anzahl",   "jets_anzahl", 13, -0.5,12.5) , "function" : "njets", "Xaxis": "Anzahl der Jets", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Anzahl der Jets mit pt>=30 GeV, |eta|<=2.4"},
                         "jets_HT" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_HT",   "jets_HT", len(neue_bin_grenzen) - 1,neue_bins) , "function" : "ht_jets","Xaxis": "Summe der Transversalimpulse aller Jets in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Summe der Transversalimpulse aller Jets mit pt>=30 GeV, |eta|<=2.4"},
                         "boson jets_fuehrende_Ordnung_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson jets_fuehrende_Ordnung_DeltaPhi",   "boson jets_fuehrende_Ordnung_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet0", "Xaxis": "Betrag des Azimutalwinkels", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und f#ddot{u}hrendem Jet"},
                         "boson_transverse_mass" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_transverse_mass",   "boson_transverse_mass", 20, 0,120) , "function" : "transverse_mass", "Xaxis": "Transversale Masse in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversale Masse des " + boson +" Bosons"},
                         "geladenes_lepton_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "geladenes_lepton_pt",   "geladenes_lepton_pt", len(neue_bin_grenzen) - 1,neue_bins) , "function" : "charged_lepton_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des geladenen Leptons"},
                         "geladenes_lepton_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "geladenes_lepton_eta",   "geladenes_lepton_eta", 20, -10, 10) , "function" : "charged_lepton_eta", "Xaxis": "Pseudorapidit#ddot{a}t", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t des geladenen Leptons"},
                         "boson_invariant_mass" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_invariant_mass",   "boson_invariant_mass",20, 0, 110) , "function" : "boson_mass", "Xaxis": "Invariante Masse in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Invariante Masse des " + boson +" Bosons"},
                         "jets_NLO_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_NLO_pt",  "jets_NLO_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet1_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des zweiten Jets"},
                         "jets_NLO_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_NLO_eta",  "jets_NLO_eta", 20, -8,8) , "function" : "jet1_eta", "Xaxis": "Pseudorapidit#ddot{a}t", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t des zweiten Jets"},
                         "jets_NNLO_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_NNLO_pt",  "jets_NNLO_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet2_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des dritten Jets"},
                         "jets_NNLO_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_NNLO_eta",  "jets_NNLO_eta", 20, -8,8) , "function" : "jet2_eta", "Xaxis": "Pseudorapidit#ddot{a}t", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t des dritten Jets"},
                         "jets_NNNLO_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_NNNLO_pt",  "jets_NNNLO_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet3_pt", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Transversalimpuls des vierten Jets"},
                         "jets_NNNLO_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "jets_NNNLO_eta",  "jets_NNNLO_eta", 20, -8,8) , "function" : "jet3_eta", "Xaxis": "Pseudorapidit#ddot{a}t", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t des vierten Jets"},
                         "boson_jets_NLO_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_jets_NLO_DeltaPhi",   "boson_jets_NLO_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet1", "Xaxis": "Betrag des Azimutalwinkels", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und zweitem Jet"},
                         "boson_jets_NNLO_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_jets_NNLO_DeltaPhi",   "boson_jets_NNLO_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet2", "Xaxis": "Betrag des Azimutalwinkels", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und drittem Jet"},
                         "boson_jets_NNNLO_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "boson_jets_NNNLO_DeltaPhi",   "boson_jets_NNNLO_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet3", "Xaxis": "Betrag des Azimutalwinkels", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und viertem Jet"},
                         "DeltaPhi_decay_prods" : {"dim" : 1, "hist" : ROOT.TH1D(  "DeltaPhi_decay_prods",  "DeltaPhi_decay_prods", 10,0,3.14) , "function" : "deltaphi_decay_prods", "Xaxis": "Betrag des Azimutalwinkels", "Yaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen den Zerfallsprodukten des " + boson + " Bosons"},
                       
                       
                         "boson_pt_eta" : {"dim" : 2, "hist" : ROOT.TH2D(  "boson_pt_eta",   "boson_pt_eta",len(neue_bin_grenzen) - 1,neue_bins,20, -10, 10) , "function1" : "boson_pt" , "function2" : "boson_eta", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Pseudorapidit#ddot{a}t", "Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Pseudorapidit#ddot{a}t als Funktion des Transversalimpulses des "+boson+" Bosons"},
                         "boson_pt_DeltaPhi" : {"dim" : 2, "hist" : ROOT.TH2D(  "boson_pt_DeltaPhi",   "boson_pt_DeltaPhi", len(neue_bin_grenzen) - 1,neue_bins, 20, 0, 3.14) , "function1" : "boson_pt" , "function2" : "deltaphi_boson_jet0","Xaxis": "Transversalimpuls in GeV", "Yaxis": "Betrag des Azimutalwinkels","Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Betrag des Azimutalwinkels zwischen "+boson+" Boson und f#ddot{u}hrendem Jet als Funktion des Transversalimpulses des "+boson+" Bosons"},
                         "boson_pt_HT" : {"dim" : 2, "hist" : ROOT.TH2D(  "boson_pt_HT",   "boson_pt_HT",len(neue_bin_grenzen) - 1,neue_bins,len(neue_bin_grenzen) - 1,neue_bins) , "function1" : "boson_pt" , "function2" : "ht_jets","Xaxis": "Transversalimpuls in GeV", "Yaxis": "#splitline{{{0}}}{{{1}}}".format("Summe der Transversalimpulse","aller Jets in GeV"),"Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Summe der Transversalimpulse aller Jets mit pt>=30 GeV, |eta|<=2.4 als Funktion des Transversalimpulses des "+boson+" Bosons"},
                         "boson_pt_anzahl" : {"dim" : 2, "hist" : ROOT.TH2D(  "boson_pt_anzahl",   "boson_pt_anzahl",len(neue_bin_grenzen) - 1,neue_bins,13, -0.5,12.5) , "function1" : "boson_pt" , "function2" : "njets", "Xaxis": "Transversalimpuls in GeV", "Yaxis": "Anzahl der Jets", "Zaxis": "Wirkungsquerschnitt in pb pro Bin", "Title": "Anzahl der Jets mit pt>=30 GeV, |eta|<=2.4 als Funktion des Transversalimpulses des "+boson+" Bosons"}
                       
                   }
