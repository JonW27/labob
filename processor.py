#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type: text/html\n'
#texplainheader = "Content-Type: text/plain"

import os
import os.path
import subprocess
import tempfile
import string
import random

userInput = cgi.FieldStorage()
docFormat = userInput['format'].value
try:
    author = userInput['authname'].value
except:
    author = ''
try:    
    title = userInput['title'].value
except:
    title = ''
try:    
    date =  userInput['date'].value
except:
    date = ''
#starter = userInput['starter'].value
#starterText = userInput['starterText'].value
try:
    bodyText = userInput['body'].value
except:
    bodyText = ''    
try:
    fxn = userInput['function'].value
except:
    fxn = 'tex'
try:    
    landscape = userInput['landscape'].value
except:
    landscape = ''    
paperstyle = userInput['paperStyle'].value
try:
    qCorrect = userInput['qCorrect'].value
except:
    qCorrect = ''
affiliation = ""
if userInput.getvalue('AfflationCHOOSER'):
    affiliation = userInput['Affiliation'].value
#affiliationN = userInput['AffiliationCHOOSER'].value
try:
    abstract = userInput['Abstract'].value
except:
    abstract = ''
try:
    fontsize = userInput['fSize'].value
except:
    fontsize=''
try:    
    parseSkip = userInput['parseSkip'].value
except:
    parseSkip=''
try:    
    keywords = userInput['Keywords'].value
except:
    keywords = ''
try:    
    Plname = userInput['Plname'].value
except:
    Plname = ''
try:    
    Classname = userInput['Classname'].value
except:
    Classname = ''

