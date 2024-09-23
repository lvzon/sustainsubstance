Title: Hairballs & Loops - Why understanding the real world is important (but not easy)
Authors: Levien van Zon
Date: 2024-08-27
Tags: complexity
Slug: hairballs-and-loops
Status: draft

Reading time: ca. 15-20 minutes.     


<div style="text-align: center; margin-left: auto; margin-right: auto;">
<img src="{static}/images/small-tangle.jpg" style="width: 25%; height: auto; border: 0px;"/>
</div>


**By Levien van Zon**

Stories are important for how we see the world. In my [first article](https://sustainsubstance.org/beyond-optimists-and-pessimists.html), I argued that stories act as internal models of the world, supercharged by our ability to share them with others. In the [subsequent article](https://sustainsubstance.org/entwined.html) I talked about complexity and about science. I stated that much of our knowledge comes from the pursuit of science, but that its tools have trouble with so-called *complex systems*. Complexity in this context means that there are many interacting parts, which are hard to separate because their interactions are strong and significant.

So far I have been a little vague about a number of things. For instance, what do I mean by "stories", "internal models" and "knowledge"? And what is the nature of "interactions" between the parts of a complex system? In this article, I want to make some of these things a little more concrete. Also, I want to show that complexity isn't just there to make our life difficult, it can actually have an important function.

Let's start with the idea that stories are models of the world. Stories are actually quite complicated things that are closely tied up with the workings of our mind. They are hard to define and they serve many functions. I will leave such complexities aside for now, and focus on a common experience: We generally feel that we *understand* an event, if we can construct a coherent story of how the event was generated.[^mentalmodel]
Such explanatory stories are not always accurate, of course. Our explanation of an event may be quite different from how the event was *actually* generated. But regardless of their accuracy, the collection of cause-and-effect stories that we believe to be true does constitute our *personal knowledge*, our internal model of how the world works.

Because a fair number of our causal beliefs are at best inaccurate and at worst plain nonsense, it is useful for a society to have some way to check our shared beliefs. Science can be seen as a collective human effort to figure out whether cause-and-effect stories (usually called *theories* or *hypotheses*) actually correspond to processes in the real world. And it turns out that this is not at all easy to establish.

The way to test a causal story is usually through experiments. If we change something in a proposed causal chain, we should see a change in the effect. However it is not always possible to perform direct experiments, for instance if we are looking at things that are too small or too big to manipulate, or that are connected to too many other things. Luckily, people have come up with many ingenious and elaborate ways to establish which causes lead to which effects.[^causality] Ideally we are able to figure out the detailed mechanism through which certain things lead to certain other things. Knowing the true (or at least likely) mechanism through which something happens is what we usually regard as "understanding" in the scientific sense. Having such a mechanistic description is very powerful, as it may allow us to control things, and to predict what may happen in the future or in other hypothetical situations.

As I wrote [earlier](https://sustainsubstance.org/entwined.html), the classical scientific approach has difficulty with complex systems, because such systems have many strong interactions between their parts. For instance in the human body or in human society, it is hard to manipulate and study parts in isolation to determine cause-effect-relationships and understand their mechanisms. Isolating parts changes the system. Moreover, cause and effect may not even be well-defined, because there may be causal loops or "feedbacks". Let's look at an actual example to make clear what I mean.

<div style="text-align: center; margin-left: auto; margin-right: auto;">
<img src="{static}/images/greenhouse-foodweb.png" style="width: 100%; height: auto; border: 0px;"/>
</div>

Imagine a small greenhouse containing a simple ecosystem with three kinds of organisms: plants, slugs and hedgehogs. This is a very simple complex system. It is not hard to describe the interactions here: the slugs eat the plants, and the hedgehogs eat the slugs. These interactions are strong in the sense that they are literally a matter of life or death for the parties involved. Hence this system is complex in at least two aspects: interactions are strong and the parts thus behave differently if you separate them. Whether specific interactions are positive or negative depends on our perspective. Clearly the slugs negatively affect the plants, but we can also say that the plants positively affect the slugs (and indirectly the hedgehogs). For an outside observer the two ways of seeing the interaction are more or less equivalent, for the plants and slugs they are not.

While the interactions seem easy to describe here, the behaviour of the system is not so easy to describe in terms of causes and effects. What happens for instance if the slugs eat *all* the plants? There will be a brief explosion of slugs and perhaps hedgehogs, after which all the animals will die of hunger. But while such a slug-armageddon is certainly possible, this little ecosystem can also be perfectly stable. The hedgehogs can keep the slugs in check, giving the plants an opportunity to grow, and the limited number of slugs will in turn limit the hedgehogs. As you can see, there are loops of causality here: the slugs affect the hedgehogs, which in turn affect the slugs, which affects both plants and hedgehogs, and so on. This is an example of circular causality, or what are often called "[feedback loops](https://en.wikipedia.org/wiki/Feedback)".

Feedback loops can be a bit tricky to describe, because there is no clear separation of cause and effect. Do the slugs limit the hedgehogs, or do the hedgehogs limit the slugs? The answer is yes. They limit each other. The relationship between slugs and hedgehogs is an example of what is often called a *negative* (or *balancing*, or *attenuating*) feedback. A familiar example of negative feedback in human engineering is the thermostat, which turns up the heating if it becomes too cold, and turns it down if it becomes too warm. Negative feedback is in many ways positive, because it can prevent things from getting out of hand, so it tends to provide stability.

The other common type of feedback loop is often called *amplifying*, *reinforcing* or simply *positive* feedback. As you will probably have guessed, positive feedback isn't always positive. An example is the "rich get richer" effect: People who have more money, have more opportunities to acquire further wealth than people who have less money. Therefore the rich tend to become richer, and inequality in societies will tend to increase unless active measures are taken to prevent the concentration of wealth and power. Positive feedback is very powerful, it drives exponential growth and can rapidly amplify things. But in the absence of stabilising mechanisms it can easily cause instability. We depend on it for our nervous and immune systems to function (among many other things), and it also drives evolution and economic growth. But it can also lead to economic depression, ecosystem collapse, runaway climate change and social revolutions.

Back to our little greenhouse. Because our "normal" human language is imprecise and has difficulty with circular causation, there is a limit to how well we can describe what goes on in this small system, even though it only contains three species and our story ignores many other things that are also important (for instance, the sunlight, water, nutrients and micro-organisms that are required for the plants to grow). Neither our description nor our picture provides enough information to predict, for instance, whether a given constellation of slugs and hedgehogs will destabilise the system by eating too much. For this, we will need a more precise description of what is going on. One thing we can do in this case is to construct a mathematical model that describes the main interactions between the three species. I will not bother you here with the gory details, you can see what such a model looks like in the footnotes if you're interested.[^gorydetails] Suffice it to say, a mathematical description is much more compact than our descriptive story, and it allows us to make very specific predictions. We can use it to determine how much the animals can eat or how fast the plants need to grow for the system to be stable. In this sense it is a richer description, although to make the mathematics manageable it also leaves out a lot of details that may or may not be important for the questions we ask of it. Like our descriptive story it is a simplification, and in many ways it is a very poor description of what *actually* goes on. All our models, whether stories, pictures, mathematical formulas or computer simulations, are tools for understanding the things that happen in the world. They are necessarily simplifications, and they are never as rich and subtle as the real thing.

Now imagine trying to understand and describe an actual, natural ecosystem that isn't an artificial greenhouse with only three species. [Puget Sound](https://en.wikipedia.org/wiki/Puget_Sound) is an estuary in Washington State, adjacent to the cities of Seattle and Tacoma. This is what it looks like:

<div style="text-align: center; margin-left: auto; margin-right: auto;">
<img src="{static}/images/puget-sound-overview.jpg" style="width: 100%; height: auto; border: 0px;"/>
</div>

And here is a picture of the main species groups and their interactions in the central basin of the Puget Sound ecosystem:

<div style="text-align: center; margin-left: auto; margin-right: auto;">
<img src="{static}/images/ecopath-diagram-puget-sound.png" style="width: 100%; height: auto; border: 0px;"/>
</div>

Good luck. Clearly this is a more complex complex system. Even though it is still much simplified, human language is no longer a very effective tool to describe all the interactions shown here. The picture above actually represents a [computer model](https://www.eopugetsound.org/articles/quantitative-models-including-ecopath-take-food-web-studies-higher-level-analysis), which in turn is based on a mathematical description of relations between groups of species, such as what they eat, and how much.[^ewemodel] These numbers in turn are based on observations and measurements of what actual creatures do. You can probably imagine how much work goes into constructing such a model, and this is not even such a complicated ecosystem, as ecosystems go. Moreover, the model mostly describes relatively big organisms. It lumps the huge diversity of micro-organisms---which constitute an ecosystem onto itself---into a few large groups such as "bacteria" and "phytoplankton".

Now imagine trying to make a model of what goes on in the human body. The Puget Sound ecosystem model describes only 65 species groups. The human body consists of roughly 30 trillion cells of [more than 400 different types](https://en.wikipedia.org/wiki/List_of_human_cell_types), plus another 38 trillion or so [micro-organisms](https://en.wikipedia.org/wiki/Human_microbiome) belonging to more than a thousand different species. Our own cells interact with this personal ecosystem of resident micro-organisms in ways that are probably essential for health but are still poorly understood. Furthermore, the internal workings of our cells depend on more than eighty-thousand different proteins and on a lot of other types of molecules, many of which we don't know about yet. Much of what goes on in our body is decentralised and self-organising, although some of it is coordinated by our nervous system, which has somewhere in the order of 60 trillion neuronal connections. The human body is so mind-bogglingly complex that there is no way that a single person can understand how it all works, exactly. Luckily we don't need to know all the details in order to operate our body. But for medical science this complexity does present somewhat of a problem.

In fact, we almost always see complexity as a problem, and with good reason. If we want to be able to control things, we need to know how they work, at least more or less. If you want a doctor to treat some serious medical condition, it helps a lot if they know what causes the condition, and what roughly happens if you treat it with a certain pharmaceutical drug. Of course trial-and-error can be a perfectly valid approach, but it helps a lot to know mechanisms (and as a patient I would much prefer the latter). And luckily we do know quite a few mechanisms, but figuring these out has taken a gigantic, time-consuming and very costly effort by millions of researchers collecting data and doing experiments for more than a century. And given how much we still don't know, the end of this effort is nowhere near in sight.


<div style="text-align: center; margin-left: auto; margin-right: auto;">
<img src="{static}/images/complexity-tangle-2.jpg" style="width: 100%; height: auto; border: 0px;"/>
</div>

One of the problems is that merely collecting detailed information isn't sufficient for understanding how things work. As science writer Philip Ball points out in his book "[How Life Works](https://how-life-works.philipball.co.uk/)", it clearly isn't the case that all details matter. If *all* details were important, life would be utterly fragile in the face of disturbance and damage. But life is remarkably resilient, so buried somewhere in the endless details there must be robust patterns and processes that keep things running, even under difficult conditions.

If we just collect a lot of details and focus mostly on these, we easily lose sight of the big picture. We risk missing the patterns and processes that actually matter most. The problem is that it isn't always clear where we should look for these "things that matter". For several decades it was believed that for living beings, *genetics* is what matters most. This is an understandable belief: If genes contain the information that we pass on between generations and that gets acted on by evolution, then surely our genome must provide a kind of "blueprint" for how to build an organism? If we can just understand how to read and interpret this information, then all the other messy molecular and cellular details may prove less important.

The [Human Genome Project](https://en.wikipedia.org/wiki/Human_Genome_Project), which started in 1990, aimed to read out all our DNA so that we could catalogue our genes and associate them with their function. But when the first results came in a decade later, they were quite different from what was expected. Rather than a neat picture of genes determining certain functions, or at least mostly encoding protein molecules with clear functions, our genetic content seemed a bewildering mess of baroque complexity, in which it is unclear what most genetic elements "do". In the years that followed, this mess did turn out to contain certain [patterns](https://en.wikipedia.org/wiki/Gene_regulatory_network#Local_feature).
For instance, some combinations of genes were found to behave in ways similar to electronic circuits. Such [biological circuits](https://biocircuits.github.io/chapters/01_intro_to_circuit_design.html) often have clear functions, they can for instance oscillate or switch between states in various ways.[^biocircuits] They are very common in single-celled organisms, but alas, such simple circuits are much less common in humans and other multicellular organisms. The "wiring" of the molecular network encoded by our genes actually more resembles the brain than it does an electronic circuit. Like an electronic circuit, it does seem to direct and process information, but the information doesn't neatly flow in one direction or stay in one part of the system. Instead, like in the brain, the information often seems to go everywhere, and it can have effects all over the organism.

How can we make sense of this mess? Why is our body (and that of other multicellular organisms) organised in such a strange and seemingly chaotic and inefficient way? Is this just the historical legacy of millions of years of random mutation? Perhaps some of it is, but certainly not all of it. Rather, the fact that chemical interaction networks in our body show similarities to the way our neurons are wired probably isn't a coincidence. Our neural networks are wired to integrate and process information in ways that are relatively flexible and that are somewhat insensitive to noise, damage and small details. The same is probably true for the molecular networks encoded by our genome. Individual genes will have an effect on the way information is processed by the network, but the effect is typically small and often it's hard to predict beforehand what the effect will be, precisely. The fact that the effects of gene mutations tend to be small provides the system with some degree of robustness and also makes the process of evolution a lot easier. And the fact that the effect is unpredictable is an advantage given the existence of viruses and other pathogens, which constantly try to co opt our molecular machinery for their own purposes.

All living beings have to survive in a world that is full of noise, variation and things that can inflict damage. If our biology was sensitive to all of this, it would never be able to build a well-functioning complex individual from a single cell, and make it last for 80 years or so.

So what does all of this tell us about how we should deal with complex systems? First of all, it seems that the role of details in such systems is complicated. If we ignore details, we risk coming up with "mystical" cause-and-effect stories that have no clear mechanism. It may take away our uncertainty to attribute effects to deities, the universe, black boxes or invisible hands. False certainties may aid us in many ways[^certainties], but usually they don't really help us in solving actual problems. For this, we need mechanistic understanding. And to understand mechanisms, we often need to know about details. If we say that "everything is connected", this may be true but doesn't help us much in our understanding. We need to figure out *which* connections are *actually important*, and what their mechanics are. But if we do this, we should be aware that our knowledge will probably be incomplete. We will usually oversimplify and miss connections that are important in a certain context.

Moreover, if we focus mostly on details, we may lose sight of the bigger picture. Especially when dealing with living systems, we need to zoom out occasionally and wonder *what a system is supposed to be doing*. What are its goals, which things matter for this, and what is their context? In living systems, the way in which details relate to the whole can perhaps be compared to the structure of human language: If you focus just on letters or on letter shapes, language seems a bewildering mess of small details. It isn't until you zoom out to words that things start to make some sense. But to fully comprehend language, you need the words to interact with each other and with grammar in sentences, which eventually interact with our mood, knowledge and experience in paragraphs and stories. Words do matter in all of this, but a sentence can remain comprehensible if we remove or substitute words, and words can remain comprehensible if we change or remove letters. Moreover, entire languages can evolve significantly and rapidly while still remaining functional. Like language, the way life works has to be both adaptable and robust. Details do matter, but it's hard to say beforehand which details do and which don't. One has to comprehend the larger-scale patterns to understand the role of details.[^causalemergence]

Finally, we need to realise that what we often see as messy, inefficient complexity can actually have a function. We tend to dislike complexity because it makes things harder to understand, manage and optimise. We prefer clear chains of cause and effect, which we can more easily communicate, understand and modify. When confronted with a complex system, the solution we often seek is to make it simpler. But in evolved, living systems, complexity is often a feature rather than a bug.

Of course it is not the case that good designs always *need* to be complex, but they do need to be both robust and adaptive if they are to survive in the long term. The essayist and mathematician [Nassim Nicholas Taleb](https://www.fooledbyrandomness.com) has gone a step further and proposed the term *[antifragile](https://en.wikipedia.org/wiki/Antifragility)* to describe things that do not just persist under adverse conditions (robustness) and are able to recover (resilience), but that actually *require* some adversity to function well and get better over time (which requires adaptation). 

We humans are quite good at optimising things for a narrow set of functions and conditions. We often design structures that are efficient (in a narrow sense of the word) and in which causes and effects are easy to understand. But these structures also tend to be fragile, especially when conditions move away from what the designer considered to be "optimal". 
If we remove or break part of such a fragile system, it often ceases to function. And when we design things to be robust, we tend to do it by *overdesign*. We make a best guess of worse case scenarios (say, the maximum strain a bridge has to endure). Subsequently we apply a [safety factor](https://en.wikipedia.org/wiki/Factor_of_safety): we design the structure so that it can withstand two or three times the worst-case strain (provided of course our calculations are correct, the scenarios don't become outdated and the structure is well-maintained).[^designfailures]

Naturally evolved systems seem to do something quite different. They tend to have many complex causal loops that are hard to understand, but that have a function in stabilising the system and in making it less sensitive to noise and damage. Such systems tend to be robust, because if they weren't, they wouldn't last very long in a world that can often be adverse and unpredictable. They also tend to recover from damage and adapt relatively quickly to new conditions.[^adaptationfailure]

Having antifragility built into a system nearly always makes it harder to comprehend (in the words of the late [James C. Scott](https://en.wikipedia.org/wiki/James_C._Scott), it is *less [legible](https://www.ribbonfarm.com/2010/07/26/a-big-little-idea-called-legibility/)*). But the approach seems a lot more efficient than overdesign to obtain robustness.[^overdesign] And it is certainly more adaptable. So if we're serious about making our societies and our infrastructure sustainable in the long term (by which I mean: more than a few decades), we may do well to broaden our view to how life does things.


<div style="text-align: center; margin-left: auto; margin-right: auto;">
<img src="{static}/images/red-thread.jpg" style="width: 100%; height: auto; border: 0px;"/>
</div>


*Images by Io Cooman, except the Puget Sound pictures and ecosystem diagram. The diagram was adapted from [Harvey et al. (2010)](https://repository.library.noaa.gov/view/noaa/3751/). Puget Sound pictures are by [Buphoff](https://en.wikipedia.org/wiki/User:Buphoff), Vickie J. Anderson ([Harbor Seal](https://commons.wikimedia.org/wiki/File:Harbor_Seal_DSC_3652a.jpg) and [Caspian Tern](https://commons.wikimedia.org/wiki/File:Caspian_Tern_6841v.jpg)), Bruce Duncan ([Plumose Anemone](https://flickr.com/photos/24400159@N05/6988302287)) and Robert Stearns ([Geoduck](https://commons.wikimedia.org/wiki/File:Geoduck.jpg)).*

Do you want to be notified when future articles in this series are published? Subscribe to my [Substack](https://lvzon.substack.com/), or follow me on [Facebook](https://www.facebook.com/sustainsubstance), [Instagram](https://www.instagram.com/sustainsubstance), [Bluesky](https://bsky.app/profile/lvzon.bsky.social) or [Twitter/X](https://twitter.com/levienvanzon). You can also subscribe to our [Atom-feed](/feeds/all.atom.xml).


### Further reading

Donella H. Meadows. *[Thinking in Systems](https://www.chelseagreen.com/product/thinking-in-systems): A Primer*. Chelsea Green Publishing, 2008.   
This book is a classic introduction to "systems thinking", written by the lead author of [The Limits To Growth](https://www.clubofrome.org/publication/the-limits-to-growth/). If you want to get more of a feel for thinking in terms of interactions, positive and negative feedbacks and dynamic patterns, this is a useful text. Furthermore, the book makes a number of important points. Among other things, Meadows argues that we need to think in patterns and mechanisms rather than events. She highlights the role of nonlinear relationships and delays in producing surprising (and often unpleasant) results, as well as the important effects of limited stocks and limited information. She explains that just searching for statistical correlations doesn't really help us much in understanding what a system does, and how or why it does it. However, I do have a few issues with the text. For instance, terms like "feedback loop" are used very often and sometimes in a very broad sense. If you call nearly every process a feedback loop, the term starts to become somewhat meaningless. More seriously, some of the terminology, definitions and proposed mechanisms are vague, sloppy and/or inconsistent. Especially when talking about things such as complexity, resilience, goals and self-organisation, Meadows' explanations sometimes mystify rather than clarify these subjects. Finally, viewing the world in terms of dynamical stock-and-flow systems (as this book does) is certainly useful for understanding systems, but truly complex systems are not always best understood this way. 
See also: <https://donellameadows.org>

Ed Yong. *I Contain Multitudes: The Microbes Within Us and a Grander View of Life*. Bodley Head, 2016.    
<https://edyong.me/i-contain-multitudes>    

Philip Ball. *How Life Works: A User's Guide to the New Biology*.    
University of Chicago Press, 2023.
<https://how-life-works.philipball.co.uk>    
See also the Big Biology podcast, [episode 119](https://www.bigbiology.org/episodes/2024/4/4/ep-119-biology-as-its-own-metaphor-with-phil-ball).

Yuri Lazebnik. '[Can a Biologist Fix a Radio?](https://doi.org/10.1016/S1535-6108(02)00133-2)---Or, What I Learned While Studying Apoptosis'. *Cancer Cell* 2, no. 3 (1 September 2002):179--82.    

Philipp Dettmer. *Immune: A Journey into the Mysterious System That Keeps You Alive*. Random House Publishing Group, 2021.    
<https://www.philippdettmer.net/immune>    

Uri Alon. *An Introduction to Systems Biology: Design Principles of Biological Circuits*. CRC Press, 2019.    
<https://doi.org/10.1201/9780429283321>    
See also the Big Biology podcast, [episode 96](https://www.bigbiology.org/episodes/2023/2/16/ep-96-the-network-motifs-that-run-the-world-with-uri-alon): The network motifs that run the world, with Uri Alon.
An alternative and freely available resource is the online book [*Biological Circuit Design*](https://biocircuits.github.io) by Michael Elowitz, Justin Bois, and John Marken (2022).

Paul Davies. *The Demon in the Machine: How Hidden Webs of Information Are Solving the Mystery of Life*. University of Chicago Press, 2019.    
<https://cosmos.asu.edu/publication/demon-machine>    
See also the Big Biology podcast, [episode 33](https://www.bigbiology.org/episodes/2020/1/30/ep-33-magic-puzzle-box-paul-davies): Magic Puzzle Box, with Paul Davies

Nassim Nicholas Taleb. *[Antifragile:](https://www.penguin.co.uk/books/56655/antifragile-by-taleb-nassim-nicholas/9780141038223) Things That Gain from Disorder*. Random House Publishing Group, 2012.    


-----------

#### Footnotes

[^mentalmodel]:
TODO: Say something about [narratives](https://en.wikipedia.org/wiki/Narrative), and refer to Paul Armstrong's book [Stories and the Brain](https://www.press.jhu.edu/books/title/12296/stories-and-brain): The Neuroscience of Narrative. Note that I have described only the mental and conscious part of our internal model, we also have many unconscious models, and many aspects of the world are even encoded deep into our physiology, e.g. in our biological clock. The neurological models have an important advantage when it comes to adaptability: they can be updated with new information, or in normal language: we can learn things. 

[^causality]:
TODO: Give examples of some of the ways in which we can establish cause-effect-relationships in science.

[^gorydetails]: 
One possible mathematical model of our little greenhouse ecosystem would be the following:
$$ 
\left\{ 
\begin{array}{l}
\frac{\mathrm{d} P}{\mathrm{d} t} = aP - bPS\\ 
\frac{\mathrm{d} S}{\mathrm{d} t} = cPS - dHS\\ 
\frac{\mathrm{d} H}{\mathrm{d} t} = fHS - g 
\end{array}
\right. 
$$
This particular model is known as a [three-species Lotka-Volterra predator-prey model](https://sites.math.washington.edu/~morrow/336_16/2016papers/lalith.pdf), it is a slightly extended version of the "classical" two-species [Lotka-Volterra model](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) familiar to most students of biology (and some economists). It belongs to a class known as dynamical population models, which are based on sets of differential equations. In this case, *P*, *S* and *H* are the population numbers of plants, slugs and hedgehogs, *a* is the plant growth rate, *g* is the rate at which hedgehogs die and *b* through *f* are "rate constants" that represent interaction strength and conversion efficiency. To learn more about such models, you can check out the material of the [Biological Modeling](https://tbb.bio.uu.nl/rdb/bm/index.html) course at Utrecht University (which I helped teach for several years). This class of models is also known as [mass-action](https://en.wikipedia.org/wiki/Law_of_mass_action) models, and these are used among other things to describe chemical reactions. When applied to biological populations, it basically assumes that individual organisms behave as randomly interacting particles in a well-mixed environment. Despite such strange implicit assumptions, these models are quite useful for analysing when a system is stable and when it is not. The particular formulation of a predator-prey population model given here can however be problematic. The formulas above don't include self-limitation within species, due to competition between individuals. Therefore they have a tendency to predict oscillations in cases where real ecosystems would probably be much more stable. In fact, the Lotka-Volterra model is famous for showing that populations can oscillate. However, if we make the model more realistic by adding additional terms to the model for self-limitation, oscillations become much less common.

[^ewemodel]:
For a description of how the model was constructed, see [Harvey et al. (2010)](https://repository.library.noaa.gov/view/noaa/3751/), ‘A Mass-Balance Model for Evaluating Food Web Structure and Community-Scale Indicators in the Central Basin of Puget Sound’.

[^biocircuits]:
For instance, so-called [feed-forward circuits](https://en.wikipedia.org/wiki/Feed_forward_(control)) are [over-represented](https://biocircuits.github.io/chapters/04_ffls.html#The-feedforward-loop-is-overrepresented-in-natural-transcriptional-networks) in the gene regulation networks of especially single-celled organisms. There exist [various types](https://biocircuits.github.io/chapters/04_ffls.html#There-are-many-kinds-of-FFLs) of such circuits with somewhat different properties. For instance the type-1 coherent feed-forward loop (C1-FFL) acts as a switch with a [delay](https://biocircuits.github.io/chapters/04_ffls.html#The-C1-FFL-circuit-enables-sign-sensitive-delay) in switching on, but no delay in switching off. Its function is to [ignore short pulses](https://biocircuits.github.io/chapters/04_ffls.html#Sign-sensitive-delay-is-observed-experimentally) of the activation signal, and to only switch on when the input is present for a longer period, thus filtering out noise. Other common biological circuits act for instance as [pulse generators](https://biocircuits.github.io/chapters/04_ffls.html#The-I1-FFL-with-AND-logic-is-a-pulse-generator), [amplifiers](https://biocircuits.github.io/chapters/07_signal_amplification.html#Amplifiers:-the-middle-managers-of-biological-circuitry) or as [oscillators](https://biocircuits.github.io/chapters/09_repressilator.html) (which for instance drive our [biological clocks](https://en.wikipedia.org/wiki/Circadian_clock)). What all biological circuits have in common is that their operation tends to be fairly robust to noise and to some degree of genetic change (although generic variation can lead to variation in "tuning" of such circuits).

[^certainties]:
TODO: Mention Harari's idea of the role of *shared fictions* in aiding cooperation, and say something about the psychological effects of (un)certainty.

[^causalemergence]:
TODO: Talk about the part-whole relationship in terms of emergence and multi-level interactions. Cause and effect still apply, but causality does not just stay within an organisational level or flow upward from parts to emergent structures, but also downwards from the structures to the parts (Ball calls this causal spreading).Point out why this is actually necessary to make things work reliably in the noisy, unreliable world of molecules. Also elaborate on the pathogen example.

[^designfailures]:
TODO: Give some recent examples of why overdesigned structures can still fail catastrophically (e.g. hydropower dams, nuclear power plants, bridges).

[^adaptationfailure]:
TODO: Note that adaptation is not necessarily successful or sufficiently rapid, there are plenty of examples of extinctions and ecosystem failures. But our immune system, as well as rapid resistance to pesticides and antibiotics and the often surprising speed of ecosystem recovery show that biological adaptation is extremely powerful.

[^overdesign]:
This doesn't mean that applying safety factors is a bad thing to do, nor that it's an "easy way out". [Engineering is hard](https://blog.saket.dk/reengineering-engineering-8312f857091c), and applying a safety margin is a very sensible solution. Also note that I chose to use the term overdesign rather than "[overengineering](https://en.wikipedia.org/wiki/Overengineering)", as the latter term is used when we design things in ways that are unnecessarily complicated. Often this is done to increase safety and robustness, but it can sometimes end up making things more fragile. Hence it is often said that "less is more", because simpler designs are easier to maintain and troubleshoot. However, neither simple designs nor overengineered ones are necessarily robust in the long term. In later articles I will elaborate on what alternative approaches could look like.


