# -*- coding: utf-8 -*-
"""Growth-corridor suburbs: new estates, and what goes wrong in them."""

FEE = ("No. Call out is free and so is the quote, at any hour, anywhere we service. "
       "You are told what the job involves and what it will cost before any work starts, "
       "so nothing on the invoice comes as a surprise.")
LIC = ("Yes. Every job is carried out by a licensed plumber, backed by insurance and completed "
       "to Australian plumbing standards. Our licence number and ABN are at the bottom of every "
       "page on this site.")
AH = ("Yes, 24 hours a day and 7 days a week, including public holidays, at no extra call out "
      "charge. Burst pipes, gas leaks, sewer overflows and dead hot water units do not keep "
      "business hours.")
WARRANTY = ("Check your builder warranty first. On a newer home the builder may be liable for the "
            "repair, and getting your own plumber in can affect that. Call and describe it and we "
            "will tell you honestly whether it is a builder problem or a plumbing one - that "
            "conversation costs nothing.")
DEBRIS = ("Almost always construction debris - render, sand or offcuts left in the line when the "
          "house was built and never flushed out. It is not something that clears itself. A camera "
          "confirms it and a jetter removes it, and once it is out the drain runs properly for good.")

def council_q(sub, council):
    return ("Which council area is this?",
            "%s sits in the %s area, and Sydney Water handles the water and sewer mains. For most "
            "household jobs it makes no difference, but it matters on anything touching the sewer "
            "main or needing approval, and we will tell you upfront if your job is one of those."
            % (sub, council))