# Communist Manifesto Example:
if author=='' and date=='' and title=='' and bodyText=='' and abstract=='':
    author="Karl Marx and Friedrich Engels"
    title="MANIFESTO OF THE COMMUNIST PARTY"
    date="February 1848"
    abstract="WORKING MEN OF ALL COUNTRIES, UNITE!"
    qCorrect="True"
    bodyText=r'''
A spectre is haunting Europe -- the spectre of Communism.
All the Powers of old Europe have entered into a holy alliance to
exorcise this spectre: Pope and Czar, Metternich and Guizot,
French Radicals and German police-spies.

Where is the party in opposition that has not been decried as Communistic by its opponents in power? Where is the Opposition that has not hurled back the branding reproach of Communism, against the more advanced opposition parties, as well as against its reactionary adversaries?

Two things result from this fact.

I. Communism is already acknowledged by all European Powers to be itself a Power.

II. It is high time that Communists should openly, in the face of the whole world, publish their views, their aims, their tendencies, and meet this nursery tale of the Spectre of Communism with a Manifesto of the party itself.

To this end, Communists of various nationalities have assembled in London, and sketched the following Manifesto, to be published in the English, French, German, Italian, Flemish and Danish languages.

\section{BOURGEOIS AND PROLETARIANS}
The history of all hitherto existing societies is the history of class struggles.

Freeman and slave, patrician and plebeian, lord and serf, guild-master and journeyman, in a word, oppressor and oppressed, stood in constant opposition to one another, carried on an uninterrupted, now hidden, now open fight, a fight that each time ended, either in a revolutionary re-constitution of society at large, or in the common ruin of the contending classes.

In the earlier epochs of history, we find almost everywhere a complicated arrangement of society into various orders, a manifold gradation of social rank. In ancient Rome we have patricians, knights, plebeians, slaves; in the Middle Ages, feudal lords, vassals, guild-masters, journeymen, apprentices, serfs; in almost all of these classes, again, subordinate gradations.

The modern bourgeois society that has sprouted from the ruins of feudal society has not done away with class antagonisms. It has but established new classes, new conditions of oppression, new forms of struggle in place of the old ones. Our epoch, the epoch of the bourgeoisie, possesses, however, this distinctive feature: it has simplified the class antagonisms. Society as a whole is more and more splitting up into two great hostile camps, into two great classes, directly facing each other: Bourgeoisie and Proletariat.

From the serfs of the Middle Ages sprang the chartered burghers of the earliest towns. From these burgesses the first elements of the bourgeoisie were developed.

The discovery of America, the rounding of the Cape, opened up fresh ground for the rising bourgeoisie. The East-Indian and Chinese markets, the colonisation of America, trade with the colonies, the increase in the means of exchange and in commodities generally, gave to commerce, to navigation, to industry, an impulse never before known, and thereby, to the revolutionary element in the tottering feudal society, a rapid development.

The feudal system of industry, under which industrial production was monopolised by closed guilds, now no longer sufficed for the growing wants of the new markets. The manufacturing system took its place. The guild-masters were pushed on one side by the manufacturing middle class; division of labour between the different corporate guilds vanished in the face of division of labour in each single workshop.

Meantime the markets kept ever growing, the demand ever rising. Even manufacture no longer sufficed. Thereupon, steam and machinery revolutionised industrial production. The place of manufacture was taken by the giant, Modern Industry, the place of the industrial middle class, by industrial millionaires, the leaders of whole industrial armies, the modern bourgeois.

Modern industry has established the world-market, for which the discovery of America paved the way. This market has given an immense development to commerce, to navigation, to communication by land. This development has, in its time, reacted on the extension of industry; and in proportion as industry, commerce, navigation, railways extended, in the same proportion the bourgeoisie developed, increased its capital, and pushed into the background every class handed down from the Middle Ages.

We see, therefore, how the modern bourgeoisie is itself the product of a long course of development, of a series of revolutions in the modes of production and of exchange.

Each step in the development of the bourgeoisie was accompanied by a corresponding political advance of that class. An oppressed class under the sway of the feudal nobility, an armed and self-governing association in the mediaeval commune; here independent urban republic (as in Italy and Germany), there taxable "third estate" of the monarchy (as in France), afterwards, in the period of manufacture proper, serving either the semi-feudal or the absolute monarchy as a counterpoise against the nobility, and, in fact, corner-stone of the great monarchies in general, the bourgeoisie has at last, since the establishment of Modern Industry and of the world-market, conquered for itself, in the modern representative State, exclusive political sway. The executive of the modern State is but a committee for managing the common affairs of the whole bourgeoisie.

The bourgeoisie, historically, has played a most revolutionary part.

The bourgeoisie, wherever it has got the upper hand, has put an end to all feudal, patriarchal, idyllic relations. It has pitilessly torn asunder the motley feudal ties that bound man to his "natural superiors," and has left remaining no other nexus between man and man than naked self-interest, than callous "cash payment." It has drowned the most heavenly ecstasies of religious fervour, of chivalrous enthusiasm, of philistine sentimentalism, in the icy water of egotistical calculation. It has resolved personal worth into exchange value, and in place of the numberless and indefeasible chartered freedoms, has set up that single, unconscionable freedom—Free Trade. In one word, for exploitation, veiled by religious and political illusions, naked, shameless, direct, brutal exploitation.

The bourgeoisie has stripped of its halo every occupation hitherto honoured and looked up to with reverent awe. It has converted the physician, the lawyer, the priest, the poet, the man of science, into its paid wage labourers.

The bourgeoisie has torn away from the family its sentimental veil, and has reduced the family relation to a mere money relation.

The bourgeoisie has disclosed how it came to pass that the brutal display of vigour in the Middle Ages, which Reactionists so much admire, found its fitting complement in the most slothful indolence. It has been the first to show what man's activity can bring about. It has accomplished wonders far surpassing Egyptian pyramids, Roman aqueducts, and Gothic cathedrals; it has conducted expeditions that put in the shade all former Exoduses of nations and crusades.

The bourgeoisie cannot exist without constantly revolutionising the instruments of production, and thereby the relations of production, and with them the whole relations of society. Conservation of the old modes of production in unaltered form, was, on the contrary, the first condition of existence for all earlier industrial classes. Constant revolutionising of production, uninterrupted disturbance of all social conditions, everlasting uncertainty and agitation distinguish the bourgeois epoch from all earlier ones. All fixed, fast-frozen relations, with their train of ancient and venerable prejudices and opinions, are swept away, all new-formed ones become antiquated before they can ossify. All that is solid melts into air, all that is holy is profaned, and man is at last compelled to face with sober senses, his real conditions of life, and his relations with his kind.

The need of a constantly expanding market for its products chases the bourgeoisie over the whole surface of the globe. It must nestle everywhere, settle everywhere, establish connexions everywhere.

The bourgeoisie has through its exploitation of the world-market given a cosmopolitan character to production and consumption in every country. To the great chagrin of Reactionists, it has drawn from under the feet of industry the national ground on which it stood. All old-established national industries have been destroyed or are daily being destroyed. They are dislodged by new industries, whose introduction becomes a life and death question for all civilised nations, by industries that no longer work up indigenous raw material, but raw material drawn from the remotest zones; industries whose products are consumed, not only at home, but in every quarter of the globe. In place of the old wants, satisfied by the productions of the country, we find new wants, requiring for their satisfaction the products of distant lands and climes. In place of the old local and national seclusion and self-sufficiency, we have intercourse in every direction, universal inter-dependence of nations. And as in material, so also in intellectual production. The intellectual creations of individual nations become common property. National one-sidedness and narrow-mindedness become more and more impossible, and from the numerous national and local literatures, there arises a world literature.

The bourgeoisie, by the rapid improvement of all instruments of production, by the immensely facilitated means of communication, draws all, even the most barbarian, nations into civilisation. The cheap prices of its commodities are the heavy artillery with which it batters down all Chinese walls, with which it forces the barbarians' intensely obstinate hatred of foreigners to capitulate. It compels all nations, on pain of extinction, to adopt the bourgeois mode of production; it compels them to introduce what it calls civilisation into their midst, i.e., to become bourgeois themselves. In one word, it creates a world after its own image.

The bourgeoisie has subjected the country to the rule of the towns. It has created enormous cities, has greatly increased the urban population as compared with the rural, and has thus rescued a considerable part of the population from the idiocy of rural life. Just as it has made the country dependent on the towns, so it has made barbarian and semi-barbarian countries dependent on the civilised ones, nations of peasants on nations of bourgeois, the East on the West.

The bourgeoisie keeps more and more doing away with the scattered state of the population, of the means of production, and of property. It has agglomerated production, and has concentrated property in a few hands. The necessary consequence of this was political centralisation. Independent, or but loosely connected provinces, with separate interests, laws, governments and systems of taxation, became lumped together into one nation, with one government, one code of laws, one national class-interest, one frontier and one customs-tariff. The bourgeoisie, during its rule of scarce one hundred years, has created more massive and more colossal productive forces than have all preceding generations together. Subjection of Nature's forces to man, machinery, application of chemistry to industry and agriculture, steam-navigation, railways, electric telegraphs, clearing of whole continents for cultivation, canalisation of rivers, whole populations conjured out of the ground—what earlier century had even a presentiment that such productive forces slumbered in the lap of social labour?

We see then: the means of production and of exchange, on whose foundation the bourgeoisie built itself up, were generated in feudal society. At a certain stage in the development of these means of production and of exchange, the conditions under which feudal society produced and exchanged, the feudal organisation of agriculture and manufacturing industry, in one word, the feudal relations of property became no longer compatible with the already developed productive forces; they became so many fetters. They had to be burst asunder; they were burst asunder.

Into their place stepped free competition, accompanied by a social and political constitution adapted to it, and by the economical and political sway of the bourgeois class.

A similar movement is going on before our own eyes. Modern bourgeois society with its relations of production, of exchange and of property, a society that has conjured up such gigantic means of production and of exchange, is like the sorcerer, who is no longer able to control the powers of the nether world whom he has called up by his spells. For many a decade past the history of industry and commerce is but the history of the revolt of modern productive forces against modern conditions of production, against the property relations that are the conditions for the existence of the bourgeoisie and of its rule. It is enough to mention the commercial crises that by their periodical return put on its trial, each time more threateningly, the existence of the entire bourgeois society. In these crises a great part not only of the existing products, but also of the previously created productive forces, are periodically destroyed. In these crises there breaks out an epidemic that, in all earlier epochs, would have seemed an absurdity—the epidemic of over-production. Society suddenly finds itself put back into a state of momentary barbarism; it appears as if a famine, a universal war of devastation had cut off the supply of every means of subsistence; industry and commerce seem to be destroyed; and why? Because there is too much civilisation, too much means of subsistence, too much industry, too much commerce. The productive forces at the disposal of society no longer tend to further the development of the conditions of bourgeois property; on the contrary, they have become too powerful for these conditions, by which they are fettered, and so soon as they overcome these fetters, they bring disorder into the whole of bourgeois society, endanger the existence of bourgeois property. The conditions of bourgeois society are too narrow to comprise the wealth created by them. And how does the bourgeoisie get over these crises? On the one hand inforced destruction of a mass of productive forces; on the other, by the conquest of new markets, and by the more thorough exploitation of the old ones. That is to say, by paving the way for more extensive and more destructive crises, and by diminishing the means whereby crises are prevented.

The weapons with which the bourgeoisie felled feudalism to the ground are now turned against the bourgeoisie itself.

But not only has the bourgeoisie forged the weapons that bring death to itself; it has also called into existence the men who are to wield those weapons—the modern working class—the proletarians.

In proportion as the bourgeoisie, i.e., capital, is developed, in the same proportion is the proletariat, the modern working class, developed—a class of labourers, who live only so long as they find work, and who find work only so long as their labour increases capital. These labourers, who must sell themselves piece-meal, are a commodity, like every other article of commerce, and are consequently exposed to all the vicissitudes of competition, to all the fluctuations of the market.

Owing to the extensive use of machinery and to division of labour, the work of the proletarians has lost all individual character, and consequently, all charm for the workman. He becomes an appendage of the machine, and it is only the most simple, most monotonous, and most easily acquired knack, that is required of him. Hence, the cost of production of a workman is restricted, almost entirely, to the means of subsistence that he requires for his maintenance, and for the propagation of his race. But the price of a commodity, and therefore also of labour, is equal to its cost of production. In proportion therefore, as the repulsiveness of the work increases, the wage decreases. Nay more, in proportion as the use of machinery and division of labour increases, in the same proportion the burden of toil also increases, whether by prolongation of the working hours, by increase of the work exacted in a given time or by increased speed of the machinery, etc.

Modern industry has converted the little workshop of the patriarchal master into the great factory of the industrial capitalist. Masses of labourers, crowded into the factory, are organised like soldiers. As privates of the industrial army they are placed under the command of a perfect hierarchy of officers and sergeants. Not only are they slaves of the bourgeois class, and of the bourgeois State; they are daily and hourly enslaved by the machine, by the over-looker, and, above all, by the individual bourgeois manufacturer himself. The more openly this despotism proclaims gain to be its end and aim, the more petty, the more hateful and the more embittering it is.

The less the skill and exertion of strength implied in manual labour, in other words, the more modern industry becomes developed, the more is the labour of men superseded by that of women. Differences of age and sex have no longer any distinctive social validity for the working class. All are instruments of labour, more or less expensive to use, according to their age and sex.

No sooner is the exploitation of the labourer by the manufacturer, so far at an end, that he receives his wages in cash, than he is set upon by the other portions of the bourgeoisie, the landlord, the shopkeeper, the pawnbroker, etc.

The lower strata of the middle class—the small tradespeople, shopkeepers, retired tradesmen generally, the handicraftsmen and peasants—all these sink gradually into the proletariat, partly because their diminutive capital does not suffice for the scale on which Modern Industry is carried on, and is swamped in the competition with the large capitalists, partly because their specialized skill is rendered worthless by the new methods of production. Thus the proletariat is recruited from all classes of the population.

The proletariat goes through various stages of development. With its birth begins its struggle with the bourgeoisie. At first the contest is carried on by individual labourers, then by the workpeople of a factory, then by the operatives of one trade, in one locality, against the individual bourgeois who directly exploits them. They direct their attacks not against the bourgeois conditions of production, but against the instruments of production themselves; they destroy imported wares that compete with their labour, they smash to pieces machinery, they set factories ablaze, they seek to restore by force the vanished status of the workman of the Middle Ages.

At this stage the labourers still form an incoherent mass scattered over the whole country, and broken up by their mutual competition. If anywhere they unite to form more compact bodies, this is not yet the consequence of their own active union, but of the union of the bourgeoisie, which class, in order to attain its own political ends, is compelled to set the whole proletariat in motion, and is moreover yet, for a time, able to do so. At this stage, therefore, the proletarians do not fight their enemies, but the enemies of their enemies, the remnants of absolute monarchy, the landowners, the non-industrial bourgeois, the petty bourgeoisie. Thus the whole historical movement is concentrated in the hands of the bourgeoisie; every victory so obtained is a victory for the bourgeoisie.

But with the development of industry the proletariat not only increases in number; it becomes concentrated in greater masses, its strength grows, and it feels that strength more. The various interests and conditions of life within the ranks of the proletariat are more and more equalised, in proportion as machinery obliterates all distinctions of labour, and nearly everywhere reduces wages to the same low level. The growing competition among the bourgeois, and the resulting commercial crises, make the wages of the workers ever more fluctuating. The unceasing improvement of machinery, ever more rapidly developing, makes their livelihood more and more precarious; the collisions between individual workmen and individual bourgeois take more and more the character of collisions between two classes. Thereupon the workers begin to form combinations (Trades Unions) against the bourgeois; they club together in order to keep up the rate of wages; they found permanent associations in order to make provision beforehand for these occasional revolts. Here and there the contest breaks out into riots.

Now and then the workers are victorious, but only for a time. The real fruit of their battles lies, not in the immediate result, but in the ever-expanding union of the workers. This union is helped on by the improved means of communication that are created by modern industry and that place the workers of different localities in contact with one another. It was just this contact that was needed to centralise the numerous local struggles, all of the same character, into one national struggle between classes. But every class struggle is a political struggle. And that union, to attain which the burghers of the Middle Ages, with their miserable highways, required centuries, the modern proletarians, thanks to railways, achieve in a few years.

This organisation of the proletarians into a class, and consequently into a political party, is continually being upset again by the competition between the workers themselves. But it ever rises up again, stronger, firmer, mightier. It compels legislative recognition of particular interests of the workers, by taking advantage of the divisions among the bourgeoisie itself. Thus the ten-hours' bill in England was carried.

Altogether collisions between the classes of the old society further, in many ways, the course of development of the proletariat. The bourgeoisie finds itself involved in a constant battle. At first with the aristocracy; later on, with those portions of the bourgeoisie itself, whose interests have become antagonistic to the progress of industry; at all times, with the bourgeoisie of foreign countries. In all these battles it sees itself compelled to appeal to the proletariat, to ask for its help, and thus, to drag it into the political arena. The bourgeoisie itself, therefore, supplies the proletariat with its own instruments of political and general education, in other words, it furnishes the proletariat with weapons for fighting the bourgeoisie.

Further, as we have already seen, entire sections of the ruling classes are, by the advance of industry, precipitated into the proletariat, or are at least threatened in their conditions of existence. These also supply the proletariat with fresh elements of enlightenment and progress.

Finally, in times when the class struggle nears the decisive hour, the process of dissolution going on within the ruling class, in fact within the whole range of society, assumes such a violent, glaring character, that a small section of the ruling class cuts itself adrift, and joins the revolutionary class, the class that holds the future in its hands. Just as, therefore, at an earlier period, a section of the nobility went over to the bourgeoisie, so now a portion of the bourgeoisie goes over to the proletariat, and in particular, a portion of the bourgeois ideologists, who have raised themselves to the level of comprehending theoretically the historical movement as a whole.

Of all the classes that stand face to face with the bourgeoisie today, the proletariat alone is a really revolutionary class. The other classes decay and finally disappear in the face of Modern Industry; the proletariat is its special and essential product. The lower middle class, the small manufacturer, the shopkeeper, the artisan, the peasant, all these fight against the bourgeoisie, to save from extinction their existence as fractions of the middle class. They are therefore not revolutionary, but conservative. Nay more, they are reactionary, for they try to roll back the wheel of history. If by chance they are revolutionary, they are so only in view of their impending transfer into the proletariat, they thus defend not their present, but their future interests, they desert their own standpoint to place themselves at that of the proletariat.

The "dangerous class," the social scum, that passively rotting mass thrown off by the lowest layers of old society, may, here and there, be swept into the movement by a proletarian revolution; its conditions of life, however, prepare it far more for the part of a bribed tool of reactionary intrigue.

In the conditions of the proletariat, those of old society at large are already virtually swamped. The proletarian is without property; his relation to his wife and children has no longer anything in common with the bourgeois family-relations; modern industrial labour, modern subjection to capital, the same in England as in France, in America as in Germany, has stripped him of every trace of national character. Law, morality, religion, are to him so many bourgeois prejudices, behind which lurk in ambush just as many bourgeois interests.

All the preceding classes that got the upper hand, sought to fortify their already acquired status by subjecting society at large to their conditions of appropriation. The proletarians cannot become masters of the productive forces of society, except by abolishing their own previous mode of appropriation, and thereby also every other previous mode of appropriation. They have nothing of their own to secure and to fortify; their mission is to destroy all previous securities for, and insurances of, individual property.

All previous historical movements were movements of minorities, or in the interests of minorities. The proletarian movement is the self-conscious, independent movement of the immense majority, in the interests of the immense majority. The proletariat, the lowest stratum of our present society, cannot stir, cannot raise itself up, without the whole superincumbent strata of official society being sprung into the air.

Though not in substance, yet in form, the struggle of the proletariat with the bourgeoisie is at first a national struggle. The proletariat of each country must, of course, first of all settle matters with its own bourgeoisie.

In depicting the most general phases of the development of the proletariat, we traced the more or less veiled civil war, raging within existing society, up to the point where that war breaks out into open revolution, and where the violent overthrow of the bourgeoisie lays the foundation for the sway of the proletariat.

Hitherto, every form of society has been based, as we have already seen, on the antagonism of oppressing and oppressed classes. But in order to oppress a class, certain conditions must be assured to it under which it can, at least, continue its slavish existence. The serf, in the period of serfdom, raised himself to membership in the commune, just as the petty bourgeois, under the yoke of feudal absolutism, managed to develop into a bourgeois. The modern laborer, on the contrary, instead of rising with the progress of industry, sinks deeper and deeper below the conditions of existence of his own class. He becomes a pauper, and pauperism develops more rapidly than population and wealth. And here it becomes evident, that the bourgeoisie is unfit any longer to be the ruling class in society, and to impose its conditions of existence upon society as an over-riding law. It is unfit to rule because it is incompetent to assure an existence to its slave within his slavery, because it cannot help letting him sink into such a state, that it has to feed him, instead of being fed by him. Society can no longer live under this bourgeoisie, in other words, its existence is no longer compatible with society.

The essential condition for the existence, and for the sway of the bourgeois class, is the formation and augmentation of capital; the condition for capital is wage-labour. Wage-labour rests exclusively on competition between the laborers. The advance of industry, whose involuntary promoter is the bourgeoisie, replaces the isolation of the labourers, due to competition, by their revolutionary combination, due to association. The development of Modern Industry, therefore, cuts from under its feet the very foundation on which the bourgeoisie produces and appropriates products. What the bourgeoisie, therefore, produces, above all, is its own grave-diggers. Its fall and the victory of the proletariat are equally inevitable.

\section{PROLETARIANS AND COMMUNISTS}
In what relation do the Communists stand to the proletarians as a whole?

The Communists do not form a separate party opposed to other working-class parties.

They have no interests separate and apart from those of the proletariat as a whole.

They do not set up any sectarian principles of their own, by which to shape and mould the proletarian movement.

The Communists are distinguished from the other working-class parties by this only: (1) In the national struggles of the proletarians of the different countries, they point out and bring to the front the common interests of the entire proletariat, independently of all nationality. (2) In the various stages of development which the struggle of the working class against the bourgeoisie has to pass through, they always and everywhere represent the interests of the movement as a whole.

The Communists, therefore, are on the one hand, practically, the most advanced and resolute section of the working-class parties of every country, that section which pushes forward all others; on the other hand, theoretically, they have over the great mass of the proletariat the advantage of clearly understanding the line of march, the conditions, and the ultimate general results of the proletarian movement.

The immediate aim of the Communist is the same as that of all the other proletarian parties: formation of the proletariat into a class, overthrow of the bourgeois supremacy, conquest of political power by the proletariat.

The theoretical conclusions of the Communists are in no way based on ideas or principles that have been invented, or discovered, by this or that would-be universal reformer. They merely express, in general terms, actual relations springing from an existing class struggle, from a historical movement going on under our very eyes. The abolition of existing property relations is not at all a distinctive feature of Communism.

All property relations in the past have continually been subject to historical change consequent upon the change in historical conditions.

The French Revolution, for example, abolished feudal property in favour of bourgeois property.

The distinguishing feature of Communism is not the abolition of property generally, but the abolition of bourgeois property. But modern bourgeois private property is the final and most complete expression of the system of producing and appropriating products, that is based on class antagonisms, on the exploitation of the many by the few.

In this sense, the theory of the Communists may be summed up in the single sentence: Abolition of private property.

We Communists have been reproached with the desire of abolishing the right of personally acquiring property as the fruit of a man's own labour, which property is alleged to be the groundwork of all personal freedom, activity and independence.

Hard-won, self-acquired, self-earned property! Do you mean the property of the petty artisan and of the small peasant, a form of property that preceded the bourgeois form? There is no need to abolish that; the development of industry has to a great extent already destroyed it, and is still destroying it daily.

Or do you mean modern bourgeois private property?

But does wage-labour create any property for the labourer? Not a bit. It creates capital, i.e., that kind of property which exploits wage-labour, and which cannot increase except upon condition of begetting a new supply of wage-labour for fresh exploitation. Property, in its present form, is based on the antagonism of capital and wage-labour. Let us examine both sides of this antagonism.

To be a capitalist, is to have not only a purely personal, but a social status in production. Capital is a collective product, and only by the united action of many members, nay, in the last resort, only by the united action of all members of society, can it be set in motion.

Capital is, therefore, not a personal, it is a social power.

When, therefore, capital is converted into common property, into the property of all members of society, personal property is not thereby transformed into social property. It is only the social character of the property that is changed. It loses its class-character.

Let us now take wage-labour.

The average price of wage-labour is the minimum wage, i.e., that quantum of the means of subsistence, which is absolutely requisite in bare existence as a labourer. What, therefore, the wage-labourer appropriates by means of his labour, merely suffices to prolong and reproduce a bare existence. We by no means intend to abolish this personal appropriation of the products of labour, an appropriation that is made for the maintenance and reproduction of human life, and that leaves no surplus wherewith to command the labour of others. All that we want to do away with, is the miserable character of this appropriation, under which the labourer lives merely to increase capital, and is allowed to live only in so far as the interest of the ruling class requires it.

In bourgeois society, living labour is but a means to increase accumulated labour. In Communist society, accumulated labour is but a means to widen, to enrich, to promote the existence of the labourer.

In bourgeois society, therefore, the past dominates the present; in Communist society, the present dominates the past. In bourgeois society capital is independent and has individuality, while the living person is dependent and has no individuality.

And the abolition of this state of things is called by the bourgeois, abolition of individuality and freedom! And rightly so. The abolition of bourgeois individuality, bourgeois independence, and bourgeois freedom is undoubtedly aimed at.

By freedom is meant, under the present bourgeois conditions of production, free trade, free selling and buying.

But if selling and buying disappears, free selling and buying disappears also. This talk about free selling and buying, and all the other "brave words" of our bourgeoisie about freedom in general, have a meaning, if any, only in contrast with restricted selling and buying, with the fettered traders of the Middle Ages, but have no meaning when opposed to the Communistic abolition of buying and selling, of the bourgeois conditions of production, and of the bourgeoisie itself.

You are horrified at our intending to do away with private property. But in your existing society, private property is already done away with for nine-tenths of the population; its existence for the few is solely due to its non-existence in the hands of those nine-tenths. You reproach us, therefore, with intending to do away with a form of property, the necessary condition for whose existence is the non-existence of any property for the immense majority of society.

In one word, you reproach us with intending to do away with your property. Precisely so; that is just what we intend.

From the moment when labour can no longer be converted into capital, money, or rent, into a social power capable of being monopolised, i.e., from the moment when individual property can no longer be transformed into bourgeois property, into capital, from that moment, you say individuality vanishes.

You must, therefore, confess that by "individual" you mean no other person than the bourgeois, than the middle-class owner of property. This person must, indeed, be swept out of the way, and made impossible.

Communism deprives no man of the power to appropriate the products of society; all that it does is to deprive him of the power to subjugate the labour of others by means of such appropriation.

It has been objected that upon the abolition of private property all work will cease, and universal laziness will overtake us.

According to this, bourgeois society ought long ago to have gone to the dogs through sheer idleness; for those of its members who work, acquire nothing, and those who acquire anything, do not work. The whole of this objection is but another expression of the tautology: that there can no longer be any wage-labour when there is no longer any capital.

All objections urged against the Communistic mode of producing and appropriating material products, have, in the same way, been urged against the Communistic modes of producing and appropriating intellectual products. Just as, to the bourgeois, the disappearance of class property is the disappearance of production itself, so the disappearance of class culture is to him identical with the disappearance of all culture.

That culture, the loss of which he laments, is, for the enormous majority, a mere training to act as a machine.

But don't wrangle with us so long as you apply, to our intended abolition of bourgeois property, the standard of your bourgeois notions of freedom, culture, law, etc. Your very ideas are but the outgrowth of the conditions of your bourgeois production and bourgeois property, just as your jurisprudence is but the will of your class made into a law for all, a will, whose essential character and direction are determined by the economical conditions of existence of your class.

The selfish misconception that induces you to transform into eternal laws of nature and of reason, the social forms springing from your present mode of production and form of property--historical relations that rise and disappear in the progress of production—this misconception you share with every ruling class that has preceded you. What you see clearly in the case of ancient property, what you admit in the case of feudal property, you are of course forbidden to admit in the case of your own bourgeois form of property.

Abolition of the family! Even the most radical flare up at this infamous proposal of the Communists.

On what foundation is the present family, the bourgeois family, based? On capital, on private gain. In its completely developed form this family exists only among the bourgeoisie. But this state of things finds its complement in the practical absence of the family among the proletarians, and in public prostitution.

The bourgeois family will vanish as a matter of course when its complement vanishes, and both will vanish with the vanishing of capital.

Do you charge us with wanting to stop the exploitation of children by their parents? To this crime we plead guilty.

But, you will say, we destroy the most hallowed of relations, when we replace home education by social.

And your education! Is not that also social, and determined by the social conditions under which you educate, by the intervention, direct or indirect, of society, by means of schools, etc.? The Communists have not invented the intervention of society in education; they do but seek to alter the character of that intervention, and to rescue education from the influence of the ruling class.

The bourgeois clap-trap about the family and education, about the hallowed co-relation of parent and child, becomes all the more disgusting, the more, by the action of Modern Industry, all family ties among the proletarians are torn asunder, and their children transformed into simple articles of commerce and instruments of labour.

But you Communists would introduce community of women, screams the whole bourgeoisie in chorus.

The bourgeois sees in his wife a mere instrument of production. He hears that the instruments of production are to be exploited in common, and, naturally, can come to no other conclusion than that the lot of being common to all will likewise fall to the women.

He has not even a suspicion that the real point is to do away with the status of women as mere instruments of production.

For the rest, nothing is more ridiculous than the virtuous indignation of our bourgeois at the community of women which, they pretend, is to be openly and officially established by the Communists. The Communists have no need to introduce community of women; it has existed almost from time immemorial.

Our bourgeois, not content with having the wives and daughters of their proletarians at their disposal, not to speak of common prostitutes, take the greatest pleasure in seducing each other's wives.

Bourgeois marriage is in reality a system of wives in common and thus, at the most, what the Communists might possibly be reproached with, is that they desire to introduce, in substitution for a hypocritically concealed, an openly legalised community of women. For the rest, it is self-evident that the abolition of the present system of production must bring with it the abolition of the community of women springing from that system, i.e., of prostitution both public and private.

The Communists are further reproached with desiring to abolish countries and nationality.

The working men have no country. We cannot take from them what they have not got. Since the proletariat must first of all acquire political supremacy, must rise to be the leading class of the nation, must constitute itself the nation, it is, so far, itself national, though not in the bourgeois sense of the word.

National differences and antagonisms between peoples are daily more and more vanishing, owing to the development of the bourgeoisie, to freedom of commerce, to the world-market, to uniformity in the mode of production and in the conditions of life corresponding thereto.

The supremacy of the proletariat will cause them to vanish still faster. United action, of the leading civilised countries at least, is one of the first conditions for the emancipation of the proletariat.

In proportion as the exploitation of one individual by another is put an end to, the exploitation of one nation by another will also be put an end to. In proportion as the antagonism between classes within the nation vanishes, the hostility of one nation to another will come to an end.

The charges against Communism made from a religious, a philosophical, and, generally, from an ideological standpoint, are not deserving of serious examination.

Does it require deep intuition to comprehend that man's ideas, views and conceptions, in one word, man's consciousness, changes with every change in the conditions of his material existence, in his social relations and in his social life?

What else does the history of ideas prove, than that intellectual production changes its character in proportion as material production is changed? The ruling ideas of each age have ever been the ideas of its ruling class.

When people speak of ideas that revolutionise society, they do but express the fact, that within the old society, the elements of a new one have been created, and that the dissolution of the old ideas keeps even pace with the dissolution of the old conditions of existence.

When the ancient world was in its last throes, the ancient religions were overcome by Christianity. When Christian ideas succumbed in the 18th century to rationalist ideas, feudal society fought its death battle with the then revolutionary bourgeoisie. The ideas of religious liberty and freedom of conscience merely gave expression to the sway of free competition within the domain of knowledge.

"Undoubtedly," it will be said, "religious, moral, philosophical and juridical ideas have been modified in the course of historical development. But religion, morality philosophy, political science, and law, constantly survived this change."

"There are, besides, eternal truths, such as Freedom, Justice, etc. that are common to all states of society. But Communism abolishes eternal truths, it abolishes all religion, and all morality, instead of constituting them on a new basis; it therefore acts in contradiction to all past historical experience."

What does this accusation reduce itself to? The history of all past society has consisted in the development of class antagonisms, antagonisms that assumed different forms at different epochs.

But whatever form they may have taken, one fact is common to all past ages, viz., the exploitation of one part of society by the other. No wonder, then, that the social consciousness of past ages, despite all the multiplicity and variety it displays, moves within certain common forms, or general ideas, which cannot completely vanish except with the total disappearance of class antagonisms.

The Communist revolution is the most radical rupture with traditional property relations; no wonder that its development involves the most radical rupture with traditional ideas.

But let us have done with the bourgeois objections to Communism.

We have seen above, that the first step in the revolution by the working class, is to raise the proletariat to the position of ruling as to win the battle of democracy.

The proletariat will use its political supremacy to wrest, by degrees, all capital from the bourgeoisie, to centralise all instruments of production in the hands of the State, i.e., of the proletariat organised as the ruling class; and to increase the total of productive forces as rapidly as possible.

Of course, in the beginning, this cannot be effected except by means of despotic inroads on the rights of property, and on the conditions of bourgeois production; by means of measures, therefore, which appear economically insufficient and untenable, but which, in the course of the movement, outstrip themselves, necessitate further inroads upon the old social order, and are unavoidable as a means of entirely revolutionising the mode of production.

These measures will of course be different in different countries.

Nevertheless in the most advanced countries, the following will be pretty generally applicable.

\begin{enumerate}
\item Abolition of property in land and application of all rents of land to public purposes.
\item A heavy progressive or graduated income tax.
\item Abolition of all right of inheritance.
\item Confiscation of the property of all emigrants and rebels.
\item Centralisation of credit in the hands of the State, by means of a national bank with State capital and an exclusive monopoly.
\item Centralisation of the means of communication and transport in the hands of the State.
\item Extension of factories and instruments of production owned by the State; the bringing into cultivation of waste-lands, and the improvement of the soil generally in accordance with a common plan.
\item Equal liability of all to labour. Establishment of industrial armies, especially for agriculture.
\item Combination of agriculture with manufacturing industries; gradual abolition of the distinction between town and country, by a more equable distribution of the population over the country.
\item Free education for all children in public schools. Abolition of children's factory labour in its present form. Combination of education with industrial production, etc. etc\ldots
\end{enumerate}

When, in the course of development, class distinctions have disappeared, and all production has been concentrated in the hands of a vast association of the whole nation, the public power will lose its political character. Political power, properly so called, is merely the organised power of one class for oppressing another. If the proletariat during its contest with the bourgeoisie is compelled, by the force of circumstances, to organise itself as a class, if, by means of a revolution, it makes itself the ruling class, and, as such, sweeps away by force the old conditions of production, then it will, along with these conditions, have swept away the conditions for the existence of class antagonisms and of classes generally, and will thereby have abolished its own supremacy as a class.

In place of the old bourgeois society, with its classes and class antagonisms, we shall have an association, in which the free development of each is the condition for the free development of all.

\section{SOCIALIST AND COMMUNIST LITERATURE}
\subsection{REACTIONARY SOCIALISM}
\subsubsection{Feudal Socialism}
Owing to their historical position, it became the vocation of the aristocracies of France and England to write pamphlets against modern bourgeois society. In the French revolution of July 1830, and in the English reform agitation, these aristocracies again succumbed to the hateful upstart. Thenceforth, a serious political contest was altogether out of the question. A literary battle alone remained possible. But even in the domain of literature the old cries of the restoration period had become impossible.

In order to arouse sympathy, the aristocracy were obliged to lose sight, apparently, of their own interests, and to formulate their indictment against the bourgeoisie in the interest of the exploited working class alone. Thus the aristocracy took their revenge by singing lampoons on their new master, and whispering in his ears sinister prophecies of coming catastrophe.

In this way arose Feudal Socialism: half lamentation, half lampoon; half echo of the past, half menace of the future; at times, by its bitter, witty and incisive criticism, striking the bourgeoisie to the very heart's core; but always ludicrous in its effect, through total incapacity to comprehend the march of modern history.

The aristocracy, in order to rally the people to them, waved the proletarian alms-bag in front for a banner. But the people, so often as it joined them, saw on their hindquarters the old feudal coats of arms, and deserted with loud and irreverent laughter.

One section of the French Legitimists and "Young England" exhibited this spectacle.

In pointing out that their mode of exploitation was different to that of the bourgeoisie, the feudalists forget that they exploited under circumstances and conditions that were quite different, and that are now antiquated. In showing that, under their rule, the modern proletariat never existed, they forget that the modern bourgeoisie is the necessary offspring of their own form of society.

For the rest, so little do they conceal the reactionary character of their criticism that their chief accusation against the bourgeoisie amounts to this, that under the bourgeois regime a class is being developed, which is destined to cut up root and branch the old order of society.

What they upbraid the bourgeoisie with is not so much that it creates a proletariat, as that it creates a revolutionary proletariat.

In political practice, therefore, they join in all coercive measures against the working class; and in ordinary life, despite their high falutin phrases, they stoop to pick up the golden apples dropped from the tree of industry, and to barter truth, love, and honour for traffic in wool, beetroot-sugar, and potato spirits.

As the parson has ever gone hand in hand with the landlord, so has Clerical Socialism with Feudal Socialism.

Nothing is easier than to give Christian asceticism a Socialist tinge. Has not Christianity declaimed against private property, against marriage, against the State? Has it not preached in the place of these, charity and poverty, celibacy and mortification of the flesh, monastic life and Mother Church? Christian Socialism is but the holy, water with which the priest consecrates the heart-burnings of the aristocrat.

\subsubsection{Petty-Bourgeois Socialism}
The feudal aristocracy was not the only class that was ruined by the bourgeoisie, not the only class whose conditions of existence pined and perished in the atmosphere of modern bourgeois society. The mediaeval burgesses and the small peasant proprietors were the precursors of the modern bourgeoisie. In those countries which are but little developed, industrially and commercially, these two classes still vegetate side by side with the rising bourgeoisie.

In countries where modern civilisation has become fully developed, a new class of petty bourgeois has been formed, fluctuating between proletariat and bourgeoisie and ever renewing itself as a supplementary part of bourgeois society. The individual members of this class, however, are being constantly hurled down into the proletariat by the action of competition, and, as modern industry develops, they even see the moment approaching when they will completely disappear as an independent section of modern society, to be replaced, in manufactures, agriculture and commerce, by overlookers, bailiffs and shopmen.

In countries like France, where the peasants constitute far more than half of the population, it was natural that writers who sided with the proletariat against the bourgeoisie, should use, in their criticism of the bourgeois regime, the standard of the peasant and petty bourgeois, and from the standpoint of these intermediate classes should take up the cudgels for the working class. Thus arose petty-bourgeois Socialism. Sismondi was the head of this school, not only in France but also in England.

This school of Socialism dissected with great acuteness the contradictions in the conditions of modern production. It laid bare the hypocritical apologies of economists. It proved, incontrovertibly, the disastrous effects of machinery and division of labour; the concentration of capital and land in a few hands; overproduction and crises; it pointed out the inevitable ruin of the petty bourgeois and peasant, the misery of the proletariat, the anarchy in production, the crying inequalities in the distribution of wealth, the industrial war of extermination between nations, the dissolution of old moral bonds, of the old family relations, of the old nationalities.

In its positive aims, however, this form of Socialism aspires either to restoring the old means of production and of exchange, and with them the old property relations, and the old society, or to cramping the modern means of production and of exchange, within the framework of the old property relations that have been, and were bound to be, exploded by those means. In either case, it is both reactionary and Utopian.

Its last words are: corporate guilds for manufacture, patriarchal relations in agriculture.

Ultimately, when stubborn historical facts had dispersed all intoxicating effects of self-deception, this form of Socialism ended in a miserable fit of the blues.

\subsubsection{German, or "True," Socialism}
The Socialist and Communist literature of France, a literature that originated under the pressure of a bourgeoisie in power, and that was the expression of the struggle against this power, was introduced into Germany at a time when the bourgeoisie, in that country, had just begun its contest with feudal absolutism.

German philosophers, would-be philosophers, and beaux esprits, eagerly seized on this literature, only forgetting, that when these writings immigrated from France into Germany, French social conditions had not immigrated along with them. In contact with German social conditions, this French literature lost all its immediate practical significance, and assumed a purely literary aspect. Thus, to the German philosophers of the eighteenth century, the demands of the first French Revolution were nothing more than the demands of "Practical Reason" in general, and the utterance of the will of the revolutionary French bourgeoisie signified in their eyes the law of pure Will, of Will as it was bound to be, of true human Will generally.

The world of the German literate consisted solely in bringing the new French ideas into harmony with their ancient philosophical conscience, or rather, in annexing the French ideas without deserting their own philosophic point of view.

This annexation took place in the same way in which a foreign language is appropriated, namely, by translation.

It is well known how the monks wrote silly lives of Catholic Saints over the manuscripts on which the classical works of ancient heathendom had been written. The German literate reversed this process with the profane French literature. They wrote their philosophical nonsense beneath the French original. For instance, beneath the French criticism of the economic functions of money, they wrote "Alienation of Humanity," and beneath the French criticism of the bourgeois State they wrote "dethronement of the Category of the General," and so forth.

The introduction of these philosophical phrases at the back of
the French historical criticisms they dubbed "Philosophy of
Action," "True Socialism," "German Science of Socialism,"
"Philosophical Foundation of Socialism," and so on.

The French Socialist and Communist literature was thus completely emasculated. And, since it ceased in the hands of the German to express the struggle of one class with the other, he felt conscious of having overcome "French one-sidedness" and of representing, not true requirements, but the requirements of truth; not the interests of the proletariat, but the interests of Human Nature, of Man in general, who belongs to no class, has no reality, who exists only in the misty realm of philosophical fantasy.

This German Socialism, which took its schoolboy task so seriously and solemnly, and extolled its poor stock-in-trade in such mountebank fashion, meanwhile gradually lost its pedantic innocence.

The fight of the German, and especially, of the Prussian bourgeoisie, against feudal aristocracy and absolute monarchy, in other words, the liberal movement, became more earnest.

By this, the long wished-for opportunity was offered to "True" Socialism of confronting the political movement with the Socialist demands, of hurling the traditional anathemas against liberalism, against representative government, against bourgeois competition, bourgeois freedom of the press, bourgeois legislation, bourgeois liberty and equality, and of preaching to the masses that they had nothing to gain, and everything to lose, by this bourgeois movement. German Socialism forgot, in the nick of time, that the French criticism, whose silly echo it was, presupposed the existence of modern bourgeois society, with its corresponding economic conditions of existence, and the political constitution adapted thereto, the very things whose attainment was the object of the pending struggle in Germany.

To the absolute governments, with their following of parsons, professors, country squires and officials, it served as a welcome scarecrow against the threatening bourgeoisie.

It was a sweet finish after the bitter pills of floggings and bullets with which these same governments, just at that time, dosed the German working-class risings.

While this "True" Socialism thus served the governments as a weapon for fighting the German bourgeoisie, it, at the same time, directly represented a reactionary interest, the interest of the German Philistines. In Germany the petty-bourgeois class, a relic of the sixteenth century, and since then constantly cropping up again under various forms, is the real social basis of the existing state of things.

To preserve this class is to preserve the existing state of things in Germany. The industrial and political supremacy of the bourgeoisie threatens it with certain destruction; on the one hand, from the concentration of capital; on the other, from the rise of a revolutionary proletariat. "True" Socialism appeared to kill these two birds with one stone. It spread like an epidemic.

The robe of speculative cobwebs, embroidered with flowers of rhetoric, steeped in the dew of sickly sentiment, this transcendental robe in which the German Socialists wrapped their sorry "eternal truths," all skin and bone, served to wonderfully increase the sale of their goods amongst such a public. And on its part, German Socialism recognised, more and more, its own calling as the bombastic representative of the petty-bourgeois Philistine.

It proclaimed the German nation to be the model nation, and the German petty Philistine to be the typical man. To every villainous meanness of this model man it gave a hidden, higher, Socialistic interpretation, the exact contrary of its real character. It went to the extreme length of directly opposing the "brutally destructive" tendency of Communism, and of proclaiming its supreme and impartial contempt of all class struggles. With very few exceptions, all the so-called Socialist and Communist publications that now (1847) circulate in Germany belong to the domain of this foul and enervating literature.

\subsection{CONSERVATIVE, OR BOURGEOIS, SOCIALISM}
A part of the bourgeoisie is desirous of redressing social grievances, in order to secure the continued existence of bourgeois society.

To this section belong economists, philanthropists, humanitarians, improvers of the condition of the working class, organisers of charity, members of societies for the prevention of cruelty to animals, temperance fanatics, hole-and-corner reformers of every imaginable kind. This form of Socialism has, moreover, been worked out into complete systems.

We may cite Proudhon's Philosophie de la Misere as an example of this form.

The Socialistic bourgeois want all the advantages of modern social conditions without the struggles and dangers necessarily resulting therefrom. They desire the existing state of society minus its revolutionary and disintegrating elements. They wish for a bourgeoisie without a proletariat. The bourgeoisie naturally conceives the world in which it is supreme to be the best; and bourgeois Socialism develops this comfortable conception into various more or less complete systems. In requiring the proletariat to carry out such a system, and thereby to march straightway into the social New Jerusalem, it but requires in reality, that the proletariat should remain within the bounds of existing society, but should cast away all its hateful ideas concerning the bourgeoisie.

A second and more practical, but less systematic, form of this Socialism sought to depreciate every revolutionary movement in the eyes of the working class, by showing that no mere political reform, but only a change in the material conditions of existence, in economic relations, could be of any advantage to them. By changes in the material conditions of existence, this form of Socialism, however, by no means understands abolition of the bourgeois relations of production, an abolition that can be effected only by a revolution, but administrative reforms, based on the continued existence of these relations; reforms, therefore, that in no respect affect the relations between capital and labour, but, at the best, lessen the cost, and simplify the administrative work, of bourgeois government.

Bourgeois Socialism attains adequate expression, when, and only when, it becomes a mere figure of speech.

Free trade: for the benefit of the working class. Protective duties: for the benefit of the working class. Prison Reform: for the benefit of the working class. This is the last word and the only seriously meant word of bourgeois Socialism.

It is summed up in the phrase: the bourgeois is a bourgeois--for the benefit of the working class.

\subsection{CRITICAL-UTOPIAN SOCIALISM AND COMMUNISM}
We do not here refer to that literature which, in every great modern revolution, has always given voice to the demands of the proletariat, such as the writings of Babeuf and others.

The first direct attempts of the proletariat to attain its own ends, made in times of universal excitement, when feudal society was being overthrown, these attempts necessarily failed, owing to the then undeveloped state of the proletariat, as well as to the absence of the economic conditions for its emancipation, conditions that had yet to be produced, and could be produced by the impending bourgeois epoch alone. The revolutionary literature that accompanied these first movements of the proletariat had necessarily a reactionary character. It inculcated universal asceticism and social levelling in its crudest form.

The Socialist and Communist systems properly so called, those of Saint-Simon, Fourier, Owen and others, spring into existence in the early undeveloped period, described above, of the struggle between proletariat and bourgeoisie (see Section 1. Bourgeois and Proletarians).

The founders of these systems see, indeed, the class antagonisms, as well as the action of the decomposing elements, in the prevailing form of society. But the proletariat, as yet in its infancy, offers to them the spectacle of a class without any historical initiative or any independent political movement.

Since the development of class antagonism keeps even pace with the development of industry, the economic situation, as they find it, does not as yet offer to them the material conditions for the emancipation of the proletariat. They therefore search after a new social science, after new social laws, that are to create these conditions.

Historical action is to yield to their personal inventive action, historically created conditions of emancipation to fantastic ones, and the gradual, spontaneous class-organisation of the proletariat to the organisation of society specially contrived by these inventors. Future history resolves itself, in their eyes, into the propaganda and the practical carrying out of their social plans.

In the formation of their plans they are conscious of caring chiefly for the interests of the working class, as being the most suffering class. Only from the point of view of being the most suffering class does the proletariat exist for them.

The undeveloped state of the class struggle, as well as their own surroundings, causes Socialists of this kind to consider themselves far superior to all class antagonisms. They want to improve the condition of every member of society, even that of the most favoured. Hence, they habitually appeal to society at large, without distinction of class; nay, by preference, to the ruling class. For how can people, when once they understand their system, fail to see in it the best possible plan of the best possible state of society?

Hence, they reject all political, and especially all revolutionary, action; they wish to attain their ends by peaceful means, and endeavour, by small experiments, necessarily doomed to failure, and by the force of example, to pave the way for the new social Gospel.

Such fantastic pictures of future society, painted at a time when the proletariat is still in a very undeveloped state and has but a fantastic conception of its own position correspond with the first instinctive yearnings of that class for a general reconstruction of society.

But these Socialist and Communist publications contain also a critical element. They attack every principle of existing society. Hence they are full of the most valuable materials for the enlightenment of the working class. The practical measures proposed in them--such as the abolition of the distinction between town and country, of the family, of the carrying on of industries for the account of private individuals, and of the wage system, the proclamation of social harmony, the conversion of the functions of the State into a mere superintendence of production, all these proposals, point solely to the disappearance of class antagonisms which were, at that time, only just cropping up, and which, in these publications, are recognised in their earliest, indistinct and undefined forms only. These proposals, therefore, are of a purely Utopian character.

The significance of Critical-Utopian Socialism and Communism bears an inverse relation to historical development. In proportion as the modern class struggle develops and takes definite shape, this fantastic standing apart from the contest, these fantastic attacks on it, lose all practical value and all theoretical justification. Therefore, although the originators of these systems were, in many respects, revolutionary, their disciples have, in every case, formed mere reactionary sects. They hold fast by the original views of their masters, in opposition to the progressive historical development of the proletariat. They, therefore, endeavour, and that consistently, to deaden the class struggle and to reconcile the class antagonisms. They still dream of experimental realisation of their social Utopias, of founding isolated "phalansteres," of establishing "Home Colonies," of setting up a "Little Icaria"---duodecimo editions of the New Jerusalem---and to realise all these castles in the air, they are compelled to appeal to the feelings and purses of the bourgeois. By degrees they sink into the category of the reactionary conservative Socialists depicted above, differing from these only by more systematic pedantry, and by their fanatical and superstitious belief in the miraculous effects of their social science.

They, therefore, violently oppose all political action on the part of the working class; such action, according to them, can only result from blind unbelief in the new Gospel.

The Owenites in England, and the Fourierists in France, respectively, oppose the Chartists and the Reformistes.

\section{POSITION OF THE COMMUNISTS IN RELATION TO THE VARIOUS EXISTING OPPOSITION PARTIES}
\small{\textbf{Section II has made clear the relations of the Communists to the existing working-class parties, such as the Chartists in England and the Agrarian Reformers in America.}}

The Communists fight for the attainment of the immediate aims, for the enforcement of the momentary interests of the working class; but in the movement of the present, they also represent and take care of the future of that movement. In France the Communists ally themselves with the Social-Democrats, against the conservative and radical bourgeoisie, reserving, however, the right to take up a critical position in regard to phrases and illusions traditionally handed down from the great Revolution.

In Switzerland they support the Radicals, without losing sight of the fact that this party consists of antagonistic elements, partly of Democratic Socialists, in the French sense, partly of radical bourgeois.

In Poland they support the party that insists on an agrarian revolution as the prime condition for national emancipation, that party which fomented the insurrection of Cracow in 1846.

In Germany they fight with the bourgeoisie whenever it acts in a revolutionary way, against the absolute monarchy, the feudal squirearchy, and the petty bourgeoisie.

But they never cease, for a single instant, to instil into the working class the clearest possible recognition of the hostile antagonism between bourgeoisie and proletariat, in order that the German workers may straightaway use, as so many weapons against the bourgeoisie, the social and political conditions that the bourgeoisie must necessarily introduce along with its supremacy, and in order that, after the fall of the reactionary classes in Germany, the fight against the bourgeoisie itself may immediately begin.

The Communists turn their attention chiefly to Germany, because that country is on the eve of a bourgeois revolution that is bound to be carried out under more advanced conditions of European civilisation, and with a much more developed proletariat, than that of England was in the seventeenth, and of France in the eighteenth century, and because the bourgeois revolution in Germany will be but the prelude to an immediately following proletarian revolution.

In short, the Communists everywhere support every revolutionary movement against the existing social and political order of things.

In all these movements they bring to the front, as the leading question in each, the property question, no matter what its degree of development at the time.

Finally, they labour everywhere for the union and agreement of the democratic parties of all countries.

The Communists disdain to conceal their views and aims.\\
They openly declare that their ends can be attained only by
the forcible overthrow of all existing social conditions.
Let the ruling classes tremble at a Communistic revolution.\\
The proletarians have nothing to lose but their chains.\\
They have a world to win.

\large{\textbf{WORKING MEN OF ALL COUNTRIES, UNITE!}}

\vfill

\textit{Transcribed by Allen Lutins with assistance from Jim Tarzia.}
'''
    

