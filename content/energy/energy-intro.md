Title: On Energy, part 1: How much do we use?
Authors: Levien van Zon
Date: 2016-10-20
Tags: energy
Slug: energyseries-intro
Status: draft

**By Levien van Zon**


This started off as a short article.   
Back in the spring of 2015, I wanted to write something about the Tesla Powerwall. This battery for home energy storage had just been announced by Elon Musk, and it was the hype of the solar energy world. Unfortunately, not much information was available on its specifications at that time. So I decided I'd write about energy storage more generally. I started to research the subject, and things got a little bit out of hand. The thing is, in order to figure out what batteries can and cannot do, I had to look at the numbers: How much energy do we actually use? And how much solar panels and batteries would we need to supply us with solar energy when there is little sunlight? How much do we need for a night, or a few grey days, or for *all of winter*? The numbers turned out to be problematic. I realised that neither the Tesla batteries nor any operational battery technology comes close to solving the sustainable energy problem: how to supply the Western world with non-fossil energy throughout the year. So I started looking into other types of energy storage as well, and into various types of sustainable energy sources. In doing so, I realised that I couldn't write all this down in a single article, I'd need an entire article series!

So, welcome to the first part in a series of articles on energy use and the transition to sustainable energy. These articles are the outcome of a research project that is still ongoing. This research has already led me to some conclusions that I did not expect, and through these articles I hope to share my insights with others. Things might get slightly technical at times, but you can safely skip such sections, as I will try to recap the important points at the end of each article. There will also be numbers. I will try to explain without numbers where I can, but the numbers are actually crucial. The energy problem, as we shall see, is mainly a problem of scale, and scale is determined by numbers. Specifically, big numbers.

#### A brief history of energy

We live in a rather unique period in history. Humanity has never had as much energy at its disposal as we have now, and never has this energy been as cheap as it has been over the last century or so. Granted, energy prices have fluctuated quite a lot during this period, as you can see in the oil price chart below. As recently as 2011, crude oil was at an almost historic high. At $0.74 per litre, the price for oil in 2011 was more than ten times that in 1970! But we easily forget that oil actually contains *a lot* of energy. A convenient measure of energy is the kilowatt-hour (kWh), which I will explain in a bit, but which you may recognise from your electricity bills. A litre of oil contains roughly 10 kWh of energy, so even the extremely high 2011 oil price translates to a mere 7 dollarcents per kWh, which, in the grand scheme of things, is really not that much.[^energyprices] 

![]({filename}/images/oilprice-1860-2015.png)

