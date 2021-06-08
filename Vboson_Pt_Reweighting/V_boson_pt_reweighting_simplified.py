# imports
from __future__ import print_function
import ROOT
import sys
from array import array
from DataFormats.FWLite import Events, Handle
from math import *
from sample_info import sample_dict

# inputs
era = str(sys.argv[1])
boson = str(sys.argv[2])
postfix = str(sys.argv[3])
filenames = sys.argv[4:]

# product labels and handles
handlePruned = Handle("std::vector<reco::GenParticle>")
handlePacked = Handle("std::vector<pat::PackedGenParticle>")
eventinfo = Handle("GenEventInfoProduct")
lheinfo = Handle("LHEEventProduct")
handleJets = Handle("std::vector<reco::GenJet>")
labelPruned = "prunedGenParticles"
labelPacked = "packedGenParticles"
labelWeight = "generator"
labelLHE = "externalLHEProducer"
labelJets = "slimmedGenJets"


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

# nominal histogram
v_boson_pt_hist = ROOT.TH1D(boson + "_boson_pt", boson + "_boson_pt", len(binning) - 1, array("d", binning))
v_boson_pt_hist.Sumw2()
v_boson_pt_hist_to1TeV=ROOT.TH1D(boson + "_boson_pt_to1TeV", boson + "_boson_pt_to1TeV",len(neue_bin_grenzen) - 1,neue_bins)
v_boson_pt_hist_to1TeV.Sumw2()
v_boson_eta_hist = ROOT.TH1D(boson + "_boson_eta", boson + "_boson_eta",20, -10, 10)
v_boson_eta_hist.Sumw2()
v_boson_phi_hist = ROOT.TH1D(boson + "_boson_phi", boson + "_boson_phi",20, -3.14, 3.14)
v_boson_phi_hist.Sumw2()
jets_fuehrende_Ordnung_pt_hist = ROOT.TH1D(boson + "_jets_fuehrende_Ordnung_pt",boson + "_jets_fuehrende_Ordnung_pt",len(neue_bin_grenzen) - 1,neue_bins)
jets_fuehrende_Ordnung_pt_hist.Sumw2()
jets_fuehrende_Ordnung_eta_hist=ROOT.TH1D(boson + "_jets_fuehrende_Ordnung_eta",boson + "_jets_fuehrende_Ordnung_eta", 20, -10,10) 
jets_fuehrende_Ordnung_eta_hist.Sumw2()
jets_anzahl_hist=ROOT.TH1D(boson + "_jets_anzahl", boson + "_jets_anzahl", 20, -0.5, 19.5)
jets_anzahl_hist.Sumw2()
jets_HT_hist=ROOT.TH1D(boson + "_jets_HT", boson + "_jets_HT", len(neue_bin_grenzen) - 1,neue_bins)
jets_HT_hist.Sumw2()
v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist=ROOT.TH1D(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi", boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi", 20, 0, 3.14)
v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist.Sumw2()
w_boson_transverse_mass_hist = ROOT.TH1D(boson + "_boson_transverse_mass", boson + "_boson_transverse_mass", 20, 0,100)
w_boson_transverse_mass_hist.Sumw2()
v_boson_jets_fuehrende_Ordnung_pt_hist2D = ROOT.TH2D(boson + "_boson_jets_fuehrende_Ordnung_pt_2D", boson + "_boson_jets_fuehrende_Ordnung_pt_2D",len(neue_bin_grenzen) - 1,neue_bins,len(neue_bin_grenzen) - 1,neue_bins)
v_boson_jets_fuehrende_Ordnung_pt_hist2D.Sumw2()
v_boson_pt_DeltaPhi_hist2D = ROOT.TH2D(boson + "_boson_pt_DeltaPhi_2D", boson + "_boson_pt_DeltaPhi_2D", len(neue_bin_grenzen) - 1,neue_bins, 20, 0, 3.14)
v_boson_pt_DeltaPhi_hist2D.Sumw2()
jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D = ROOT.TH2D(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D", boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D", len(neue_bin_grenzen) - 1,neue_bins, 20, 0, 3.14)
jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D.Sumw2()
jets_anzahl_HT_hist2D = ROOT.TH2D(boson + "_jets_anzahl_HT_2D", boson + "_jets_anzahl_HT_2D", 20, -0.5, 19.5, len(neue_bin_grenzen) - 1,neue_bins)
jets_anzahl_HT_hist2D.Sumw2()
w_boson_transverse_mass_pt_hist2D = ROOT.TH2D(boson + "_boson_transverse_mass_pt_2D", boson + "_boson_transverse_mass_pt_2D", 20,0,100,len(neue_bin_grenzen) - 1,neue_bins)
w_boson_transverse_mass_pt_hist2D.Sumw2()
w_boson_transverse_mass_phizwlundnu_hist2D=ROOT.TH2D(boson + "_boson_transverse_mass_phizwlundnu_2D", boson + "_boson_transverse_mass_phizwlundnu_2D", 20,0,100, 20,0,3.14)
w_boson_transverse_mass_phizwlundnu_hist2D.Sumw2()
v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D=ROOT.TH3D(boson + "_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_3D", boson +"_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_3D", len(neue_bin_grenzen) - 1,neue_bins, len(neue_bin_grenzen) - 1,neue_bins,20,0,3.14)
v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D.Sumw2()
v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D=ROOT.TH3D(boson+ "_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_3D", boson + "_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_3D", len(neue_bin_grenzen) - 1,neue_bins,len(neue_bin_grenzen) - 1,neue_bins,20,-0.5,19.5)
v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D.Sumw2()
v_boson_pt_DeltaPhi_anzahl_hist3D=ROOT.TH3D(boson + "_boson_pt_DeltaPhi_anzahl_3D", boson + "_boson_pt_DeltaPhi_anzahl_3D", len(neue_bin_grenzen) - 1,neue_bins,20,0,3.14,20,-0.5,19.5)
v_boson_pt_DeltaPhi_anzahl_hist3D.Sumw2()