latexc = tempfile.NamedTemporaryFile() # DO NOT Erase this line. Temporary file for LaTeX storage.
#try:
#    print 'temp:', temp
#    print 'temp.name:', temp.name
fileName=latexc.name

latextextfile=open('output.tex','w')
# Important! To prevent file permissions error, create output.tex file and give all permissions to all users
#            modify both processor.py and output.tex -> This is not secure, but things work smoothly this way.
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def checkIfFile():
    global filePath
    filePath = 'pages/'+id_generator()+'.html'
    if os.path.isfile(filePath):
        return checkIfFile()
    else:
        return filePath       
    
latexhtmlfile=open(checkIfFile(),'w')
# Important! To prevent file permissions error, create output.html file and give all permissions to all users
#            modify both processor.py and output.html -> This is not secure, but things work smoothly this way.

# An MLA Name Breaker:
def namebreak():
	namelist=author.split(' ') # This assumes that the name is separated properly by spaces.
	global fname
	fname=' '.join(namelist[:-1]) # This assumes that the first name(s) is (are) supplied first in the query page.
	global lname
	lname=namelist[-1] # This assumes that the last name is next and last.
	if fname=="":
		fname="FirstName?"
if docFormat == "MLA":
	namebreak()

# Quotation mark Correcter:
def qcorrecter(string):
	yandex0=False
	yandex1=False
	for x in string:
		if x == '"' and yandex0==False:
			string.replace(x,"``")
			yandex0=True
		if x == '"' and yandex0==True:
			string.replace(x,"''")
			yandex0=False
		if x == '“':
			string.replace(x,"``")
		if x == '”':
			string.replace(x,"''")
		if x == "'" and yandex1==False:
			string.replace(x,"`")
			yandex1=True
		if x == "'" and yandex1==True:
			yandex1=False
		if x == "‘":
			string.replace(x,"`")
		if x == "’":
			string.replace(x,"'")
	return(string)

