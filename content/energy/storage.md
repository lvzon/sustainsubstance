Title: Energy storage and the Tesla battery
Authors: Levien van Zon
Date: 2015-06-03
Modified: 2015-10-18
Tags: energy
Slug: storage
Status: draft

**By Levien van Zon**

*This is an in-depth background article, with a reading time of more than 15 minutes. The footnotes provide additional background information, and can safely be skipped or read separately.*

Last April, Tesla's Elon Musk [announced](https://www.youtube.com/watch?v=yKORsrlN-2k) a new product for energy storage, the [Tesla PowerWall](http://www.teslamotors.com/powerwall). The announcement of this battery range, which should begin shipping in the coming month or so, generated a lot of attention. Some hail it as the next disruptive technological step in the sustainable energy revolution. Others are more skeptical, pointing out the technical limitations and hidden costs of the system[^tesladiscussion]. Such discussions aside for a moment, I think it's good to take a step back and look at what all the fuss is about. The first question to ask would be this: What problem is Tesla Energy trying to solve with its new battery products? 

As Elon Musk explains in his [keynote speech](https://www.youtube.com/watch?v=yKORsrlN-2k): *"We have this handy fusion reactor in the sky, the sun,"* which *"produces ridiculous amounts of power."* However, "*the obvious problem with solar power is that the sun does not shine at night.*" So, if we want solar energy to replace the electricity generated from fossil fuels, we need some way of storing the power generated during the day, so we can use it any time we need it. This may sound trivial: After all we have batteries, right? True, but *"the issue with existing batteries, is that they suck."* They are large, expensive, have a short life span and are hard to integrate with existing infrastructure. That's where the PowerWall comes in. It's designed to be an attractive, scalable and relatively cheap battery solution that "just works". It comes in two versions, a 7 kW·h model[^kWh] designed for daily charging and discharging, and a 10 kW·h model designed for occasional use as a backup power supply. Up to nine batteries can be combined, for storage up to 90 kW·h. And for use on a more industrial scale, Tesla introduced the PowerPack, which comes in 100 kW·h units that are infinitely scalable. Moreover, addressing the problem of short life span, Tesla offers a 10-year warranty on the PowerWall.

![A PowerWall battery unit on the left, and Elon Musk showcasing a PowerPack unit on the right]({filename}/images/storage/2015-powerwall-musk-powerpack.jpg)   
*A PowerWall battery unit on the left, and Elon Musk showcasing a PowerPack unit on the right.*

In short, the PowerWall promises to be the iPhone of energy storage solutions, solving the problem of solar energy availability in a fairly elegant way. Moreover, it promises to offer a sustainable option for going "off-grid", at a fraction of the cost of comparable alternatives. Does that sound too good to be true? Well, to some extent it is.


### The problem with batteries

Batteries are hardly a new technology. The first "modern" electrochemical battery was built over two centuries ago by Alessandro Volta, and in fact the principle hasn't really changed since then. The first rechargeable battery, a lead-acid battery, was invented in 1859 by Gaston Planté. This type of battery is still widely used in cars today.[^batteryhistory] The first electric car was built almost two centuries ago, in the 1830's, and by the start of the 20th century electric vehicles with rechargeable batteries were commonplace. In fact, when it comes to driving a car, an electric motor is superior to a combustion engine in almost every way. It's simpler, cleaner, less noisy, and *much* more efficient. So what happened? Why did electric cars disappear for almost a century, and why is it now taking so long for electric driving to really take off again? The answer lies mainly in energy storage.[^evhistory]

![]({filename}/images/storage/1881-battery-1902-baker.png)   
*On the left, a flooded lead-acid battery from the 1880's ([source](https://nationalmaglab.org/education/magnet-academy/history-of-electricity-magnetism/museum/plante-battery))*.
*On the right, a 1909 advert for the Baker Electric Roadster, which could drive 100 miles (160 km) on a single charge ([advert source](http://chuckstoyland.com/national/electric/baker)). In 1909, Emil Gruenfeldt of the Baker Motor Vehicle Company covered 160.8 miles (259 km) on a single charge in his Baker Electric Roadster. Two years later, he beat his earlier mark by travelling 201.6 miles (324 km) without recharging the batteries (source: [David Kirsch](http://www.amazon.com/gp/product/0813528097?ie=UTF8&tag=lowtemagaz-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0813528097), as quoted in [Lowtech Magazine](http://www.lowtechmagazine.com/overview-of-early-electric-cars.html)).*


The internal combustion engine is a ridiculously complicated way of converting fuel into movement. Moreover, it's hopelessly inefficient, with even modern designs wasting around 75% of their input energy as heat. But it has one important advantage: fossil fuels have an extremely high energy density. The energy density is a measure of how much energy is packed in a given volume or weight.[^energydensity] Burning 1 kg of gasoline or diesel yields around 13 kW·h of energy, which is more than most houses use in a day. By comparison, 1 kg of modern lithium-ion battery can store somewhere between 0.1 and 0.3 kW·h of energy. And that does not even take into account the weight of the battery casing and electronics. Lead-acid batteries are even worse, with 1 kg of battery holding only around 0.04 kW·h of energy. In other words, an amount of fossil fuel with the same weight as a modern battery, will contain 50 to 100 times as much energy. This leads to the strange situation that an average gasoline-powered SUV can easily outperform an electric car when it comes to its action radius. Even though the SUV actually wastes *over 99% of the energy* in its fuel in producing heat, overcoming friction and lugging around at least 1500 kg of steel. It can afford such terrible inefficiency because its fuel contains so much energy! A car like that drives roughly 10 km on a litre of gasoline[^volumedistance], which contains roughly 10 kW·h of energy. Another way of saying this, is that a 10 kW·h PowerWall battery pack (which currently costs $3500) can hold the same amount of energy as one litre of gasoline (which currently costs less than $2). Granted, electrical cars are more efficient in their use of energy than cars with a combustion engine. But from an economical and practical perspective, it's hard to compete with oil when it comes to powering transport.


Apart from their relatively low energy density and relatively high cost, there is another problem with batteries. Most batteries are electrochemical devices, which is to say they store electric energy in a chemical form. Charging a battery adds electrons to positively charged particles (cations) inside the battery. Discharging it removes electrons from negatively charged particles (anions) in the battery. Such chemical reactions, known as *redox reactions*, result in a flow of electrons that we call an electrical current, and which we can use to power our electrical devices. However, during each charge and discharge, the internal chemical state of a battery changes a little bit, negatively influencing its operation in the long term. Moreover, as the speed of a chemical reaction depends on temperature, so does the operation of a battery. Low temperatures decrease a battery's charge and output current, and high temperatures increase the rate at which internal damage accumulates. In other words, a battery won't work well when it's cold. And it has a limited life span, which rapidly decreases with heavy use and high temperatures.


![](http://www.volcanoecigs.com/media/wysiwyg/How_Battery_Works.gif)   
Sources: <http://www.mpoweruk.com/chemistries.htm>   
<http://www.mpoweruk.com/graphics/battery.swf>   
See also: http://sustainablenano.files.wordpress.com/2013/10/lithium-ion-battery-powering-device.png   
Source: <http://sustainable-nano.com/2013/10/15/how-do-lithium-ion-batteries-work/>


The lithium-ion batteries in your average smart-phone or laptop typically only last a few (roughly 2-5) years under normal, daily use. For comparison, other electronic components typically have an operational life span of 10-30 years. In modern portable devices, the battery is clearly the weakest link. In an electrical car however, the battery is also the single most expensive component, so a life span of only a few years would be unacceptable. This is why the makers of electric cars have resorted to a number of measures that increase the life span of their batteries. They select battery types that favour durability over maximising energy density. They add thermal management systems that keep the battery at optimal operating temperatures. And they use software to monitor and manage battery discharge, making sure that the battery is only partially discharged, increasing its life span at the cost of usable capacity.[^dodlifespan]



### Grid issues

So, energy storage is important for mobile and portable devices. But the life span of portable electronic devices is often limited by the short life span of their batteries. It is a good thing then, that most devices that need electricity are stationary. Think of heating and cooling and cooking equipment, lights, televisions, desktop computers and battery chargers. We plug them in, and they continue to work until we turn them off, or until they break. Their power source doesn't run out, wear out or weigh down the device. Instead, the energy they need is generated, usually from coal or gas, in very large power plants[^plantefficiency], and then transported to our house through a fairly efficient network of cables and transformers, better known as the electricity grid.


The electricity grid is quite an amazing and often underrated piece of human engineering. But what many people don't realise is that it cannot magically store electricity. Quite the contrary: in order for the electricity grid to function, energy supply and demand have to be *almost perfectly balanced at all times*.[^gridbalance] If the demand for electricity falls, power plants have to be physically throttled back or taken offline. If energy demand rises, supply is increased, where possible by increasing power plant output, or by bringing extra plants online.[^plantthrottle] But if this cannot be done fast enough, industrial-scale electricity users such as aluminium smelters are under contract with grid operators to automatically cut back their power use for short periods of time.


Advocates of sustainable energy often claim that we can get rid of fossil fuels, simply by installing sufficient windmills and solar PV-panels, which are hooked up to the grid. Because supply and demand always need to be balanced, it is true that a supply of electricity generated from solar and wind will at any given moment reduce the fraction of fossil-fuel powered electricity on the grid. To compensate for the renewable energy supply, especially gas-fired plants will be throttled back or powered down. But as soon as the renewable electricity supply is reduced by cloudy weather, lack of wind or nightfall, these same power plants will have to be fired back up to compensate for the reduced supply of renewable electricity.


The important point here is that, while adding wind and solar power to the grid may *reduce* the use of fossil fuels on a daily or yearly basis, they still require a full fossil-powered energy infrastructure to be built and maintained. This infrastructure is needed to provide an equivalent power-generating capacity during, say, windless nights, or winter. This double investment in infrastructure greatly increases the costs of "greening" the electricity supply. Moreover, our electricity consumption has only been increasing, and will continue to increase as we gradually electrify the world's transport and heating systems. While using an electric vehicle may reduce your consumption of oil, it easily has the potential to double or triple your electricity consumption.[^EVload]

 - TODO: check figures and show graph of per capita electricity consumption in several countries


What all this means that electricity derived from solar and wind currently cannot replace fossil-powered energy plants, nor prevent new ones from being built. Our continued *dependence* on fossil fuels, combined with their attractively low costs, doesn't provide any incentive to actually *switch* to alternative sources of energy. After all, what's the point of switching if you need a full fossil-powered backup infrastructure that is actually cheaper to operate than the thing you'd want to switch to?


This is where energy storage comes in. Installing for instance solar PV on a large scale, tends to generate a surplus of energy on sunny days. If the surplus generated during the day could be stored, and used at night, there would be less need to keep fossil-powered power plants around as a backup. Of course, to make a real difference, such storage must be significant, it must be at the scale of power-plants. And also, you need to have sufficient surplus energy on an average day to recharge your storage, even in winter.


### Storing the grid?

How much power does a typical power plant generate? It depends very much on the plant, but a typical coal-fired plant in the US can generate around 500 million watts (500 MW).[^watts] New plants tend to have a larger capacity, up to 3000 or even 5000 MW, especially in countries like China, where power generating capacity is being expanded at an almost unbelievable rate. A 500 MW power plant can generate around 12 million kW·h (= 12 GW·h) of electricity in a day. To store that amount of energy you would need 120,000 of Tesla's PowerPack battery units, or over 1.7 *million* PowerWall batteries (the 7 kW·h model for daily use). And that's only for *one* fairly small power plant.


In the keynote speech where he introduced Tesla's batteries, Elon Musk showed how much land would be required to cover the entire US electricity demand with solar panels:


![The "tiny blue square"]({filename}/images/storage/2015-musk-bluesquare.png)   
*Elon Musk's "tiny blue square".*


On the scale of a country, it's not that much ([less than 1% of land area for the US](http://www.nrel.gov/docs/fy08osti/42463.pdf)). It's still a lot of land of course, the area shown by Musk is roughly a 100 km × 100 km square in North-West Texas. Filled with solar panels, this could generate around 500 GW of electric power on average, indeed more than the current mean US electricity demand of 425 GW.[^musksquare] On an average day, the entire US uses over 10 billion kW·h of electricity (10.2 TW·h). Storing this amount of energy would require a little over 102 million Tesla PowerPack battery units. You'd probably need a bit more storage than that, to cover bad days and peak loads. Indeed, Musk himself estimates that around 160 million PowerPacks would be needed. It is by no means impossible to produce and install that much capacity, Musk noted that around 100 million new cars and trucks are put on the market every year. But it won't be cheap: the batteries alone would cost around 4 trillion dollars, and producing them would require up to 20% of the world's currently known lithium-reserves.[^squarebatt]


If the above sounds impractical, the situation gets worse if you realise that *electricity use* is only a small fraction of actual *energy use*. The US uses around 3 TW of energy in total, or about 72 TW·h per day on average. In other words, the energy use is seven times the electricity use! In the US, most of this energy is used for transport. But remember that combustion engines are very inefficient. So say we switch everything to electricity, this would reduce heat losses, bringing the power demand down by roughly a third, to 2 TW, or 48 TW·h per day.

On his blog [Do the Math](http://physics.ucsd.edu/do-the-math/2011/08/nation-sized-battery/), Tom Murphy shows that using lead-acid batteries to store a week's worth of US energy demand would require 4.5 trillion kg (4536 Mt)[^weight] of lead, and would cost more than the annual US GDP. Even if we would reduce the storage capacity to just one day, we would still need more lead to build the batteries (648 Mt) than the world's known lead reserves (around 80 Mt). Using lithium-ion batteries we would fare a bit better. Extrapolating from Musk's estimate, we'd need around 753 million PowerPack batteries to cover total US energy use.[^ustotalenergy] This would require around 90% of the world's known lithium reserves.


Elon Musk furthermore states that with 900 million PowerPacks, we could transition the entire world *electricity* production to solar power. And with approximately 2 billion PowerPacks, we could transition all transport and heating as well. Obviously these are purely hypothetical figures. With current technology and known lithium reserves, it isn't possible to transition the entire US energy demand to solar power, let alone the global energy demand. But that doesn't mean you can't start somewhere, say with a somewhat more modest goal.


### Pump up the storage

When it comes to energy storage, we tend to be focused on chemical batteries. Actually there are simpler ways of storing energy, especially when it comes to storing large amounts. And the easiest method is actually already in wide use: When you have too much electricity, just pump water up to a lake somewhere in the hills. Then when you have too little electricity, you can let it flow back down through a turbine. This is called Pumped Hydro Storage (PHS). You will lose some energy in the process of course, but the round-trip efficiency[^roundtrip] of modern PHS systems is around 80%, which is actually pretty good.


According to a [study](https://www.hydropower.org/study-the-hydropower-sector%E2%80%99s-contribution-to-a-sustainable-and-prosperous-europe) done for the International Hydropower Association (IHA), the current hydro storage capacity in Europe is estimated to be over 220 TW·h. That's equivalent to over 2.2 billion PowerPack batteries, enough to cover nearly 25 days of average European consumption! And what's more, contrary to Li-ion batteries, hydro storage requires less resources to produce on a large scale and doesn't need replacing every 15-20 years or so. So that solves the energy storage problem, or does it?


Of course there's a catch. Or rather, there are two. First of all, the 220 TW·h figure includes the storage capacity of *all* European hydro-power basins. Only a small fraction of this is pumped storage. The rest is conventional hydro-power, which cannot actively be recharged but has to wait for rivers and rain to refill the basin. This may take months or years. A large country like Germany only has around 0.05 TW·h of actual pumped storage, which can deliver 6.8 GW (= 6800 MW) of power for a period of 6 to 8 hours. That's a lot of power, comparable to the output of two large coal-fired plants. But it's not nearly enough to cover the German electricity demand, which amounts to roughly 1.6 TW·h on an average day, with demand fluctuating between lulls as low as 32 GW in summer, to peaks over 90 GW in winter. In fact, it's not even sufficient to cover the contribution of solar PV in Germany, which currently has a production capacity of around 38.5 GWp (gigawatt-peak, the power output under optimal laboratory conditions).[^germanpowerstats]

![Electricity production and demand in Germany on December 4th 2014 and June 14th 2015.]({filename}/images/agora-20141204-20150614.png)

 - 20141204 at 12:00: 1.7 GW solar, 3 GW wind, 2 GW pumped storage, 0.4 seasonal storage, 11.2 gas, 37.4 GW coal, 12.3 GW nuclear, 5.9 biomass, 4.9 hydro, 0.2 other, -0.8 export
 - 20150614 at 12:00: 15.7 GW solar, 3.1 GW wind, 0.5 GW pumped storage, 0.1 seasonal storage, 1.9 gas, 15 GW coal, 9.2 GW nuclear, 4.8 biomass, 3.1 hydro, 0.3 other, -8 export
 - In winter, much higher consumption, much more coal and gas, solar is negligable, hydro-storage plays a role. In summer, much more solar and lower consumption so lower baseload-production, significant export of energy.
 - Sources: www.energy-charts.de and http://www.agora-energiewende.de/en/topics/-agothem-/Produkt/produkt/76/Agorameter/


The second catch is more serious. If the problem were merely one of capacity, you could just build more pumped storage plants. But this is not so easy, because in fact the energy density of pumped hydro storage is absolutely terrible. In practice, this means that adding pumped hydro storage capacity requires space, *a lot* of space. The principle of pumped hydro is that lifting a weight to a certain height requires energy in order to overcome gravity. In this case, the weight is provided by a volume of water. To give you an idea of the amount of energy versus the volume of water needed: Storing the amount of energy in a normal AA-battery (3 W·h), would require hoisting 360 litres of water (roughly 2.5 filled bathtubs) up to a height of 3 metres, or 100 litres to a height of 10 metres.[^volumedistance] And that's just the energy in one small battery. Storing the energy in a litre of gasoline or a 10 kW·h PowerWall would require lifting our 100 litres to a height of 36 km, or perhaps more practical, lifting 360 m^3^ of water (e.g. a swimming pool of 25×10×1.44 m, weighing 360 tonnes) to a height of 10 m! Matching the capacity of the 100 kW·h PowerPack would require roughly an olympic swimming pool (50×25×2.88 m, containing 3.6 Mt water) lifted to 10 metres height.[^pumpedenergy] You probably get the point, the dismal energy density of pumped storage will make even a lowly lead-acid battery look *great*.


To have a pumped storage plant with any significant capacity, you'll need a rather big lake on a hill, and another one at least equally big at the base of the hill. There's not many places where you will find this situation occurring naturally. And if you do, emptying and refilling the lakes on a regular basis is going to have a big impact on water life. Of course you can always *create* a large lake by building a dam in a valley, this is how we often construct hydro-power facilities. But while such projects may contribute to reducing greenhouse gas emissions, the local environmental destruction that results certainly does not qualify them as "environmentally friendly".


In short, large-scale hydro-storage isn't going to solve the energy storage problem. There simply isn't enough space. And even if there were enough space, building the required infrastructure would result in widespread environmental destruction. Of course electrochemical batteries and pumped hydro storage aren't the only large-scale energy storage options. In fact, the second most important storage method is Compressed Air Energy Storage, or CAES. This has been around since the late 19th century, when compressed air was distributed over cities with pipes, and was used to power machines directly.[^caeshistory] Modern CAES uses electricity to compress air, and turns the compressed air back into electricity when needed. This is a bit more complicated than pumped hydro storage. You need some kind of high-pressure container, and the pressure generally isn't constant, so converting it back to a constant power supply is somewhat tricky. Also, air heats up when compressed, and absorbs heat when expanded, so in order to get a decent round-trip efficiency you need to store this heat as well as the compressed air. 


For small-scale storage applications, portable CAES modules exist. Lightsail has developed a 750 kW·h CAES storage module, the size of a shipping container.[^lightsail] In theory, compressed air can be used to store energy on a power-plant scale, but no installation yet exists at this scale. Currently there are three large CAES-installations in operation world-wide.[^caesexamples] The newest one, commissioned in 2012, can store up to 500 MWh (0.5 GWh) of electricity, and can deliver 2 MW of power — a mere treacle compared to even a modest 500 MW coal power station. All three large CAES installations store the compressed air in disused salt mines. This is a lot cheaper and safer than building a storage unit above ground, and it takes less space. Of course the number of disused mines is fairly limited, but some projects are looking into storing compressed air in aquifers, disused oil- and gas-fields, and even in large "bags" on the ocean floor.[^caesexperiments] A lot of work still needs to be done to scale up this technology to the level of pumped hydro storage, and country-scale CAES will probably never be feasible. But with regard to energy density and round-trip efficiency, CAES is roughly comparable to lead-acid batteries. And for large-scale energy storage it can probably be much cheaper than batteries (although currently, it isn't).


### Hype or hope?

There are a few more technologies for energy storage that I haven't mentioned. Fly-wheel storage, for instance, is probably the least high-tech of all methods. But unfortunately its capacity doesn't scale up very well. And then there's hydrogen. Especially in the 1990s, grand visions were painted of a "hydrogen economy". Clean energy would be used to produce hydrogen, which would then serve as a fuel for our cars and planes. While we have seen a few demonstration projects, and some small-scale use of hydrogen, anything resembling a hydrogen economy failed to materialise. There are many reasons for this, but most have to do with efficiency, infrastructure and costs. While hydrogen is fairly easy to produce and use, it has large conversion losses and may be hard to store and transport. Hydrogen is not an energy source, it's an energy carrier. Production of hydrogen gas from water (by electrolysis) is easy, but requires electricity and is only around 70% efficient. As with compressed air, large quantities of hydrogen can be stored under high pressure in tanks, or better, in underground caverns, with an efficiency of about 85% (or more, at lower pressure). Conversion of hydrogen back to electricity requires either fuel cells (see below) or combustion in a gas-powered generator. The most efficient hybrid fuel cells should be able to do this with around 70% efficiency, but most fuel cells on the market today have an efficiency below 50%. And even these are rather expensive. In total, the round-trip efficiency of hydrogen-based electricity storage is at best around 50%, but more commonly 20-40%. In other words, you commonly *lose* around 60-80% of your energy along the way. In the current best-case, you would still lose around half.[^hydogenefficiency] Compared to the other storage options we've seen, this is pretty bad.


For most energy storage applications, hydrogen is less than ideal. For large-scale storage, compressed air is more efficient and probably cheaper. For smaller-scale storage, Lithium-ion batteries are definitely cheaper and a lot more efficient than hydrogen, and they have a higher energy density (at least by volume). So why look at hydrogen at all? Well, it turns out that hydrogen and fuel cells have some interesting additional applications.


Like a battery, a fuel cell is an electrochemical device that produces electricity. But unlike a battery, it does this by consuming fuel. 
You can think of a fuel cell as a very controlled form of combustion. As with combustion, part of the energy in the fuel is released as heat. In a traditional combustion-based electricity generator, *all* of the energy in the fuel is converted to heat. A small part of this heat is then converted to movement, usually rotating a magnet in a coil, which then generates electricity. But a fuel cell can convert part of the energy from its fuel *directly* into electricity. Therefore it is more efficient than a combustion engine, up to about 60-70%. Unfortunately, being electrochemical cells, fuel cells also have many of the disadvantages that batteries have: they are expensive, have a limited life-span and are fairly sensitive to (chemical) damage. Moreover, like a combustion engine, fuel cells that process carbon-based (fossil) fuels such as natural gas, will also produce CO~2~. But, at least in certain large-scale applications, the CO~2~ produced by fuel cells can be captured relatively easily (by cooling it to -40°C, which does require some energy), after which it can be stored underground. Moreover, a certain kind of fuel cell, the Molten Carbonate Fuel Cell (MCFC), actually *requires* CO~2~ to operate. This quirk enables it to capture CO~2~ from the exhaust gases of industrial installations such as power plants. Rather than decreasing the power output of a plant, as most carbon-capture techniques do, this would actually combine carbon capture with producing *additional* electricity from fuel. MCFSs are industrial devices that operate at high temperatures, but their efficiency can approach 60%, which is above usual power plant efficiency. Moreover, they can process a large range of fuels, including hydrogen, methane and (in principle) even liquid fuels such as methanol and ethanol.


In other words, certain fuel cells can provide an efficient method to capture carbon from coal- and gas-powered power plants. Great, I hear you think, but what does this have to do with energy storage? Well, of course surplus electricity (e.g. solar energy during the day) can be used to generate hydrogen gas, which can be stored for short periods of time, or can be fed into gas distribution networks. When demand is high (e.g. in the evening), the hydrogen generated earlier would contribute to running gas-powered generators and/or fuel cells. We've already seen that this is not the most efficient form of energy storage, but it has one big advantage: Such short-term energy storage using hydrogen requires very little modification of existing energy infrastructure, especially in regions that already have a large storage- and distribution-network for natural gas.


We've seen that hydrogen is not a very good option for long-term energy storage[^hydrogenproblems]. But it is actually possible to chemically combine hydrogen gas with CO~2~, again from the exhaust of fossil-based power plants. This process is based on the so-called *Sabatier reaction*, and it can be used to produce, among other things, methane and methanol.[^sabatier] Methane is the main ingredient of natural gas, and because it has a higher energy density and is less reactive than hydrogen gas, it is somewhat easier to store and transport. National gas distribution networks are actually excellent energy storage facilities, generally able to store more than a year's worth of a country's energy use. And the Sabatier reaction can also produce Methanol, a liquid fuel that is basically a toxic variant of alcohol. This can relatively easily be stored for longer periods. Long-term storage using methane or methanol produced from hydrogen and CO~2~ may not have a high efficiency, as storage goes. But it does offer something that batteries or pumped storage cannot: the possibility of seasonal-scale storage. This way, an energy surplus produced in summer by solar PV, can be stored and used in winter.


It is certainly an interesting option to combine coal-based based electricity production with carbon capture using fuel cells and/or the Sabatier reaction. It would be a win/win situation, drastically reducing the CO~2~-emissions of coal power plants without reducing their efficiency too much, and offering options for long-term storage of renewable energy. However, while the technology involved is already quite established, its application for this purpose and on this scale is still experimental.


The US-based company [Fuel Cell Energy](http://www.fuelcellenergy.com/advanced-technologies/carbon-capture/) offers a fuel-cell based carbon capture and power generation system, which has been tested under laboratory conditions. A field-pilot will probably commence next year, with installing a 2.8 MW industrial fuel-cell module at a coal power plant. The second stage of the pilot will probably involve 12 modules. However, to capture 90% of the emissions of a 500 MW coal power plant, you'd need to install over 140 fuel cell modules. These fuel cells would have a combined capacity of around 400 MW, almost doubling the power output from the coal plant.[^fuelcellplants]


Car-producer Audi has built a 6 MW plant in Werlte, Germany, which uses electricity to produce hydrogen. The hydrogen is then combined with CO~2~ into methane, which is fed into the gas distribution network. This plant has a conversion efficiency of around 54%, and produces around 42 MW·h worth of methane per day (although roughly half of that would probably be lost when converting it back to electricity).
Another large commercial facility is the [George Olah carbon dioxide recycling plant](http://www.carbonrecycling.is/index.php?option=com_content&view=article&id=14&Itemid=8&lang=en) in Grindavík, Iceland. This commercial plant uses 
around 5 MW of electricity from the 75 MW [Svartsengi Geothermal Power Station](http://www.hsorka.is/english/HSProduction/HSProductionSvartsengi.aspx) to produce hydrogen. The hydrogen is then combined with CO~2~ from the power station exhaust, to make methanol. The facility has a maximum production capacity of around 13700 L methanol per day (equivalent to roughly 59 MW·h of stored energy). The methanol is currently blended with gasoline and used as transportation fuel.[^sabatierplants]


[![The Audi power-to-gas plant in Germany, and the George Olah carbon dioxide recycling plant in Iceland]({filename}/images/storage/sabatier-plants-audi-olah.jpg)]({filename}/images/storage/sabatier-plants-audi-olah.jpg)   
*On the left, the 6 MW Audi power-to-gas plant in Werlte, Germany. On the right, the George Olah carbon dioxide recycling plant in Iceland, with the Svartsengi Geothermal Power Station in the background. (Click to enlarge.)*


The main advantage of these fuel-cell and Sabatier-based techniques is that they use existing technology, and do not require gigantic up-front investments in new infrastructure. They can be added incrementally to existing power plants, and can use existing infrastructure for energy storage and distribution. Modifying existing plants and technology would enable a gradual transition toward a sustainable, carbon-free energy supply. Carbon capture and energy storage would be slowly scaled up, allowing contribution of renewable energy to increase while reducing the CO~2~ emission of existing energy sources. Power plants could grow into highly integrated energy generation and storage systems. Moreover, their efficiency and capacity would increase by adding fuel cells, while their emissions would decrease, as MCFCs don't just capture CO~2~ but also seem to capture and break down nitrogen compounds as a side-effect.


### Scaling up, scaling down

So far, I've mostly been talking about techniques for centralised, grid-based energy storage. This fits well with the idea of large wind- and solar farms, and with Elon Musk's vision of entirely replacing fossil-generated electricity by PV and wind power. Of course it would be somewhat naive to take this vision literally. There are many practical reasons why 100 × 100 km PV farms, for instance, are a bad idea, if only because of maintenance, power transmission and the effects on local climate. Instead, the future will be powered by a diverse mix of energy sources, with both centralised and decentralised power generation. The possibilities of running coal plants with efficient carbon capture (and perhaps of new nuclear energy technologies such as thorium molten salt reactors), suggest that centralised industrial-scale energy infrastructure will probably remain important. Even if we would switch mostly switch to renewable energy sources, we would still need a large-scale energy buffer in seasonal climates. Solar PV with battery storage may get you through the night, but it will simply not get you through a Northern European, Canadian or Russian winter, especially not if you drive around in an electric car.

For example, if everyone were to switch now to all-electric cars, the average person in The Netherlands would use roughly 7 kW·h of electricity per day (just for home use and transport, so not counting the energy used outside the house or car). Using only solar energy, and without seasonal storage, the Dutch would need roughly 62 solar panels *per person* to still generate sufficient electricity in December. That's 137 PV-panels for an average household, covering an area of 226 m^2^. With long-term energy storage, this could be reduced to something like 17 PV-panels per person, or about 38 panels per household.[^NLEVPVexample] In either case, the average household will not have space for that many panels, so some kind of centralised infrastructure will be needed to generate electricity and store energy.


However, this does not mean that we should focus *solely* or even *mostly* on large-scale infrastructure. There is much to win by focusing also on decentral energy production, storage and control of demand. Even if the majority of people would remain dependent on grid-electricity, a decentral approach will be important to better match electricity supply and demand. A transition to sustainable energy will require reducing energy demand, mostly by increasing the efficiency of transport and heating. Matching energy demand and supply will require shifting the peak energy demand to mid-day, when most solar energy is available. And energy storage will be needed for demand that cannot be shifted, especially during nights and winters. And decentralisation and energy conversion will play an increasingly important role in all of this.

Our current energy infrastructure is extremely centralised and segregated. Electricity, gas and heat are mostly treated as separate energy sources, each with their own infrastructure, both on a large scale and within buildings. Electricity is relatively easy to transport over large distances, and it is very versatile, but as we've seen it's very hard to store. Gas (be it natural gas, biogas, hydrogen or synthetic methane) and liquid fuels (oil-derivatives and alcohols) are harder to transport and are less versatile than electricity. But with the possible exception of hydrogen, gaseous and liquid energy carriers are much easier to store in large amounts and for long periods of time. Heat is hard to transport over long distances, and is the least versatile form of energy, but when a heat pump is used, it is relatively easy and cheap to store. 
We currently tend to use liquid fuels to power our transport, gas for heating and electricity for all sorts of things. But these traditional roles of our energy carriers will probably become less clear and separated in the near future. One reason is that heat is produced as a by-product of nearly everything we do, and is fairly easy to store. Yet in Northern countries we use vast amounts of gas and electricity in our buildings, just to produce heat.

Making smarter use of heat is probably the single most important step we can take to reduce our dependence on fossil fuels. In cold climates, the first step would be to make it less easy for heat to escape our buildings.[^insulation] The second step would be to stop getting most of our heat from burning fossil fuels and biomass. Even in Northern winters it's still possible to get a significant amount of heat directly from sunlight, using passive building designs or thermal solar collectors. Additional heat can be extracted from the environment using a heat pump. Moreover, much better use can be made of waste heat from other processes, such as power generation.[^heatextraction] The third step in using heat more effectively, is to store it in a heat buffer for later use. A heat buffer can take the form of an underground water reservoir, a large mass of rock, or for shorter periods, even walls and floors.[^heatstorage]


 - This does not just apply to heating, but also to cooling: absorption chillers. And to hot water, running washing machines, pre-heating heat engines etc.
 - You can even make electricity out of heat, but the efficiency of thermoelectric is too low.
 - Much better is to combine power generation with heat collection. Combined solar thermal and PV is an attractive option if space is limited. 
 - While it generally still uses fossil fuels, micro-CHP is an efficient option: fuel cells are more efficient than generators, and the waste heat can be directly used for heating or cooling. Combining with solar and perhaps batteries would be a good option. But it's too expensive for most households (mostly used for companies and larger complexes). Also, lifespan is an issue. 



### The role of Tesla

It is unlikely that the main role of Tesla Energy will be to provide battery power storage on the scale of entire countries, no matter how trivial Elon Musk may make this sound. No doubt it would be a lucrative contract for Tesla, but as we've seen, reliable and durable energy storage on that scale is a hard problem that requires a significant investment. A problem like that is best solved with a mix of approaches and technologies. Certainly, Tesla's Li-ion batteries may play a role, as will expansion of pumped storage and use of other battery technologies such as redox flow[^redoxflow], and development of fuel-cell technologies.

But for individuals and organisations, there is no need to wait for large-scale grid-based energy storage. If you want to contribute to the sustainable energy transition without relying (too much) on fossil-powered backup electricity from the grid, there is no reason why you cannot install solar panels and batteries at the scale of households or office buildings. And this is where Tesla's batteries can make a big contribution.

Household-scale battery storage is not exactly a new idea. 

  - Already used for years for off-grid homes, especially in places where a connection to the grid is prohibitively expensive. 
  - Show some lead-acid examples, pictures and cost of lead-acid and Li-ion storage systems (name some companies). 
  - Lead-acid batteries are cumbersome: flooded batteries require regular equalization and topping-off with water, have a limited number of deep cycles (500-1000 typically), do not tolerate extended periods at low charge, etc. Plus they are heavy and big, often weighing over a tonne.
  - Other alternatives such as iron-phosphate, durable but also have many problems. Anything but an "appliance".

Up until a few years ago, affordable battery storage generally required a room full of lead-acid batteries. Because the life-span of batteries quickly decreases with the depth of discharge (DoD), you usually need to install much more battery capacity than you will actually need on a day-to-day basis. Li-ion batteries may be more expensive than lead-acid, they also last longer and take up much less space. Compared to alternative systems, Tesla's batteries are small, fairly durable, look attractive and are relatively affordable due to their projected large-scale production. 

 - In notes or in main text?
   - Mention durability tricks (12kW·h, cooling, charging).
   - However, special inverters needed and max. power output will increase cost and EROI. 

In other words, while Tesla Energy is not the first to offer a home-scale electricity storage solution, they certainly have better PR and more attractive pricing than most alternative solutions currently on the market. But a more important point is perhaps this: Tesla is the first company to offer and market battery storage not as a custom niche-market solution, but rather as a mass-produced consumer appliance that should "just work".[^customsolution] 


In a technical sense, Tesla's Powerwall is not a revolutionary product. It is proven technology, just nicely packaged and fitted with smart software and some other tricks to extend the inherently limited life-span of its Li-ion cells.[^teslatricks] But this is exactly the thing that Tesla does right: using and scaling up existing technologies, thereby making it more widely available to consumers and organisations, instead of waiting around for some technological breakthrough that may or may not happen soon. It is the same strategy they use with their electric vehicles: make them attractive for people who can afford them, and then gradually bring down costs. (And incidentally, Tesla's and other electric cars are excellent small-scale electricity storage devices!) 
There are no doubt many people and companies that can afford the luxury of battery storage, or even going off-grid completely. The well-off early adopters of electric and hybrid cars may well be the same people who will want a fancy sleek power-storage device on their walls. As I wrote before, revolutions have to start somewhere, and this seems a good place to start. And this is a point that is generally missed by people who merely complain that solar power with Powerwall-storage currently tends to be more expensive than grid power.

 - Notes: Tesla's vehicles and other EVs can also be used as storage. Experiments being done in Utrecht.
   - https://www.stedin.net/over-stedin/pers-en-media/persberichten/wereldprimeur-utrecht-laadpaal-maakt-opslag-zonneenergie-mogelijk
   - Mart van de Kam, UU
     - http://www.uu.nl/staff/MJvanderKam
     - http://dx.doi.org/10.1016/j.apenergy.2015.04.092
     - Dissertation should be in http://www.narcis.nl/search/coll/person/uquery/kam/Language/nl

### But is it sustainable?

 - If solar + battery replaces fossil demand, yes. Mostly the battery will only make a difference if it makes solar worthwile where it wasn't before, e.g. in absence of grid-metering or when replacing a generator in off-grid systems. 
 - May help less coal/gas plants to be built for backup, but only if solar + storage is introduced at very large-scale (doesn't seem likely yet). We probably need larger-scale storage techniques for that to happen.
 - Energy needed to produce panels + battery leads to energy payback time, time needed to be energy-neutral.
   - Li-ion requires ~500 kW·h per kW·h of capacity. A large part of this energy is utilized in mining scarce elements and achieving
the high temperatures required to make the electrode materials.
   - The Powerwall-cells (12 kW·h) require around 6000 kW·h (6 MWh) to produce. Maybe a bit less for modern production, but we also need to include electronics.
   - Mono-Si solar-panel takes ~1200 kW·h to produce, plus ~546 kW·h mounting, so say 1700 kW·h.
   - Ribbon-Si is closer to ~750 kW·h per panel, so ~1300 kW·h per panel.
   - A 265 Wp-panel in Spain generates ~338 kW·h per year, and in NL ~199 kW·h per year, with 0.75 performance ratio (TODO: check the calculation!).
   - So energy payback time for a mono-Si module is ~5 years in Spain, and >8 years in NL. Ribbon-Si is ~4 years in Spain and ~6.5 years in NL. More optimistic figures of 1.5 years assume ribbon-Si, production in Europe, using less primary energy, and excluding frame and mounting.
   - An installation of 20 panels would generate 6760 kW·h per year in Spain, and ~4000 kW·h in NL, per year. So after 4-6.5 years, an additional 1-1.5 years are needed to "pay back" the energy needed to produce a PowerWall or equivalent Li-ion battery.
 - Often used argument: Lithium is toxic and will run out. Bit of an odd argument, as this goes for a lot of resources, including oil. Lead-acid batteries are a lot more toxic. Recycling will reduce all of the above problems, is possible and already done for lead-acid. Certainly, lithium and other components (e.g. cobalt) may run out at some point, but not yet by far, and Lithium-ion isn't the only technology.Many alternatives exist, many more are being developed. See Larcher & Tarascon.
 - Biggest challenges: Life span needs to go up, production energy cost and carbon need to go down. This is certainly possible.


 - Sources: 
   - 1 MJ = 0.277778 kW·h
   - http://www.lowtechmagazine.com/2015/04/how-sustainable-is-pv-solar-power.html
   - http://www.sciencedirect.com/science/article/pii/S0038092X14001935
     - Energy Payback Time for PV modules ranged from 1.4 - 2.4 years, depending on type and where it was produced.
     - Cumulative primary energy demand is 2500-5000 MJ per module, or 694-1389 kW·h, say 1200 kW·h average
     - Uses data from 2004-2006, and assumes 1700 kW·h/(m3 yr), typical for southern europe
   - http://www.nrel.gov/docs/fy13osti/56487.pdf
   - http://www.lowtechmagazine.com/2015/05/sustainability-off-grid-solar-power.html
   - The making of 1 kW·h of lithium-ion battery storage requires 400 kW·h of energy.
   - Rydh & Sanden, 2004, http://dx.doi.org/10.1016/j.enconman.2004.10.004
     - Energy requirements for PV panel production in 2004: 32 MJ/Wp +/- 20% (8.89 kW·h/Wp), or 4200 MJ/m2 (1167 kW·h/m2)
     - For panel frames: 500 MJ/m2 (139 kW·h/m2)
     - Roof mounting: 700 MJ/m2 (194 kW·h/m2)
     - Total would be 1914 kW·h per panel, plus 228 kW·h for its frame and 318 kW·h for mounting, in total 2460 kW·h per panel.
     - For inverter, charger and AC: 1 MJ/W (278 kW·h/kW)
     - For Li-ion materials, virgin: 0.67 MJ/Wh (186 kW·h/kW·h)
     - For Li-ion materials, recycled: 0.31 MJ/Wh (86 kW·h/kW·h)
     - For battery production: 1.2 MJ/Wh (333 kW·h/kW·h)
     - Total: 519 kW·h/kW·h for new Li-ion batteries, or 419 kW·h/kW·h for recycled ones.
     - PbA does a bit worse for materials, but uses only about a third of energy for manufacturing (242 kW·h/kW·h recycled and 331 for new) 
   - Rydh & Sanden, 2004, http://dx.doi.org/10.1016/j.enconman.2004.10.004
     - Production and transportation of batteries contributes 24–70% to the total indirect energy use of the PV-battery system compared to 26–68% for the PV array (Fig. 6). Given a system lifetime of 30 years, the PV array contributes 1.8–3.3 yr and batteries 0.72–10 yr to the energy payback time depending on the technology. 
     - Efficiency of total PV-battery system is ca. 80% (including indirect energy costs for production). 
     - Energy return factor for Li-ion is 7.9, so the PV-battery system uses 8 times less fossil energy than a comparable Diesel generator would have done.
   - Report: EPA 744-R-12-001, April 24, 2013 (Application of Life-Cycle Assessment to Nanoscale Technology: Lithium-ion Batteries for Electric Vehicles), http://www2.epa.gov/sites/production/files/2014-01/documents/lithium_batteries_lca.pdf
     - Average primary energy use across the Li-ion battery chemistries totaled 1,780 MJ/kW·h of battery capacity (= 494 kW·h/kW·h).
   - D. Larcher & J-M. Tarascon, Towards greener and more sustainable batteries for electrical energy storage (2014), http://dx.doi.org/10.1038/nchem.2085
     - While such hydroelectricity is widely used, it stores just 3 Wh for every 1 m3 (ton) of water lifted by 1m.
     - early integrated LCA estimations 6–9 (for example, taking into account the
production of batteries, materials and recycling) have revealed that
more than 400  kW·h are needed to make a 1  kW·h Li-ion battery
(Fig. 2), resulting in the emission of about 75 kg of CO 2 — as much
as burning 35 l of gasoline. In comparison, the production of 1 kW·h
of electricity from coal produces around 1 kg of CO 2 (refs 10,11).
Despite the fact that the CO 2 generated by battery manufacturing
is undesirable, the associated energy cost is still a bigger concern.
In other words, under these conditions, batteries will only begin
to have an environmental benefit beyond hundreds of cycles.
Despite the very large discrepancy in reported LCA data regarding
the relative impacts of materials production versus cell assembly, it
is clear (Fig. 2) that ‘materials production’ is a main contributor to
CO 2 emissions and energy costs. It includes various aspects such as
mining, ore transport, ore treatment, and so on. In fact, a large part
of this energy is utilized in mining scarce elements and achieving
the high temperatures required to make the electrode materials 16,17 .
Consequently, the only viable path towards a ‘greener and more
sustainable’ battery is rooted in our ability to design electroactive
materials that have comparable performances to today’s electrodes,
but cost less energy and release less CO 2 during production.
Batteries have traditionally been considered to be potentially haz-
ardous to the environment due to the wide use of toxic lead, cad-
mium, mercury, and so on. Li-ion batteries do not contain any of
these materials but 3d metals such as nickel or cobalt are used in
most of them. Their use together with lithium is problematic due to
limited supply, their continuously increasing cost and the environ-
mentally questionable extraction methods. Furthermore, a wide-
spread use of Li-ion batteries for automotive or grid applications
will, over time, require that either the 3d metals (cobalt, nickel) are
partially substituted and/or that an efficient recovery or recycling
method for batteries is adopted. In today’s Li-ion batteries for port-
able electronics, cobalt and lithium contents range between about
5 and 15  wt% and 2 and 7  wt%, respectively 105 . Several hundred
thousand tons of batteries are sold annually; this constitutes an
‘urban mine’ for the recovery of thousands of tons of metal with
cost advantages over direct mining.

### Wrap-up

 - We've gotten used to a lot of energy.
 - Of course energy transition will be slow, messy, expensive. It is also inevitable.
 - Don't put eggs in one basket. We need a mix of technologies, each with its strong and weak points.
 - This time we don't have the benefits of the fossil energy transition: pre-packaged energy almost for free. But we will get more energy democracy, and in the end a more flexible infrastructure. Mix of central and decentral. Some long-term storage and long-distance transport needed to overcome winter in case of solar.
 - Fuel-cell development (integrated generation/storage system) and more battery development needed.
 - Also, more investment in energy conversion, cogeneration and using/storing "waste" heat. we still waste most of our high-grade energy (fossil and electrical) by turning it into heat! (And most of that escapes.) Even the technology for passive houses is widely available but rarely used.
 - But don't stand around waiting for new technologies. Solar + storage is not affordable, off-grid or on-grid. And think long-term, fossil energy will become more expensive in the long run, if only because the increasing EROI.
 - The future is now. It already makes sense to electrify your home, office and transport, to use solar energy and installing heat buffers and batteries. And as fossil-derived energy will have to become more expensive, it will only make more sense in the future.
 


Interested in reading more articles like this? Follow us [on Facebook](https://www.facebook.com/sustainsubstance), or through our [Atom-feed](/feeds/all.atom.xml).



-----

### Notes:


[^tesladiscussion]:
*Some hail it as the next step in the sustainable energy revolution, while others are more sceptical, pointing out the technical limitations and hidden costs of the system.*   
Most online-discussions I have seen on Tesla batteries tend to focus mainly on the costs of the batteries and the entire system, versus the cost of more traditional power sources. 
Some good examples:

	- Namez Raam, [Tesla Battery Economics: On the Path to Disruption](http://rameznaam.com/2015/04/30/tesla-powerwall-battery-economics-almost-there/)
	- Tom Lombardo, [Tesla's Powerwall by the Numbers](http://www.engineering.com/ElectronicsDesign/ElectronicsDesignArticles/ArticleID/10057/Teslas-Powerwall-by-the-Numbers.aspx)
	- Dan Steingart, [More Thoughts on Energy Storage and the Powerwall: Power and Energy](https://medium.com/@steingart/more-thoughts-on-energy-storage-and-the-powerwall-b9865c7ae5ee)
	- Christopher Helman, [Why Tesla's Powerwall Is Just Another Toy For Rich Green People](http://www.forbes.com/sites/christopherhelman/2015/05/01/why-teslas-powerwall-is-just-another-toy-for-rich-green-people/)
	- Zachary Shahan on CleanTechnica, [Tesla Powerwall Price vs Battery Storage Competitor Prices (Residential & Utility-Scale)](http://cleantechnica.com/2015/05/07/tesla-powerwall-price-vs-battery-storage-competitor-prices-residential-utility-scale/) and [Tesla Powerwall & Powerpacks Per-kWh Lifetime Prices vs Aquion Energy, Eos Energy, & Imergy](http://cleantechnica.com/2015/05/09/tesla-powerwall-powerblocks-per-kwh-lifetime-prices-vs-aquion-energy-eos-energy-imergy/)
	- Bruce Lin and Matthew Klippenstein on Catalytic Engineering, [Top Ten Facts about Tesla’s $350/kWh (DC) PowerWall battery](http://www.catalyticengineering.com/top-ten-facts-about-teslas-350kwh-powerwall-battery/) and [The Berlin (Power) Wall: Germany and Tesla’s Powerwall](http://www.catalyticengineering.com/the-berlin-powerwall/)

	The main technical limitation mentioned is the maximum sustained output power of 2 kW, although the PowerWall can deliver 3.3 kW peak power, and up to 9 PowerWall units can be combined in one installation. The main sources of hidden costs are the number of batteries required to be fully self-sustainable, the fact that a PowerWall-ready inverter is needed (e.g. a post-2013 [SolarEdge PV-inverter](http://www.solaredge.com/groups/products/pv-inverter) with a [StorEdge unit](http://www.solaredge.com/groups/products/storedge)), and the costs for installation, maintenance and service.

	In response to critical reviews of the technical specifications, Tesla Energy [recently announced](http://www.computerworld.com/article/2933426/sustainable-it/tesla-boosts-power-output-of-its-home-battery-keeps-prices-the-same.html) that the maximum sustained power output of Powerwall units will be increased to 5 kW, with a peak output of 7 kW.


[^kWh]:
The kilowatt-hour (kW·h, but often written as kWh) is a unit of *energy*, mostly used to express electricity-use and -storage. A kilowatt-hour is the amount of energy consumed in an hour, by a device that constantly draws 1000 Watt[^watts] of power. Technically, the SI-unit [Joule](https://en.wikipedia.org/wiki/Joule) should used for this, one kW·h being equal to 3.6 MJ (megajoule). However, following author [David MacKay](http://www.withouthotair.com), I prefer to use kW·h as the unit for energy, rather than MJ or something else, because people tend to be more familiar with it (e.g. from their electricity bill).   
For really small or really large amounts of energy, I will occasionally use the related units W·h, MW·h, GW·h and TW·h. One kW·h is equal to 1000 W·h (Watt-hour). Moreover, one MW·h (Megawatt-hour) is 1000 kW·h, a GW·h (Gigawatt-hour) is 1000 MW·h, and a TW·h (Terawatt-hour) is 1000 GW·h.   

	For more information on energy and power and their units, I can recommend the overviews given in [David MacKay's book](http://www.withouthotair.com/c2/page_24.shtml) and on [Tom Murphy's blog](http://physics.ucsd.edu/do-the-math/useful-energy-relations/).


[^watts]:
The [Watt (W)](https://en.wikipedia.org/wiki/Watt) is a unit of *power*. It specifies how much *energy* is transferred in a given *time* (and its definition in SI-units is therefore J/s). You can think of power as the speed at which energy flows. For larger amounts of power I will use the related units kW, MW, GW and TW. One kW (kilowatt) is 1000 W, one MW (Megawatt) is 1000 kW, a GW (Gigawatt) is 1000 MW, and a TW (Terawatt) is 1000 GW.   
For more information on energy and power and their units, I can recommend the overviews given in [David MacKay's book](http://www.withouthotair.com/c2/page_24.shtml) and on [Tom Murphy's blog](http://physics.ucsd.edu/do-the-math/useful-energy-relations/).


[^weight]:
For expressing weight (or rather, mass), I use the units kilogram (kg), metric tonne (t) and Megatonne (Mt). One kg is 2.2 pounds (lbs). One metric tonne is 1000 kg, or 2205 lbs. One Megatonne is one million metric tonnes.


[^volumedistance]:
For expressing volume, I use litres (L),  One litre is approximately equal to one US liquid quart (qt) or 2 US pints, and is around 1.76 UK pints. For expressing distance, I use metres (m) or kilometres (km). One metre corresponds to 3.3 feet (ft). One km is 1000 metres, or 0.6 miles.


[^batteryhistory]:
*The first "modern" electrochemical battery was built over two centuries ago by Alessandro Volta, and in fact the principle hasn't really changed since then. The first rechargeable battery, a lead-acid battery, was invented in 1859 by Gaston Planté. This type of battery is still widely used in cars today.*   
The UC Davis ChemWiki has a [very nice overview of battery development over the ages](http://chemwiki.ucdavis.edu/Analytical_Chemistry/Electrochemistry/Electrochemistry_6%3A_Electrochemical_Energy_Storage_and_Conversion).


[^evhistory]:
*Why did electric cars disappear for almost a century, and why is it now taking so long for electric driving to really take off? The answer lies mainly in energy storage.*

	Electric vehicles (EVs) were the dominant type of cars in the early decades on the 20th century. As long as the roads were generally not very suitable for cars, the practical maximum speed of a car was very limited. Around 1911, a common range for EVs was around 120-160 km (75-100 miles) on a single charge, which was sufficient in most cases. Moreover, except for their smaller range, EVs were considered superior to gasoline-powered cars. They were less noisy, safer and much easier to get running. However, after the [Model-T Ford](https://en.wikipedia.org/wiki/Ford_Model_T) was introduced in 1908, gasoline-powered cars gradually became a more attractive option. [Better roads](https://en.wikipedia.org/wiki/Transportation_in_the_United_States#History) made range more important, and electric starters (introduced in 1912) improved user-friendliness. Moreover, the booming car- and oil-industry in the US played an important role in decreasing the price of gasoline, dismantling public transport and promoting gasoline-powered cars and buses over EVs, trams and trains. 

	Kris de Decker has written [an interesting article on the subject of early vs. modern EVs on Lowtech Magazine](http://www.lowtechmagazine.com/2010/05/the-status-quo-of-electric-cars-better-batteries-same-range.html), and has compiled a [great overview of early 20th century electric cars and their specifications](http://www.lowtechmagazine.com/overview-of-early-electric-cars.html). And there are many articles on the roles played by [General Motors](https://en.wikipedia.org/wiki/General_Motors_streetcar_conspiracy) and [Standard Oil](https://en.wikipedia.org/wiki/Standard_Oil) in the dismantling of US public transport, e.g. on [Wikipedia](https://en.wikipedia.org/wiki/General_Motors_streetcar_conspiracy), [The Linux Information Project](http://www.linfo.org/standardoil.html) and the [LA Times](http://articles.latimes.com/2003/mar/23/local/me-then23).


[^energydensity]:
*The energy density is a measure of how much energy is packed in a given volume or weight.*   
Actually, energy density is energy per unit volume. Energy per unit weight is called *specific energy*. Gasoline has a specific energy of around 12.8 kW·h/kg, and an energy density of around 9.6 kW·h/L. Diesel has a specific energy of around 12.7 kW·h/kg, and an energy density of around 10.8 kW·h/L. A lithium-ion battery cell has a specific energy of 0.1-0.3 kW·h/kg, and an energy density of around 0.2-0.6 kW·h/L. Uranium has a specific energy of over 21 million kW·h/kg. See also: <https://xkcd.com/1162/>


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
*If the demand for electricity falls, power plants have to be physically throttled back or taken offline. If energy demand rises, supply is increased where possible by increasing power plant output, or by bringing extra plants online.*   
Typically, only the output of gas-fired power plants can be rapidly modified (and even that takes around ten seconds).


[^EVload]:
*While using an electric vehicle may reduce your consumption of oil, it easily has the potential to double or triple your electricity consumption.*

	- An average Dutch person would use 7 kWh per day, if everyone would switch to using an EV or hybrid
   		- average NL family, 2.2 persons, 3500 kW·h per year, so 4.5 kW·h per day per person.
   		- plus ~2.5 kW·h for recharging EV (assuming 22 km driving, 16 kW·h effective battery capacity for a 100 mile / 160 km range, and 90% efficient charging)
   		- Total would be ~7 kW·h per day per person, or 2555 kW·h per year.
 		- In average case, it increases electricity use with more than 50%. For individuals that drive more than 22 km per day, it can easily more than double electricity use.

   	- An average Dutch person drives around 22 km per day
   	- Plug-in hybrid car 16 kW·h, 40 miles
   	- EV passenger car 24 kW·h, 100 miles
   	- DoD ca. 67% gives effective capacity around 16 kW·h
   	- EV delivery van 50 kW·h, 100 miles
   	- Tesla Roadster: 53 kW·h, 244 mi (393 km)
   	- Tesla Model S EV: 40-90 kW·h, 240 mi (390 km) - 265 mi (426 km)



[^musksquare]:
*... the area shown is roughly a 100 km × 100 km square in North-West Texas. Filled with solar panels, this could generate around 500 GW of electric power, indeed more than the current mean US electricity demand of 425 GW.*   
Andrew ZP Smith checked the statement of Musk on the UCL Energy Blog, the figures above are based on [his estimate](http://blogs.ucl.ac.uk/energy/2015/05/21/fact-checking-elon-musks-blue-square-how-much-solar-to-power-the-us/).   
Of course, literally placing all the solar panels in a 100,000 km^2^ square would be a silly idea. Rather, the panels would be distributed over the country, and would mostly be on roofs. And of course, this would somewhat increase the panel area needed, to compensate for the fact that you have less sun up north.


[^squarebatt]:
*On an average day, the entire US uses over 10 billion kW·h of electricity (10.2 TW·h). Storing this amount of energy would require a little over 102 million Tesla PowerPack batteries. You'd probably need a bit more storage than that to cover bad days and peak loads. Indeed, Musk himself estimates that around 160 million PowerPacks would be needed. It's by no means impossible to install that much capacity, but the batteries alone would cost around 4 trillion dollars, and producing them would require close to 20% of the world's known lithium-reserves.*

	According to the EIA, [total US electricity sales in 2013](http://www.eia.gov/electricity/annual/html/epa_01_02.html) were 3725 TW·h, which comes down to 10205 GW·h per day on average. A Tesla PowerPack battery stores 100 kW·h (= 0.0001 GW·h), and costs $25000. Producing a Li-ion battery [requires 0.17-0.28 kg lithium per kW·h of storage, depending on the battery type](http://seekingalpha.com/article/654441-ev-myths-and-realities-part-1-the-battery-crisis). Using the upper boundary, we would need 2.86 Mt of lithium to produce 10205 GW·h of battery capacity, or 4.48 Mt for 160 million PowerPacks. We take 23.6 Mt as a best estimate of the known lithium reserves ([Mohr et al. 2012](http://dx.doi.org/10.3390/min2010065)).


[^ustotalenergy]:
*Tom Murphy shows that using lead-acid batteries to store a week's worth of US energy demand would require 4.5 trillion kg (4536 Mt) of lead, and would cost more than the annual US GDP. Even if we would reduce the storage capacity to just one day, we would still need more lead to build the batteries (648 Mt) than the world's known lead reserves (around 80 Mt). Using lithium-ion batteries we would fare a bit better. Extrapolating from Musk's estimate, we'd need around 753 million PowerPack batteries to cover total US energy use.*   
Comparing the total US *energy use* (48 TWh per day if we would switch everything to electricity) to the current *electricity use* (10.2 TW·h per day), total energy use is a factor 4.7 higher.


[^roundtrip]:
*the round-trip efficiency of modern systems is around 80%, which is actually pretty good.*   
The round-trip efficiency is a measure of how much of your original energy is left after having stored it. A round-trip efficiency of 80% means that of the original 100% of energy you put in, you lose 20% in conversion and storage, and you're left with 80%. Battery storage tends to be quite efficient, with round-trip efficiencies over 80% for lead-acid systems and over 90% for lithium-ion batteries. Hydrogen-based electricity storage tends to be rather inefficient, with round-trip efficiencies being between 20-50%, which means that 50-80% of the electricity is lost after storage. This "lost energy" isn't literally gone, of course. It just is no longer available in the form of electricity. In the conversion processes involved in storage, the "lost electricity" has been converted into heat. In some cases, this heat can be put to good use, increasing the overall usable energy (or thermal) efficiency of the storage. However, when I talk about round-trip efficiency in this article, I specifically mean electrical efficiency.


[^germanpowerstats]:
*But it's not nearly enough to cover the German electricity demand, which amounts to roughly 1.6 TW·h on an average day, with demand fluctuating between lulls as low as 32 GW in summer, to peaks over 90 GW in winter. In fact, it's not even sufficient to cover the contribution of solar PV in Germany, which currently has a production capacity of around 38.5 GWp (gigawatt-peak, the power output under optimal laboratory conditions).*   
TODO: sources


[^pumpedenergy]:
*Storing the amount of energy in a normal AA-battery (3 W·h), would require hoisting 360 litres of water (roughly 2.5 filled bathtubs) up to a height of 3 metres, or 100 litres to a height of 10 metres. And that's just the energy in one small battery. Storing the energy in a litre of gasoline or a 10 kW·h PowerWall would require lifting our 100 litres to a height of 36 km, or perhaps more practical, lifting 360 m^3^ of water (e.g. a swimming pool of 25×10×1.44 m, weighing 360 tonnes) to a height of 10 m! Matching the capacity of the 100 kW·h PowerPack would require roughly an olympic swimming pool (50×25×2.88 m, containing 3.6 Mt water) lifted to 10 metres height.*   
     
	You can calculate the potential energy contained in a mass of *m* kg at a height of *h* metres as: *m* × *g* × *h*, where *g* is the gravitational accelleration (9.8 m·s^-2^). The result will be in Joule. (This derives directly from Newton's Law, *F* = *m* × *a*, where *F* is the force exerted by the mass *m*, in N. A Joule, or 1 kg·m^2^/s^2^, is the energy transferred when a force of 1 N acts over a distance of 1 m.) To get the result in kW·h rather than Joule, divide it by 3.6·10^6^. I've assumed here that 1 L of water will weigh 1 kg, and therefore that 1 m^3^ of water will weigh 1 metric tonne. Also, I've approximated the gravitational accelleration as 10 m/s/s. So, for example, 10 kW·h = 36,000,000 J, which would be the energy contained in 100 L water at 36 km height (100 kg × 36000 m × 10 m·s^-2^), or in 360 m^3^ at 10 m height (360000 kg × 10 m × 10 m·s^-2^). Similarly, 100 kW·h would be 3600 m^3^ water at 10 m height. This would require a basin of 40×30×3 m, or 50×25×2.88 m. An olympic-size swimming pool is 50×25 m, with a minimum depth of 2 m and a recommended depth of 3 m.


[^caeshistory]:
*In fact, the second most important storage method is Compressed Air Energy Storage, or CAES. This has been around since the late 19th century, when compressed air was distributed over cities with pipes, and was used to power machines directly.*   


[^lightsail]:
*Lightsail has developed a 750 kW·h CAES storage module, the size of a shipping container.*   
   - http://www.lightsail.com/
   - To store energy, an electric motor drives an air compressor. To deliver energy, we reverse the process–the air compressor becomes an expander, and the electric motor becomes a generator.
   - Heat from compression is stored or routed to nearby buildings, providing heating. During expansion, heat is extracted from storage, or buildings providing air conditioning. This dramatically increases building energy efficiency.
   - 90% Thermal efficiency, roundtrip
   - <10°C Final temperature difference
   - 1200 RPM, 100 kW scale; 500+ hrs reliable operation Reciprocating piston compressor/expander
   - Air can be stored in simple, low cost air storage tanks, packed in a convenient shipping container form factor using industry standard pipes and matching ASME and ISO safety standards. For truly massive installations, air can be stored in underground caverns which is the standard for large scale natural gas storage.
   - Storage Unit
      - 750 kW·h modules
      - Shipping container form factor
      - ASME certified


[^caesexamples]:
*Currently there are three large CAES-installations in operation world-wide.*   
   - In December 2012, General Compression commissioned a 2 MW (500 MWh) Dispatchable Wind™ GCAES™ project in Gaines, Texas. Source: http://www.generalcompression.com/index.php/who
   - 1978 – The first utility-scale compressed air energy storage project was the 290 megawatt Huntorf plant in Germany using a salt dome.
   - 1991 – A 110 megawatt plant with a capacity of 26 hours was built in McIntosh, Alabama (1991). The Alabama facility's $65 million cost works out to $550 per Kilowatt hour of capacity, using a 19 million cubic foot solution mined salt cavern to store air at up to 1100 psi. Although the compression phase is approximately 82% efficient, the expansion phase requires combustion of natural gas at one third the rate of a gas turbine producing the same amount of electricity. Source: https://en.wikipedia.org/wiki/Compressed_air_energy_storage


[^caesexperiments]:
*some projects are looking into storing compressed air in aquifers, disused oil- and gas-fields, and even in large "bags" on the ocean floor.*   
   - The Iowa Stored Energy Park (ISEP) will use aquifer storage rather than cavern storage. The displacement of water in the aquifer results in regulation of the air pressure by the constant hydrostatic pressure of the water. A spokesperson for ISEP claims, "you can optimize your equipment for better efficiency if you have a constant pressure."[35] Power output of the McIntosh and Iowa systems is in the range of 2–300 MW.[36]
   - Deep water in lakes and the ocean can provide pressure without requiring high-pressure vessels or drilling into salt caverns or aquifers.[38] The air goes into inexpensive, flexible containers such as plastic bags below in deep lakes or off sea coasts with steep drop-offs. Obstacles include the limited number of suitable locations and the need for high-pressure pipelines between the surface and the containers. Since the containers would be very inexpensive, the need for great pressure (and great depth) may not be as important. A key benefit of systems built on this concept is that charge and discharge pressures are a constant function of depth. Carnot inefficiencies can thereby be reduced in the power plant. Carnot efficiency can be increased by using multiple charge and discharge stages and using inexpensive heat sources and sinks such as cold water from rivers or hot water from solar ponds. Ideally, the system must be very clever—for example, by cooling air before pumping on summer days. It must be engineered to avoid inefficiency, such as wasteful pressure changes caused by inadequate piping diameter.[39]


[^hydogenefficiency]:
*In total, the round-trip efficiency of hydrogen-based electricity storage is at best around 50%, but more commonly 20-40%. In other words, you commonly lose around 60-80% of your energy along the way. In the current best-case, you would still lose around half.*   
As a hypothetical "best case", I assume 73% efficiency of electrolysis, 95% efficient pressurised storage and 70% electrical efficiency for a hybrid fuel cell. This gives 0.73 × 0.95 × 0.70 = 0.485, or a round-trip efficiency of 49%.
   - Electrolysis is energy intensive. The power consumption at 100%  theoretical  efficiency  is  39.4  kW·h/kg  of  hydrogen; however, in practice it is closer to 50-65 kW·h/kg. The conversion efficiency of water to hydrogen, depending
on the system, can be between 80 and 95%. Considering the power needed for a complete electrolyzer system, the best energy efficiency is today around 73%. This means that about 53 kW·h of electricity is needed to produce 1 kg of hydrogen. Current R&D efforts are aimed at improving net system efficiencies of commercial electrolysis toward 85%.
   - Source:
   http://photonics.inescporto.pt/outputs/fct2009/olah-g-a-_2009.pdf
   Chemical Recycling of Carbon Dioxide to Methanol and
   Dimethyl Ether: From Greenhouse Gas to Renewable,
   Environmentally Carbon Neutral Fuels and Synthetic Hydrocarbons
   George A. Olah, Alain Goeppert, and G. K. Surya Prakash
   J. Org. Chem. 2009
   DOI: 10.1021/jo801260f


[^hydrogenproblems]:
*We've seen that hydrogen is not a very good option for long-term energy storage.*   
Notes: storing hydrogen for transport is problematic
 - Hydrogen is not a fuel but an energy carrier.
 - It's a small molecule and highly reactive 
 - Hard to store because of low volume density, generally stored at high pressure or at low temperatures, both of which require energy and material.
   - High-pressure storage is the most common
   - Liquification isn't practical, requires cooling down to -253 degrees, is only ~60% efficient and requires energy to maintain.
   - Both require further energy for long-term storage.
   - Solid state storage
 - Hard and expensive to transport due to low energy density, safety issues and interaction with other materials.


[^sabatier]:
*But it is actually possible to chemically combine hydrogen gas with CO~2~, again from the exhaust of fossil-based power plants. This process is based on the so-called *Sabatier reaction*, and it can be used to produce, among other things, methane and methanol.*   
The [Sabatier reaction](https://en.wikipedia.org/wiki/Sabatier_reaction) is a CO~2~ hydrogenation process, which involves the reaction of hydrogen with carbon dioxide, forming methane and water. The process was discovered by the French chemist Paul Sabatier in the early 20th century, and can be summarised as follows: CO~2~ + 4 H~2~ → CH~4~ + 2 H~2~O + energy. While the reaction is exothermic, it does require elevated temperatures, high pressure, a catalyst and activation energy to get started. Depending on the process and catalysts used, hydrocarbons other than methane can be formed, such as methanol or dimethyl ether. For a slightly more extensive explanation of the chemistry and potential, see e.g. [this short article by Barbarossa and Varga, 2011](http://www.enea.it/it/pubblicazioni/EAI/anno-2011/n.-6-2011-novembre-dicembre-2011/alternative-use-of-co2). For the full gory details of various CO~2~ hydrogenation techniques, see e.g. [Wang et al. 2011](http://dx.doi.org/10.1039/c1cs15008a) ([PDF](http://www.talknicer.com/co2hydrogenation.pdf)).


[^fuelcellplants]:
So far, the biggest fuel cell power facility built by Fuel Cell Energy is located in Hwasung, South Korea. It consists of 21 modules, which use natural gas to generate 59 MW of electricity and 27 MW of steam (used for district heating). The installation does not do CO~2~-capture, although hypothetically it could capture around 48 tonnes of CO~2~ per hour. This would be enough to "clean up" the emissions of around 60 MW of coal-generated electricity.

	- 21 modules, each of which can capture about 2300 kg per hour of external CO2, gives 48300 kg per hour, enough for CCS of ~60 MW of coal power? (or ~65 MW with 90% capture), and producing 59 MW of electricity
	- http://www.fuelcellenergy.com/advanced-technologies/carbon-capture/
	  - White paper: http://www.fuelcellenergy.com/assets/DFC-Carbon-Capture-White-Paper.pdf
	  - A 500 MW pulverized coal plant requires almost as large a DFC capture plant (about 400 MW) for a 90% carbon capture rate.  In the near term, capture systems can be configured as multiple-unit systems based on the largest DFC plant currently available, the 2.8MW DFC3000. The largest such system so far is a 59 MW system consisting  of twenty one DFC3000 powerplants, a project developed by POSCO, Korea Hydro Nuclear Power Co. (KHNP) and Samchully Gas Co in South Korea.
	- Largest CHP Power Plant installed worldwide in South Korea (Hwasung City) having 59 MW electrical and about 27 MW thermal (steam = used for district heating) Here the link for a video showing construction / installation of this park (truly impressive !) https://www.youtube.com/watch?v=yVPrbh7UHDY
	- A conventional pulverized coal power plant with a typical CO2 emission rate of 820 kg/MWh would require a larger capture system than a large scale natural gas combined cycle plant with a CO2 emission rate of 360 kg/MWh. A 2.8MW DFC3000 
powerplant during normal power operation is transferring about 3200 kg of CO2 per hour from the cathode to anode streams
in the stack modules. In carbon capture mode, this system could capture and purify about 2300 kg per hour of external CO2 in addition to 
the CO2 exhaust of the DFC powerplant.
	- DFC® power plants are designed for a 20-years-lifespan (http://www.all-energy.co.uk/__novadocuments/54261?v=635376488533500000)
	- http://www3.epa.gov/chp/documents/wbnr061715.pdf
	- http://fortune.com/2015/09/04/new-tech-cleans-up-coal-plants/
	- Carbon capture pilot financed by DOE, to start in 2016. The project requires FuelCell Energy to install a two-megawatt Direct FuelCell ("DFC") system, which will be a modification of the company’s commercial DFC3000 fuel cell power plant. The carbon capture fuel cell system will be installed beside an existing coal-fired power plant to capture carbon dioxide (CO2) from the exhaust of a coal plant apart from generating power. The second phase of the project requires the installation of 11 additional fuel cell power plants to capture roughly 700 tons of CO2 per day, while simultaneously generating about 648,000 kW·h of ultra-clean power on a daily basis. http://www.greencarcongress.com/2015/09/20150902-fcedfc.html 
	- FuelCell Energy Inc. (Danbury, CT) will design, fabricate, and test a small pilot-scale system that incorporates FuelCell Energy’s combined electric power and CO2 separation (CEPACS) system, based on electrochemical membrane (ECM) technology, to separate at least 90 percent of CO2 from a 3 MWe equivalent slipstream of pulverized coal plant flue gas and achieve 95 percent CO2 purity at a cost of $40/tonne of CO2 captured and at a cost of electricity 30 percent less than baseline CO2 capture approaches. Successful pilot-scale validation of the CEPACS system is expected to pave the path toward commercial deployment of cost-effective ECM technology for large scale coal-based carbon capture applications by 2025. Partner is AECOM.  http://energy.gov/fe/articles/doe-selects-eight-projects-receive-funding-reducing-cost-co2-capture-and-compression



[^sabatierplants]:
The German [Centre for Solar Energy and Hydrogen Research](http://www.zsw-bw.de/en) (ZSW, Zentrum für Sonnenenergie- und Wasserstoff-Forschung) was the first to build a large-scale test-plant that uses electricity to produce methane from CO~2~. Their [250 kW test facility](http://www.zsw-bw.de/en/topics/fuelshydrogen/power-to-gas.html) in Stuttgart has been operating since 2012, and can produce up to 300 m^3^ of methane per day. At an energy mass density of 15.4 kW·h/kg, this represents around 2900 kW·h (2.9 MW·h) of stored chemical energy. The bigger and commercial Audi e-gas plant was based on the [technology developed by ZSW](http://www.etogas.com/referenzen/article/industrielle-63-mw-ptg-anlage-audi-e-gas-anlage/). The Audi plant opened in 2013, and produces roughly 1000 tonnes of methane per year, or 2738 kg per day. In terms of chemical energy storage, this would come down to 42208 kW·h per day. The [George Olah carbon dioxide recycling plant](http://www.chemicals-technology.com/projects/george-olah-renewable-methanol-plant-iceland/) in Grindavík, Iceland opened in 2011. It produces around 2 million liters of methanol per year, and has the capacity to produce around 5 million liters per year. Methanol has a specific energy of around 5.5 kW·h/L. The CO~2~ is captured from the Svartsengi geothermal power station. Contrary to popular belief, geothermal power stations do emit CO~2~, albeit less than fossil fuel powered energy generators. The chemistry Nobel laureate [George Olah](https://en.wikipedia.org/wiki/George_Andrew_Olah) was an important advocate of the [methanol economy](https://en.wikipedia.org/wiki/Methanol_economy), in which synthetic methanol would be the main form of energy storage.



[^NLEVPVexample]:
*For example, if everyone were to switch now to all-electric cars, the average person in The Netherlands would use roughly 7 kW·h of electricity per day (just for home use and transport, not counting the energy used outside the house or car). Using only solar energy, and without seasonal storage, the Dutch would need roughly 62 solar panels *per person* to generate sufficient electricity in December. That's 137 PV-panels for an average household, covering 226 m^2^. With long-term energy storage, this could be reduced to something like 17 PV-panels per person, or about 38 panels per household.*   
   - average NL family, 2.2 persons, 3500 kW·h per year, so 4.5 kW·h per day per person.
   - plus ~2.5 kW·h for recharging EV (assuming 22 km driving, 16 kW·h effective battery capacity for a 100 mile / 160 km range, and 90% efficient charging)
   - Total would be ~7 kW·h per day per person, or 2555 kW·h per year.
   - Yearly average for NL is 1000 volle zonuren. A single 265 Wp-panel would generate around 225 kW·h per year.
   - 7 kW·h per day would require around 11.4 panels per person. Let's assume long-term storage being 50% efficient, so say we'd need to generate 1.5 times the energy we need, which would require around 17 panels per person.
   - Average in december is 0.5 volle zonuren in NL (http://www.solsolutions.nl/zonnestroom/opbrengst-zonnestroom/). A single 265 Wp PW-panel would generate 0.5×0.85×265=113 Wh = 0.113 kW·h on an average December day in NL. So to generate our average 7 kW·h with only short-term storage, we would need 62 solar panels *per person*. Or around 6555 modern 3 MW windmills at the coast.
   - A standard panel is 1.650×0.991 m, or 1.64 m^2^, so we'd need 101.4 m^2^ per person. With 16,920,510 people, this would be 1,715,389,459 m^2^, or 1715.4 km2. The country is 33.883 km2, so this would be roughly 5% of land area.


[^insulation]:
*Making smarter use of heat is probably the single most important step we can take to reduce our dependence on fossil fuels. In cold climates, the first step would be to make it less easy for heat to escape our buildings.*   


[^heatextraction]:
*The second step would be to stop getting most of our heat from burning fossil fuels and biomass. Even in Northern winters it's still possible to get a significant amount of heat directly from sunlight, using passive building designs or thermal solar collectors. Additional heat can be extracted from the environment using a heat pump. Moreover, much better use can be made of waste heat from other processes, such as power generation.*   
<http://physics.ucsd.edu/do-the-math/2012/01/basking-in-the-sun/>


[^heatstorage]:
*The third step in using heat more effectively, is to store it in a heat buffer for later use. A heat buffer can take the form of an underground water reservoir, a large mass of rock, or for shorter periods, even walls and floors.*   



[^redoxflow]:
*It is unlikely that the main role of Tesla Energy will be to provide battery power storage on the scale of entire countries, [...] A problem like that is best solved with a mix of approaches and technologies. Certainly, Tesla's Li-ion batteries may play a role, as will expansion of pumped storage and use of other battery technologies such as redox flow.*   

[^customsolution]:
*But a more important point is perhaps this: Tesla is the first company to offer and market battery storage not as a custom niche-market solution, but rather as a mass-produced consumer appliance that should "just work".*   
Of course, a PV-installation with battery storage *is* actually a highly customised product. There is no "one size fits all" solution, because every location is different in terms of latitude, orientation, weather patterns, construction, electrical installation and electricity use. You will always need someone with specialised knowledge to design and install the system. But this is not the point. Tesla's batteries will allow battery storage to be offered as a regular and fairly affordable option with new (and existing) PV-installations, rather than as a costly solution only to be applied in special cases.

[^teslatricks]:
*In a technical sense, Tesla's Powerwall is not a revolutionary product. It is proven technology, just nicely packaged and fitted with smart software and some other tricks to extend the inherently limited life-span of its Li-ion cells.*   
The boys at Catalytic Engineering have written a very nice article on [why heat is such a problem for batteries](http://www.catalyticengineering.com/keeping-your-cool-when-youre-a-battery-a-fuel-cell-or-an-engine/).

