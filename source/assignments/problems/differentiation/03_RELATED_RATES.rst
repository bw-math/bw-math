.. _related_rates_classwork:

=============
Related Rates
=============

1. Water is draining out of the bottom of a 5000-gallon tank. The volume *V* of the water (in gallons) remaining in the tank after *t* minutes is given by the following formula:

.. math::

	V = 5000 (1 - \frac{t}{40})^2
	
a. Find a formula for :math:`\frac{dV}{dt}` in terms of *t*.

b. How quickly is the water initially draining from the tank?

c. How quickly is the water draining from the tank at :math:`t = 30 \text{minutes}`?



2. In the theory of electrical circuits, *Ohm's Law* describe the relationship between the voltage *V* across a resistor, the electrical current *I* passing through the resistor, and a quantity *R* known as the resistance. The law can be written as follows:

.. math::

	V = IR
	
Usually voltage is measured in volts, current is measured in amperes (amps), and resistance is measured in ohms, where :math:`1 \text{ohm}=\frac{1 \text{volt}}{\text{amp}}`. In a circuit with variable resistance, the quantities *V*, *I* and *R*, all depend on time.

a. Take the derivative of *Ohm's Law* to find an equation relating :math:`\frac{dV}{dt}`, :math:`\frac{dI}{dt}` and :math:`\frac{dR}{dt}`.

b. Suppose the current is increasing at a rate of :math:`0.3 \frac{\text{amps}}{\text{sec}}`, while the resistance is holding steady at 4 ohms. How quickly is the voltage across the resistor increasing?

c. Now suppose the voltage across the resistor is held constant at 20 volts, while the resistance is steadily increased at a rate of :math:`0.4 \frac{\text{ohms}}{\text{sec}}`. What is the current through the resistor when the resistance reaches 10 ohms?

d. In the same scenario as *part c*, at what rate is the current changing at that time? Is it increasing or decreasing?



3. Boat A is sailing north away from a dock, while boat B is sailing west towards the same dock:

.. image:: ../../../assets/imgs/classwork/jimbelk_hw4_03.png
	:align: center
	
a. Find an equation that relates :math:`\frac{dA}{dt}`, :math:`\frac{dB}{dt}` and :math:`\frac{dL}{dt}`.

b. Is :math:`\frac{dA}{dt}` positive or negative? What about :math:`\frac{dB}{dt}`? Explain.

c. Suppose that boat A is 30 kilometers north of the dock, and is sailing north at a rate of :math:`10 \frac{\text{km}}{\text{hour}}`. Meanwhile, boat B is 40 kilometers east of the dock and is sailing west at a rate of :math:`15 \frac{\text{km}}{\text{hour}}`. What is the present distance between the two boats?

d. In the same scenario as *part c*, what is :math:`\frac{dA}{dt}`?? What is :math:`\frac{dB}{dt}`?

c. In the same scenario as *part c* and *part d*, how quickly is the distance between the boats changing? Is the distance increasing or decreasing? 



4. A positively charged particle is flying in the vicinity of a charged conductor. The electric potential energy of the particle is given by the formula,

.. math::
	
	E = k_{e} \cdot \frac{qQ}{r}
	
Where *q* is the charge of the particle, *Q* is the charge on the conductor and *r* is the distance between them. :math:`k_{e}` is an electrical field constant with a known value of :math:`k_{e} = 0.90 cm \cdot \frac{J}{{\mu C}^2}`.

a. Assuming *q* and *Q* are constant, find a formula for :math:`\frac{dE}{dt}` in terms of *q*, *Q*, :math:`k_e`, *r* and :math:`\frac{dr}{dt}`.

b. At a certain instant, a particle with a charge of :math:`1.5 \mu C` is 20 centimeters away from a conductor, and is flying directly towards the conductor at a rate of :math:`2 \frac{\text{cm}}{\text{s}}`. Given that the conductor has a charge of :math:`4.0 \mu C`, how quickly is the electrical potential energy of the particle increasing?



5. *Boyle's Law* states that when a sample gas is compressed at a constant temperature, the pressure *P* and volume *V* satisfy the equation :math:`PV = c`, where *c* is a constant. Suppose that at a certain instant, the volume is 600 cubic centimeters, the pressure is *150 kPA* (*kilo-pascals*) and the pressure is increasing at a rate of :math:`20 \frac{\text{kPA}}{\text{min}}`. At what rate is the volume decreasing at this instant?
