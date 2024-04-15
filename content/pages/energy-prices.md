Title: Energy prices over time
Authors: Levien van Zon
Date: 2017-02-16
Tags: energy
Slug: energy-prices
Status: hidden

[![crude oil price 1860-2015]({static}/images/oilprice-1860-2015.png)]({static}/images/oilprice-1860-2015.png)

The global price of a litre of crude oil from 1860 to 2015. Historical prices are inflation-corrected and are expressed in 2015 US dollars, for fair comparison. Data source: [BP Statistical Review of World Energy, June 2016](http://www.bp.com/statisticalreview).

   - [SVG-figure]({static}/images/svg/oilprice-1860-2015.svg)
   - [Data as CSV](https://raw.githubusercontent.com/lvzon/energydata/master/energyprices/crude-oil-price-inflation-corrected.csv)
   - [R-script use to generate plot](https://github.com/lvzon/energydata/blob/master/energyprices/plot-oil-price-timeseries.r)

For comparison, we can look at other fuels as well. The following figures shows energy prices for crude oil, natural gas and coal after 1970:

[![energy prices 1970-2015]({static}/images/fuelprices-1970-2015.png)]({static}/images/fuelprices-1970-2015.png)

These prices are in US dollarcents per kWh, and are not inflation-corrected. Unfortunately there seems to be no general measure for the global prices of natural gas and coal, and regional price variation is much larger than for crude oil. For the above figure, I used US indices (the [Henry Hub](https://en.wikipedia.org/wiki/Henry_Hub) price for gas, and the US Central Appalachian coal spot price index). The data is based on the [BP Statistical Review of World Energy, June 2016](http://www.bp.com/statisticalreview).

You can clearly see that, at least in the United States, [primary energy](https://en.wikipedia.org/wiki/Primary_energy) derived from coal and gas has been cheaper in recent decades than primary energy derived from oil. The recent drop in gas and oil prices has been driven mostly by the exploitation of shale gas and oil in the United States, which significantly increased the global supply and made coal a much less competitive energy source with regard to price.

The full procedure for deriving the timeseries-data in these graphs is described in an [iPython notebook](https://github.com/lvzon/energydata/blob/master/energyprices/energyprices.ipynb), which is available in our [git repository](https://github.com/lvzon/energydata).

Interestingly, the price of electricity isn't influenced much by the primary energy prices and has generally been increasing over time in most countries. In the US for example, the average retail electricity price has [fluctuated roughly around 9 dollarcents per kWh since the 1960s](http://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0810), and it hasn't really decreased since 2002.

In Europe, [retail electricity prices tend to be somewhat higher](http://ec.europa.eu/eurostat/statistics-explained/index.php/Electricity_price_statistics), on average above 15 eurocents per kWh and rising to above 20 eurocents per kWh in recent years:

[![EU energy prices since 2008, in euro per kWh]( http://ec.europa.eu/eurostat/statistics-explained/images/e/ec/Evolution_of_EU-28_and_EA_electricity_prices_for_household_consumers_%28EUR_kWh%29.png)](http://ec.europa.eu/eurostat/statistics-explained/index.php/File:Evolution_of_EU-28_and_EA_electricity_prices_for_household_consumers_(EUR_kWh).png)

While most electricity is still generated from fossil fuels, it's price is generally not directly linked to the price of fossil fuels, and includes a tax-component [that may differ greatly between countries](http://ec.europa.eu/eurostat/statistics-explained/index.php/File:Electricity_prices_for_household_consumers,_2016s1_(EUR_kWh).png). It makes sense that electricity is more expensive than [primary energy](https://en.wikipedia.org/wiki/Primary_energy) from fossil fuels, as a significant amount of energy is lost when converting fossil fuels to electricity and in transporting this electricity to the end-user. Moreover, the cost of electricity should also cover (at least in part) the investments in and maintenance of infrastructure such as electricity generators (traditional power stations as well as renewable energy sources) and the electricity grid itself.
 