v_boson_pt_hist_ana = ROOT.TH1D(boson + "_boson_pt_ana", boson + "_boson_pt_ana", len(binning) - 1, array("d", binning))
v_boson_pt_hist_ana.Sumw2()
v_boson_pt_hist_to1TeV_ana=ROOT.TH1D(boson + "_boson_pt_to1TeV_ana", boson + "_boson_pt_to1TeV_ana",len(neue_bin_grenzen) - 1,neue_bins)
v_boson_pt_hist_to1TeV_ana.Sumw2()
v_boson_eta_hist_ana = ROOT.TH1D(boson + "_boson_eta_ana", boson + "_boson_eta_ana",20, -10, 10)
v_boson_eta_hist_ana.Sumw2()
v_boson_phi_hist_ana = ROOT.TH1D(boson + "_boson_phi_ana", boson + "_boson_phi_ana",20, -3.14, 3.14)
v_boson_phi_hist_ana.Sumw2()
jets_fuehrende_Ordnung_pt_hist_ana = ROOT.TH1D(boson + "_jets_fuehrende_Ordnung_pt_ana",boson + "_jets_fuehrende_Ordnung_pt_ana", 20, 0, 1000)
jets_fuehrende_Ordnung_pt_hist_ana.Sumw2()
jets_fuehrende_Ordnung_eta_hist_ana=ROOT.TH1D(boson + "_jets_fuehrende_Ordnung_eta_ana",boson + "_jets_fuehrende_Ordnung_eta_ana", 20, -10,10) 
jets_fuehrende_Ordnung_eta_hist_ana.Sumw2()
jets_anzahl_hist_ana=ROOT.TH1D(boson + "_jets_anzahl_ana", boson + "_jets_anzahl_ana", 20, -0.5, 19.5)
jets_anzahl_hist_ana.Sumw2()
jets_HT_hist_ana=ROOT.TH1D(boson + "_jets_HT_ana", boson + "_jets_HT_ana", len(neue_bin_grenzen) - 1,neue_bins)
jets_HT_hist_ana.Sumw2()
v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist_ana=ROOT.TH1D(boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana", boson + "_boson_jets_fuehrende_Ordnung_DeltaPhi_ana", 20, 0, 3.14)
v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist_ana.Sumw2()
w_boson_transverse_mass_hist_ana = ROOT.TH1D(boson + "_boson_transverse_mass_ana", boson + "_boson_transverse_mass_ana", 20, 0,100)
w_boson_transverse_mass_hist_ana.Sumw2()
v_boson_jets_fuehrende_Ordnung_pt_hist2D_ana = ROOT.TH2D(boson + "_boson_jets_fuehrende_Ordnung_pt_2D_ana", boson + "_boson_jets_fuehrende_Ordnung_pt_2D_ana",len(neue_bin_grenzen) - 1,neue_bins,len(neue_bin_grenzen) - 1,neue_bins)
v_boson_jets_fuehrende_Ordnung_pt_hist2D_ana.Sumw2()
v_boson_pt_DeltaPhi_hist2D_ana = ROOT.TH2D(boson + "_boson_pt_DeltaPhi_2D_ana", boson + "_boson_pt_DeltaPhi_2D_ana", len(neue_bin_grenzen) - 1,neue_bins, 20, 0, 3.14)
v_boson_pt_DeltaPhi_hist2D_ana.Sumw2()
jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D_ana = ROOT.TH2D(boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_ana", boson + "_jets_fuehrende_Ordnung_pt_DeltaPhi_2D_ana", len(neue_bin_grenzen) - 1,neue_bins, 20, 0, 3.14)
jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D_ana.Sumw2()
jets_anzahl_HT_hist2D_ana = ROOT.TH2D(boson + "_jets_anzahl_HT_2D_ana", boson + "_jets_anzahl_HT_2D_ana", 20, -0.5, 19.5, len(neue_bin_grenzen) - 1,neue_bins)
jets_anzahl_HT_hist2D_ana.Sumw2()
w_boson_transverse_mass_pt_hist2D_ana = ROOT.TH2D(boson + "_boson_transverse_mass_pt_2D_ana", boson + "_boson_transverse_mass_pt_2D_ana", 20,0,100, len(neue_bin_grenzen) - 1,neue_bins)
w_boson_transverse_mass_pt_hist2D_ana.Sumw2()
w_boson_transverse_mass_phizwlundnu_hist2D_ana=ROOT.TH2D(boson + "_boson_transverse_mass_phizwlundnu_2D_ana", boson + "_boson_transverse_mass_phizwlundnu_2D_ana", 20,0,100, 20,0,3.14)
w_boson_transverse_mass_phizwlundnu_hist2D_ana.Sumw2()
v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D_ana=ROOT.TH3D(boson + "_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_3D_ana", boson + "_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_3D_ana", len(neue_bin_grenzen) - 1,neue_bins, len(neue_bin_grenzen) - 1,neue_bins,20,0,3.14)
v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D_ana.Sumw2()
v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D_ana=ROOT.TH3D(boson+ "_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_3D_ana", boson + "_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_3D_ana", len(neue_bin_grenzen) - 1,neue_bins,len(neue_bin_grenzen) - 1,neue_bins,20,-0.5,19.5)
v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D_ana.Sumw2()
v_boson_pt_DeltaPhi_anzahl_hist3D_ana=ROOT.TH3D(boson + "_boson_pt_DeltaPhi_anzahl_3D_ana", boson + "_boson_pt_DeltaPhi_anzahl_3D_ana",len(neue_bin_grenzen) - 1,neue_bins,20,0,3.14,20,-0.5,19.5)
v_boson_pt_DeltaPhi_anzahl_hist3D_ana.Sumw2()

file_ = ROOT.TFile(boson + "_boson_pt_" + era + "_" + postfix + ".root", "RECREATE")

count = 0

# loop over files
for filename in filenames:
    print (filename)
    # cross section weights
    weight_xs = 1.0
    if boson == "Zvv":
        print ("looking at Zvv events")
    elif boson == "Zll":
        print ("looking at Zll events")
    elif boson == "W":
        print ("looking at W events")
    elif boson == "G":
        print ("looking at Photon events")
    else:
        print ("only W or Z boson or Photon allowed")
        exit()
    # information to calculate cross section weight
    subdict = sample_dict.get(era, None).get(boson, None)
    for key in subdict:
        if key in filename:
            subsubdict = subdict.get(key, None)
            print ("sigma: ", subsubdict.get("sigma", None))
            print ("X: ", subsubdict.get("X", None))
            print ("N_gen: ", subsubdict.get("N_gen", None))
            weight_xs = subsubdict.get("sigma", None) / (subsubdict.get("X", None) * subsubdict.get("N_gen", None))
    weight_xs *= 1000.0
    print ("weight_xs = ", weight_xs)
    # loop over events
    events = Events(filename)
    for event in events:
        count += 1
        if count % 1000 == 0:
            print (count)
        event.getByLabel(labelPruned, handlePruned)
        event.getByLabel(labelWeight, eventinfo)
        event.getByLabel(labelLHE, lheinfo)
        event.getByLabel(labelJets, handleJets)
        # get the products (prunedGenParticles collection, GenEventInfoProduct and LHEEventProduct)
        pruned = handlePruned.product()
        weight = eventinfo.product().weight()
        lhe_weight = lheinfo.product().originalXWGTUP()
        jets = handleJets.product()
        njets = jets.size()
        #print(jets[0].pt())
        # list for decay products of W or Z boson
        decay_prods = []
        # list for photons either for photon+jets events or for radiated photons to add back to charged leptons
        photons = []
        # list for hadrons needed for photon isolation
        hadrons = []
        # list for isolated photons
        isolated_photons = []

        if boson == "Zvv":
            for p in pruned:
                if p.isPromptFinalState() and (abs(p.pdgId()) == 12 or abs(p.pdgId()) == 14 or abs(p.pdgId()) == 16):
                    decay_prods.append(p)
                    # print("found neutrino")
        elif boson == "Zll":
            for p in pruned:
                # need to save stable photons to calculate dressed leptons later
                if abs(p.pdgId()) == 22 and p.status() == 1 and p.statusFlags().isPrompt():
                    photons.append(p)
                    continue
                # check for prompt final state charged leptons
                if ((abs(p.pdgId()) == 11 or abs(p.pdgId()) == 13) and p.isPromptFinalState()) or (abs(p.pdgId()) == 15 and p.isPromptDecayed()):
                    decay_prods.append(p)
                    # print("found charged lepton")
        elif boson == "W":
            for p in pruned:
                # need to save stable photons to calculate dressed leptons later
                if abs(p.pdgId()) == 22 and p.status() == 1 and p.statusFlags().isPrompt():
                    photons.append(p)
                    continue
                # check for prompt final state charged leptons and neutrinos
                if (
                    (abs(p.pdgId()) == 11 or abs(p.pdgId()) == 12 or abs(p.pdgId()) == 13 or abs(p.pdgId()) == 14 or abs(p.pdgId()) == 16)
                    and p.isPromptFinalState()
                ) or (abs(p.pdgId()) == 15 and p.isPromptDecayed()):
                    decay_prods.append(p)
                    # print("found neutrino/charged lepton")
        elif boson == "G":
            # need packedGenParticles collection for final state hadrons
            event.getByLabel(labelPacked, handlePacked)
            packed = handlePacked.product()
            for p in pruned:
                # need to save stable photons
                if abs(p.pdgId()) == 22 and p.status() == 1 and p.statusFlags().isPrompt():
                    photons.append(p)
            for p in packed:
                # exclude final state photons and leptons from final state gen particle collection -> final state hadrons
                if p.status() == 1 and not (abs(p.pdgId()) == 22 or (abs(p.pdgId()) >= 11 and abs(p.pdgId()) <= 16)):
                    hadrons.append(p)
        else:
            print ("only W or Z boson or Photon allowed")
            exit()

        # fail-safe: check if the number of found daughters is exactly 2 as one would expect for W/Z
        if boson == "Zvv" or boson == "Zll" or boson == "W":
            # if there are more than 2 final state leptons, e.g. from additional hadron decays, take the leading two leptons (this works in 99.999% of all cases)
            if len(decay_prods) > 2:
                decay_prods.sort(key=lambda dp: dp.pt(), reverse=True)
            # if there are less than 2 final state leptons, do not consider this event (happens in O(0.01%) of all cases so basically never)
            elif len(decay_prods) < 2:
                continue
        # fail-safe: check if there is at least one final state photon for gamma+jets events
        elif boson == "G":
            if len(photons) < 1:
                continue
        else:
            print ("only W or Z boson or Photon allowed")
            exit()

        if boson == "Zvv":
            # fail-safe: check if the daughters of the Z boson are particle and anti-particle as well as same lepton flavor
            if decay_prods[0].pdgId() + decay_prods[1].pdgId() != 0:
                continue

        elif boson == "Zll":
            # fail-safe: check if the daughters of the Z boson are particle and anti-particle as well as same lepton flavor
            if decay_prods[0].pdgId() + decay_prods[1].pdgId() != 0:
                continue
            # add radiated photons back to leptons
            for decay_prod in decay_prods:
                if abs(decay_prod.pdgId()) == 11 or abs(decay_prod.pdgId()) == 13 or abs(decay_prod.pdgId()) == 15:
                    for photon in photons:
                        if sqrt(ROOT.Math.VectorUtil.DeltaR2(decay_prod.p4(), photon.p4())) < 0.1:
                            decay_prod.setP4(decay_prod.p4() + photon.p4())

        elif boson == "W":
            # fail-safe: check if the daughters of the W boson are particle and anti-particle as well as same lepton flavor adapted for W decays
            if decay_prods[0].pdgId() * decay_prods[1].pdgId() >= 0 or abs(abs(decay_prods[0].pdgId()) - abs(decay_prods[1].pdgId())) != 1:
                continue
            # add radiated photons back to lepton
            for decay_prod in decay_prods:
                if abs(decay_prod.pdgId()) == 11 or abs(decay_prod.pdgId()) == 13 or abs(decay_prod.pdgId()) == 15:
                    for photon in photons:
                        if sqrt(ROOT.Math.VectorUtil.DeltaR2(decay_prod.p4(), photon.p4())) < 0.1:
                            decay_prod.setP4(decay_prod.p4() + photon.p4())
        # photons are more complicated on theory level
        # one has to find isolated photons using the isolation prescription in https://arxiv.org/pdf/1705.04664.pdf
        elif boson == "G":
            epsilon_0_dyn = 0.1
            n_dyn = 1
            iterations = 5.0
            for photon in photons:
                isolated = True
                R_dyn = 91.1876 / (photon.pt() * sqrt(epsilon_0_dyn))
                R_0_dyn = min(1.0, R_dyn)
                for R in [R_0_dyn / iterations * i for i in range(1, int(iterations) + 1)]:
                    isolation = 0.0
                    for hadron in hadrons:
                        if sqrt(ROOT.Math.VectorUtil.DeltaR2(hadron.p4(), photon.p4())) <= R:
                            isolation += hadron.pt()
                    if isolation > (epsilon_0_dyn * photon.pt() * pow((1 - cos(R)) / (1 - cos(R_0_dyn)), n_dyn)):
                        isolated = False
                        break
                if isolated:
                    isolated_photons.append(photon)
            # if there is more than 1 isolated photon, take the leading one
            if len(isolated_photons) > 1:
                isolated_photons.sort(key=lambda dp: dp.pt(), reverse=True)
            elif len(isolated_photons) < 1:
                # print ("no isolated photon found")
                continue

        # reconstruct vector boson from the two decay products
        if boson == "Zvv" or boson == "Zll" or boson == "W":
            v_boson = decay_prods[0].p4() + decay_prods[1].p4()
        elif boson == "G":
            v_boson = isolated_photons[0].p4()
        else:
            print ("only W or Z boson or Photon allowed")
            exit()
        v_boson_pt = v_boson.pt()
        v_boson_eta = v_boson.eta()
        v_boson_phi = v_boson.phi()
        v_boson_mass = v_boson.mass()
        
        
        
        
        
        # print (v_boson_pt)
        # fill the vector boson pt
        
        v_boson_pt_hist.Fill(v_boson_pt, weight * weight_xs / 1000.0)
        v_boson_pt_hist_to1TeV.Fill(v_boson_pt, weight * weight_xs / 1000.0)
        v_boson_eta_hist.Fill(v_boson_eta, weight * weight_xs / 1000.0)
        v_boson_phi_hist.Fill(v_boson_phi, weight * weight_xs / 1000.0)
        if boson == "W":
            DeltaPhi_lnu=abs(ROOT.TVector2.Phi_mpi_pi(decay_prods[0].phi()-decay_prods[1].phi()))
            w_boson_mt = pow(2*decay_prods[0].pt()*decay_prods[1].pt()*(1-cos(DeltaPhi_lnu)), 0.5)
            w_boson_transverse_mass_hist.Fill(w_boson_mt, weight * weight_xs / 1000.0)
            w_boson_transverse_mass_pt_hist2D.Fill(w_boson_mt, v_boson_pt, weight * weight_xs / 1000.0)
            w_boson_transverse_mass_phizwlundnu_hist2D.Fill(w_boson_mt, DeltaPhi_lnu, weight * weight_xs / 1000.0)
            
        
        anzahl = 0
        sum_pt = 0
        for jet in jets:
            if abs(jet.eta())<= 2.4:
                if jet.pt() >= 30:
                    anzahl += 1
                    sum_pt += jet.pt()
        jets_anzahl_hist.Fill(anzahl, weight * weight_xs / 1000.0)
        jets_HT_hist.Fill(sum_pt, weight * weight_xs / 1000.0)
        jets_anzahl_HT_hist2D.Fill(anzahl, sum_pt, weight * weight_xs / 1000.0)
        
        
        if njets > 0:
            jets_fuehrende_Ordnung_pt = jets[0].pt()
            jets_fuehrende_Ordnung_eta = jets[0].eta()
            jets_fuehrende_Ordnung_phi = jets[0].phi()
            DeltaPhi = v_boson_phi - jets_fuehrende_Ordnung_phi
            DeltaPhi_richtigerBereich = ROOT.TVector2.Phi_mpi_pi(DeltaPhi)
            DeltaPhi_betrag= abs(DeltaPhi_richtigerBereich)
            jets_fuehrende_Ordnung_pt_hist.Fill(jets_fuehrende_Ordnung_pt, weight * weight_xs / 1000.0)
            jets_fuehrende_Ordnung_eta_hist.Fill(jets_fuehrende_Ordnung_eta, weight * weight_xs / 1000.0)
            v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist.Fill(DeltaPhi_betrag, weight * weight_xs / 1000.0)
            v_boson_jets_fuehrende_Ordnung_pt_hist2D.Fill(v_boson_pt, jets_fuehrende_Ordnung_pt, weight * weight_xs / 1000.0)
            v_boson_pt_DeltaPhi_hist2D.Fill(v_boson_pt, DeltaPhi_betrag, weight * weight_xs / 1000.0)
            jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D.Fill(jets_fuehrende_Ordnung_pt, DeltaPhi_betrag, weight * weight_xs / 1000.0)
            v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D.Fill(v_boson_pt, jets_fuehrende_Ordnung_pt, DeltaPhi_betrag,weight * weight_xs / 1000.0) 
            v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D.Fill(v_boson_pt, jets_fuehrende_Ordnung_pt, anzahl, weight * weight_xs / 1000.0)
            v_boson_pt_DeltaPhi_anzahl_hist3D.Fill(v_boson_pt, DeltaPhi_betrag, anzahl,  weight * weight_xs / 1000.0)
            
            if jets_fuehrende_Ordnung_pt >= 100:
                if abs(jets_fuehrende_Ordnung_eta) <= 2.4:
                    if v_boson_pt >= 250:
                        if DeltaPhi_betrag >= 1.57:
                            v_boson_pt_hist_ana.Fill(v_boson_pt, weight * weight_xs / 1000.0)
                            v_boson_pt_hist_to1TeV_ana.Fill(v_boson_pt, weight * weight_xs / 1000.0)
                            v_boson_eta_hist_ana.Fill(v_boson_eta, weight * weight_xs / 1000.0)
                            v_boson_phi_hist_ana.Fill(v_boson_phi, weight * weight_xs / 1000.0)
                            if boson == "W":
                                DeltaPhi_lnu=abs(ROOT.TVector2.Phi_mpi_pi(decay_prods[0].phi()-decay_prods[1].phi()))
                                w_boson_mt = pow(2*decay_prods[0].pt()*decay_prods[1].pt()*(1-cos(DeltaPhi_lnu)), 0.5)
                                w_boson_transverse_mass_hist_ana.Fill(w_boson_mt, weight * weight_xs / 1000.0)
                                w_boson_transverse_mass_pt_hist2D_ana.Fill(w_boson_mt, v_boson_pt, weight * weight_xs / 1000.0)
                                w_boson_transverse_mass_phizwlundnu_hist2D_ana.Fill(w_boson_mt, DeltaPhi_lnu, weight * weight_xs / 1000.0)
                                    
                            anzahl_ana = 0
                            sum_pt_ana = 0
                            for jet in jets:
                                if abs(jet.eta())<= 2.4:
                                    if jet.pt() >= 30:
                                        anzahl_ana += 1
                                        sum_pt_ana += jet.pt()
                            jets_anzahl_hist_ana.Fill(anzahl_ana, weight * weight_xs / 1000.0)
                            jets_HT_hist_ana.Fill(sum_pt_ana, weight * weight_xs / 1000.0)
                            jets_anzahl_HT_hist2D_ana.Fill(anzahl_ana, sum_pt_ana, weight * weight_xs / 1000.0)
                                
                                    
                            jets_fuehrende_Ordnung_pt_hist_ana.Fill(jets_fuehrende_Ordnung_pt, weight * weight_xs / 1000.0)
                            jets_fuehrende_Ordnung_eta_hist_ana.Fill(jets_fuehrende_Ordnung_eta, weight * weight_xs / 1000.0)
                            v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist_ana.Fill(DeltaPhi_betrag, weight * weight_xs / 1000.0)
                            v_boson_jets_fuehrende_Ordnung_pt_hist2D_ana.Fill(v_boson_pt, jets_fuehrende_Ordnung_pt, weight * weight_xs / 1000.0)
                            v_boson_pt_DeltaPhi_hist2D_ana.Fill(v_boson_pt, DeltaPhi_betrag, weight * weight_xs / 1000.0)
                            jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D_ana.Fill(jets_fuehrende_Ordnung_pt, DeltaPhi_betrag, weight * weight_xs / 1000.0)
                            v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D_ana.Fill(v_boson_pt, jets_fuehrende_Ordnung_pt, DeltaPhi_betrag,weight * weight_xs / 1000.0) 
                            v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D_ana.Fill(v_boson_pt, jets_fuehrende_Ordnung_pt, anzahl_ana, weight * weight_xs / 1000.0)
                            v_boson_pt_DeltaPhi_anzahl_hist3D_ana.Fill(v_boson_pt, DeltaPhi_betrag, anzahl_ana,  weight * weight_xs / 1000.0)
                                
        
        
        
        
        
                               
                        
                
        
        

# write all to a file
file_.WriteTObject(v_boson_eta_hist)
file_.WriteTObject(v_boson_phi_hist)
file_.WriteTObject(v_boson_pt_hist)
file_.WriteTObject(v_boson_pt_hist_to1TeV)
file_.WriteTObject(jets_fuehrende_Ordnung_pt_hist)
file_.WriteTObject(jets_fuehrende_Ordnung_eta_hist)
file_.WriteTObject(jets_anzahl_hist)
file_.WriteTObject(jets_HT_hist)
file_.WriteTObject(v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist)
file_.WriteTObject(w_boson_transverse_mass_hist)
file_.WriteTObject(v_boson_jets_fuehrende_Ordnung_pt_hist2D)
file_.WriteTObject(v_boson_pt_DeltaPhi_hist2D)
file_.WriteTObject(jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D)
file_.WriteTObject(jets_anzahl_HT_hist2D)
file_.WriteTObject(w_boson_transverse_mass_pt_hist2D)
file_.WriteTObject(w_boson_transverse_mass_phizwlundnu_hist2D)
file_.WriteTObject(v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D)
file_.WriteTObject(v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D)
file_.WriteTObject(v_boson_pt_DeltaPhi_anzahl_hist3D)

file_.WriteTObject(v_boson_eta_hist_ana)
file_.WriteTObject(v_boson_phi_hist_ana)
file_.WriteTObject(v_boson_pt_hist_ana)
file_.WriteTObject(v_boson_pt_hist_to1TeV_ana)
file_.WriteTObject(jets_fuehrende_Ordnung_pt_hist_ana)
file_.WriteTObject(jets_fuehrende_Ordnung_eta_hist_ana)
file_.WriteTObject(jets_anzahl_hist_ana)
file_.WriteTObject(jets_HT_hist_ana)
file_.WriteTObject(v_boson_jets_fuehrende_Ordnung_DeltaPhi_hist_ana)
file_.WriteTObject(w_boson_transverse_mass_hist_ana)
file_.WriteTObject(v_boson_jets_fuehrende_Ordnung_pt_hist2D_ana)
file_.WriteTObject(v_boson_pt_DeltaPhi_hist2D_ana)
file_.WriteTObject(jets_fuehrende_Ordnung_pt_DeltaPhi_hist2D_ana)
file_.WriteTObject(jets_anzahl_HT_hist2D_ana)
file_.WriteTObject(w_boson_transverse_mass_pt_hist2D_ana)
file_.WriteTObject(w_boson_transverse_mass_phizwlundnu_hist2D_ana)
file_.WriteTObject(v_boson_pt_jets_fuehrende_Ordnung_pt_DeltaPhi_hist3D_ana)
file_.WriteTObject(v_boson_pt_jets_fuehrende_Ordnung_pt_anzahl_hist3D_ana)
file_.WriteTObject(v_boson_pt_DeltaPhi_anzahl_hist3D_ana)



file_.Close()
print ("finished")
