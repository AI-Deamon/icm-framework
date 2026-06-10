# Afternoon Tea #2: Stop Building Production-Ready AI. Solve for One Client First

**Channel:** Jake Van Clief  
**Uploaded:** 2026-04-29  
**Duration:** 54:46  
**URL:** [https://www.youtube.com/watch?v=AZ1l-oaD3tk](https://www.youtube.com/watch?v=AZ1l-oaD3tk)  

---

## Transcript

`00:01` start talking here in a moment. All
`00:01` start talking here in a moment. All right. Well, hello everyone. This is our
`00:03` right. Well, hello everyone. This is our
`00:03` right. Well, hello everyone. This is our second official afternoon tea for all of
`00:06` second official afternoon tea for all of
`00:06` second official afternoon tea for all of our lovely premium members out there and
`00:08` our lovely premium members out there and
`00:08` our lovely premium members out there and of course VIP inside of it. Now, the
`00:10` of course VIP inside of it. Now, the
`00:10` of course VIP inside of it. Now, the main goal for today is to actually look
`00:12` main goal for today is to actually look
`00:12` main goal for today is to actually look at skills and plugins because I saw a
`00:14` at skills and plugins because I saw a
`00:14` at skills and plugins because I saw a lot of questions from all of you about
`00:15` lot of questions from all of you about
`00:15` lot of questions from all of you about that. But from a kind of higher level
`00:17` that. But from a kind of higher level
`00:17` that. But from a kind of higher level perspective and then I also wanted to
`00:19` perspective and then I also wanted to
`00:19` perspective and then I also wanted to talk about the affiliate program that we
`00:21` talk about the affiliate program that we
`00:21` talk about the affiliate program that we just launched with the links that you
`00:23` just launched with the links that you
`00:23` just launched with the links that you all can access. Um, but let's uh let's
`00:26` all can access. Um, but let's uh let's
`00:26` all can access. Um, but let's uh let's go ahead and dive in. I also am probably
`00:28` go ahead and dive in. I also am probably
`00:28` go ahead and dive in. I also am probably going to ask some questions from chat
`00:29` going to ask some questions from chat
`00:29` going to ask some questions from chat today, too. So, that's cool. Again, for
`00:32` today, too. So, that's cool. Again, for
`00:32` today, too. So, that's cool. Again, for some of you, you may really deeply
`00:33` some of you, you may really deeply
`00:33` some of you, you may really deeply understand a skill. And this may seem
`00:35` understand a skill. And this may seem
`00:35` understand a skill. And this may seem basic. Just hold on your horses. I'm
`00:37` basic. Just hold on your horses. I'm
`00:37` basic. Just hold on your horses. I'm going to dive into some more advanced
`00:38` going to dive into some more advanced
`00:38` going to dive into some more advanced stuff as well. But essentially, skills
`00:42` stuff as well. But essentially, skills
`00:42` stuff as well. But essentially, skills are my folder architecture, but in kind
`00:45` are my folder architecture, but in kind
`00:45` are my folder architecture, but in kind of a different routing way. And it's not
`00:47` of a different routing way. And it's not
`00:47` of a different routing way. And it's not just for Claude. Claude definitely
`00:49` just for Claude. Claude definitely
`00:49` just for Claude. Claude definitely really uses it well. Um, but the folder
`00:52` really uses it well. Um, but the folder
`00:52` really uses it well. Um, but the folder architecture of skills is very
`00:55` architecture of skills is very
`00:55` architecture of skills is very different. Um, oh, blue services. I see
`00:57` different. Um, oh, blue services. I see
`00:57` different. Um, oh, blue services. I see you hear no audio. It might just be a
`00:59` you hear no audio. It might just be a
`00:59` you hear no audio. It might just be a you thing. I don't know. Can we Does
`01:02` you thing. I don't know. Can we Does
`01:02` you thing. I don't know. Can we Does everyone else can still hear me? Okay.
`01:04` everyone else can still hear me? Okay.
`01:04` everyone else can still hear me? Okay. I'm sorry, bud. That might be a that
`01:06` I'm sorry, bud. That might be a that
`01:06` I'm sorry, bud. That might be a that might be a you thing. Um I'm sorry.
`01:09` might be a you thing. Um I'm sorry.
`01:09` might be a you thing. Um I'm sorry. Well, if anything, I'll have it recorded
`01:11` Well, if anything, I'll have it recorded
`01:11` Well, if anything, I'll have it recorded after if uh you can't get to it. But
`01:13` after if uh you can't get to it. But
`01:14` after if uh you can't get to it. But essentially, um one of the most
`01:15` essentially, um one of the most
`01:15` essentially, um one of the most important things with Claude skills
`01:17` important things with Claude skills
`01:17` important things with Claude skills specifically is they have a little YAML
`01:19` specifically is they have a little YAML
`01:19` specifically is they have a little YAML um or JSON uh initiation at the
`01:21` um or JSON uh initiation at the
`01:21` um or JSON uh initiation at the beginning. So, anytime Claude is looking
`01:24` beginning. So, anytime Claude is looking
`01:24` beginning. So, anytime Claude is looking for a skill, it's going to look for a
`01:26` for a skill, it's going to look for a
`01:26` for a skill, it's going to look for a name and a description first without
`01:28` name and a description first without
`01:28` name and a description first without reading the entire markdown file. It's
`01:30` reading the entire markdown file. It's
`01:30` reading the entire markdown file. It's how it saves a lot of tokens searching
`01:32` how it saves a lot of tokens searching
`01:32` how it saves a lot of tokens searching through documents. And it has its own
`01:34` through documents. And it has its own
`01:34` through documents. And it has its own routing structure as well to go search
`01:36` routing structure as well to go search
`01:36` routing structure as well to go search through all of those as well. Like, hey,
`01:38` through all of those as well. Like, hey,
`01:38` through all of those as well. Like, hey, you know, locate these skills in this
`01:40` you know, locate these skills in this
`01:40` you know, locate these skills in this area. You can even create your own
`01:42` area. You can even create your own
`01:42` area. You can even create your own routing structure. And I'm going to show
`01:43` routing structure. And I'm going to show
`01:43` routing structure. And I'm going to show it here in a second. Um, one thing is if
`01:47` it here in a second. Um, one thing is if
`01:47` it here in a second. Um, one thing is if you relay it to my ICM. So again my
`01:51` you relay it to my ICM. So again my
`01:51` you relay it to my ICM. So again my inter interpretable
`01:54` inter interpretable
`01:54` inter interpretable context methodology framework uh that
`01:56` context methodology framework uh that
`01:56` context methodology framework uh that I've kind of created that paper for
`01:58` I've kind of created that paper for
`01:58` I've kind of created that paper for those of you who've read it and for
`02:00` those of you who've read it and for
`02:00` those of you who've read it and for those of you who haven't it's
`02:01` those of you who haven't it's
`02:01` those of you who haven't it's essentially I tried to take thinking the
`02:04` essentially I tried to take thinking the
`02:04` essentially I tried to take thinking the way in which we think about processes we
`02:06` way in which we think about processes we
`02:06` way in which we think about processes we break them down we organize them and I
`02:09` break them down we organize them and I
`02:09` break them down we organize them and I took it and applied it to the way that
`02:11` took it and applied it to the way that
`02:11` took it and applied it to the way that AI reads these and over time I started
`02:14` AI reads these and over time I started
`02:14` AI reads these and over time I started seeing patterns of really good
`02:15` seeing patterns of really good
`02:16` seeing patterns of really good efficiency and formatting a skill is
`02:19` efficiency and formatting a skill is
`02:19` efficiency and formatting a skill is essentially what I am doing in a
`02:22` essentially what I am doing in a
`02:22` essentially what I am doing in a different format. And that's why I
`02:23` different format. And that's why I
`02:23` different format. And that's why I always say you don't have to take all of
`02:25` always say you don't have to take all of
`02:25` always say you don't have to take all of my stuff as concrete. It can be a
`02:28` my stuff as concrete. It can be a
`02:28` my stuff as concrete. It can be a version that you kind of develop on your
`02:30` version that you kind of develop on your
`02:30` version that you kind of develop on your own or you tweak it. It's just the way
`02:32` own or you tweak it. It's just the way
`02:32` own or you tweak it. It's just the way that it makes sense for me in most cases
`02:35` that it makes sense for me in most cases
`02:35` that it makes sense for me in most cases and I formalized it. A lot of people in
`02:37` and I formalized it. A lot of people in
`02:37` and I formalized it. A lot of people in this community were already doing ICM
`02:40` this community were already doing ICM
`02:40` this community were already doing ICM processes, but they just weren't calling
`02:42` processes, but they just weren't calling
`02:42` processes, but they just weren't calling it that. They discovered it on their own
`02:44` it that. They discovered it on their own
`02:44` it that. They discovered it on their own because it was the most useful way to
`02:46` because it was the most useful way to
`02:46` because it was the most useful way to route an AI through context context
`02:49` route an AI through context context
`02:49` route an AI through context context engineering with very little
`02:50` engineering with very little
`02:50` engineering with very little infrastructure. Obviously, there's a lot
`02:52` infrastructure. Obviously, there's a lot
`02:52` infrastructure. Obviously, there's a lot of ways to create infrastructure and
`02:54` of ways to create infrastructure and
`02:54` of ways to create infrastructure and route context. There's rag pipelines.
`02:57` route context. There's rag pipelines.
`02:57` route context. There's rag pipelines. There's vector databases, lang chain,
`02:59` There's vector databases, lang chain,
`02:59` There's vector databases, lang chain, langraph, semantic kernel, the list goes
`03:01` langraph, semantic kernel, the list goes
`03:01` langraph, semantic kernel, the list goes on. I just really love the simplicity of
`03:04` on. I just really love the simplicity of
`03:04` on. I just really love the simplicity of a couple folders and a couple markdown
`03:06` a couple folders and a couple markdown
`03:06` a couple folders and a couple markdown files with the occasional script here or
`03:08` files with the occasional script here or
`03:08` files with the occasional script here or there. Um but if you really look at what
`03:12` there. Um but if you really look at what
`03:12` there. Um but if you really look at what skills do right the YAML front matter
`03:14` skills do right the YAML front matter
`03:14` skills do right the YAML front matter that little thing that the skill has at
`03:16` that little thing that the skill has at
`03:16` that little thing that the skill has at the top is its identity right the
`03:18` the top is its identity right the
`03:18` the top is its identity right the description of where and what it's used
`03:21` description of where and what it's used
`03:21` description of where and what it's used for is kind of like routing for the
`03:23` for is kind of like routing for the
`03:23` for is kind of like routing for the skill itself but back at the model the
`03:26` skill itself but back at the model the
`03:26` skill itself but back at the model the skill MD the whole body or the multiple
`03:28` skill MD the whole body or the multiple
`03:28` skill MD the whole body or the multiple of them also has workflows and steps and
`03:31` of them also has workflows and steps and
`03:31` of them also has workflows and steps and that body may also route to other
`03:34` that body may also route to other
`03:34` that body may also route to other markdown files and references which
`03:36` markdown files and references which
`03:36` markdown files and references which you'll see there and if you look these
`03:38` you'll see there and if you look these
`03:38` you'll see there and if you look these are layers
`03:39` are layers
`03:39` are layers in thought. It's what when do you need
`03:42` in thought. It's what when do you need
`03:42` in thought. It's what when do you need to think about something? You think
`03:43` to think about something? You think
`03:43` to think about something? You think about the identity. Then you go in route
`03:45` about the identity. Then you go in route
`03:46` about the identity. Then you go in route to why you're using that identity. Then
`03:48` to why you're using that identity. Then
`03:48` to why you're using that identity. Then you're reading the contract of that
`03:50` you're reading the contract of that
`03:50` you're reading the contract of that process, that instruction. And then
`03:52` process, that instruction. And then
`03:52` process, that instruction. And then you're going and referencing maybe
`03:53` you're going and referencing maybe
`03:54` you're going and referencing maybe certain things inside of that process
`03:55` certain things inside of that process
`03:55` certain things inside of that process and then you create an output and then
`03:57` and then you create an output and then
`03:57` and then you create an output and then maybe you need to rework that output and
`03:59` maybe you need to rework that output and
`04:00` maybe you need to rework that output and do something with it. Skills are using
`04:02` do something with it. Skills are using
`04:02` do something with it. Skills are using this methodology. Absolutely. Um and
`04:05` this methodology. Absolutely. Um and
`04:05` this methodology. Absolutely. Um and there's a couple ways. So I I wanted to
`04:07` there's a couple ways. So I I wanted to
`04:07` there's a couple ways. So I I wanted to instead of just sitting here and talking
`04:08` instead of just sitting here and talking
`04:08` instead of just sitting here and talking head you just dive in for some people
`04:11` head you just dive in for some people
`04:11` head you just dive in for some people again referencing where to find them,
`04:14` again referencing where to find them,
`04:14` again referencing where to find them, how to organize your file structure.
`04:15` how to organize your file structure.
`04:15` how to organize your file structure. These are all really important
`04:17` These are all really important
`04:17` These are all really important questions, but we want to think about
`04:18` questions, but we want to think about
`04:18` questions, but we want to think about how to think about these things. If you
`04:21` how to think about these things. If you
`04:21` how to think about these things. If you noticed all of my videos, I don't really
`04:23` noticed all of my videos, I don't really
`04:23` noticed all of my videos, I don't really talk about features that much. I talk
`04:26` talk about features that much. I talk
`04:26` talk about features that much. I talk about processes. And I could make a
`04:28` about processes. And I could make a
`04:28` about processes. And I could make a whole bunch of videos about new updates
`04:30` whole bunch of videos about new updates
`04:30` whole bunch of videos about new updates that Claude or the new 5.5 Codeex,
`04:32` that Claude or the new 5.5 Codeex,
`04:32` that Claude or the new 5.5 Codeex, right? I have subscriptions to Codeex,
`04:34` right? I have subscriptions to Codeex,
`04:34` right? I have subscriptions to Codeex, to Gemini, all of these. I'm constantly
`04:36` to Gemini, all of these. I'm constantly
`04:36` to Gemini, all of these. I'm constantly testing them, but I'm trying to create
`04:38` testing them, but I'm trying to create
`04:38` testing them, but I'm trying to create methodology that works with all of them
`04:41` methodology that works with all of them
`04:41` methodology that works with all of them at all times. And that comes down to
`04:43` at all times. And that comes down to
`04:43` at all times. And that comes down to breaking the thinking about using the
`04:45` breaking the thinking about using the
`04:45` breaking the thinking about using the features, not the features themselves.
`04:47` features, not the features themselves.
`04:47` features, not the features themselves. But if you're sitting in there and
`04:48` But if you're sitting in there and
`04:48` But if you're sitting in there and you're in the app, you can come to
`04:50` you're in the app, you can come to
`04:50` you're in the app, you can come to customize and you can actually see
`04:52` customize and you can actually see
`04:52` customize and you can actually see there's a whole list of skills that and
`04:54` there's a whole list of skills that and
`04:54` there's a whole list of skills that and you can add as many as you want. You can
`04:56` you can add as many as you want. You can
`04:56` you can add as many as you want. You can create a skill. Well, when you actually
`04:58` create a skill. Well, when you actually
`04:58` create a skill. Well, when you actually look at that skill, this UI is handling
`05:01` look at that skill, this UI is handling
`05:02` look at that skill, this UI is handling the routing for you. It's coming in and
`05:04` the routing for you. It's coming in and
`05:04` the routing for you. It's coming in and saying, "Hey, this is where the skills
`05:06` saying, "Hey, this is where the skills
`05:06` saying, "Hey, this is where the skills are. Here's an easy way." Instead of me
`05:08` are. Here's an easy way." Instead of me
`05:08` are. Here's an easy way." Instead of me having to go in here, find Claude
`05:10` having to go in here, find Claude
`05:10` having to go in here, find Claude installed on my computer, click into the
`05:12` installed on my computer, click into the
`05:12` installed on my computer, click into the skills, and go find those skills. It's
`05:14` skills, and go find those skills. It's
`05:14` skills, and go find those skills. It's saying, "Hey, it's right here. This is
`05:15` saying, "Hey, it's right here. This is
`05:16` saying, "Hey, it's right here. This is the routing for us." And it makes it
`05:17` the routing for us." And it makes it
`05:18` the routing for us." And it makes it easier to find that. But you want to do
`05:19` easier to find that. But you want to do
`05:19` easier to find that. But you want to do the same thing with AI. And if you open
`05:22` the same thing with AI. And if you open
`05:22` the same thing with AI. And if you open it up, uh, let's actually look at the
`05:23` it up, uh, let's actually look at the
`05:24` it up, uh, let's actually look at the skill creator skill. It's literally a
`05:26` skill creator skill. It's literally a
`05:26` skill creator skill. It's literally a skill on how to create skills. Uh it's
`05:28` skill on how to create skills. Uh it's
`05:28` skill on how to create skills. Uh it's the same thing. Markdown files followed
`05:31` the same thing. Markdown files followed
`05:31` the same thing. Markdown files followed by organized folder structure for
`05:33` by organized folder structure for
`05:33` by organized folder structure for different types of thinking. What types
`05:35` different types of thinking. What types
`05:35` different types of thinking. What types of skills would it need to do? Are you
`05:37` of skills would it need to do? Are you
`05:38` of skills would it need to do? Are you going to compare skills together? Can
`05:40` going to compare skills together? Can
`05:40` going to compare skills together? Can you grade that skill? And it creates an
`05:42` you grade that skill? And it creates an
`05:42` you grade that skill? And it creates an quote unquote agent, but it's just again
`05:44` quote unquote agent, but it's just again
`05:44` quote unquote agent, but it's just again an agent is just another type of
`05:46` an agent is just another type of
`05:46` an agent is just another type of markdown file read by the initial model
`05:49` markdown file read by the initial model
`05:49` markdown file read by the initial model and sharing that across, right? That's
`05:52` and sharing that across, right? That's
`05:52` and sharing that across, right? That's essentially all skills are. And
`05:54` essentially all skills are. And
`05:54` essentially all skills are. And sometimes they have HTML. Um, so this is
`05:57` sometimes they have HTML. Um, so this is
`05:57` sometimes they have HTML. Um, so this is like a little uh thing that they built
`05:59` like a little uh thing that they built
`05:59` like a little uh thing that they built inside of the skills so that it could
`06:00` inside of the skills so that it could
`06:00` inside of the skills so that it could add queries itself and um Claude can
`06:04` add queries itself and um Claude can
`06:04` add queries itself and um Claude can actually do a tool call inside of the
`06:06` actually do a tool call inside of the
`06:06` actually do a tool call inside of the skill to go and look at the evaluation
`06:08` skill to go and look at the evaluation
`06:08` skill to go and look at the evaluation of that skill. So it's just a very deep
`06:11` of that skill. So it's just a very deep
`06:11` of that skill. So it's just a very deep workflow. This skill creator is a
`06:13` workflow. This skill creator is a
`06:13` workflow. This skill creator is a workflow that someone did manually with
`06:15` workflow that someone did manually with
`06:16` workflow that someone did manually with the AI and created a process and
`06:19` the AI and created a process and
`06:19` the AI and created a process and organized that process into natural
`06:21` organized that process into natural
`06:21` organized that process into natural language and gave it a tool or two that
`06:23` language and gave it a tool or two that
`06:23` language and gave it a tool or two that maybe isn't uh just HTML. In this case,
`06:27` maybe isn't uh just HTML. In this case,
`06:27` maybe isn't uh just HTML. In this case, a pi, it runs this Python script every
`06:30` a pi, it runs this Python script every
`06:30` a pi, it runs this Python script every time to output something so that the AI
`06:32` time to output something so that the AI
`06:32` time to output something so that the AI doesn't have to create this script every
`06:34` doesn't have to create this script every
`06:34` doesn't have to create this script every time it's doing it. But they noticed
`06:36` time it's doing it. But they noticed
`06:36` time it's doing it. But they noticed when they were creating skill, they
`06:38` when they were creating skill, they
`06:38` when they were creating skill, they needed an HTML file. they needed a
`06:40` needed an HTML file. they needed a
`06:40` needed an HTML file. they needed a Python thing and they just put it in
`06:42` Python thing and they just put it in
`06:42` Python thing and they just put it in there so that the AI doesn't have to
`06:45` there so that the AI doesn't have to
`06:45` there so that the AI doesn't have to think about using it. It's already good.
`06:47` think about using it. It's already good.
`06:47` think about using it. It's already good. It's already where it needs to be. And
`06:48` It's already where it needs to be. And
`06:48` It's already where it needs to be. And that goes for every single skill out
`06:51` that goes for every single skill out
`06:51` that goes for every single skill out there. There's some sort of combination
`06:53` there. There's some sort of combination
`06:53` there. There's some sort of combination or process. But beneath under all of the
`06:56` or process. But beneath under all of the
`06:56` or process. But beneath under all of the skills is that ICM, that kind of folder
`07:00` skills is that ICM, that kind of folder
`07:00` skills is that ICM, that kind of folder architecture. And uh you can also
`07:02` architecture. And uh you can also
`07:02` architecture. And uh you can also download like plugins which are
`07:04` download like plugins which are
`07:04` download like plugins which are essentially skills but a little bit more
`07:06` essentially skills but a little bit more
`07:06` essentially skills but a little bit more connected. Um so if we come Whoops. come
`07:09` connected. Um so if we come Whoops. come
`07:09` connected. Um so if we come Whoops. come back to the customize thing and I'm
`07:11` back to the customize thing and I'm
`07:11` back to the customize thing and I'm going to show what this looks like
`07:12` going to show what this looks like
`07:12` going to show what this looks like behind the scenes too with VS Code. But
`07:14` behind the scenes too with VS Code. But
`07:14` behind the scenes too with VS Code. But these Oh, I'm not in cloud code. Hold
`07:16` these Oh, I'm not in cloud code. Hold
`07:16` these Oh, I'm not in cloud code. Hold on. Let's fix that. Yeah, this the other
`07:18` on. Let's fix that. Yeah, this the other
`07:18` on. Let's fix that. Yeah, this the other thing. Plugins only work for cloud code.
`07:20` thing. Plugins only work for cloud code.
`07:20` thing. Plugins only work for cloud code. So, let me go do that real quick. At
`07:22` So, let me go do that real quick. At
`07:22` So, let me go do that real quick. At least on the desktop. Oh my gosh. I
`07:25` least on the desktop. Oh my gosh. I
`07:25` least on the desktop. Oh my gosh. I cannot This is why I prefer.
`07:28` cannot This is why I prefer.
`07:28` cannot This is why I prefer. Okay, there we go. Um, you can come in
`07:31` Okay, there we go. Um, you can come in
`07:31` Okay, there we go. Um, you can come in and these plugins are also like skills
`07:34` and these plugins are also like skills
`07:34` and these plugins are also like skills but with connectors built into them. So
`07:36` but with connectors built into them. So
`07:36` but with connectors built into them. So it's that idea of okay, I've created the
`07:39` it's that idea of okay, I've created the
`07:39` it's that idea of okay, I've created the folder architecture. I've created these
`07:40` folder architecture. I've created these
`07:40` folder architecture. I've created these markdown files. Now I want to connect it
`07:43` markdown files. Now I want to connect it
`07:43` markdown files. Now I want to connect it to outside systems. Well, that's exactly
`07:46` to outside systems. Well, that's exactly
`07:46` to outside systems. Well, that's exactly what this does. When you look inside,
`07:48` what this does. When you look inside,
`07:48` what this does. When you look inside, this is a markdown file. Again, it's in
`07:50` this is a markdown file. Again, it's in
`07:50` this is a markdown file. Again, it's in full markdown. You can see it here. It's
`07:53` full markdown. You can see it here. It's
`07:53` full markdown. You can see it here. It's describing a method or a process of
`07:55` describing a method or a process of
`07:55` describing a method or a process of doing something. But inside of the
`07:57` doing something. But inside of the
`07:57` doing something. But inside of the skill, it might be a reference to
`07:59` skill, it might be a reference to
`07:59` skill, it might be a reference to something it needs to do like a
`08:01` something it needs to do like a
`08:01` something it needs to do like a connector. So here I can actually
`08:03` connector. So here I can actually
`08:03` connector. So here I can actually connect Asauna or notion or Google
`08:06` connect Asauna or notion or Google
`08:06` connect Asauna or notion or Google calendar or Figma. So if I'm designing
`08:09` calendar or Figma. So if I'm designing
`08:09` calendar or Figma. So if I'm designing something and then I need to check in
`08:11` something and then I need to check in
`08:11` something and then I need to check in with my project management tool like
`08:12` with my project management tool like
`08:12` with my project management tool like Asauna, I can just install that and
`08:15` Asauna, I can just install that and
`08:15` Asauna, I can just install that and connect my Asauna account or maybe I
`08:17` connect my Asauna account or maybe I
`08:18` connect my Asauna account or maybe I have an in notion big database and I'm
`08:20` have an in notion big database and I'm
`08:20` have an in notion big database and I'm using notion to share notes on a team. I
`08:23` using notion to share notes on a team. I
`08:23` using notion to share notes on a team. I can connect that directly still living
`08:25` can connect that directly still living
`08:25` can connect that directly still living locally with folders in here. And this
`08:27` locally with folders in here. And this
`08:27` locally with folders in here. And this is what I think is going to become
`08:29` is what I think is going to become
`08:29` is what I think is going to become easier to do. Anthropic, OpenAI, all of
`08:31` easier to do. Anthropic, OpenAI, all of
`08:31` easier to do. Anthropic, OpenAI, all of these people are going to make this
`08:33` these people are going to make this
`08:33` these people are going to make this process easier. And even when you're
`08:35` process easier. And even when you're
`08:36` process easier. And even when you're inside of VS Code, it's the same thing
`08:38` inside of VS Code, it's the same thing
`08:38` inside of VS Code, it's the same thing if instead of having the skills in your
`08:42` if instead of having the skills in your
`08:42` if instead of having the skills in your so let's take uh let's take this for
`08:44` so let's take uh let's take this for
`08:44` so let's take uh let's take this for example. This is my writing and
`08:45` example. This is my writing and
`08:46` example. This is my writing and scripting um process, one of the many
`08:49` scripting um process, one of the many
`08:49` scripting um process, one of the many that I've made. I have my cloud MD that
`08:51` that I've made. I have my cloud MD that
`08:51` that I've made. I have my cloud MD that routes to everywhere, right? But if you
`08:54` routes to everywhere, right? But if you
`08:54` routes to everywhere, right? But if you notice, there's not a skill file in
`08:55` notice, there's not a skill file in
`08:55` notice, there's not a skill file in here. Now, I could put some in here, but
`08:58` here. Now, I could put some in here, but
`08:58` here. Now, I could put some in here, but Claude Code installed on my computer
`09:00` Claude Code installed on my computer
`09:00` Claude Code installed on my computer already has skills involved, right? I
`09:03` already has skills involved, right? I
`09:04` already has skills involved, right? I did add some specific ones inside of
`09:07` did add some specific ones inside of
`09:07` did add some specific ones inside of this one, scene generation, because it
`09:09` this one, scene generation, because it
`09:09` this one, scene generation, because it needed stuff specifically and I built
`09:11` needed stuff specifically and I built
`09:12` needed stuff specifically and I built them myself. These are my own skills
`09:14` them myself. These are my own skills
`09:14` them myself. These are my own skills that I'm using for Nano Banana Pro, Seed
`09:17` that I'm using for Nano Banana Pro, Seed
`09:17` that I'm using for Nano Banana Pro, Seed Dance, a certain style that I like. Um,
`09:20` Dance, a certain style that I like. Um,
`09:20` Dance, a certain style that I like. Um, because I'm testing a I do my
`09:22` because I'm testing a I do my
`09:22` because I'm testing a I do my animations, but I'm testing where the
`09:23` animations, but I'm testing where the
`09:24` animations, but I'm testing where the animations are actually done by like
`09:25` animations are actually done by like
`09:25` animations are actually done by like Seed Dance or Cling, which are visual
`09:27` Seed Dance or Cling, which are visual
`09:27` Seed Dance or Cling, which are visual models. Um, and it's a it's a it's a
`09:30` models. Um, and it's a it's a it's a
`09:30` models. Um, and it's a it's a it's a test and process. You'll see a video on
`09:31` test and process. You'll see a video on
`09:31` test and process. You'll see a video on it here. But most of the time the skills
`09:34` it here. But most of the time the skills
`09:34` it here. But most of the time the skills I need when I just open up and I'm
`09:36` I need when I just open up and I'm
`09:36` I need when I just open up and I'm saying working most of the time those
`09:39` saying working most of the time those
`09:39` saying working most of the time those skills are already installed across
`09:41` skills are already installed across
`09:41` skills are already installed across everything right and there's also a
`09:43` everything right and there's also a
`09:43` everything right and there's also a skill to find skills right so if I can
`09:46` skill to find skills right so if I can
`09:46` skill to find skills right so if I can say hey let me use a skill to find
`09:48` say hey let me use a skill to find
`09:48` say hey let me use a skill to find skills that skill is not in my folder
`09:50` skills that skill is not in my folder
`09:50` skills that skill is not in my folder structure here it's actually installed
`09:52` structure here it's actually installed
`09:52` structure here it's actually installed directly inside of claude on my computer
`09:55` directly inside of claude on my computer
`09:55` directly inside of claude on my computer right so if you go and find um the
`09:58` right so if you go and find um the
`09:58` right so if you go and find um the enthropic folder where uh claude is
`10:00` enthropic folder where uh claude is
`10:00` enthropic folder where uh claude is installed which you can see Here they
`10:03` installed which you can see Here they
`10:03` installed which you can see Here they actually have their own local skills. So
`10:05` actually have their own local skills. So
`10:05` actually have their own local skills. So this is across all the projects. Anytime
`10:07` this is across all the projects. Anytime
`10:07` this is across all the projects. Anytime I open up claude, these skills are all
`10:11` I open up claude, these skills are all
`10:11` I open up claude, these skills are all available. And if we look at the where's
`10:13` available. And if we look at the where's
`10:13` available. And if we look at the where's this find skill? Find skills skill,
`10:15` this find skill? Find skills skill,
`10:15` this find skill? Find skills skill, right? It's just a markdown file on how
`10:17` right? It's just a markdown file on how
`10:17` right? It's just a markdown file on how to find skills, right? Hey, find skills
`10:20` to find skills, right? Hey, find skills
`10:20` to find skills, right? Hey, find skills helps users discover and install skills
`10:22` helps users discover and install skills
`10:22` helps users discover and install skills when they ask questions like this or
`10:24` when they ask questions like this or
`10:24` when they ask questions like this or this. And then it goes through and it
`10:26` this. And then it goes through and it
`10:26` this. And then it goes through and it has a link inside of it already as if
`10:29` has a link inside of it already as if
`10:29` has a link inside of it already as if you're copying and pasting this to go
`10:30` you're copying and pasting this to go
`10:30` you're copying and pasting this to go and find that skill which it goes to
`10:32` and find that skill which it goes to
`10:32` and find that skill which it goes to this website which is a really great
`10:34` this website which is a really great
`10:34` this website which is a really great website if none of you are aware of it
`10:36` website if none of you are aware of it
`10:36` website if none of you are aware of it skills.sh SH again as I mentioned last
`10:39` skills.sh SH again as I mentioned last
`10:39` skills.sh SH again as I mentioned last week be very aware of prompt injection
`10:43` week be very aware of prompt injection
`10:43` week be very aware of prompt injection because as all of these things are
`10:45` because as all of these things are
`10:46` because as all of these things are markdown files and prompts someone could
`10:48` markdown files and prompts someone could
`10:48` markdown files and prompts someone could be malicious and hide you know if let's
`10:51` be malicious and hide you know if let's
`10:51` be malicious and hide you know if let's let's look at a really intense uh and
`10:53` let's look at a really intense uh and
`10:53` let's look at a really intense uh and deep skill here um which one has a lot I
`10:56` deep skill here um which one has a lot I
`10:56` deep skill here um which one has a lot I think yeah so this one has a bunch right
`11:00` think yeah so this one has a bunch right
`11:00` think yeah so this one has a bunch right they could have a prompt that's inside
`11:02` they could have a prompt that's inside
`11:02` they could have a prompt that's inside of the Python code that injects into
`11:05` of the Python code that injects into
`11:05` of the Python code that injects into your cloud session and tells it to
`11:07` your cloud session and tells it to
`11:07` your cloud session and tells it to navigate to a website and then maybe
`11:10` navigate to a website and then maybe
`11:10` navigate to a website and then maybe upload some sort of work that you're
`11:12` upload some sort of work that you're
`11:12` upload some sort of work that you're working on or share av file. Same thing
`11:15` working on or share av file. Same thing
`11:15` working on or share av file. Same thing in here. These are markdown files, but
`11:17` in here. These are markdown files, but
`11:17` in here. These are markdown files, but they could have code or a prompt
`11:20` they could have code or a prompt
`11:20` they could have code or a prompt injection hidden somewhere in here and
`11:22` injection hidden somewhere in here and
`11:22` injection hidden somewhere in here and it might not notice it. It's just going
`11:24` it might not notice it. It's just going
`11:24` it might not notice it. It's just going to know, oh, these are my instructions.
`11:25` to know, oh, these are my instructions.
`11:25` to know, oh, these are my instructions. I'm going to run these instructions. And
`11:28` I'm going to run these instructions. And
`11:28` I'm going to run these instructions. And that's something you want to be very
`11:29` that's something you want to be very
`11:29` that's something you want to be very careful and aware of. However, these
`11:31` careful and aware of. However, these
`11:31` careful and aware of. However, these kind of open agent skill systems, people
`11:33` kind of open agent skill systems, people
`11:34` kind of open agent skill systems, people are usually monitoring it and going
`11:35` are usually monitoring it and going
`11:35` are usually monitoring it and going through it. Um, but there's some amazing
`11:38` through it. Um, but there's some amazing
`11:38` through it. Um, but there's some amazing skills on this website. Let me actually
`11:39` skills on this website. Let me actually
`11:40` skills on this website. Let me actually throw it into chat for you all. Um,
`11:44` throw it into chat for you all. Um,
`11:44` throw it into chat for you all. Um, yes. And Erin, I know I me and you, we
`11:46` yes. And Erin, I know I me and you, we
`11:46` yes. And Erin, I know I me and you, we need to get together. Erin has been huge
`11:48` need to get together. Erin has been huge
`11:48` need to get together. Erin has been huge for me um in a lot of these, but am I
`11:50` for me um in a lot of these, but am I
`11:50` for me um in a lot of these, but am I moving too fast for anyone by the way?
`11:53` moving too fast for anyone by the way?
`11:53` moving too fast for anyone by the way? Is this all making sense? if you could
`11:55` Is this all making sense? if you could
`11:55` Is this all making sense? if you could throw into chat whether or not I'm
`11:56` throw into chat whether or not I'm
`11:56` throw into chat whether or not I'm moving too fast or um oh it's good. I
`12:00` moving too fast or um oh it's good. I
`12:00` moving too fast or um oh it's good. I thought you said yes I am moving too
`12:01` thought you said yes I am moving too
`12:02` thought you said yes I am moving too fast.
`12:02` fast.
`12:02` fast. Carlos is like, "Yes, Carlos, I this is
`12:05` Carlos is like, "Yes, Carlos, I this is
`12:05` Carlos is like, "Yes, Carlos, I this is actually a lot of this is in response to
`12:06` actually a lot of this is in response to
`12:06` actually a lot of this is in response to what you asked in Discord." And this is
`12:08` what you asked in Discord." And this is
`12:08` what you asked in Discord." And this is the whole point of of kind of premium
`12:10` the whole point of of kind of premium
`12:10` the whole point of of kind of premium like obviously I'm sharing I'm going to
`12:12` like obviously I'm sharing I'm going to
`12:12` like obviously I'm sharing I'm going to share a lot of these markdown files
`12:14` share a lot of these markdown files
`12:14` share a lot of these markdown files constantly uploading our my the vault
`12:17` constantly uploading our my the vault
`12:17` constantly uploading our my the vault with these things so you have them, but
`12:19` with these things so you have them, but
`12:19` with these things so you have them, but I think it's more valuable for you to
`12:21` I think it's more valuable for you to
`12:21` I think it's more valuable for you to ask specific questions. And my time is
`12:23` ask specific questions. And my time is
`12:23` ask specific questions. And my time is extremely limited. Um, but this is
`12:26` extremely limited. Um, but this is
`12:26` extremely limited. Um, but this is what's not scalable is these kind of
`12:27` what's not scalable is these kind of
`12:28` what's not scalable is these kind of back and forth. So, uh, Carlos, is this
`12:30` back and forth. So, uh, Carlos, is this
`12:30` back and forth. So, uh, Carlos, is this mostly answering some of the questions
`12:31` mostly answering some of the questions
`12:31` mostly answering some of the questions you had in a lot of ways? Uh, I'll let
`12:33` you had in a lot of ways? Uh, I'll let
`12:34` you had in a lot of ways? Uh, I'll let you share what you're working on here
`12:35` you share what you're working on here
`12:35` you share what you're working on here shortly as well. Um, but I just wanted
`12:37` shortly as well. Um, but I just wanted
`12:37` shortly as well. Um, but I just wanted to make sure we're on point. Let's see.
`12:39` to make sure we're on point. Let's see.
`12:39` to make sure we're on point. Let's see. Janette, curious to know what all
`12:42` Janette, curious to know what all
`12:42` Janette, curious to know what all uh your workspaces are. I currently just
`12:44` uh your workspaces are. I currently just
`12:44` uh your workspaces are. I currently just work in one master where I do all of my
`12:46` work in one master where I do all of my
`12:46` work in one master where I do all of my work and some personal stuff, too.
`12:48` work and some personal stuff, too.
`12:48` work and some personal stuff, too. Curious how better to think about
`12:49` Curious how better to think about
`12:50` Curious how better to think about multiple workspaces. So, there's there's
`12:51` multiple workspaces. So, there's there's
`12:51` multiple workspaces. So, there's there's there's actually some divided opinions
`12:53` there's actually some divided opinions
`12:53` there's actually some divided opinions on this. Um, one of my favorite opinions
`12:56` on this. Um, one of my favorite opinions
`12:56` on this. Um, one of my favorite opinions is actually from Andre Cap Kaparthy. Um,
`13:00` is actually from Andre Cap Kaparthy. Um,
`13:00` is actually from Andre Cap Kaparthy. Um, and his wiki, his a AI wiki. Um, yes,
`13:03` and his wiki, his a AI wiki. Um, yes,
`13:03` and his wiki, his a AI wiki. Um, yes, right here, this one. And I'm actually
`13:05` right here, this one. And I'm actually
`13:05` right here, this one. And I'm actually making a video on this as well because
`13:06` making a video on this as well because
`13:06` making a video on this as well because it's very good, but his idea is that you
`13:09` it's very good, but his idea is that you
`13:09` it's very good, but his idea is that you create a kind of self-learning
`13:11` create a kind of self-learning
`13:11` create a kind of self-learning environment where um, let's see, does he
`13:14` environment where um, let's see, does he
`13:14` environment where um, let's see, does he have an image of it? Um, I'd rather show
`13:16` have an image of it? Um, I'd rather show
`13:16` have an image of it? Um, I'd rather show this visually um because it's much
`13:18` this visually um because it's much
`13:18` this visually um because it's much better. But the idea there is imagine
`13:20` better. But the idea there is imagine
`13:20` better. But the idea there is imagine you're sitting there and Oh, no. No, no,
`13:23` you're sitting there and Oh, no. No, no,
`13:24` you're sitting there and Oh, no. No, no, no, no, no. By the way, this is one of
`13:25` no, no, no. By the way, this is one of
`13:25` no, no, no. By the way, this is one of the founders of OpenAI, but um he
`13:28` the founders of OpenAI, but um he
`13:28` the founders of OpenAI, but um he basically had this idea of if you have
`13:30` basically had this idea of if you have
`13:30` basically had this idea of if you have all these workspaces, there's things you
`13:32` all these workspaces, there's things you
`13:32` all these workspaces, there's things you can pull from it and create memories on
`13:33` can pull from it and create memories on
`13:34` can pull from it and create memories on it and basically give your AI a brain of
`13:37` it and basically give your AI a brain of
`13:37` it and basically give your AI a brain of where the workspaces are, what the
`13:39` where the workspaces are, what the
`13:39` where the workspaces are, what the workspaces are, being able to search
`13:41` workspaces are, being able to search
`13:41` workspaces are, being able to search them. So, the organization doesn't
`13:43` them. So, the organization doesn't
`13:43` them. So, the organization doesn't matter as much as allowing them to kind
`13:45` matter as much as allowing them to kind
`13:45` matter as much as allowing them to kind of go in there. Um, and then another
`13:48` of go in there. Um, and then another
`13:48` of go in there. Um, and then another good one, yeah, David, that's actually
`13:50` good one, yeah, David, that's actually
`13:50` good one, yeah, David, that's actually another great marketplace um, for skills
`13:52` another great marketplace um, for skills
`13:52` another great marketplace um, for skills is Lowhub. Um, there's a lot of
`13:54` is Lowhub. Um, there's a lot of
`13:54` is Lowhub. Um, there's a lot of different curated collections,
`13:55` different curated collections,
`13:56` different curated collections, especially for Obsidian skills. And
`13:57` especially for Obsidian skills. And
`13:57` especially for Obsidian skills. And Obsidian is actually one of the main
`14:00` Obsidian is actually one of the main
`14:00` Obsidian is actually one of the main things that Andrew Kaparthy is using to
`14:03` things that Andrew Kaparthy is using to
`14:03` things that Andrew Kaparthy is using to organize uh, a lot of his models
`14:06` organize uh, a lot of his models
`14:06` organize uh, a lot of his models knowledge um, or it's one of the
`14:08` knowledge um, or it's one of the
`14:08` knowledge um, or it's one of the references and other ways people are
`14:09` references and other ways people are
`14:09` references and other ways people are doing it. However, the other thing is
`14:12` doing it. However, the other thing is
`14:12` doing it. However, the other thing is just very informal structure. So for me,
`14:15` just very informal structure. So for me,
`14:15` just very informal structure. So for me, I just put everything on my desktop,
`14:17` I just put everything on my desktop,
`14:17` I just put everything on my desktop, right? These are all workspaces for me
`14:19` right? These are all workspaces for me
`14:19` right? These are all workspaces for me and they're just right there on my
`14:21` and they're just right there on my
`14:21` and they're just right there on my desktop. When I'm done working with it,
`14:23` desktop. When I'm done working with it,
`14:23` desktop. When I'm done working with it, I can toss it into a folder of past work
`14:26` I can toss it into a folder of past work
`14:26` I can toss it into a folder of past work and then it's all there. But they're
`14:27` and then it's all there. But they're
`14:27` and then it's all there. But they're also not technically in the same folder.
`14:29` also not technically in the same folder.
`14:29` also not technically in the same folder. They're kind of separate and I can just
`14:30` They're kind of separate and I can just
`14:30` They're kind of separate and I can just come in, log in, and and call it a day.
`14:33` come in, log in, and and call it a day.
`14:33` come in, log in, and and call it a day. Another option is to hide all of these
`14:36` Another option is to hide all of these
`14:36` Another option is to hide all of these on something cloud-based. So if you have
`14:38` on something cloud-based. So if you have
`14:38` on something cloud-based. So if you have a one drive and you could do this
`14:40` a one drive and you could do this
`14:40` a one drive and you could do this methodology with co-pilot, you could put
`14:43` methodology with co-pilot, you could put
`14:43` methodology with co-pilot, you could put all of your workspaces into one drive.
`14:45` all of your workspaces into one drive.
`14:45` all of your workspaces into one drive. I've seen people do it inside of notion.
`14:47` I've seen people do it inside of notion.
`14:48` I've seen people do it inside of notion. Um it it really comes down to again your
`14:51` Um it it really comes down to again your
`14:51` Um it it really comes down to again your personal preference. Where where do you
`14:54` personal preference. Where where do you
`14:54` personal preference. Where where do you want to keep your information? What is
`14:57` want to keep your information? What is
`14:57` want to keep your information? What is simple for you? Um is in one drive. So I
`15:00` simple for you? Um is in one drive. So I
`15:00` simple for you? Um is in one drive. So I moved it to the root as I was concerned
`15:01` moved it to the root as I was concerned
`15:01` moved it to the root as I was concerned about files with credentials backing up
`15:04` about files with credentials backing up
`15:04` about files with credentials backing up to one drive. Okay, this is a very great
`15:06` to one drive. Okay, this is a very great
`15:06` to one drive. Okay, this is a very great thing. Um there is something and that's
`15:09` thing. Um there is something and that's
`15:09` thing. Um there is something and that's actually the final place which I see
`15:11` actually the final place which I see
`15:11` actually the final place which I see which is people are actually using
`15:13` which is people are actually using
`15:13` which is people are actually using GitHub a lot more because GitHub is
`15:16` GitHub a lot more because GitHub is
`15:16` GitHub a lot more because GitHub is already designed to help you navigate
`15:18` already designed to help you navigate
`15:18` already designed to help you navigate file structure. So well and when I
`15:20` file structure. So well and when I
`15:20` file structure. So well and when I upload maybe a workspace like I have a
`15:23` upload maybe a workspace like I have a
`15:23` upload maybe a workspace like I have a whole bunch of repos out there and I'm
`15:25` whole bunch of repos out there and I'm
`15:25` whole bunch of repos out there and I'm shared repos where I'm working on Adoba
`15:27` shared repos where I'm working on Adoba
`15:27` shared repos where I'm working on Adoba stuff with my company right we can add
`15:29` stuff with my company right we can add
`15:30` stuff with my company right we can add something called a git ignore and what
`15:32` something called a git ignore and what
`15:32` something called a git ignore and what this is is a markdown file or in many
`15:34` this is is a markdown file or in many
`15:34` this is is a markdown file or in many cases it's actually its own file a git
`15:37` cases it's actually its own file a git
`15:37` cases it's actually its own file a git ignore git ignore um and it basically
`15:39` ignore git ignore um and it basically
`15:39` ignore git ignore um and it basically says hey ignore these type of files um
`15:41` says hey ignore these type of files um
`15:42` says hey ignore these type of files um and one of them can be aenv so anytime
`15:45` and one of them can be aenv so anytime
`15:45` and one of them can be aenv so anytime you're uploading or sending stuff to a
`15:47` you're uploading or sending stuff to a
`15:47` you're uploading or sending stuff to a shared workspace certain certain files
`15:49` shared workspace certain certain files
`15:49` shared workspace certain certain files can be said, hey, don't upload those.
`15:52` can be said, hey, don't upload those.
`15:52` can be said, hey, don't upload those. Um, you could do a kind of fake git
`15:56` Um, you could do a kind of fake git
`15:56` Um, you could do a kind of fake git ignore inside of like a markdown file.
`15:59` ignore inside of like a markdown file.
`15:59` ignore inside of like a markdown file. So, let's say we're let's go back to our
`16:00` So, let's say we're let's go back to our
`16:00` So, let's say we're let's go back to our simple one here. Let's say I wanted to
`16:03` simple one here. Let's say I wanted to
`16:03` simple one here. Let's say I wanted to go in and I wanted to create a new file.
`16:05` go in and I wanted to create a new file.
`16:05` go in and I wanted to create a new file. Um, ignore these MD. Um, this won't
`16:10` Um, ignore these MD. Um, this won't
`16:10` Um, ignore these MD. Um, this won't always work, right? This is this is
`16:12` always work, right? This is this is
`16:12` always work, right? This is this is where AI becomes kind of a problem. But
`16:14` where AI becomes kind of a problem. But
`16:14` where AI becomes kind of a problem. But you could say you could literally
`16:16` you could say you could literally
`16:16` you could say you could literally describe these are the types of oops
`16:20` describe these are the types of oops
`16:20` describe these are the types of oops types
`16:23` types
`16:23` types of oh my gosh I cannot type today. types
`16:25` of oh my gosh I cannot type today. types
`16:25` of oh my gosh I cannot type today. types of files I want you to ignore. And then
`16:29` of files I want you to ignore. And then
`16:29` of files I want you to ignore. And then you could describe them, share them,
`16:31` you could describe them, share them,
`16:31` you could describe them, share them, even link them. And you would just need
`16:33` even link them. And you would just need
`16:33` even link them. And you would just need to make sure that in your claw.md right
`16:35` to make sure that in your claw.md right
`16:35` to make sure that in your claw.md right at the top you have a ensure to always
`16:39` at the top you have a ensure to always
`16:39` at the top you have a ensure to always check um ignore
`16:42` check um ignore
`16:42` check um ignore MD. Right? This is the most broken down
`16:45` MD. Right? This is the most broken down
`16:45` MD. Right? This is the most broken down simple version
`16:47` simple version
`16:47` simple version of what you know a git ignore does.
`16:50` of what you know a git ignore does.
`16:50` of what you know a git ignore does. Problem is it's much less programmatic.
`16:52` Problem is it's much less programmatic.
`16:52` Problem is it's much less programmatic. you're relying on whatever model you're
`16:54` you're relying on whatever model you're
`16:54` you're relying on whatever model you're using to read that and then read this
`16:56` using to read that and then read this
`16:56` using to read that and then read this and then verify before you're pushing or
`16:59` and then verify before you're pushing or
`16:59` and then verify before you're pushing or it's reading those things which is
`17:01` it's reading those things which is
`17:01` it's reading those things which is another part of it. The other thing
`17:04` another part of it. The other thing
`17:04` another part of it. The other thing which actually Toby this is a really
`17:05` which actually Toby this is a really
`17:06` which actually Toby this is a really great point is just keeping it on a
`17:08` great point is just keeping it on a
`17:08` great point is just keeping it on a separate drive or a virtual machine.
`17:10` separate drive or a virtual machine.
`17:10` separate drive or a virtual machine. There's a lot of YouTube videos out
`17:12` There's a lot of YouTube videos out
`17:12` There's a lot of YouTube videos out there. Again, I find that simplicity is
`17:15` there. Again, I find that simplicity is
`17:15` there. Again, I find that simplicity is king for me. If I'm working on a project
`17:18` king for me. If I'm working on a project
`17:18` king for me. If I'm working on a project and I don't need to upload anything, I
`17:20` and I don't need to upload anything, I
`17:20` and I don't need to upload anything, I won't upload it. when I do need to
`17:22` won't upload it. when I do need to
`17:22` won't upload it. when I do need to upload something, I usually upload it to
`17:24` upload something, I usually upload it to
`17:24` upload something, I usually upload it to GitHub and then share it with my team
`17:26` GitHub and then share it with my team
`17:26` GitHub and then share it with my team because then I can just use a git ignore
`17:28` because then I can just use a git ignore
`17:28` because then I can just use a git ignore file. Um, I hope that kind of answers
`17:31` file. Um, I hope that kind of answers
`17:31` file. Um, I hope that kind of answers some of your questions. Uh, Windows
`17:33` some of your questions. Uh, Windows
`17:33` some of your questions. Uh, Windows Credential Manager is a really good one
`17:35` Credential Manager is a really good one
`17:35` Credential Manager is a really good one as well. Um, because you can flag
`17:37` as well. Um, because you can flag
`17:37` as well. Um, because you can flag certain files or or even folders from
`17:39` certain files or or even folders from
`17:39` certain files or or even folders from having access. Um, even in your one
`17:41` having access. Um, even in your one
`17:41` having access. Um, even in your one drive itself, let's say you do upload an
`17:44` drive itself, let's say you do upload an
`17:44` drive itself, let's say you do upload an ENV file, that's okay as long as that
`17:47` ENV file, that's okay as long as that
`17:47` ENV file, that's okay as long as that one drive is secure and people don't
`17:50` one drive is secure and people don't
`17:50` one drive is secure and people don't have access to it. It's password
`17:51` have access to it. It's password
`17:51` have access to it. It's password protected. You actually have a pretty
`17:53` protected. You actually have a pretty
`17:53` protected. You actually have a pretty good bit of security with one drive. It
`17:55` good bit of security with one drive. It
`17:55` good bit of security with one drive. It doesn't mean it's perfect, but Microsoft
`17:58` doesn't mean it's perfect, but Microsoft
`17:58` doesn't mean it's perfect, but Microsoft does have a history of being, you know,
`18:00` does have a history of being, you know,
`18:00` does have a history of being, you know, with the US government. It's why they
`18:01` with the US government. It's why they
`18:02` with the US government. It's why they get kind of well, one vendor lock in.
`18:04` get kind of well, one vendor lock in.
`18:04` get kind of well, one vendor lock in. That's another big part of it, but they
`18:06` That's another big part of it, but they
`18:06` That's another big part of it, but they do have pretty decent security with a
`18:08` do have pretty decent security with a
`18:08` do have pretty decent security with a lot of things they do. Um, so that's
`18:10` lot of things they do. Um, so that's
`18:10` lot of things they do. Um, so that's that's another side of it as well. Um,
`18:12` that's another side of it as well. Um,
`18:12` that's another side of it as well. Um, OpenBrain Project. Yes. Yeah. No, Nest
`18:15` OpenBrain Project. Yes. Yeah. No, Nest
`18:15` OpenBrain Project. Yes. Yeah. No, Nest Openrain Project is really cool. Let me
`18:17` Openrain Project is really cool. Let me
`18:17` Openrain Project is really cool. Let me actually pull that up here. Um, I've
`18:19` actually pull that up here. Um, I've
`18:19` actually pull that up here. Um, I've messed around with that a lot. Again, I
`18:20` messed around with that a lot. Again, I
`18:20` messed around with that a lot. Again, I always break down to the fundamentals
`18:21` always break down to the fundamentals
`18:22` always break down to the fundamentals and I end up rebuilding stuff myself.
`18:24` and I end up rebuilding stuff myself.
`18:24` and I end up rebuilding stuff myself. Um, but let me see if I can find uh
`18:28` Um, but let me see if I can find uh
`18:28` Um, but let me see if I can find uh yeah, with Oh, that's because I I want
`18:30` yeah, with Oh, that's because I I want
`18:30` yeah, with Oh, that's because I I want to also I would love So, Nate B. Jones
`18:33` to also I would love So, Nate B. Jones
`18:33` to also I would love So, Nate B. Jones is one of my favorite YouTubers. I don't
`18:35` is one of my favorite YouTubers. I don't
`18:35` is one of my favorite YouTubers. I don't know if any of you know him. Other
`18:37` know if any of you know him. Other
`18:37` know if any of you know him. Other obviously, my favorite YouTuber should
`18:38` obviously, my favorite YouTuber should
`18:38` obviously, my favorite YouTuber should be myself, but Nate B. Jones is someone
`18:41` be myself, but Nate B. Jones is someone
`18:41` be myself, but Nate B. Jones is someone I've watched for a while and kind of
`18:43` I've watched for a while and kind of
`18:43` I've watched for a while and kind of dove in. And one of the things that he
`18:45` dove in. And one of the things that he
`18:45` dove in. And one of the things that he looks at is this kind of idea of a uh
`18:48` looks at is this kind of idea of a uh
`18:48` looks at is this kind of idea of a uh open brain project. Oh, this is my
`18:49` open brain project. Oh, this is my
`18:50` open brain project. Oh, this is my notion. Um of this open brain project.
`18:53` notion. Um of this open brain project.
`18:53` notion. Um of this open brain project. This idea of like hey we have these
`18:55` This idea of like hey we have these
`18:55` This idea of like hey we have these workflows, we have these processors,
`18:58` workflows, we have these processors,
`18:58` workflows, we have these processors, there's infrastructure layers for
`19:00` there's infrastructure layers for
`19:00` there's infrastructure layers for thinking. He it's using the same concept
`19:02` thinking. He it's using the same concept
`19:02` thinking. He it's using the same concept that I'm teaching you here. And that's
`19:04` that I'm teaching you here. And that's
`19:04` that I'm teaching you here. And that's why I'm always saying like be careful
`19:06` why I'm always saying like be careful
`19:06` why I'm always saying like be careful how concrete you take from me. Yes, my
`19:09` how concrete you take from me. Yes, my
`19:09` how concrete you take from me. Yes, my stuff is great. It is a great
`19:11` stuff is great. It is a great
`19:11` stuff is great. It is a great fundamental, right? this this paper this
`19:13` fundamental, right? this this paper this
`19:13` fundamental, right? this this paper this GitHub wait interpretive
`19:17` GitHub wait interpretive
`19:17` GitHub wait interpretive interpreted
`19:19` interpreted
`19:19` interpreted context methodology we need to find the
`19:21` context methodology we need to find the
`19:21` context methodology we need to find the paper um oh what does Gemini have to say
`19:24` paper um oh what does Gemini have to say
`19:24` paper um oh what does Gemini have to say about me interpret is a fuller
`19:26` about me interpret is a fuller
`19:26` about me interpret is a fuller architecture man it organizes work in
`19:28` architecture man it organizes work in
`19:28` architecture man it organizes work in spaces yet developed by Jake Van Clee in
`19:30` spaces yet developed by Jake Van Clee in
`19:30` spaces yet developed by Jake Van Clee in there I see him uses three that's okay
`19:32` there I see him uses three that's okay
`19:32` there I see him uses three that's okay that's not dec that's not bad I like
`19:34` that's not dec that's not bad I like
`19:34` that's not dec that's not bad I like that look at that Gemini talking about
`19:35` that look at that Gemini talking about
`19:35` that look at that Gemini talking about me anyway um this paper is useful and is
`19:39` me anyway um this paper is useful and is
`19:39` me anyway um this paper is useful and is great to give you an idea of the
`19:40` great to give you an idea of the
`19:40` great to give you an idea of the thinking behind all of this, but it
`19:42` thinking behind all of this, but it
`19:42` thinking behind all of this, but it doesn't mean this is the only way to do
`19:44` doesn't mean this is the only way to do
`19:44` doesn't mean this is the only way to do this. There is going to be a multiple
`19:47` this. There is going to be a multiple
`19:47` this. There is going to be a multiple ways and whichever one clicks with you
`19:49` ways and whichever one clicks with you
`19:49` ways and whichever one clicks with you the fastest. That's the best way.
`19:51` the fastest. That's the best way.
`19:51` the fastest. That's the best way. Something that you can understand faster
`19:53` Something that you can understand faster
`19:53` Something that you can understand faster and better is always going to be the
`19:56` and better is always going to be the
`19:56` and better is always going to be the most useful to you. Even if there's a
`19:58` most useful to you. Even if there's a
`19:58` most useful to you. Even if there's a more efficient one hiding on GitHub
`20:00` more efficient one hiding on GitHub
`20:00` more efficient one hiding on GitHub somewhere, right? I find that engineers
`20:02` somewhere, right? I find that engineers
`20:02` somewhere, right? I find that engineers take so much time trying to find the
`20:04` take so much time trying to find the
`20:04` take so much time trying to find the perfect most efficient solution when in
`20:07` perfect most efficient solution when in
`20:07` perfect most efficient solution when in actuality the solution that works the
`20:09` actuality the solution that works the
`20:09` actuality the solution that works the best is the one that most people can use
`20:11` best is the one that most people can use
`20:11` best is the one that most people can use as quickly as possible especially in
`20:13` as quickly as possible especially in
`20:13` as quickly as possible especially in consumer culture. Um so on that you want
`20:15` consumer culture. Um so on that you want
`20:15` consumer culture. Um so on that you want to search OB1
`20:17` to search OB1
`20:17` to search OB1 um on Git Oh yeah. No, that's that's a
`20:19` um on Git Oh yeah. No, that's that's a
`20:19` um on Git Oh yeah. No, that's that's a good spot to look as well. U
`20:28` get open rank. Let's see if it actually
`20:28` get open rank. Let's see if it actually pulls it up for everyone. Um, yeah, same
`20:30` pulls it up for everyone. Um, yeah, same
`20:30` pulls it up for everyone. Um, yeah, same exact thing there. Let me actually toss
`20:32` exact thing there. Let me actually toss
`20:32` exact thing there. Let me actually toss that in
`20:35` that in
`20:35` that in here. That one. And then this one is a
`20:38` here. That one. And then this one is a
`20:38` here. That one. And then this one is a different type of project. Actually, it
`20:40` different type of project. Actually, it
`20:40` different type of project. Actually, it should be the same. Is this not the
`20:41` should be the same. Is this not the
`20:41` should be the same. Is this not the same? No, this is the same. Yes, I was
`20:43` same? No, this is the same. Yes, I was
`20:43` same? No, this is the same. Yes, I was correct. Um, so yeah, Open Brain's a
`20:45` correct. Um, so yeah, Open Brain's a
`20:46` correct. Um, so yeah, Open Brain's a really cool project. Uh, hopefully I can
`20:47` really cool project. Uh, hopefully I can
`20:47` really cool project. Uh, hopefully I can do a collab with him. I need to reach
`20:49` do a collab with him. I need to reach
`20:49` do a collab with him. I need to reach out to him. Um, I don't think he would
`20:51` out to him. Um, I don't think he would
`20:51` out to him. Um, I don't think he would have any problem with it. I just haven't
`20:53` have any problem with it. I just haven't
`20:53` have any problem with it. I just haven't spent the time. Um, he also has massive
`20:55` spent the time. Um, he also has massive
`20:56` spent the time. Um, he also has massive amount of subscribers and stuff, so I'm
`20:57` amount of subscribers and stuff, so I'm
`20:57` amount of subscribers and stuff, so I'm sure he's super busy. But really
`20:59` sure he's super busy. But really
`20:59` sure he's super busy. But really recommend this guy. Um, anyway, that was
`21:02` recommend this guy. Um, anyway, that was
`21:02` recommend this guy. Um, anyway, that was a lot of information all at once, so I
`21:04` a lot of information all at once, so I
`21:04` a lot of information all at once, so I hope you uh you got it there. But yeah,
`21:06` hope you uh you got it there. But yeah,
`21:06` hope you uh you got it there. But yeah, that at the end of the day, skills,
`21:08` that at the end of the day, skills,
`21:08` that at the end of the day, skills, going all the way back to the beginning,
`21:10` going all the way back to the beginning,
`21:10` going all the way back to the beginning, skills are my folder structure, but for
`21:13` skills are my folder structure, but for
`21:13` skills are my folder structure, but for smaller workflows or parts of workflows.
`21:15` smaller workflows or parts of workflows.
`21:15` smaller workflows or parts of workflows. And that's the idea, right? Eventually,
`21:18` And that's the idea, right? Eventually,
`21:18` And that's the idea, right? Eventually, that workflow that you've created out of
`21:20` that workflow that you've created out of
`21:20` that workflow that you've created out of folders can be condensed into a skill.
`21:23` folders can be condensed into a skill.
`21:23` folders can be condensed into a skill. It depends how much you want a human in
`21:26` It depends how much you want a human in
`21:26` It depends how much you want a human in the loop though because for me I
`21:29` the loop though because for me I
`21:29` the loop though because for me I actually don't always download skills. I
`21:31` actually don't always download skills. I
`21:31` actually don't always download skills. I often just look at what other skills
`21:33` often just look at what other skills
`21:33` often just look at what other skills people have made and then make my own,
`21:36` people have made and then make my own,
`21:36` people have made and then make my own, right? Like there's skills out there for
`21:39` right? Like there's skills out there for
`21:39` right? Like there's skills out there for these models, for these processes, but I
`21:41` these models, for these processes, but I
`21:41` these models, for these processes, but I wanted one specifically for what my
`21:44` wanted one specifically for what my
`21:44` wanted one specifically for what my process was. And that's why I teach this
`21:46` process was. And that's why I teach this
`21:46` process was. And that's why I teach this process because nine times out of 10,
`21:48` process because nine times out of 10,
`21:48` process because nine times out of 10, your thinking, your opinion, and I
`21:51` your thinking, your opinion, and I
`21:51` your thinking, your opinion, and I actually made a slide for this because I
`21:53` actually made a slide for this because I
`21:53` actually made a slide for this because I knew I was going to get here. Um, ends
`21:55` knew I was going to get here. Um, ends
`21:55` knew I was going to get here. Um, ends up beating the downloads half the time,
`21:58` up beating the downloads half the time,
`21:58` up beating the downloads half the time, right? You yourself can really learn
`22:01` right? You yourself can really learn
`22:01` right? You yourself can really learn from the patterns of those skills and
`22:03` from the patterns of those skills and
`22:03` from the patterns of those skills and then write your own to match your work,
`22:06` then write your own to match your work,
`22:06` then write your own to match your work, pull from those skills. And that's
`22:07` pull from those skills. And that's
`22:08` pull from those skills. And that's that's software development in a
`22:09` that's software development in a
`22:09` that's software development in a nutshell. Before AI, I don't know how
`22:11` nutshell. Before AI, I don't know how
`22:11` nutshell. Before AI, I don't know how many of you were software developers
`22:12` many of you were software developers
`22:12` many of you were software developers before AI, but Stack Overflow was
`22:15` before AI, but Stack Overflow was
`22:15` before AI, but Stack Overflow was basically people finding scripts, Python
`22:17` basically people finding scripts, Python
`22:17` basically people finding scripts, Python scripts, C scripts, HTML, asking people
`22:21` scripts, C scripts, HTML, asking people
`22:21` scripts, C scripts, HTML, asking people question, hey, what have you built? We
`22:23` question, hey, what have you built? We
`22:23` question, hey, what have you built? We would take someone else's codebase, rip
`22:25` would take someone else's codebase, rip
`22:25` would take someone else's codebase, rip out what we don't need, put in what we
`22:27` out what we don't need, put in what we
`22:27` out what we don't need, put in what we wanted, and integrate it into our own
`22:29` wanted, and integrate it into our own
`22:29` wanted, and integrate it into our own codebase. That that's software
`22:30` codebase. That that's software
`22:30` codebase. That that's software engineering most of the time. Very
`22:33` engineering most of the time. Very
`22:33` engineering most of the time. Very rarely are people building every single
`22:35` rarely are people building every single
`22:35` rarely are people building every single part of the software. Um, but let's see.
`22:39` part of the software. Um, but let's see.
`22:39` part of the software. Um, but let's see. uh
`22:41` uh
`22:41` uh in regards to skill. Oh, wait. No,
`22:42` in regards to skill. Oh, wait. No,
`22:42` in regards to skill. Oh, wait. No, everyone's on comments on Nate video.
`22:44` everyone's on comments on Nate video.
`22:44` everyone's on comments on Nate video. Oh, yeah, dude. That's great. And
`22:46` Oh, yeah, dude. That's great. And
`22:46` Oh, yeah, dude. That's great. And everyone go comment on his like, "Hey,
`22:47` everyone go comment on his like, "Hey,
`22:47` everyone go comment on his like, "Hey, you gotta work with this guy." I haven't
`22:49` you gotta work with this guy." I haven't
`22:49` you gotta work with this guy." I haven't even messaged him yet, so let me message
`22:50` even messaged him yet, so let me message
`22:50` even messaged him yet, so let me message him. But go ahead and do that. In
`22:52` him. But go ahead and do that. In
`22:52` him. But go ahead and do that. In regards to skills, how much context also
`22:54` regards to skills, how much context also
`22:54` regards to skills, how much context also so you guys can see this. Um, in regards
`22:57` so you guys can see this. Um, in regards
`22:57` so you guys can see this. Um, in regards to skills, how much context have you
`22:59` to skills, how much context have you
`22:59` to skills, how much context have you seen usage increased as you keep adding
`23:01` seen usage increased as you keep adding
`23:01` seen usage increased as you keep adding skills? Yes. So, this is this is hugely
`23:04` skills? Yes. So, this is this is hugely
`23:04` skills? Yes. So, this is this is hugely important.
`23:06` important.
`23:06` important. don't want to just add a whole bunch of
`23:07` don't want to just add a whole bunch of
`23:07` don't want to just add a whole bunch of skills to something, right? Because
`23:09` skills to something, right? Because
`23:09` skills to something, right? Because look, look at just these few skills.
`23:12` look, look at just these few skills.
`23:12` look, look at just these few skills. These are lots of lines of markdown
`23:14` These are lots of lines of markdown
`23:14` These are lots of lines of markdown files. If it was reading every single
`23:16` files. If it was reading every single
`23:16` files. If it was reading every single one of these every single time, you're
`23:18` one of these every single time, you're
`23:18` one of these every single time, you're increasing context a lot. How much from
`23:21` increasing context a lot. How much from
`23:21` increasing context a lot. How much from that skill do you need actually? And
`23:25` that skill do you need actually? And
`23:25` that skill do you need actually? And you'll see some people have already what
`23:27` you'll see some people have already what
`23:27` you'll see some people have already what I call um made their skills more
`23:29` I call um made their skills more
`23:29` I call um made their skills more efficient. So, if you come in, right,
`23:32` efficient. So, if you come in, right,
`23:32` efficient. So, if you come in, right, you'll see uh that's not a good one. I'm
`23:35` you'll see uh that's not a good one. I'm
`23:35` you'll see uh that's not a good one. I'm trying to think. Is it the MCP builder
`23:37` trying to think. Is it the MCP builder
`23:37` trying to think. Is it the MCP builder one? Yeah. They'll break their skill
`23:39` one? Yeah. They'll break their skill
`23:40` one? Yeah. They'll break their skill into multiple markdown files depending
`23:42` into multiple markdown files depending
`23:42` into multiple markdown files depending on what they're doing for each step. And
`23:44` on what they're doing for each step. And
`23:44` on what they're doing for each step. And you could have sub agents only read one
`23:47` you could have sub agents only read one
`23:47` you could have sub agents only read one part of the skill while another sub
`23:49` part of the skill while another sub
`23:49` part of the skill while another sub agent's reading another. And it lowers
`23:50` agent's reading another. And it lowers
`23:50` agent's reading another. And it lowers how many the initial tokens are. Um, but
`23:54` how many the initial tokens are. Um, but
`23:54` how many the initial tokens are. Um, but I do will say I mean skills literally
`23:56` I do will say I mean skills literally
`23:56` I do will say I mean skills literally are just a massive amount of tokens that
`23:59` are just a massive amount of tokens that
`23:59` are just a massive amount of tokens that are going to increase it, which is why
`24:00` are going to increase it, which is why
`24:00` are going to increase it, which is why it's so important. You only use them
`24:03` it's so important. You only use them
`24:03` it's so important. You only use them when you need them, which is where my
`24:05` when you need them, which is where my
`24:05` when you need them, which is where my ICM comes in. When I'm creating pillars
`24:08` ICM comes in. When I'm creating pillars
`24:08` ICM comes in. When I'm creating pillars and brand ideas, I don't want to use
`24:10` and brand ideas, I don't want to use
`24:10` and brand ideas, I don't want to use every skill. But in the same project, I
`24:12` every skill. But in the same project, I
`24:12` every skill. But in the same project, I might need 150 skills. So, I'm
`24:15` might need 150 skills. So, I'm
`24:15` might need 150 skills. So, I'm organizing the folders by structure so
`24:18` organizing the folders by structure so
`24:18` organizing the folders by structure so that if I point Claude at understanding
`24:21` that if I point Claude at understanding
`24:21` that if I point Claude at understanding my pillars, it's only going to read the
`24:23` my pillars, it's only going to read the
`24:23` my pillars, it's only going to read the ones it needs for that task it's put on
`24:26` ones it needs for that task it's put on
`24:26` ones it needs for that task it's put on and then I can open up another instance
`24:28` and then I can open up another instance
`24:28` and then I can open up another instance of it. Or maybe I want to open up codecs
`24:30` of it. Or maybe I want to open up codecs
`24:30` of it. Or maybe I want to open up codecs or maybe I have a local model. It's the
`24:33` or maybe I have a local model. It's the
`24:33` or maybe I have a local model. It's the same concept. You're trying to break
`24:34` same concept. You're trying to break
`24:34` same concept. You're trying to break apart and make it so that the AI doesn't
`24:37` apart and make it so that the AI doesn't
`24:37` apart and make it so that the AI doesn't have to think where to find the task,
`24:39` have to think where to find the task,
`24:39` have to think where to find the task, but it can read the task as it needs to.
`24:42` but it can read the task as it needs to.
`24:42` but it can read the task as it needs to. Um, let's see. Can I make this bigger?
`24:45` Um, let's see. Can I make this bigger?
`24:45` Um, let's see. Can I make this bigger? Let's see. Um, I take what I learned
`24:47` Let's see. Um, I take what I learned
`24:47` Let's see. Um, I take what I learned from you and prove my message. Do you
`24:49` from you and prove my message. Do you
`24:49` from you and prove my message. Do you keep skills outside or in projects?
`24:50` keep skills outside or in projects?
`24:50` keep skills outside or in projects? Both. Both. Both. Both. Both. Both.
`24:52` Both. Both. Both. Both. Both. Both.
`24:52` Both. Both. Both. Both. Both. Both. Both. So, if I find that that skill I'm
`24:55` Both. So, if I find that that skill I'm
`24:55` Both. So, if I find that that skill I'm never going to use outside of that
`24:57` never going to use outside of that
`24:57` never going to use outside of that project, toss it in there because then
`25:00` project, toss it in there because then
`25:00` project, toss it in there because then it doesn't have to do a bash command
`25:01` it doesn't have to do a bash command
`25:02` it doesn't have to do a bash command into another folder. It can just in its
`25:04` into another folder. It can just in its
`25:04` into another folder. It can just in its process read it in there. Right. The
`25:06` process read it in there. Right. The
`25:06` process read it in there. Right. The skill. That's why I put these skills
`25:07` skill. That's why I put these skills
`25:08` skill. That's why I put these skills here. I'm not really going to use these
`25:09` here. I'm not really going to use these
`25:09` here. I'm not really going to use these skills for any other project because
`25:11` skills for any other project because
`25:11` skills for any other project because these skills are dedicated to
`25:13` these skills are dedicated to
`25:13` these skills are dedicated to specifically this folder in this
`25:15` specifically this folder in this
`25:15` specifically this folder in this project, right? But there's a lot of
`25:17` project, right? But there's a lot of
`25:17` project, right? But there's a lot of skills I use all the time and those ones
`25:20` skills I use all the time and those ones
`25:20` skills I use all the time and those ones I like to have installed so that I can,
`25:22` I like to have installed so that I can,
`25:22` I like to have installed so that I can, you know, access them without having to
`25:24` you know, access them without having to
`25:24` you know, access them without having to install them into my product and then I
`25:26` install them into my product and then I
`25:26` install them into my product and then I don't have to make my workspace flooded
`25:29` don't have to make my workspace flooded
`25:29` don't have to make my workspace flooded with extra stuff. Right? So there's
`25:31` with extra stuff. Right? So there's
`25:31` with extra stuff. Right? So there's certain skills that you might use across
`25:33` certain skills that you might use across
`25:33` certain skills that you might use across workflows. Um, let's see. Your skills
`25:37` workflows. Um, let's see. Your skills
`25:37` workflows. Um, let's see. Your skills create a script for D. Yes. Yes,
`25:39` create a script for D. Yes. Yes,
`25:39` create a script for D. Yes. Yes, absolutely. This is one of the best
`25:41` absolutely. This is one of the best
`25:41` absolutely. This is one of the best things you can do. Um, and you'll see
`25:43` things you can do. Um, and you'll see
`25:43` things you can do. Um, and you'll see most skills actually have scripts in
`25:46` most skills actually have scripts in
`25:46` most skills actually have scripts in them for the deterministic thinking. And
`25:48` them for the deterministic thinking. And
`25:48` them for the deterministic thinking. And this is why I made an argument months
`25:50` this is why I made an argument months
`25:50` this is why I made an argument months ago on a YouTube video saying that AI
`25:53` ago on a YouTube video saying that AI
`25:53` ago on a YouTube video saying that AI are the current level of models are kind
`25:55` are the current level of models are kind
`25:55` are the current level of models are kind of like compilers as they're taking
`25:58` of like compilers as they're taking
`25:58` of like compilers as they're taking logic and compiling it into a new
`26:00` logic and compiling it into a new
`26:00` logic and compiling it into a new semantic language. They're not exactly
`26:02` semantic language. They're not exactly
`26:02` semantic language. They're not exactly like compilers. Compilers are very
`26:04` like compilers. Compilers are very
`26:04` like compilers. Compilers are very deterministic, but they're also it took
`26:06` deterministic, but they're also it took
`26:06` deterministic, but they're also it took a while to get them there. If you look
`26:08` a while to get them there. If you look
`26:08` a while to get them there. If you look at a lot of skills, some skills, uh, is
`26:11` at a lot of skills, some skills, uh, is
`26:11` at a lot of skills, some skills, uh, is it front-end design? No, docs. Yeah,
`26:14` it front-end design? No, docs. Yeah,
`26:14` it front-end design? No, docs. Yeah, doc. Docx creating a word document as a
`26:17` doc. Docx creating a word document as a
`26:17` doc. Docx creating a word document as a skill. It has PI files, Python files, so
`26:21` skill. It has PI files, Python files, so
`26:21` skill. It has PI files, Python files, so that it's very deterministic on what
`26:22` that it's very deterministic on what
`26:22` that it's very deterministic on what it's outputed and how it outputs it. But
`26:25` it's outputed and how it outputs it. But
`26:25` it's outputed and how it outputs it. But on the fly, it can also edit that Python
`26:29` on the fly, it can also edit that Python
`26:29` on the fly, it can also edit that Python file. So, it's kind of the best of both
`26:31` file. So, it's kind of the best of both
`26:31` file. So, it's kind of the best of both worlds. And you can even describe in the
`26:33` worlds. And you can even describe in the
`26:33` worlds. And you can even describe in the skill how to use those scripts. Um, so
`26:36` skill how to use those scripts. Um, so
`26:36` skill how to use those scripts. Um, so yes, absolutely. Um, you want scripts
`26:40` yes, absolutely. Um, you want scripts
`26:40` yes, absolutely. Um, you want scripts for deterministic outputs. I I highly
`26:42` for deterministic outputs. I I highly
`26:42` for deterministic outputs. I I highly recommend that. Um, and it's really good
`26:44` recommend that. Um, and it's really good
`26:44` recommend that. Um, and it's really good for token. And you can see eventually
`26:47` for token. And you can see eventually
`26:47` for token. And you can see eventually you you maybe you might start out with
`26:49` you you maybe you might start out with
`26:49` you you maybe you might start out with no scripts at all and that's your skill
`26:50` no scripts at all and that's your skill
`26:50` no scripts at all and that's your skill and there's just a whole bunch of
`26:52` and there's just a whole bunch of
`26:52` and there's just a whole bunch of markdown and things. You might notice
`26:53` markdown and things. You might notice
`26:54` markdown and things. You might notice parts of it where you're like, wait a
`26:55` parts of it where you're like, wait a
`26:55` parts of it where you're like, wait a second, why am I describing this and
`26:57` second, why am I describing this and
`26:57` second, why am I describing this and making the AI do this? I could just
`26:59` making the AI do this? I could just
`26:59` making the AI do this? I could just write a script that tells it to do this
`27:02` write a script that tells it to do this
`27:02` write a script that tells it to do this instead of waiting for the AI to figure
`27:03` instead of waiting for the AI to figure
`27:03` instead of waiting for the AI to figure it out and write the script for itself.
`27:06` it out and write the script for itself.
`27:06` it out and write the script for itself. That's the whole idea behind skills and
`27:08` That's the whole idea behind skills and
`27:08` That's the whole idea behind skills and ICM. And my um my 60 3010 method is
`27:12` ICM. And my um my 60 3010 method is
`27:12` ICM. And my um my 60 3010 method is built on that. Most of the time 60% of
`27:15` built on that. Most of the time 60% of
`27:15` built on that. Most of the time 60% of your workflow is probably going to be
`27:17` your workflow is probably going to be
`27:17` your workflow is probably going to be traditional solutions, right? Most of my
`27:20` traditional solutions, right? Most of my
`27:20` traditional solutions, right? Most of my workflows are folders and files. people
`27:22` workflows are folders and files. people
`27:22` workflows are folders and files. people were trying to use AI to do all these
`27:24` were trying to use AI to do all these
`27:24` were trying to use AI to do all these crazy routing logics and stuff, but I
`27:26` crazy routing logics and stuff, but I
`27:26` crazy routing logics and stuff, but I could just use traditional solutions.
`27:28` could just use traditional solutions.
`27:28` could just use traditional solutions. 30% might be database. The magic of the
`27:32` 30% might be database. The magic of the
`27:32` 30% might be database. The magic of the 10% AI really 10% of your workflow being
`27:35` 10% AI really 10% of your workflow being
`27:35` 10% AI really 10% of your workflow being AI is where the magic really happens.
`27:37` AI is where the magic really happens.
`27:37` AI is where the magic really happens. You're you're really lowering how much
`27:39` You're you're really lowering how much
`27:39` You're you're really lowering how much tokens and processes there. Um, yes. No,
`27:43` tokens and processes there. Um, yes. No,
`27:43` tokens and processes there. Um, yes. No, I'm very excited to drop about that
`27:45` I'm very excited to drop about that
`27:45` I'm very excited to drop about that competition. We'll um I'm having Matt
`27:47` competition. We'll um I'm having Matt
`27:47` competition. We'll um I'm having Matt and I kind of look through it and we're
`27:49` and I kind of look through it and we're
`27:49` and I kind of look through it and we're definitely, again, this is our first
`27:50` definitely, again, this is our first
`27:50` definitely, again, this is our first competition. Um, for those of you who
`27:53` competition. Um, for those of you who
`27:53` competition. Um, for those of you who who don't know, we we ran a uh a
`27:55` who don't know, we we ran a uh a
`27:55` who don't know, we we ran a uh a competition um right now and we I've
`27:58` competition um right now and we I've
`27:58` competition um right now and we I've been giving them I realized some of the
`27:59` been giving them I realized some of the
`27:59` been giving them I realized some of the best ways to learn is just to create,
`28:01` best ways to learn is just to create,
`28:01` best ways to learn is just to create, right? And so we created a whole series
`28:03` right? And so we created a whole series
`28:04` right? And so we created a whole series of fake kind of don't worry these aren't
`28:05` of fake kind of don't worry these aren't
`28:05` of fake kind of don't worry these aren't actually real things. We're not
`28:06` actually real things. We're not
`28:06` actually real things. We're not offloading work on to you all. Um but
`28:09` offloading work on to you all. Um but
`28:09` offloading work on to you all. Um but it's uh let's see where did Matt put it.
`28:11` it's uh let's see where did Matt put it.
`28:11` it's uh let's see where did Matt put it. It was essentially like hey you have
`28:13` It was essentially like hey you have
`28:13` It was essentially like hey you have this client and you're trying to do work
`28:15` this client and you're trying to do work
`28:15` this client and you're trying to do work for them. Um, and it was a dog washing
`28:19` for them. Um, and it was a dog washing
`28:19` for them. Um, and it was a dog washing client. And the idea is what can you do
`28:20` client. And the idea is what can you do
`28:20` client. And the idea is what can you do to help them with their branding
`28:22` to help them with their branding
`28:22` to help them with their branding workflow process. Um, here we go. Here
`28:24` workflow process. Um, here we go. Here
`28:24` workflow process. Um, here we go. Here it is. And the idea is you just get a
`28:27` it is. And the idea is you just get a
`28:27` it is. And the idea is you just get a basic brief. Now you have to figure out,
`28:30` basic brief. Now you have to figure out,
`28:30` basic brief. Now you have to figure out, can you build the structure process, the
`28:31` can you build the structure process, the
`28:32` can you build the structure process, the brand voice, something like you see
`28:33` brand voice, something like you see
`28:33` brand voice, something like you see here, right? Like can you build this
`28:36` here, right? Like can you build this
`28:36` here, right? Like can you build this type of process for them for someone
`28:38` type of process for them for someone
`28:38` type of process for them for someone else and hand it off to them? And we're
`28:40` else and hand it off to them? And we're
`28:40` else and hand it off to them? And we're kind of excited to see. And then of
`28:42` kind of excited to see. And then of
`28:42` kind of excited to see. And then of course whoever wins is going to be $200.
`28:44` course whoever wins is going to be $200.
`28:44` course whoever wins is going to be $200. We are gonna do community vote because I
`28:46` We are gonna do community vote because I
`28:46` We are gonna do community vote because I figured it would be kind of bias. Um,
`28:49` figured it would be kind of bias. Um,
`28:49` figured it would be kind of bias. Um, and I don't also have enough time to
`28:50` and I don't also have enough time to
`28:50` and I don't also have enough time to really focus in on it. But if that
`28:52` really focus in on it. But if that
`28:52` really focus in on it. But if that doesn't work well, we're doing one of
`28:54` doesn't work well, we're doing one of
`28:54` doesn't work well, we're doing one of these every week. Um, and we're going to
`28:57` these every week. Um, and we're going to
`28:57` these every week. Um, and we're going to refine what the voting is like when it's
`28:59` refine what the voting is like when it's
`28:59` refine what the voting is like when it's pushed there. So, please just work with
`29:00` pushed there. So, please just work with
`29:00` pushed there. So, please just work with us on this. Um, but I want to and don't
`29:02` us on this. Um, but I want to and don't
`29:02` us on this. Um, but I want to and don't worry, Jenna, that you missed it. We're
`29:03` worry, Jenna, that you missed it. We're
`29:03` worry, Jenna, that you missed it. We're doing one every single week because you
`29:05` doing one every single week because you
`29:05` doing one every single week because you all have been supporting me. Every
`29:07` all have been supporting me. Every
`29:07` all have been supporting me. Every premium member is getting immediately
`29:09` premium member is getting immediately
`29:09` premium member is getting immediately allowed to come into this. You guys are
`29:10` allowed to come into this. You guys are
`29:10` allowed to come into this. You guys are giving me $27 or for those of you who
`29:12` giving me $27 or for those of you who
`29:12` giving me $27 or for those of you who joined early, $7. um you all are gonna
`29:15` joined early, $7. um you all are gonna
`29:15` joined early, $7. um you all are gonna be having access to win 200 bucks every
`29:18` be having access to win 200 bucks every
`29:18` be having access to win 200 bucks every single week because I just again I make
`29:20` single week because I just again I make
`29:20` single week because I just again I make good money with my main company. I'm not
`29:22` good money with my main company. I'm not
`29:22` good money with my main company. I'm not here to take money from everyone, but I
`29:24` here to take money from everyone, but I
`29:24` here to take money from everyone, but I need to put a pay wall behind some of my
`29:26` need to put a pay wall behind some of my
`29:26` need to put a pay wall behind some of my time. So, I figured a good way to make
`29:27` time. So, I figured a good way to make
`29:27` time. So, I figured a good way to make me feel less crappy. Um even though,
`29:30` me feel less crappy. Um even though,
`29:30` me feel less crappy. Um even though, right, you all are hopefully getting a
`29:31` right, you all are hopefully getting a
`29:31` right, you all are hopefully getting a massive amount of value is like, well,
`29:33` massive amount of value is like, well,
`29:33` massive amount of value is like, well, let's make competitions where you all
`29:34` let's make competitions where you all
`29:34` let's make competitions where you all can earn money. Um and that's that's
`29:36` can earn money. Um and that's that's
`29:36` can earn money. Um and that's that's something there. And I'm sorry that you
`29:38` something there. And I'm sorry that you
`29:38` something there. And I'm sorry that you missed this, Matt. Um, but again,
`29:39` missed this, Matt. Um, but again,
`29:40` missed this, Matt. Um, but again, literally every single week. So, for the
`29:42` literally every single week. So, for the
`29:42` literally every single week. So, for the next year, every week, we're doing a
`29:44` next year, every week, we're doing a
`29:44` next year, every week, we're doing a competition. So, if you missed this one,
`29:46` competition. So, if you missed this one,
`29:46` competition. So, if you missed this one, there's going to be more. I'm realizing
`29:48` there's going to be more. I'm realizing
`29:48` there's going to be more. I'm realizing now we could have done better marketing
`29:50` now we could have done better marketing
`29:50` now we could have done better marketing on it and letting people know. So, I'll
`29:52` on it and letting people know. So, I'll
`29:52` on it and letting people know. So, I'll work on that in the future and talking
`29:53` work on that in the future and talking
`29:53` work on that in the future and talking about it in Discord. Um, but that's the
`29:56` about it in Discord. Um, but that's the
`29:56` about it in Discord. Um, but that's the idea there, too. So, uh, just wanted to
`29:58` idea there, too. So, uh, just wanted to
`29:58` idea there, too. So, uh, just wanted to share about that. Um, yeah. No, dude. I
`30:01` share about that. Um, yeah. No, dude. I
`30:01` share about that. Um, yeah. No, dude. I And this is I checked on it this
`30:02` And this is I checked on it this
`30:02` And this is I checked on it this morning. I'm literally You know what?
`30:04` morning. I'm literally You know what?
`30:04` morning. I'm literally You know what? Let me just give you an idea of what
`30:06` Let me just give you an idea of what
`30:06` Let me just give you an idea of what like my normal kind of day is. My
`30:09` like my normal kind of day is. My
`30:09` like my normal kind of day is. My Instagram and my um my chats I when when
`30:13` Instagram and my um my chats I when when
`30:13` Instagram and my um my chats I when when I respond to you understand I'm
`30:15` I respond to you understand I'm
`30:15` I respond to you understand I'm responding after a massive amount
`30:17` responding after a massive amount
`30:17` responding after a massive amount because not only do I have crazy general
`30:19` because not only do I have crazy general
`30:20` because not only do I have crazy general but my request it says 15. It's not 15.
`30:23` but my request it says 15. It's not 15.
`30:23` but my request it says 15. It's not 15. This is in the last 24 hours, right? And
`30:25` This is in the last 24 hours, right? And
`30:25` This is in the last 24 hours, right? And I love it. Like don't get me wrong, this
`30:27` I love it. Like don't get me wrong, this
`30:27` I love it. Like don't get me wrong, this is a great problem to have, but like I
`30:29` is a great problem to have, but like I
`30:29` is a great problem to have, but like I am I am putting payw walls in around
`30:32` am I am putting payw walls in around
`30:32` am I am putting payw walls in around stuff because if I tried to answer every
`30:34` stuff because if I tried to answer every
`30:34` stuff because if I tried to answer every single one of these, I just I would
`30:36` single one of these, I just I would
`30:36` single one of these, I just I would never get to any of you all. Um could
`30:38` never get to any of you all. Um could
`30:38` never get to any of you all. Um could the competition get pinned? Yeah, I'll
`30:40` the competition get pinned? Yeah, I'll
`30:40` the competition get pinned? Yeah, I'll repin it right now actually. Um so, uh
`30:44` repin it right now actually. Um so, uh
`30:44` repin it right now actually. Um so, uh so that could be there just in case too.
`30:46` so that could be there just in case too.
`30:46` so that could be there just in case too. Let me share the link here for you all.
`30:49` Let me share the link here for you all.
`30:49` Let me share the link here for you all. Um so that you kind of get into that.
`30:52` Um so that you kind of get into that.
`30:52` Um so that you kind of get into that. Yeah, I know. I feel bad. Aaron
`30:53` Yeah, I know. I feel bad. Aaron
`30:53` Yeah, I know. I feel bad. Aaron literally puts massive amount of work
`30:55` literally puts massive amount of work
`30:55` literally puts massive amount of work for me. I'm he's amazing and like also a
`30:58` for me. I'm he's amazing and like also a
`30:58` for me. I'm he's amazing and like also a devil dog brother Marine and I still
`30:59` devil dog brother Marine and I still
`31:00` devil dog brother Marine and I still barely have time for him and it's super
`31:01` barely have time for him and it's super
`31:01` barely have time for him and it's super bad because he has two really cool
`31:03` bad because he has two really cool
`31:03` bad because he has two really cool projects I want to work on with him. Um
`31:05` projects I want to work on with him. Um
`31:05` projects I want to work on with him. Um and he also has a friend that he sent a
`31:07` and he also has a friend that he sent a
`31:07` and he also has a friend that he sent a thing there. So I'm it's it's I need to
`31:09` thing there. So I'm it's it's I need to
`31:09` thing there. So I'm it's it's I need to get a second phone and a virtual
`31:10` get a second phone and a virtual
`31:10` get a second phone and a virtual assistant. But I also struggle
`31:13` assistant. But I also struggle
`31:13` assistant. But I also struggle automating this because then I'm missing
`31:16` automating this because then I'm missing
`31:16` automating this because then I'm missing the interaction. The whole point I
`31:17` the interaction. The whole point I
`31:17` the interaction. The whole point I started this was the interaction for
`31:19` started this was the interaction for
`31:19` started this was the interaction for things and thank you Erin, you're you're
`31:20` things and thank you Erin, you're you're
`31:20` things and thank you Erin, you're you're the best. Um but yeah, I'll make sure
`31:22` the best. Um but yeah, I'll make sure
`31:22` the best. Um but yeah, I'll make sure that the those are there. Um,
`31:25` that the those are there. Um,
`31:25` that the those are there. Um, skillbuilder MCP also great by
`31:27` skillbuilder MCP also great by
`31:27` skillbuilder MCP also great by anthropic. Um, and I'm glad that you
`31:29` anthropic. Um, and I'm glad that you
`31:29` anthropic. Um, and I'm glad that you really like this kind of method. My
`31:31` really like this kind of method. My
`31:31` really like this kind of method. My research paper um on the history of
`31:33` research paper um on the history of
`31:33` research paper um on the history of software development. Yeah, let me let
`31:35` software development. Yeah, let me let
`31:35` software development. Yeah, let me let me go ahead. So, it's on it's published
`31:36` me go ahead. So, it's on it's published
`31:36` me go ahead. So, it's on it's published on rxive
`31:38` on rxive
`31:38` on rxive um I also have an ethics engine research
`31:41` um I also have an ethics engine research
`31:41` um I also have an ethics engine research paper where I go into um psychometrics
`31:44` paper where I go into um psychometrics
`31:44` paper where I go into um psychometrics in AI that I published which is cool.
`31:45` in AI that I published which is cool.
`31:45` in AI that I published which is cool. So, that one and then interpret
`31:49` So, that one and then interpret
`31:49` So, that one and then interpret interpretive context methodology. We'll
`31:52` interpretive context methodology. We'll
`31:52` interpretive context methodology. We'll go right here and I'll share that. I do
`31:54` go right here and I'll share that. I do
`31:54` go right here and I'll share that. I do make posts around it every so often, but
`31:55` make posts around it every so often, but
`31:55` make posts around it every so often, but I'll make a big post. So, those two are
`31:57` I'll make a big post. So, those two are
`31:57` I'll make a big post. So, those two are really good papers if you want to dive
`31:59` really good papers if you want to dive
`31:59` really good papers if you want to dive into like my more academic research.
`32:01` into like my more academic research.
`32:01` into like my more academic research. This one's really crazy. I um I I
`32:04` This one's really crazy. I um I I
`32:04` This one's really crazy. I um I I basically gave a whole bunch of I
`32:05` basically gave a whole bunch of I
`32:05` basically gave a whole bunch of I created a data pipeline uh where I took
`32:08` created a data pipeline uh where I took
`32:08` created a data pipeline uh where I took a whole bunch of psychometric tests,
`32:10` a whole bunch of psychometric tests,
`32:10` a whole bunch of psychometric tests, personality tests, and aimed them
`32:12` personality tests, and aimed them
`32:12` personality tests, and aimed them thousands and thousands of times at some
`32:14` thousands and thousands of times at some
`32:14` thousands and thousands of times at some of the top models and collected their
`32:16` of the top models and collected their
`32:16` of the top models and collected their answers and basically found patterns on
`32:18` answers and basically found patterns on
`32:18` answers and basically found patterns on how they answer. Uh which is is really
`32:21` how they answer. Uh which is is really
`32:21` how they answer. Uh which is is really interesting. Um, and then of course,
`32:23` interesting. Um, and then of course,
`32:23` interesting. Um, and then of course, yeah, the the context methodology. I go
`32:25` yeah, the the context methodology. I go
`32:25` yeah, the the context methodology. I go all the way into kind of the history of
`32:28` all the way into kind of the history of
`32:28` all the way into kind of the history of like, okay, um, the Unix tradition, what
`32:31` like, okay, um, the Unix tradition, what
`32:31` like, okay, um, the Unix tradition, what we're doing there. I talk about David
`32:33` we're doing there. I talk about David
`32:33` we're doing there. I talk about David Parn's ideas and there's a lot of good
`32:35` Parn's ideas and there's a lot of good
`32:35` Parn's ideas and there's a lot of good links like I have even if you don't read
`32:37` links like I have even if you don't read
`32:37` links like I have even if you don't read most of my paper going back to some of
`32:39` most of my paper going back to some of
`32:39` most of my paper going back to some of the original content uh back from the
`32:41` the original content uh back from the
`32:41` the original content uh back from the 1970s 1980s is really cool because again
`32:45` 1970s 1980s is really cool because again
`32:45` 1970s 1980s is really cool because again these are super important processes that
`32:48` these are super important processes that
`32:48` these are super important processes that were developed way before I was even
`32:50` were developed way before I was even
`32:50` were developed way before I was even born. That's what I'm doing. I'm
`32:52` born. That's what I'm doing. I'm
`32:52` born. That's what I'm doing. I'm learning from the past to build the
`32:54` learning from the past to build the
`32:54` learning from the past to build the future and that's that's where a lot of
`32:55` future and that's that's where a lot of
`32:56` future and that's that's where a lot of this comes. Same for that. I realize I'm
`32:57` this comes. Same for that. I realize I'm
`32:57` this comes. Same for that. I realize I'm talking very fast so I need to slow
`32:59` talking very fast so I need to slow
`32:59` talking very fast so I need to slow down. I get very excited about these
`33:01` down. I get very excited about these
`33:01` down. I get very excited about these things. But yeah, I uh I I I very highly
`33:04` things. But yeah, I uh I I I very highly
`33:04` things. But yeah, I uh I I I very highly recommend checking that stuff out. This
`33:06` recommend checking that stuff out. This
`33:06` recommend checking that stuff out. This is why I make videos because it forces
`33:08` is why I make videos because it forces
`33:08` is why I make videos because it forces me to slow down. And Woosaw um outside
`33:11` me to slow down. And Woosaw um outside
`33:11` me to slow down. And Woosaw um outside of the competition too. Again, I wanted
`33:13` of the competition too. Again, I wanted
`33:13` of the competition too. Again, I wanted this to be I realized I'm getting so
`33:15` this to be I realized I'm getting so
`33:15` this to be I realized I'm getting so many people in here and a lot of other
`33:16` many people in here and a lot of other
`33:16` many people in here and a lot of other communities will charge a lot more money
`33:19` communities will charge a lot more money
`33:19` communities will charge a lot more money than what I'm charging to get people in.
`33:21` than what I'm charging to get people in.
`33:21` than what I'm charging to get people in. They won't even make it free to join.
`33:23` They won't even make it free to join.
`33:23` They won't even make it free to join. And right, I I I I think that's because
`33:26` And right, I I I I think that's because
`33:26` And right, I I I I think that's because they want to make money in the front
`33:27` they want to make money in the front
`33:27` they want to make money in the front end. But in my opinion, making other
`33:29` end. But in my opinion, making other
`33:29` end. But in my opinion, making other people money makes you more money in the
`33:31` people money makes you more money in the
`33:31` people money makes you more money in the long term. Um, and so we we figure it
`33:34` long term. Um, and so we we figure it
`33:34` long term. Um, and so we we figure it out. We're going to test it and see how
`33:35` out. We're going to test it and see how
`33:35` out. We're going to test it and see how you all like it. If you do, it's a um a
`33:38` you all like it. If you do, it's a um a
`33:38` you all like it. If you do, it's a um a referral program. So, if you refer
`33:39` referral program. So, if you refer
`33:40` referral program. So, if you refer someone to premium or you refer them to
`33:41` someone to premium or you refer them to
`33:41` someone to premium or you refer them to VIP, you make money. Now, I want to be
`33:44` VIP, you make money. Now, I want to be
`33:44` VIP, you make money. Now, I want to be very careful with this. This is
`33:45` very careful with this. This is
`33:45` very careful with this. This is dangerously touching on multi-level
`33:47` dangerously touching on multi-level
`33:47` dangerously touching on multi-level marketing, and I do not want that to be
`33:49` marketing, and I do not want that to be
`33:49` marketing, and I do not want that to be here. I just wanted to give you all
`33:51` here. I just wanted to give you all
`33:51` here. I just wanted to give you all something of value. This is not a
`33:52` something of value. This is not a
`33:52` something of value. This is not a full-time job. This is not me saying,
`33:54` full-time job. This is not me saying,
`33:54` full-time job. This is not me saying, "Hey, here's a course on how to make
`33:55` "Hey, here's a course on how to make
`33:56` "Hey, here's a course on how to make more money with more money." I just
`33:57` more money with more money." I just
`33:57` more money with more money." I just wanted to say here's a link if you want
`33:59` wanted to say here's a link if you want
`33:59` wanted to say here's a link if you want to share it with people because you're
`34:01` to share it with people because you're
`34:01` to share it with people because you're getting value. Here's some cash because
`34:03` getting value. Here's some cash because
`34:03` getting value. Here's some cash because I'm getting value out of all of you
`34:04` I'm getting value out of all of you
`34:04` I'm getting value out of all of you being here by being a part of this. Um,
`34:07` being here by being a part of this. Um,
`34:07` being here by being a part of this. Um, and that's to me is important. It should
`34:09` and that's to me is important. It should
`34:09` and that's to me is important. It should be I think um let me see. Whoops. Going
`34:12` be I think um let me see. Whoops. Going
`34:12` be I think um let me see. Whoops. Going to open all the Discord. Oh, there's my
`34:14` to open all the Discord. Oh, there's my
`34:14` to open all the Discord. Oh, there's my desktop background. For those of you who
`34:15` desktop background. For those of you who
`34:15` desktop background. For those of you who are Dragon Ball Z fans, well, this is
`34:17` are Dragon Ball Z fans, well, this is
`34:17` are Dragon Ball Z fans, well, this is Dragon Ball before even Dragon Ball Z.
`34:19` Dragon Ball before even Dragon Ball Z.
`34:19` Dragon Ball before even Dragon Ball Z. Um, is very good to Where did I Oops.
`34:21` Um, is very good to Where did I Oops.
`34:22` Um, is very good to Where did I Oops. School. Here we go. Um, one thing that
`34:24` School. Here we go. Um, one thing that
`34:24` School. Here we go. Um, one thing that you I think you just go into settings
`34:27` you I think you just go into settings
`34:27` you I think you just go into settings and then go to invite and it should have
`34:29` and then go to invite and it should have
`34:29` and then go to invite and it should have an affiliate link. I'm an owner of this
`34:31` an affiliate link. I'm an owner of this
`34:31` an affiliate link. I'm an owner of this so I can't remember where it is or I
`34:33` so I can't remember where it is or I
`34:33` so I can't remember where it is or I don't see it. I don't have that option.
`34:35` don't see it. I don't have that option.
`34:35` don't see it. I don't have that option. Um, Matt kind of talks about it right
`34:37` Um, Matt kind of talks about it right
`34:37` Um, Matt kind of talks about it right here. Where is it?
`34:40` here. Where is it?
`34:40` here. Where is it? Yeah, open school. Click invite button.
`34:42` Yeah, open school. Click invite button.
`34:42` Yeah, open school. Click invite button. Okay, you click the invite button. That
`34:43` Okay, you click the invite button. That
`34:43` Okay, you click the invite button. That should be at the top of the page and you
`34:45` should be at the top of the page and you
`34:45` should be at the top of the page and you should see an personal affiliate link.
`34:47` should see an personal affiliate link.
`34:47` should see an personal affiliate link. Feel free to share it with those people
`34:48` Feel free to share it with those people
`34:48` Feel free to share it with those people and uh it it's pretty good. Oh yeah,
`34:51` and uh it it's pretty good. Oh yeah,
`34:51` and uh it it's pretty good. Oh yeah, dude. I've dra I've read and watched all
`34:53` dude. I've dra I've read and watched all
`34:53` dude. I've dra I've read and watched all of the manga of Dragon Ball, Dragon Ball
`34:55` of the manga of Dragon Ball, Dragon Ball
`34:55` of the manga of Dragon Ball, Dragon Ball Z, Dragon Ball Super. Uh I'm like uh
`34:58` Z, Dragon Ball Super. Uh I'm like uh
`34:58` Z, Dragon Ball Super. Uh I'm like uh what is it? Dragon Ball GT, which
`35:00` what is it? Dragon Ball GT, which
`35:00` what is it? Dragon Ball GT, which technically isn't canon, but I like
`35:02` technically isn't canon, but I like
`35:02` technically isn't canon, but I like that, too. And then for those of you who
`35:03` that, too. And then for those of you who
`35:03` that, too. And then for those of you who don't know, uh but maybe you should
`35:05` don't know, uh but maybe you should
`35:05` don't know, uh but maybe you should check it out. Dragon Ball Z Abridged is
`35:07` check it out. Dragon Ball Z Abridged is
`35:07` check it out. Dragon Ball Z Abridged is one of the funniest shows I've ever seen
`35:09` one of the funniest shows I've ever seen
`35:09` one of the funniest shows I've ever seen in my life. Basically, they dubbed over
`35:11` in my life. Basically, they dubbed over
`35:11` in my life. Basically, they dubbed over all of the characters um ideas uh and
`35:14` all of the characters um ideas uh and
`35:14` all of the characters um ideas uh and voices, and it is so funny. Uh highly
`35:17` voices, and it is so funny. Uh highly
`35:17` voices, and it is so funny. Uh highly recommend it from Team Four Star. Little
`35:19` recommend it from Team Four Star. Little
`35:19` recommend it from Team Four Star. Little bit offensive. probably wouldn't go well
`35:21` bit offensive. probably wouldn't go well
`35:21` bit offensive. probably wouldn't go well um in in every, you know, walk of life,
`35:24` um in in every, you know, walk of life,
`35:24` um in in every, you know, walk of life, but definitely definitely check that
`35:25` but definitely definitely check that
`35:25` but definitely definitely check that out. Uh let's see. Okay, so uh let me
`35:29` out. Uh let's see. Okay, so uh let me
`35:29` out. Uh let's see. Okay, so uh let me stop sharing my screen and and kind of
`35:30` stop sharing my screen and and kind of
`35:30` stop sharing my screen and and kind of go. I I think I promised Carlos that I
`35:33` go. I I think I promised Carlos that I
`35:33` go. I I think I promised Carlos that I would let him talk about his project and
`35:35` would let him talk about his project and
`35:35` would let him talk about his project and I took up a whole bunch of time here.
`35:37` I took up a whole bunch of time here.
`35:37` I took up a whole bunch of time here. So, um I know we're six minutes over,
`35:39` So, um I know we're six minutes over,
`35:39` So, um I know we're six minutes over, but that's okay. I I like hanging out
`35:40` but that's okay. I I like hanging out
`35:40` but that's okay. I I like hanging out with you all. Um you got to start at
`35:43` with you all. Um you got to start at
`35:43` with you all. Um you got to start at Dragon Ball if you haven't. Oh, you know
`35:44` Dragon Ball if you haven't. Oh, you know
`35:44` Dragon Ball if you haven't. Oh, you know what would be cool is if I made shirts
`35:46` what would be cool is if I made shirts
`35:46` what would be cool is if I made shirts based off of Cleaf Notes for Dragon Ball
`35:48` based off of Cleaf Notes for Dragon Ball
`35:48` based off of Cleaf Notes for Dragon Ball Z competition winners. got them. That
`35:50` Z competition winners. got them. That
`35:50` Z competition winners. got them. That would make me happy because I would wear
`35:51` would make me happy because I would wear
`35:52` would make me happy because I would wear those too. Anyway, um Carlos, would you
`35:54` those too. Anyway, um Carlos, would you
`35:54` those too. Anyway, um Carlos, would you let me let me make it so that you can
`35:57` let me let me make it so that you can
`35:57` let me let me make it so that you can share your screen and talk. Where are we
`35:59` share your screen and talk. Where are we
`36:00` share your screen and talk. Where are we here? Um there we are. So, you should be
`36:03` here? Um there we are. So, you should be
`36:03` here? Um there we are. So, you should be allowed allow audio and allow video. Um
`36:07` allowed allow audio and allow video. Um
`36:07` allowed allow audio and allow video. Um but yeah, let's uh share your project
`36:09` but yeah, let's uh share your project
`36:09` but yeah, let's uh share your project questions, things like that. I'll give
`36:10` questions, things like that. I'll give
`36:10` questions, things like that. I'll give you give you some time here. Um like I
`36:12` you give you some time here. Um like I
`36:12` you give you some time here. Um like I said, I know we're over time, so anyone
`36:14` said, I know we're over time, so anyone
`36:14` said, I know we're over time, so anyone who doesn't want to sit around, you're
`36:15` who doesn't want to sit around, you're
`36:15` who doesn't want to sit around, you're not you don't have to, but I'd love to
`36:17` not you don't have to, but I'd love to
`36:17` not you don't have to, but I'd love to hear from you, Carlos. Yeah, thanks man.
`36:19` hear from you, Carlos. Yeah, thanks man.
`36:19` hear from you, Carlos. Yeah, thanks man. Can you hear me there?
`36:21` Can you hear me there?
`36:21` Can you hear me there? >> Absolutely. Right. So pretty much what
`36:23` >> Absolutely. Right. So pretty much what
`36:23` >> Absolutely. Right. So pretty much what I'm trying to build here is I've been
`36:24` I'm trying to build here is I've been
`36:24` I'm trying to build here is I've been going around um you know AI agencies
`36:28` going around um you know AI agencies
`36:28` going around um you know AI agencies for you know go high level and all those
`36:31` for you know go high level and all those
`36:31` for you know go high level and all those automations but now I moved apart from
`36:33` automations but now I moved apart from
`36:34` automations but now I moved apart from the companies I work with and I'm trying
`36:36` the companies I work with and I'm trying
`36:36` the companies I work with and I'm trying to build a personal AI assistant which
`36:39` to build a personal AI assistant which
`36:39` to build a personal AI assistant which can then create for business owner a a
`36:43` can then create for business owner a a
`36:43` can then create for business owner a a personal assistant which they're able to
`36:46` personal assistant which they're able to
`36:46` personal assistant which they're able to manage data from their business or maybe
`36:48` manage data from their business or maybe
`36:48` manage data from their business or maybe create a new workflow without breaking
`36:51` create a new workflow without breaking
`36:51` create a new workflow without breaking the structure so the agent won't be
`36:53` the structure so the agent won't be
`36:54` the structure so the agent won't be hallucinating or having all these
`36:55` hallucinating or having all these
`36:55` hallucinating or having all these difficulties. So it's kind of something
`36:58` difficulties. So it's kind of something
`36:58` difficulties. So it's kind of something I want to build as I already have my AI
`37:01` I want to build as I already have my AI
`37:01` I want to build as I already have my AI agent but try to replicate that. So
`37:03` agent but try to replicate that. So
`37:03` agent but try to replicate that. So between me and him scaffold the whole
`37:06` between me and him scaffold the whole
`37:06` between me and him scaffold the whole thing for business owners non- tech guys
`37:09` thing for business owners non- tech guys
`37:09` thing for business owners non- tech guys you know people don't want to mess
`37:10` you know people don't want to mess
`37:10` you know people don't want to mess around with programming don't want to be
`37:12` around with programming don't want to be
`37:12` around with programming don't want to be managing files and stuff. So me having
`37:16` managing files and stuff. So me having
`37:16` managing files and stuff. So me having the, you know, the admin permissions and
`37:19` the, you know, the admin permissions and
`37:19` the, you know, the admin permissions and then they'll have the owner permissions
`37:21` then they'll have the owner permissions
`37:21` then they'll have the owner permissions for the AI assistant, which practically
`37:23` for the AI assistant, which practically
`37:23` for the AI assistant, which practically when they say, "Hey, I have a new
`37:25` when they say, "Hey, I have a new
`37:25` when they say, "Hey, I have a new employee," they can call their AI and
`37:27` employee," they can call their AI and
`37:27` employee," they can call their AI and let them know the their phone number and
`37:29` let them know the their phone number and
`37:29` let them know the their phone number and just move with their business, you know,
`37:32` just move with their business, you know,
`37:32` just move with their business, you know, pretty much. I mean, I have I haven't
`37:33` pretty much. I mean, I have I haven't
`37:33` pretty much. I mean, I have I haven't gone through it a lot. My AI assistant
`37:36` gone through it a lot. My AI assistant
`37:36` gone through it a lot. My AI assistant works pretty great. is still managing a
`37:38` works pretty great. is still managing a
`37:38` works pretty great. is still managing a lot of stuff there. But I understand
`37:40` lot of stuff there. But I understand
`37:40` lot of stuff there. But I understand that every client, every business owner
`37:42` that every client, every business owner
`37:42` that every client, every business owner needs different MCPs. So I I found that
`37:45` needs different MCPs. So I I found that
`37:45` needs different MCPs. So I I found that Composio could do a custom MCP connector
`37:50` Composio could do a custom MCP connector
`37:50` Composio could do a custom MCP connector which then I would link it to manage
`37:53` which then I would link it to manage
`37:53` which then I would link it to manage agents from Tropic so that their AI
`37:55` agents from Tropic so that their AI
`37:55` agents from Tropic so that their AI agent would be living via Appy because
`37:59` agent would be living via Appy because
`37:59` agent would be living via Appy because mine would live from my subscription,
`38:01` mine would live from my subscription,
`38:01` mine would live from my subscription, right? So instead of me setting up the
`38:04` right? So instead of me setting up the
`38:04` right? So instead of me setting up the whole cloud subscription for them, I
`38:07` whole cloud subscription for them, I
`38:07` whole cloud subscription for them, I would just put them on an API for
`38:09` would just put them on an API for
`38:09` would just put them on an API for anthropic manage agents and, you know,
`38:11` anthropic manage agents and, you know,
`38:11` anthropic manage agents and, you know, try to make it work.
`38:18` You're you're muted, brother. So
`38:18` You're you're muted, brother. So >> thank you. Um, I think that's a really
`38:20` >> thank you. Um, I think that's a really
`38:20` >> thank you. Um, I think that's a really solid idea. One thing that I I've I've
`38:22` solid idea. One thing that I I've I've
`38:22` solid idea. One thing that I I've I've gotten some success with in the past is
`38:24` gotten some success with in the past is
`38:24` gotten some success with in the past is like organizational management uh is
`38:26` like organizational management uh is
`38:26` like organizational management uh is really annoying for a lot of companies.
`38:28` really annoying for a lot of companies.
`38:28` really annoying for a lot of companies. And if you can like make that easier
`38:30` And if you can like make that easier
`38:30` And if you can like make that easier through like a UI, um, being able to do
`38:33` through like a UI, um, being able to do
`38:33` through like a UI, um, being able to do that, people will pay money for that. I
`38:34` that, people will pay money for that. I
`38:34` that, people will pay money for that. I know I'm constantly see me on Instagram
`38:36` know I'm constantly see me on Instagram
`38:36` know I'm constantly see me on Instagram just absolutely crapping on agents and
`38:38` just absolutely crapping on agents and
`38:38` just absolutely crapping on agents and stuff like that. It's it's for most
`38:41` stuff like that. It's it's for most
`38:41` stuff like that. It's it's for most people. I will say there's plenty of
`38:42` people. I will say there's plenty of
`38:42` people. I will say there's plenty of situations to make money and and today's
`38:44` situations to make money and and today's
`38:44` situations to make money and and today's VIP session, we're actually going to
`38:46` VIP session, we're actually going to
`38:46` VIP session, we're actually going to dive deep into um kind of uh one of one
`38:49` dive deep into um kind of uh one of one
`38:49` dive deep into um kind of uh one of one of the uh individuals in there had a
`38:51` of the uh individuals in there had a
`38:51` of the uh individuals in there had a similar question like, "Hey, I'm
`38:52` similar question like, "Hey, I'm
`38:52` similar question like, "Hey, I'm building this stuff on Langraph. Is it
`38:54` building this stuff on Langraph. Is it
`38:54` building this stuff on Langraph. Is it going to get replaced?" And my response
`38:55` going to get replaced?" And my response
`38:56` going to get replaced?" And my response to him is essentially going to be, well,
`38:58` to him is essentially going to be, well,
`38:58` to him is essentially going to be, well, it might. Anthropic can drop something
`39:00` it might. Anthropic can drop something
`39:00` it might. Anthropic can drop something tomorrow that does what your company
`39:02` tomorrow that does what your company
`39:02` tomorrow that does what your company does. It doesn't mean that you can't
`39:03` does. It doesn't mean that you can't
`39:03` does. It doesn't mean that you can't make money with that company, right?
`39:05` make money with that company, right?
`39:05` make money with that company, right? People are still not, some people don't
`39:07` People are still not, some people don't
`39:07` People are still not, some people don't even know what chatt is, or they do and
`39:09` even know what chatt is, or they do and
`39:09` even know what chatt is, or they do and have never used it. I just worked with a
`39:11` have never used it. I just worked with a
`39:11` have never used it. I just worked with a uh a client down in Miami. Everyone in
`39:13` uh a client down in Miami. Everyone in
`39:13` uh a client down in Miami. Everyone in his office, all of his admins had never
`39:16` his office, all of his admins had never
`39:16` his office, all of his admins had never even used a chatbot, right? That still
`39:18` even used a chatbot, right? That still
`39:18` even used a chatbot, right? That still exists. And this is a multi-million
`39:19` exists. And this is a multi-million
`39:19` exists. And this is a multi-million dollar company. It's not like they were
`39:21` dollar company. It's not like they were
`39:21` dollar company. It's not like they were just some small. They're bringing in a
`39:23` just some small. They're bringing in a
`39:23` just some small. They're bringing in a lot of money, but they're in the
`39:24` lot of money, but they're in the
`39:24` lot of money, but they're in the construction side. So, they don't always
`39:26` construction side. So, they don't always
`39:26` construction side. So, they don't always maybe see that in their algorithm. And a
`39:28` maybe see that in their algorithm. And a
`39:28` maybe see that in their algorithm. And a lot of you might see a lot of AI out
`39:30` lot of you might see a lot of AI out
`39:30` lot of you might see a lot of AI out there, but at the end of the day, you
`39:31` there, but at the end of the day, you
`39:31` there, but at the end of the day, you have to remember a huge amount of people
`39:33` have to remember a huge amount of people
`39:33` have to remember a huge amount of people are not touching it and using it in the
`39:35` are not touching it and using it in the
`39:35` are not touching it and using it in the way you are. And that's value. That's
`39:36` way you are. And that's value. That's
`39:36` way you are. And that's value. That's shortcut that people are willing to pay
`39:38` shortcut that people are willing to pay
`39:38` shortcut that people are willing to pay for. Now, for your specific example,
`39:40` for. Now, for your specific example,
`39:40` for. Now, for your specific example, Carlos, I think um yeah, the things you
`39:43` Carlos, I think um yeah, the things you
`39:43` Carlos, I think um yeah, the things you want to look at there is um if you are
`39:46` want to look at there is um if you are
`39:46` want to look at there is um if you are building through anthropic managed
`39:48` building through anthropic managed
`39:48` building through anthropic managed agents, understand you're going to be
`39:49` agents, understand you're going to be
`39:49` agents, understand you're going to be locked into anthropic. That's okay.
`39:51` locked into anthropic. That's okay.
`39:52` locked into anthropic. That's okay. That's fine. If if you're able if you
`39:53` That's fine. If if you're able if you
`39:53` That's fine. If if you're able if you like the value in them and you see
`39:55` like the value in them and you see
`39:55` like the value in them and you see value, then you know, do that. Run with
`39:58` value, then you know, do that. Run with
`39:58` value, then you know, do that. Run with that. The only thing is if Anthropic ups
`40:00` that. The only thing is if Anthropic ups
`40:00` that. The only thing is if Anthropic ups their prices, if they change how manage
`40:02` their prices, if they change how manage
`40:02` their prices, if they change how manage agents work, you have to then and you
`40:05` agents work, you have to then and you
`40:05` agents work, you have to then and you have clients and businesses using it at
`40:07` have clients and businesses using it at
`40:07` have clients and businesses using it at scale, you now have to deal with what
`40:09` scale, you now have to deal with what
`40:09` scale, you now have to deal with what that is. So, I would always keep in the
`40:11` that is. So, I would always keep in the
`40:11` that is. So, I would always keep in the back of your head, it doesn't mean stop
`40:13` back of your head, it doesn't mean stop
`40:13` back of your head, it doesn't mean stop using managed agents. If it's the
`40:15` using managed agents. If it's the
`40:15` using managed agents. If it's the cheapest, quickest, fastest solution
`40:16` cheapest, quickest, fastest solution
`40:16` cheapest, quickest, fastest solution that gets you value, absolutely use it.
`40:18` that gets you value, absolutely use it.
`40:18` that gets you value, absolutely use it. But always think, okay, is there a way
`40:21` But always think, okay, is there a way
`40:21` But always think, okay, is there a way for me to do this without anthropics
`40:23` for me to do this without anthropics
`40:24` for me to do this without anthropics mandated agents or how can I create the
`40:26` mandated agents or how can I create the
`40:26` mandated agents or how can I create the structure separate from it that I could
`40:28` structure separate from it that I could
`40:28` structure separate from it that I could latch on elsewhere later? You don't have
`40:30` latch on elsewhere later? You don't have
`40:30` latch on elsewhere later? You don't have to implement it, but it's just one of
`40:32` to implement it, but it's just one of
`40:32` to implement it, but it's just one of those things where you want to have it
`40:33` those things where you want to have it
`40:33` those things where you want to have it in your back pocket. So, if you get a
`40:35` in your back pocket. So, if you get a
`40:35` in your back pocket. So, if you get a bill from anthropic API that's triple
`40:37` bill from anthropic API that's triple
`40:37` bill from anthropic API that's triple what you were expecting and you're at
`40:39` what you were expecting and you're at
`40:39` what you were expecting and you're at scale and you have 2,000 clients on this
`40:41` scale and you have 2,000 clients on this
`40:41` scale and you have 2,000 clients on this software, which I think you could,
`40:43` software, which I think you could,
`40:43` software, which I think you could, right? What you were describing is very
`40:44` right? What you were describing is very
`40:44` right? What you were describing is very useful. Um, and you want to pilot it.
`40:47` useful. Um, and you want to pilot it.
`40:47` useful. Um, and you want to pilot it. Are are you already pil piloting it with
`40:49` Are are you already pil piloting it with
`40:49` Are are you already pil piloting it with anyone right now or um is it not?
`40:51` anyone right now or um is it not?
`40:51` anyone right now or um is it not? >> So what I have here is um pretty much
`40:54` >> So what I have here is um pretty much
`40:54` >> So what I have here is um pretty much the the front end for my clients right
`40:56` the the front end for my clients right
`40:56` the the front end for my clients right now is go high level because that allows
`40:59` now is go high level because that allows
`40:59` now is go high level because that allows me not to create an API for WhatsApp for
`41:02` me not to create an API for WhatsApp for
`41:02` me not to create an API for WhatsApp for Facebook, Instagram. So the front end as
`41:04` Facebook, Instagram. So the front end as
`41:04` Facebook, Instagram. So the front end as a CRM for them to manage their clients
`41:07` a CRM for them to manage their clients
`41:07` a CRM for them to manage their clients and then I would I would connect my AI
`41:10` and then I would I would connect my AI
`41:10` and then I would I would connect my AI assistant. So everything lives in the
`41:13` assistant. So everything lives in the
`41:13` assistant. So everything lives in the same repo in GitHub. And then when I
`41:15` same repo in GitHub. And then when I
`41:15` same repo in GitHub. And then when I have my client's folder only in their
`41:18` have my client's folder only in their
`41:18` have my client's folder only in their folder their their assistant can use uh
`41:22` folder their their assistant can use uh
`41:22` folder their their assistant can use uh GitHub API to manage business configs
`41:26` GitHub API to manage business configs
`41:26` GitHub API to manage business configs and it would be and that's why I'm using
`41:29` and it would be and that's why I'm using
`41:29` and it would be and that's why I'm using my managed agents practically so that
`41:31` my managed agents practically so that
`41:31` my managed agents practically so that they can touch the part of GitHub only
`41:33` they can touch the part of GitHub only
`41:33` they can touch the part of GitHub only the business part not the config but I'm
`41:35` the business part not the config but I'm
`41:35` the business part not the config but I'm still on top of everything with my AI
`41:37` still on top of everything with my AI
`41:38` still on top of everything with my AI assistant and he's trying to you know
`41:40` assistant and he's trying to you know
`41:40` assistant and he's trying to you know like actually correct mapping and all
`41:42` like actually correct mapping and all
`41:42` like actually correct mapping and all that ICM that you've saying I would not
`41:46` that ICM that you've saying I would not
`41:46` that ICM that you've saying I would not made something custom right now because
`41:48` made something custom right now because
`41:48` made something custom right now because I think those tools like the go level
`41:50` I think those tools like the go level
`41:50` I think those tools like the go level and manage agents are far instead of me
`41:53` and manage agents are far instead of me
`41:53` and manage agents are far instead of me going creating something you always say
`41:55` going creating something you always say
`41:55` going creating something you always say like until then you know until you have
`41:57` like until then you know until you have
`41:57` like until then you know until you have that issue go ahead and do it I do not
`42:00` that issue go ahead and do it I do not
`42:00` that issue go ahead and do it I do not have any pilot right now I mean I was
`42:01` have any pilot right now I mean I was
`42:01` have any pilot right now I mean I was trying to do it for some one of my
`42:03` trying to do it for some one of my
`42:03` trying to do it for some one of my clients but I think I'm I've been kind
`42:06` clients but I think I'm I've been kind
`42:06` clients but I think I'm I've been kind of stuck on the on the part of the
`42:07` of stuck on the on the part of the
`42:07` of stuck on the on the part of the skills and all that you were saying at
`42:09` skills and all that you were saying at
`42:09` skills and all that you were saying at the beginning this is actually something
`42:12` the beginning this is actually something
`42:12` the beginning this is actually something I can you know replicate for a new
`42:15` I can you know replicate for a new
`42:15` I can you know replicate for a new client without me having to go through
`42:16` client without me having to go through
`42:16` client without me having to go through the whole thing about onboarding and and
`42:19` the whole thing about onboarding and and
`42:19` the whole thing about onboarding and and all that.
`42:20` all that.
`42:20` all that. >> So, it's I'm kind of stuck on that part
`42:21` >> So, it's I'm kind of stuck on that part
`42:21` >> So, it's I'm kind of stuck on that part where I can make it scalable, right?
`42:24` where I can make it scalable, right?
`42:24` where I can make it scalable, right? >> Yes,
`42:24` >> Yes,
`42:24` >> Yes, >> it should be easy. I mean, it should be
`42:26` >> it should be easy. I mean, it should be
`42:26` >> it should be easy. I mean, it should be easy the way you put things, you know?
`42:27` easy the way you put things, you know?
`42:28` easy the way you put things, you know? It sounds easy and it I understand it
`42:30` It sounds easy and it I understand it
`42:30` It sounds easy and it I understand it might be a lot easier with the workspace
`42:32` might be a lot easier with the workspace
`42:32` might be a lot easier with the workspace builders and client delivery and all
`42:34` builders and client delivery and all
`42:34` builders and client delivery and all that you already you already have in
`42:36` that you already you already have in
`42:36` that you already you already have in your but I'm kind of stuck in that part
`42:39` your but I'm kind of stuck in that part
`42:39` your but I'm kind of stuck in that part where I'm I'm trying to make it
`42:40` where I'm I'm trying to make it
`42:40` where I'm I'm trying to make it manageable and scalable for myself
`42:42` manageable and scalable for myself
`42:42` manageable and scalable for myself without having to you know
`42:46` without having to you know
`42:46` without having to you know go through all the well pretty much from
`42:49` go through all the well pretty much from
`42:49` go through all the well pretty much from not to start from zero but actually go
`42:52` not to start from zero but actually go
`42:52` not to start from zero but actually go forward and and scale that. Yeah, I
`42:55` forward and and scale that. Yeah, I
`42:56` forward and and scale that. Yeah, I think the scalability question is going
`42:58` think the scalability question is going
`42:58` think the scalability question is going to be a question you're going to hear me
`42:59` to be a question you're going to hear me
`42:59` to be a question you're going to hear me talk about a lot more too because we're
`43:01` talk about a lot more too because we're
`43:01` talk about a lot more too because we're we're looking at how to scale ICM inside
`43:03` we're looking at how to scale ICM inside
`43:04` we're looking at how to scale ICM inside of enterprise a lot more um the process
`43:06` of enterprise a lot more um the process
`43:06` of enterprise a lot more um the process the learning and uh our solution was to
`43:09` the learning and uh our solution was to
`43:09` the learning and uh our solution was to build a kind of scalable learning
`43:11` build a kind of scalable learning
`43:11` build a kind of scalable learning solution called scribe. Um, but for your
`43:14` solution called scribe. Um, but for your
`43:14` solution called scribe. Um, but for your specific situation, um, I think, and
`43:19` specific situation, um, I think, and
`43:19` specific situation, um, I think, and this might sound crazy, what might be
`43:21` this might sound crazy, what might be
`43:21` this might sound crazy, what might be interesting, have you have you thought
`43:23` interesting, have you have you thought
`43:23` interesting, have you have you thought about this and maybe I'm maybe you've
`43:24` about this and maybe I'm maybe you've
`43:24` about this and maybe I'm maybe you've already done this and have you thought
`43:25` already done this and have you thought
`43:26` already done this and have you thought about trying to have the process be
`43:28` about trying to have the process be
`43:28` about trying to have the process be manual and train and work with one of
`43:30` manual and train and work with one of
`43:30` manual and train and work with one of your clients or even a new client and
`43:32` your clients or even a new client and
`43:32` your clients or even a new client and upfront say most of this is haphazard
`43:36` upfront say most of this is haphazard
`43:36` upfront say most of this is haphazard and manual. I want to work with you or
`43:38` and manual. I want to work with you or
`43:38` and manual. I want to work with you or one of your people to get the outcome.
`43:41` one of your people to get the outcome.
`43:41` one of your people to get the outcome. So you use your kind of disgruntled kind
`43:43` So you use your kind of disgruntled kind
`43:43` So you use your kind of disgruntled kind of all over the place systems and you
`43:45` of all over the place systems and you
`43:45` of all over the place systems and you use people to scale it short term and
`43:48` use people to scale it short term and
`43:48` use people to scale it short term and then as they're using it as they find
`43:51` then as they're using it as they find
`43:51` then as they're using it as they find problems you find just one little thing
`43:53` problems you find just one little thing
`43:53` problems you find just one little thing to automate and you chip away over a
`43:55` to automate and you chip away over a
`43:55` to automate and you chip away over a month or two months automating those
`43:57` month or two months automating those
`43:57` month or two months automating those small parts and then you integrate those
`43:59` small parts and then you integrate those
`43:59` small parts and then you integrate those together rather than trying to figure
`44:01` together rather than trying to figure
`44:01` together rather than trying to figure out what the scalability is now or what
`44:03` out what the scalability is now or what
`44:03` out what the scalability is now or what the integrations are now. try to get the
`44:06` the integrations are now. try to get the
`44:06` the integrations are now. try to get the outcome that they would get with that
`44:08` outcome that they would get with that
`44:08` outcome that they would get with that software manually. And then as they're
`44:11` software manually. And then as they're
`44:11` software manually. And then as they're working with it, I guarantee you you're
`44:13` working with it, I guarantee you you're
`44:13` working with it, I guarantee you you're going to notice points like, "Oh, oh,
`44:15` going to notice points like, "Oh, oh,
`44:15` going to notice points like, "Oh, oh, this is what I could add in here." Or,
`44:17` this is what I could add in here." Or,
`44:17` this is what I could add in here." Or, "Oh, wait. Go High Level already has
`44:19` "Oh, wait. Go High Level already has
`44:19` "Oh, wait. Go High Level already has this integration to handle that. Let's
`44:21` this integration to handle that. Let's
`44:21` this integration to handle that. Let's just stop doing it manually." Um, yeah,
`44:24` just stop doing it manually." Um, yeah,
`44:24` just stop doing it manually." Um, yeah, it's almost like key loggers. That's
`44:25` it's almost like key loggers. That's
`44:25` it's almost like key loggers. That's funny. Um, David, that's really good.
`44:27` funny. Um, David, that's really good.
`44:27` funny. Um, David, that's really good. And Toby, you said you're you're doing
`44:29` And Toby, you said you're you're doing
`44:29` And Toby, you said you're you're doing that for your company. Maybe I shouldn't
`44:31` that for your company. Maybe I shouldn't
`44:31` that for your company. Maybe I shouldn't be talking. Um, Toby, would you be
`44:33` be talking. Um, Toby, would you be
`44:33` be talking. Um, Toby, would you be willing to maybe describe to Carlos in
`44:35` willing to maybe describe to Carlos in
`44:35` willing to maybe describe to Carlos in in your perspective? Because again, I'm
`44:38` in your perspective? Because again, I'm
`44:38` in your perspective? Because again, I'm not the only one that has value here.
`44:39` not the only one that has value here.
`44:39` not the only one that has value here. This is the whole reason I bring these
`44:40` This is the whole reason I bring these
`44:40` This is the whole reason I bring these groups together. Uh, if not, you don't
`44:42` groups together. Uh, if not, you don't
`44:42` groups together. Uh, if not, you don't have to talk, but um Oh, wait. You have
`44:44` have to talk, but um Oh, wait. You have
`44:44` have to talk, but um Oh, wait. You have to be allowed to talk, don't you? Let me
`44:46` to be allowed to talk, don't you? Let me
`44:46` to be allowed to talk, don't you? Let me show you. You should be uh let's see.
`44:49` show you. You should be uh let's see.
`44:49` show you. You should be uh let's see. Allow audio and allow video. There we
`44:52` Allow audio and allow video. There we
`44:52` Allow audio and allow video. There we go. Um, yeah. Toby, do you want to chat
`44:55` go. Um, yeah. Toby, do you want to chat
`44:55` go. Um, yeah. Toby, do you want to chat on that?
`44:57` on that?
`44:57` on that? Possibly. If not, it's okay. Um, I think
`45:00` Possibly. If not, it's okay. Um, I think
`45:00` Possibly. If not, it's okay. Um, I think I just gave you the ability to talk
`45:03` I just gave you the ability to talk
`45:03` I just gave you the ability to talk allegedly.
`45:05` allegedly.
`45:05` allegedly. Is that making sense, Carlos, while
`45:07` Is that making sense, Carlos, while
`45:07` Is that making sense, Carlos, while we're waiting for?
`45:08` we're waiting for?
`45:08` we're waiting for? >> Yeah, I mean it it totally makes one of
`45:10` >> Yeah, I mean it it totally makes one of
`45:10` >> Yeah, I mean it it totally makes one of the things that I also use as um, you
`45:13` the things that I also use as um, you
`45:13` the things that I also use as um, you know, infra is the same high level
`45:16` know, infra is the same high level
`45:16` know, infra is the same high level because you can build workflows in
`45:18` because you can build workflows in
`45:18` because you can build workflows in there. So instead of me building like on
`45:21` there. So instead of me building like on
`45:21` there. So instead of me building like on the folder side some workflows some of
`45:24` the folder side some workflows some of
`45:24` the folder side some workflows some of them I just make them hey I have this
`45:26` them I just make them hey I have this
`45:26` them I just make them hey I have this workflow in high level what you can use
`45:28` workflow in high level what you can use
`45:28` workflow in high level what you can use instead of pulling it out you know not
`45:31` instead of pulling it out you know not
`45:31` instead of pulling it out you know not letting any like everything to the AI
`45:33` letting any like everything to the AI
`45:33` letting any like everything to the AI but the problem is that what you said
`45:36` but the problem is that what you said
`45:36` but the problem is that what you said because not every client's going to be
`45:38` because not every client's going to be
`45:38` because not every client's going to be the same. So I'm trying to be a more
`45:40` the same. So I'm trying to be a more
`45:40` the same. So I'm trying to be a more niche guy for some businesses that this
`45:43` niche guy for some businesses that this
`45:43` niche guy for some businesses that this can be, you know, a little bit more
`45:45` can be, you know, a little bit more
`45:45` can be, you know, a little bit more replicable.
`45:47` replicable.
`45:47` replicable. >> And that's actually a huge part. Start
`45:50` >> And that's actually a huge part. Start
`45:50` >> And that's actually a huge part. Start niche, then find the scalability.
`45:53` niche, then find the scalability.
`45:53` niche, then find the scalability. Everyone tries to find the scalability
`45:54` Everyone tries to find the scalability
`45:54` Everyone tries to find the scalability and then niche down. I think in the AI
`45:57` and then niche down. I think in the AI
`45:57` and then niche down. I think in the AI world, you'll find the patterns if you
`45:59` world, you'll find the patterns if you
`45:59` world, you'll find the patterns if you solve the problems of something niche
`46:01` solve the problems of something niche
`46:01` solve the problems of something niche and you'll slowly take components out of
`46:03` and you'll slowly take components out of
`46:03` and you'll slowly take components out of it um with every single niche client
`46:05` it um with every single niche client
`46:05` it um with every single niche client that you get. And now this is hard,
`46:07` that you get. And now this is hard,
`46:07` that you get. And now this is hard, right? like that's going to take time.
`46:09` right? like that's going to take time.
`46:09` right? like that's going to take time. That's that's a good moat. If it takes
`46:11` That's that's a good moat. If it takes
`46:11` That's that's a good moat. If it takes time and it's hard, even with AI, that
`46:14` time and it's hard, even with AI, that
`46:14` time and it's hard, even with AI, that means you found a very good business
`46:17` means you found a very good business
`46:17` means you found a very good business because now it's not something that
`46:18` because now it's not something that
`46:18` because now it's not something that someone can copy easily, right? You want
`46:21` someone can copy easily, right? You want
`46:21` someone can copy easily, right? You want to look for the things that are not best
`46:23` to look for the things that are not best
`46:23` to look for the things that are not best but different that are are opinionated
`46:26` but different that are are opinionated
`46:26` but different that are are opinionated or are niche because that's where you're
`46:28` or are niche because that's where you're
`46:28` or are niche because that's where you're going to find value over the next
`46:29` going to find value over the next
`46:29` going to find value over the next decade. Sure. Are most of the things
`46:32` decade. Sure. Are most of the things
`46:32` decade. Sure. Are most of the things we're creating now going to be
`46:33` we're creating now going to be
`46:33` we're creating now going to be automatable in two years, three years?
`46:36` automatable in two years, three years?
`46:36` automatable in two years, three years? Probably. We're moving at a fast pace,
`46:38` Probably. We're moving at a fast pace,
`46:38` Probably. We're moving at a fast pace, but the problem is doesn't matter if you
`46:40` but the problem is doesn't matter if you
`46:40` but the problem is doesn't matter if you automate everything. What matters is who
`46:43` automate everything. What matters is who
`46:43` automate everything. What matters is who you're reaching and if they see you
`46:45` you're reaching and if they see you
`46:45` you're reaching and if they see you first, right? There's a thousand copies
`46:47` first, right? There's a thousand copies
`46:48` first, right? There's a thousand copies of every company out there. Every single
`46:50` of every company out there. Every single
`46:50` of every company out there. Every single one of them is making money. Almost
`46:52` one of them is making money. Almost
`46:52` one of them is making money. Almost every single one of them. The ones that
`46:53` every single one of them. The ones that
`46:53` every single one of them. The ones that aren't are the ones that either give up
`46:56` aren't are the ones that either give up
`46:56` aren't are the ones that either give up or invest too much in the wrong thing.
`46:58` or invest too much in the wrong thing.
`46:58` or invest too much in the wrong thing. At the end of the day, you could make an
`47:00` At the end of the day, you could make an
`47:00` At the end of the day, you could make an Uber app in your local city that does
`47:03` Uber app in your local city that does
`47:03` Uber app in your local city that does something specific for your local city
`47:04` something specific for your local city
`47:04` something specific for your local city that Uber doesn't, and you'd probably
`47:06` that Uber doesn't, and you'd probably
`47:06` that Uber doesn't, and you'd probably get some good customers. Like, I
`47:08` get some good customers. Like, I
`47:08` get some good customers. Like, I guarantee you. But a lot of people won't
`47:09` guarantee you. But a lot of people won't
`47:10` guarantee you. But a lot of people won't try to build that because they're
`47:11` try to build that because they're
`47:11` try to build that because they're looking at too big of a market. Start
`47:13` looking at too big of a market. Start
`47:14` looking at too big of a market. Start with a niche market. Start with one
`47:15` with a niche market. Start with one
`47:16` with a niche market. Start with one company, one person, then build up.
`47:19` company, one person, then build up.
`47:19` company, one person, then build up. Because I promise you, once you get it
`47:21` Because I promise you, once you get it
`47:21` Because I promise you, once you get it right with one person, you can get it
`47:22` right with one person, you can get it
`47:22` right with one person, you can get it right with 10. Once you get it right
`47:24` right with 10. Once you get it right
`47:24` right with 10. Once you get it right with 10 people, you know what you need
`47:26` with 10 people, you know what you need
`47:26` with 10 people, you know what you need to get to a 100 people. Once you get it
`47:28` to get to a 100 people. Once you get it
`47:28` to get to a 100 people. Once you get it right with a hundred people, then you
`47:29` right with a hundred people, then you
`47:29` right with a hundred people, then you can get it to a thousand. But until
`47:31` can get it to a thousand. But until
`47:32` can get it to a thousand. But until then, you will, if you try to skip to
`47:33` then, you will, if you try to skip to
`47:33` then, you will, if you try to skip to 10,000, nine times out of ten, you will
`47:36` 10,000, nine times out of ten, you will
`47:36` 10,000, nine times out of ten, you will just be stuck in a loop of figuring it
`47:38` just be stuck in a loop of figuring it
`47:38` just be stuck in a loop of figuring it out and getting stuck in barriers versus
`47:40` out and getting stuck in barriers versus
`47:40` out and getting stuck in barriers versus just brute forcing it. Plus, with
`47:42` just brute forcing it. Plus, with
`47:42` just brute forcing it. Plus, with smaller niches, they're more forgiving.
`47:44` smaller niches, they're more forgiving.
`47:44` smaller niches, they're more forgiving. They're more willing for you to say,
`47:46` They're more willing for you to say,
`47:46` They're more willing for you to say, "Hey, I don't have this fully solved.
`47:48` "Hey, I don't have this fully solved.
`47:48` "Hey, I don't have this fully solved. I'd love for you to work as a partner to
`47:50` I'd love for you to work as a partner to
`47:50` I'd love for you to work as a partner to help me break through this
`47:51` help me break through this
`47:52` help me break through this productionizing thing." Uh, to see if I
`47:54` productionizing thing." Uh, to see if I
`47:54` productionizing thing." Uh, to see if I should even productionize it in the
`47:55` should even productionize it in the
`47:55` should even productionize it in the first place. uh right because your goal
`47:57` first place. uh right because your goal
`47:57` first place. uh right because your goal should be get the outcome they want
`47:59` should be get the outcome they want
`47:59` should be get the outcome they want today regardless of how manual it is and
`48:02` today regardless of how manual it is and
`48:02` today regardless of how manual it is and then work backwards on making it
`48:04` then work backwards on making it
`48:04` then work backwards on making it automatable like a lot of clients a lot
`48:06` automatable like a lot of clients a lot
`48:06` automatable like a lot of clients a lot of software I've built I did the process
`48:08` of software I've built I did the process
`48:08` of software I've built I did the process manually for a client with a couple of
`48:10` manually for a client with a couple of
`48:10` manually for a client with a couple of AI tools scattered and then did it more
`48:12` AI tools scattered and then did it more
`48:12` AI tools scattered and then did it more and more and out of annoyance I found
`48:15` and more and out of annoyance I found
`48:15` and more and out of annoyance I found the production because I'm like I don't
`48:16` the production because I'm like I don't
`48:16` the production because I'm like I don't want to do this anymore and so I'm
`48:18` want to do this anymore and so I'm
`48:18` want to do this anymore and so I'm always trying to automate myself that's
`48:20` always trying to automate myself that's
`48:20` always trying to automate myself that's always the goal every day I'm like how
`48:22` always the goal every day I'm like how
`48:22` always the goal every day I'm like how can I replace what I'm doing today
`48:24` can I replace what I'm doing today
`48:24` can I replace what I'm doing today because I feel like there's so much more
`48:25` because I feel like there's so much more
`48:26` because I feel like there's so much more I could be doing. Uh there's always
`48:28` I could be doing. Uh there's always
`48:28` I could be doing. Uh there's always people that I'm trying to help, always
`48:29` people that I'm trying to help, always
`48:30` people that I'm trying to help, always people that I'm trying to think. And
`48:31` people that I'm trying to think. And
`48:31` people that I'm trying to think. And then also there's the artistic side. I'm
`48:32` then also there's the artistic side. I'm
`48:32` then also there's the artistic side. I'm always trying to make music or art or
`48:34` always trying to make music or art or
`48:34` always trying to make music or art or these things. I think the idea that if
`48:37` these things. I think the idea that if
`48:37` these things. I think the idea that if this skill I have gets automated or this
`48:40` this skill I have gets automated or this
`48:40` this skill I have gets automated or this process I have gets automated, I'm
`48:42` process I have gets automated, I'm
`48:42` process I have gets automated, I'm replaced is is crazy. Humans aren't
`48:45` replaced is is crazy. Humans aren't
`48:45` replaced is is crazy. Humans aren't replaceable when this is very hippie-
`48:47` replaceable when this is very hippie-
`48:47` replaceable when this is very hippie- dippy. So some of you might not believe
`48:48` dippy. So some of you might not believe
`48:48` dippy. So some of you might not believe this, but humans aren't replaceable in
`48:51` this, but humans aren't replaceable in
`48:51` this, but humans aren't replaceable in the same way I think people put it out
`48:52` the same way I think people put it out
`48:52` the same way I think people put it out to be. I mean, human creativity is
`48:54` to be. I mean, human creativity is
`48:54` to be. I mean, human creativity is infinite. I believe that. And yeah,
`48:57` infinite. I believe that. And yeah,
`48:57` infinite. I believe that. And yeah, okay, sure, we replaced carriage and
`48:59` okay, sure, we replaced carriage and
`48:59` okay, sure, we replaced carriage and horses with cars, but guess what? In St.
`49:01` horses with cars, but guess what? In St.
`49:01` horses with cars, but guess what? In St. Augustine, I see more carriage horses
`49:04` Augustine, I see more carriage horses
`49:04` Augustine, I see more carriage horses going down my street than cars. Like, we
`49:06` going down my street than cars. Like, we
`49:06` going down my street than cars. Like, we have a whole bunch of them still because
`49:08` have a whole bunch of them still because
`49:08` have a whole bunch of them still because people care about those things. And that
`49:10` people care about those things. And that
`49:10` people care about those things. And that is a market and someone is making a good
`49:12` is a market and someone is making a good
`49:12` is a market and someone is making a good living off of that. We're we're so
`49:14` living off of that. We're we're so
`49:14` living off of that. We're we're so focused on this crazy unreachable goal.
`49:17` focused on this crazy unreachable goal.
`49:17` focused on this crazy unreachable goal. It's not unreachable. Everyone in here
`49:19` It's not unreachable. Everyone in here
`49:19` It's not unreachable. Everyone in here could be a billionaire and I'd have no
`49:20` could be a billionaire and I'd have no
`49:20` could be a billionaire and I'd have no idea.
`49:21` idea.
`49:21` idea. this this idea that's like, "Oh, I have
`49:23` this this idea that's like, "Oh, I have
`49:23` this this idea that's like, "Oh, I have to I have to change the whole world."
`49:25` to I have to change the whole world."
`49:25` to I have to change the whole world." Not necessarily. Sometimes changing the
`49:27` Not necessarily. Sometimes changing the
`49:27` Not necessarily. Sometimes changing the world is one person's world. You've
`49:29` world is one person's world. You've
`49:29` world is one person's world. You've changed their whole world, right? And
`49:30` changed their whole world, right? And
`49:30` changed their whole world, right? And that could be enough. And then you can
`49:32` that could be enough. And then you can
`49:32` that could be enough. And then you can scale that later. Right. I'm a
`49:33` scale that later. Right. I'm a
`49:33` scale that later. Right. I'm a capitalist hippie. I don't know what to
`49:35` capitalist hippie. I don't know what to
`49:35` capitalist hippie. I don't know what to tell you there, but that's the way I see
`49:36` tell you there, but that's the way I see
`49:36` tell you there, but that's the way I see it. And your niche is much easier to
`49:39` it. And your niche is much easier to
`49:39` it. And your niche is much easier to handle. Exactly, David. Um, Toby. Oh,
`49:42` handle. Exactly, David. Um, Toby. Oh,
`49:42` handle. Exactly, David. Um, Toby. Oh, yeah. Sorry, Carlos. I went on a
`49:43` yeah. Sorry, Carlos. I went on a
`49:43` yeah. Sorry, Carlos. I went on a freaking rant there. Sorry.
`49:44` freaking rant there. Sorry.
`49:44` freaking rant there. Sorry. >> No, that's great. I mean, that's pretty
`49:46` >> No, that's great. I mean, that's pretty
`49:46` >> No, that's great. I mean, that's pretty much what I did. I did wrong that I try
`49:48` much what I did. I did wrong that I try
`49:48` much what I did. I did wrong that I try to scale the whole thing, you know, to
`49:50` to scale the whole thing, you know, to
`49:50` to scale the whole thing, you know, to every business I can I can get in
`49:52` every business I can I can get in
`49:52` every business I can I can get in contact with. So then I I run into the
`49:55` contact with. So then I I run into the
`49:55` contact with. So then I I run into the same problem, right? That it's not
`49:56` same problem, right? That it's not
`49:56` same problem, right? That it's not maintainable for me. And now I I went
`49:59` maintainable for me. And now I I went
`49:59` maintainable for me. And now I I went back steps I I I backed up my steps and
`50:02` back steps I I I backed up my steps and
`50:02` back steps I I I backed up my steps and you know I I just I'm trying to
`50:05` you know I I just I'm trying to
`50:05` you know I I just I'm trying to restructure the whole thing, but I'm
`50:06` restructure the whole thing, but I'm
`50:06` restructure the whole thing, but I'm still learning the ICM. I'm still
`50:09` still learning the ICM. I'm still
`50:09` still learning the ICM. I'm still learning your p mythology. It's kind of
`50:11` learning your p mythology. It's kind of
`50:11` learning your p mythology. It's kind of like uh I'm stuck with both things,
`50:14` like uh I'm stuck with both things,
`50:14` like uh I'm stuck with both things, learning, but also produ, you know,
`50:16` learning, but also produ, you know,
`50:16` learning, but also produ, you know, going to production. But I guess I I
`50:18` going to production. But I guess I I
`50:18` going to production. But I guess I I went a few steps back and and and
`50:20` went a few steps back and and and
`50:20` went a few steps back and and and instead of building like a whole thing,
`50:22` instead of building like a whole thing,
`50:22` instead of building like a whole thing, I'm just going to start by a niche,
`50:24` I'm just going to start by a niche,
`50:24` I'm just going to start by a niche, which I already have an offer for that
`50:25` which I already have an offer for that
`50:26` which I already have an offer for that and I'm going to be hitting that, you
`50:27` and I'm going to be hitting that, you
`50:27` and I'm going to be hitting that, you know, probably this week. Uh,
`50:30` know, probably this week. Uh,
`50:30` know, probably this week. Uh, >> good.
`50:30` >> good.
`50:30` >> good. >> So, yeah. Good.
`50:31` >> So, yeah. Good.
`50:31` >> So, yeah. Good. >> Thanks for that, man. Really appreciate
`50:32` >> Thanks for that, man. Really appreciate
`50:32` >> Thanks for that, man. Really appreciate it.
`50:33` it.
`50:33` it. >> Few steps back is still moving forward,
`50:36` >> Few steps back is still moving forward,
`50:36` >> Few steps back is still moving forward, right? Because sometimes if you were
`50:39` right? Because sometimes if you were
`50:39` right? Because sometimes if you were kept pushing through that wall, guess
`50:41` kept pushing through that wall, guess
`50:41` kept pushing through that wall, guess what? In six months, you would have come
`50:42` what? In six months, you would have come
`50:42` what? In six months, you would have come to the same conclusion that you are now.
`50:45` to the same conclusion that you are now.
`50:45` to the same conclusion that you are now. The all business is is pivoting. Right?
`50:48` The all business is is pivoting. Right?
`50:48` The all business is is pivoting. Right? My what Aduba was I went this is
`50:50` My what Aduba was I went this is
`50:50` My what Aduba was I went this is something that all of you need to know.
`50:51` something that all of you need to know.
`50:51` something that all of you need to know. My company, right? I I would argue I'm
`50:53` My company, right? I I would argue I'm
`50:53` My company, right? I I would argue I'm very successful now. Four years ago, I
`50:56` very successful now. Four years ago, I
`50:56` very successful now. Four years ago, I was in a business competition at one of
`50:58` was in a business competition at one of
`50:58` was in a business competition at one of my older schools. I lost I went to it
`51:00` my older schools. I lost I went to it
`51:00` my older schools. I lost I went to it three times. I didn't even place in the
`51:02` three times. I didn't even place in the
`51:02` three times. I didn't even place in the top three every single time with what I
`51:05` top three every single time with what I
`51:05` top three every single time with what I am doing today because it was different.
`51:07` am doing today because it was different.
`51:07` am doing today because it was different. I wasn't perceiving it right. I didn't
`51:08` I wasn't perceiving it right. I didn't
`51:08` I wasn't perceiving it right. I didn't All of the things I'm telling you aren't
`51:10` All of the things I'm telling you aren't
`51:10` All of the things I'm telling you aren't because I'm smart. It's because I
`51:11` because I'm smart. It's because I
`51:11` because I'm smart. It's because I screwed up. I took the steps back. But
`51:14` screwed up. I took the steps back. But
`51:14` screwed up. I took the steps back. But guess what? Those steps back were steps
`51:17` guess what? Those steps back were steps
`51:17` guess what? Those steps back were steps forward. They only stay steps back if
`51:20` forward. They only stay steps back if
`51:20` forward. They only stay steps back if you don't learn from them. But when you
`51:22` you don't learn from them. But when you
`51:22` you don't learn from them. But when you actually look at the whole thing, those
`51:23` actually look at the whole thing, those
`51:23` actually look at the whole thing, those steps back were you learning. If you
`51:25` steps back were you learning. If you
`51:25` steps back were you learning. If you look at it as a huge progress bar, it's
`51:28` look at it as a huge progress bar, it's
`51:28` look at it as a huge progress bar, it's not that you're falling down back on
`51:30` not that you're falling down back on
`51:30` not that you're falling down back on progress. It's that you found a new way
`51:32` progress. It's that you found a new way
`51:32` progress. It's that you found a new way to navigate the learning, right? It's a
`51:34` to navigate the learning, right? It's a
`51:34` to navigate the learning, right? It's a different path to the same direction.
`51:36` different path to the same direction.
`51:36` different path to the same direction. So, yeah, dude, focus on that one niche.
`51:39` So, yeah, dude, focus on that one niche.
`51:39` So, yeah, dude, focus on that one niche. You'll figure out a way. Just trust that
`51:41` You'll figure out a way. Just trust that
`51:41` You'll figure out a way. Just trust that you'll figure out a way to scale it and
`51:43` you'll figure out a way to scale it and
`51:43` you'll figure out a way to scale it and try to make it so good for that one
`51:45` try to make it so good for that one
`51:45` try to make it so good for that one client, so killer that from that
`51:48` client, so killer that from that
`51:48` client, so killer that from that process, you watch. I guarantee you're
`51:50` process, you watch. I guarantee you're
`51:50` process, you watch. I guarantee you're going to come back in like a week or
`51:51` going to come back in like a week or
`51:51` going to come back in like a week or two, you'll be like, "Oh, while you were
`51:52` two, you'll be like, "Oh, while you were
`51:52` two, you'll be like, "Oh, while you were doing this, I had this brain explosion
`51:53` doing this, I had this brain explosion
`51:53` doing this, I had this brain explosion and I figured out how I could scale it
`51:55` and I figured out how I could scale it
`51:55` and I figured out how I could scale it here." Because I'm telling you, you
`51:57` here." Because I'm telling you, you
`51:57` here." Because I'm telling you, you will. Like I'm glad that you're learning
`51:58` will. Like I'm glad that you're learning
`51:58` will. Like I'm glad that you're learning from ICM, but what you are doing now is
`52:01` from ICM, but what you are doing now is
`52:01` from ICM, but what you are doing now is creating your own solution, which will
`52:03` creating your own solution, which will
`52:03` creating your own solution, which will be as valuable, if not more valuable
`52:05` be as valuable, if not more valuable
`52:05` be as valuable, if not more valuable than mine, right? Mine is a general
`52:07` than mine, right? Mine is a general
`52:08` than mine, right? Mine is a general solution to the way of thinking, not to
`52:10` solution to the way of thinking, not to
`52:10` solution to the way of thinking, not to the way of implementing, which is where
`52:11` the way of implementing, which is where
`52:12` the way of implementing, which is where it's limited. And I'm trying to figure
`52:13` it's limited. And I'm trying to figure
`52:13` it's limited. And I'm trying to figure out how to do that. But yeah, just just
`52:15` out how to do that. But yeah, just just
`52:15` out how to do that. But yeah, just just focus on one, then move up again. Right?
`52:18` focus on one, then move up again. Right?
`52:18` focus on one, then move up again. Right? If you bite off more of your chinchu,
`52:20` If you bite off more of your chinchu,
`52:20` If you bite off more of your chinchu, that's okay. Take a few steps back and
`52:22` that's okay. Take a few steps back and
`52:22` that's okay. Take a few steps back and try again. That's the whole that's
`52:23` try again. That's the whole that's
`52:23` try again. That's the whole that's business, man. That's business. you're
`52:25` business, man. That's business. you're
`52:25` business, man. That's business. you're it's never never going to work out
`52:27` it's never never going to work out
`52:27` it's never never going to work out perfectly and that's the point.
`52:29` perfectly and that's the point.
`52:29` perfectly and that's the point. >> That's right. Thanks, man. Appreciate
`52:31` >> That's right. Thanks, man. Appreciate
`52:31` >> That's right. Thanks, man. Appreciate that. Really
`52:33` that. Really
`52:33` that. Really >> know, of course. That's why I do these.
`52:34` >> know, of course. That's why I do these.
`52:34` >> know, of course. That's why I do these. These are my favorite things. Um well,
`52:36` These are my favorite things. Um well,
`52:36` These are my favorite things. Um well, on that note, I am 25 minutes over, 23
`52:40` on that note, I am 25 minutes over, 23
`52:40` on that note, I am 25 minutes over, 23 minutes over, which is fine. This is the
`52:41` minutes over, which is fine. This is the
`52:41` minutes over, which is fine. This is the kind of stuff I like. Um I will make
`52:43` kind of stuff I like. Um I will make
`52:43` kind of stuff I like. Um I will make sure everyone has this recording. I'll
`52:45` sure everyone has this recording. I'll
`52:45` sure everyone has this recording. I'll be putting um a bunch of extra stuff. I
`52:47` be putting um a bunch of extra stuff. I
`52:47` be putting um a bunch of extra stuff. I think um the markdown files and stuff I
`52:49` think um the markdown files and stuff I
`52:49` think um the markdown files and stuff I shared at the beginning, I'll share a
`52:50` shared at the beginning, I'll share a
`52:50` shared at the beginning, I'll share a whole bunch of that. I'm going to make a
`52:52` whole bunch of that. I'm going to make a
`52:52` whole bunch of that. I'm going to make a new um digital asset in the vault for
`52:54` new um digital asset in the vault for
`52:54` new um digital asset in the vault for everyone based off of that and based off
`52:56` everyone based off of that and based off
`52:56` everyone based off of that and based off the questions I saw. Um for those of you
`52:58` the questions I saw. Um for those of you
`52:58` the questions I saw. Um for those of you who are here, seriously, thank you. This
`53:01` who are here, seriously, thank you. This
`53:01` who are here, seriously, thank you. This is this is my favorite thing to do is
`53:03` is this is my favorite thing to do is
`53:03` is this is my favorite thing to do is just talk and learn and teach. Um so
`53:06` just talk and learn and teach. Um so
`53:06` just talk and learn and teach. Um so stay stay careful out there. Be careful.
`53:08` stay stay careful out there. Be careful.
`53:08` stay stay careful out there. Be careful. I'll have this out there. Don't rush,
`53:11` I'll have this out there. Don't rush,
`53:11` I'll have this out there. Don't rush, but rush as much as you want. Just make
`53:12` but rush as much as you want. Just make
`53:12` but rush as much as you want. Just make sure to give yourself the grace when you
`53:15` sure to give yourself the grace when you
`53:15` sure to give yourself the grace when you when you trip. That's fine. Learn from
`53:17` when you trip. That's fine. Learn from
`53:17` when you trip. That's fine. Learn from how you tripped and where the crack that
`53:18` how you tripped and where the crack that
`53:18` how you tripped and where the crack that you tripped on was. So much love. Oh.
`53:21` you tripped on was. So much love. Oh.
`53:21` you tripped on was. So much love. Oh. Uh, shoot. Hold on before I go. Ness,
`53:23` Uh, shoot. Hold on before I go. Ness,
`53:23` Uh, shoot. Hold on before I go. Ness, how do you join this Discord? If you're
`53:24` how do you join this Discord? If you're
`53:24` how do you join this Discord? If you're not part of the Discord, huge, huge
`53:26` not part of the Discord, huge, huge
`53:26` not part of the Discord, huge, huge thing you want to be a part of. Um,
`53:28` thing you want to be a part of. Um,
`53:28` thing you want to be a part of. Um, basically, let me just share this real
`53:30` basically, let me just share this real
`53:30` basically, let me just share this real quick. Uh, there's a lot of value in the
`53:32` quick. Uh, there's a lot of value in the
`53:32` quick. Uh, there's a lot of value in the Discord that I recommend because I also
`53:34` Discord that I recommend because I also
`53:34` Discord that I recommend because I also go in there and answer questions outside
`53:36` go in there and answer questions outside
`53:36` go in there and answer questions outside of this. So, if you're, you know, if
`53:38` of this. So, if you're, you know, if
`53:38` of this. So, if you're, you know, if you're in here, you're a premium member,
`53:39` you're in here, you're a premium member,
`53:39` you're in here, you're a premium member, you go in the vault, you come in and it
`53:41` you go in the vault, you come in and it
`53:41` you go in the vault, you come in and it says Discord setup, you're going to
`53:43` says Discord setup, you're going to
`53:43` says Discord setup, you're going to click this link if you're premium. If
`53:46` click this link if you're premium. If
`53:46` click this link if you're premium. If you're a VIP member and you're in here,
`53:48` you're a VIP member and you're in here,
`53:48` you're a VIP member and you're in here, then you want to go into the drawing
`53:49` then you want to go into the drawing
`53:49` then you want to go into the drawing room. um and click that link. These
`53:52` room. um and click that link. These
`53:52` room. um and click that link. These links are designed for um to give you
`53:55` links are designed for um to give you
`53:55` links are designed for um to give you the role automatically and then it'll
`53:57` the role automatically and then it'll
`53:57` the role automatically and then it'll throw you into the uh into the Discord
`54:00` throw you into the uh into the Discord
`54:00` throw you into the uh into the Discord and there's a lot of people talking. I
`54:02` and there's a lot of people talking. I
`54:02` and there's a lot of people talking. I sometimes come in and I'll do um kind of
`54:04` sometimes come in and I'll do um kind of
`54:04` sometimes come in and I'll do um kind of big dumps like this responding to people
`54:06` big dumps like this responding to people
`54:06` big dumps like this responding to people who are asking questions. We've got
`54:08` who are asking questions. We've got
`54:08` who are asking questions. We've got voice chat in there for for collabs. Um
`54:11` voice chat in there for for collabs. Um
`54:11` voice chat in there for for collabs. Um I have a collab in here that I've I've
`54:13` I have a collab in here that I've I've
`54:13` I have a collab in here that I've I've been super ignoring this channel which
`54:14` been super ignoring this channel which
`54:14` been super ignoring this channel which is bad. Um but there's a lot of ideas
`54:16` is bad. Um but there's a lot of ideas
`54:16` is bad. Um but there's a lot of ideas for pushes and ideas. So, I highly
`54:18` for pushes and ideas. So, I highly
`54:18` for pushes and ideas. So, I highly recommend getting in the Discord because
`54:20` recommend getting in the Discord because
`54:20` recommend getting in the Discord because it's nice and also Shishro and Aaron are
`54:23` it's nice and also Shishro and Aaron are
`54:23` it's nice and also Shishro and Aaron are actively in it a lot, which is super
`54:24` actively in it a lot, which is super
`54:24` actively in it a lot, which is super nice, too. Um, so yeah. Cool. Now, now I
`54:28` nice, too. Um, so yeah. Cool. Now, now I
`54:28` nice, too. Um, so yeah. Cool. Now, now I am ending it. Um, because I have to get
`54:29` am ending it. Um, because I have to get
`54:29` am ending it. Um, because I have to get ready for the VIP call coming up in the
`54:31` ready for the VIP call coming up in the
`54:31` ready for the VIP call coming up in the next five minutes. Um, so cool. Much
`54:34` next five minutes. Um, so cool. Much
`54:34` next five minutes. Um, so cool. Much love, everyone. Bye a second time. And,
`54:37` love, everyone. Bye a second time. And,
`54:37` love, everyone. Bye a second time. And, uh, if you all want to chat and talk in
`54:39` uh, if you all want to chat and talk in
`54:39` uh, if you all want to chat and talk in here, go for it. But, uh, I'd recommend
`54:41` here, go for it. But, uh, I'd recommend
`54:41` here, go for it. But, uh, I'd recommend just going and checking everything else.
`54:43` just going and checking everything else.
`54:43` just going and checking everything else. And happy learning as always.