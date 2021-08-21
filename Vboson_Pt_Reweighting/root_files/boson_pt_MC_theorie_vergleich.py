import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys 
from array import array

canvas=ROOT.TCanvas("canvas", "canvas", 4000, 3000)
legend=ROOT.TLegend(0.17,0.27)
legend2=ROOT.TLegend(0.17,0.17)
latex=ROOT.TLatex()

boson=sys.argv[1]
evj_eej=sys.argv[2]
file_evj_eej=ROOT.TFile.Open(sys.argv[3])
file_MC_LO=ROOT.TFile.Open(sys.argv[4])
file_MC_NLO=ROOT.TFile.Open(sys.argv[5])

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
    1000
]

hist_evj_eej_LO=file_evj_eej.Get(evj_eej + "_pTV_LO")
hist_evj_eej_NLO=file_evj_eej.Get(evj_eej + "_pTV_NLO")
hist_evj_eej_NNLO=file_evj_eej.Get(evj_eej + "_pTV_NNLO")
hist_MC_LO=file_MC_LO.Get(boson + "_incl_boson_pt_")
hist_MC_NLO=file_MC_NLO.Get(boson + "_incl_boson_pt_")

hist_evj_eej_LO.Scale(3)
hist_evj_eej_NLO.Scale(3)
hist_evj_eej_NNLO.Scale(3)
hist_evj_eej_LO.SetLineColor(1)
hist_evj_eej_NLO.SetLineColor(2)
hist_evj_eej_NNLO.SetLineColor(7)
hist_MC_LO.SetLineColor(4)
hist_MC_NLO.SetLineColor(6)
hist_evj_eej_LO.GetXaxis().SetTitle("Transversalimpuls in GeV") 
hist_evj_eej_LO.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")
hist_evj_eej_LO.SetTitle("")
hist_evj_eej_LO.GetXaxis().CenterTitle()
hist_evj_eej_LO.GetYaxis().CenterTitle()
hist_evj_eej_LO.GetXaxis().SetTitleSize(0.049)
hist_evj_eej_LO.GetYaxis().SetTitleSize(0.049)
hist_evj_eej_LO.GetXaxis().SetLabelSize(0.05)
hist_evj_eej_LO.GetYaxis().SetLabelSize(0.05)
hist_evj_eej_LO.GetXaxis().SetRangeUser(30,1000)
legend.AddEntry(hist_MC_LO, "LO +<=4 Jets, MC Simulation", "l")
legend.AddEntry(hist_MC_NLO, "NLO +<=2 Jets, MC Simulation", "l")
legend.AddEntry(hist_evj_eej_LO, "LO , Theorie-Verteilung", "l")
legend.AddEntry(hist_evj_eej_NLO, "NLO, Theorie-Verteilung", "l")
legend.AddEntry(hist_evj_eej_NNLO, "NNLO, Theorie-Verteilung", "l")

hist_ratio_LO_theorie=hist_evj_eej_LO.Clone()
hist_ratio_LO_theorie.Divide(hist_evj_eej_NLO)
hist_ratio_NNLO_theorie=hist_evj_eej_NNLO.Clone()
hist_ratio_NNLO_theorie.Divide(hist_evj_eej_NLO)
neue_bins=array("d", binning)
neues_NLO_theorie_histogramm=hist_evj_eej_NLO.Rebin(len(binning)-1,boson+ "_boson_pt_neue_grenzen",neue_bins)
hist_ratio_LO_MC=hist_MC_LO.Clone()
hist_ratio_LO_MC.Divide(neues_NLO_theorie_histogramm)
hist_ratio_NLO_MC=hist_MC_NLO.Clone()
hist_ratio_NLO_MC.Divide(neues_NLO_theorie_histogramm)


hist_ratio_LO_theorie.SetLineColor(1)
#hist_evj_eej_NLO.SetLineColor(2)
hist_ratio_NNLO_theorie.SetLineColor(7)
hist_ratio_LO_MC.SetLineColor(4)
hist_ratio_NLO_MC.SetLineColor(6)
hist_ratio_LO_MC.GetXaxis().SetTitle("Transversalimpuls in GeV") 
hist_ratio_LO_MC.GetYaxis().SetTitle("#splitline{{{0}}}{{{1}}}".format("Wirkungsquerschnittsverh#ddot{a}ltnis zu NLO"," der Theorie-Verteilung"))
hist_ratio_LO_MC.SetTitle("")
hist_ratio_LO_MC.GetXaxis().CenterTitle()
hist_ratio_LO_MC.GetYaxis().CenterTitle()
hist_ratio_LO_MC.GetXaxis().SetTitleSize(0.049)
hist_ratio_LO_MC.GetYaxis().SetTitleSize(0.049)
hist_ratio_LO_MC.GetXaxis().SetLabelSize(0.05)
hist_ratio_LO_MC.GetYaxis().SetLabelSize(0.05)
hist_ratio_LO_MC.GetXaxis().SetRangeUser(30,1000)
hist_ratio_LO_MC.GetYaxis().SetRangeUser(0,2.6)
legend2.AddEntry(hist_ratio_LO_MC, "LO +<=4 Jets, MC Simulation", "l")
legend2.AddEntry(hist_ratio_NLO_MC, "NLO +<=2 Jets, MC Simulation", "l")
legend2.AddEntry(hist_ratio_LO_theorie, "LO , Theorie-Verteilung", "l")
legend2.AddEntry(hist_ratio_NNLO_theorie, "NNLO, Theorie-Verteilung", "l")


canvas.Divide(1,2)
canvas.cd(1)
canvas.cd(1).SetLogy()
hist_evj_eej_LO.Draw("histe")
hist_evj_eej_NLO.Draw("histesame")
hist_evj_eej_NNLO.Draw("histesame")
hist_MC_LO.Draw("histesame")
hist_MC_NLO.Draw("histesame")
legend.Draw("same")
latex.SetTextSize(0.03)
latex.DrawLatexNDC(0.1,0.9155,"CMS simulation #it{#bf{private Work}}")
latex.DrawLatexNDC(0.766,0.9155,"pp #rightarrow W(l#nu) + Jets @ 13 TeV")
#latex.DrawLatexNDC(0.766,0.9155,"pp #rightarrow Z(l^{#plus}l^{#minus}) + Jets @ 13 TeV")

canvas.cd(2)
#canvas.cd(2).SetLogy()
hist_ratio_LO_MC.Draw("histe")
hist_ratio_NLO_MC.Draw("histesame")
hist_ratio_LO_theorie.Draw("histesame")
hist_ratio_NNLO_theorie.Draw("histesame")
legend2.Draw("same")

canvas.Print(boson + "_boson_pt_MC_theorie.pdf")
canvas.Print(boson + "_boson_pt_MC_theorie.png")

canvas.Clear()
legend.Clear()
legend2.Clear()
file_evj_eej.Close()
file_MC_LO.Close()
file_MC_NLO.Close()

print("finished") 
