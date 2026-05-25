# Thoughts

This file just sort of track some notes about how I feel for now when I use the project as it is right now.

## 'Status' on thoughts

1. **Text too small =** still relevant going further but in some ways fixed in current CLI where better separation of sections and lines have improved readability and action
2. **Bullets listed as 'Step 1' and so on =** Fixed already - very good solution that makes the whole thing more actionable
3. **Make the 3 steps related =** Fixed = Massive improvement!
4. **Step 1 is super important =** Still extremely relevant but the highlighting of this with empty lines above and below it has improved both readability and action upon it
5. **CLI output - separate input from output =** Fixed - massive improvement!

## Noted thoughts

### Text too small

Although the model output suggestions (the three it produces) are beginning to become somewhat useful - and perhaps even more so motivational - I get the feeling the text output from in the command line is (kinda obviously) too small to really make that "POW! In your face, Jonas .. do these 3 things!".

Hence, the output in some way or the other be larger and perhaps (without being 'corny' and so on) get shown more in some motivational form - whether that's in a sort of "IN YOUR FACE!" kinda way I don't know yet. But in general the output needs to both stand out somehow and be larger in order to make a bigger impact on me for wanting to do the suggested things.

### Bullet should listed as step 1, step 2 and so on

While using the model for suggestions based on a "My kitchen is a mess with quite a few things that I'll need to do for washing the dishes" prompt that at least (and eventually) made me do it's step 1 - which was "Clear off one small area of countertop" - I get the feeling that the output could be improved in the following manner.

Firstly, the suggestions should come listed as this (here with a modified reproduction of how the suggestions to my prompt could be to be better motivational):

- **Step 1:** Clear off one small area of countertop
- **Step 2:** Pick up and put away one item
- **Step 3:** Load first dishwasher rack

Because getting the output like this - i.e. in a numbered way - would make me feel more like "Okay, just do step 1 for now". And this because even though it might seem like "a failure" to only do just one thing, the fact that list would be listed as "Step 1", "Step2, "Step 3" feels like it would make more motivated to perhaps be like "Okay, step 1 is done. Now what. Let me do step 2". Meaning even though just having the output in a numbered list (even though the three from the output isn't quite - or doesn't feel - too related to each other) the fact that the output is shown as a sort of progressive list makes the whole thing feel more motivational for wanting to do the next thing after doing/finishing the previous one.

## Make the 3 steps related 
Furthermore, I feel that if the model could output 3 steps that was really, really related to each other than it would be both more easy and motivational to more steps done. 

Because - in the case of my prompt about doing the dishes - if the could sort of give me some related steps like the below then I'd be more like "Hell yeah! Step 1 done! What's next".

Example of related steps with regards to doing my dishes:

- **Step 1:** Clear off one small area of countertop
- **Step 2:** Do the dishes of what's in the sink already
- **Step 3:** Do just a bit more dishes (if you have the energy)

This example would be sort a "dream example" so I don't expect the/a model to be able to produce something like this - and that's okay!

The main take-away here is at least to try and prompt the model to suggest 3 microsteps steps that are really, really related to each other as this feels like something that would make me do various things better and more motivated.

### Step 1 is SUPER important!!

As the header says .. step 1 is SUPER, SUPER important in that getting that "nailed" feels like it would make me really want to act on whatever it is I would like to act on!!!

So .. perhaps it should be (very) important to make the AI model make the first step 1 as easy, manageable, concrete and motivational since this seems to make me feel like "Hell yeah! I can do this!" - and also kinda "Who cares if don't get step 2 done! At least I got started and got one thing done and now I'm 'pumped' to get stuff out of the way (finished or not)!".

In short: this one thing makes the whole thing feel SO good! And exactly why I wanted to code this project in the first place!

### CLI output - separate input from output

As of now when running "py test_cli.py" for testing the project the total output (meaning the prompt + my input + AI output) looks like this:

"What do you want to do? Get some clothes folded and put away (nicely) in my closet since the clothes have been on my chair for way too long

--- Micro-steps ---

Start here:

👉 Step 1: Pick up one worn-out t-shirt
   Step 2: Fold it neatly into a square shape
   Step 3: Put it directly into the closet shelf"

From this its quite a good addition to get finger emoji pointing at step 1. So that's nice.

In general, however, and also taking the project being a sort of cli right now, the total output from running the project should:

- be separate more clearly into what is the "input part" of the output and what is the "output part" (meaning the suggestion header and 3 AI steps)
- perhaps coloring - and even some sort of "top level" header - might be a good way to both make use, feel and feel of usefulness of using the project even better

### Model time-awareness

Based on the below input and output the model could probably become even better if it was somehow fine tuned to be time aware (see why below the output):

```

What do you want to do?

> How do I best relax - perhaps even get a quick nap - before my plan of going out later to night at 20:30

                    
==================================================
START HERE
==================================================

👉 Step 1: Turn off all screens (phone, TV, computer).

   Step 2: Dim the room lights and adjust temperature.
   Step 3: Put on cozy pajamas or comfortable clothes.

==================================================

```

And "why"?

Because I sure as hell wouldn't put on a pyjamas since I asked to model my question at around 17:30 (hence, suggestions about "pyjamas" is useless around that time of the day)