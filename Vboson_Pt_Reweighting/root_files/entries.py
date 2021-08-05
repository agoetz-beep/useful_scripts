import ROOT
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
import sys 
from array import array
canvas=ROOT.TCanvas("canvas", "canvas", 2000, 1500)
boson=sys.argv[1]
file_hadd=ROOT.TFile.Open(sys.argv[2])
hist1=file_hadd.Get(boson+ "_incl_boson_pt_")
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
#neue_bins=array("d", neue_bin_grenzen)
#neues_histogramm=hist1.Rebin(len(neue_bin_grenzen)-1,boson+ "_boson_pt_neue_grenzen",neue_bins)
entries=hist1.GetEntries()
print("Entries: " ,entries)
#neues_histogramm.GetXaxis().SetRangeUser(30,1000)
#neues_histogramm.Draw("histe")
#canvas.SetLogy(1)
#canvas.Print(boson + "_boson_pt_neue_grenzen.png")


print("finished")
