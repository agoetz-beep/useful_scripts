# python3 print function
from __future__ import print_function
# import ROOT package functionalities
import ROOT
#from ROOT import TH1D
# import sys package functionalities
import sys
# import needed FrameworkLite objects
from DataFormats.FWLite import Events, Handle
# import math package functionalities
from math import *
ROOT.gROOT.SetBatch(True)

# function to find out whether a is an ancestor of p
def isAncestor(a,p) :
        if a == p :
                return True
        for i in xrange(0,p.numberOfMothers()) :
                if isAncestor(a,p.mother(i)) :
                         return True
        return False

# function to find all mother particles of particle
def FindAllMothers(particle):
    mother_ids = []
    #print("particle id ",particle.pdgId())
    #print("# mothers ",particle.numberOfMothers())
    for i in range(p.numberOfMothers()):
        #print("mother id ",particle.mother(i).pdgId())
        mother_ids.append(particle.mother(i).pdgId())
        next_mothers_ids = FindAllMothers(particle.mother(i))
        for next_mother_id in next_mothers_ids:
            mother_ids.append(next_mother_id)
    return mother_ids

input_files = sys.argv[1:]
#print("test", input_files)
events = Events (input_files)

# container for pruned generator particles
handlePruned  = Handle ("std::vector<reco::GenParticle>")
# container for packed generator particles
handlePacked  = Handle ("std::vector<pat::PackedGenParticle>")
# label to retrieve pruned generator particles
labelPruned = ("prunedGenParticles")
# label to retrieve packed generator particles
labelPacked = ("packedGenParticles")

mass=ROOT.TH1D("mass_histogram", "mass_distribution;mass of particle (GeV);fequency",10,1,91)
mass_charge=ROOT.TH2D("mass_charge_histogram_pruned", "mass_charge_histogram_pruned;mass of particle (GeV);charge of particle (e)",1000,0.0001,1,5,-2.5,2.5)
mass_charge_withZ=ROOT.TH2D("mass_charge_histogram_pruned_withZ", "mass_charge_histogram_pruned;mass of particle (GeV);charge of particle (e)",1000,1,100,5,-2.5,2.5)
mass_charge_packed=ROOT.TH2D("mass_charge_packed_particles", "mass_charge_packed_particles;mass of particle (GeV);charge of particle (e)",1000,0.0001,1.4,5,-2.5,2.5)
pt_Z_boson=ROOT.TH1D("pt_Z", "transverse momentum distribution of Z boson;transverse momentum (GeV); frequency",21,0,420)

# loop over events
#cnt=0
for counter,event in enumerate(events):
    if counter > 10000:
        break
    #print(" ")
    #print("========================================= Event {} =========================================".format(counter))
    #print(" ")
    # retrieve packed generator particles and put them into the container defined above
    event.getByLabel (labelPacked, handlePacked)
    # retrieve pruned generator particles and put them into the container defined above
    event.getByLabel (labelPruned, handlePruned)
    # get the packed generator particle container (to not have to work with pointers)
    packed = handlePacked.product()
    # get the pruned generator particle container (to not have to work with pointers)
    pruned = handlePruned.product()

    # loop over pruned generator particles
    #print("---------- Most important generator particles (prundGenParticles) ----------")
    #print(" ")
    
    for i,p in enumerate(pruned) :
        mass.Fill(p.mass())
        mass_charge.Fill(p.mass(), p.charge())
        mass_charge_withZ.Fill(p.mass(), p.charge())

        if p.pdgId()== 23:
            pt_Z_boson.Fill(p.pt())
            
    
    
        #if p.mass()< 0.15 and p.mass()> 0.1:
          #  if p.pdgId() == 111:
           #     print("PdgId: ",p.pdgId(),"   ", "mass: ", p.mass(), "   ", "Pion_0")
            #
            #elif p.pdgId() == 211:
             #   print("PdgId: ",p.pdgId(),"   ", "mass: ", p.mass(), "   ", "Pion_+")
            
            #elif p.pdgId() == -211:
             #   print("PdgId: ",p.pdgId(),"   ", "mass: ", p.mass(), "   ", "Pion_-")
            #
            #else:
             #   print("PdgId: ",p.pdgId(),"   ", "mass: ", p.mass(), "   ", "anderes Teilchen")
           
       # if p.mass()>1 and p.mass()< 1.2:
           # print(p.pdgId(), p.mass(), p.charge(), p.status())
           # cnt+=1
        
        #else:
           # print("nicht der richtige Energiebereich")
            
        #mothers = FindAllMothers(p)
        #print("mothers")
        #print(mothers)
        #print("daughters")
    for pa in packed:
        mass_charge_packed.Fill(pa.mass(), pa.charge())
        mother = pa.mother(0)
        
        if p.mass()> 1.19999 and p.mass()< 1.2:
            print(p.pdgId(), p.mass(), p.charge(), p.status())
        #print("     PdgId : %s   pt : %s  eta : %s   phi : %s m : %s e: %s px: %s py: %s pz: %s status: %s"%         #(pa.pdgId(),pa.pt(),pa.eta(),pa.phi(),pa.mass(),pa.energy(),pa.px(),pa.py(),pa.pz(), pa.status()))

        
            
#print("Teilchen in diesem Massenbereich: ", cnt)

ROOT.gStyle.SetOptStat(0)
canvas=ROOT.TCanvas("canvas","canvas",1500,1000)
canvas.SetLogx(1)
mass.SetFillColor(3)
mass.Draw()
canvas.Print("mass.pdf")

canvas.Clear()
canvas.SetLogx(1)
mass_charge.Draw()
canvas.Print("mass_charge.pdf")
canvas.Clear()

canvas_2=ROOT.TCanvas("canvas_2","canvas_2",1500,1000)
pt_Z_boson.SetFillColor(4)
pt_Z_boson.Draw()
canvas_2.Print("pt_Z_boson.pdf")

canvas.Clear()
canvas.SetLogx(1)
mass_charge_packed.Draw()
canvas.Print("mass_charge_packed.pdf")
canvas.Clear()

canvas.Clear()
canvas.SetLogx(1)
mass_charge_withZ.Draw()
canvas.Print("mass_charge_withZ.pdf")
canvas.Clear()


#print("#{}   PdgId: {}      pt: {:.2f}      eta: {:.2f}      phi: {:.2f}      m: {:.2f}     e: {:.2f}       px: {:.2f}        py: {:.2f}        pz: {:.2f}         status: {}         charge: {}".format(i,p.pdgId(),p.pt(),p.eta(),p.phi(),p.mass(),p.energy(),p.px(),p.py(),p.pz(),p.status(), p.charge()))

