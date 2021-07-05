import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys
from Definitions import var_info_dict

boson=sys.argv[1]
file_LO=ROOT.TFile.Open(sys.argv[2])
file_NLO=ROOT.TFile.Open(sys.argv[3])
file_factors=ROOT.TFile(boson + "_factors.root", "RECREATE")

canvas=ROOT.TCanvas("canvas", "canvas", 4000, 3000)

legend=ROOT.TLegend(0.15,0.15)
legend2=ROOT.TLegend(0.15,0.15)

corr_factor_dict = { 
                            "" : "",
#                            "Vpt_corr_factor_incl" :" mit Korrekturfaktor (Vpt, inklusiver Phasenraum)",
#                           "Vpt_theory_binning_corr_factor_incl" : " mit Korrekturfaktor (Vpt, inklusiver Phasenraum, Theorie-Binning)",
#                            "Vpt_corr_factor_ana" : " mit Korrekturfaktor (Vpt, Analysephasenraum)",
#                            "Vpt_theory_binning_corr_factor_ana" : " mit Korrekturfaktor (Vpt, Analysephasenraum, Theorie-Binning)",
#                            "Vpt_Veta_corr_factor_incl" : " mit Korrekturfaktor (Vpt_Veta, inklusiver Phasenraum)",
#                            "Vpt_DeltaPhi_corr_factor_incl" : " mit Korrekturfaktor (Vpt_Deltaphi, inklusiver Phasenraum)",
#                            "Vpt_HT_corr_factor_incl" : " mit Korrekturfaktor (Vpt_HT, inklusiver Phasenraum)",
#                            "Vpt_anzahl_corr_factor_incl" : " mit Korrekturfaktor (Vpt_anzahl, inklusiver Phasenraum)"
                            
                        }

sel_func_dict = {"incl" : {"Title": " im inklusiven Phasenraum"} , "ana" : {"Title": " im Analysephasenraum"}}

histo_dict = {"LO":{}, "NLO":{}, "ratio":{}}

for key in var_info_dict:
    for key_ in corr_factor_dict:
        for key__ in sel_func_dict:
            histo_dict["LO"][key__+"_"+key+"_"+key_]=file_LO.Get(boson+"_"+key__+"_"+key+"_"+key_)
            histo_dict["NLO"][key__+"_"+key+"_"+key_]=file_NLO.Get(boson+"_"+key__+"_"+key+"_"+key_)
            histo_dict["ratio"][key__+"_"+key+"_"+key_]=histo_dict["NLO"][key__+"_"+key+"_"+key_].Clone()
            histo_dict["ratio"][key__+"_"+key+"_"+key_].Divide(histo_dict["LO"][key__+"_"+key+"_"+key_])
            for key___ in histo_dict:
                histo_dict[key__+"_"+key+"_"+key_].SetName(boson+"_"+key__+"_"+key+"_"+key_)
                histo_dict[key__+"_"+key+"_"+key_].GetXaxis().SetTitle(var_info_dict[key]["Xaxis"])
                histo_dict[key__+"_"+key+"_"+key_].GetXaxis().CenterTitle()
                histo_dict[key__+"_"+key+"_"+key_].GetYaxis().SetTitle(var_info_dict[key]["Yaxis"])
                histo_dict[key__+"_"+key+"_"+key_].GetYaxis().CenterTitle()
            if var_info_dict[key]["dim"] == 1:
                if key__ == incl:
                    histo_dict["LO"][key__+"_"+key+"_"+key_].SetLineColor(1)
                    histo_dict["NLO"][key__+"_"+key+"_"+key_].SetLineColor(2)
                    histo_dict["ratio"][key__+"_"+key+"_"+key_].SetLineColor(1)
                if key__ == ana:
                    histo_dict["LO"][key__+"_"+key+"_"+key_].SetLineColor(4)
                    histo_dict["NLO"][key__+"_"+key+"_"+key_].SetLineColor(6)
                    histo_dict["ratio"][key__+"_"+key+"_"+key_].SetLineColor(2)
                histo_dict["LO"][key__+"_"+key+"_"+key_].SetTitle(var_info_dict[key]["Title"] + sel_func_dict[key__]["Title"] + corr_factor_dict[key_])
                histo_dict["NLO"][key__+"_"+key+"_"+key_].SetTitle("")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().SetTitle("Wikunsquerschnittsverhaeltnis NLO/LO")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().CenterTitle()
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(0,2)
            if var_info_dict[key]["dim"] == 2:
                for key___ in histo_dict:
                    histo_dict[key__+"_"+key+"_"+key_].GetZaxis().SetTitle(var_info_dict[key]["Zaxis"])
                    histo_dict[key__+"_"+key+"_"+key_].GetZaxis().CenterTitle()
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetZaxis().SetTitle("Wikunsquerschnittsverhaeltnis NLO/LO")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetZaxis().CenterTitle()
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetZaxis().SetRangeUser(0,2)
                histo_dict["LO"][key__+"_"+key+"_"+key_].SetTitle(var_info_dict[key]["Title"] + sel_func_dict[key__]["Title"] + corr_factor_dict[key_]+" -LO")
                histo_dict["NLO"][key__+"_"+key+"_"+key_].SetTitle(" -NLO")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].SetTitle(" -Verhaeltnis NLO zu LO")
            histo_dict["ratio"][key__+"_"+key+"_"+key_].SetName(boson + "_"+ key_)
            file_factors.WriteTObject(histo_dict["ratio"][key__+"_"+key+"_"+key_])
                
                
                
                
file_factors.Close()
file_LO.Close()
file_NLO.Close()

print("finished")                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
