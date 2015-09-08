Title: Energy storage and the Tesla battery 
Authors: Levien van Zon
Date: 2015-06-03
Modified: 2015-09-03
Tags: energy
Slug: storage

**By Levien van Zon**

*The footnotes provide additional background information, and can safely be skipped or read separately.*

A few months ago, Tesla's Elon Musk [announced](https://www.youtube.com/watch?v=yKORsrlN-2k) a new product for energy storage, the [Tesla Powerwall](http://www.teslamotors.com/powerwall). This announcement generated a lot of attention, both on the Internet and in the global media. Some hail it as the next disruptive technological step in the sustainable energy revolution. Others are more sceptical, pointing out the technical limitations and hidden costs of the system[^tesladiscussion]. Such discussions aside for a moment, I think it's good to take a step back and look at what all the fuss is about. The first question to ask would be this: What problem is Tesla Energy trying to solve with its new battery products? 


As Elon Musk explains in his [keynote speech](https://www.youtube.com/watch?v=yKORsrlN-2k): *"We have this handy fusion reactor in the sky, the sun,"* which *"produces ridiculous amounts of power."* However, "*the obvious problem with solar power is that the sun does not shine at night.*" So, if we want solar energy to replace the electricity generated from fossil fuels, we need some way of storing the power generated during the day, so we can use it any time we need it. This may sound trivial: After all we have batteries, right? True, but *"the issue with existing batteries, is that they suck."* They are large, expensive, have a short life span and are hard to integrate with existing infrastructure. That's where the Powerwall comes in. It's designed to be an attractive, scalable and relatively cheap battery solution that "just works". It comes in two versions, a 7 kW·h model designed for daily charging and discharging, and a 10 kW·h model designed for occasional use as backup power supply. Up to nine batteries can be combined, for storage up to 90 kW·h. And for industrial use, Tesla introduced the Powerpack, which comes in 100 kW·h units that are infinitely scalable. And addressing the problem of short life span, Tesla offers a 10-year warranty on the Powerwall.


In short, the Powerwall promises to be the iPhone of energy storage solutions, solving the problem of solar energy availability in an elegant way. Moreover, it promises to offer a sustainable option for going "off-grid", at a fraction of the cost of comparable alternatives. Does that sound too good to be true? Well, to some extent it is.


### The problem with batteries

Batteries are hardly a new technology. The first "modern" electrochemical battery was built over two centuries ago by Alessandro Volta, and in fact the principle hasn't really changed since then. The first rechargable battery, a lead-acid battery, was invented in 1859 by Gaston Planté. This type of battery is still widely used in cars today. The first electric car was built in the 1830's, and by the start of the 20th century electric vehicles with rechargable batteries were commonplace. In fact, when it comes to driving a car, an electric motor is superior to a combustion engine in almost every way. It's simpler, cleaner, more quiet, and *much* more efficient. So what happened? Why did electric cars disappear for almost a century, and why is it now taking so long for electric driving to really take off? The answer lies mainly in energy storage.[^evhistory]


The internal combustion engine is a ridiculously complicated way of converting fuel into movement. Moreover, it's hopelessly inefficient, with even modern designs wasting around 75% of their energy as heat. But it has one important advantage: fossil fuels have an extremely high energy density. The energy density is a measure of how much energy is packed in a given volume or weight.[^energydensity] Burning 1 kg of gasoline or diesel yields around 13 kW·h of energy. By comparison, 1 kg of modern lithium-ion battery can store somewhere between 0.1 and 0.3 kW·h of energy. And that does not even take into account the weight of the battery casing and electronics. Lead-acid batteries are even worse, with 1 kg of battery holding only around 0.04 kW·h of energy. In other words, an amount of fossil fuel with the same weight as a modern battery, will contain 50 to 100 times as much energy. This leads to the strange situation that an average gasoline-powered SUV can easily outperform an electric car when it comes to action radius. Even though the SUV actually wastes *over 99% of the energy* in its fuel in producing heat, overcoming friction and lugging around 1500 kg of steel, it can afford such terrible inefficiency because its fuel contains so much energy! A car like that drives roughly 10 km on a litre of gasoline, which contains roughly 10 kW·h of energy. Another way of saying this, is that a 10 kW·h Powerwall battery pack (which currently costs $3500) can hold the same amount of energy as one litre of gasoline (which currently costs less than $2). Granted, electrical cars are more efficient in their use of energy than cars with a combustion engine. But from an economical and practical perspective, it's hard to compete with oil when it comes to powering transport.


Apart from their relatively low energy density and relatively high cost, there is another problem with batteries. Most batteries are electrochemical devices, which is to say they store electric energy in a chemical form. Charging a battery adds electrons to positively charged particles (cations) inside the battery. Discharging it removes electrons from negatively charged particles (anions) in the battery. Such chemical reactions, known as *redox reactions*, result in a flow of electrons which we call an electrical current, and which we can use to power our electrical devices. However, during each charge and discharge, the internal chemical state of a battery changes a little bit, negatively influencing its operation in the long term. Moreover, as the speed of a chemical reaction depends on temperature, so does the operation of a battery. Low temperatures decrease a battery's charge and current, and high temperatures increase the rate at which internal damage occurs. In other words, a battery won't work well when it's cold. And it has a limited life span, which rapidly decreases with heavy use and high temperatures.


The lithium-ion batteries in your average smartphone or laptop only last a few (roughly 2-5) years under normal, daily use. For comparison, other electronic components typically have an operational life span of 10-30 years. In modern portable devices, the battery is clearly the weakest link. In an electrical car however, the battery is the single most expensive component, so a life span of only a few years would be unacceptable. This is why the makers of electric cars have to resort to a number of measures that increase the life span of their batteries. They select battery types that favour durability over maximising energy density. They add thermal management systems that keep the battery at optimal operating temeratures. And they use software to monitor and manage battery discharge, making sure that the battery is only partially discharged, increasing its life span at the cost of usable capacity.[^dodlifespan]



### Grid issues

So, energy storage is important for mobile and portable devices. But in the case of electricity storage, the life span and usability of such devices is often limited by the low energy density and short life span of their batteries. It is a good thing then, that most devices that need electricity are stationary. Think of heating and cooling and cooking equipment, lights, televisions, many computers and all chargers. We plug them in, and they continue to work until we turn them off, or until they break. Their power source doesn't run out, wear out or weigh down the device. Instead, the energy they need is generated, usually from coal or gas, in very large power plants[^plantefficiency], and then transported to our house through a fairly efficient network of cables and transformers, better known as the electricity grid.


The electricity grid is quite an amazing and often underrated piece of human engineering. But what many people don't realise is that electricity cannot be magically stored in it. Quite the contrary: in order for the electricity grid to function, energy supply and demand have to be *almost perfectly balanced at all times*.[^gridbalance] If the demand for electricity falls, power plants have to be physically throttled back or taken offline. If energy demand rises, supply is increased where possible by increasing power plant output, or by bringing extra plants online.[^plantthrottle] But if this cannot be done fast enough, industrial-scale electricity users such as aluminium smelters are under contract with grid operators to automatically cut back their power use for a short time.


Advocates of sustainable energy often claim that we can get rid of fossil fuels, simply by installing sufficient windmills and solar PV-panels and hooking them up to the grid. Because supply and demand always need to be balanced, it is true that a supply of electricity generated from solar and wind will at any given moment reduce the fraction of fossil-fuel powered electricity on the grid. To compensate for the renewable energy supply, especially gas-powered plants will be throttled back or powered down. But as soon as the renewable electricity supply is reduced by cloudy weather, lack of wind, or nightfall, these same power plants will have to be fired back up to compensate for the reduced supply.


The important point here is that, while adding wind and solar power to the grid may *reduce* the use of fossil fuels, they still require a full fossil-powered energy infrastructure to be built and maintained to provide an equivalent power-generating capacity during, say, windless nights. This double investment in infrastructure greatly increases the costs of "greening" the electricity supply. And the continued *dependence* on fossil fuels, combined with their attractively low costs, doesn't provide any incentive to actually *switch* to using mainly 

alternative sources of energy. After all, what's the point of switching if you need a fossil-powered backup that is actually cheaper to operate than the thing you'd want to switch to?


This is where energy storage comes in. Installing for instance solar PV on a large scale, tends to generate a surplus of energy on sunny days. If this surplus generated during the day could be stored, and used at night, there would be less need to keep fossil-powered power plants around as a backup. Of course, to make a real difference, such storage must be significant, it must be at the scale of power-plants. And also, you need to have sufficient surplus energy on an average day to recharge the storage, even in winter.


There are not many practical ways to store large amounts of energy. The easiest method is actually already in wide use: just pump water up to a lake somewhere in the hills when you have too much electricity, and let it flow back down through a turbine when you have too little. 

   - Look up pumped storage capacity example(s). The one in Wales has country-scale capacity.
   - You do need two big lakes and a hill. Most really good locations are already in use.
   - Calculate how much water and how many batteries would be needed to replace one power station. 
   - Quote how much would be needed for the entire US (the example given by Musk). There is not enough lead in the world to do this with lead-acid. With Li-ion it would be possible, but of course quite expensive (how much?).

 - Note: Also decentral energy is unpredictable and hard to control, and therefore does not fit well with a highly centrally managed system like the grid.


### The role of Tesla

 - The role of Tesla is not (yet) to provide power backup for an entire country (no matter how trivial Musk makes it sound). This would be a lucrative contract no doubt. And Tesla can certainly contribute to grid storage, but it is a hard problem, best solved by a mix of approaches.
 - Better to start small: household-scale energy storage. For instance, for people with solar panels.
 - Batteries as home-scale storage are also not new (look up pictures), first lead acid, later Li-ion (name some companies) 
 - Li-ion has better life span than lead-acid, and takes up (much) less space.
 - Tesla offers relatively affordable home-scale storage and grid-scale storage, mostly due to scale of production.
 - Not the first ones, just better PR and very competitive pricing. 
   - But this is very important: they're the first to offer this not as a specialised niche-market solution, but as a mass produced "out of the box" solution (although, of course, it isn't exactly). 
 - Technically speaking it's nothing revolutionary. Proven technology, just nicely packaged and with some smart tricks to extend the inherently limited life span.
   - But this is actually the thing they do right: using and scaling up existing technology, making it widely available to consumers, instead of waiting around for some breakthrough. Trying to bring down cost. First aiming at those who can afford the luxury of backup storage or going off-grid, or just having a fancy sleek device on the wall. Same strategy as with their EV, which, incidentally is also an excellent grid power storage device. 



