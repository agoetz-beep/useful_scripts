from ROOT import TVector2
from math import cos

class VariableCalculator:
    def __init__(self, boson_p4, jets_vector, decay_prods):
        self.boson_p4 = boson_p4
        self.jets_vector = jets_vector
        self.decay_prods = decay_prods
        self.charged_lepton = None
        for decay_prod in self.decay_prods:
            if decay_prod.charge()!=0.:
                self.charged_lepton = decay_prod
                break
    
    def boson_pt(self):
        return self.boson_p4.pt()
    
    def boson_eta(self):
        return self.boson_p4.eta()
    
    def jet0_pt(self):
        if self.jets_vector.size()>0:
            return self.jets_vector[0].pt()
        else:
            return -999.

    def jet0_eta(self):
        if self.jets_vector.size()>0:
            return self.jets_vector[0].eta()
        else:
            return -999.

    def jet1_pt(self):
        if self.jets_vector.size()>1:
            return self.jets_vector[1].pt()
        else:
            return -999.

    def jet1_eta(self):
        if self.jets_vector.size()>1:
            return self.jets_vector[1].eta()
        else:
            return -999.

    def jet2_pt(self):
        if self.jets_vector.size()>2:
            return self.jets_vector[2].pt()
        else:
            return -999.

    def jet2_eta(self):
        if self.jets_vector.size()>2:
            return self.jets_vector[2].eta()
        else:
            return -999.

    def jet3_pt(self):
        if self.jets_vector.size()>3:
            return self.jets_vector[3].pt()
        else:
            return -999.

    def jet3_eta(self):
        if self.jets_vector.size()>3:
            return self.jets_vector[3].eta()
        else:
            return -999.

    def njets(self):
        n = 0
        for jet in self.jets_vector:
            if jet.pt()>=30. and jet.eta()<=2.4:
                n += 1
        return n

    def ht_jets(self):
        ht = 0.
        for jet in self.jets_vector:
            if jet.pt()>=30. and jet.eta()<=2.4:
                ht += jet.pt()
        return ht

    def deltaphi_boson_jet0(self):
        if self.jets_vector.size()>0:
            return abs(TVector2.Phi_mpi_pi(self.boson_p4.phi() - self.jets_vector[0].phi()))
        else:
            return -999.

    def deltaphi_boson_jet1(self):
        if self.jets_vector.size()>1:
            return abs(TVector2.Phi_mpi_pi(self.boson_p4.phi() - self.jets_vector[1].phi()))
        else:
            return -999.

    def deltaphi_boson_jet2(self):
        if self.jets_vector.size()>2:
            return abs(TVector2.Phi_mpi_pi(self.boson_p4.phi() - self.jets_vector[2].phi()))
        else:
            return -999.

    def deltaphi_boson_jet3(self):
        if self.jets_vector.size()>3:
            return abs(TVector2.Phi_mpi_pi(self.boson_p4.phi() - self.jets_vector[3].phi()))
        else:
            return -999.    

    def charged_lepton_pt(self):
        if self.charged_lepton:
            return self.charged_lepton.pt()
        else:
            return -999.
    
    def charged_lepton_eta(self):
        if self.charged_lepton:
            return self.charged_lepton.eta()
        else:
            return -999.

    def deltaphi_decay_prods(self):
        return abs(TVector2.Phi_mpi_pi(self.decay_prods[0].phi()-self.decay_prods[1].phi()))

    def transverse_mass(self):
        return pow(2*self.decay_prods[0].pt()*self.decay_prods[1].pt()*(1-cos(self.deltaphi_decay_prods())), 0.5)

    def boson_mass(self):
        return self.boson_p4.mass()
    
    def incl_sel(self):
        return True
    
    def ana_sel(self):
        sel = self.boson_pt()>=250. and self.jet0_pt()>=100. and abs(self.jet0_eta())<=2.4 and self.deltaphi_boson_jet0()>=1.57
        return sel
