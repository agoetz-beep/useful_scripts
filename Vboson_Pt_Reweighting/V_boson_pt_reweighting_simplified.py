# imports
from __future__ import print_function
import ROOT
import sys
from array import array
from DataFormats.FWLite import Events, Handle
from math import pow,sqrt,cos
from sample_info import sample_dict
from Definitions import var_info_dict
from VariableCalculator import VariableCalculator

def GetCorrFactor(hist,input_tuple):
    if len(input_tuple)==1:
        corr_factor=hist.GetBinContent(hist.FindBin(input_tuple[0]))
    elif len(input_tuple)==2:
        corr_factor=hist.GetBinContent(hist.FindBin(input_tuple[0],input_tuple[1]))
    else:
        corr_factor=None
    return corr_factor

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






file_ = ROOT.TFile(boson + "_boson_pt_" + era + "_" + postfix + ".root", "RECREATE")

corrfactor_file=ROOT.TFile.Open(boson + "_factors.root")

# dictionary containing information regarding corrections factors
corr_factor_dict = { 
#                            "" : {},
                            "Vpt_corr_factor_incl" : {"dim" : 1, "hist" : corrfactor_file.Get(boson +"_incl_boson_pt_to1TeV_corr_factor"), "function" : "boson_pt"},
                            "Vpt_theory_binning_corr_factor_incl" : {"dim" : 1, "hist" : corrfactor_file.Get(boson + "_incl_boson_pt_corr_factor"), "function" : "boson_pt"},
                            "Vpt_corr_factor_ana" : {"dim" : 1, "hist" : corrfactor_file.Get(boson +"_ana_boson_pt_to1TeV_corr_factor"), "function" : "boson_pt"},
                            "Vpt_theory_binning_corr_factor_ana" : {"dim" : 1, "hist" : corrfactor_file.Get(boson + "_ana_boson_pt_corr_factor"), "function" : "boson_pt"},
                            "Vpt_Veta_corr_factor_incl" : {"dim" : 2, "hist" : corrfactor_file.Get(boson+"_incl_boson_pt_eta_corr_factor"), "function1" : "boson_pt" , "function2" : "boson_eta"},
                            "Vpt_DeltaPhi_corr_factor_incl" : {"dim" : 2, "hist" : corrfactor_file.Get(boson+"_incl_boson_pt_DeltaPhi_corr_factor") , "function1" : "boson_pt" , "function2" : "deltaphi_boson_jet0"},
                            "Vpt_HT_corr_factor_incl" : {"dim" : 2, "hist" : corrfactor_file.Get(boson+"_incl_boson_pt_HT_corr_factor") , "function1" : "boson_pt" , "function2" : "ht_jets"},
                            "Vpt_anzahl_corr_factor_incl" : {"dim" : 2, "hist" : corrfactor_file.Get(boson+"_incl_boson_pt_anzahl_corr_factor") , "function1" : "boson_pt" , "function2" : "njets"}
                            
                        }

# dictionary containing reference between selection label and variablecalculator function checking selection
sel_func_dict = {"incl" : "incl_sel" , "ana" : "ana_sel"}

# dictionary to store resulting histograms
histo_dict = {}

# create histograms for all combinations of desired histograms and correction factors
for key in var_info_dict:
    for key_ in corr_factor_dict:
        for key__ in sel_func_dict:
            histo_dict[key__+"_"+key+"_"+key_]=var_info_dict[key]["hist"].Clone()
            histo_dict[key__+"_"+key+"_"+key_].SetName(boson+"_"+key__+"_"+key+"_"+key_)
            histo_dict[key__+"_"+key+"_"+key_].SetTitle(boson+"_"+key__+"_"+key+"_"+key_)
            histo_dict[key__+"_"+key+"_"+key_].Sumw2()



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
        
        # variablecalculator class instance to calculate necessary variables in an automated way
        vc = VariableCalculator(v_boson,jets,decay_prods)
        
        # loop over selections
        for key__ in sel_func_dict:
            if not getattr(vc,sel_func_dict[key__])():
                continue
            # loop over keys describing desired correction factors
            for key_ in corr_factor_dict:
                # regular weight
                final_weight = weight * weight_xs / 1000.0
                # apply correction factors depending on its dimension
                # empty string -> no correction factor
                if key_=="":
                    final_weight*=1
                elif corr_factor_dict[key_]["dim"]==1:
                    final_weight*=corr_factor_dict[key_]["hist"].GetBinContent(corr_factor_dict[key_]["hist"].FindBin(getattr(vc,corr_factor_dict[key_]["function"])()))
                elif corr_factor_dict[key_]["dim"]==2:
                    final_weight*=corr_factor_dict[key_]["hist"].GetBinContent(corr_factor_dict[key_]["hist"].FindBin(getattr(vc,corr_factor_dict[key_]["function1"])(),getattr(vc,corr_factor_dict[key_]["function2"])()))
                else:
                    print("correction factor calculation problem")
                    exit()
                # loop over keys describing desired variables
                for key in var_info_dict:
                    # fill histograms depending on dimension of histograms
                    if var_info_dict[key]["dim"]==1:
                        histo_dict[key__+"_"+key+"_"+key_].Fill(getattr(vc,var_info_dict[key]["function"])(), final_weight)
                    elif var_info_dict[key]["dim"]==2:
                        histo_dict[key__+"_"+key+"_"+key_].Fill(getattr(vc,var_info_dict[key]["function1"])(), getattr(vc,var_info_dict[key]["function2"])(), final_weight)
                    else:
                        print("only 1 and 2 dimensions supported at the moment")
                        exit()

# write all histograms to a file
for key in histo_dict:
    file_.WriteTObject(histo_dict[key])


file_.Close()
print ("finished")
