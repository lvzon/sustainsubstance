Title: On Energy, part 1: How much do we use?
Authors: Levien van Zon
Date: 2016-11-02
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

Two centuries ago, in 1800, the average human used just over 16 kWh per day. A century ago this had increased to just over 24 kWh per day. Today, the average person uses around 60 kWh per day. Before we continue, what is this kWh-thing exactly? Well, the technical description would be this: If we take a device that draws 1000 Watts of power (1 kiloWatt), say a decent toaster, 1 kiloWatt-hour (kW·h or kWh) is the amount of *energy* that it will consume in one hour. So kWh is a measure of energy, and a fair amount of energy at that. For people who like standard units: 1 kWh is qual to 3.6 MJ (megaJoules). Let's look at a few examples. 

**TODO:** Make a figure which shows what a kWh is, what you can do with 1 kWh, how much energy is in some other fuels, how much is used for some common activities (driving a car, powering a house, average daily use).

1 kWh of energy will keep my small 2000 W electrical space heater running for half an hour. It will keep an old-fashioned 40 W lightbulb burning for roughly 24 hours, and it's enough energy to boil a bucket of water.[^waterboiling] However, an average (gasoline) car will only drive around 1 to 1.5 km on 1 kWh of energy.[^carenergy] Being derived from crude oil, a litre of gasoline contains almost 9 kWh of energy (or 33 kWh per gallon). And a cubic metre of natural gas contains around 11 kWh (or 0.3 kWh per cubic foot).[^energycontent]    
Worldwide, an average electrified household uses around 10 kWh of *electricity* per day inside their home, although in Australia and France it's almost double this amount, and in the US and Canada it's easily three time this figure.[^electricityuse] 

And as for the terawatt-hour unit (TWh) I mentioned earlier, 1 TWh is 1 billion kWh. So we humans currently use over 430 billion kWh of energy *per day*. That's a very large number, and therefore a lot of energy. Then again, there are over 7 billion of us on this planet, so we are a lot of people. That's why it's so useful to look at the energy use per person. But the figure of 60 kWh per person per day can actually be misleading. This is the *average* energy use of a human being, but if you're reading this, there's a very large probability that you are not average. If you live in an industrialised "Western" country, say somewhere in North America, Europe or Australia or New Zealand, you probably use quite a bit more energy than those 60 kWh per day.

#### We are not average

As you can see in this figure, countries vary quite a lot in how much energy they use and where they get it from:


<div style="display: block; margin: 30px 0; width: 80vw; margin-left: 50%; -webkit-transform: translateX(-50%); -moz-transform: translateX(-50%); -ms-transform: translateX(-50%); -o-transform: translateX(-50%); transform: translateX(-50%);">

<img src="{filename}/images/energy-country-consumption-countries-2013.png" />

</div>


