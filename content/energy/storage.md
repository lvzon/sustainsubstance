Title: Energy storage and the Tesla battery 
Authors: Levien van Zon
Date: 2015-06-03
Modified: 2015-09-03
Tags: energy
Slug: storage

**By Levien van Zon**

*The footnotes provide additional background information, and can safely be skipped or read separately.*

A few months ago, Tesla's Elon Musk [announced](https://www.youtube.com/watch?v=yKORsrlN-2k) a new product for energy storage, the [Tesla Powerwall](http://www.teslamotors.com/powerwall). This announcement generated a lot of attention, both on the Internet and in the global media. Some hail it as the next disruptive technological step in the sustainable energy revolution. Others are more sceptical, pointing out the technical limitations and hidden costs of the system[^tesladiscussion]. Such discussions aside for a moment, I think it's good to take a step back and look at what all the fuss is about. The first question to ask would be this: What problem is Tesla Energy trying to solve with its new battery products? 


As Elon Musk explains in his [keynote speech](https://www.youtube.com/watch?v=yKORsrlN-2k): *"We have this handy fusion reactor in the sky, the sun,"* which *"produces ridiculous amounts of power."* However, "*the obvious problem with solar power is that the sun does not shine at night.*" So, if we want solar energy to replace the electricity generated from fossil fuels, we need some way of storing the power generated during the day, so we can use it any time we need it. This may sound trivial: After all we have batteries, right? True, but *"the issue with existing batteries, is that they suck."* They are large, expensive, have a short life span and are hard to integrate with existing infrastructure. That's where the Powerwall comes in. It's designed to be an attractive, scalable and relatively cheap battery solution that "just works". It comes in two versions, a 7 kW·h[^kWh] model designed for daily charging and discharging, and a 10 kW·h model designed for occasional use as backup power supply. Up to nine batteries can be combined, for storage up to 90 kW·h. And for industrial use, Tesla introduced the Powerpack, which comes in 100 kW·h units that are infinitely scalable. And addressing the problem of short life span, Tesla offers a 10-year warranty on the Powerwall.


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

   - TODO: Look up pumped storage capacity and example(s). 
     - World
     - US: >22 MW (~2%), with ~34 MW planned
     - UK: 2.8 GW, 30 GWh in 4 facilities. Dinorwig can switch on, from 0 to 1.3 GW power, in 12 seconds. Dinorwig stats: 1.80 GW, 6.7 million m^3 volume, 9.1 GWh storage, ~500m height difference, maximum flow rate 390 m3/s, allowing power delivery at 1.7 GW for 5 hours, efficiency 75%.

     - Germany: 6.8 GW, 0.05 TWh, good for about 6 to 8 hours of operation. The Goldisthal pumped storage project, at 1060MW is Germany's largest, followed by Markersbach at 1050MW. Both projects are owned by Vattenfall. The expansion potential in Baden-Württemberg and Thuringia alone amounts to nearly 24GW, according to studies. Fraunhoffer: The currently installed pumped storage capacity in the German grid stands at almost 38 GWh, while rated power is approximately 6.4 GW and the average efficiency value is 70 percent (without transmission losses). As a comparison, the aforementioned storage capacity corresponds to the yield generated by German PV power plants in the space of fewer than two full-load hours.

     - Europe: almost 45 GW estimated in 2011, 170 plants, average 300 MW per plant, with ~27GW extra planned by 2020. A 2013 JRC study puts the European theoretical potential around 54-123 TWh of storage, with a significant fraction (>50%) of potential sites outside the EU.
     - Norway and Sweden: 116 TWh combined.
     - Austria and Switzerland ~12 TWh combined.
     - Portugal is planning to deploy 1GW of new storage for every 3.5GW of renewables.

   - You do need two big lakes and a hill (or other height difference). Most really good locations are already in use, but studies for many countries show that capacity can easily be increased by ~50% (EU) or more (~105% US). Also, old hydroelectric and PHS systems can be retrofitted to add storage and improve efficiency (can be <70% for old installations, >80% for new ones). But environmental impacts can be significant for new locations, and capital investment takes decades te recover. Interesting alternatives include compressed air storage and underground and undersea storage. But it still needs big volumes of water, so constructing reservoirs will require space, capital and energy.
   - Calculate how much water and how many batteries would be needed to replace one average coal or gas power station. See also McKay.
      - A typical US coal power plant is 500 MW. Big ones are 2-5 GW. China builds mostly big ones.
   - Show graph of current power generation, use and storage in Germany. Estimate storage needed for current German wind and solar, and figures if all German power were wind and solar.
      - At the end of 2014, the cumulative installed PV capacity worldwide reached approximately 180 GW. 
      - In 2014, PV-generated power totaled 35.2 TWh and covered approximately 6.9 percent of Germany’s net electricity consumption. Renewable energy as a whole (RE) accounted for ca. 31 percent of net electricity consumption, while the proportion of PV and total RE in Germany’s gross electricity consumption stood at ca. 6.1 percent and 27 percent respectively. On sunny weekdays, PV power can at times cover 35 percent of the momentary electricity demand, and on weekends and holidays up to 50 percent. The total nominal power of PV installed in Germany rose to ca. 38.5 GW, distributed over 1.5 million power plants, by the end of 2014. With this figure, the installed PV capacity exceeds that of all other types of power plants in Germany.
   - Quote how much would be needed for the entire US (the example given by Musk). There is not enough lead in the world to do this with lead-acid (see State o/t World 2013). With Li-ion it would be possible, but of course quite expensive (how much?).

 - Note: Also decentral energy is unpredictable and hard to control, and therefore does not fit well with a highly centrally managed system like the grid.


### The role of Tesla

It is unlikely that the main role of Tesla Energy will be to provide battery power storage on the scale of entire countries, no matter how trivial Elon Musk may make this sound. No doubt it would be a lucrative contract for Tesla, but reliable and durable energy storage on that scale is a hard problem that requires a significant investment. A problem like that is best solved with a mix of approaches and technologies. Certainly, Tesla's Li-ion batteries may play a role, as will expansion of pumped storage and use of other battery technologies such as redox flow[^redoxflow].

But for individuals and organisations, there is no need to wait for large-scale grid-based energy storage. If you want to contribute to the sustainable energy transition without relying (too much) on fossil-powered backup electricity from the grid, there is no reason why you cannot install solar panels and batteries at the scale of households or office buildings. And this is where Tesla's batteries can make a big contribution.

Household-scale battery storage is not exactly a new idea. 
 - TODO: Look up early examples, pictures and cost of lead-acid and Li-ion storage systems (name some companies). 
 - Lead-acid batteries require monthly equalization and topping-off with water, have a limited number of deep cycles (500-1000 typically), and do not tolerate extended periods at low charge.
Up until a few years ago, affordable battery storage generally required a room full of lead-acid batteries. Because the life-span of batteries quickly decreases with the depth of discharge (DoD), you usually need to install much more battery capacity than you will actually need on a day-to-day basis. Li-ion batteries may be more expensive than lead-acid, they also last longer and take up much less space. Compared to alternative systems, Tesla's batteries are small, fairly durable, look attractive and are relatively affordable due to their projected large-scale production. 

In other words, while Tesla Energy is not the first to offer a home-scale electricity storage solution, they certainly have better PR and more attractive pricing than most alternative solutions currently on the market. But a more important point is perhaps this: Tesla is the first company to offer and market battery storage not as a custom niche-market solution, but rather as a mass-produced consumer appliance that should "just work".[^customsolution] 

In a technical sense, Tesla's Powerwall is not a revolutionary product. It is proven technology, just nicely packaged and fitted with smart software and some other tricks to extend the inherently limited life-span of its Li-ion cells. But this is excatly the thing that Tesla does right: using and scaling up existing technologies, thereby making it more widely available to consumers and organisations, instead of waiting around for some technological breakthrough that may or may not happen soon. It is the same strategy they use with their electric verhicles: make them attractive for people who can afford them, and then gradually bring down costs. (And incidentally, Tesla's and other electric cars are excellent small-scale electricity storage devices!) 
There are no doubt many people and companies that can afford the luxury of battery storage, or even going off-grid completely. The well-off early adopters of electric and hybrid cars may well be the same people who will want a fancy sleek power-storage device on their walls. As I wrote before, revolutions have to start somewhere, and this seems a good place to start. And this is a point that is generally missed by people who merely complain that solar power with Powerwall-storage currently tends to be more expensive than grid power.
 
 - TODO: look up current EV battery capacity.



