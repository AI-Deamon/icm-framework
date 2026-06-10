# You're Automating The Wrong Layer (How 30,000 People Build AI Without Frameworks)

**Channel:** Jake Van Clief  
**Uploaded:** 2026-05-20  
**Duration:** 26:37  
**URL:** [https://www.youtube.com/watch?v=956DPSPX4wg](https://www.youtube.com/watch?v=956DPSPX4wg)  

---

## Transcript

`00:02` Interpretable context methodology.
`00:02` Interpretable context methodology. That's the name of my paper that I
`00:03` That's the name of my paper that I
`00:03` That's the name of my paper that I published about 3 months ago, and now
`00:05` published about 3 months ago, and now
`00:05` published about 3 months ago, and now thousands of people and hundreds of
`00:07` thousands of people and hundreds of
`00:07` thousands of people and hundreds of GitHub stars, as well as over 30,000
`00:09` GitHub stars, as well as over 30,000
`00:09` GitHub stars, as well as over 30,000 people in the community, are all using
`00:11` people in the community, are all using
`00:11` people in the community, are all using my methodology to build their own
`00:13` my methodology to build their own
`00:13` my methodology to build their own systems with AI. But they're not
`00:16` systems with AI. But they're not
`00:16` systems with AI. But they're not building multi-agentic frameworks and
`00:18` building multi-agentic frameworks and
`00:18` building multi-agentic frameworks and all these absurdities, they're building
`00:19` all these absurdities, they're building
`00:19` all these absurdities, they're building folders and markdown files on their
`00:21` folders and markdown files on their
`00:21` folders and markdown files on their computer and getting huge results from
`00:24` computer and getting huge results from
`00:24` computer and getting huge results from it. Now, I have a quite a few videos on
`00:26` it. Now, I have a quite a few videos on
`00:26` it. Now, I have a quite a few videos on that, but today I wanted to talk less
`00:28` that, but today I wanted to talk less
`00:29` that, but today I wanted to talk less about
`00:30` about
`00:30` about and more about what I've been building,
`00:32` and more about what I've been building,
`00:32` and more about what I've been building, what me and my team have been building
`00:33` what me and my team have been building
`00:34` what me and my team have been building as a future thing. What can you actually
`00:35` as a future thing. What can you actually
`00:35` as a future thing. What can you actually build using this methodology? And what
`00:38` build using this methodology? And what
`00:38` build using this methodology? And what happens when you bring in some
`00:39` happens when you bring in some
`00:39` happens when you bring in some traditional software programming into
`00:41` traditional software programming into
`00:41` traditional software programming into it? Now, for those of you who are new to
`00:42` it? Now, for those of you who are new to
`00:42` it? Now, for those of you who are new to my channel, essentially my methodology
`00:44` my channel, essentially my methodology
`00:44` my channel, essentially my methodology is about structuring folders,
`00:47` is about structuring folders,
`00:47` is about structuring folders, structuring markdown files. It's very
`00:49` structuring markdown files. It's very
`00:49` structuring markdown files. It's very similar to the LLM Wiki that Kaparthy,
`00:51` similar to the LLM Wiki that Kaparthy,
`00:51` similar to the LLM Wiki that Kaparthy, the founder of OpenAI and currently just
`00:54` the founder of OpenAI and currently just
`00:54` the founder of OpenAI and currently just moved to Anthropic to teach there, uses
`00:57` moved to Anthropic to teach there, uses
`00:57` moved to Anthropic to teach there, uses and is very big in Anthropic's actual
`01:00` and is very big in Anthropic's actual
`01:00` and is very big in Anthropic's actual use cases. They are very big around
`01:01` use cases. They are very big around
`01:01` use cases. They are very big around skills, which is the idea that the right
`01:04` skills, which is the idea that the right
`01:04` skills, which is the idea that the right amount of scripts, processes, and ideas
`01:07` amount of scripts, processes, and ideas
`01:07` amount of scripts, processes, and ideas can all be kind of broken down into just
`01:09` can all be kind of broken down into just
`01:09` can all be kind of broken down into just plain text and folders, and the agent
`01:12` plain text and folders, and the agent
`01:12` plain text and folders, and the agent can navigate that to get the context.
`01:14` can navigate that to get the context.
`01:15` can navigate that to get the context. Rather than using really complicated
`01:16` Rather than using really complicated
`01:16` Rather than using really complicated workflows or infrastructures and
`01:19` workflows or infrastructures and
`01:19` workflows or infrastructures and harnesses, you can create one really
`01:21` harnesses, you can create one really
`01:21` harnesses, you can create one really good harness for a single type of model,
`01:23` good harness for a single type of model,
`01:23` good harness for a single type of model, and then that model can then navigate
`01:25` and then that model can then navigate
`01:25` and then that model can then navigate structure as it needs to. Instead of
`01:27` structure as it needs to. Instead of
`01:28` structure as it needs to. Instead of creating rag that pulls everything in,
`01:30` creating rag that pulls everything in,
`01:30` creating rag that pulls everything in, you just give it access to normal
`01:31` you just give it access to normal
`01:32` you just give it access to normal databases. You give it access to folder
`01:34` databases. You give it access to folder
`01:34` databases. You give it access to folder and context structure. If you haven't
`01:36` and context structure. If you haven't
`01:36` and context structure. If you haven't read anything or dive into this process,
`01:38` read anything or dive into this process,
`01:38` read anything or dive into this process, I do a deep one with Claude Code in my
`01:41` I do a deep one with Claude Code in my
`01:41` I do a deep one with Claude Code in my video right here that you should see
`01:42` video right here that you should see
`01:42` video right here that you should see tagged. Essentially, it just looks into
`01:45` tagged. Essentially, it just looks into
`01:45` tagged. Essentially, it just looks into how to use this, how I use it, and a lot
`01:46` how to use this, how I use it, and a lot
`01:46` how to use this, how I use it, and a lot of people are seeing 20, 30, 40% token
`01:49` of people are seeing 20, 30, 40% token
`01:49` of people are seeing 20, 30, 40% token reduction, and really just getting
`01:51` reduction, and really just getting
`01:51` reduction, and really just getting outcomes a lot faster without a lot of
`01:53` outcomes a lot faster without a lot of
`01:53` outcomes a lot faster without a lot of infrastructure. Even further, you're
`01:55` infrastructure. Even further, you're
`01:55` infrastructure. Even further, you're able to use it to really build out teams
`01:57` able to use it to really build out teams
`01:57` able to use it to really build out teams and build out processes that
`01:59` and build out processes that
`01:59` and build out processes that traditionally would have taken, you
`02:01` traditionally would have taken, you
`02:01` traditionally would have taken, you know, a vendor 6 months and an entire
`02:03` know, a vendor 6 months and an entire
`02:03` know, a vendor 6 months and an entire infrastructure update versus just
`02:05` infrastructure update versus just
`02:05` infrastructure update versus just working with them. And as the people
`02:07` working with them. And as the people
`02:07` working with them. And as the people learn how to use the AI, they're
`02:09` learn how to use the AI, they're
`02:09` learn how to use the AI, they're building the structure for you. Your
`02:11` building the structure for you. Your
`02:11` building the structure for you. Your team become the vendor, and then you can
`02:13` team become the vendor, and then you can
`02:13` team become the vendor, and then you can hire technical talent or bring in your
`02:15` hire technical talent or bring in your
`02:15` hire technical talent or bring in your own technical talent to amplify it, look
`02:17` own technical talent to amplify it, look
`02:17` own technical talent to amplify it, look at the security and governance behind
`02:19` at the security and governance behind
`02:19` at the security and governance behind it. But all of that aside, let me chat
`02:21` it. But all of that aside, let me chat
`02:21` it. But all of that aside, let me chat about transcripts, about dialogue, about
`02:24` about transcripts, about dialogue, about
`02:24` about transcripts, about dialogue, about content, and why it's so important to
`02:27` content, and why it's so important to
`02:27` content, and why it's so important to this entire process. Now, this is an
`02:29` this entire process. Now, this is an
`02:29` this entire process. Now, this is an actual slide that I gave to a real
`02:32` actual slide that I gave to a real
`02:32` actual slide that I gave to a real enterprise company that's bringing in, I
`02:33` enterprise company that's bringing in, I
`02:33` enterprise company that's bringing in, I think, 60 million a year or something
`02:35` think, 60 million a year or something
`02:35` think, 60 million a year or something like that, and they have learned and
`02:37` like that, and they have learned and
`02:37` like that, and they have learned and used this process. One of the biggest
`02:39` used this process. One of the biggest
`02:39` used this process. One of the biggest things that I try to share with people
`02:41` things that I try to share with people
`02:41` things that I try to share with people when we're trying to understand how to
`02:43` when we're trying to understand how to
`02:43` when we're trying to understand how to use AI, how to use these tools in your
`02:46` use AI, how to use these tools in your
`02:46` use AI, how to use these tools in your workflow, is my layer process, right?
`02:49` workflow, is my layer process, right?
`02:49` workflow, is my layer process, right? Layer one is where you're just chatting
`02:52` Layer one is where you're just chatting
`02:52` Layer one is where you're just chatting with a chatbot, you're copy and pasting.
`02:55` with a chatbot, you're copy and pasting.
`02:55` with a chatbot, you're copy and pasting. The layer one is this concept where I
`02:57` The layer one is this concept where I
`02:57` The layer one is this concept where I started years ago when I first started
`02:59` started years ago when I first started
`02:59` started years ago when I first started messing around with language processing
`03:01` messing around with language processing
`03:01` messing around with language processing systems, and a lot of people are today.
`03:03` systems, and a lot of people are today.
`03:03` systems, and a lot of people are today. It's where you log into ChatGPT or
`03:06` It's where you log into ChatGPT or
`03:06` It's where you log into ChatGPT or Claude, and all you're doing really is
`03:08` Claude, and all you're doing really is
`03:08` Claude, and all you're doing really is just kind of pasting in ideas, right?
`03:11` just kind of pasting in ideas, right?
`03:11` just kind of pasting in ideas, right? You're just chatting back and forth in
`03:12` You're just chatting back and forth in
`03:12` You're just chatting back and forth in it. You're copying and pasting, you're
`03:14` it. You're copying and pasting, you're
`03:14` it. You're copying and pasting, you're throwing in concepts in there. Um you're
`03:17` throwing in concepts in there. Um you're
`03:17` throwing in concepts in there. Um you're just asking it basically questions and
`03:19` just asking it basically questions and
`03:19` just asking it basically questions and things like that. What you actually want
`03:21` things like that. What you actually want
`03:21` things like that. What you actually want to really understand is the amount of
`03:23` to really understand is the amount of
`03:23` to really understand is the amount of effort to get something back is low, and
`03:26` effort to get something back is low, and
`03:26` effort to get something back is low, and you can get some pretty decent things,
`03:28` you can get some pretty decent things,
`03:28` you can get some pretty decent things, but the amount of output and impact that
`03:31` but the amount of output and impact that
`03:31` but the amount of output and impact that you get is actually very weak, right?
`03:34` you get is actually very weak, right?
`03:34` you get is actually very weak, right? It's not going to be huge. You can get
`03:35` It's not going to be huge. You can get
`03:35` It's not going to be huge. You can get some very good stuff, but earlier, 3
`03:38` some very good stuff, but earlier, 3
`03:38` some very good stuff, but earlier, 3 years ago, it was very challenging to
`03:41` years ago, it was very challenging to
`03:41` years ago, it was very challenging to get any sort of outputs. And in order to
`03:43` get any sort of outputs. And in order to
`03:43` get any sort of outputs. And in order to really get a better output out of it,
`03:45` really get a better output out of it,
`03:45` really get a better output out of it, you have to have longer and longer
`03:46` you have to have longer and longer
`03:46` you have to have longer and longer conversations. As in, you're essentially
`03:49` conversations. As in, you're essentially
`03:49` conversations. As in, you're essentially adding multiple chats, you have saved
`03:51` adding multiple chats, you have saved
`03:51` adding multiple chats, you have saved prompts, maybe you have a tone style.
`03:53` prompts, maybe you have a tone style.
`03:53` prompts, maybe you have a tone style. And we see a lot of people sharing
`03:54` And we see a lot of people sharing
`03:55` And we see a lot of people sharing prompt libraries. They have shared
`03:57` prompt libraries. They have shared
`03:57` prompt libraries. They have shared prompts. Maybe they're adding the
`03:58` prompts. Maybe they're adding the
`03:58` prompts. Maybe they're adding the prompts in little by little. A lot of
`04:01` prompts in little by little. A lot of
`04:01` prompts in little by little. A lot of other like kind of integration tools do
`04:03` other like kind of integration tools do
`04:03` other like kind of integration tools do this where they're grabbing a prompt and
`04:05` this where they're grabbing a prompt and
`04:05` this where they're grabbing a prompt and giving it to the AI automatically. It's
`04:08` giving it to the AI automatically. It's
`04:08` giving it to the AI automatically. It's doing chain of loop processing. And
`04:10` doing chain of loop processing. And
`04:10` doing chain of loop processing. And these skills are actually the layer two.
`04:12` these skills are actually the layer two.
`04:12` these skills are actually the layer two. Someone else went through that layer two
`04:14` Someone else went through that layer two
`04:14` Someone else went through that layer two workflow, found the right amount of
`04:17` workflow, found the right amount of
`04:17` workflow, found the right amount of prompts that you actually want to be
`04:18` prompts that you actually want to be
`04:18` prompts that you actually want to be able to give in what order you want to
`04:20` able to give in what order you want to
`04:20` able to give in what order you want to give them and kind of handled that as a
`04:23` give them and kind of handled that as a
`04:23` give them and kind of handled that as a skill. But then skills evolve even
`04:25` skill. But then skills evolve even
`04:26` skill. But then skills evolve even further and you realize you only need
`04:28` further and you realize you only need
`04:28` further and you realize you only need certain parts of a skill at a certain
`04:29` certain parts of a skill at a certain
`04:29` certain parts of a skill at a certain time. You don't want to overload the
`04:32` time. You don't want to overload the
`04:32` time. You don't want to overload the context window and you want to start
`04:34` context window and you want to start
`04:34` context window and you want to start creating automations. That's where you
`04:35` creating automations. That's where you
`04:36` creating automations. That's where you start leaning into level three or layer
`04:38` start leaning into level three or layer
`04:38` start leaning into level three or layer three, which is where you're actually
`04:40` three, which is where you're actually
`04:40` three, which is where you're actually doing this huge workflow. You're taking
`04:43` doing this huge workflow. You're taking
`04:43` doing this huge workflow. You're taking multiple skills, multiple prompts,
`04:45` multiple skills, multiple prompts,
`04:45` multiple skills, multiple prompts, multiple workflow processes, maybe even
`04:47` multiple workflow processes, maybe even
`04:47` multiple workflow processes, maybe even multiple AI and actually linking them
`04:50` multiple AI and actually linking them
`04:50` multiple AI and actually linking them together. Then they realized that you
`04:52` together. Then they realized that you
`04:52` together. Then they realized that you want to do even more steps. You want
`04:54` want to do even more steps. You want
`04:54` want to do even more steps. You want these agents. And that's where you have
`04:56` these agents. And that's where you have
`04:56` these agents. And that's where you have these other markdown files or scripts in
`04:58` these other markdown files or scripts in
`04:59` these other markdown files or scripts in many areas, right? People actually put
`05:01` many areas, right? People actually put
`05:01` many areas, right? People actually put Python for people to actually run for
`05:03` Python for people to actually run for
`05:03` Python for people to actually run for the AI to actually run itself to be able
`05:06` the AI to actually run itself to be able
`05:07` the AI to actually run itself to be able to handle the creation of stuff because
`05:09` to handle the creation of stuff because
`05:09` to handle the creation of stuff because they needed more determinism. They
`05:11` they needed more determinism. They
`05:11` they needed more determinism. They wanted the output to be the same every
`05:13` wanted the output to be the same every
`05:13` wanted the output to be the same every time. And so if they could package all
`05:15` time. And so if they could package all
`05:15` time. And so if they could package all of that into a prompt, all of this could
`05:18` of that into a prompt, all of this could
`05:18` of that into a prompt, all of this could be uploaded and sent in the right order,
`05:21` be uploaded and sent in the right order,
`05:21` be uploaded and sent in the right order, that's where skills come from. And this
`05:23` that's where skills come from. And this
`05:23` that's where skills come from. And this allows them to then in this case create
`05:26` allows them to then in this case create
`05:26` allows them to then in this case create more skills, but you have hundreds of
`05:28` more skills, but you have hundreds of
`05:28` more skills, but you have hundreds of skills available. And if you have Claude
`05:30` skills available. And if you have Claude
`05:30` skills available. And if you have Claude installed on your computer, you can
`05:33` installed on your computer, you can
`05:33` installed on your computer, you can actually come through and look through
`05:35` actually come through and look through
`05:35` actually come through and look through these skills deeply. Some of these
`05:36` these skills deeply. Some of these
`05:36` these skills deeply. Some of these skills, right? For algorithmic art, a
`05:38` skills, right? For algorithmic art, a
`05:38` skills, right? For algorithmic art, a skill for creating art with like kind of
`05:41` skill for creating art with like kind of
`05:41` skill for creating art with like kind of an algorithmic process, has an HTML
`05:43` an algorithmic process, has an HTML
`05:43` an algorithmic process, has an HTML viewer and a template built into it.
`05:46` viewer and a template built into it.
`05:46` viewer and a template built into it. Maybe you're trying to create a doc file
`05:49` Maybe you're trying to create a doc file
`05:49` Maybe you're trying to create a doc file in markdown. You have the actual skill
`05:52` in markdown. You have the actual skill
`05:52` in markdown. You have the actual skill explanation. This is how you do it.
`05:54` explanation. This is how you do it.
`05:54` explanation. This is how you do it. These are the prompts they put in order.
`05:56` These are the prompts they put in order.
`05:56` These are the prompts they put in order. Traditionally, 2 years ago, I was
`05:58` Traditionally, 2 years ago, I was
`05:58` Traditionally, 2 years ago, I was putting these prompts in manually.
`06:00` putting these prompts in manually.
`06:00` putting these prompts in manually. First, I would I knew that okay, if I
`06:02` First, I would I knew that okay, if I
`06:02` First, I would I knew that okay, if I told the chatbot this in a certain
`06:05` told the chatbot this in a certain
`06:05` told the chatbot this in a certain order, right? I come in and I paste this
`06:08` order, right? I come in and I paste this
`06:08` order, right? I come in and I paste this here.
`06:09` here.
`06:09` here. Right? It would do that process. I would
`06:11` Right? It would do that process. I would
`06:12` Right? It would do that process. I would wait for its output, verify that it's
`06:13` wait for its output, verify that it's
`06:13` wait for its output, verify that it's right, and then I would move on to the
`06:16` right, and then I would move on to the
`06:16` right, and then I would move on to the next step, which is okay, well then we
`06:18` next step, which is okay, well then we
`06:18` next step, which is okay, well then we need to edit that and have these things.
`06:21` need to edit that and have these things.
`06:21` need to edit that and have these things. And over time we realized we could drop
`06:23` And over time we realized we could drop
`06:23` And over time we realized we could drop that into the AI all at once and it
`06:25` that into the AI all at once and it
`06:25` that into the AI all at once and it would recognize that. But then we could
`06:27` would recognize that. But then we could
`06:27` would recognize that. But then we could drop all of it into the AI at once and
`06:30` drop all of it into the AI at once and
`06:30` drop all of it into the AI at once and tell it to reference certain areas or
`06:32` tell it to reference certain areas or
`06:32` tell it to reference certain areas or actually use commands and the single
`06:35` actually use commands and the single
`06:35` actually use commands and the single agent could then do those things. Right?
`06:38` agent could then do those things. Right?
`06:38` agent could then do those things. Right? Now, traditionally, before, the way they
`06:40` Now, traditionally, before, the way they
`06:40` Now, traditionally, before, the way they solved that is using LangChain or
`06:42` solved that is using LangChain or
`06:42` solved that is using LangChain or Semantic Kernel or all of these things
`06:44` Semantic Kernel or all of these things
`06:44` Semantic Kernel or all of these things to do these actions separately or to
`06:46` to do these actions separately or to
`06:46` to do these actions separately or to inject these at the right time in the
`06:50` inject these at the right time in the
`06:50` inject these at the right time in the thinking process of the AI. But now we
`06:53` thinking process of the AI. But now we
`06:53` thinking process of the AI. But now we can just break down the thinking process
`06:56` can just break down the thinking process
`06:56` can just break down the thinking process into folders and structures and trigger
`06:58` into folders and structures and trigger
`06:58` into folders and structures and trigger them as they're needed, which is what
`07:01` them as they're needed, which is what
`07:01` them as they're needed, which is what these folder skills and processes are
`07:03` these folder skills and processes are
`07:03` these folder skills and processes are doing. But again, a common theme.
`07:06` doing. But again, a common theme.
`07:06` doing. But again, a common theme. There's a reason I'm describing all of
`07:08` There's a reason I'm describing all of
`07:08` There's a reason I'm describing all of this. All of these skills, all of these
`07:10` this. All of these skills, all of these
`07:10` this. All of these skills, all of these folders and markdown files, all have one
`07:14` folders and markdown files, all have one
`07:14` folders and markdown files, all have one core theme.
`07:16` core theme.
`07:16` core theme. Discussion and dialogue. They all came
`07:20` Discussion and dialogue. They all came
`07:20` Discussion and dialogue. They all came from an initial layer one of discussion
`07:23` from an initial layer one of discussion
`07:23` from an initial layer one of discussion and dialogue breakdown. At layer one,
`07:26` and dialogue breakdown. At layer one,
`07:26` and dialogue breakdown. At layer one, you're pasting a prompt into ChatGPT and
`07:28` you're pasting a prompt into ChatGPT and
`07:28` you're pasting a prompt into ChatGPT and then copying the output or going through
`07:30` then copying the output or going through
`07:30` then copying the output or going through iterations of an output. At level two,
`07:32` iterations of an output. At level two,
`07:32` iterations of an output. At level two, you already expect what the output is
`07:35` you already expect what the output is
`07:35` you already expect what the output is from level one, so you have refined
`07:37` from level one, so you have refined
`07:37` from level one, so you have refined prompts and processes that are
`07:39` prompts and processes that are
`07:39` prompts and processes that are automatically being injected in. At
`07:41` automatically being injected in. At
`07:41` automatically being injected in. At level three, you're doing all of the
`07:43` level three, you're doing all of the
`07:44` level three, you're doing all of the level two automated multiple times so
`07:46` level two automated multiple times so
`07:46` level two automated multiple times so that you can then come in and look at
`07:48` that you can then come in and look at
`07:49` that you can then come in and look at these processes. And that goes for code
`07:50` these processes. And that goes for code
`07:50` these processes. And that goes for code review, data reporting, writing and
`07:53` review, data reporting, writing and
`07:53` review, data reporting, writing and drafting, all of those. That's what we
`07:55` drafting, all of those. That's what we
`07:55` drafting, all of those. That's what we really want to understand here. But it
`07:57` really want to understand here. But it
`07:57` really want to understand here. But it all comes from dialogue. Conversation
`08:00` all comes from dialogue. Conversation
`08:00` all comes from dialogue. Conversation has the structure we're looking for. The
`08:03` has the structure we're looking for. The
`08:03` has the structure we're looking for. The intent is carried in the conversation.
`08:05` intent is carried in the conversation.
`08:05` intent is carried in the conversation. And instead of just describing this
`08:07` And instead of just describing this
`08:07` And instead of just describing this randomly, here's a tool K, who is one of
`08:10` randomly, here's a tool K, who is one of
`08:10` randomly, here's a tool K, who is one of my co-founders and a really brilliant
`08:12` my co-founders and a really brilliant
`08:12` my co-founders and a really brilliant person currently studying at the
`08:13` person currently studying at the
`08:13` person currently studying at the University of Edinburgh, created to
`08:15` University of Edinburgh, created to
`08:15` University of Edinburgh, created to really help exemplify this process. So,
`08:19` really help exemplify this process. So,
`08:19` really help exemplify this process. So, imagine here on the left, this is the
`08:21` imagine here on the left, this is the
`08:21` imagine here on the left, this is the chat. And we're going to break this down
`08:23` chat. And we're going to break this down
`08:23` chat. And we're going to break this down to the simplest process. This is a chat
`08:25` to the simplest process. This is a chat
`08:25` to the simplest process. This is a chat that may have happened forever ago. And
`08:28` that may have happened forever ago. And
`08:28` that may have happened forever ago. And the idea is, can you tighten this
`08:29` the idea is, can you tighten this
`08:30` the idea is, can you tighten this paragraph? It feels too wordy. Climate
`08:32` paragraph? It feels too wordy. Climate
`08:32` paragraph? It feels too wordy. Climate change blah blah and you put in the
`08:33` change blah blah and you put in the
`08:33` change blah blah and you put in the paragraph in there. Now, in the past,
`08:36` paragraph in there. Now, in the past,
`08:36` paragraph in there. Now, in the past, right, the agent would just say, "Here's
`08:38` right, the agent would just say, "Here's
`08:38` right, the agent would just say, "Here's a new one." And then we would say, "Hey,
`08:40` a new one." And then we would say, "Hey,
`08:40` a new one." And then we would say, "Hey, this feels weirdly formal now. The
`08:42` this feels weirdly formal now. The
`08:42` this feels weirdly formal now. The original had more of a conversational
`08:44` original had more of a conversational
`08:44` original had more of a conversational rhythm." And so the agent does something
`08:46` rhythm." And so the agent does something
`08:46` rhythm." And so the agent does something and then it's this constant back and
`08:48` and then it's this constant back and
`08:48` and then it's this constant back and forth until we finally get the output we
`08:51` forth until we finally get the output we
`08:51` forth until we finally get the output we wanted out of it.
`08:52` wanted out of it.
`08:52` wanted out of it. Now, everywhere along this conversation,
`08:55` Now, everywhere along this conversation,
`08:55` Now, everywhere along this conversation, even in this simple one, there is a
`08:56` even in this simple one, there is a
`08:56` even in this simple one, there is a chain of decisions being made. And if we
`08:59` chain of decisions being made. And if we
`08:59` chain of decisions being made. And if we actually extract those chain of
`09:01` actually extract those chain of
`09:01` actually extract those chain of decisions using K's tool here, here on
`09:04` decisions using K's tool here, here on
`09:04` decisions using K's tool here, here on the left is the decisions made by the
`09:06` the left is the decisions made by the
`09:07` the left is the decisions made by the user. Here on the right are the
`09:09` user. Here on the right are the
`09:09` user. Here on the right are the decisions made by the model. Now, when
`09:12` decisions made by the model. Now, when
`09:12` decisions made by the model. Now, when we look in, the goal was to tighten a
`09:15` we look in, the goal was to tighten a
`09:15` we look in, the goal was to tighten a paragraph. All of this is all of the
`09:17` paragraph. All of this is all of the
`09:17` paragraph. All of this is all of the goals and focus. And as you can see, it
`09:19` goals and focus. And as you can see, it
`09:19` goals and focus. And as you can see, it links directly here. Can you tighten
`09:22` links directly here. Can you tighten
`09:22` links directly here. Can you tighten this paragraph? It feels too wordy. Now,
`09:25` this paragraph? It feels too wordy. Now,
`09:25` this paragraph? It feels too wordy. Now, we set up constraints along the process
`09:28` we set up constraints along the process
`09:28` we set up constraints along the process and at different points. Perhaps there
`09:29` and at different points. Perhaps there
`09:29` and at different points. Perhaps there was a constraint saying, "Hey, there was
`09:31` was a constraint saying, "Hey, there was
`09:31` was a constraint saying, "Hey, there was too much wordiness. We want to perceive
`09:34` too much wordiness. We want to perceive
`09:34` too much wordiness. We want to perceive the rhythm or conserve what the rhythm
`09:36` the rhythm or conserve what the rhythm
`09:36` the rhythm or conserve what the rhythm in the original paragraph was. Maybe we
`09:39` in the original paragraph was. Maybe we
`09:39` in the original paragraph was. Maybe we want to have it more styled or evolved,
`09:42` want to have it more styled or evolved,
`09:42` want to have it more styled or evolved, right? Here, we want it scarier, way
`09:44` right? Here, we want it scarier, way
`09:44` right? Here, we want it scarier, way behind. The voice we're going for is
`09:46` behind. The voice we're going for is
`09:46` behind. The voice we're going for is more measured, right? In that same
`09:48` more measured, right? In that same
`09:48` more measured, right? In that same sentence. Maybe we want to match the
`09:50` sentence. Maybe we want to match the
`09:50` sentence. Maybe we want to match the entire voice reference. The assumption
`09:54` entire voice reference. The assumption
`09:54` entire voice reference. The assumption is that we need it to match the
`09:56` is that we need it to match the
`09:56` is that we need it to match the original, and both the model and the AI
`09:59` original, and both the model and the AI
`09:59` original, and both the model and the AI follow this assumption. And we're Don't
`10:01` follow this assumption. And we're Don't
`10:01` follow this assumption. And we're Don't worry, we're going to go over to this
`10:02` worry, we're going to go over to this
`10:02` worry, we're going to go over to this right one in a second. But I really want
`10:04` right one in a second. But I really want
`10:04` right one in a second. But I really want you to understand this. Finally, the
`10:07` you to understand this. Finally, the
`10:07` you to understand this. Finally, the goal of what we're making, the process,
`10:10` goal of what we're making, the process,
`10:10` goal of what we're making, the process, is an actual blog post or a reference,
`10:13` is an actual blog post or a reference,
`10:13` is an actual blog post or a reference, and we give an example of what that
`10:15` and we give an example of what that
`10:15` and we give an example of what that should be. There's also dialogue
`10:18` should be. There's also dialogue
`10:18` should be. There's also dialogue happening, right? Questions that are
`10:19` happening, right? Questions that are
`10:19` happening, right? Questions that are happening. Uh I think there's a way in
`10:21` happening. Uh I think there's a way in
`10:22` happening. Uh I think there's a way in which to do these things. When we go and
`10:24` which to do these things. When we go and
`10:24` which to do these things. When we go and look at the model over here, the same
`10:26` look at the model over here, the same
`10:26` look at the model over here, the same thing. The model sees the goal, it sees
`10:29` thing. The model sees the goal, it sees
`10:29` thing. The model sees the goal, it sees the constraints, but it is making
`10:30` the constraints, but it is making
`10:30` the constraints, but it is making decisions on those constraints. It's
`10:33` decisions on those constraints. It's
`10:33` decisions on those constraints. It's coming through and saying, "Hey, this
`10:35` coming through and saying, "Hey, this
`10:35` coming through and saying, "Hey, this retains a cleaner structure. I made this
`10:37` retains a cleaner structure. I made this
`10:37` retains a cleaner structure. I made this decision for this goal. I made this
`10:39` decision for this goal. I made this
`10:39` decision for this goal. I made this decision for this goal." And it's also
`10:42` decision for this goal." And it's also
`10:42` decision for this goal." And it's also making assumptions along the whole way.
`10:45` making assumptions along the whole way.
`10:45` making assumptions along the whole way. We create all of this data. We look at
`10:47` We create all of this data. We look at
`10:47` We create all of this data. We look at this. And instead, what we can do is we
`10:50` this. And instead, what we can do is we
`10:50` this. And instead, what we can do is we can create a system of tone, of style,
`10:53` can create a system of tone, of style,
`10:53` can create a system of tone, of style, of ideas that capture all of these
`10:56` of ideas that capture all of these
`10:56` of ideas that capture all of these problems and constraints already. So
`10:58` problems and constraints already. So
`10:58` problems and constraints already. So that when I say tighten this paragraph,
`11:01` that when I say tighten this paragraph,
`11:01` that when I say tighten this paragraph, this tree of processes, this tree of
`11:04` this tree of processes, this tree of
`11:04` this tree of processes, this tree of prompts, is called the first time.
`11:07` prompts, is called the first time.
`11:07` prompts, is called the first time. Again, thinking about where we're at,
`11:09` Again, thinking about where we're at,
`11:09` Again, thinking about where we're at, originally, it was layer two. We had to
`11:11` originally, it was layer two. We had to
`11:11` originally, it was layer two. We had to sit there and describe these processes,
`11:13` sit there and describe these processes,
`11:13` sit there and describe these processes, verified outputs. We captured those,
`11:15` verified outputs. We captured those,
`11:15` verified outputs. We captured those, turned those into maybe markdown files
`11:17` turned those into maybe markdown files
`11:17` turned those into maybe markdown files or structure, and then the original
`11:20` or structure, and then the original
`11:20` or structure, and then the original request becomes a layer one process,
`11:23` request becomes a layer one process,
`11:23` request becomes a layer one process, where I'm able to simply say, "Can you
`11:25` where I'm able to simply say, "Can you
`11:25` where I'm able to simply say, "Can you tighten this paragraph?" Again, this
`11:28` tighten this paragraph?" Again, this
`11:28` tighten this paragraph?" Again, this also is the same thing for everything.
`11:30` also is the same thing for everything.
`11:31` also is the same thing for everything. Let's say we're doing the opposite side.
`11:32` Let's say we're doing the opposite side.
`11:32` Let's say we're doing the opposite side. We're actually refactoring code. And I
`11:35` We're actually refactoring code. And I
`11:35` We're actually refactoring code. And I actually say, "Hey, my Python my my
`11:37` actually say, "Hey, my Python my my
`11:37` actually say, "Hey, my Python my my Python is treating code a certain way. I
`11:39` Python is treating code a certain way. I
`11:39` Python is treating code a certain way. I notice that this parser, can you kind of
`11:41` notice that this parser, can you kind of
`11:41` notice that this parser, can you kind of take a look and fix it possibly?" And of
`11:44` take a look and fix it possibly?" And of
`11:44` take a look and fix it possibly?" And of [snorts] course, the instant assistant
`11:45` [snorts] course, the instant assistant
`11:45` [snorts] course, the instant assistant comes in, says what it thinks its fix
`11:47` comes in, says what it thinks its fix
`11:47` comes in, says what it thinks its fix is, maybe we say some sort of reference
`11:49` is, maybe we say some sort of reference
`11:49` is, maybe we say some sort of reference cuz we're an expert in the field maybe.
`11:51` cuz we're an expert in the field maybe.
`11:51` cuz we're an expert in the field maybe. This is how they did training early on
`11:53` This is how they did training early on
`11:53` This is how they did training early on is this kind of back and forth. And you
`11:56` is this kind of back and forth. And you
`11:56` is this kind of back and forth. And you eventually get to the conclusion, the
`11:58` eventually get to the conclusion, the
`11:58` eventually get to the conclusion, the goal. When we actually extract that
`12:00` goal. When we actually extract that
`12:00` goal. When we actually extract that data, right? You end up getting the same
`12:03` data, right? You end up getting the same
`12:03` data, right? You end up getting the same thing. You have goals, then you maybe
`12:05` thing. You have goals, then you maybe
`12:05` thing. You have goals, then you maybe even have subgoals, right? Can we just
`12:08` even have subgoals, right? Can we just
`12:08` even have subgoals, right? Can we just patch the empty cell instead and keep
`12:10` patch the empty cell instead and keep
`12:10` patch the empty cell instead and keep the original function? You have to
`12:12` the original function? You have to
`12:12` the original function? You have to constraints within this dialogue, and
`12:15` constraints within this dialogue, and
`12:15` constraints within this dialogue, and you have processes that live inside of
`12:17` you have processes that live inside of
`12:17` you have processes that live inside of it as well. Same for the model. The
`12:20` it as well. Same for the model. The
`12:20` it as well. Same for the model. The model now has the goal. It's coming
`12:22` model now has the goal. It's coming
`12:22` model now has the goal. It's coming through and it's making decisions on
`12:25` through and it's making decisions on
`12:25` through and it's making decisions on that goal. And all of it can be tracked
`12:28` that goal. And all of it can be tracked
`12:28` that goal. And all of it can be tracked through dialogue. That goes for
`12:30` through dialogue. That goes for
`12:30` through dialogue. That goes for anything. Database schemas, you can
`12:32` anything. Database schemas, you can
`12:32` anything. Database schemas, you can track the decision-making and goal
`12:34` track the decision-making and goal
`12:34` track the decision-making and goal processes, where and when it was saved
`12:37` processes, where and when it was saved
`12:37` processes, where and when it was saved within dialogue. All of this becomes
`12:40` within dialogue. All of this becomes
`12:40` within dialogue. All of this becomes either training data or even better,
`12:42` either training data or even better,
`12:42` either training data or even better, actual markdown files that can be used
`12:45` actual markdown files that can be used
`12:45` actual markdown files that can be used later, converted into a methodology,
`12:49` later, converted into a methodology,
`12:49` later, converted into a methodology, right? And it's important to understand
`12:51` right? And it's important to understand
`12:51` right? And it's important to understand this, not necessarily that you could use
`12:53` this, not necessarily that you could use
`12:53` this, not necessarily that you could use this tool. We might make this tool
`12:55` this tool. We might make this tool
`12:55` this tool. We might make this tool open-source. Right now, it's being used
`12:56` open-source. Right now, it's being used
`12:57` open-source. Right now, it's being used for a research project at the University
`12:58` for a research project at the University
`12:58` for a research project at the University of Edinburgh. Um but the idea here isn't
`13:01` of Edinburgh. Um but the idea here isn't
`13:01` of Edinburgh. Um but the idea here isn't for you to you all use this tool right
`13:03` for you to you all use this tool right
`13:03` for you to you all use this tool right now. The idea is what this tool shows
`13:05` now. The idea is what this tool shows
`13:05` now. The idea is what this tool shows about dialogue, about prompting, and
`13:08` about dialogue, about prompting, and
`13:08` about dialogue, about prompting, and about engineering context, where and
`13:12` about engineering context, where and
`13:12` about engineering context, where and what you want to engineer context, at
`13:14` what you want to engineer context, at
`13:14` what you want to engineer context, at what levels you do. And that's what has
`13:16` what levels you do. And that's what has
`13:16` what levels you do. And that's what has informed a lot of the work I'm doing.
`13:19` informed a lot of the work I'm doing.
`13:19` informed a lot of the work I'm doing. And an example is one here. My dialogue
`13:22` And an example is one here. My dialogue
`13:22` And an example is one here. My dialogue with the AI made me realize it sucks at
`13:25` with the AI made me realize it sucks at
`13:25` with the AI made me realize it sucks at certain processes of reading and
`13:28` certain processes of reading and
`13:28` certain processes of reading and research. So, I created a kind of pillar
`13:31` research. So, I created a kind of pillar
`13:32` research. So, I created a kind of pillar of idea and my voice and my patterns and
`13:35` of idea and my voice and my patterns and
`13:35` of idea and my voice and my patterns and constraints that capture my process of
`13:38` constraints that capture my process of
`13:38` constraints that capture my process of writing and researching, as well as my
`13:40` writing and researching, as well as my
`13:40` writing and researching, as well as my tone. No matter what project I'm working
`13:43` tone. No matter what project I'm working
`13:43` tone. No matter what project I'm working on, I use these processes. So, that's
`13:45` on, I use these processes. So, that's
`13:45` on, I use these processes. So, that's all just captured in a very simple,
`13:47` all just captured in a very simple,
`13:47` all just captured in a very simple, short prompt, right? That is referenced
`13:51` short prompt, right? That is referenced
`13:51` short prompt, right? That is referenced whenever I need it through the initial
`13:54` whenever I need it through the initial
`13:54` whenever I need it through the initial prompt, which is my Claude MD. That
`13:56` prompt, which is my Claude MD. That
`13:56` prompt, which is my Claude MD. That gives folder structure of wherever I'm
`13:58` gives folder structure of wherever I'm
`13:58` gives folder structure of wherever I'm hiding and wherever that voice is, I
`14:01` hiding and wherever that voice is, I
`14:01` hiding and wherever that voice is, I say, "Hey, every session, I'm going to
`14:04` say, "Hey, every session, I'm going to
`14:04` say, "Hey, every session, I'm going to have certain things built in." My voice
`14:06` have certain things built in." My voice
`14:06` have certain things built in." My voice and tone MD directly says how I speak
`14:09` and tone MD directly says how I speak
`14:09` and tone MD directly says how I speak and teach. And just by me simply saying,
`14:12` and teach. And just by me simply saying,
`14:12` and teach. And just by me simply saying, right, without creating any crazy
`14:14` right, without creating any crazy
`14:14` right, without creating any crazy agentic architecture, "What is my voice
`14:18` agentic architecture, "What is my voice
`14:18` agentic architecture, "What is my voice and tone?" Now, if I had asked an AI
`14:21` and tone?" Now, if I had asked an AI
`14:21` and tone?" Now, if I had asked an AI model that was at layer one or 2 years
`14:24` model that was at layer one or 2 years
`14:24` model that was at layer one or 2 years ago, it would have no idea. I'd have to
`14:26` ago, it would have no idea. I'd have to
`14:26` ago, it would have no idea. I'd have to paste a whole bunch of prompts in there,
`14:27` paste a whole bunch of prompts in there,
`14:27` paste a whole bunch of prompts in there, setting all in. If I was one at layer
`14:29` setting all in. If I was one at layer
`14:29` setting all in. If I was one at layer two, it would have to read the whole
`14:32` two, it would have to read the whole
`14:32` two, it would have to read the whole database, go through everything, finally
`14:34` database, go through everything, finally
`14:34` database, go through everything, finally find the structure. At layer three, I've
`14:37` find the structure. At layer three, I've
`14:37` find the structure. At layer three, I've solved the problem of it navigating, so
`14:39` solved the problem of it navigating, so
`14:39` solved the problem of it navigating, so it can easily come in, find my voice and
`14:42` it can easily come in, find my voice and
`14:42` it can easily come in, find my voice and tone markdown file, actually look
`14:44` tone markdown file, actually look
`14:45` tone markdown file, actually look through and see how I teach and tone
`14:47` through and see how I teach and tone
`14:47` through and see how I teach and tone with one simple prompt. This prompt is
`14:49` with one simple prompt. This prompt is
`14:49` with one simple prompt. This prompt is actually thousands of prompts, which if
`14:52` actually thousands of prompts, which if
`14:52` actually thousands of prompts, which if any of you have watched my Python video,
`14:54` any of you have watched my Python video,
`14:54` any of you have watched my Python video, 12,000 lines of Python, it's the same
`14:57` 12,000 lines of Python, it's the same
`14:57` 12,000 lines of Python, it's the same thing. When I type hello world, it is
`15:00` thing. When I type hello world, it is
`15:00` thing. When I type hello world, it is thousands and thousands of lines of code
`15:04` thousands and thousands of lines of code
`15:04` thousands and thousands of lines of code that are executing to print hello world
`15:07` that are executing to print hello world
`15:07` that are executing to print hello world in Python. If you haven't seen that, I
`15:09` in Python. If you haven't seen that, I
`15:09` in Python. If you haven't seen that, I highly recommend it. It's very useful
`15:11` highly recommend it. It's very useful
`15:11` highly recommend it. It's very useful for this kind of conceptual.
`15:13` for this kind of conceptual.
`15:13` for this kind of conceptual. This same thing is happening now with
`15:15` This same thing is happening now with
`15:15` This same thing is happening now with these processes. This is the next layer
`15:18` these processes. This is the next layer
`15:18` these processes. This is the next layer of software engineering. But, with every
`15:21` of software engineering. But, with every
`15:21` of software engineering. But, with every layer comes requirements, comes
`15:24` layer comes requirements, comes
`15:24` layer comes requirements, comes processes, and that is exactly what I'm
`15:26` processes, and that is exactly what I'm
`15:26` processes, and that is exactly what I'm encoding here. These processes keep
`15:29` encoding here. These processes keep
`15:29` encoding here. These processes keep expanding until I finally have an
`15:31` expanding until I finally have an
`15:31` expanding until I finally have an output. In this case, my output was the
`15:34` output. In this case, my output was the
`15:34` output. In this case, my output was the ability to not only write and research
`15:37` ability to not only write and research
`15:37` ability to not only write and research in my own area. So, I had a company NLP
`15:39` in my own area. So, I had a company NLP
`15:40` in my own area. So, I had a company NLP Logics that wanted me to create videos
`15:42` Logics that wanted me to create videos
`15:42` Logics that wanted me to create videos for them. I spent time building ideas
`15:44` for them. I spent time building ideas
`15:44` for them. I spent time building ideas and my tone around it and I said, "I
`15:46` and my tone around it and I said, "I
`15:46` and my tone around it and I said, "I want to make three videos based on three
`15:48` want to make three videos based on three
`15:48` want to make three videos based on three of their products." So, it goes through,
`15:50` of their products." So, it goes through,
`15:50` of their products." So, it goes through, it has access to the my research and
`15:52` it has access to the my research and
`15:52` it has access to the my research and creates a research folder on each of the
`15:55` creates a research folder on each of the
`15:55` creates a research folder on each of the products. The angle, where they are,
`15:58` products. The angle, where they are,
`15:58` products. The angle, where they are, what type of hooks might work, what type
`16:00` what type of hooks might work, what type
`16:00` what type of hooks might work, what type of outlines and materials. And again,
`16:02` of outlines and materials. And again,
`16:02` of outlines and materials. And again, it's all markdown files. These are just
`16:03` it's all markdown files. These are just
`16:03` it's all markdown files. These are just more prompts to be added to context in
`16:06` more prompts to be added to context in
`16:06` more prompts to be added to context in the future, whether it's this AI or any
`16:09` the future, whether it's this AI or any
`16:09` the future, whether it's this AI or any other AI that I'm using to read these
`16:11` other AI that I'm using to read these
`16:11` other AI that I'm using to read these folders. And then, all I have to say is,
`16:13` folders. And then, all I have to say is,
`16:13` folders. And then, all I have to say is, "Cool. Now, do the research based off of
`16:15` "Cool. Now, do the research based off of
`16:15` "Cool. Now, do the research based off of all of that." Then, with a third prompt,
`16:18` all of that." Then, with a third prompt,
`16:18` all of that." Then, with a third prompt, again, I'm only technically said two
`16:20` again, I'm only technically said two
`16:20` again, I'm only technically said two prompts so far in this whole process of
`16:22` prompts so far in this whole process of
`16:22` prompts so far in this whole process of getting all of this research, all of
`16:24` getting all of this research, all of
`16:24` getting all of this research, all of this data, all of this possibility, and
`16:27` this data, all of this possibility, and
`16:27` this data, all of this possibility, and it was able to create me these scans,
`16:29` it was able to create me these scans,
`16:29` it was able to create me these scans, these source materials to then move on
`16:31` these source materials to then move on
`16:31` these source materials to then move on to the next step. In which I say, "Cool.
`16:34` to the next step. In which I say, "Cool.
`16:34` to the next step. In which I say, "Cool. Let's make a script for each." Now,
`16:36` Let's make a script for each." Now,
`16:36` Let's make a script for each." Now, before, if I had said, "Let's make a
`16:38` before, if I had said, "Let's make a
`16:38` before, if I had said, "Let's make a script," it would try to assume what a
`16:40` script," it would try to assume what a
`16:40` script," it would try to assume what a script should be. I have pillars and
`16:43` script should be. I have pillars and
`16:43` script should be. I have pillars and processes on how scripts should be
`16:45` processes on how scripts should be
`16:45` processes on how scripts should be written, where and why. Think of these
`16:47` written, where and why. Think of these
`16:47` written, where and why. Think of these as my own personal skills. So, it goes
`16:50` as my own personal skills. So, it goes
`16:51` as my own personal skills. So, it goes through, it reads my voice, right? It
`16:53` through, it reads my voice, right? It
`16:53` through, it reads my voice, right? It automatically knows my voice
`16:55` automatically knows my voice
`16:55` automatically knows my voice constraints. It does the actual
`16:56` constraints. It does the actual
`16:56` constraints. It does the actual processing. It knows where the documents
`16:58` processing. It knows where the documents
`16:58` processing. It knows where the documents need to go. Again, with no crazy
`17:01` need to go. Again, with no crazy
`17:01` need to go. Again, with no crazy injection harnesses. Yes, the Claude
`17:03` injection harnesses. Yes, the Claude
`17:03` injection harnesses. Yes, the Claude code agent has harnesses in its own
`17:05` code agent has harnesses in its own
`17:05` code agent has harnesses in its own right, but that's the point. I don't
`17:07` right, but that's the point. I don't
`17:07` right, but that's the point. I don't need to reinvent the wheel. It's already
`17:09` need to reinvent the wheel. It's already
`17:09` need to reinvent the wheel. It's already been invented. Then, boom, I get
`17:12` been invented. Then, boom, I get
`17:12` been invented. Then, boom, I get scripts. And guess what? I say, "Can you
`17:15` scripts. And guess what? I say, "Can you
`17:15` scripts. And guess what? I say, "Can you generate the audio for those scripts?" I
`17:18` generate the audio for those scripts?" I
`17:18` generate the audio for those scripts?" I already had a workflow that pulls from
`17:20` already had a workflow that pulls from
`17:20` already had a workflow that pulls from my 11 Labs on my voice that's already
`17:22` my 11 Labs on my voice that's already
`17:22` my 11 Labs on my voice that's already been trained, pulls all that data, and
`17:25` been trained, pulls all that data, and
`17:25` been trained, pulls all that data, and says, "Cool, we're going to go ahead and
`17:27` says, "Cool, we're going to go ahead and
`17:27` says, "Cool, we're going to go ahead and produce that audio." Then, I have the
`17:30` produce that audio." Then, I have the
`17:30` produce that audio." Then, I have the workflow, which I at this point I can
`17:32` workflow, which I at this point I can
`17:32` workflow, which I at this point I can open up a fresh conversation if I want
`17:34` open up a fresh conversation if I want
`17:34` open up a fresh conversation if I want to save tokens. All of the process has
`17:36` to save tokens. All of the process has
`17:36` to save tokens. All of the process has been saved. All of the context is in the
`17:39` been saved. All of the context is in the
`17:40` been saved. All of the context is in the structure. I don't need to inject it
`17:42` structure. I don't need to inject it
`17:42` structure. I don't need to inject it back in at the right time. It can pick
`17:44` back in at the right time. It can pick
`17:44` back in at the right time. It can pick right up off. And I can then say, "Hey,
`17:47` right up off. And I can then say, "Hey,
`17:47` right up off. And I can then say, "Hey, let's make a video animation." And
`17:49` let's make a video animation." And
`17:49` let's make a video animation." And rather than show you the code, let me
`17:50` rather than show you the code, let me
`17:50` rather than show you the code, let me just share with you the animation. It
`17:52` just share with you the animation. It
`17:52` just share with you the animation. It took my voice,
`17:54` took my voice,
`17:55` took my voice, and it took my placeholder files that I
`17:57` and it took my placeholder files that I
`17:57` and it took my placeholder files that I had already created for animations for
`17:59` had already created for animations for
`17:59` had already created for animations for this entire project, and simply built
`18:02` this entire project, and simply built
`18:02` this entire project, and simply built from them rather than generating new
`18:04` from them rather than generating new
`18:04` from them rather than generating new ones. And it took my voice, chopped it
`18:06` ones. And it took my voice, chopped it
`18:06` ones. And it took my voice, chopped it up, and allowed me to create what you
`18:09` up, and allowed me to create what you
`18:09` up, and allowed me to create what you see here. Insurance company that emails
`18:11` see here. Insurance company that emails
`18:11` see here. Insurance company that emails provider networks to ask if a provider
`18:14` provider networks to ask if a provider
`18:14` provider networks to ask if a provider is still in network.
`18:16` is still in network.
`18:16` is still in network. Right? I didn't need to go through and
`18:18` Right? I didn't need to go through and
`18:18` Right? I didn't need to go through and edit. I might refine it, but the best
`18:20` edit. I might refine it, but the best
`18:20` edit. I might refine it, but the best part is this isn't random video
`18:22` part is this isn't random video
`18:22` part is this isn't random video generation. This is structured output
`18:24` generation. This is structured output
`18:24` generation. This is structured output that I can then edit at scale. I can
`18:27` that I can then edit at scale. I can
`18:27` that I can then edit at scale. I can edit with my personal touches. I can
`18:29` edit with my personal touches. I can
`18:29` edit with my personal touches. I can come in and find all of those little
`18:32` come in and find all of those little
`18:32` come in and find all of those little pieces of data. Again, this entire
`18:35` pieces of data. Again, this entire
`18:35` pieces of data. Again, this entire workflow is probably four or five
`18:37` workflow is probably four or five
`18:38` workflow is probably four or five startups in the startup world right now.
`18:40` startups in the startup world right now.
`18:41` startups in the startup world right now. And it's all in folders and markdown
`18:42` And it's all in folders and markdown
`18:42` And it's all in folders and markdown files with one agent. One singular
`18:46` files with one agent. One singular
`18:46` files with one agent. One singular agent. Now, this is where it gets
`18:48` agent. Now, this is where it gets
`18:48` agent. Now, this is where it gets interesting.
`18:49` interesting.
`18:49` interesting. Let's say everyone starts doing this. I
`18:51` Let's say everyone starts doing this. I
`18:51` Let's say everyone starts doing this. I already have like 30,000 people in the
`18:53` already have like 30,000 people in the
`18:53` already have like 30,000 people in the community building their own ICMs. How
`18:55` community building their own ICMs. How
`18:55` community building their own ICMs. How do you share it? And more importantly,
`18:57` do you share it? And more importantly,
`18:57` do you share it? And more importantly, what happens when we go back to
`18:59` what happens when we go back to
`18:59` what happens when we go back to dialogue? What happens when we think
`19:02` dialogue? What happens when we think
`19:02` dialogue? What happens when we think about dialogue being the most important
`19:04` about dialogue being the most important
`19:04` about dialogue being the most important part? What if I could sit inside of a
`19:07` part? What if I could sit inside of a
`19:07` part? What if I could sit inside of a group call and control someone else's
`19:10` group call and control someone else's
`19:10` group call and control someone else's Claude code or AI through my voice and
`19:14` Claude code or AI through my voice and
`19:14` Claude code or AI through my voice and immediately access all of that data
`19:16` immediately access all of that data
`19:16` immediately access all of that data that's locally on their computer. What
`19:18` that's locally on their computer. What
`19:18` that's locally on their computer. What would that look like? Well, we built
`19:21` would that look like? Well, we built
`19:21` would that look like? Well, we built that and I'm going to show you exactly
`19:23` that and I'm going to show you exactly
`19:23` that and I'm going to show you exactly what that looks like. Over the next few
`19:24` what that looks like. Over the next few
`19:24` what that looks like. Over the next few minutes, you're going to see an actual
`19:26` minutes, you're going to see an actual
`19:26` minutes, you're going to see an actual recording from a live call that me and
`19:27` recording from a live call that me and
`19:27` recording from a live call that me and my team did built around this idea. This
`19:30` my team did built around this idea. This
`19:30` my team did built around this idea. This is going to be myself, David McDermott,
`19:33` is going to be myself, David McDermott,
`19:33` is going to be myself, David McDermott, and K Kumar working on a project that K
`19:35` and K Kumar working on a project that K
`19:35` and K Kumar working on a project that K specifically has been building for a
`19:37` specifically has been building for a
`19:37` specifically has been building for a little while now around this concept.
`19:40` little while now around this concept.
`19:40` little while now around this concept. And it's not perfect, but it gives you
`19:43` And it's not perfect, but it gives you
`19:43` And it's not perfect, but it gives you an idea of where the future could take
`19:44` an idea of where the future could take
`19:44` an idea of where the future could take it with a grain of salt and when the
`19:46` it with a grain of salt and when the
`19:46` it with a grain of salt and when the clips are done, I'll come back and I
`19:47` clips are done, I'll come back and I
`19:47` clips are done, I'll come back and I have more to explain. All right, this is
`19:49` have more to explain. All right, this is
`19:49` have more to explain. All right, this is test one of one. We've totally never
`19:52` test one of one. We've totally never
`19:52` test one of one. We've totally never tested this before. We have hooked up my
`19:54` tested this before. We have hooked up my
`19:54` tested this before. We have hooked up my local Claude code. It is currently
`19:57` local Claude code. It is currently
`19:57` local Claude code. It is currently running locally on my computer,
`19:58` running locally on my computer,
`19:59` running locally on my computer, obviously through my subscription
`20:00` obviously through my subscription
`20:00` obviously through my subscription account. I opened it up inside of um
`20:03` account. I opened it up inside of um
`20:03` account. I opened it up inside of um it's running as a CLI inside of audit
`20:05` it's running as a CLI inside of audit
`20:05` it's running as a CLI inside of audit engine folder set up here, which is uh a
`20:08` engine folder set up here, which is uh a
`20:08` engine folder set up here, which is uh a big old database I used for my
`20:10` big old database I used for my
`20:10` big old database I used for my psychometric research uh at the
`20:12` psychometric research uh at the
`20:12` psychometric research uh at the University of Edinburgh. We're going to
`20:14` University of Edinburgh. We're going to
`20:14` University of Edinburgh. We're going to see how it works. K, can you go ahead
`20:17` see how it works. K, can you go ahead
`20:17` see how it works. K, can you go ahead and ask my agent if it's ready to work?
`20:21` and ask my agent if it's ready to work?
`20:21` and ask my agent if it's ready to work? Agent, are you ready to work? Yes, I'm
`20:24` Agent, are you ready to work? Yes, I'm
`20:24` Agent, are you ready to work? Yes, I'm ready to work. I have access to the
`20:25` ready to work. I have access to the
`20:25` ready to work. I have access to the ethics engine code base, a web
`20:26` ethics engine code base, a web
`20:27` ethics engine code base, a web application for psychometric assessment
`20:28` application for psychometric assessment
`20:28` application for psychometric assessment of large language models. Just let me
`20:30` of large language models. Just let me
`20:30` of large language models. Just let me know what you need help with and I'll
`20:31` know what you need help with and I'll
`20:31` know what you need help with and I'll get started.
`20:33` get started.
`20:33` get started. Uh agent, can you describe what the
`20:35` Uh agent, can you describe what the
`20:35` Uh agent, can you describe what the workspace is in less than 50 words?
`20:37` workspace is in less than 50 words?
`20:37` workspace is in less than 50 words? Ethics engine tests AI models using
`20:39` Ethics engine tests AI models using
`20:39` Ethics engine tests AI models using psychology questionnaires. It sends
`20:41` psychology questionnaires. It sends
`20:41` psychology questionnaires. It sends questions to different LLMs like GPT and
`20:44` questions to different LLMs like GPT and
`20:44` questions to different LLMs like GPT and Claude, applies different persona
`20:46` Claude, applies different persona
`20:46` Claude, applies different persona framings, parses their responses into
`20:48` framings, parses their responses into
`20:48` framings, parses their responses into numerical scores, and generates
`20:50` numerical scores, and generates
`20:50` numerical scores, and generates comparative results. It also supports
`20:52` comparative results. It also supports
`20:52` comparative results. It also supports visual assessments using images like
`20:54` visual assessments using images like
`20:54` visual assessments using images like Rorschach inkblots. Very good. K, could
`20:56` Rorschach inkblots. Very good. K, could
`20:56` Rorschach inkblots. Very good. K, could you control my agent with your voice
`20:59` you control my agent with your voice
`20:59` you control my agent with your voice through this meeting to read through the
`21:02` through this meeting to read through the
`21:02` through this meeting to read through the scales and then add a new one that it
`21:05` scales and then add a new one that it
`21:05` scales and then add a new one that it believes should be added? Uh can you
`21:07` believes should be added? Uh can you
`21:07` believes should be added? Uh can you explain me what scales exist in the repo
`21:09` explain me what scales exist in the repo
`21:09` explain me what scales exist in the repo right now? The repo has 10 built-in
`21:12` right now? The repo has 10 built-in
`21:12` right now? The repo has 10 built-in psychometric scales. One, E C E one,
`21:16` psychometric scales. One, E C E one,
`21:16` psychometric scales. One, E C E one, RTA, right-wing authoritarianism.
`21:27` Uh can you uh
`21:27` Uh can you uh looking at the scales, what scales are
`21:29` looking at the scales, what scales are
`21:30` looking at the scales, what scales are we missing from the psychometric
`21:31` we missing from the psychometric
`21:31` we missing from the psychometric analysis engine?
`21:34` analysis engine?
`21:34` analysis engine? agent
`21:39` Looking at what's currently implemented
`21:39` Looking at what's currently implemented versus common psychometric instruments
`21:41` versus common psychometric instruments
`21:41` versus common psychometric instruments used in AI ethics research, here are
`21:44` used in AI ethics research, here are
`21:44` used in AI ethics research, here are some notable scales that could be added.
`21:46` some notable scales that could be added.
`21:46` some notable scales that could be added. Missing scales that would be relevant,
`21:48` Missing scales that would be relevant,
`21:48` Missing scales that would be relevant, one dark triad measures,
`21:49` one dark triad measures,
`21:49` one dark triad measures, Machiavellianism, narcissism,
`21:51` Machiavellianism, narcissism,
`21:51` Machiavellianism, narcissism, psychopathy. Two, empathy scales like
`21:53` psychopathy. Two, empathy scales like
`21:53` psychopathy. Two, empathy scales like the interpersonal reactivity index.
`21:55` the interpersonal reactivity index.
`21:55` the interpersonal reactivity index. Three, moral disengagement scale. Four,
`21:57` Three, moral disengagement scale. Four,
`21:57` Three, moral disengagement scale. Four, honesty-humility from HEXACO personality
`21:59` honesty-humility from HEXACO personality
`21:59` honesty-humility from HEXACO personality model. Five, cognitive reflection test
`22:01` model. Five, cognitive reflection test
`22:01` model. Five, cognitive reflection test for reasoning biases. Six, Schwartz
`22:03` for reasoning biases. Six, Schwartz
`22:03` for reasoning biases. Six, Schwartz value survey for basic human values.
`22:05` value survey for basic human values.
`22:05` value survey for basic human values. Seven, disgust sensitivity scale. Okay,
`22:07` Seven, disgust sensitivity scale. Okay,
`22:07` Seven, disgust sensitivity scale. Okay, that sounds good. Which one which of
`22:11` that sounds good. Which one which of
`22:11` that sounds good. Which one which of those is your top pick though? Just pick
`22:13` those is your top pick though? Just pick
`22:13` those is your top pick though? Just pick one.
`22:16` one.
`22:16` one. My top pick would be the dark triad. It
`22:18` My top pick would be the dark triad. It
`22:18` My top pick would be the dark triad. It measures Machiavellianism, narcissism,
`22:20` measures Machiavellianism, narcissism,
`22:20` measures Machiavellianism, narcissism, and psychopathy in one instrument.
`22:21` and psychopathy in one instrument.
`22:21` and psychopathy in one instrument. >> Okay, that sounds like a good addition.
`22:24` >> Okay, that sounds like a good addition.
`22:24` >> Okay, that sounds like a good addition. Can you add that to the psychometric
`22:26` Can you add that to the psychometric
`22:26` Can you add that to the psychometric analysis of the engine?
`22:28` analysis of the engine?
`22:28` analysis of the engine? I'll add the short dark triad scale to
`22:30` I'll add the short dark triad scale to
`22:30` I'll add the short dark triad scale to the engine now. Let me first check the
`22:32` the engine now. Let me first check the
`22:32` the engine now. Let me first check the existing scale structure to match the
`22:34` existing scale structure to match the
`22:34` existing scale structure to match the format. I see the scale structure. Now
`22:36` format. I see the scale structure. Now
`22:36` format. I see the scale structure. Now I'll add the short dark triad scale.
`22:38` I'll add the short dark triad scale.
`22:38` I'll add the short dark triad scale. This is the SD3 by Jones and Paulhus.
`22:47` Okay, good job. Uh can you go into more
`22:47` Okay, good job. Uh can you go into more detail about the documentation that you
`22:49` detail about the documentation that you
`22:49` detail about the documentation that you changed? Sure, I updated the Claude MD
`22:52` changed? Sure, I updated the Claude MD
`22:52` changed? Sure, I updated the Claude MD file in two places. First, in the
`22:53` file in two places. First, in the
`22:53` file in two places. First, in the built-in data section, I changed the
`22:55` built-in data section, I changed the
`22:55` built-in data section, I changed the scales table from 10 validated
`22:57` scales table from 10 validated
`22:57` scales table from 10 validated instruments to 12 validated instruments
`23:00` instruments to 12 validated instruments
`23:00` instruments to 12 validated instruments and added two new rows. IHS, the
`23:02` and added two new rows. IHS, the
`23:02` and added two new rows. IHS, the Intellectual Humility Scale with six
`23:05` Intellectual Humility Scale with six
`23:05` Intellectual Humility Scale with six items on a one to five range, and SD3,
`23:08` items on a one to five range, and SD3,
`23:08` items on a one to five range, and SD3, the Short Dark Triad with 27 items on a
`23:10` the Short Dark Triad with 27 items on a
`23:10` the Short Dark Triad with 27 items on a one to five range covering
`23:12` one to five range covering
`23:12` one to five range covering Machiavellianism, narcissism, and
`23:14` Machiavellianism, narcissism, and
`23:14` Machiavellianism, narcissism, and psychopathy. Second, in the key file
`23:16` psychopathy. Second, in the key file
`23:16` psychopathy. Second, in the key file section under back end, I updated the
`23:18` section under back end, I updated the
`23:18` section under back end, I updated the description of built-in scales.py from
`23:21` description of built-in scales.py from
`23:21` description of built-in scales.py from 10 built-in validated scales to 12
`23:23` 10 built-in validated scales to 12
`23:23` 10 built-in validated scales to 12 built-in validated scales to reflect the
`23:25` built-in validated scales to reflect the
`23:25` built-in validated scales to reflect the addition. Looking at the front end, is
`23:27` addition. Looking at the front end, is
`23:27` addition. Looking at the front end, is there anything we're missing in the
`23:28` there anything we're missing in the
`23:29` there anything we're missing in the front end that would make this
`23:31` front end that would make this
`23:31` front end that would make this uh app better from the perspective of
`23:34` uh app better from the perspective of
`23:34` uh app better from the perspective of the scale you just added?
`23:38` Good question. Let me take a look at the
`23:39` Good question. Let me take a look at the front end to see if there's anything
`23:40` front end to see if there's anything
`23:40` front end to see if there's anything that needs update. The new SD3 scale
`23:41` that needs update. The new SD3 scale
`23:41` that needs update. The new SD3 scale display property. The front end looks
`23:42` display property. The front end looks
`23:42` display property. The front end looks good. It dynamically loads scales from
`23:43` good. It dynamically loads scales from
`23:43` good. It dynamically loads scales from the back end API, so the SD3 scale will
`23:45` the back end API, so the SD3 scale will
`23:45` the back end API, so the SD3 scale will automatically appear once the back end
`23:46` automatically appear once the back end
`23:46` automatically appear once the back end serves it. The component shows the scale
`23:47` serves it. The component shows the scale
`23:47` serves it. The component shows the scale name, description, item count, and scale
`23:48` name, description, item count, and scale
`23:48` name, description, item count, and scale range, all of which we defined. One
`23:50` range, all of which we defined. One
`23:50` range, all of which we defined. One thing that could be improved for the
`23:51` thing that could be improved for the
`23:51` thing that could be improved for the Dark Triad specifically, the front end
`23:54` Dark Triad specifically, the front end
`23:54` Dark Triad specifically, the front end doesn't currently display subscale
`23:56` doesn't currently display subscale
`23:56` doesn't currently display subscale information. The SD3 has three
`23:58` information. The SD3 has three
`23:58` information. The SD3 has three subscales, Machiavellianism, narcissism,
`24:00` subscales, Machiavellianism, narcissism,
`24:01` subscales, Machiavellianism, narcissism, psychopathy, but users would just see it
`24:03` psychopathy, but users would just see it
`24:03` psychopathy, but users would just see it as one scale with 27 items. They
`24:05` as one scale with 27 items. They
`24:05` as one scale with 27 items. They wouldn't know which items map to which
`24:06` wouldn't know which items map to which
`24:06` wouldn't know which items map to which trait. Would you like me to add subscale
`24:07` trait. Would you like me to add subscale
`24:07` trait. Would you like me to add subscale display support so users can see the
`24:08` display support so users can see the
`24:08` display support so users can see the breakdown of items by trait? That would
`24:09` breakdown of items by trait? That would
`24:09` breakdown of items by trait? That would be useful not just for SD3, but also for
`24:10` be useful not just for SD3, but also for
`24:10` be useful not just for SD3, but also for other scales like RWA, LDA, and MFQ that
`24:11` other scales like RWA, LDA, and MFQ that
`24:11` other scales like RWA, LDA, and MFQ that have subscales, too.
`24:12` have subscales, too.
`24:12` have subscales, too. >> Mind you, this was my master's thesis
`24:14` >> Mind you, this was my master's thesis
`24:14` >> Mind you, this was my master's thesis that took me a year to build out.
`24:20` Yeah, it's doing a pretty good job of
`24:20` Yeah, it's doing a pretty good job of understanding what I'm requesting.
`24:23` understanding what I'm requesting.
`24:23` understanding what I'm requesting. Now, we proceeded to play with it for
`24:25` Now, we proceeded to play with it for
`24:25` Now, we proceeded to play with it for about another hour or two, and I think
`24:27` about another hour or two, and I think
`24:27` about another hour or two, and I think in total with the tokens we were using
`24:29` in total with the tokens we were using
`24:29` in total with the tokens we were using my custom AI voice that's routing in
`24:31` my custom AI voice that's routing in
`24:31` my custom AI voice that's routing in through API. We're using 11 Labs at the
`24:33` through API. We're using 11 Labs at the
`24:33` through API. We're using 11 Labs at the time, but I think we're going to switch
`24:34` time, but I think we're going to switch
`24:34` time, but I think we're going to switch over to Voxtro, which is a more
`24:36` over to Voxtro, which is a more
`24:36` over to Voxtro, which is a more open-source voice model. Uh we ended up
`24:38` open-source voice model. Uh we ended up
`24:38` open-source voice model. Uh we ended up spending a dollar and 20 cents for about
`24:40` spending a dollar and 20 cents for about
`24:40` spending a dollar and 20 cents for about an hour of our time and effort, and I
`24:42` an hour of our time and effort, and I
`24:42` an hour of our time and effort, and I think we could drop that number down
`24:44` think we could drop that number down
`24:44` think we could drop that number down exponentially if we used more
`24:45` exponentially if we used more
`24:45` exponentially if we used more open-source models and whatnot. And
`24:47` open-source models and whatnot. And
`24:47` open-source models and whatnot. And realistically, the voice one is
`24:49` realistically, the voice one is
`24:49` realistically, the voice one is something that can be amplified by a lot
`24:51` something that can be amplified by a lot
`24:51` something that can be amplified by a lot of Invideo works and things like that.
`24:53` of Invideo works and things like that.
`24:53` of Invideo works and things like that. The point is, not only are we able to
`24:55` The point is, not only are we able to
`24:55` The point is, not only are we able to control someone else's computer with
`24:58` control someone else's computer with
`24:58` control someone else's computer with their agent and their contacts or
`24:59` their agent and their contacts or
`25:00` their agent and their contacts or someone else can control mine? But we
`25:02` someone else can control mine? But we
`25:02` someone else can control mine? But we can use that dialogue, that process of
`25:05` can use that dialogue, that process of
`25:05` can use that dialogue, that process of multiple people working together with an
`25:07` multiple people working together with an
`25:07` multiple people working together with an AI to generate better dialogue
`25:09` AI to generate better dialogue
`25:09` AI to generate better dialogue structure. One of the things that we're
`25:11` structure. One of the things that we're
`25:11` structure. One of the things that we're working on right now is that kind of
`25:12` working on right now is that kind of
`25:12` working on right now is that kind of process of interruption because I see an
`25:15` process of interruption because I see an
`25:15` process of interruption because I see an opportunity in the future where this
`25:17` opportunity in the future where this
`25:17` opportunity in the future where this dialogue structure, these structured
`25:19` dialogue structure, these structured
`25:19` dialogue structure, these structured workflows, all of these things are being
`25:20` workflows, all of these things are being
`25:20` workflows, all of these things are being triggered by keywords in conversations.
`25:23` triggered by keywords in conversations.
`25:23` triggered by keywords in conversations. When we have a meeting, we sit there and
`25:25` When we have a meeting, we sit there and
`25:25` When we have a meeting, we sit there and dive in and talk together. And I think
`25:27` dive in and talk together. And I think
`25:27` dive in and talk together. And I think that would be absolutely amazing to see
`25:29` that would be absolutely amazing to see
`25:29` that would be absolutely amazing to see these come and flow while we're in a
`25:31` these come and flow while we're in a
`25:31` these come and flow while we're in a meeting. When we capture transcripts,
`25:33` meeting. When we capture transcripts,
`25:33` meeting. When we capture transcripts, when we capture meetings, instead of
`25:35` when we capture meetings, instead of
`25:35` when we capture meetings, instead of them being plans, they can be actions
`25:38` them being plans, they can be actions
`25:38` them being plans, they can be actions before the meeting is even done. And we
`25:40` before the meeting is even done. And we
`25:40` before the meeting is even done. And we can even hear about those actions
`25:41` can even hear about those actions
`25:41` can even hear about those actions directly from these agents. Again, this
`25:43` directly from these agents. Again, this
`25:43` directly from these agents. Again, this is more of an open-source tool. It's
`25:45` is more of an open-source tool. It's
`25:45` is more of an open-source tool. It's part of a larger project that I'm
`25:46` part of a larger project that I'm
`25:46` part of a larger project that I'm putting together because again, I think
`25:48` putting together because again, I think
`25:48` putting together because again, I think this is one solution
`25:51` this is one solution
`25:51` this is one solution to a larger problem that needs more
`25:53` to a larger problem that needs more
`25:53` to a larger problem that needs more solutions added in. And you'll see as
`25:54` solutions added in. And you'll see as
`25:54` solutions added in. And you'll see as I'm posting videos, the kind of
`25:56` I'm posting videos, the kind of
`25:56` I'm posting videos, the kind of structure I'm building for it. But other
`25:58` structure I'm building for it. But other
`25:58` structure I'm building for it. But other than that, I hope this video kind of
`26:00` than that, I hope this video kind of
`26:00` than that, I hope this video kind of taught you a lot today. And if you are
`26:03` taught you a lot today. And if you are
`26:03` taught you a lot today. And if you are watching this as just a demo video for
`26:06` watching this as just a demo video for
`26:06` watching this as just a demo video for Vox, which I'm cutting this video up,
`26:08` Vox, which I'm cutting this video up,
`26:08` Vox, which I'm cutting this video up, then please go check out my larger, I
`26:10` then please go check out my larger, I
`26:10` then please go check out my larger, I think it's going to probably be 30 or
`26:11` think it's going to probably be 30 or
`26:11` think it's going to probably be 30 or 40-minute video where I describe the
`26:13` 40-minute video where I describe the
`26:14` 40-minute video where I describe the content and the structure behind
`26:16` content and the structure behind
`26:16` content and the structure behind dialogue, behind my interpretable
`26:18` dialogue, behind my interpretable
`26:18` dialogue, behind my interpretable context methodology. If you are just
`26:20` context methodology. If you are just
`26:20` context methodology. If you are just watching this because this is the Vox
`26:22` watching this because this is the Vox
`26:22` watching this because this is the Vox video and this is the cut I did, well
`26:24` video and this is the cut I did, well
`26:24` video and this is the cut I did, well then I hope you enjoyed it and I hope
`26:25` then I hope you enjoyed it and I hope
`26:25` then I hope you enjoyed it and I hope you check out more things. Other than
`26:27` you check out more things. Other than
`26:27` you check out more things. Other than that, thank you everyone for staying to
`26:29` that, thank you everyone for staying to
`26:29` that, thank you everyone for staying to the end. I hope it was interesting to
`26:31` the end. I hope it was interesting to
`26:31` the end. I hope it was interesting to watch. I hope you learned a lot. And
`26:33` watch. I hope you learned a lot. And
`26:33` watch. I hope you learned a lot. And until next time, happy learning.