import statistics as stat
import random as random
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Button, TextBox, RadioButtons

mpl.use("tkagg")

(fig, axes) = plot.subplots()

n, m = 20, 500

plot.suptitle(f"Simulated Sampling Distributions \n Observations Per Sim = {n}, Simulations = {m}")
axes.set_xlabel("Simulated Statistic")
axes.set_ylabel("Probability Density")

fig.subplots_adjust(left=0.3, bottom=0.25)

button_axes = fig.add_axes([0.81, 0.05, 0.1, 0.075])
simulate_button = Button(button_axes, "Simulate")

mtext_axes = fig.add_axes([0.1, 0.8, 0.10, 0.075])
mean_text = TextBox(mtext_axes, "Pop. Mean", textalignment="center")

stext_axes = fig.add_axes([0.1, 0.7, 0.10, 0.075])
s_text = TextBox(stext_axes, "Pop. St. Dev", textalignment="center")

stat_axes = fig.add_axes([0.05, 0.35, 0.15, 0.3])
stat_radio = RadioButtons(
    stat_axes,
    (
        'sample mean',
        'sample median',
        'sample variance(n)',
        'sample variance(n-1)',
        'sample iqr',
        'sample range'
    ),
    label_props={
        'color': [ 'red', 'blue', 'green', 'orange', 'yellow', 'purple']
    },
    radio_props={
        'facecolor': ['red', 'blue', 'green', 'orange', 'yellow', 'purple'],
        'edgecolor': ['darkred', 'darkblue', 'darkgreen', 'darkorange', 'gold', 'black'],
    }
)

default_mu, default_s = 10, 3

mu, s = default_mu, default_s

simulation_goal = "sample mean"

def reset():
    mu, s, n, m = default_mu, default_s, default_n, default_m

def set_mean(new_mu):
    global mu
    mu = float(new_mu)

def set_standard_deviation(new_s):
    global s
    s = float(new_s)

def set_simulation_goal(goal):
    global simulation_goal
    simulation_goal = goal
    
def simulate(event):
    # simulate samples from a normal population
    
    sampling_distribution = []
    
    for i in range(m):
        sim_sample = [
            random.gauss(mu, s) for _ in range(n)
        ]

        if simulation_goal == "sample mean":
            sampling_distribution.append(
                stat.mean(sim_sample)
            )
            
        elif simulation_goal == "sample median":
            sampling_distribution.append(
                stat.median(sim_sample)
            )

        elif simulation_goal == "sample variance(n)":
            sampling_distribution.append(
                stat.pvariance(sim_sample)
            )
        
        elif simulation_goal == "sample variance(n-1)":
            sampling_distribution.append(
                stat.variance(sim_sample)
            )

        elif simulation_goal == "sample iqr":
            percentiles = stat.quantiles(sim_sample, n=100)
            iqr = percentiles[74] - percentiles[24]
            sampling_distribution.append(
                iqr
            )
            
        elif simulation_goal == "sample range":
            s_range = max(sim_sample) - min(sim_sample)
            sampling_distribution.append(
                s_range
            )
            
    axes.clear()
    axes.set_xlabel("Observation")
    axes.set_ylabel("Probability Density")

    simulated_stat = stat.mean(sampling_distribution)

    if simulation_goal == "sample mean":
        axes.axvline(mu, linestyle="-", color="red", label="True Value")

    elif simulation_goal == "sample variance(n)" \
       or simulation_goal == "sample variance(n-1)":
        axes.axvline(s**2, linestyle="-", color="red", label="True Value")

    elif simulation_goal == "sample median":
        axes.axvline(mu, linestyle="-", color="red", label="True Value")


    elif simulation_goal == "sample iqr":
        dist = stat.NormalDist(mu, s)
        iqr = dist.inv_cdf(0.75) - dist.inv_cdf(0.25)
        axes.axvline(iqr, linestyle="-", color="red", label="True Value")

    elif simulation_goal == "sample range":
        axes.axvline(6*s, linestyle="-", color="red", label="True Value")
        
    axes.axvline(simulated_stat, linestyle="--", color="green", label="Estimated Value")
    
    axes.hist(sampling_distribution, density=True, color="lightblue", ec="darkblue")

    axes.legend()

    fig.canvas.draw_idle()

simulate_button.on_clicked(simulate)
stat_radio.on_clicked(set_simulation_goal)

mean_text.on_text_change(set_mean)
s_text.on_text_change(set_standard_deviation)

mean_text.set_val(default_mu)
s_text.set_val(default_s)

plot.show()