def easyMark(string):
	for x in range(len(string)):
		if string[x]=="~":
			# Making Lists:
			if string[x:x+11]=="~start-list":
				string=string[:x]+"\begin{enumerate}"+string[x+11:]
			if string[x:x+9]=="~end-list":
				string=string[:x]+"\end{enumerate}"+string[x+9:]
			if string[x:x+2]=="~ ":
				string=string[:x]+"\item "+string[x+2:]
			if string[x:x+14]=="~start-bullets":
				string=string[:x]+"\begin{itemize}"+string[x+14:]
			if string[x:x+12]=="~end-bullets":
				string=string[:x]+"\end{itemize}"+string[x+12:]
			if string[x:x+18]=="~start-custom-list":
				string=string[:x]+"\begin{description}"+string[x+18:]
			if string[x:x+16]=="~end-custom-list":
				string=string[:x]+"\end{description}"+string[x+16:]
			# Structuring Your Paper:
			if string[x:x+10]=="~chapter [":
				yandexf=string.find("]", x+10)
				string=string[:x]+"\chapter{"+string[x+10:yandexf]+"}"+string[yandexf+1:]
			# easyMark is failing in actually working!
	return(string)

mlapackager=""
mla=""
maketitle="\maketitle"
mlastop=""
apaAffiliation=""
documentclassb=""
graphicxstopper=""