### But is it sustainable?

 - At first glance, yes. 
   - The idea of promoting home-scale PV is that any electricity it produces, will not have to be produced from fossil fuels. 
   - In countries like Germany and The Netherlands, this is easy: you hook up your PV-installation to the grid, and you get money for electricity you produce. This is why PV is so widely installed in Germany, even though it is not exactly the sunniest country in the world. 
   - In many countries the situation is different, you don't get any money for the power you produce, so your financial gain comes from using the power you produce yourself (thereby saving money on grid-power). In these cases it makes sense to install a battery, to make sure you can actually use all the power your panels produce during the day.
   - Especially if such countries are sunny (e.g. Australia and the US), affordable batteries may speed up the adoption of PV.

- From a sustainability perspective, there is a catch. Batteries are not free, they cost not only money but also energy to produce.
  - Actually, quite a lot of energy. (How much?)
  - Add to that the energy needed to produce the solar panels and inverter.
  - How long is the EROI? And how long before the carbon emissions become negative?
  - Presumably, battery recycling can at least reduce the manufacturing energy and material requirements. 

- So, from a "weak sustainability" perspective, PV makes sense after some time (with or without battery). 
  - Weak, in the sense that it reduces the use of fossil energy somewhat, for every house with PV. 
  - But if it stays connected to the grid, you still need a full traditional grid-infrastructure as backup. That is, PV hardly reduces the maximum demand at night. Large-scale adoption of batteries *would* help reduce this. 

  - But many claim that the point of PV is to *replace* a fossil-derived electricity production system.
   - This means that enough stored energy must be available at night to offset the absence of sun. (Assuming that power-cables from the other side of the world are not a realistic option in the short term.)
   - How many batteries would you need for the US? (Musk claims not that much - how much energy would this require to produce? How much would this cost? Who would pay for this?)
   - Enough big numbers. Let's start small and keep the examples managable: scale of one house. Let's say the goal would be to take your house off-grid. (This could be attractive for more reasons than just sustainability.) (It would mean that the cost of maintaining a grid would go up for everyone else - but lets ignore that for a moment.)
   - Using Tesla's Powerwall, we'd need the daily cycling model (7 kWh).
    - Neat trick: using a 10 kWh battery at 70% DoD, plus thermal and load management.
    - Max. power is a problem, if you want to go fully off-grid. How many batteries would be needed to cover load peaks (washing machines, water cookers, ovens, etc.) at night?
    - Depends on where you live, how much electricity you use at what times, and how many solar panels you have. 
    - Look up typical electricity use curve for several countries, how much capacity would be needed for one night?
    - How much surplus solar energy is needed to charge this capacity during the day? 
    - Would probably require a fair number of panels in winter, how much in e.g. NL/DE?
    - Becomes more interesting when additive to electric car storage, could be combined with low-power lighting, smart grid equipment to limit peak loads etc. Good excercise in reducing power use.



