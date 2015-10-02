Title: Energy storage and the Tesla battery
Authors: Levien van Zon
Date: 2015-06-03
Modified: 2015-09-23
Tags: energy
Slug: storage
Status: draft

**By Levien van Zon**

*The footnotes provide additional background information, and can safely be skipped or read separately.*

 - TODO: look up when battery production and sales are planned to start

Last April, Tesla's Elon Musk [announced](https://www.youtube.com/watch?v=yKORsrlN-2k) a new product for energy storage, the [Tesla PowerWall](http://www.teslamotors.com/powerwall). This announcement generated a lot of attention, both on the Internet and in the global media. Some hail it as the next disruptive technological step in the sustainable energy revolution. Others are more skeptical, pointing out the technical limitations and hidden costs of the system[^tesladiscussion]. Such discussions aside for a moment, I think it's good to take a step back and look at what all the fuss is about. The first question to ask would be this: What problem is Tesla Energy trying to solve with its new battery products? 


As Elon Musk explains in his [keynote speech](https://www.youtube.com/watch?v=yKORsrlN-2k): *"We have this handy fusion reactor in the sky, the sun,"* which *"produces ridiculous amounts of power."* However, "*the obvious problem with solar power is that the sun does not shine at night.*" So, if we want solar energy to replace the electricity generated from fossil fuels, we need some way of storing the power generated during the day, so we can use it any time we need it. This may sound trivial: After all we have batteries, right? True, but *"the issue with existing batteries, is that they suck."* They are large, expensive, have a short life span and are hard to integrate with existing infrastructure. That's where the PowerWall comes in. It's designed to be an attractive, scalable and relatively cheap battery solution that "just works". It comes in two versions, a 7 kW·h[^kWh] model designed for daily charging and discharging, and a 10 kW·h model designed for occasional use as a backup power supply. Up to nine batteries can be combined, for storage up to 90 kW·h. And for use on a more industrial scale, Tesla introduced the PowerPack, which comes in 100 kW·h units that are infinitely scalable. Moreover, addressing the problem of short life span, Tesla offers a 10-year warranty on the PowerWall.


In short, the PowerWall promises to be the iPhone of energy storage solutions, solving the problem of solar energy availability in a fairly elegant way. Moreover, it promises to offer a sustainable option for going "off-grid", at a fraction of the cost of comparable alternatives. Does that sound too good to be true? Well, to some extent it is.


### The problem with batteries

Batteries are hardly a new technology. The first "modern" electrochemical battery was built over two centuries ago by Alessandro Volta, and in fact the principle hasn't really changed since then. The first rechargeable battery, a lead-acid battery, was invented in 1859 by Gaston Planté. This type of battery is still widely used in cars today. The first electric car was built almost two centuries ago, in the 1830's, and by the start of the 20th century electric vehicles with rechargeable batteries were commonplace. In fact, when it comes to driving a car, an electric motor is superior to a combustion engine in almost every way. It's simpler, cleaner, less noisy, and *much* more efficient. So what happened? Why did electric cars disappear for almost a century, and why is it now taking so long for electric driving to really take off again? The answer lies mainly in energy storage.[^evhistory]


The internal combustion engine is a ridiculously complicated way of converting fuel into movement. Moreover, it's hopelessly inefficient, with even modern designs wasting around 75% of their input energy as heat. But it has one important advantage: fossil fuels have an extremely high energy density. The energy density is a measure of how much energy is packed in a given volume or weight.[^energydensity] Burning 1 kg of gasoline or diesel yields around 13 kW·h of energy, which is more than most houses use in a day. By comparison, 1 kg of modern lithium-ion battery can store somewhere between 0.1 and 0.3 kW·h of energy. And that does not even take into account the weight of the battery casing and electronics. Lead-acid batteries are even worse, with 1 kg of battery holding only around 0.04 kW·h of energy. In other words, an amount of fossil fuel with the same weight as a modern battery, will contain 50 to 100 times as much energy. This leads to the strange situation that an average gasoline-powered SUV can easily outperform an electric car when it comes to its action radius. Even though the SUV actually wastes *over 99% of the energy* in its fuel in producing heat, overcoming friction and lugging around at least 1500 kg of steel. It can afford such terrible inefficiency because its fuel contains so much energy! A car like that drives roughly 10 km on a litre of gasoline, which contains roughly 10 kW·h of energy. Another way of saying this, is that a 10 kW·h PowerWall battery pack (which currently costs $3500) can hold the same amount of energy as one litre of gasoline (which currently costs less than $2). Granted, electrical cars are more efficient in their use of energy than cars with a combustion engine. But from an economical and practical perspective, it's hard to compete with oil when it comes to powering transport.


Apart from their relatively low energy density and relatively high cost, there is another problem with batteries. Most batteries are electrochemical devices, which is to say they store electric energy in a chemical form. Charging a battery adds electrons to positively charged particles (cations) inside the battery. Discharging it removes electrons from negatively charged particles (anions) in the battery. Such chemical reactions, known as *redox reactions*, result in a flow of electrons that we call an electrical current, and which we can use to power our electrical devices. However, during each charge and discharge, the internal chemical state of a battery changes a little bit, negatively influencing its operation in the long term. Moreover, as the speed of a chemical reaction depends on temperature, so does the operation of a battery. Low temperatures decrease a battery's charge and output current, and high temperatures increase the rate at which internal damage accumulates. In other words, a battery won't work well when it's cold. And it has a limited life span, which rapidly decreases with heavy use and high temperatures.


The lithium-ion batteries in your average smart-phone or laptop typically only last a few (roughly 2-5) years under normal, daily use. For comparison, other electronic components typically have an operational life span of 10-30 years. In modern portable devices, the battery is clearly the weakest link. In an electrical car however, the battery is also the single most expensive component, so a life span of only a few years would be unacceptable. This is why the makers of electric cars have resorted to a number of measures that increase the life span of their batteries. They select battery types that favour durability over maximising energy density. They add thermal management systems that keep the battery at optimal operating temperatures. And they use software to monitor and manage battery discharge, making sure that the battery is only partially discharged, increasing its life span at the cost of usable capacity.[^dodlifespan]



### Grid issues

So, energy storage is important for mobile and portable devices. But the life span and usability of portable electronic devices is often limited by the low energy density and short life span of their batteries. It is a good thing then, that most devices that need electricity are stationary. Think of heating and cooling and cooking equipment, lights, televisions, desktop computers and battery chargers. We plug them in, and they continue to work until we turn them off, or until they break. Their power source doesn't run out, wear out or weigh down the device. Instead, the energy they need is generated, usually from coal or gas, in very large power plants[^plantefficiency], and then transported to our house through a fairly efficient network of cables and transformers, better known as the electricity grid.


The electricity grid is quite an amazing and often underrated piece of human engineering. But what many people don't realise is that it cannot magically store electricity. Quite the contrary: in order for the electricity grid to function, energy supply and demand have to be *almost perfectly balanced at all times*.[^gridbalance] If the demand for electricity falls, power plants have to be physically throttled back or taken offline. If energy demand rises, supply is increased, where possible by increasing power plant output, or by bringing extra plants online.[^plantthrottle] But if this cannot be done fast enough, industrial-scale electricity users such as aluminium smelters are under contract with grid operators to automatically cut back their power use for short periods of time.


Advocates of sustainable energy often claim that we can get rid of fossil fuels, simply by installing sufficient windmills and solar PV-panels, which are hooked up to the grid. Because supply and demand always need to be balanced, it is true that a supply of electricity generated from solar and wind will at any given moment reduce the fraction of fossil-fuel powered electricity on the grid. To compensate for the renewable energy supply, especially gas-fired plants will be throttled back or powered down. But as soon as the renewable electricity supply is reduced by cloudy weather, lack of wind or nightfall, these same power plants will have to be fired back up to compensate for the reduced supply of renewable electricity.


The important point here is that, while adding wind and solar power to the grid may *reduce* the use of fossil fuels on a daily or yearly basis, they still require a full fossil-powered energy infrastructure to be built and maintained to provide an equivalent power-generating capacity during, say, windless nights, or winter. This double investment in infrastructure greatly increases the costs of "greening" the electricity supply. And the continued *dependence* on fossil fuels, combined with their attractively low costs, doesn't provide any incentive to actually *switch* to alternative sources of energy. After all, what's the point of switching if you need a full fossil-powered backup infrastructure that is actually cheaper to operate than the thing you'd want to switch to?


This is where energy storage comes in. Installing for instance solar PV on a large scale, tends to generate a surplus of energy on sunny days. If the surplus generated during the day could be stored, and used at night, there would be less need to keep fossil-powered power plants around as a backup. Of course, to make a real difference, such storage must be significant, it must be at the scale of power-plants. And also, you need to have sufficient surplus energy on an average day to recharge your storage, even in winter.


### Storing the grid?

How much power does a typical power plant generate? It depends very much on the plant, but a typical coal-fired plant in the US can generate around 500 million watts (500 MW). New plants tend to have a larger capacity, up to 2000, 3000 or even 5000 MW especially in countries like China, where power generating capacity is being expanded at an almost unbelievable rate. A 500 MW power plant can generate around 12 million kW·h (= 12 GW·h) of electricity in a day. To store that amount of energy you would need 120,000 of Tesla's PowerPack battery units, or over 1.7 *million* PowerWall batteries (the 7 kW·h model for daily use). And that's only for *one* fairly small power plant.


In the keynote speech where he introduced Tesla's batteries, Elon Musk showed how much land would be required to cover the entire US electricity demand with solar panels:

![The "tiny blue square".](http://nerdist.com/wp-content/uploads/2015/05/MuskEnergy_2.png)

On the scale of a country, it's not that much ([less than 1% of land area for the US](http://www.nrel.gov/docs/fy08osti/42463.pdf)). It's still a lot of land of course, the area shown by Musk is roughly a 100 km x 100 km square in North-West Texas. Filled with solar panels, this could generate around 500 GW of electric power on average, indeed more than the current mean US electricity demand of 425 GW.[^musksquare] On an average day, the entire US uses over 10 billion kW·h of electricity (10.2 TW·h). Storing this amount of energy would require a little over 102 million Tesla PowerPack battery units. You'd probably need a bit more storage than that, to cover bad days and peak loads. Indeed, Musk himself estimates that around 160 million PowerPacks would be needed. It is by no means impossible to produce and install that much capacity, Musk noted that around 100 million new cars and trucks are put on the market every year. But it won't be cheap: the batteries alone would cost around 4 trillion dollars, and producing them would require up to 20% of the world's currently known lithium-reserves.[^squarebatt]


If the above sounds impractical, the situation gets worse if you realise that *electricity use* is only a small fraction of actual *energy use*. The US uses around 3 TW of energy in total, or about 72 TW·h per day on average. In other words, the energy use is seven times the electricity use! In the US, most of this energy is used for transport. But remember that combustion engines are very inefficient. So say we switch everything to electricity, this would reduce heat losses, bringing the power demand down by roughly a third, to 2 TW, or 48 TW·h per day.

On his blog [Do the Math](http://physics.ucsd.edu/do-the-math/2011/08/nation-sized-battery/), Tom Murphy shows that using lead-acid batteries to store a week's worth of US energy demand would require 4.5 trillion kg (4536 Mt) of lead, and would cost more than the annual US GDP. Even if we would reduce the storage capacity to just one day, we would still need more lead to build the batteries (648 Mt) than the world's known lead reserves (around 80 Mt). Using lithium-ion batteries we would fare a bit better. Extrapolating from Musk's estimate, we'd need around 753 million PowerPack batteries to cover total US energy use.[^ustotalenergy] This would require around 90% of the world's known lithium reserves.


Elon Musk furthermore states that with 900 million PowerPacks, we could transition the entire world electricity production to solar power. And with approximately 2 billion PowerPacks, we could transition all transport and heating as well. Obviously these are purely hypothetical figures. With current technology and known lithium reserves, it isn't possible to transition the entire US energy demand to solar power, let alone the global energy demand. But that doesn't mean you can't start somewhere, with a more modest goal.


### Pump up the storage

When it comes to energy storage, we tend to be focused on chemical batteries. Actually there are simpler ways of storing energy, especially when it comes to storing large amounts. And the easiest method is actually already in wide use: When you have too much electricity, just pump water up to a lake somewhere in the hills. Then when you have too little electricity, you can let it flow back down through a turbine. This is called Pumped Hydro Storage (PHS). You will lose some energy in the process of course, but the round-trip efficiency[^roundtrip] of modern PHS systems is around 80%, which is actually pretty good.


According to a [study](https://www.hydropower.org/study-the-hydropower-sector%E2%80%99s-contribution-to-a-sustainable-and-prosperous-europe) done for the International Hydropower Association (IHA), the current hydro storage capacity in Europe is estimated to be over 220 TW·h. That's equivalent to over 2.2 billion PowerPack batteries, enough to cover nearly 25 days of average European consumption! And what's more, contrary to Li-ion batteries, hydro storage requires less resources to produce on a large scale and doesn't need replacing every 15-20 years or so. So that solves the energy storage problem, or does it?


Of course there's a catch. Or rather, there are two. First of all, the 220 TW·h figure includes the storage capacity of *all* European hydro-power basins. Only a small fraction of this is pumped storage. The rest is conventional hydro-power, which cannot actively be recharged but has to wait for rivers and rain to refill the basin. This may take months or years. A large country like Germany only has around 0.05 TW·h of actual pumped storage, which can deliver 6.8 GW (= 6800 MW) of power for a period of 6 to 8 hours. That's a lot of power, comparable to the output of two large coal-fired plants. But it's not nearly enough to cover the German electricity demand, which amounts to roughly 1.6 TW·h on an average day, with demand fluctuating between lulls as low as 32 GW in summer, to peaks over 90 GW in winter. In fact, it's not even sufficient to cover the contribution of solar PV in Germany, which currently has a production capacity of around 38.5 GWp (gigawatt-peak, the power output under optimal laboratory conditions).[^germanpowerstats]

![Electricity production and demand in Germany on December 4th 2014 and June 14th 2015.]({filename}/images/agora-20141204-20150614.png)

 - 20141204 at 12:00: 1.7 GW solar, 3 GW wind, 2 GW pumped storage, 0.4 seasonal storage, 11.2 gas, 37.4 GW coal, 12.3 GW nuclear, 5.9 biomass, 4.9 hydro, 0.2 other, -0.8 export
 - 20150614 at 12:00: 15.7 GW solar, 3.1 GW wind, 0.5 GW pumped storage, 0.1 seasonal storage, 1.9 gas, 15 GW coal, 9.2 GW nuclear, 4.8 biomass, 3.1 hydro, 0.3 other, -8 export
 - In winter, much higher consumption, much more coal and gas, solar is negligable, hydro-storage plays a role. In summer, much more solar and lower consumption so lower baseload-production, significant export of energy.
 - Sources: www.energy-charts.de and http://www.agora-energiewende.de/en/topics/-agothem-/Produkt/produkt/76/Agorameter/


The second catch is more serious. If the problem were merely one of capacity, you could just build more pumped storage plants. But this is not so easy, because in fact the energy density of pumped hydro storage is absolutely terrible. In practice, this means that adding pumped hydro storage capacity requires space, *a lot* of space. The principle of pumped hydro is that lifting a weight to a certain height requires energy in order to overcome gravity. In this case, the weight is provided by a volume of water. To give you an idea of the amount of energy versus the volume of water needed: Storing the amount of energy in a normal AA-battery (3 W·h), would require hoisting 360 litres of water (roughly 2.5 filled bathtubs) up to a height of 3 metres, or 100 litres to a height of 10 metres. And that's just the energy in one small battery. Storing the energy in a litre of gasoline or a 10 kW·h PowerWall would require lifting our 100 litres to a height of 36 km, or perhaps more practical, lifting 360 m^3^ of water (e.g. a swimming pool of 25×10×1.44 m, weighing 360 tonnes) to a height of 10 m! Matching the capacity of the 100 kW·h PowerPack would require roughly an olympic swimming pool (50×25×2.88 m, containing 3.6 Mt water) lifted to 10 metres height.[^pumpedenergy] You probably get the point, the dismal energy density of pumped storage will make even a lowly lead-acid battery look *great*.


To have a pumped storage plant with any significant capacity, you'll need a rather big lake on a hill, and another one at least equally big at the base of the hill. There's not many places where you will find this situation occurring naturally. And if you do, emptying and refilling the lakes on a regular basis is going to have a big impact on water life. Of course you can always *create* a large lake by building a dam in a valley, this is how we often construct hydro-power facilities. But while such projects may contribute to reducing greenhouse gas emissions, the local environmental destruction that results certainly does not qualify them as "environmentally friendly".


In short, large-scale hydro-storage isn't going to solve the energy storage problem. There simply isn't enough space. And even if there were enough space, building the required infrastructure would result in widespread environmental destruction. Of course electrochemical batteries and pumped hydro storage aren't the only large-scale energy storage options. In fact, the second most important storage method is Compressed Air Energy Storage, or CAES. This has been around since the late 19th century, when compressed air was distributed over cities with pipes, and was used to power machines directly.[^caeshistory] Modern CAES uses electricity to compress air, and turns the compressed air back into electricity when needed. This is a bit more complicated than pumped hydro storage. You need some kind of high-pressure container, and the pressure generally isn't constant, so converting it back to a constant power supply is somewhat tricky. Also, air heats up when compressed, and absorbs heat when expanded, so in order to get a decent round-trip efficiency you need to store this heat as well as the compressed air. 


For small-scale storage applications, portable CAES modules exist. Lightsail has developed a 750 kWh CAES storage module, the size of a shipping container.[^lightsail] In theory, compressed air can be used to store energy on a power-plant scale, but no installation yet exists at this scale. Currently there are three large CAES-installations in operation world-wide.[^caesexamples] The newest one, commissioned in 2012, can store up to 500 MWh (0.5 GWh) of electricity, and can deliver 2 MW of power — a mere treacle compared to even a modest 500 MW coal power station. All three large CAES installations store the compressed air in disused salt mines. This is a lot cheaper and safer than building a storage unit above ground, and it takes less space. Of course the number of disused mines is fairly limited, but some projects are looking into storing compressed air in aquifers, disused oil- and gas-fields, and even in large "bags" on the ocean floor.[^caesexperiments] A lot of work still needs to be done to scale up this technology to the level of pumped hydro storage, and country-scale CAES will probably never be feasible. But with regard to energy density and round-trip efficiency, CAES is roughly comparable to lead-acid batteries. And for large-scale energy storage it can probably be much cheaper than batteries (although currently, it isn't).


### Hype or hope?

There are a few more technologies for energy storage that I haven't mentioned. Fly-wheel storage is probably the least high-tech of all methods, but its capacity doesn't scale up very well. And then there's hydrogen. Despite much talk of the "hydrogen economy", this never seems to have materialised, apart from a few demonstration projects. There are many reasons for this, but most have to do with efficiency, infrastructure and costs. While hydrogen is fairly easy to produce and use, it has large conversion losses and may be hard to store and transport. Hydrogen is not an energy source, it's an energy carrier. Production of hydrogen gas from water (by electrolysis) is easy, but requires electricity and is only around 70% efficient. As with compressed air, large quantities of hydrogen can be stored under high pressure in tanks, or better, in underground caverns, with an efficiency of about 85% (or more, at lower pressure). Conversion of hydrogen back to electricity requires either fuel cells (see below) or combustion in a gas-powered generator. The most efficient hybrid fuel cells should be able to do this with around 70% efficiency, but most fuel cells on the market today have an efficiency below 50%. And even these are rather expensive. In total, the round-trip efficiency of hydrogen-based electricity storage is at best around 50%, but more commonly 20-40%. In other words, you commonly *lose* around 60-80% of your energy along the way. In the current best-case, you would still lose around half. Compared to the other storage options we've seen, this is pretty bad.

 - Note: the best-case assumes 73% efficiency of electrolysis, 95% efficient pressurised storage and 70% efficiency of a hybrid fuel cell, which would yield a 49% round-trip efficiency (0.73 × 0.95 × 0.70 = 0.485).

For most energy storage applications, hydrogen is less than ideal. For large-scale storage, compressed air is more efficient and probably cheaper. For smaller-scale storage, Lithium-ion batteries are definitely cheaper and a lot more efficient than hydrogen, and they have a higher energy density (at least by volume). So why look at hydrogen at all? Well, it turns out that hydrogen and fuel cells have some interesting additional applications.

Like a battery, a fuel cell is an electrochemical device that produces electricity. But unlike a battery, it does this by consuming fuel. 
You can think of a fuel cell as a very controlled form of combustion. As with combustion, at least part of the energy in the fuel is released as heat. In a traditional combustion-based electricity generator, the heat from burning fuel would first be converted to movement, and then to electricity. But a fuel cell can convert part of the energy from its fuel *directly* into electricity. Therefore is is more efficient than a combustion engine, up to about 60-70%. Unfortunately, being electrochemical cells, they also have many of the disadvantages that batteries have: they are expensive, have a limited life-span and are fairly sensitive to (chemical) damage. Moreover, like a combustion engine, fuel cells that process carbon-based (fossil) fuels such as natural gas will also produce CO~2~. But, at least in certain large-scale applications, the CO~2~ produced by fuel cells can be captured relatively easily (by cooling it to -40 degrees C, which does require some energy), after which in can be stored underground. Moreover, a certain kind of fuel cell, the Molten Carbonate Fuel Cell (MCFC), actually *requires* CO~2~ to operate. This quirk enables them to capture CO~2~ from the exhaust gases of industrial installations such as power plants, whicle *producing* electricity from fuel. MCFSs are industrial devices that operate at high temperatures, but their efficiency can approach 60% and they can process a large range of fuels, including hydrogen, methane and (in principle) even liquid fuels such as methanol and ethanol.

In other words, certain fuel cells can provide an efficient method to capture carbon from coal- and gas-powered power plants. Great, I hear you think, but what does this have to do with energy storage? Well, of course surplus electricity (e.g. solar energy during the day) can be used to generate hydrogen gas, which can be stored for short periods of time, or can be fed into gas distribution networks. When demand is high (e.g. in the evening), the hydrogen generated earlier would contribute to running gas-powered generators and/or fuel cells. We've already seen that this is not the most efficient form of energy storage, but it has one big advantage: Such short-term energy storage using hydrogen requires very little modification of existing energy infrastructure, especially in regions that already have a large storage- and distribution-network for natural gas.

We've seen that hydrogen is not a very good option for long-term energy storage. But it is actually possible to chemically combine hydrogen gas with CO~2~, again from the exhaust of fossil-based power plants. This process is based on the so-called Sabatier reaction, and it can be used to produce, among other things, methane and methanol. Methane is the main ingredient of natural gas, and because it has a higher energy density and is less reactive than hydrogen gas, it is somewhat easier to store and transport. Methanol is a liquid fuel (basically a toxic variant of alcohol), which can relatively easily be stored for longer periods. This could open up the possibility of seasonal energy storage, whereby an energy surplus in summer can be stored and used in winter.

Carbon capture techniques using fuel cells or the Sabatier reaction are promising but still experimental, and not ready for large-scale deployment. 

 - TODO: name pilot projects and their capacities

The main advantage of these techniques is that they do not require gigantic up-front investments in new infrastructure. They can be added incrementally to existing power plants, and can use existing infrastructure for energy storage and distribution. Modifying existing plants and technology would enable a gradual energy transition. Carbon capture and energy storage would be slowly scaled up, allowing contribution of renewable energy to increase while reducing the CO~2~ emission of existing energy sources. Power plants could grow into highly integrated energy generation and storage systems. Moreover, their efficiency and capacity would increase by adding fuel cells, while their emissions would decrease, as MCFCs don't just capture CO~2~ but also seem to capture and break down nitrogen compounds as a side-effect.



Notes: storing hydrogen for transport is problematic
 - Hydrogen is not a fuel but an energy carrier.
 - It's a small molecule and highly reactive 
 - Hard to store because of low volume density, generally stored at high pressure or at low temperatures, both of which require energy and material.
   - High-pressure storage is the most common
   - Liquification isn't practical, requires cooling down to -253 degrees, is only ~60% efficient and requires energy to maintain.
   - Both require further energy for long-term storage.
   - Solid state storage
 - Hard and expensive to transport due to low energy density, safety issues and interaction with other materials.




### Scaling up, scaling down

 - Been using Musk's example, assuming the goal is replacing fossil with solar PV and wind and focusing on country-scale storage.
 - It's naive to take this literally. The future will be a diverse mix of energy sources, both central and decentral.
 - The last example suggests that central, industrial-scale energy infrastructure may remain important, if only to provide a large-scale energy buffer in seasonal climates (where batteries won't help).
 - But that doesn't mean that we should focus solely on large-scale infrastructure. There is much to win by also focusing on decentral energy production, storage and demand.
 - Matching supply and demand is one issue, which will require both reducing demand (efficiency), shifting demand (smart grids) and providing energy storage for the demand that cannot be shifted (nights and winters).
 - Decentralisation and energy conversion will play a more important role. 
 - The current energy infrastructure is an extremely centralised and segregated infrastructure (gas and electricity). It is efficient, but not very flexible.
 - Electricity is easy to transport, and very versatile, but hard to store. 
 - Gas (be it hydrogen, natural gas, biogas) and liquid fuel (oil-based, bio-ethanol, methanol) is harder to transport and less versatile, but easier to store (except perhaps hydrogen).
 - Heat is hard to transport over long distance, and the least versatile, but by far the easiest to store.
 - We now use liquids for transport, gas for heating and electricity as multi-purpose source, but the roles will become less separated and will blend. One reason is that heat is produced as byproduct of nearly everything we do, and is easy to store. So why waste valueable gas in producing it?
 - Examples of combined electricity and heat production (micro-CHP/WKK, solar).
 - Heat can be used for cooling and heating, heat pumps are becoming common and heat buffers are fairly easy to build. There's enormous potential for reducing energy use for heating and cooling, and heat engines can be fed with pre-heated air/fuel/water.
 - Only generating significant electricity out of heat is tricky. Efficiency of thermoelectric is too low. We need flexible heat/cold infrastructures in homes and offices.


### The role of Tesla

It is unlikely that the main role of Tesla Energy will be to provide battery power storage on the scale of entire countries, no matter how trivial Elon Musk may make this sound. No doubt it would be a lucrative contract for Tesla, but as we've seen, reliable and durable energy storage on that scale is a hard problem that requires a significant investment. A problem like that is best solved with a mix of approaches and technologies. Certainly, Tesla's Li-ion batteries may play a role, as will expansion of pumped storage and use of other battery technologies such as redox flow[^redoxflow], and development of fuel-cell technologies.

But for individuals and organisations, there is no need to wait for large-scale grid-based energy storage. If you want to contribute to the sustainable energy transition without relying (too much) on fossil-powered backup electricity from the grid, there is no reason why you cannot install solar panels and batteries at the scale of households or office buildings. And this is where Tesla's batteries can make a big contribution.

Household-scale battery storage is not exactly a new idea. 
 - Show some lead-acid examples, pictures and cost of lead-acid and Li-ion storage systems (name some companies). 
 - Lead-acid batteries are cumbersome: flooded batteries require regular equalization and topping-off with water, have a limited number of deep cycles (500-1000 typically), do not tolerate extended periods at low charge, etc. Plus they are heavy and big, often weighing over a tonne.
 - Other alternatives such as iron-phosphate, durable but also have many problems. Anything but an "appliance".

Up until a few years ago, affordable battery storage generally required a room full of lead-acid batteries. Because the life-span of batteries quickly decreases with the depth of discharge (DoD), you usually need to install much more battery capacity than you will actually need on a day-to-day basis. Li-ion batteries may be more expensive than lead-acid, they also last longer and take up much less space. Compared to alternative systems, Tesla's batteries are small, fairly durable, look attractive and are relatively affordable due to their projected large-scale production. 

In other words, while Tesla Energy is not the first to offer a home-scale electricity storage solution, they certainly have better PR and more attractive pricing than most alternative solutions currently on the market. But a more important point is perhaps this: Tesla is the first company to offer and market battery storage not as a custom niche-market solution, but rather as a mass-produced consumer appliance that should "just work".[^customsolution] 

In a technical sense, Tesla's Powerwall is not a revolutionary product. It is proven technology, just nicely packaged and fitted with smart software and some other tricks to extend the inherently limited life-span of its Li-ion cells.[^teslatricks] But this is excatly the thing that Tesla does right: using and scaling up existing technologies, thereby making it more widely available to consumers and organisations, instead of waiting around for some technological breakthrough that may or may not happen soon. It is the same strategy they use with their electric verhicles: make them attractive for people who can afford them, and then gradually bring down costs. (And incidentally, Tesla's and other electric cars are excellent small-scale electricity storage devices!) 
There are no doubt many people and companies that can afford the luxury of battery storage, or even going off-grid completely. The well-off early adopters of electric and hybrid cars may well be the same people who will want a fancy sleek power-storage device on their walls. As I wrote before, revolutions have to start somewhere, and this seems a good place to start. And this is a point that is generally missed by people who merely complain that solar power with Powerwall-storage currently tends to be more expensive than grid power.

 - Somewhere, mention durability tricks (12kWh, cooling, charging), special inverters needed and max. power output. These latter things will increase cost and EROI. 
 - Tesla's vehicles and other EVs can also be used as storage. Experiments being done.


### But is it sustainable?

 - If solar + battery replaces fossil demand, yes. Mostly the battery will only make a difference if it makes solar worthwile where it wasn't before, e.g. in absence of grid-metering or when replacing a generator in off-grid systems. 
 - May help less coal/gas plants to be built for backup, but only if solar + storage is introduced at very large-scale (doesn't seem likely yet).
 - Energy needed to produce panels + battery, EROI, time needed to be energy-neutral. 
 - Often used argument: Lithium is toxic and will run out. Bit of an odd argument, as this goes for a lot of resources, including oil. Recycling will reduce all of the above problems, is possible and already done for lead-acid. Certainly, lithium may run out at some point, but not yet by far, and Lithium-ion isn't the only technology.
 - Biggest challenges: Life span needs to go up, production energy cost and carbon need to go down.


### Wrap-up

 - We've gotten used to a lot of energy.
 - Of course energy transition will be slow, messy, expensive. It is also inevitable.
 - Don't put eggs in one basket. We need a mix of technologies, each with its strong and weak points.
 - This time we don't have the benefits of the fossil energy transition: pre-packaged energy almost for free. But we will get more energy democracy, and in the end a more flexible infrastructure. Mix of central and decentral. Some long-term storage and long-distance transport needed to overcome winter in case of solar.
 - Fuel-cell development (integrated generation/storage system) and more battery development needed.
 - Also, more investment in energy conversion, cogeneration and using/storing "waste" heat. we still waste most of our high-grade energy (fossil and electrical) by turning it into heat! (And most of that escapes.)
 - But don't stand around waiting for new technologies. Solar + storage is not affordable, off-grid or on-grid. And think long-term, fossil energy will become more expensive in the long run, if only because the increasing EROI.
 - The future is now. It already makes sense to electrify your home, office and transport, to use solar energy and installing heat buffers and batteries. And as fossil-derived energy will have to become more expensive, it will only make more sense in the future.
 


Interested in reading more articles like this? Follow us [on Facebook](https://www.facebook.com/sustainsubstance), or through our [Atom-feed](/feeds/all.atom.xml).



-----

### Notes:


[^tesladiscussion]:
*Some hail it as the next step in the sustainable energy revolution, while others are more sceptical, pointing out the technical limitations and hidden costs of the system.*   
Most online-discussions I have seen on Tesla batteries, have focused mainly on the costs of the batteries and the entire system, vs. the cost of more traditional power sources. 


[^kWh]:
*... battery solution that "just works". It comes in two versions, a 7 kW·h model designed for daily charging and discharging, and a 10 kW·h model designed for occasional use as backup power supply. Up to nine batteries can be combined, for storage up to 90 kW·h. And for industrial use, Tesla introduced the Powerpack, which comes in 100 kW·h units that are infinitely scalable.*   
The kilowatt-hour (kW·h, but often written as kWh) is a unit mostly used to express electricity-use and -storage. A kilowatt-hour is the amount of energy consumed in an hour, by a device that constantly draws 1000 Watt of power. In SI-units this is 3.6 MJ (megajoule). However, following author [David MacKay](http://www.withouthotair.com), I prefer to use kW·h as the unit for energy, rather than MJ or something else, because people tend to be more familiar with it (e.g. from their electricity bill).


[^evhistory:]:
*Why did electric cars disappear for almost a century, and why is it now taking so long for electric driving to really take off? The answer lies mainly in energy storage.*  
Electric vehicles (EVs) were the dominant type of cars in the early decades on the 20th century. As long as the roads were generally not very suitable for cars, the practical maximum speed of a car was very limited. Early EVs had a range of around [...] km, which was sufficient in most cases. Apart from their smaller range, EVs were considered superior to gasoline-powered cars, being less noisy, safer and much easier to get running. However, the advent of better roads, electric starters and other technological improvements and the introduction of the relatively cheap Model-T Ford, gradually made gasoline-powered cars a more attractive option. Moreover, the booming oil industry in the US played an important role in dismantling public transport and promoting gasoline-powered cars and busses over EVs, trams and trains. 
TODO: add figures and sources.


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

[^musksquare]:
*... the area shown is roughly a 100 km x 100 km square in North-West Texas. Filled with solar panels, this could generate around 500 GW of electric power, indeed more than the current mean US electricity demand of 425 GW.*   
Andrew ZP Smith checked the statement of Musk on the UCL Energy Blog, the figures above are based on [his estimate](http://blogs.ucl.ac.uk/energy/2015/05/21/fact-checking-elon-musks-blue-square-how-much-solar-to-power-the-us/).
Of course, literally placing all the solar panels in a 100,000 km2 square would be a silly idea. Rather, the panels would be distributed over the country, and would mostly be on roofs. And of course, this would somewhat increase the panel area needed, to compensate for the fact that you have less sun up north.


[^squarebatt]:
*On an average day, the entire US uses over 10 billion kW·h of electricity (10.2 TW·h). Storing this amount of energy would require a little over 102 million Tesla PowerPack batteries. You'd probably need a bit more storage than that to cover bad days and peak loads. Indeed, Musk himself estimates that around 160 million PowerPacks would be needed. It's by no means impossible to install that much capacity, but the batteries alone would cost around 4 trillion dollars, and producing them would require close to 20% of the world's known lithium-reserves.*   
According to the EIA, [total US electricity sales in 2013](http://www.eia.gov/electricity/annual/html/epa_01_02.html) were 3725 TW·h, which comes down to 10205 GW·h per day on average. A Tesla PowerPack battery stores 100 kW·h (= 0.0001 GW·h), and costs $25000. Producing a Li-ion battery [requires 0.17-0.28 kg lithium per kW·h of storage, depending on the battery type](http://seekingalpha.com/article/654441-ev-myths-and-realities-part-1-the-battery-crisis). Using the upper boundary, we would need 2.86 Mt of lithium to produce 10205 GW·h of battery capacity, or 4.48 Mt for 160 million PowerPacks. We take 23.6 Mt as a best estimate of the known lithium reserves ([Mohr et al. 2012](http://dx.doi.org/10.3390/min2010065)).

[^ustotalenergy]:
Comparing the total US energy use (48 TWh per day if we would switch everything to electricity) to the current electricity use (10.2 TW·h per day), total energy use is a factor 4.7 higher.

[^roundtrip]:
*the round-trip efficiency of modern systems is around 80%, which is actually pretty good.*   
The round-trip efficiency is a measure of how much of your original energy is left after having stored it. A round-trip efficiency of 80% means that of the original 100% of energy you put in, you lose 20% in conversion and storage, and you're left with 80%. Battery storage tends to be quite efficient, with round-trip efficiencies over 80% for lead-acid systems and over 90% for lithium-ion batteries. Hydrogen-based electricity storage tends to be rather inefficient, with round-trip efficiencies being between 20-50%, which means that 50-80% of the electricity is lost after storage. This "lost energy" isn't literally gone, of course. It just is no longer available in the form of electricity. In the conversion processes involved in storage, the "lost electricity" has been converted into heat. In some cases, this heat can be put to good use, increasing the overall usable energy (or thermal) efficiency of the storage. However, when I talk about round-trip efficiency in this article, I specifically mean electrical efficiency.


[^germanpowerstats]:
*But it's not nearly enough to cover the German electricity demand, which amounts to roughly 1.6 TW·h on an average day, with demand fluctuating between lulls as low as 32 GW in summer, to peaks over 90 GW in winter. In fact, it's not even sufficient to cover the contribution of solar PV in Germany, which currently has a production capacity of around 38.5 GWp (gigawatt-peak, the power output under optimal laboratory conditions).*   
TODO: sources


[^pumpedenergy]:
*Storing the amount of energy in a normal AA-battery (3 W·h), would require hoisting 360 litres of water (roughly 2.5 filled bathtubs) up to a height of 3 metres, or 100 litres to a height of 10 metres. And that's just the energy in one small battery. Storing the energy in a litre of gasoline or a 10 kW·h PowerWall would require lifting our 100 litres to a height of 36 km, or perhaps more practical, lifting 360 m^3^ of water (e.g. a swimming pool of 25×10×1.44 m, weighing 360 tonnes) to a height of 10 m! Matching the capacity of the 100 kW·h PowerPack would require roughly an olympic swimming pool (50×25×2.88 m, containing 3.6 Mt water) lifted to 10 metres height.*   
TODO: explain the calculations:
   - m*g*h, where g = 10 m/s/s, h is in m, m is in kg, and the result is in Joule (force F = m*a in N over a distance h in m), and assuming that 1 L = 1 kg.
 - calculate for 10m, also compare with 1 L gasoline, 7 kWh PowerWall, and 100 kWh PowerPack.
   - "For example, to get the amount of energy stored in a single AA battery, we would have to lift 100 kg (220 lb) 10 m (33 ft) to match it. To match the energy contained in a gallon of gasoline, we would have to lift 13 tons of water (3500 gallons) one kilometer high (3,280 feet). - See more at: http://physics.ucsd.edu/do-the-math/2011/11/pump-up-the-storage/#sthash.J7yQcRpw.dpuf"
   - 10 kWh = 36 000 000 J, gives 100 L at 36 km height, or 360 tonnes (360 m3) at 10 m. 100 kWh would be 3600m3 at 10 m, or a basin 40x30x3m, or 50x25x2.88m (roughly an olympic swimming pool).


[^caeshistory]:
*In fact, the second most important storage method is Compressed Air Energy Storage, or CAES. This has been around since the late 19th century, when compressed air was distributed over cities with pipes, and was used to power machines directly.*   


[^lightsail]:
*Lightsail has developed a 750 kWh CAES storage module, the size of a shipping container.*   

[^caesexamples]:
*Currently there are three large CAES-installations in operation world-wide.*   

[^caesexperiments]:
*some projects are looking into storing compressed air in aquifers, disused oil- and gas-fields, and even in large "bags" on the ocean floor.*   



[^redoxflow]:
*It is unlikely that the main role of Tesla Energy will be to provide battery power storage on the scale of entire countries, [...] A problem like that is best solved with a mix of approaches and technologies. Certainly, Tesla's Li-ion batteries may play a role, as will expansion of pumped storage and use of other battery technologies such as redox flow.*   

[^customsolution]:
*But a more important point is perhaps this: Tesla is the first company to offer and market battery storage not as a custom niche-market solution, but rather as a mass-produced consumer appliance that should "just work".*   
Of course, a PV-installation with battery storage *is* actually a highly customised product. There is no "one size fits all" solution, because every location is different in terms of latitude, orientation, weather patterns, construction, electrical installation and electricity use. You will always need someone with specialised knowledge to design and install the system. But this is not the point. Tesla's batteries will allow battery storage to be offered as a regular and fairly affordable option with new (and existing) PV-installations, rather than as a costly solution only to be applied in special cases.

[^teslatricks]:
*In a technical sense, Tesla's Powerwall is not a revolutionary product. It is proven technology, just nicely packaged and fitted with smart software and some other tricks to extend the inherently limited life-span of its Li-ion cells.*   