articleclass="article"
# Document Formatting Changes:
if docFormat == "Standard" or fxn=="pdf":
	documentclassb=fontsize+", oneside"
elif docFormat == "Turabian (Standard)":
	articleclass="turabian-formatting"
	documentclassb=fontsize
elif docFormat == "Turabian (Research Paper)":
	articleclass="turabian-researchpaper"
	documentclassb=fontsize
elif docFormat == "Turabian (Thesis or Dissertation)":
	articleclass="turabian-thesis"
	documentclassb=fontsize
elif docFormat == "APA":
	articleclass="apa6" # http://ctan.mackichan.com/macros/latex/contrib/apa6/apa6.pdf
	apaAffiliation=r"\affiliation{"+affiliation+"}"
	apaAbstract="\abstract{"+abstract+"}" #Warning! New abstract needs to be added to query page!
	apaKeywords="\keywords{"+keywords+"}"
elif docFormat == "MLA":
	articleclass="article"
	mlapackager="\usepackage{mla}"
	mla=r"\begin{mla}{"+fname+"}{"+lname+"}{"+Plname+"}{"+Classname+"}{"+date+"}{"+title+"}"
	#Warning!: Professor name (Plname) needs to be added to query page!
	maketitle=""
	mlastop="\end{mla}"
	graphicxstopper="%"

