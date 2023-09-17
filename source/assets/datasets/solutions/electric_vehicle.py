

import csv, os, sys

import matplotlib as mpl

mpl.use("tkagg")

import matplotlib.pyplot as plt

def joint_freq_xy(sample, x, y):
    freq = sum(1 for obs in sample if obs[0] == x and obs[1] == y)
    return freq

def marginal_freq_x(sample, x):
    freq = sum(1 for obs in sample if obs == x)
    return freq

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

# read in data
with open(f'{data_directory}/electric_vehicle_population_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]

n = len(columns)

make = [ row[6] for row in columns ]
veh_type = [ row[8] for row in columns ]
make_and_type = [ (row[6], row[8]) for row in columns ]
eligibility = [row[9] for row in columns ]
veh_and_elig = [ (row[8], row[9]) for row in columns ]

freq_of_tesla = marginal_freq_x(make, "TESLA")
freq_of_chev = marginal_freq_x(make, "CHEVROLET")
freq_of_niss = marginal_freq_x(make, "NISSAN")
freq_of_toy = marginal_freq_x(make, "TOYOTA")
freq_of_vw = marginal_freq_x(make, "VOLKSWAGEN")

joint_freq_of_tesla_and_bev = joint_freq_xy(make_and_type, "TESLA", "Battery Electric Vehicle (BEV)")
joint_freq_of_tesla_and_phev = joint_freq_xy(make_and_type, "TESLA", "Plug-in Hybrid Electric Vehicle (PHEV)")

joint_freq_of_chev_and_bev = joint_freq_xy(make_and_type, "CHEVROLET", "Battery Electric Vehicle (BEV)")
joint_freq_of_chev_and_phev = joint_freq_xy(make_and_type, "CHEVROLET", "Plug-in Hybrid Electric Vehicle (PHEV)")

joint_freq_of_niss_and_bev = joint_freq_xy(make_and_type, "NISSAN", "Battery Electric Vehicle (BEV)")
joint_freq_of_niss_and_phev = joint_freq_xy(make_and_type, "NISSAN", "Plug-in Hybrid Electric Vehicle (PHEV)")

joint_freq_of_toy_and_bev = joint_freq_xy(make_and_type, "TOYOTA", "Battery Electric Vehicle (BEV)")
joint_freq_of_toy_and_phev = joint_freq_xy(make_and_type, "TOYOTA", "Plug-in Hybrid Electric Vehicle (PHEV)")

joint_freq_of_vw_and_bev = joint_freq_xy(make_and_type, "VOLKSWAGEN", "Battery Electric Vehicle (BEV)")
joint_freq_of_vw_and_phev = joint_freq_xy(make_and_type, "VOLKSWAGEN", "Plug-in Hybrid Electric Vehicle (PHEV)")

print("    Marginal Distribution of Make      ")
print("f(TESLA) = ", freq_of_tesla)
print("f(CHEVROLET) = ", freq_of_chev)
print("f(NISSAN) = ", freq_of_niss)
print("f(TOYOTA) = ", freq_of_toy)
print("f(VOLKSWAGEN) = ", freq_of_vw)
print("\n\n")

print("     Joint Distribution of Make AND Type       ")

print("f(TESLA and BEV)", joint_freq_of_tesla_and_bev)
print("f(TESLA and PHEV)", joint_freq_of_tesla_and_phev)

print("f(CHEVROLET and BEV)", joint_freq_of_chev_and_bev)
print("f(CHEVROLET and PHEV)", joint_freq_of_chev_and_phev)

print("f(NISSAN and BEV)", joint_freq_of_niss_and_bev)
print("f(NISSA and PHEV)", joint_freq_of_niss_and_phev)

print("f(TOYOTA and BEV)", joint_freq_of_toy_and_bev)
print("f(TOYOTA and PHEV)", joint_freq_of_toy_and_phev)

print("f(VOLKSWAGEN and BEV)", joint_freq_of_vw_and_bev)
print("f(VOLKSWAGEN and PHEV)", joint_freq_of_vw_and_phev)
print("\n\n")

marg_freq_of_not_eligible = marginal_freq_x(eligibility, "Not eligible due to low battery range")
marg_freq_of_unknown = marginal_freq_x(eligibility, "Eligibility unknown as battery range has not been researched")
marg_freq_of_eligible = marginal_freq_x(eligibility, "Clean Alternative Fuel Vehicle Eligible")

marg_freq_of_battery = marginal_freq_x(veh_type, "Battery Electric Vehicle (BEV)")
marg_freq_of_hybrid = marginal_freq_x(veh_type, "Plug-in Hybrid Electric Vehicle (PHEV)")


joint_freq_of_not_elig_and_battery = joint_freq_xy(veh_and_elig,"Battery Electric Vehicle (BEV)",   "Not eligible due to low battery range")
joint_freq_of_not_elig_and_hybrid = joint_freq_xy(veh_and_elig,"Plug-in Hybrid Electric Vehicle (PHEV)",   "Not eligible due to low battery range")

joint_freq_of_unknown_and_battery = joint_freq_xy(veh_and_elig,"Battery Electric Vehicle (BEV)",   "Eligibility unknown as battery range has not been researched")
joint_freq_of_unknown_and_hybrid = joint_freq_xy(veh_and_elig,"Plug-in Hybrid Electric Vehicle (PHEV)",   "Eligibility unknown as battery range has not been researched")

joint_freq_of_elig_and_battery = joint_freq_xy(veh_and_elig,"Battery Electric Vehicle (BEV)",   "Clean Alternative Fuel Vehicle Eligible")
joint_freq_of_elig_and_hybrid = joint_freq_xy(veh_and_elig,"Plug-in Hybrid Electric Vehicle (PHEV)",   "Clean Alternative Fuel Vehicle Eligible")

# MARGINAL FREQUENCIES
print("        Marginal Distribution of Eligibility    ")
print("P(Not Eligible) = ", marg_freq_of_not_eligible/n)
print("P(Unknown) = ", marg_freq_of_unknown/n)
print("P(Eligible)", marg_freq_of_eligible/n)
print("\n\n")


print("        Marginal Distribution of Type        ")
print("P(Battery Vehicle) = ", marg_freq_of_battery/n)
print("P(Hybrid) = ", marg_freq_of_hybrid/n)
print("\n\n")

# JOINT FREQUENCIES
print("        Joint Frequency of Type and Eligibility        ")
print("P(Battery and Not Eligible) = ", joint_freq_of_not_elig_and_battery/n) 
print("P(Battery and Unknown) = ", joint_freq_of_unknown_and_battery/n) 
print("P(Battery and Eligible) = ", joint_freq_of_elig_and_battery/n) 
print("P(Hybrid and Not Eligible) = ", joint_freq_of_not_elig_and_hybrid/n) 
print("P(Hybrid and Unknown) = ", joint_freq_of_unknown_and_hybrid/n) 
print("P(Hybrid and Eligible) = ", joint_freq_of_elig_and_hybrid/n) 
print("\n\n")

# CONDITIONAL FREQUENCIES
print("   Conditional Distribution of Eligibility given Type = Battery    ")
print("P(Not Eligible | Battery) = ", joint_freq_of_not_elig_and_battery/marg_freq_of_battery)
print("P(Unknown | Battery) = ", joint_freq_of_unknown_and_battery/marg_freq_of_battery)
print("P(Eligible | Battery) = ", joint_freq_of_elig_and_battery/marg_freq_of_battery)
print("\n\n")

print("   Conditional Distribution of Eligibility given Type = Hybrid    ")
print("P(Not Eligible | Hybrid) = ", joint_freq_of_not_elig_and_hybrid/marg_freq_of_hybrid)
print("P(Unknown | Hybrid) = ", joint_freq_of_unknown_and_hybrid/marg_freq_of_hybrid)
print("P(Eligible | Hybrid) = ", joint_freq_of_elig_and_hybrid/marg_freq_of_hybrid)
print("\n\n")

print("   Conditional Distribution of Type Given Eligibility = Not Eligible")
print("P(Battery | Not Eligible) = ", joint_freq_of_not_elig_and_battery/marg_freq_of_not_eligible)
print("P(Hybrid| Not Eligible) = ", joint_freq_of_not_elig_and_hybrid/marg_freq_of_not_eligible)
print("\n\n")


print("   Conditional Distribution of Type Given Eligibility = Unknown")
print("P(Battery | Unknown) = ", joint_freq_of_unknown_and_battery/marg_freq_of_unknown)
print("P(Hybrid| Unknown) = ", joint_freq_of_unknown_and_hybrid/marg_freq_of_unknown)
print("\n\n")

print("   Conditional Distribution of Type Given Eligibility = Eligibile")
print("P(Battery | Eligible) = ", joint_freq_of_elig_and_battery/marg_freq_of_eligible)
print("P(Hybrid| Eligible) = ", joint_freq_of_elig_and_hybrid/marg_freq_of_eligible)
print("\n\n")


fig, axes = plt.subplots()

axes.bar("Eligible", joint_freq_of_elig_and_hybrid/marg_freq_of_eligible, color="lightcoral", ec="blue", label= "Hybrid")
axes.bar("Eligible", joint_freq_of_elig_and_battery/marg_freq_of_eligible, bottom=joint_freq_of_elig_and_hybrid/marg_freq_of_eligible, color="lightgreen", ec="blue", label="Battery")

axes.bar("Unknown", joint_freq_of_unknown_and_hybrid/marg_freq_of_unknown, color="lightcoral", ec="blue")
axes.bar("Unknown", joint_freq_of_unknown_and_battery/marg_freq_of_unknown, bottom=joint_freq_of_unknown_and_hybrid/marg_freq_of_unknown, color="lightgreen", ec="blue")

axes.bar("Not Eligible", joint_freq_of_not_elig_and_hybrid/marg_freq_of_not_eligible, color="lightcoral", ec="blue")
axes.bar("Not Eligible", joint_freq_of_not_elig_and_battery/marg_freq_of_not_eligible, bottom=joint_freq_of_not_elig_and_hybrid/marg_freq_of_not_eligible, color="lightgreen", ec="blue")

axes.legend()
plt.show()
