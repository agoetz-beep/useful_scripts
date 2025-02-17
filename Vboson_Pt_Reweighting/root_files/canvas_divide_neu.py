import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys
from Definitions import var_info_dict

boson=sys.argv[1]
file_LO=ROOT.TFile.Open(sys.argv[2])
file_NLO=ROOT.TFile.Open(sys.argv[3])
#file_factors=ROOT.TFile(boson + "_factors.root", "RECREATE")

canvas=ROOT.TCanvas("canvas", "canvas", 4000, 3000)

legend=ROOT.TLegend(0.15,0.15)
legend2=ROOT.TLegend(0.15,0.15)

latex=ROOT.TLatex()

corr_factor_dict = { 
                            "" : "",
                            "Vpt_corr_factor_incl" :" mit Korrekturfaktor (Vpt, inklusiver Phasenraum)",
                            "Vpt_theory_binning_corr_factor_incl" : " mit Korrekturfaktor (Vpt, inklusiver Phasenraum, Theorie-Binning)",
                            "Vpt_corr_factor_ana" : " mit Korrekturfaktor (Vpt, Analysephasenraum)",
                            "Vpt_theory_binning_corr_factor_ana" : " mit Korrekturfaktor (Vpt, Analysephasenraum, Theorie-Binning)",
                            "Vpt_Veta_corr_factor_incl" : " mit Korrekturfaktor (Vpt_Veta, inklusiver Phasenraum)",
                            "Vpt_DeltaPhi_corr_factor_incl" : " mit Korrekturfaktor (Vpt_Deltaphi, inklusiver Phasenraum)",
                            "Vpt_HT_corr_factor_incl" : " mit Korrekturfaktor (Vpt_HT, inklusiver Phasenraum)",
                            "Vpt_anzahl_corr_factor_incl" : " mit Korrekturfaktor (Vpt_anzahl, inklusiver Phasenraum)"
                            
                        }

sel_func_dict = {"incl" : {"Title": " im inklusiven Phasenraum"} , "ana" : {"Title": " im Analysephasenraum"}}

histo_dict = {"LO":{}, "NLO":{}, "ratio":{}}

