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

mass=ROOT.TH1D("mass_histogram", "mass_distribution;mass of particle;fequency",100,0,150)
mass_charge=ROOT.TH2D("mass_charge_graph", "mass_charge_chart;mass of particle;charge of particle",100,0,150,2,-1,1)

pt_Z_boson=ROOT.TH1D("pt_Z", "transverse momentum distribution of Z boson;transverse momentum; frequency",500,0,420)

# loop over events
for counter,event in enumerate(events):
    if counter > 1000:
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
        #print("#{}   PdgId: {}      pt: {:.2f}      eta: {:.2f}      phi: {:.2f}      m: {:.2f}     e: {:.2f}       px: {:.2f}        py: {:.2f}        pz: {:.2f}         status: {}         charge: {}".format(i,p.pdgId(),p.pt(),p.eta(),p.phi(),p.mass(),p.energy(),p.px(),p.py(),p.pz(),p.status(), p.charge()))
	mass.Fill(p.mass())
	mass_charge.Fill(p.mass(), p.charge())

	if p.pdgId()== 23:
		pt_Z_boson.Fill(p.pt())

	
        #mothers = FindAllMothers(p)
        #print("mothers")
        #print(mothers)
        #print("daughters")
        #for pa in packed:
            #mother = pa.mother(0)
            #if mother and isAncestor(p,mother) :
                #print("     PdgId : %s   pt : %s  eta : %s   phi : %s m : %s e: %s px: %s py: %s pz: %s" %(pa.pdgId(),pa.pt(),pa.eta(),pa.phi(),pa.mass(),pa.energy(),pa.px(),pa.py(),pa.pz()))

#mit Klasse TH1D-----------------------------------------------------------------------------------------
#TH1D *mass = new TH1D("mass_histogram", "mass distribution", 100, 0, 150);
#TH1D* mass=new TH1D("mass_histogram", "mass_distribution;mass of particle;fequency",100,0,150);
#mass->Fill(p.mass());

mass.SetFillColor(3)
mass.Draw()
#mass_charge.SetLineColor(3)
mass_charge.Draw()
pt_Z_boson.SetFillColor(4)
pt_Z_boson.Draw()

raw_input("test")



