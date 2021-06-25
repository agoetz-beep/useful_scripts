from ROOT import TH1D,TH2D


var_info_dict = {
                       ### 1D ###
                         "_boson_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_pt",   "_boson_pt", 29, array("d", binning)) , "function" : "boson_pt"},
                         "_boson_pt_to1TeV" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_pt_to1TeV",   "_boson_pt_to1TeV",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "boson_pt"},
                         "_boson_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_eta",   "_boson_eta",20, -10, 10) , "function" : "boson_eta"},
                         "_jets_fuehrende_Ordnung_pt": {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_fuehrende_Ordnung_pt",  "_jets_fuehrende_Ordnung_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet0_pt"},
                         "_jets_fuehrende_Ordnung_eta": {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_fuehrende_Ordnung_eta",  "_jets_fuehrende_Ordnung_eta", 20, -8,8) , "function" : "jet0_eta"},
                         "_jets_anzahl" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_anzahl",   "_jets_anzahl", 13, -0.5,12.5) , "function" : "njets"},
                         "_jets_HT" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_HT",   "_jets_HT", len(neue_bin_grenzen) - 1,neue_bins) , "function" : "ht_jets"},
                         "_boson_jets_fuehrende_Ordnung_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_jets_fuehrende_Ordnung_DeltaPhi",   "_boson_jets_fuehrende_Ordnung_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet0"},
                         "_boson_transverse_mass" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_transverse_mass",   "_boson_transverse_mass", 20, 0,100) , "function" : "transverse_mass"},
                         "_geladenes_lepton_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "_geladenes_lepton_pt",   "_geladenes_lepton_pt", len(neue_bin_grenzen) - 1,neue_bins) , "function" : "charged_lepton_pt"},
                         "_geladenes_lepton_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "_geladenes_lepton_eta",   "_geladenes_lepton_eta", 20, -10, 10) , "function" : "charged_lepton_eta"},
                         "_boson_invariant_mass" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_invariant_mass",   "_boson_invariant_mass",20, 0, 100) , "function" : "boson_mass"},
                         "_jets_NLO_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_NLO_pt",  "_jets_NLO_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet1_pt"},
                         "_jets_NLO_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_NLO_eta",  "_jets_NLO_eta", 20, -8,8) , "function" : "jet1_eta"},
                         "_jets_NNLO_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_NNLO_pt",  "_jets_NNLO_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet2_pt"},
                         "_jets_NNLO_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_NNLO_eta",  "_jets_NNLO_eta", 20, -8,8) , "function" : "jet2_eta"},
                         "_jets_NNNLO_pt" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_NNNLO_pt",  "_jets_NNNLO_pt",len(neue_bin_grenzen) - 1,neue_bins) , "function" : "jet3_pt"},
                         "_jets_NNNLO_eta" : {"dim" : 1, "hist" : ROOT.TH1D(  "_jets_NNNLO_eta",  "_jets_NNNLO_eta", 20, -8,8) , "function" : "jet3_eta"},
                         "_boson_jets_NLO_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_jets_NLO_DeltaPhi",   "_boson_jets_NLO_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet1"},
                         "_boson_jets_NNLO_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_jets_NNLO_DeltaPhi",   "_boson_jets_NNLO_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet2"},
                         "_boson_jets_NNNLO_DeltaPhi" : {"dim" : 1, "hist" : ROOT.TH1D(  "_boson_jets_NNNLO_DeltaPhi",   "_boson_jets_NNNLO_DeltaPhi", 20, 0, 3.14) , "function" : "deltaphi_boson_jet3"},
                         "_DeltaPhi_decay_prods" : {"dim" : 1, "hist" : ROOT.TH1D(  "_DeltaPhi_decay_prods",  "_DeltaPhi_decay_prods", 10,0,3.14) , "function" : "deltaphi_decay_prods"},
                       
                       
                       ### 2D ###
                         "_boson_pt_eta" : {"dim" : 2, "hist" : ROOT.TH2D(  "_boson_pt_eta",   "_boson_pt_eta",len(neue_bin_grenzen) - 1,neue_bins,20, -10, 10) , "function1" : "boson_pt" , "function2" : "boson_eta"},
                         "_boson_pt_DeltaPhi" : {"dim" : 2, "hist" : ROOT.TH2D(  "_boson_pt_DeltaPhi",   "_boson_pt_DeltaPhi", len(neue_bin_grenzen) - 1,neue_bins, 20, 0, 3.14) , "function1" : "boson_pt" , "function2" : "deltaphi_boson_jet0"},
                         "_boson_pt_HT" : {"dim" : 2, "hist" : ROOT.TH2D(  "_boson_pt_HT",   "_boson_pt_HT",len(neue_bin_grenzen) - 1,neue_bins,len(neue_bin_grenzen) - 1,neue_bins) , "function1" : "boson_pt" , "function2" : "ht_jets"},
                         "_boson_pt_anzahl" : {"dim" : 2, "hist" : ROOT.TH2D(  "_boson_pt_anzahl",   "_boson_pt_anzahl",len(neue_bin_grenzen) - 1,neue_bins,13, -0.5,12.5) , "function1" : "boson_pt" , "function2" : "njets"}
                       
                   }
