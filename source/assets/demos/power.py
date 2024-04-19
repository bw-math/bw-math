import statistics as stat
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Button, TextBox, Slider

null_mean = 11
alternate_mean = 10
stdev = 3
n = 30
significance = 0.05
increments = 1000

std_err = stdev / math.sqrt(n)

(fig, axes) = plot.subplots()

plot.suptitle(f"Null vs Alternative Distribution \n Known Std Dev σ of  = {stdev}, n = {n}")

axes.set_ylabel("Probability Density")
axes.set_xlabel("Sample Mean")

fig.subplots_adjust(left=0.5, bottom=0.25)

fig.text(0.05, 0.85, "Null Distribution")
fig.text(0.05, 0.70, "Alternate Distribution")

null_axis = fig.add_axes([0.20, 0.75, 0.15, 0.075])
null_slider = Slider(
    ax=null_axis,
    label="μ_null",
    valmin=10,
    valmax=14,
    valinit=null_mean,
    orientation="horizontal"
)
         
alternate_axis = fig.add_axes([0.20, 0.60, 0.15, 0.075])
alternate_slider = Slider(
    ax=alternate_axis,
    label="μ_alternate",
    valmin=6,
    valmax=11,
    valinit=alternate_mean,
    orientation="horizontal"
)
         
significance_axis = fig.add_axes([0.20, 0.45, 0.15, 0.075])
significance_text = TextBox(significance_axis, "Significance: ", textalignment="center")

power_axis = fig.add_axes([0.20, 0.30, 0.15, 0.075])
power_text = TextBox(power_axis, "Power: ", textalignment="center")

error_axis = fig.add_axes([0.20, 0.15, 0.15, 0.075])
error_text = TextBox(error_axis, "P(Type II Error): ", textalignment="center")

def redraw():
    axes.clear()
    
    start = int(
        min([ null_mean - 3 * std_err, alternate_mean - 3 * std_err])
    )
    end = int(
        max([null_mean + 3 * std_err, alternate_mean + 3 * std_err])
    )
    delta = (end - start)/increments
    
    null = stat.NormalDist(null_mean, stdev/math.sqrt(n))
    alternate = stat.NormalDist(alternate_mean, stdev/math.sqrt(n))

    null_crits = crit = null.inv_cdf(significance/2), null.inv_cdf(1-significance/2)
    power = alternate.cdf(null_crits[0])
    
    power_text.set_val(round(power, 4))
    error_text.set_val(round(1-power, 4))

    axis = [ start + delta*i for i in range(increments+1) ]
    null_density = [ null.pdf(x) for x in axis ]
    alternate_density = [ alternate.pdf(x) for x in axis ]

    axes.plot(axis, null_density, label = "Null", color = "black")
    axes.plot(axis, alternate_density, label = "Alternate", color = "gray")

    lower_null_axis = [ x for x in axis if x < null_crits[0] ]
    lower_null_region = [ null.pdf(x) for x in lower_null_axis ]
    axes.fill_between(lower_null_axis, lower_null_region, 0, color = "red", alpha =0.7)

    lower_alternate_axis = [ x for x in axis if x > null_crits[0] ]
    lower_alternate_region = [ alternate.pdf(x) for x in lower_alternate_axis ]
    axes.fill_between(lower_alternate_axis, lower_alternate_region, 0, color = "purple", alpha = 0.7)
    
    fig.legend()
    fig.canvas.draw_idle()
    
def set_null_mean(new_mu):
    global null_mean
    null_mean = float(new_mu)
    redraw()
    
def set_alternate_mean(new_mu):
    global alternate_mean
    alternate_mean = float(new_mu)
    redraw()
    
def set_significance(new_alpha):
    global significance
    significance = float(new_alpha)
    redraw()


null_slider.on_changed(set_null_mean)
alternate_slider.on_changed(set_alternate_mean)
significance_text.on_text_change(set_significance)

significance_text.set_val(significance)
plot.show()