#Important edits for documentclass:
if not documentclassb=="":
	documentclassb="["+documentclassb+"]"
	
#Landscaping:
if landscape=="True":
	lsss=""
else:
	lsss="%"

# Begin paragraphs with an empty line rathen than an indent:
if parseSkip=="True":
	psss=''
else:
	psss="%"

# Quotation marks corrections
if qCorrect=="True":
	qcorrecter(author)
	qcorrecter(title)
	qcorrecter(date)
	#qcorrecter(starterText)
	qcorrecter(bodyText)
	# Any more fields need to have quotation marks corrected?

lbasic='''
\documentclass'''+documentclassb+'''{'''+articleclass+'''}   	% use "amsart" instead of "article" for AMSLaTeX format
\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
\geometry{'''+paperstyle+'''}                   		% ... or a4paper or a5paper or ... 
'''+lsss+'''\geometry{landscape}                		% Activate for rotated page geometry
'''+psss+'''\usepackage[parfill]{parskip}    		% Activate to begin paragraphs with an empty line rather than an indent
'''+graphicxstopper+'''\usepackage{graphicx}				% Use pdf, png, jpg, or epsÂ§ with pdflatex; use eps in DVI mode
								% TeX will automatically convert eps --> pdf in pdflatex		
\usepackage{amssymb}

%SetFonts

%SetFonts


'''+r"\title{"+title+r'''}
\author{'''+author+'''}
'''+apaAffiliation+r'''
\date{'''+date+'''}							% Activate to display a given date or no date

'''+mlapackager+r'''

\begin{document}
'''+maketitle+'''
'''+mla+'''
%\section{}
%\subsection{}
'''+bodyText+'''

'''+mlastop+'''
\end{document}  	
'''
# string concatenation needs to be on the same line!