### But is it sustainable?

At first glance, promoting PV-systems with battery storage would seem to be a favourable measure in terms of sustainability, for at least two reasons. Firstly, adding battery storage may make the adoption of solar energy more attractive in many countries. And secondly, storing solar and wind energy reduces the need to keep fossil-fuel power stations around as backup during nights and periods with little wind.

From a sustainability-perspective, the main reason to promote household- or company-scale PV-installations is that any electricity they produce will not have to be generated from fossil fuels. Countries like Germany or The Netherlands have it relatively easy for households to adopt PV solar panels: just have a PV-system installed on your house or company building, and hook it up to the grid. The grid operator then pays you money (up to a point) for the electricity you generate but don't use yourself. This is probably the main reason why solar energy is so widespread in Germany, even though it is not exactly the sunniest country in the world.

 - TODO: look up peak capacity and % of solar energy in Germany (and NL), as well as effective insolation (W/m2 and compared to places in Southern Europe, the Saharah, Australia and the US). Compare with % solar energy in Italy, Spain, Australia and US. Note that this system is effective but expensive (look up cost estimation for NL and Germany in terms of subsidies / tax money).

   - The average total horizontal irradiance in Germany between 1981 and 2010 stands at 1055 kWh/m2 per year and fluctuates according to location between approximately 951 and 1257 kWh/m2 per year. Tilting the PV modules increases the total incident irradiance on the modules by around 15 percent compared to the horizontal surface. This increases the average incident irradiation to roughly 1200 kWh/m2 per year throughout Germany.
   - Germans pay a surcharge on the grid-energy they use, which is then used to pay for the feed-in tariff. On the costs side, the cumulative amount paid for PV power fed into the grid up to and including 2013 amounted to around 41 billion euros. Energy consumers therefore pay for the energy transition. Fossil fuels however are subsidised by public money. If these costs were also to be added to the electricity price as a ‘conventional energy tariff,’ they would amount to 10.2 cts/kWh, which is almost three times the value of the Renewable Energy Tariff in 2012.


 - At first glance, yes. 
   - The idea of promoting home-scale PV is that any electricity it produces, will not have to be produced from fossil fuels. 
     - Germany: Based on data from 2013 giving the proportional amount of power generated from each energy source and the primary energy factors, each kWh of PV-generated electricity saved about 2.2 kWh of primary energy. In 2013, total primary energy savings amounted to 65 TWh. The consumption of 28 TWh PV electricity in 2012 avoided greenhouse gas emissions on the order of 18.6 million tons of CO2 equivalent.
     - Germany has a (granted, somewhat ambitious) scenario for completely switching to renewables by 2050.
   - In countries like Germany and The Netherlands, this is easy: you hook up your PV-installation to the grid, and you get money for electricity you produce. This is why PV is so widely installed in Germany, even though it is not exactly the sunniest country in the world. 
   - In many countries the situation is different, you don't get any money for the power you produce, so your financial gain comes from using the power you produce yourself (thereby saving money on grid-power). In these cases it makes sense to install a battery, to make sure you can actually use all the power your panels produce during the day.
   - Especially if such countries are sunny (e.g. Australia and the US), affordable batteries may speed up the adoption of PV.

