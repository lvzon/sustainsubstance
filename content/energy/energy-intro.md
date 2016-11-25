Title: On Energy, part 1: How much do we use?
Authors: Levien van Zon
Date: 2016-11-02
Tags: energy
Slug: energyseries-intro
Status: draft

**By Levien van Zon**


This started off as a short article.   
Back in the spring of 2015, I wanted to write something about the Tesla Powerwall. This battery for home energy storage had just been announced by Elon Musk, and it was the hype of the solar energy world. Unfortunately, not much information was available on its specifications at that time. So I decided I'd write about energy storage more generally. I started to research the subject, and things got a little bit out of hand. The thing is, in order to figure out what batteries can and cannot do, I had to look at the numbers: How much energy do we actually use? And how much solar panels and batteries would we need to supply us with solar energy when there is little sunlight? How much do we need for a night, or a few grey days, or for *all of winter*? The numbers turned out to be problematic. I realised that neither the Tesla batteries nor any operational battery technology comes close to solving the problem of sustainable energy, that problem being: How can we supply the world, especially northern countries, with non-fossil energy throughout the entire year? So I started looking into more types of energy storage, and into various types of sustainable energy sources. In doing so, I realised that I couldn't write all this down in a single article, I'd need an entire article series!

So, welcome to the first part in a series of articles on energy use and the transition to sustainable energy. These articles are the outcome of a research project that is still ongoing. This research has already led me to some conclusions that I did not expect, and through these articles I hope to share my insights with others. Things might get slightly technical at times, but you can safely skip such sections, as I will try to recap the important points at the end of each article. There will also be numbers. I will try to explain without numbers where I can, but the numbers are actually crucial. The energy problem, as we shall see, is mainly a problem of scale, and scale is determined by numbers. Specifically, big numbers.

#### A brief history of energy

We live in a rather unique period in history. Humanity has never had as much energy at its disposal as we have now, and never has this energy been as cheap as it has been over the last century or so. Granted, energy prices have fluctuated quite a lot during this period, as you can see in the oil price chart below. As recently as 2011, crude oil was at an almost historic high. At $0.74 per litre, the price for oil in 2011 was more than ten times that in 1970! But we easily forget that oil actually contains *a lot* of energy. A convenient measure of energy is the kilowatt-hour (kWh), which I will explain in a bit, but which you may recognise from your electricity bills. A litre of oil contains roughly 10 kWh of energy, so even the extremely high 2011 oil price translates to a mere 7 dollarcents per kWh, which, in the grand scheme of things, is really not that much.[^energyprices] 

![]({filename}/images/oilprice-1860-2015.png)