#finally:     got rid of finally because that's not needed unless an exception is thrown and if an exception if thrown and you want to use finally you need a try statement
    # Automatically cleans up the file

# print 'Exists after close:', os.path.exists(temp.name)

#subprocess.call(['shell scripts/convertToPDF.sh', str(fileName)])
# above statement will need the temp file as fileName for it to be passed to the shell script

# for pdfs and webpages \includegraphics needs to be changed so that images are displayed. NOTE images from the TeX code will not work unless saved in local dir
bodyTextSplit = bodyText.split('\n')
for lin in range(len(bodyTextSplit)):
    if bodyTextSplit[lin].startswith(r'\includegraphics{'):
        url = bodyTextSplit[lin][17:-1]
        if url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png') or url.endswith('.gif') or url.endswith('.svg'):
            os.chdir('images')
            subprocess.Popen("wget "+url, shell=True)
            os.chdir('../')
            parts = url.split("/")
            url = 'images/'+parts[len(parts)-1]
            bodyTextSplit[lin] = r'\includegraphics{'+url+'}'
bodyText = '\n'.join(bodyTextSplit)        
        
    
bodytextHTML = bodyText
bodytextHTML = bodytextHTML.replace(r'\begin{enumerate}', '<ol>')
bodytextHTML = bodytextHTML.replace(r'\ldots', '')
bodytextHTML = bodytextHTML.replace(r'\vfill', '')
bodytextHTML = bodytextHTML.replace('\end{enumerate}', '</ol>')
bodysplit = bodytextHTML.split('\n')
for line in range(len(bodysplit)):
    if bodysplit[line].startswith('\item'):
        bodysplit[line] = '<li>'+bodysplit[line][5:]+'</li>'
    if bodysplit[line].startswith('\section{'):
        bodysplit[line] = '<h3>'+bodysplit[line][9:-1] + '</h3>'
    if bodysplit[line].startswith(r'\textit{'):
        bodysplit[line] = '<i>'+bodysplit[line][8:-1] + '</i>'
    if bodysplit[line].startswith('\subsection{'):
        bodysplit[line] = '<h3><small>'+bodysplit[line][12:-1] + '</small></h3>'
    if bodysplit[line].startswith('\subsubsection{'):
        bodysplit[line] = '<h4>'+bodysplit[line][15:-1] + '</h4>'
    if bodysplit[line].startswith(r'\large{'):
        bodysplit[line] = '<span class="spec">'+bodysplit[line][7:-1] + '</span>'
    if bodysplit[line].find(r'\textbf{') != -1:
        bodysplit[line] = bodysplit[line][:bodysplit[line].index(r'\textbf{')]+'<b>'+bodysplit[line][bodysplit[line].index(r'\textbf{')+1:] +'</b>'