- From a sustainability perspective, there is a catch. Batteries are not free, they cost not only money but also energy to produce.
  - Actually, quite a lot of energy. (How much?)
  - Add to that the energy needed to produce the solar panels and inverter. 
  - How long is the EROI? And how long before the carbon emissions become negative?
    - A solar plant’s energy payback time depends on the technology used and the plant’s location. For an annual global horizontal irradiance of 1055 kWh/m2 , which is the mean value for Germany, this takes approximately two years, and falling with better manufacturing techniques. Wind power plants in Germany demonstrate even shorter energy pay back times ranging from 2-7 months. (Fraunhoffer).
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
    - For the 3 Wh of energy stored in an AA battery, you'd need a mass of 360 kg, or about 800 lb at 3m height.
 - Flywheels and compressed air are also relatively efficient and low-tech, but not really feasible (as in: too bulky and dangerous) for storage on a small scale.
 - Most hydrogen fuel cells on the market today have less than 50% efficiency and are terribly expensive, so not suitable for home-scale storage.
 - Heat is much easier to store than electricity! 
   - Collecting it is no problem: Heat collectors, thermal storage, both on power-plant and residential scale. 
    - Hybrid concentrating solar collectors ("sunflowers") as example.
    - Proven technology: solar collector, thermal buffer, heat pump.
    - Are there options for molten salt as small-scale storage, heated by concentrated sunlight during the day, e.g. for cooking and heating?
   - The hard part is converting heat back to electricity. 
    - We do this all the time: combustion engines and steam engines work by converting fossil fuel into heat, and then into movement. In power gerenators, movement is then converted into electricity. It's a ludicrous process if youthink about it. Again, we only get away with it because fossil fuel contains so much energy that we can currently afford to waste most of it.
    - What is the efficiency of turning low-grade heat into electricity. What are the techniques available? Is this feasible on a small scale?
      - It's terrible. Mostly less than 5% or so.
 - Other forms of chemical storage than a redox cell? That's how nature does it (ATP etc.), but turning it back into electricity is still tricky. Carbohydrates can be made (basically oil), but combustion means a dismal efficiency. Our technology is rather primitive, still mostly relies on burning things. The best thing we have is still in essence 19th century technology, with a lot of tweaks.
 - Generating hydrogen, which can later be used to generate electricity. 
   - Main problems: hydrogen is hard to store/transport, has a low energy density and conversion back to electricity is not very efficient. You'll probably lose around 40%, a dsmal efficiency when compared to batteries or pumped storage. 
   - Interesting option: turning hydrogen together with CO2 from power stations into methane or methanol (Sabatier reaction). Back-conversion still has low efficiency, but both are much easier to store/transport, combination with carbon storage may be an option and both can alternatively be used in existing transport and natural gas applications. Moreover, hydrogen can also be produced using thermal processes.
 - Rather than (or in addition to) storage, bring down electricity use, and mostly use it at times when it is available. But despite much talk of and investment in smart grids, their impact so far is practically nonexistent. It is still a big mess of competing standards, with not much real-world applications to speak so far. Current applications do not proceed much beyond the pilot-project stage, and no-one basically knows yet how to organise a practical large-scale smart-grid. Certainly the technology is there, but it is an almost intractable organisational problem, and will probably remain so for a fair number of years.
 - But don't stand waiting around for new technology, especially with thermal energy. We still waste most of our high-grade energy (fossil and electrical) by turning it into heat! (And most of that escapes.)
 - And installing PV won't immediately solve the energy problem, but it goes a litle way. And at least investing in storage solutions and smart grids becomes more interesting as PV-production capacity increases.


