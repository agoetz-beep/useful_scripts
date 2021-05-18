import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys

boson=sys.argv[1]
file_LO=ROOT.TFile.Open(sys.argv[2])
file_NLO=ROOT.TFile.Open(sys.argv[3])
 

canvas=ROOT.TCanvas("canvas", "canvas", 2000, 1500)

legend=ROOT.TLegend(0.15,0.15)

######################################################

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

##################################################

hist3=hist2.Clone()
hist3.Divide(hist)
hist.GetXaxis().SetTitle("transversaler Impuls in GeV")
hist.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")
hist.GetXaxis().SetRangeUser(30.0,1000.0)
#hist.GetYaxis().SetRangeUser(0.00000001,100000000)
hist.GetXaxis().CenterTitle()
hist.GetYaxis().CenterTitle()
hist.SetLineColor(1)
hist2.SetLineColor(2)
hist3.GetXaxis().SetTitle("transversaler Impuls in GeV")
hist3.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist3.GetXaxis().SetRangeUser(30.0,1000.0)
hist3.GetXaxis().CenterTitle()
hist3.GetYaxis().CenterTitle()

hist6=hist5.Clone()
hist6.Divide(hist4)
hist4.GetXaxis().SetTitle("transversaler Impuls in GeV")
hist4.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")    
hist4.GetXaxis().CenterTitle()
hist4.GetYaxis().CenterTitle()
#hist.GetYaxis().SetRangeUser(0.0000001,100)
hist4.SetLineColor(1)
hist5.SetLineColor(2)
hist6.GetXaxis().SetTitle("transversaler Impuls in GeV")
hist6.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist6.GetXaxis().CenterTitle()
hist6.GetYaxis().CenterTitle() 

hist9=hist8.Clone()
hist9.Divide(hist7)
hist7.GetXaxis().SetTitle("Pseudorapiditaet")
hist7.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")    
hist7.GetXaxis().CenterTitle()
hist7.GetYaxis().CenterTitle()
hist7.SetLineColor(1)
hist8.SetLineColor(2)
#hist7.GetYaxis().SetRangeUser(0.0,10000.0)
#hist7.GetXaxis().SetRangeUser(-20,20)
hist9.GetXaxis().SetTitle("Pseudorapiditaet")
hist9.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist9.GetXaxis().CenterTitle()
hist9.GetYaxis().CenterTitle()

hist12=hist11.Clone()
hist12.Divide(hist10)
hist10.GetXaxis().SetTitle("Azimutalwinkel")
hist10.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")    
hist10.GetXaxis().CenterTitle()
hist10.GetYaxis().CenterTitle()
hist10.SetLineColor(1)
hist11.SetLineColor(2)
#hist10.GetYaxis().SetRangeUser(0.0,10000.0)
hist12.GetXaxis().SetTitle("Azimutalwinkel")
hist12.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist12.GetXaxis().CenterTitle()
hist12.GetYaxis().CenterTitle()

hist15=hist14.Clone()
hist15.Divide(hist13)
hist13.GetXaxis().SetTitle("transversaler Impuls in GeV")
hist13.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")
hist13.GetXaxis().CenterTitle()
hist13.GetYaxis().CenterTitle()
hist13.SetLineColor(1)
hist14.SetLineColor(2)
hist15.GetXaxis().SetTitle("transversaler Impuls in GeV")
hist15.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist15.GetXaxis().CenterTitle()
hist15.GetYaxis().CenterTitle()

hist18=hist17.Clone()
hist18.Divide(hist16)
hist16.GetXaxis().SetTitle("Pseudorapiditaet")
hist16.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")    
hist16.GetXaxis().CenterTitle()
hist16.GetYaxis().CenterTitle()
hist16.SetLineColor(1)
hist17.SetLineColor(2)
hist18.GetXaxis().SetTitle("Pseudorapiditaet")
hist18.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist18.GetXaxis().CenterTitle()
hist18.GetYaxis().CenterTitle()

hist21=hist20.Clone()
hist21.Divide(hist19)
hist19.GetXaxis().SetTitle("Anzahl der Jets")
hist19.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")    
hist19.GetXaxis().CenterTitle()
hist19.GetYaxis().CenterTitle()
hist19.SetLineColor(1)
hist20.SetLineColor(2)
hist21.GetXaxis().SetTitle("Anzahl der Jets")
hist21.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist21.GetXaxis().CenterTitle()
hist21.GetYaxis().CenterTitle()

hist24=hist23.Clone()
hist24.Divide(hist22)
hist22.GetXaxis().SetTitle("Summe aller Transversalimpulse in GeV aller Jets")
hist22.GetYaxis().SetTitle("Wirkungsquerschnitt in pb pro Bin")
hist22.GetXaxis().CenterTitle()
hist22.GetYaxis().CenterTitle()
hist22.SetLineColor(1)
hist23.SetLineColor(2)
hist24.GetXaxis().SetTitle("Summe aller Transversalimpulse in GeV aller Jets")
hist24.GetYaxis().SetTitle("Wirkungsquerschnittsverhaeltnis NLO/LO")
hist24.GetXaxis().CenterTitle()
hist24.GetYaxis().CenterTitle()

########################################

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
canvas.Print(boson + "_boson_pt.pdf")

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
canvas.Print(boson + "_boson_pt_to1TeV.pdf")

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
canvas.Print(boson + "_boson_eta.pdf")

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
canvas.Print(boson + "_boson_phi.pdf")

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
canvas.Print(boson + "_jets_fuehrende_Ordnung_pt.pdf")

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
canvas.Print(boson + "_jets_fuehrende_Ordnung_eta.pdf")

canvas.Clear()
legend.Clear()

############################################

legend.AddEntry(hist19, "LO", "l")
legend.AddEntry(hist20, "NLO", "l")

canvas.Divide(1,2)
canvas.cd(1)

hist19.Draw("histe")
hist20.Draw("histesame")

legend.Draw("same")

canvas.cd(2)
hist21.Draw("histe")

canvas.Print(boson + "_jets_anzahl.png")
canvas.Print(boson + "_jets_anzahl.pdf")

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
canvas.Print(boson + "_jets_HT.pdf")

canvas.Clear()
legend.Clear()

###########################################
print("finished")