for key in var_info_dict:
    for key_ in corr_factor_dict:
        for key__ in sel_func_dict:
            histo_dict["LO"][key__+"_"+key+"_"+key_]=file_LO.Get(boson+"_"+key__+"_"+key+"_"+key_)
            histo_dict["NLO"][key__+"_"+key+"_"+key_]=file_NLO.Get(boson+"_"+key__+"_"+key+"_"+"")
            histo_dict["ratio"][key__+"_"+key+"_"+key_]=histo_dict["NLO"][key__+"_"+key+"_"+key_].Clone()
            histo_dict["ratio"][key__+"_"+key+"_"+key_].Divide(histo_dict["LO"][key__+"_"+key+"_"+key_])
            for key___ in histo_dict:
                histo_dict[key___][key__+"_"+key+"_"+key_].SetName(boson+"_"+key__+"_"+key+"_"+key_)
                histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetTitle(var_info_dict[key]["Xaxis"])
                histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().CenterTitle()
                histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetTitleSize(0.049)
                histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetLabelSize(0.05)
                histo_dict[key___][key__+"_"+key+"_"+key_].GetYaxis().SetTitle(var_info_dict[key]["Yaxis"])
                histo_dict[key___][key__+"_"+key+"_"+key_].GetYaxis().CenterTitle()
                histo_dict[key___][key__+"_"+key+"_"+key_].GetYaxis().SetTitleSize(0.049)
                histo_dict[key___][key__+"_"+key+"_"+key_].GetYaxis().SetLabelSize(0.05)
            if var_info_dict[key]["dim"] == 1:
                if key__ == "incl":
                    histo_dict["LO"][key__+"_"+key+"_"+key_].SetLineColor(1)
                    histo_dict["NLO"][key__+"_"+key+"_"+key_].SetLineColor(2)
                    histo_dict["ratio"][key__+"_"+key+"_"+key_].SetLineColor(1)
                    if key_ == "":
                        histo_dict["ratio"][key__+"_"+key+"_"+key_].SetLineColor(1)
                    maximum_NLO=histo_dict["NLO"][key__+"_"+key+"_"+key_].GetMaximum()
                    maximum_LO=histo_dict["LO"][key__+"_"+key+"_"+key_].GetMaximum()
                    maximum_NLO=histo_dict["NLO"][key__+"_"+key+"_"+key_].GetMaximum()
                    maximum_ratio=histo_dict["ratio"][key__+"_"+key+"_"+key_].GetMaximum()
                    minimum_LO=histo_dict["LO"][key__+"_"+key+"_"+key_].GetMinimum()
                    minimum_NLO=histo_dict["NLO"][key__+"_"+key+"_"+key_].GetMinimum()
                    minimum_ratio=histo_dict["ratio"][key__+"_"+key+"_"+key_].GetMinimum()
                    if maximum_LO > maximum_NLO:
                        maximum_LONLO = maximum_LO
                    else:
                        maximum_LONLO = maximum_NLO
                    if minimum_LO < minimum_NLO:
                        minimum_LONLO = minimum_LO
                    else:
                        minimum_LONLO = minimum_NLO
                else:
                    histo_dict["LO"][key__+"_"+key+"_"+key_].SetLineColor(4)
                    histo_dict["NLO"][key__+"_"+key+"_"+key_].SetLineColor(6)
                    histo_dict["ratio"][key__+"_"+key+"_"+key_].SetLineColor(2)
                    maximum_LO_ana=histo_dict["LO"][key__+"_"+key+"_"+key_].GetMaximum()
                    maximum_NLO_ana=histo_dict["NLO"][key__+"_"+key+"_"+key_].GetMaximum()
                    maximum_ratio_ana=histo_dict["ratio"][key__+"_"+key+"_"+key_].GetMaximum()
                    minimum_LO_ana=histo_dict["LO"][key__+"_"+key+"_"+key_].GetMinimum()
                    minimum_NLO_ana=histo_dict["NLO"][key__+"_"+key+"_"+key_].GetMinimum()
                    minimum_ratio_ana=histo_dict["ratio"][key__+"_"+key+"_"+key_].GetMinimum()
                    if maximum_LO_ana > maximum_NLO_ana:
                        maximum_LONLO_ana = maximum_LO_ana
                    else:
                        maximum_LONLO_ana = maximum_NLO_ana
                    if minimum_LO_ana < minimum_NLO_ana:
                        minimum_LONLO_ana = minimum_LO_ana
                    else:
                        minimum_LONLO_ana = minimum_NLO_ana
                    if maximum_LONLO > maximum_LONLO_ana:
                        maximum_LONLO_final = maximum_LONLO*1.2
                    else:
                        maximum_LONLO_final = maximum_LONLO_ana*1.2
                    if minimum_LONLO < minimum_LONLO_ana:
                        minimum_LONLO_final = minimum_LONLO*0.8
                    else:
                        minimum_LONLO_final = minimum_LONLO_ana*0.8
                    if maximum_ratio > maximum_ratio_ana:
                        maximum_ratio_final = maximum_ratio*1.2
                    else:
                        maximum_ratio_final = maximum_ratio_ana*1.2
                    if minimum_ratio < minimum_ratio_ana:
                        minimum_ratio_final = minimum_ratio*0.8
                    else:
                        minimum_ratio_final = minimum_ratio_ana*0.8
                    if minimum_LONLO_final<0 or minimum_LONLO_final==0 :
                        histo_dict["LO"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(0.001,maximum_LONLO_final)
                        histo_dict["NLO"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(0.001,maximum_LONLO_final)
                    else:
                        histo_dict["LO"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(minimum_LONLO_final,maximum_LONLO_final)
                        histo_dict["NLO"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(minimum_LONLO_final,maximum_LONLO_final)
                    if minimum_ratio_final<0 or minimum_ratio_final==0:
                        histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(0.001,maximum_ratio_final)
                    else:
                        histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(minimum_ratio_final,maximum_ratio_final)
                histo_dict["LO"][key__+"_"+key+"_"+key_].SetTitle(var_info_dict[key]["Title"] + corr_factor_dict[key_])
                if key =="boson_pt":
                    histo_dict["LO"][key__+"_"+key+"_"+key_].SetTitle(var_info_dict[key]["Title"] + corr_factor_dict[key_]+ " mit Theorie-Binning")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].SetTitle("")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().SetTitle("Wikungsquerschnittsverhaeltnis NLO/LO")
                #histo_dict["ratio"][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(0,2)
                for key___ in histo_dict:
                    if key =="boson_eta" or key =="geladenes_lepton_eta" or key=="jets_fuehrende_Ordnung_eta" or key=="jets_NLO_eta" or key=="jets_NNLO_eta" or key=="jets_NNNLO_eta":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetRangeUser(-5,5)
                    if key =="boson_invariant_mass":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetRangeUser(50,110)
                    if key =="boson_transverse_mass":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetRangeUser(0,120)
                    if key =="jets_anzahl":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetRangeUser(0,8)
                    if key =="jets_NNLO_pt":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetRangeUser(0,700)
                    if key =="jets_NNNLO_pt":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetXaxis().SetRangeUser(0,500)
            if var_info_dict[key]["dim"] == 2:
                for key___ in histo_dict:
                    histo_dict[key___][key__+"_"+key+"_"+key_].GetZaxis().SetTitle(var_info_dict[key]["Zaxis"])
                    histo_dict[key___][key__+"_"+key+"_"+key_].GetZaxis().CenterTitle()
                    histo_dict[key___][key__+"_"+key+"_"+key_].GetZaxis().SetTitleSize(0.049)
                    histo_dict[key___][key__+"_"+key+"_"+key_].GetZaxis().SetLabelSize(0.05)
                    if key =="boson_pt_anzahl":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(0,6)
                    if key =="boson_pt_eta":
                        histo_dict[key___][key__+"_"+key+"_"+key_].GetYaxis().SetRangeUser(-5,5)
                    if key__ == "incl":
                        maximum_incl=histo_dict[key___][key__+"_"+key+"_"+key_].GetMaximum()
                        minimum_incl=histo_dict[key___][key__+"_"+key+"_"+key_].GetMinimum()
                    if key__ == "ana":
                        maximum_ana=histo_dict[key___][key__+"_"+key+"_"+key_].GetMaximum()
                        minimum_ana=histo_dict[key___][key__+"_"+key+"_"+key_].GetMinimum()
                        if maximum_incl > maximum_ana:
                            maximum_final = maximum_incl*1.2
                        else:
                            maximum_final = maximum_ana*1.2
                        if minimum_incl < minimum_ana:
                            minimum_final = minimum_incl*0.8
                        else:
                            minimum_final = minimum_ana*0.8
                        if minimum_final<0:
                            histo_dict[key___][key__+"_"+key+"_"+key_].GetZaxis().SetRangeUser(0,maximum_final)
                        else:
                            histo_dict[key___][key__+"_"+key+"_"+key_].GetZaxis().SetRangeUser(minimum_final,maximum_final)
                        if key___ == "LO":
                            maximum_final_LO = maximum_final
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetZaxis().SetTitle("Wikunsquerschnittsverhaeltnis NLO/LO")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].GetZaxis().CenterTitle()
                #histo_dict["ratio"][key__+"_"+key+"_"+key_].GetZaxis().SetRangeUser(0,2)
                histo_dict["LO"][key__+"_"+key+"_"+key_].SetTitle("#splitline{{{0}}}{{{1}}}".format(var_info_dict[key]["Title"] + sel_func_dict[key__]["Title"] + corr_factor_dict[key_]," -LO"))
                histo_dict["NLO"][key__+"_"+key+"_"+key_].SetTitle(" -NLO")
                histo_dict["ratio"][key__+"_"+key+"_"+key_].SetTitle(" -Verhaeltnis NLO zu LO")
            #histo_dict["ratio"][key__+"_"+key+"_"+key_].SetName(boson +"_"+key__+"_"+key+"_corr_factor")
            #file_factors.WriteTObject(histo_dict["ratio"][key__+"_"+key+"_"+key_])
                

            
for key in var_info_dict:
    for key_ in corr_factor_dict:
        if var_info_dict[key]["dim"] == 1:
            canvas.Divide(1,2)
            for key__ in sel_func_dict:
                if key__ == "incl":
                    legend.AddEntry(histo_dict["LO"][key__+"_"+key+"_"+key_], "LO +<=4 Jets, inklusiver Phasenraum", "l")
                    legend.AddEntry(histo_dict["NLO"][key__+"_"+key+"_"+key_], "NLO +<=2 Jets, inklusiver Phasenraum", "l")
                    legend2.AddEntry(histo_dict["ratio"][key__+"_"+key+"_"+key_], "inklusiver Phasenraum", "l")
                if key__ == "ana":
                    legend.AddEntry(histo_dict["LO"][key__+"_"+key+"_"+key_], "LO +<=4 Jets, Analysephasenraum", "l")
                    legend.AddEntry(histo_dict["NLO"][key__+"_"+key+"_"+key_], "NLO +<=2 Jets, Analysephasenraum", "l")
                    legend2.AddEntry(histo_dict["ratio"][key__+"_"+key+"_"+key_], "Analysephasenraum", "l")
                if key == "boson_pt" or key =="boson_pt_to1TeV" or key=="jets_fuehrende_Ordnung_pt" or key=="jets_HT" or key=="boson_transverse_mass" or key=="geladenes_lepton_pt" or key=="boson_invariant_mass" or key=="jets_NLO_pt" or key=="jets_NNLO_pt" or key=="jets_NNNLO_pt" or key=="jets_anzahl":
                    canvas.cd(1).SetLogy(1)
                canvas.cd(1)
                if key__ == "incl":
                    histo_dict["LO"][key__+"_"+key+"_"+key_].Draw("histe")
                    histo_dict["NLO"][key__+"_"+key+"_"+key_].Draw("histesame")
                if key__ == "ana":
                    histo_dict["LO"][key__+"_"+key+"_"+key_].Draw("histesame")
                    histo_dict["NLO"][key__+"_"+key+"_"+key_].Draw("histesame")
                legend.Draw("same")
                latex.SetTextSize(0.03)
                latex.DrawLatexNDC(0.00001,0.95,"#splitline{{{0}}}{{{1}}}".format("CMS simulation","work in progress"))
                canvas.cd(2)
                if key__ == "incl":
                    histo_dict["ratio"][key__+"_"+key+"_"+key_].Draw("histe")
                if key__ == "ana":
                    histo_dict["ratio"][key__+"_"+key+"_"+key_].Draw("histesame")
                legend2.Draw("same")
            canvas.Print(boson + "_"+key+"_"+key_+ ".png")
            canvas.Print(boson +"_"+key+"_"+key_+ ".pdf")
            canvas.Clear()
            legend.Clear()
            legend2.Clear()
            latex.Clear()
        if var_info_dict[key]["dim"] == 2:  
            for key__ in sel_func_dict:
                canvas.Divide(1,3)
                canvas.cd(1)
                canvas.cd(1).SetLogz(1)
                #canvas.cd(1).SetTitle("-LO")
                ROOT.gPad.SetRightMargin(0.2)
                histo_dict["LO"][key__+"_"+key+"_"+key_].Draw("colz")
                latex.SetTextSize(0.03)
                latex.DrawLatexNDC(0.00001,0.95,"#splitline{{{0}}}{{{1}}}".format("CMS simulation","work in progress"))
                canvas.cd(2)
                canvas.cd(2).SetLogz(1)
                ROOT.gPad.SetRightMargin(0.2)
                histo_dict["NLO"][key__+"_"+key+"_"+key_].Draw("colz")
                canvas.cd(3)
                ROOT.gPad.SetRightMargin(0.2)
                histo_dict["ratio"][key__+"_"+key+"_"+key_].Draw("colz")
                canvas.Print(boson + "_"+key__+"_"+key+"_"+key_+ ".png")
                canvas.Print(boson + "_"+key__+"_"+key+"_"+key_+ ".pdf")
                canvas.Clear()
                latex.Clear()
                
#file_factors.Close()
file_LO.Close()
file_NLO.Close()

print("finished")                
                
            
            
