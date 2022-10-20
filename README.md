# Pharmodel
Software engineering miniproject \
Group 1: Arun Raja, Henriette Capel, Nathan Schofield, Jiayuan Zhu

## :pill: Pharmokinetic Modelling
This pharmokinetic model describes the concentration of a drug in a patient. This model includes the delivery, diffusion, and clearance of the drug in the patient. The patient will be modelled as a central compartment into which the drug is administered and from which it is excreted. One or two peripheral compartements can be added by the user. The drug can be distributed to these peripheral compartments and from these compartments back to the central compartment. The dynamics of the drug are modelled by zeroth-order and first-order rate equations. 

![](Pharmodel.png)

## :rocket: Installing Pharmodel

## :running: Using Pharmodel
### Input Parameters
The model takes a csv file and the parameters as input parameters: 
- The csv file describes the dosing protocol including the start of a certain dose (tstart, in [h]), the end of the dosing period (tend, in [h]), the drug mass (dose, in [ng]), and a binary value indicating if the dose is given instantaneous at a certain time point or constant over a certain time period. Three examples of dosing protocols are provided ("test_dosis_continuous.csv", "test_dosis_instantaneous.csv", and "test_dosis_combined.csv"). 
- the folowing parameters can be specified by the user:
 absorb: binary value indicating intravenous bolus dosing (0) or subcutaneous dosing (1);\
 comp: integer indicating the number of compartment. The three possibilities are only the central compartment (0), an additional peripheral compartment (1), or an second additional peripheral compartment (2);\
 

## :page_facing_up: Licence 
Pharmodel is fully open source. For more information about the license, see LICENSE.