bodytextHTML = '<br>'.join(bodysplit)        

stuff = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>'''+title+'''</title>
        <meta name="author" content="'''+author+'''">
        <meta name="description" content="'''+abstract+'''">
        <meta name="keywords" content="'''+keywords+'''">
        <script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>
        <script src="js/renderer.js"></script>
        <style>
            @font-face { font-family: latex; src: url('../fonts/cmunrm.ttf'); }
            body {
                font-family: latex, serif;
                margin-left: 50px;
                margin-right: 50px;
            }
            h1, h2 {
                text-align: center;
            }
            .spec {
                font-size: 18px;
            }
        </style>    
    </head>
    <body>
'''+'<h1>'+title+'</h1>'+'<h2>'+author+'<br>'+keywords+'</h2>'+bodytextHTML+'''
    </body>
</html>    
'''

latexc.write(lbasic)
latextextfile.write(lbasic)
latextextfile.close()
latexhtmlfile.write(stuff)
latexhtmlfile.close()
# def makepdf():
#     subprocess.Popen("pdflatex output", shell=True)
if fxn=="pdf":
    subprocess.Popen("pdflatex output", shell=True)
    print "Location: output.pdf\r\n"

easystuff = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Generated</title>
        <meta charset="UTF-8">    
'''

morestuff = '''
    </head>
    <body>
    </body>
</html>    
'''


# Requires JavaScript? Can be avoided! see megatex()
redirectTEX = '<script>window.location.href="output.tex";</script>'
redirectPDF = '<script>window.location.href="output.pdf";</script>'
redirectHTML = '<script>window.location.href="output.html";</script>'

# Document Handling:
# !! texman() is deprecated.
def texman():
    print HTML_HEADER
    if fxn == "tex":
        g = open('output.tex', 'w')
        g.write(lbasic)
        g.close()
        TELE = redirectTEX+morestuff
        print TELE
    if fxn == "pdf":
        g = open('output.tex', 'w')
        g.write(lbasic)
        g.close()
        subprocess.call(["./convertToPDF.sh"])
        TELE = redirectPDF+morestuff
        print TELE
    else:
        g = open('output.html', 'wU')
        g.write(stuff)
        TELE = redirectHTML+morestuff
        print TELE
    #print texplainheader
	# Or, use the latexc file that has lbasic written in.
#texman()
## !! texman() is depreceated.

def megatex():
    print "Location: output.tex\r\n"
if fxn=="tex":
    megatex()
# def pdftex():
#     subprocess.call(["./convertToPDF.sh"])
#     print "Location: output.pdf\r\n"
# if fxn=="pdf":
#     pdftex()
def htmltex():
    print "Location: "+filePath+"\r\n"
if fxn=="webpage" and lbasic.find('<script') == -1:
    htmltex()
else:
    print "<!DOCTYPE html><head><title>You dun goofed.</title></head><body>Your query was messed up or you tried to do stuff you weren't supposed to do.</body></html>"

# def pdftex():
#     print "Location: google.com\r\n"
# if fxn=="pdf":
#     pdftex()

# Let's close this file at the very end:
latexc.close()
