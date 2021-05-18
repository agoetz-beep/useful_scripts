import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys 
canvas=ROOT.TCanvas("canvas", "canvas", 2000, 1500)
boson=sys.argv[1]
file_hadd=ROOT.TFile.Open(sys.argv[2])
hist1=file_hadd.Get(boson + "_jets_HT")
entries=hist1.GetEntries()
print("Entries: " ,entries)
hist1.Draw("histe")
canvas.Print(boson + "_jets_HT.png")

print("finished")