*The global price of a litre of crude oil from 1860 to 2015. Historical prices are inflation-corrected and are expressed in 2015 US dollars, for fair comparison. Source: [BP Statistical Review of World Energy, June 2016](http://www.bp.com/statisticalreview)*

Fact is that *we all have become rather dependent on energy being so cheap*, because we use an incredible amount of it, especially in industrialised countries. In many ways, this abundance of cheap energy is a good thing. Energy quite literally powers everything we do. Things like food production, transport, heating and cooling become a lot easier and cheaper with abundant energy, and modern communication wouldn't even be possible without it. So what exactly is the problem? 

Take a look at the following graph, which shows how much energy we humans use per day, and where it comes from, from 1800 until the present day. (These are estimates of energy, expressed in terawatt-hours, a unit which I shall explain in a moment.)

![]({filename}/images/energy-timeseries-total-per-day.png)

Until about 1850, people mostly used biomass (stuff directly derived from plants or animals) as an energy source. Things like cooking, heating and lighting were done using wood, charcoal, peat, dung and whale-oil. Transport and agriculture were mostly powered by animals, mainly horses, mules and cattle. Wind and water played an important role as well, in industry (think windmills and watermills) and in long-distance transport (think sailing ships).

By 1850 the Industrial Revolution was well on its way. The Industrial Revolution was as much about technical innovation as it was about social change and energy transition: The technological developments were intimately tied to the availability of cheap labour and the large-scale mining of fossil coal. But the use of coal was still mostly limited to cities, to industry and to steam locomotives and ships. In 1850, firewood was still and by far the most important energy source for humanity. 

By 1900, the use of coal had grown to be more or less equal to the use of biomass. The half-century that followed saw a further increase in the use of coal for industry, heating and transport. It also saw the slow expansion of car use and the development of aeroplanes. The two world wars were an important driver for technological development and the expansion of fossil fuel mining.  

By the end of World War II, the energy provided by coal had doubled again and was almost twice the amount provided by biomass. Also, energy derived from natural gas and oil started to become significant, and its use grew extremely rapidly. A mere two decades later, by the 1970s, oil had become the most important energy source, closely followed by coal and gas. This just goes to show how fast the energy landscape can change.

Since 1800, human energy use has increased 28-fold, and 82% of our energy is currently provided by fossil fuels. Of course this enormous increase in global energy use is in part due to the more than seven-fold increase in world population over the last two centuries. If we factor this out and look at the daily energy use *per human*, the increase since 1800 has been somewhat more modest:
	
![]({filename}/images/energy-timeseries-per-person.png)

What you can see here is that the energy consumption *per person* has gone up too: it almost doubled between 1800 and 1950, and has doubled again since then. However, we can see that most of this second increase actually occured during the 1960s and 70s. This period saw the rise of energy-intensive consumer culture, personal car ownership and comfortable housing for small families, at least in the Western world. In the 1980s and 90s, recession and increases in energy efficiency actually led to a slight *decrease* in personal energy consumption. And energy efficiency is still increasing, but unfortunately so is our energy consumption in this age of digital gadgets, datacentres, cheap air travel and increasingly heavy cars. This has led to a renewed increase in personal energy use over the last 15 years.

#### The kWh and other animals

Two centuries ago, in 1800, an average human was estimated to use just over 16 kWh per day. A century ago this had increased to just over 24 kWh per day. Today, the average person uses around 60 kWh per day. Before we continue, what is this kWh-thing exactly? Well, the technical description would be this: If we take a device that draws 1000 Watts of power (1 kiloWatt), say a decent toaster, 1 kiloWatt-hour (kW·h or kWh) is the amount of *energy* that it will consume in one hour. So kWh is a measure of energy, and a fair amount of energy at that. For people who like standard units: 1 kWh is qual to 3.6 MJ (megaJoules). Let's look at a few examples. 

**TODO:** Make a figure which shows what a kWh is, what you can do with 1 kWh, how much energy is in some other fuels, how much is used for some common activities (driving a car, powering a house, average daily use).

1 kWh of energy will keep my small 2000 W electrical space heater running for half an hour. It will keep an old-fashioned 40 W lightbulb burning for roughly 24 hours, and it's enough energy to boil a bucket of water.[^waterboiling] However, an average (gasoline) car will only drive around 1 to 1.5 km on 1 kWh of energy.[^carenergy] Being derived from crude oil, a litre of gasoline contains almost 9 kWh of energy (or 33 kWh per gallon). And a cubic metre of natural gas contains around 11 kWh (or 0.3 kWh per cubic foot).[^energycontent]    
Worldwide, an average electrified household uses around 10 kWh of *electricity* per day inside their home, although in Australia and France it's almost double this amount, and in the US and Canada it's easily three time this figure.[^electricityuse] 

And as for the terawatt-hour unit (TWh) I mentioned earlier, 1 TWh is 1 billion kWh. So we humans currently use over 430 billion kWh of energy *per day*. That's a very large number, and therefore a lot of energy. Then again, there are over 7 billion of us on this planet, so we are a lot of people. 

I've been talking about this figure of 60 kWh per person per day, but actually that's a bit misleading. This is the *average* energy use of a human being, but very few people are average human beings. In fact, most humans use less energy than average. But if you're reading this, chances are that you don't belong to this group. In fact, you probably use quite a bit more energy than average.


#### We are not average

As you can see in this figure, countries and regions vary quite a lot in how much energy they use per person:

![]({filename}/images/energy-tpes-iea-2014-kwh-person-day.png)

The red bar in this figure is the average worldwide energy use. Most countries above it are either relatively wealthy, or they have a lot of industry or oil reserves. Most countries below it are lower-income countries. And most people live in low-income countries. In fact, three quarters of humanity lives in Asia (around 51.7%), Africa (15.5%) and Latin America (8.6%). Asians use 40 kWh/person/day, but if you leave out China the average drops to 22, and in a country like Bangladesh it's only 7. Africans use 21 kWh/person/day, but someone in Central Africa uses only 8.5. In Eritrea, Mali and Niger, average energy use is under 5 kWh/person/day, and in South Sudan, Burundi and Chad it's even less. And most of the energy used in Africa is actually firewood for cooking. It seems that there is a strong relationship between "development" and energy use. A minority of humans use most of the world's energy supply, while most people still use as much energy or less as humanity did a century ago.


There's a few things to notice here. The red bar is the average worldwide energy use. Most countries shown in this figure that are above it are either industrialised countries or countries that have oil reserves. But most people don't live there, in fact over three quarters of humanity lives in Asia (around 51.7%), Africa (15.5%) and Latin America (8.6%). In all of these regions, average energy use is well below 60 kWh per person per day. Asians use 40 kWh/person/day, but if you leave out China the average drops to 22, and in a country like Bangladesh it's only 7. Africans use 21 kWh/person/day, but someone in Central Africa uses only 8.5, and in Eritrea, Mali and Niger, average energy use is under 5 kWh/person/day! In South Sudan, Burundi and Chad it's even less, and most of that is actually firewood for cooking. Many people still uses as much energy or less as humanity did a century ago.

Now let's look at the countries where people use much more energy than the world average of 60 kWh/person/day. There's places like France, Germany, Japan or New Zealand where people use close to twice as much energy, and an average Australian, Korean, Norwegian or Swede uses almost three times as much, and an average American or Canadian close to four times as much. The countries where energy use per person is highest all have cold winters and/or warm summers and tend to have a relatively low population density. This makes sense, as much of the energy is used for heating, cooling or transportation. Having a large industrial sector also boosts a country's energy use. The industry needed for mining and refining fossil fuels actually consumes a lot of energy, as does the manufacturing industry, especially for manufacturing processes that require high temperatures. China is a good example, it's energy use per person is somewhat above world average, and in absolute terms China is actually the world's biggest energy consumer, because it houses a fifth of the world's population (19%). But over two thirds of that energy is used for industry, most of which is export-oriented. Much of the stuff we buy in the West is made in China, and therefore the energy needed to produce it will also be allocated to China, at least in the figures I'm discussing here.

It should be clear by now that people in industrialised and relatively wealthy countries use a lot more energy than people in poorer and less industrialised countries. As a point in case, the United States are home to a mere 4.4% of the world's population (less than Bangladesh and Pakistan combined), but the US uses over 16% of the world energy supply, while Bangladesh and Pakistan together use only 0.9%. This is a problem for several reasons. It means that the use of energy and other resources tends to go up as countries "develop" and poverty is reduced. And unfortunately, most of this energy tends to come from fossil fuels, of which there is not an endless supply. Moreover, as I discussed in previous articles, fossil fuels are the main source of human greenhouse gas emissions, and our energy use is therefore the main driver of climate change. If we want to reduce greenhouse gas emissions, we need to reduce fossil energy use, but this is not as easy as it may sound. To understand why this is a hard problem, take a look at the following figure, which shows where several countries and regions get their energy from:

![]({filename}/images/energy-tpes-iea-2014-energy-sources.png)

What we see here is that "industrialised" countries are mostly dependent on fossil fuels. Transport relies very heavily on oil, so oil tends to be an important energy source. My tiny home country of The Netherlands by itself already uses more oil than nearly all of the of the 40+ countries in sub-saharan Africa taken together (if we exclude South Africa and Nigeria).   
Natural gas and coal are also very important, as these are the energy sources used widely for industry, heating and for generating electricity. France is one of the few countries where nuclear energy plays a significant role in the energy supply, as France uses almost exclusively uses nuclear power plants for electricity generation, and many houses have electrical heating. And there are a few countries where renewable energy sources are important, mainly hydro-energy. But even in mountainous countries with fairly small populations, such as Norway, Switzerland and Austria, hydro-power covers only third or less of total energy use. In most countries, the main source of renewable energy is still biomass, as it has been for all of human history. And the problem is that we cannot scale up biomass as an energy source, to replace our huge consumption of oil, coal and gas.

<div style="display: block; margin: 30px 0; width: 80vw; margin-left: 50%; -webkit-transform: translateX(-50%); -moz-transform: translateX(-50%); -ms-transform: translateX(-50%); -o-transform: translateX(-50%); transform: translateX(-50%);">

<img src="{filename}/images/energy-country-consumption-countries-2013.png" />

</div>

I will talk a lot about alternative energy sources later on in this series. For now it will suffice to say that solar energy is one of the few energy sources that can conceivably be scaled up sufficiently the coming few decades to cover a large part of our energy consumption. But if that's what we want, we have a very long way to go. Even Germany, often hailed as the renewable energy frontrunner, actually only gets 3% of its energy from wind, solar and hydro power. In the UK this is only 1.5%, and The Netherlands is even worse of, with only 0.7% of its energy being derived from renewable sources outside biomass. On the other hand, Spain, currently one of the poorest nations in Western Europe, does relatively well. Profiting from its relatively sunny climate, Spain is actually the European leader in solar energy at almost 2 kWh per person per day (2.4% of its energy supply). Moreover, 9% of its energy supply already comes from wind energy, hydro power, thermal solar power and PV solar power. France and Spain both have a *fossil* energy consumption that is only slightly above the world average, so they will have a much easier time phasing out coal compared to, say, Germany or the UK. The biggest energy-transition challenge for most countries will be to replace their oil consumption by sustainable energy sources. 

TODO:
 
   - check Denmark, Austria and Switzerland (% renewable energy, esp. hydro and wind)
   - for extra background material, make stacked bar graph with oil/coal/gas/renewable for all/most countries in the 2014 IEA-dataset 
   - draw kWh-cartoon
   - finish main text, write conclusion, rewrite/shorten boring bits: "too much information" or irrelevant bits should be removed, moved to background pages, footnotes or next article
   - finish background pages (with extra figures, source data references and source data/scripts, and extra information based on notes and deleted material).
   - start writing on next article, then publish this one

   - Conclusions: There is a lot to be improved. Solar is growing rapidly, which is good, but it has to grow faster if it is to make any impact the coming decade. 
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