*The global price of a litre of crude oil from 1860 to 2015. Historical prices are inflation-corrected and are expressed in 2015 US dollars, for fair comparison. Source: [BP Statistical Review of World Energy, June 2016](http://www.bp.com/statisticalreview)*

Fact is that *we all have become rather dependent on energy being so cheap*, because we use an incredible amount of it, especially in industrialised countries. In many ways, this abundance of cheap energy is a good thing. Energy quite literally powers everything we do. Things like food production, transport, heating and cooling become a lot easier and cheaper with abundant energy, and modern communication wouldn't even be possible without it. So what exactly is the problem? 

Take a look at the following graph, which shows how much energy we humans use per day, and where it comes from, from 1800 until the present day. (The energy is expressed in terawatt-hours, which I shall explain in a moment.)

![]({filename}/images/energy-timeseries-total-per-day.png)

Until about 1850, people mostly used biomass (stuff directly derived from plants or animals) as an energy source. Things like cooking, heating and lighting were done using wood, charcoal, peat, dung and whale-oil. Transport and agriculture were mostly powered by animals, mainly horses, mules and cattle. Wind and water played an important role as well, in industry (think windmills and watermills) and in long-distance transport (think sailing ships).

By 1850 the Industrial Revolution was well on its way. The Industrial Revolution was as much about technical innovation as it was about social change and energy transition: The technological developments were intimately tied to the availability of cheap labour and the large-scale mining of fossil coal. Having said that, the use of coal was still mostly limited to cities, to industry and to steam locomotives and ships. In 1850, firewood was still and by far the most important energy source for humanity. 

By 1900, the use of coal had grown to be more or less equal to the use of biomass. The half-century that followed saw a further increase in the use of coal for industry, heating and transport. It also saw the slow expansion of car use and the development of aeroplanes. The two World Wars were an important driver for technological development and the expansion of fossil fuel mining.  

By the end of World War II, the energy provided by coal had doubled and was almost twice the amount provided by biomass. Also, energy derived from natural gas and oil started to become significant, and its use grew extremely rapidly. A mere two decades later, by the 1970s, oil had become the most important energy source, closely followed by coal and gas. This just goes to show how fast the energy landscape can change.

Since 1800, human energy use has increased 28-fold, and 82% of our energy is currently provided by fossil fuels. Of course this enormous increase in global energy use is in part due to the more than seven-fold increase in world population over the last two centuries. If we factor this out and look at the daily energy use *per human*, the increase since 1800 has been somewhat more modest:
	
![]({filename}/images/energy-timeseries-per-person.png)

What you can see here is that the energy consumption *per person* has gone up too: it almost doubled between 1800 and 1950, and has doubled again since then. However, it is clear that most of this second increase actually occured during the 1960s and 70s, with the rise of energy-intensive consumer culture, personal car ownership and comfortable housing for small families, at least in the Western world. In the 1980s and 90s, recession and increases in energy efficiency actually led to a slight *decrease* in personal energy consumption. However, while energy efficiency is still increasing, so is our energy consumption in this age of digital gadgets, datacentres, cheap air travel and increasingly heavy cars. This has led to a renewed increase in personal energy use over the last 15 years.

#### The kWh and other animals

Two centuries ago, in 1800, the average human used just over 16 kWh per day. A century ago this had increased to just over 24 kWh per day. Today, the average person uses around 60 kWh per day. Before we continue, what is this kWh-thing exactly? Well, the technical description would be this: If we take a device that draws 1000 Watts of power (1 kiloWatt), say a decent toaster, 1 kiloWatt-hour (kWh or kW·h) is the amount of *energy* that it will consume in one hour. So kWh is a measure of energy, and a fair amount of energy at that. For people who like standard units: 1 kWh is qual to 3.6 MJ (megaJoules). Let's look at a few examples. 

1 kWh of energy will keep my small 2000 W electrical space heater running for half an hour. It will keep an old-fashioned 40 W lightbulb burning for roughly 24 hours, and it's enough energy to boil a bucket of water.[^waterboiling] However, an average (gasoline) car will only drive around 1 to 1.5 km on 1 kWh of energy.[^carenergy] Being derived from crude oil, a litre of gasoline contains almost 9 kWh of energy (or 33 kWh per gallon). And a cubic metre of natural gas contains around 11 kWh (or 0.3 kWh per cubic foot).[^energycontent]    
Worldwide, an average electrified household uses around 10 kWh of *electricity* per day inside their home, although in Australia and France it's almost double this amount, and in the US and Canada it's easily three time this figure.[^electricityuse] 

And as for the terawatt-hour unit (TWh) I mentioned earlier, 1 TWh is 1 billion kWh. So we humans currently use over 430 billion kWh of energy *per day*. That's a very large number, and therefore a lot of energy. And it begs the question: What do we use all this energy for?

#### Where does all the energy go?

![]({filename}/images/energy-global-production-consumption-2013.png)

The figure above shows where our energy comes from, and what we use it for. Let's take a closer look at it. We already talked a little about where our energy comes from, so we'll start with the right side: Where does the energy go?

For most of us, including myself, this figure reveals a rather stunning surprise: Almost a third (31%) of our energy supply isn't really used for anything! Part of this energy goes into the mining process of fossil fuels. The rest goes into transport and storage, or is lost in conversion: in refining fuels, in converting them to electricity and transporting this electricity. 

Another 10-14% or so of our energy supply (up to three-quarters of the "transport" energy) is lost due to the inefficiency of internal combustion engines. This means that only around half of our energy supply (±55%) is effectively available for use by us humans. And we can probably assume that much of our use of this is also unnecessarily wasteful, but let's ignore that for now (I will talk about that in a later article).

A small fraction, around 6% of our fossil fuel supply, is not used for energy but is used for the production of plastics and other materials. We actually use less than half of our global energy sources (44%, or 24 kWh per human per day) to power all our industry, services, infrastructure, agriculture and our houses. Of this energy, about three quarters is used in the form of heat, and around a quarter is currently used in the form of electricity. A further 5% or so of our global energy supply (roughly 3 kWh per human per day) is effectively used to move stuff and people around (if we don't count the energy lost as heat in combustion engines).

These figures are strange if you think about them for a bit. How can we use only 24 kWh per person per day for almost everything we do, including all our work and infrastructure, if the average electrified home already uses 10 kWh of electricity per day? Also the energy available for transport won't get us very far, perhaps 10 km per person per day, and that's including air traffic. Most of us reading this will travel a lot more on average, as does the stuff we buy. 

The reason for the figures being so low is of course that some people and countries use a lot more energy than others. Most humans live in Asia and Latin America and Africa, where energy use per person is a lot lower than the average depicted here.[^china] Conversely, energy use in regions like North America, Europe and Australia is a lot higher than average. 60 kWh per person per day is not nearly enough to power your average industrialised consumption society. Moreover, countries vary quite a lot in their energy sources:

![]({filename}/images/energy-country-consumption-countries-2013.png)
 
With regard to energy sources, an average person in France or Germany will use more than twice the world average, over 125 kWh per person per day. And that's not even counting the energy needed to make imported products. An average Australian uses over three times the world average, and an American uses more than four times the average. Someone in Central Africa on the other hand, uses only 8.5 kWh per day on average. This is a tiny fraction of the global average, and most of that is actually in the form of firewood for cooking.  

*Africans use 16 kWh/day, while North Americans 258, and Europe is somewhere in the middle.
Also large differences between countries within a given region.
For instance within Africa, most of the energy is used by just a few countries. In Central Africa, energy use is 8.5 kWh/person/day, just over half the continent’s average. But in Chad, Burundi, Eritrea, Mali and Niger, it is under 1 kWh/person/day.
The Netherlands alone uses more oil than the 40+ countries in sub-saharan africa together (minus South Africa and Nigeria), which have 30 times more people.*


So, we've established that much of our energy is actually lost to inefficiencies, and that there are large differences in energy use between regions and countries. Let's go back and look at where our energy comes from. Globally, oil and coal each make up just under a third, and natural gas makes up about a fifth. Together, these fossil fuels make up most (82%) of our energy supply, and nuclear energy provides another measly 5%. The remaining 13-14% or so of energy sources are what we would call renewable energy sources. For most people this immediately conjures up images of windmills and solar panels. In fact, this renewable energy is almost all provided by biomass and various kinds of waste, which form around 10% of total global energy supply. Hydropower contributes another 2.4%, and sources such as geothermal energy provide most of the remainder. Windmills currently provide a rather pathetic 0.3% of the global energy supply, and PV solar panels even less, around 0.1%. PV solar panels currently provide as much energy per person per day as is in a teaspoon of crude oil. This is roughly enough to boil every person on Earth a bit under half a litre of water per day (430 mL to be precise, at least in 2013). That's great if we could live on two cups of tea, but obviously we still have quite some way to go if we want to get rid of fossil fuels, especially if we'd like to power our economies and creature comforts using mostly solar energy and wind power.

*About those regional and country differences: 
In Africa, most energy comes from biomass, mostly wood used for cooking.
In Europe and the US, it’s quite a different picture.
What these countries have in common is that they use a lot of oil, at least double the world average (?), most of which is for transport.
Most use some combination of coal and gas for electricity, heating and industry.
Some exceptions: Lot of nuclear in France, lot of hydro power in Norway (provides most of the “green” electricity in Northern Europe), lot of natural gas in NL (has to do with greenhouses).
US just uses a lot of everything.
Another thing most of these countries have in common is the small contribution of renewable energy. Norway has a lot of hydro and some wind, but together this still makes up only a third of its energy use. In most other countries, this figure is a lot lower, and most of the “renewable” energy comes from biomass.
Even Germany, often hailed as the renewable energy miracle, actually only gets 3% of its energy from wind, solar and hydro power.
Dismally low figure in relatively wealthy countries such as NL (0.7%) and UK (1.5%)
Spain, currently one of the poorest nations in Western Europe, does relatively well, and is actually the European leader in solar energy with almost 2 kWh per person per day (2.4%)*



It is not uncommon these days for policy makers and politicians to boast about the growth of the renewable energy sector in their countries. However, the above figure shows some things that we rarely hear about. Germany and Norway are often praised for being frontrunners in renewable energy. However, if we look at fossil energy use per person, both countries actually do rather badly compared to some of their European neighbours. A German uses twice the world average in fossil fuels, a Norwegian even more. In Europe, only the Netherlands and Luxemburg do worse when it comes to fossil fuels used per person. The average Frenchman or Spaniard or Greek actually does a lot better when it comes to fossil fuel use: at or slightly above the world average. And Spain in particular does quite well when in comes to non-biomass renewable energy: 9% of its energy supply already comes from wind energy, hydro power, thermal solar power and PV solar power. The expansion of renewable energy sources in countries like Germany and Denmark is certainly important, but their contribution is still tiny relative to fossil fuel use. If we really want to make progress, perhaps we should start ranking countries according to how much fossil energy they still use per inhabitant, rather than by the fraction of electricity generated by biomass, windmills and solar panels, which tends to make things look better than they really are.



*With regard to Spain: Only Denmark has a higher percentage of wind power (5.4%), and Spain uses more solar energy per person (2.4%, almost 2 kWh/day) than Germany (1%, 1.3 kWh/day), although most of it is thermal rather than electrical.* 

TODO: check Switzerland, Austria, Finland, Sweden, Belgium, Luxemburg, and mark hydro separately for Spain
Should we add Denmark as well?


*So, what do we learn from this? Firstly, we use a lot of energy, especially in "developed" nations. Why? We use/need energy to drive to work, to the supermarket, drive the children to/from school, drive or fly to our holiday destinations, build roads, build houses and offices, heat them, cool them, run computers and servers, farm food, transport food, store food, and produce the mountains of other stuff we constantly buy. In a small village in Africa, South America or Asia, this will probably be a different story.*

*Second, almost all of this comes from fossil fuels, with only a few exceptions. Almost none is provided directly by solar or wind. Especially solar lags behind: world-wide, less than a percent, and for western countries, even the leading ones, it is rarely more.* 

*Third, we waste most of our energy, almost certainly more than half, probably closer to 75%. Most losses occur in energy conversion and in the transport sector, but large efficiency gains are possible in industry and houses and offices as well. As losses are so significant, if we manage to reduce energy losses and waste, we'd be well on our way to slash our energy consumption.*

*Fourth, most of our energy is used in the form of heat, while sustainable energy efforts tend to be more focussed on electricity. Understandable, as you can easily convert electricity into heat. But it's a bit of a waste: electricity is hard to come by, while heat is relatively easy to come by, it is a by-product of nearly everything. Also, compared to electricity, it is relatively easy to store, although it is much harder to transport. More on the role of heat energy in later articles.*

*It seems that there is plenty of room for improvement, right?
In the next article I will examine the potential for non-fossil energy sources.*

----

[^energyprices]:
The problem is of course that converting one form of energy to another always implies losses. The 10 kWh of energy that is in a litre of oil can only be fully extracted in the form of heat. If you take the energy in oil or coal or natural gas and convert it into electricity, you'll a quarter to a third of the energy in the conversion process, possibly even more. Still, in many countries electricity is also relatively cheap. In the US the [average electricity price](http://www.eia.gov/electricity/data/browser/#/topic/7?agg=0,1&geo=vvvvvvvvvvvvo&endsec=vg&freq=A&start=2001&end=2015&ctype=linechart&ltype=pin&rtype=s&pin=&rse=0&maptype=0) is only slightly over 10 dollarcents per kWh (a bit more for residential use). While oil was expensive in 2011, [this comparison of 2011 electricity prices](https://www.ovoenergy.com/guides/energy-guides/average-electricity-prices-kwh.html) shows that the relative cost of electricity (adjusted for purchasing power) was below 12 dollarcents per kWh in Canada, China and the US. Electricity is generally generated from coal and natural gas, the price of which is linked to oil prices but only loosely. Electricity prices are therefore typically not a very good refection of oil prices, or even fossil fuel prices. Moreover, readers who have followed [recent developments in solar energy costs](http://www.pv-magazine.com/news/details/beitrag/abu-dhabi--three-world-record-bids-entered-for-sweihan-solar-project_100026191) will have noticed that the cost for solar-generated electricity has recently dropped below 3 sollarcents per kWh for some projects in the Middle East. 

[^waterboiling]:
Actually 10.75 L, starting from room temperature.
Starting from 20 degrees and assuming 1 kg of water per L and 4186 J per g per degree: 334.880 
Assuming a standard bathtub volume of around 160-170 L (42 gallons in the US).

[^carenergy]:
1:15 in NL
25 MPG in US (http://www.autonews.com/article/20150604/OEM05/150609925/average-u.s.-mpg-edges-up-to-25.5-in-may)
say 10 kWh in 1L, so 1.5 km per kWh
40.2 km on 3.8 L is 1:10.6, or 1.1 km per kWh

[^energycontent]:
 - Gasoline: 
   - 8.8 kWh/L
   - http://hypertextbook.com/facts/2003/ArthurGolnik.shtml
 - Gas: 
   - Depends somewhat on region, around 10.6 (10.3-11.4) kWh/m3
   - 1000 BTU or 0.29 kWh per cubic ft
   - http://hypertextbook.com/facts/2002/JanyTran.shtml


[^electricityuse]:
 - NL: 8 https://www.nibud.nl/consumenten/energie-en-water/
 - US: 30 https://www.eia.gov/tools/faqs/faq.cfm?id=97&t=3
 - FR: 17 http://shrinkthatfootprint.com/average-household-electricity-consumption

[^china]:
Of course, there are some exceptions, such as China. Moreover, absolute energy use is still rather high for Asia and Latin America, simply because so many people live there. As people in the West often point out, China is the world's biggest emitter of greenhouse gases, as well as the world's biggest consumer of coal. This is true, but in fact most of this energy is used for making export products. And even if we would count everything as domestic energy use, the population of China is so big that it comes down to only around 72 kWh per person per day, just above world average but well below the energy use of European countries. 