SUBS = [

{
 'slug': 'plumber-schofields', 'name': 'Schofields', 'pc': '2765',
 'title': 'Plumber Schofields | 24/7 Emergency | Straight Away Plumbing',
 'og': 'Plumber Schofields | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing Schofields 2765. Blocked drains, hot water, burst pipes and gas fitting. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing Schofields NSW 2765. Blocked drains, hot water systems, burst and leaking pipes, gas fitting and 24/7 emergency callouts, with no call out fee.',
 'hero': 'Licensed plumbing across Schofields and the North West - 24 hours a day, with no call out fee and free quotes. Call and we will tell you straight away when we can be there.',
 'h2': 'New Estates and Old Acreage, Side by Side',
 'paras': [
   'Schofields has two halves, and they break in completely different ways. The estates around the station went up in the last ten or fifteen years. Head toward Riverstone and you are into older homes and acreage that were here long before any of it.',
   'On the new side it is builder-grade fittings giving out early, drains that never ran properly because something was left in the line during construction, and gas or hot water fit-off signed off in a hurry. On the older side it is tree roots, tired pipework and hot water units nobody has thought about in a decade.',
   'Worth knowing which one you are dealing with before anybody starts pulling things apart - because on a newer home, the fix may not be yours to pay for at all.',
 ],
 'cards_intro': 'A fast-growing suburb with housing from two very different eras, and a fairly predictable set of jobs from each.',
 'cards': [
   ('house', 'Builder-grade fittings failing early', 'Tapware, flexible hoses and cistern parts chosen to hit a price rather than to last. They tend to go within the first few years. Replacing them with something decent costs little more than repairing them twice.'),
   ('drain', 'Drains blocked since day one', 'If a drain has never run properly, it is usually debris left in the line during construction - render, sand, offcuts. A camera finds it and a jetter clears it, and it does not come back.'),
   ('shield', 'Builder warranty questions', 'On a newer home the builder may be liable, and calling your own plumber can affect that. Tell us what is happening and we will say honestly whether it is a warranty claim or a plumbing job.'),
   ('jet', 'Tree roots on the older side', 'Toward Riverstone the sewer lines are old earthenware with fifty-year-old trees over them. Roots get into the joints and catch everything. Jetted out, then a camera to see whether the pipe is still sound.'),
   ('hot', 'Hot water, new and old', 'The first wave of estate systems is reaching the age where they start to fail, and the older homes are well past it. We repair what will hold and replace what will not.'),
   ('gas', 'Gas fit-off and new appliances', 'Cooktops, heaters, hot water and BBQ points, connected and leak tested to code - including the ones the original build left off the list.'),
 ],
 'nearby_eyebrow': 'Around the North West',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-the-ponds', 'plumber-tallawong', 'plumber-riverstone', 'plumber-quakers-hill', 'plumber-marsden-park', 'plumber-rouse-hill'],
 'faqs': [
   ('Do you charge a call out fee in Schofields?', FEE),
   ('My house is only a few years old. Should I call you or the builder?', WARRANTY),
   ('A drain in my new place has never run properly. What is that?', DEBRIS),
   ('Do you come out to Schofields after hours?', AH),
   council_q('Schofields', 'Blacktown City Council'),
   ('Are you licensed and insured?', LIC),
 ],
},

{
 'slug': 'plumber-the-ponds', 'name': 'The Ponds', 'pc': '2769',
 'title': 'Plumber The Ponds | 24/7 Emergency | Straight Away Plumbing',
 'og': 'Plumber The Ponds | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing The Ponds 2769. Hot water, blocked drains, burst pipes and gas fitting. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing The Ponds NSW 2769. Hot water systems, blocked drains, burst and leaking pipes, gas fitting and 24/7 emergency callouts, with no call out fee.',
 'hero': 'Licensed plumbing across The Ponds - 24 hours a day, with no call out fee and free quotes. Call and we will tell you straight away when we can be there.',
 'h2': 'A Master-Planned Suburb Hitting Its Teens',
 'paras': [
   'The Ponds was built out in one go, which means most of it is the same age. Everything installed at the same time also tends to fail at the same time.',
   'That stage has arrived. Hot water systems that went in with the houses are well into their second decade, original tapware and flexible hoses are past their useful life, and the first round of bathrooms is starting to come out.',
   'Small lots and big roofs also put a lot of water into a short stormwater run, which is its own set of problems every time there is a proper downpour.',
 ],
 'cards_intro': 'A suburb built all at once, now reaching the age where the original fit-out starts giving up all at once too.',
 'cards': [
   ('hot', 'Original hot water systems', 'A storage unit gets ten to fifteen years. Most of The Ponds installed them within a few years of each other, so they are reaching the end together. We will tell you whether a repair will actually hold.'),
   ('tap', 'Failing flexible hoses', 'The braided hoses under sinks and vanities perish, and when one lets go it empties the mains into your house until somebody finds the stop tap. Cheap to replace, expensive to ignore.'),
   ('storm', 'Stormwater on a small lot', 'Big roof, small block, short run to the street. When the line packs up with leaf and grit the water comes over the gutters and down the wall instead. Better cleared before a storm than during one.'),
   ('drain', 'Blocked kitchen and laundry lines', 'Ten years of fat, grit and detergent narrows a waste line until it stops. A jetter takes it back to full bore, which a plunger never will.'),
   ('reno', 'First-round renovations', 'Original bathrooms and kitchens are starting to come out across the suburb. We handle the full plumbing scope, rough-in to fit-off, working in with your builder.'),
   ('gas', 'Gas appliances and BBQ points', 'Cooktops, heaters and outdoor points installed and leak tested to code, including connections the original build never ran.'),
 ],
 'nearby_eyebrow': 'Around the North West',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-schofields', 'plumber-tallawong', 'plumber-kellyville-ridge', 'plumber-riverstone', 'plumber-rouse-hill', 'plumber-quakers-hill'],
 'faqs': [
   ('Do you charge a call out fee in The Ponds?', FEE),
   ('My hot water system is about fifteen years old. Repair or replace?', 'Depends what has failed. A thermostat or an element is worth replacing on a unit that age. A leaking tank is not - once the cylinder goes, it is done, and money spent on it is money wasted. We will tell you which one you have before you commit to anything.'),
   ('What are the braided hoses under my sink and should I worry about them?', 'They are the flexible connectors between the stop taps and the tapware, and they have a finite life. When one fails it runs at full mains pressure, usually while nobody is home. On a house of this age they are worth checking, and replacing them is a small job.'),
   ('Do you come out to The Ponds after hours?', AH),
   council_q('The Ponds', 'Blacktown City Council'),
   ('Are you licensed and insured?', LIC),
 ],
},

{
 'slug': 'plumber-tallawong', 'name': 'Tallawong', 'pc': '2762',
 'title': 'Plumber Tallawong | 24/7 Emergency | Straight Away Plumbing',
 'og': 'Plumber Tallawong | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing Tallawong 2762. Units, townhouses and new builds - blocked drains, hot water, leaks. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing Tallawong NSW 2762, including apartments and townhouses. Blocked drains and shared stacks, hot water systems, leaks and 24/7 emergency callouts, with no call out fee.',
 'hero': 'Licensed plumbing across Tallawong - houses, townhouses and apartments, 24 hours a day, with no call out fee and free quotes.',
 'h2': 'New Buildings, New Building Problems',
 'paras': [
   'Tallawong is about as new as Sydney gets, and a good deal of it is townhouses and apartments rather than freestanding houses. That changes the plumbing entirely.',
   'In a building with shared walls and shared stacks, your problem is often not your problem. A blockage two floors up shows itself in your bathroom, and the repair may be common property rather than yours to pay for.',
   'On the brand-new side it is defects: fittings never finished properly, waste lines with debris still sitting in them, and hot water that has never worked the way it should.',
 ],
 'cards_intro': 'A mix of brand-new houses and strata buildings, which means two completely different sets of problems.',
 'cards': [
   ('block', 'Shared stacks and common property', 'In a unit, a blockage in the stack shows up in the lowest bathroom on the line - which is often not the one causing it. We find where it actually is, and tell you whether it is yours or the building\'s before anybody starts paying.'),
   ('drain', 'Construction debris in the lines', 'On brand-new work, a drain that has never run right usually has render, sand or offcuts in it. A camera confirms it and a jetter clears it for good.'),
   ('shield', 'New-build defects and warranty', 'If the place is still under builder or developer warranty, the repair may not be yours to pay for. Call and describe it and we will tell you honestly which it is.'),
   ('hot', 'Hot water that never worked properly', 'Undersized, badly plumbed, or never commissioned correctly. Common on new work and usually fixable without replacing the unit.'),
   ('tap', 'Leaking taps and cistern parts', 'The first fittings to go into a new build are the cheapest ones on the schedule. Replaced with something that will actually last.'),
   ('alert', 'Emergencies in a strata building', 'Water travels in apartments, and it travels fast. We are on call 24 hours, and we will work in with your building manager or strata agent.'),
 ],
 'nearby_eyebrow': 'Around the North West',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-schofields', 'plumber-the-ponds', 'plumber-rouse-hill', 'plumber-box-hill', 'plumber-riverstone', 'plumber-kellyville-ridge'],
 'faqs': [
   ('Do you charge a call out fee in Tallawong?', FEE),
   ('I am in an apartment. Is a blocked drain my problem or the building\'s?', 'It depends where the blockage actually is. Inside your own fixtures and branch lines it is normally yours. In the shared stack or the common drainage it is normally the building\'s. We find out which before anybody commits to paying for it, and we are happy to put that in writing for your strata manager.'),
   ('Do you work with strata managers and building managers?', 'Yes, regularly. Tell us who is handling it and we will deal with them directly. For common property work we will provide what they need to approve it.'),
   ('My place is brand new. Should I call you or the developer?', WARRANTY),
   ('Do you come out to Tallawong after hours?', AH),
   ('Are you licensed and insured?', LIC),
 ],
},

{
 'slug': 'plumber-marsden-park', 'name': 'Marsden Park', 'pc': '2765',
 'title': 'Plumber Marsden Park | 24/7 Emergency | Straight Away Plumbing',
 'og': 'Plumber Marsden Park | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing Marsden Park 2765. New builds, blocked drains, hot water, gas connections. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing Marsden Park NSW 2765. Blocked drains, new gas and water connections, hot water systems, burst pipes and 24/7 emergency callouts, with no call out fee.',
 'hero': 'Licensed plumbing across Marsden Park - 24 hours a day, with no call out fee and free quotes. Call and we will tell you straight away when we can be there.',
 'h2': 'A Suburb Still Under Construction',
 'paras': [
   'Marsden Park is still going up. Whole streets are finished while the next ones are still slabs, and that mix creates its own problems.',
   'Active construction means debris in drainage lines, services getting knocked about, and gas and water being run to houses that were paddock a year ago. A fair amount of what we are called to here was created on site rather than by anything the owner did.',
   'The finished side has the usual new-build set: builder-grade fittings, hot water fit-off done at speed, and stormwater that has never really been tested until the first big storm.',
 ],
 'cards_intro': 'Half-built streets and brand-new houses produce a distinctive set of calls.',
 'cards': [
   ('drain', 'Construction debris in drains', 'The most common call out here. Render, sand and offcuts left in the line when the house was built. A camera finds it, a jetter clears it, and it does not come back.'),
   ('shield', 'Builder warranty', 'On a house this new the builder may well be liable. Call and describe it before you commit to anything, and we will tell you honestly which it is.'),
   ('storm', 'Untested stormwater', 'A new stormwater run does not prove itself until a real downpour. If water is coming over the gutters or pooling against the house, it is worth looking at before the next one.'),
   ('gas', 'New gas connections', 'Cooktops, heaters, hot water and BBQ points, run and leak tested to code on houses where the gas was only connected recently.'),
   ('hot', 'Hot water fit-off done at speed', 'Systems installed to a deadline rather than to a standard. Usually fixable without replacing the unit, if somebody actually looks at it properly.'),
   ('pipe', 'Damaged or leaking new pipework', 'Services get knocked about on an active site. We locate the damage, stop the water and repair it properly rather than patching it.'),
 ],
 'nearby_eyebrow': 'Around the North West',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-schofields', 'plumber-riverstone', 'plumber-box-hill', 'plumber-the-ponds', 'plumber-blacktown', 'plumber-tallawong'],
 'faqs': [
   ('Do you charge a call out fee in Marsden Park?', FEE),
   ('My house was finished last year. Should I call you or the builder?', WARRANTY),
   ('A drain has never run properly since we moved in. What is that?', DEBRIS),
   ('Do you come out to Marsden Park after hours?', AH),
   council_q('Marsden Park', 'Blacktown City Council'),
   ('Are you licensed and insured?', LIC),
 ],
},

{
 'slug': 'plumber-box-hill', 'name': 'Box Hill', 'pc': '2765',
 'title': 'Plumber Box Hill | 24/7 Emergency | Straight Away Plumbing',
 'og': 'Plumber Box Hill | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing Box Hill 2765. New estates and rural properties - tanks, pumps, drains, hot water. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing Box Hill NSW 2765, covering new estate homes and rural properties. Rainwater tanks and pumps, blocked drains, hot water systems, gas fitting and 24/7 emergency callouts.',
 'hero': 'Licensed plumbing across Box Hill - new estates and rural properties alike, 24 hours a day, with no call out fee and free quotes.',
 'h2': 'Paddocks Turning Into Streets',
 'paras': [
   'Box Hill was farmland until recently, and parts of it still are. That makes it one of the more mixed places we work - brand-new estate homes on one road, properties that have been here for decades on the next.',
   'The older places often have their own infrastructure: rainwater tanks, pressure pumps, and on-site waste systems rather than a sewer connection. They need a different sort of attention, and someone who has actually worked on one before.',
   'The new side has the standard list - construction debris in the drains, builder-grade fittings, and stormwater runs that have not yet met a serious storm.',
 ],
 'cards_intro': 'Two kinds of property on the same street, and two completely different plumbing jobs.',
 'cards': [
   ('filter', 'Tanks, pumps and filtration', 'Rainwater tanks, pressure pumps and filtration on the properties that are not on mains. Serviced, repaired and replaced.'),
   ('drain', 'Construction debris in new drains', 'On the estate side, a drain that has never run right usually has something in it from the build. A camera confirms it and a jetter clears it.'),
   ('house', 'Older rural pipework', 'Long runs, old materials and joins nobody has looked at in years. Worth knowing where yours actually go before something fails.'),
   ('storm', 'Stormwater on new lots', 'Big roofs on small blocks, with runs that have not been tested. If water is coming over the gutters, worth checking before the next downpour.'),
   ('hot', 'Hot water systems', 'New installs on the estate side, and replacements on the older properties where the existing unit is well past its life.'),
   ('gas', 'Gas fitting', 'Cooktops, heaters, hot water and BBQ points, installed and leak tested to code - including bottled gas on properties without a mains connection.'),
 ],
 'nearby_eyebrow': 'Around The Hills',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-rouse-hill', 'plumber-marsden-park', 'plumber-schofields', 'plumber-kellyville', 'plumber-riverstone', 'plumber-the-ponds'],
 'faqs': [
   ('Do you charge a call out fee in Box Hill?', FEE),
   ('My property is on tank water, not mains. Can you still help?', 'Yes. Tanks, pressure pumps, filtration and the pipework around them are all normal work for us. If the pump is short cycling, the pressure has dropped or the water has changed taste or colour, that is usually the pump or the filtration rather than the tank itself.'),
   ('We are not connected to the sewer. Do you work on on-site waste systems?', 'We do work on the plumbing side of them - the lines running to the system, blockages and failures in that pipework. Tell us what the system is when you call and we will tell you straight away whether the job is ours or whether you need the system\'s own service agent.'),
   ('Do you come out to Box Hill after hours?', AH),
   council_q('Box Hill', 'The Hills Shire'),
   ('Are you licensed and insured?', LIC),
 ],
},

{
 'slug': 'plumber-kellyville-ridge', 'name': 'Kellyville Ridge', 'pc': '2155',
 'title': 'Plumber Kellyville Ridge | 24/7 | Straight Away Plumbing',
 'og': 'Plumber Kellyville Ridge | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing Kellyville Ridge 2155. Hot water, blocked drains, leaking taps, gas fitting. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing Kellyville Ridge NSW 2155. Hot water replacement, blocked drains and tree roots, leaking taps, gas fitting and 24/7 emergency callouts, with no call out fee.',
 'hero': 'Licensed plumbing across Kellyville Ridge - 24 hours a day, with no call out fee and free quotes. Call and we will tell you straight away when we can be there.',
 'h2': 'Twenty Years In, Things Start To Go',
 'paras': [
   'Kellyville Ridge went up in the early 2000s, which puts most of it at the age where the original everything comes due for replacement at roughly the same time.',
   'Hot water systems installed with the houses are now beyond their expected life. Flexible hoses under sinks have perished. Original tapware and cistern parts have been dripping for years. None of it is dramatic, and all of it eventually costs more than dealing with it would have.',
   'The trees planted when the estate was landscaped are also now big enough to matter, which is when roots start finding their way into drainage.',
 ],
 'cards_intro': 'An estate that went up together is now wearing out together, in a fairly predictable order.',
 'cards': [
   ('hot', 'Hot water past its life', 'Twenty-year-old storage units are living on borrowed time. We will tell you straight whether a repair will hold or whether you are better off replacing it.'),
   ('tap', 'Perished flexible hoses', 'The braided hoses under sinks and vanities do not last forever, and when one bursts it runs at mains pressure until somebody finds the stop tap. Worth replacing before that happens.'),
   ('drain', 'Roots in the drainage', 'Estate landscaping has had twenty years to grow. Roots find joints in drainage lines and catch everything that passes. Jetted out, then a camera to check the pipe.'),
   ('reno', 'Bathrooms and kitchens being redone', 'Original fit-outs are coming out across the suburb. We handle the full plumbing scope and work in with your builder and the other trades.'),
   ('storm', 'Gutters and stormwater', 'Mature trees drop into gutters, and what gets past packs the stormwater line. Clearing it costs less than repairing what overflowing water does.'),
   ('gas', 'Gas appliances', 'Cooktops, heaters, hot water and BBQ points, installed, replaced and leak tested to code.'),
 ],
 'nearby_eyebrow': 'Around the North West',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-the-ponds', 'plumber-kellyville', 'plumber-schofields', 'plumber-quakers-hill', 'plumber-rouse-hill', 'plumber-blacktown'],
 'faqs': [
   ('Do you charge a call out fee in Kellyville Ridge?', FEE),
   ('Everything seems to be failing at once. Is that normal?', 'For an estate built all in one go, yes. The houses were finished within a few years of each other with the same fittings and the same hot water systems, so they reach the end of their life at the same time too. It feels like bad luck and it is really just arithmetic.'),
   ('Is it worth replacing a twenty-year-old hot water system before it fails?', 'Often, yes - a planned replacement is cheaper and a lot less disruptive than an emergency one, and a failed tank usually takes some flooring with it. If yours is that age we will give you an honest read on how much life is left rather than pushing a sale.'),
   ('Do you come out to Kellyville Ridge after hours?', AH),
   council_q('Kellyville Ridge', 'Blacktown City Council'),
   ('Are you licensed and insured?', LIC),
 ],
},

{
 'slug': 'plumber-rouse-hill', 'name': 'Rouse Hill', 'pc': '2155',
 'title': 'Plumber Rouse Hill | 24/7 Emergency | Straight Away Plumbing',
 'og': 'Plumber Rouse Hill | 24/7 Emergency Plumbing',
 'desc': 'Licensed plumber servicing Rouse Hill 2155. Houses, townhouses and units - hot water, blocked drains, leaks. 24/7, $0 call out fee. Call 0403 322 290.',
 'ld_desc': 'Licensed plumber servicing Rouse Hill NSW 2155, covering houses, townhouses and apartments. Hot water systems, blocked drains and shared stacks, leaks and 24/7 emergency callouts, with no call out fee.',
 'hero': 'Licensed plumbing across Rouse Hill - houses, townhouses and apartments, 24 hours a day, with no call out fee and free quotes.',
 'h2': 'Houses, Townhouses and a Town Centre',
 'paras': [
   'Rouse Hill is not one kind of housing. There are detached homes from the 2000s build-out, townhouses and duplexes through the middle, and apartments around the town centre. Each brings different plumbing.',
   'In the houses it is the twenty-year mark: hot water at the end of its life, perished flexible hoses, original tapware finally giving up. In the units it is shared stacks, common property, and the question of whose problem a blockage actually is.',
   'Whatever the building, the answer usually starts with finding where the problem actually is rather than where it happens to be showing itself.',
 ],
 'cards_intro': 'Three kinds of housing in one suburb, and a different set of problems in each.',
 'cards': [
   ('hot', 'Hot water at end of life', 'Systems that went in with the estate are now past their expected run. Repaired where a repair will hold, replaced where it will not.'),
   ('block', 'Units, stacks and common property', 'A blockage in a shared stack shows up in the lowest bathroom on the line, which is often not the one causing it. We find where it actually is before anybody pays for it.'),
   ('drain', 'Blocked drains and roots', 'Twenty years of landscaping over drainage lines does what it always does. Jetted out, with a camera afterwards to check the condition of the pipe.'),
   ('tap', 'Leaking taps and toilets', 'Original tapware and cistern parts across the suburb are all the same age, and they are going at the same time. Quick to fix, and it shows on the water bill.'),
   ('reno', 'Renovations', 'First-round bathrooms and kitchens being redone. Full plumbing scope, rough-in to fit-off, working in with your builder and the other trades.'),
   ('alert', 'After hours emergencies', 'Burst pipes, gas leaks and sewer overflows, 24 hours a day. In a strata building we will work in with your building manager.'),
 ],
 'nearby_eyebrow': 'Around The Hills',
 'nearby_intro': 'We are through this corridor most days. If your suburb is not listed here, search the full list or just call and ask.',
 'nearby': ['plumber-box-hill', 'plumber-kellyville', 'plumber-the-ponds', 'plumber-schofields', 'plumber-castle-hill', 'plumber-kellyville-ridge'],
 'faqs': [
   ('Do you charge a call out fee in Rouse Hill?', FEE),
   ('I am in an apartment. Is a blocked drain my problem or the building\'s?', 'It depends where the blockage actually is. Inside your own fixtures and branch lines it is normally yours. In the shared stack or common drainage it is normally the building\'s. We find out which before anybody commits to paying, and we can put that in writing for your strata manager.'),
   ('Do you work with strata managers?', 'Yes, regularly. Tell us who is handling it and we will deal with them directly, and provide whatever they need to approve common property work.'),
   ('Do you come out to Rouse Hill after hours?', AH),
   council_q('Rouse Hill', 'The Hills Shire'),
   ('Are you licensed and insured?', LIC),
 ],
},

]
