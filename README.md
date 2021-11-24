# CESP_MSc_thesis

This repository has been created to the scope of sharing the input files and the results of my MSc thesis. It is structured as follows: 

* **RAMPinput-villageX-airconditioned.xls** contains a summary of all users and appliances used to build the input files of RAMP_CESP_Thesis. 
Each user is reported in a sheet of the file, with the corresponding appliances. 
Each appliance is described with the parameters required by RAMP.
* **RAMPinput_references.txt** for the references used to assume powers and specific cycles of usage (e.g., for refrigerators or cold rooms).
* **RAMP_CESP_Thesis** contains the files as in https://github.com/RAMP-project/RAMP with inputs adapted to the case study. Three sub-cases have been considered:
	* Case A - This case formulates the demand of the 21 IGAs only ([1],[3],[4],[5],[6],[7])
	* Case B - As Case A with additional 80 low income households and 20 high income ones 	(appliances referred to Tier 1 and Tier 4 of [2])
	* Case C - As Case B with the additional installation of air conditioning units of three sizes depending on the user [8]
* **MicroGridsPy_CESP_Thesis** contains the files as in https://github.com/SESAM-Polimi/MicroGridsPy-SESAM/tree/MYCE/Code with the demands for the three cases, the renewable energy sources available and the parameters described in the Case Study. The standard input is referred to Case A.
*  **mintohours_norm.py** simple code to convert the average output profile of RAMP from minute to hourly resolution, as required to input in MicrogridsPy