### Hurdles and alternatives

 - We've seen that the Powerwall could contribute to sustainability of the electricity supply, but with a lot of ifs and maybes, and it won't be cheap.
 - Biggest challenges: Life span needs to go up, production energy cost and carbon need to go down.
 - For it to catch on a significant scale, probably fossil fuel needs to become more expensive first (which would unfortunately also raise the price of the equipment).
 - And then still: remember that we have become very used to being able to get large amounts of energy cheaply whenever we want to (at least 16A @230V in NL for a normal house, ~3.8kW). Our lifestyle has become dependent on *a lot* of power always being available, in the form of gas, electricity, gasoline and diesel.
 - Energy transition will probably be a bumpy ride. It always is, but it usually also comes with benefits. Last time the benefit was cheap and abundant energy. This will probably not be the case this time, at least not for a while. (Oil gives you *a lot* of stored energy basically for free, you just have to pump it up.) But at the very least, a diverse and decentralised power supply for the world would certainly be more robust and in a sense more democratic (people would become responsible for locally generating the power they (directly) use, and countries would be less dependent on other countries far away for their energy). 

 - What about alternatives for storage? Li-ion is a fairly complicated and not very robust technology. Lots of electronics is needed to manage charge and discharge. If it gets too warm, it breaks. And it's all highly integrated, so if it breaks, you basically have to replace the entire thing.
 - Alternative battery technologies: Low-tech iron batteries (could be cheap, without deep-cycling problems), high-tech redox flow (for utility scale). 
 - Pumped storage is very simple. Could maybe be used more at sea or in disused mines, but as it requires large volumes/weights (due to low density) it isn't really practical on a small scale, unless you happen to own a reservoir on a hill.

 - Heat is much easier to store than electricity! 
   - Collecting it is no problem: Heat collectors, thermal storage, both on power-plant and residential scale. 
    - Hybrid concentrating solar collectors ("sunflowers") as example of a CPVT-system (https://en.wikipedia.org/wiki/Concentrator_photovoltaics#Concentrated_photovoltaics_and_thermal). Airlight/Dsolar's parabolic solar dishes track and concentrate solar (12 kW PV + 21 kW thermal), and use several tricks to reduce material use (thin film mirrors, concenterating light on small PV chips instead of panels, transparent inflatable cover, fiber-based concrete structure rather than steel/aluminium). Hot-water cooling technology, developed by IBM to cool CPUs, cools PV chips and generate hot water (for heating/cooling/desalination). http://www.zurich.ibm.com/news/14/dsolar.html
    - Slightly more traditional: https://en.wikipedia.org/wiki/Photovoltaic_thermal_hybrid_solar_collector
       - http://www.northburnsolar.co.uk/solarpanels/solarpvt/solarpvt.html
       - http://www.solimpeks.com/pv-t-hybrid-solar-collectors/
       - http://solarwall.com/en/products/pvthermal.php
       - http://www.tessolarwater.com/index_en.html?zeuspv-t.html&2
       - http://www.engineering.com/ElectronicsDesign/ElectronicsDesignArticles/ArticleID/6123/Photovoltaic-Thermal-System-Achieves-86-Efficiency.aspx
       - Problems: http://www.solarblogger.net/2012/10/hybrid-pv-thermal-solar-panels-good-idea.html
    - Proven technology: solar collector, thermal buffer, heat pump.
    - Are there options for molten salt as small-scale storage, heated by concentrated sunlight during the day, e.g. for cooking and heating?
    - Sorption cooling (thermally driven cooling) is an interesting alternative to using electrical heat pumps. There are other techniques: https://en.wikipedia.org/wiki/Solar_air_conditioning
    - Thermochemical heat storage is also interesting: https://www.fraunhofer.de/en/press/research-news/2014/march/sorption-energy-storage.html
   - The hard part is converting heat back to electricity.
    - We do this all the time: combustion engines and steam engines work by converting fossil fuel into heat, and then into movement. In power gerenators, movement is then converted into electricity. It's a ludicrous process if you think about it. Again, we only get away with it because fossil fuel contains so much energy that we can currently afford to waste most of it.
    - What is the efficiency of turning low-grade heat into electricity. What are the techniques available? Is this feasible on a small scale?
      - Thermoelectric generators currently have low output and efficiency, but are improving:
      - http://www.sciencedirect.com/science/article/pii/S1364032114001038
      - http://www.sciencedirect.com/science/article/pii/S1364032114000082
      - http://www.sciencedirect.com/science/article/pii/S1364032113008447
 - Other forms of chemical storage than a redox cell? That's how nature does it (ATP etc.), but turning it back into electricity is still tricky. Carbohydrates can be made (basically oil), but combustion means a dismal efficiency. Our technology is rather primitive, still mostly relies on burning things. The best thing we have is still in essence 19th century technology, with a lot of tweaks.
 - But don't stand waiting around for new technology, especially with thermal energy. We still waste most of our high-grade energy (fossil and electrical) by turning it into heat! (And most of that escapes.)



[![A graph from Bosch Solar Storage, comparing energy consumption and PV production in a European country.](http://bosch-solar-storage.com/wp-content/uploads/2012/11/aut_1.jpg)](http://bosch-solar-storage.com/wp-content/uploads/2012/11/aut_1.jpg)
Source: http://bosch-solar-storage.com/independence/self-reliance/

[![Energy consumption and PV production in Sidney, Australia.](http://www.solarchoice.net.au/blog/wp-content/uploads/Average-NSW-household-in-summer-electricity-consumption-vs-PV-generation1.JPG)](http://www.solarchoice.net.au/blog/wp-content/uploads/Average-NSW-household-in-summer-electricity-consumption-vs-PV-generation1.JPG)
Source: http://www.solarchoice.net.au/blog/home-energy-consumption-versus-solar-pv-generation/

[![Energy consumption and PV production in the US](http://blogs-images.forbes.com/jamesconca/files/2014/11/SolarGrid.jpg)](http://blogs-images.forbes.com/jamesconca/files/2014/11/SolarGrid.jpg)
Source: Edison Foundation Institute for Electric Innovation, via http://www.forbes.com/sites/jamesconca/2014/11/28/net-energy-metering-are-we-capitalists-or-what/

[![Individual household load profiles](http://www.pv-magazine.com/typo3temp/pics/11071_Individual_household_load_profiles_3sppdf_431ed866aa.jpg)](http://www.pv-magazine.com/typo3temp/pics/11071_Individual_household_load_profiles_3sppdf_431ed866aa.jpg)
Source: http://www.pv-magazine.com/archive/articles/beitrag/storage-has-landed-_100009059/501/#axzz3YryioctT

http://www.agora-energiewende.de/en/
http://www.compendiumvoordeleefomgeving.nl/indicatoren/nl0035-Energieverbruik-door-de-huishoudens.html?i=6-40



Interested in reading more articles like this? Follow us [on Facebook](https://www.facebook.com/duurzaamheidsweb), or through our [Atom-feed](/feeds/all.atom.xml).



-----

### Notes:


[^tesladiscussion]:
*Some hail it as the next step in the sustainable energy revolution, while others are more sceptical, pointing out the technical limitations and hidden costs of the system.*   


[^evhistory:]:
*Why did electric cars disappear for almost a century, and why is it now taking so long for electric driving to really take off? The answer lies mainly in energy storage.*  


[^energydensity]:
*The energy density is a measure of how much energy is packed in a given volume or weight.**  
Actually, energy density is energy per unit volume. Energy per unit weight is called *specific energy*. Gasoline has a specific energy of around 12.8 kW·h/kg, and an energy density of around 9.6 kW·h/L. Diesel has a specific energy of around 12.7 kW·h/kg, and an energy density of around 10.8 kW·h/L. A lithium-ion battery cell has a specific energy of 0.1-0.3 kW·h/kg, and an energy density of around 0.2-0.6 kW·h/L. Uranium has a specific energy of over 21 million kW·h/kg. See also: https://xkcd.com/1162/


[^dodlifespan]:
*And they use software to monitor and manage battery discharge, making sure that the battery is only partially discharged, increasing its life span at the cost of usable capacity.*  
The life span of a chemical battery depends to a very large extent on the *Depth of Discharge (DoD)*, the percentage of the battery capacity that is utilised during normal use. A lithium-ion battery typically lasts around 3000-5000 charge/discharge cycles, if its full capacity is used (a DoD of 100%). With daily use, this would translate to a life span of roughly 8-14 years. If only 80% of the capacity is regularly used, the battery life span increases to 5000-7000 cycles, or 14-19 years. And a modern Li-ion battery is expected to last up to 10,000 cycles (27 years) if the DoD is reduced to 33%.  
One of the reasons to prefer Li-ion over lead acid batteries for daily energy storage needs, is that lead acid batteries degrade much faster. With a DoD of 100%, a lead acid battery will only last 300-800 charge/discharge cycles, or 1-2 years with daily use. At 80% DoD the life span is 400-1000 cycles (1-3 years), and at 33% DoD it is still only 900-2000 cycles (2.5-5.5 years).  
The definition of battery life span used here assumes that its service life ends when capacity falls below 80%, or when the battery stops functioning. Source: [Rydh & Sandén, 2005](http://dx.doi.org/10.1016/j.enconman.2004.10.003), table 3.


[^plantefficiency]:
*the energy they need is generated, usually from coal or gas, in very large power plants* 
Although certainly better than your average car engine, the generation of electricity from fossil fuels is also not overly efficient. A modern power plant still wastes around 55-60% of the fossil energy as heat. The grid electricity we use, when generated from coal or gas, is the 40-45% of the energy remaining after burning these fossil fuels.


[^gridbalance]:
*In order for the electricity grid to function, energy supply and energy demand have to be almost perfectly balanced at all times.*  
The system can actually overcome faily significant load imbalances that last from a few milliseconds up to a few minutes. In fact, the design is such that if the largest power plant in a grid suddenly goes offline, the grid should still continue to function. To understand how this works, read [this fascinating explanation on the Forbes website](http://www.forbes.com/sites/quora/2013/10/07/what-is-the-holding-capacity-of-the-us-power-grid/).


[^plantthrottle]:
*If the demand for electricity falls, power plants have to be physically throttled back or taken offline. If energy demand rises, supply is increased where possible by increasing power plant output, or by bringing extra plans online.*  
Typically, only the output of gas-fired power plants can be rapidly modified (and even that takes around ten seconds).