**TODO:**
   - Create a full ranking graph of primary energy consumption, using IEA-data
      - Make Python-script to extract and convert IEA data from spreadsheet table (TPES for various energy sources)
      - Extract TPES (and TPES/person?) from the indicator tables in the IEA PDF. Either manually, or transform PDF, or find data online. 
      - Manually add data estimates for China, India and regions (Latin America, North America, Europe, Middle East, North/South/Central Africa) if needed
      - Plot in R or Python and show in extras: total daily primary consumption per person in kWh and absolute in TWh, based on full data, ranked with biggest first
      - Plot in R or Python and show in extras: same with subdivisions in colour for various energy sources, based on free data subset (+ some extra estimates?)
      - Show subset of data in text? (main regional averages, OECD countries, several countries with very low figures) 
   - Point out average, most countries are below this, some are (far) above (up to 4x).
      - An average person in France, Germany, Japan or New Zealand will use more than twice the world average, over 125 kWh per person per day.
      - An average Australian, Korean, Norwegian or Swede uses close to three times the world average.
      - An American or Canadian uses close to four times the average.
      - Most humans however do not live in North America, Europe or Australia. Over three quarters of humanity lives in Asia (ca. 51.7%), Africa (15.5%) and Latin America (8.6%). 
      - But energy use per person is a lot lower there than the average (around 40 kWh/person/day in Latin America and Asia, roughly half that figure for Africa and Asia minus China).
      - And within regions there are large differences. Asians use 40 kWh/person/day, but if you leave out China the average drops to 22, and in a country like Bangladesh it's only 7. Africans use 21 kWh/day, but someone in Central Africa uses only 8.5 kWh per day on average. In Eritrea, Mali and Niger, average energy use is under 5 kWh/person/day, in South Sudan and Burundi it's around 2 and in Chad it's even less, just over 1 kWh/person/day. And most of that is actually biomass, in the form of firewood for cooking.
      - On the other extreme: the US by itself houses a mere 4.4% of the world population (less than Bangladesh and Pakistan combined), but uses over 16% of the world energy supply (Bangladesh and Pakistan together use 0.9%, at 4.7% of the world's population).
      - China and India are often mentioned as big users of fossil energy. And indeed, they use a lot of energy compared to other *countries*, but they're also a lot bigger than any other country: together they house well over a third (37%) of the world's people. China, which uses just over a fifth of the world's energy supply (22%). But it also houses around a fifth of the world's population (19%), which means that energy use per person is actually only just above average in China (61 to 71 kWh/person/day, depending on the source). India  has almost as many inhabitants as China (18% of world population), but its energy use is well below average, at 19 kWh/person/day, and it uses less than 6% of the world's energy supply. And especially in China most of the energy is used for export to Western countries (more than two-thirds, close to 70% of energy consumption is for industry). 
   - Show more detailed graph for a subset of countries, with energy sources.
   - Point out some similarities between "industrialised" countries: oil for transport, mostly fossil fuel for electricity and heat production (coal or nuclear and increasingly gas for electricity, will talk a bit more about industry and electricity vs. heat in next article).
      - There are large differences between countries, but we can see that the European and North American countries shown here all have one thing in common: they use more energy thann the world average, and they use at least twice as much oil. 
      - The Netherlands alone uses more oil than the 40+ countries in sub-saharan africa together (minus South Africa and Nigeria), which have 30 times more people.
   - Some exceptions: countries with hydro-electricity (Norway, Switzerland, Austria), although almost always low percentage of total energy use, and countries with geothermal (Iceland).
   - Percentage of "renewable" energy includes a lot of biomass. If you leave that out, things look pretty bad for most countries. Especially solar energy lags behind, both globally and nationally. In Europe, the frontrunner is actually Spain, rather than Germany.
   - There is a lot to be improved. Solar is growing rapidly, which is good, but it has to grow faster if it is to make any impact the coming decade. 
   - So what *is* the problem? 
      - We are very dependent on fossil fuels, especially in the west.
      - Fossil is a finite resource, with volatile prices. 
      - It generates most of our CO2-emissions.
      - If we want to transition western countries to renewables, we still have a long way to go.
   - Lessons learnt: 
      - We use a lot of energy, mostly from fossil.
      - The widespread use of fossil fuels was established esp. in the 60s and 70s.
      - Energy use in western countries (per person) is much higher than elsewhere.
      - Most renewable energy comes either from biomass, waste or hydro-power. 
      - Especially with regard to solar power, there is *a lot* of room for improvement.

Most humans live in Asia and Latin America and Africa, where energy use per person is a lot lower than the average depicted here.[^china] Conversely, energy use in regions like North America, Europe and Australia is a lot higher than average. 60 kWh per person per day is not nearly enough to power your average industrialised consumption society. Moreover, countries vary quite a lot in their energy sources:

 
With regard to energy sources, an average person in France or Germany will use more than twice the world average, over 125 kWh per person per day. And that's not even counting the energy needed to make imported products. An average Australian uses over three times the world average, and an American uses more than four times the average. Someone in Central Africa on the other hand, uses only 8.5 kWh per day on average. This is a tiny fraction of the global average, and most of that is actually in the form of firewood for cooking.  

*Africans use 16 kWh/day, while North Americans 258, and Europe is somewhere in the middle.
Also large differences between countries within a given region.
For instance within Africa, most of the energy is used by just a few countries. In Central Africa, energy use is 8.5 kWh/person/day, just over half the continent’s average. But in Chad, Burundi, Eritrea, Mali and Niger, it is under 1 kWh/person/day.
The Netherlands alone uses more oil than the 40+ countries in sub-saharan africa together (minus South Africa and Nigeria), which have 30 times more people.*


Globally, oil and coal each make up just under a third, and natural gas makes up about a fifth. Together, these fossil fuels make up most (82%) of our energy supply, and nuclear energy provides another measly 5%. The remaining 13-14% or so of energy sources are what we would call renewable energy sources. For most people this immediately conjures up images of windmills and solar panels. In fact, this renewable energy is almost all provided by biomass and various kinds of waste, which form around 10% of total global energy supply. Hydropower contributes another 2.4%, and sources such as geothermal energy provide most of the remainder. Windmills currently provide a rather pathetic 0.3% of the global energy supply, and PV solar panels even less, around 0.1%. PV solar panels currently provide as much energy per person per day as is in a teaspoon of crude oil. This is roughly enough to boil every person on Earth a bit under half a litre of water per day (430 mL to be precise, at least in 2013). That's great if we could live on two cups of tea, but obviously we still have quite some way to go if we want to get rid of fossil fuels, especially if we'd like to power our economies and creature comforts using mostly solar energy and wind power.

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