[![A graph from Bosch Solar Storage, comparing energy consumption and PV production in a European country.](http://bosch-solar-storage.com/wp-content/uploads/2012/11/aut_1.jpg)](http://bosch-solar-storage.com/wp-content/uploads/2012/11/aut_1.jpg)
Source: http://bosch-solar-storage.com/independence/self-reliance/

[![Energy consumption and PV production in Sidney, Australia.](http://www.solarchoice.net.au/blog/wp-content/uploads/Average-NSW-household-in-summer-electricity-consumption-vs-PV-generation1.JPG)](http://www.solarchoice.net.au/blog/wp-content/uploads/Average-NSW-household-in-summer-electricity-consumption-vs-PV-generation1.JPG)
Source: http://www.solarchoice.net.au/blog/home-energy-consumption-versus-solar-pv-generation/

[![Energy consumption and PV production in the US](http://blogs-images.forbes.com/jamesconca/files/2014/11/SolarGrid.jpg)](http://blogs-images.forbes.com/jamesconca/files/2014/11/SolarGrid.jpg)
Source: Edison Foundation Institute for Electric Innovation, via http://www.forbes.com/sites/jamesconca/2014/11/28/net-energy-metering-are-we-capitalists-or-what/

[![Individual household load profiles](http://www.pv-magazine.com/typo3temp/pics/11071_Individual_household_load_profiles_3sppdf_431ed866aa.jpg)](http://www.pv-magazine.com/typo3temp/pics/11071_Individual_household_load_profiles_3sppdf_431ed866aa.jpg)
Source: http://www.pv-magazine.com/archive/articles/beitrag/storage-has-landed-_100009059/501/#axzz3YryioctT





Interested in reading more articles like this? Follow us [on Facebook](https://www.facebook.com/duurzaamheidsweb), or through our [Atom-feed](/feeds/all.atom.xml).



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


[^redoxflow]:
*It is unlikely that the main role of Tesla Energy will be to provide battery power storage on the scale of entire countries, [...] A problem like that is best solved with a mix of approaches and technologies. Certainly, Tesla's Li-ion batteries may play a role, as will expansion of pumped storage and use of other battery technologies such as redox flow.*   

[^customsolution]:
*But a more important point is perhaps this: Tesla is the first company to offer and market battery storage not as a custom niche-market solution, but rather as a mass-produced consumer appliance that should "just work".*   
Of course, a PV-installation with battery storage *is* actually a highly customised product. There is no "one size fits all" solution, because every location is different in terms of latitude, orientation, weather patterns, construction, electrical installation and electricity use. You will always need someone with specialised knowledge to design and install the system. But this is not the point. Tesla's batteries will allow battery storage to be offered as a regular and fairly affordable option with new (and existing) PV-installations, rather than as a costly solution only to be applied in special cases.

