# Claude Design Full Breakdown: GitHub Imports, Skills, and Local Model Handoff

**Channel:** Jake Van Clief  
**Uploaded:** 2026-04-20  
**Duration:** 42:29  
**URL:** [https://www.youtube.com/watch?v=pdoSAWWCDO8](https://www.youtube.com/watch?v=pdoSAWWCDO8)  

---

## Transcript

`00:02` So, you want to know how Claude design
`00:02` So, you want to know how Claude design works? You want to know how not to hit
`00:03` works? You want to know how not to hit
`00:03` works? You want to know how not to hit usage limits? And you want to know,
`00:05` usage limits? And you want to know,
`00:05` usage limits? And you want to know, maybe is there a way to do it without
`00:06` maybe is there a way to do it without
`00:06` maybe is there a way to do it without Claude? Could you possibly use local
`00:08` Claude? Could you possibly use local
`00:08` Claude? Could you possibly use local models? What kind of assets do you want?
`00:11` models? What kind of assets do you want?
`00:11` models? What kind of assets do you want? I'm going to be going over a lot of that
`00:12` I'm going to be going over a lot of that
`00:12` I'm going to be going over a lot of that over the next maybe 20, 30 minutes.
`00:14` over the next maybe 20, 30 minutes.
`00:14` over the next maybe 20, 30 minutes. We'll see. It could be 40 minutes by the
`00:16` We'll see. It could be 40 minutes by the
`00:16` We'll see. It could be 40 minutes by the time I'm done recording these. I always
`00:17` time I'm done recording these. I always
`00:17` time I'm done recording these. I always record them in one shot. But I'm going
`00:19` record them in one shot. But I'm going
`00:19` record them in one shot. But I'm going to show you my experiments with it, what
`00:20` to show you my experiments with it, what
`00:21` to show you my experiments with it, what I've learned, and how I've built a
`00:22` I've learned, and how I've built a
`00:22` I've learned, and how I've built a process locally, as well as building one
`00:24` process locally, as well as building one
`00:24` process locally, as well as building one in front of you that mostly works. And
`00:26` in front of you that mostly works. And
`00:27` in front of you that mostly works. And we'll show you what that looks like here
`00:28` we'll show you what that looks like here
`00:28` we'll show you what that looks like here shortly. Now, starting off the bat,
`00:30` shortly. Now, starting off the bat,
`00:30` shortly. Now, starting off the bat, Claude design is a new app from Claude
`00:33` Claude design is a new app from Claude
`00:33` Claude design is a new app from Claude that essentially is a series of Claude
`00:35` that essentially is a series of Claude
`00:35` that essentially is a series of Claude code and folder structures, which if
`00:37` code and folder structures, which if
`00:37` code and folder structures, which if you've been following my work, I'm a big
`00:39` you've been following my work, I'm a big
`00:39` you've been following my work, I'm a big folder structure design guy. It helps
`00:41` folder structure design guy. It helps
`00:41` folder structure design guy. It helps you create all sorts of prototypes and
`00:42` you create all sorts of prototypes and
`00:42` you create all sorts of prototypes and processes. It create You can create
`00:44` processes. It create You can create
`00:44` processes. It create You can create slide decks. You can create entire areas
`00:46` slide decks. You can create entire areas
`00:46` slide decks. You can create entire areas from your own branding and literally
`00:48` from your own branding and literally
`00:48` from your own branding and literally download branding and logo processes.
`00:50` download branding and logo processes.
`00:50` download branding and logo processes. You can create animations from it as
`00:53` You can create animations from it as
`00:53` You can create animations from it as well, being able to go into I think I
`00:55` well, being able to go into I think I
`00:55` well, being able to go into I think I created one. Yep, just yesterday. You
`00:57` created one. Yep, just yesterday. You
`00:57` created one. Yep, just yesterday. You can create all sorts of different
`00:58` can create all sorts of different
`00:58` can create all sorts of different explainer video animations and stuff
`01:00` explainer video animations and stuff
`01:00` explainer video animations and stuff with just basic prompting and brand
`01:02` with just basic prompting and brand
`01:02` with just basic prompting and brand assets as well. I created quite a few
`01:04` assets as well. I created quite a few
`01:04` assets as well. I created quite a few videos the other day on this. Now, when
`01:07` videos the other day on this. Now, when
`01:07` videos the other day on this. Now, when you're actually using this, the problem
`01:09` you're actually using this, the problem
`01:09` you're actually using this, the problem is when you're inside of Claude, you can
`01:11` is when you're inside of Claude, you can
`01:11` is when you're inside of Claude, you can come down here. It has its own usage
`01:14` come down here. It has its own usage
`01:14` come down here. It has its own usage credits, and it uses it fast. I'm on the
`01:16` credits, and it uses it fast. I'm on the
`01:16` credits, and it uses it fast. I'm on the top max plan that you can have, and I
`01:19` top max plan that you can have, and I
`01:19` top max plan that you can have, and I went through almost the full usage in
`01:21` went through almost the full usage in
`01:21` went through almost the full usage in the matter of gosh, I don't even know, a
`01:23` the matter of gosh, I don't even know, a
`01:24` the matter of gosh, I don't even know, a day. We can come down here and actually
`01:26` day. We can come down here and actually
`01:26` day. We can come down here and actually look. Claude design, I just started
`01:28` look. Claude design, I just started
`01:28` look. Claude design, I just started using it yesterday, and it's already at
`01:30` using it yesterday, and it's already at
`01:30` using it yesterday, and it's already at 83%, and I didn't even use it that much
`01:32` 83%, and I didn't even use it that much
`01:32` 83%, and I didn't even use it that much to just test these features. So, what
`01:34` to just test these features. So, what
`01:34` to just test these features. So, what does it actually look like to maybe get
`01:36` does it actually look like to maybe get
`01:37` does it actually look like to maybe get around that? How do we not How do we use
`01:39` around that? How do we not How do we use
`01:39` around that? How do we not How do we use it best? How do we best get the best
`01:41` it best? How do we best get the best
`01:41` it best? How do we best get the best output out of it? But also, how do we
`01:42` output out of it? But also, how do we
`01:42` output out of it? But also, how do we maybe figure out better ways to use it?
`01:45` maybe figure out better ways to use it?
`01:45` maybe figure out better ways to use it? Well, right off the bat, let's just look
`01:46` Well, right off the bat, let's just look
`01:47` Well, right off the bat, let's just look at what you can actually do with it.
`01:49` at what you can actually do with it.
`01:49` at what you can actually do with it. Now, what I like to do, and where I
`01:51` Now, what I like to do, and where I
`01:51` Now, what I like to do, and where I think the most power behind it is
`01:53` think the most power behind it is
`01:53` think the most power behind it is actually taking things that you or maybe
`01:55` actually taking things that you or maybe
`01:55` actually taking things that you or maybe your designers have used. So, I'm going
`01:57` your designers have used. So, I'm going
`01:57` your designers have used. So, I'm going to go through and show you different
`01:59` to go through and show you different
`01:59` to go through and show you different assets that you can actually bring in,
`02:00` assets that you can actually bring in,
`02:00` assets that you can actually bring in, extract information from, and create a
`02:03` extract information from, and create a
`02:03` extract information from, and create a design system that allows you to create
`02:05` design system that allows you to create
`02:05` design system that allows you to create almost anything from those assets in a
`02:07` almost anything from those assets in a
`02:07` almost anything from those assets in a very controlled environment. Now, I have
`02:09` very controlled environment. Now, I have
`02:09` very controlled environment. Now, I have a large GitHub where me and my front-end
`02:12` a large GitHub where me and my front-end
`02:12` a large GitHub where me and my front-end developer K, who's awesome, have put a
`02:14` developer K, who's awesome, have put a
`02:15` developer K, who's awesome, have put a whole bunch assets, components, SVGs.
`02:17` whole bunch assets, components, SVGs.
`02:17` whole bunch assets, components, SVGs. Some he built custom himself in Figma,
`02:20` Some he built custom himself in Figma,
`02:20` Some he built custom himself in Figma, some with React, HTML, all sorts of
`02:22` some with React, HTML, all sorts of
`02:22` some with React, HTML, all sorts of different things, JavaScript, right? We
`02:24` different things, JavaScript, right? We
`02:24` different things, JavaScript, right? We have all sorts of different weird assets
`02:25` have all sorts of different weird assets
`02:25` have all sorts of different weird assets in here that we've built for my personal
`02:27` in here that we've built for my personal
`02:27` in here that we've built for my personal company, uh Aduba. But we also have
`02:30` company, uh Aduba. But we also have
`02:30` company, uh Aduba. But we also have Figma, right? I've made quite a lot of
`02:32` Figma, right? I've made quite a lot of
`02:32` Figma, right? I've made quite a lot of different uh assets and slides for
`02:34` different uh assets and slides for
`02:34` different uh assets and slides for workshops that I've been doing, and a
`02:36` workshops that I've been doing, and a
`02:36` workshops that I've been doing, and a lot of these are really good, and I want
`02:37` lot of these are really good, and I want
`02:37` lot of these are really good, and I want to keep them and use them. You could
`02:39` to keep them and use them. You could
`02:39` to keep them and use them. You could also, maybe if you had Canva, you can
`02:41` also, maybe if you had Canva, you can
`02:41` also, maybe if you had Canva, you can use this as a starting point, or even
`02:43` use this as a starting point, or even
`02:43` use this as a starting point, or even just slides and PowerPoint. You can
`02:45` just slides and PowerPoint. You can
`02:45` just slides and PowerPoint. You can extract assets from that, right? That's
`02:47` extract assets from that, right? That's
`02:47` extract assets from that, right? That's a whole area.
`02:48` a whole area.
`02:48` a whole area. But essentially, what you can actually
`02:50` But essentially, what you can actually
`02:50` But essentially, what you can actually do is you could just come in and create
`02:52` do is you could just come in and create
`02:52` do is you could just come in and create a new project, right? I created a new
`02:54` a new project, right? I created a new
`02:54` a new project, right? I created a new test project here where I wanted to
`02:55` test project here where I wanted to
`02:55` test project here where I wanted to create an animated video on the skills
`02:58` create an animated video on the skills
`02:58` create an animated video on the skills that it's using. Or you can just come in
`03:01` that it's using. Or you can just come in
`03:01` that it's using. Or you can just come in and say, "Hey, I want to create a slide
`03:03` and say, "Hey, I want to create a slide
`03:03` and say, "Hey, I want to create a slide deck very quickly." Or just a project
`03:05` deck very quickly." Or just a project
`03:05` deck very quickly." Or just a project that doesn't have a aspect here. Now,
`03:08` that doesn't have a aspect here. Now,
`03:08` that doesn't have a aspect here. Now, generally, when you start a new project,
`03:10` generally, when you start a new project,
`03:10` generally, when you start a new project, project for video,
`03:13` project for video,
`03:13` project for video, you have a the standard default design
`03:15` you have a the standard default design
`03:15` you have a the standard default design system. You won't see any other design
`03:16` system. You won't see any other design
`03:16` system. You won't see any other design systems. I'll show you what happens when
`03:18` systems. I'll show you what happens when
`03:18` systems. I'll show you what happens when you make your own, but for right now,
`03:19` you make your own, but for right now,
`03:19` you make your own, but for right now, let's stick in here. Now, wireframe is
`03:22` let's stick in here. Now, wireframe is
`03:22` let's stick in here. Now, wireframe is using a lot less tokens and essentially
`03:24` using a lot less tokens and essentially
`03:24` using a lot less tokens and essentially is a way to just look at what something
`03:26` is a way to just look at what something
`03:26` is a way to just look at what something might look like. High fidelity is
`03:28` might look like. High fidelity is
`03:28` might look like. High fidelity is actually building something. Uh and it
`03:30` actually building something. Uh and it
`03:30` actually building something. Uh and it will create a lot better outputs faster,
`03:32` will create a lot better outputs faster,
`03:32` will create a lot better outputs faster, but again, use tokens significantly
`03:34` but again, use tokens significantly
`03:34` but again, use tokens significantly fast. When you actually come in, it has
`03:36` fast. When you actually come in, it has
`03:36` fast. When you actually come in, it has a folder set up, much like something you
`03:38` a folder set up, much like something you
`03:38` a folder set up, much like something you would have on your desktop or with uh
`03:40` would have on your desktop or with uh
`03:40` would have on your desktop or with uh Claude code. And you immediately have
`03:43` Claude code. And you immediately have
`03:43` Claude code. And you immediately have specific skills. So, you'll see these
`03:45` specific skills. So, you'll see these
`03:45` specific skills. So, you'll see these things right here, interactive
`03:46` things right here, interactive
`03:46` things right here, interactive prototype, high-fi design, design
`03:48` prototype, high-fi design, design
`03:48` prototype, high-fi design, design system. These are all skills. These are
`03:51` system. These are all skills. These are
`03:51` system. These are all skills. These are prompt systems. And if you actually come
`03:53` prompt systems. And if you actually come
`03:53` prompt systems. And if you actually come in and want to add more, when you click
`03:55` in and want to add more, when you click
`03:55` in and want to add more, when you click on design system, you'll see skills that
`03:58` on design system, you'll see skills that
`03:58` on design system, you'll see skills that you can add. And for those of you who
`04:00` you can add. And for those of you who
`04:00` you can add. And for those of you who are familiar with skills, they're
`04:01` are familiar with skills, they're
`04:01` are familiar with skills, they're essentially large text files or maybe a
`04:04` essentially large text files or maybe a
`04:04` essentially large text files or maybe a little bit of code on teaching Claude
`04:06` little bit of code on teaching Claude
`04:06` little bit of code on teaching Claude how to use certain things. And I've
`04:08` how to use certain things. And I've
`04:08` how to use certain things. And I've shown in past videos, uh which if you
`04:10` shown in past videos, uh which if you
`04:11` shown in past videos, uh which if you want to check them out, how to access
`04:12` want to check them out, how to access
`04:12` want to check them out, how to access some of the best skills out there.
`04:14` some of the best skills out there.
`04:14` some of the best skills out there. Anthropic actually has their own GitHub
`04:18` Anthropic actually has their own GitHub
`04:18` Anthropic actually has their own GitHub where they show their skills that they
`04:19` where they show their skills that they
`04:19` where they show their skills that they actually publish. Not all of them are
`04:21` actually publish. Not all of them are
`04:21` actually publish. Not all of them are there. Uh you can come in and see,
`04:23` there. Uh you can come in and see,
`04:23` there. Uh you can come in and see, right? Let's say you want to go in,
`04:25` right? Let's say you want to go in,
`04:25` right? Let's say you want to go in, there's a front-end design skill that
`04:26` there's a front-end design skill that
`04:26` there's a front-end design skill that helps Claude or other AI. You can give
`04:29` helps Claude or other AI. You can give
`04:29` helps Claude or other AI. You can give these skills to any AI out there because
`04:32` these skills to any AI out there because
`04:32` these skills to any AI out there because of how they're designed. And
`04:33` of how they're designed. And
`04:33` of how they're designed. And essentially, all it is is a markdown
`04:34` essentially, all it is is a markdown
`04:34` essentially, all it is is a markdown file describing how to think about
`04:37` file describing how to think about
`04:37` file describing how to think about design. Before you're building anything,
`04:39` design. Before you're building anything,
`04:39` design. Before you're building anything, do these things. You can build your own
`04:40` do these things. You can build your own
`04:40` do these things. You can build your own skills all the time, but that's
`04:42` skills all the time, but that's
`04:42` skills all the time, but that's essentially what these are. Now, inside
`04:45` essentially what these are. Now, inside
`04:45` essentially what these are. Now, inside of Claude design, it's kind of the same
`04:47` of Claude design, it's kind of the same
`04:47` of Claude design, it's kind of the same concept here, right? You come in, and
`04:49` concept here, right? You come in, and
`04:49` concept here, right? You come in, and all of these are markdown files, maybe
`04:51` all of these are markdown files, maybe
`04:51` all of these are markdown files, maybe multiple markdown files depending on the
`04:53` multiple markdown files depending on the
`04:53` multiple markdown files depending on the order, how to convert stuff into PDFs,
`04:56` order, how to convert stuff into PDFs,
`04:56` order, how to convert stuff into PDFs, how to save things as an HTML. This
`04:58` how to save things as an HTML. This
`04:58` how to save things as an HTML. This allows AI to do the same thing every
`05:00` allows AI to do the same thing every
`05:00` allows AI to do the same thing every time, the best way. And actually,
`05:02` time, the best way. And actually,
`05:02` time, the best way. And actually, skills, while they upload and use
`05:04` skills, while they upload and use
`05:04` skills, while they upload and use tokens, can often save you tokens
`05:06` tokens, can often save you tokens
`05:06` tokens, can often save you tokens downstream if from it making errors or
`05:09` downstream if from it making errors or
`05:09` downstream if from it making errors or just getting you the best area. But
`05:10` just getting you the best area. But
`05:10` just getting you the best area. But right? So, if I hit use, boom, it adds
`05:12` right? So, if I hit use, boom, it adds
`05:12` right? So, if I hit use, boom, it adds that in there. All of these are just
`05:14` that in there. All of these are just
`05:14` that in there. All of these are just markdown documents, ideas, right? Create
`05:16` markdown documents, ideas, right? Create
`05:16` markdown documents, ideas, right? Create an animated video for this. Now, there
`05:18` an animated video for this. Now, there
`05:18` an animated video for this. Now, there is a lot more behind the skill that
`05:20` is a lot more behind the skill that
`05:20` is a lot more behind the skill that they're not showing there. If you were
`05:22` they're not showing there. If you were
`05:22` they're not showing there. If you were to actually lay this skill out, it looks
`05:24` to actually lay this skill out, it looks
`05:24` to actually lay this skill out, it looks like something else. I actually had
`05:26` like something else. I actually had
`05:26` like something else. I actually had Claude design create a design for that
`05:30` Claude design create a design for that
`05:30` Claude design create a design for that skill. I believe it was No, it was this
`05:33` skill. I believe it was No, it was this
`05:33` skill. I believe it was No, it was this test. And I was basically, "Hey, go
`05:36` test. And I was basically, "Hey, go
`05:36` test. And I was basically, "Hey, go ahead and create a page that explains
`05:39` ahead and create a page that explains
`05:39` ahead and create a page that explains your animated video skill." And it
`05:40` your animated video skill." And it
`05:40` your animated video skill." And it immediately did that for me, which is
`05:43` immediately did that for me, which is
`05:43` immediately did that for me, which is See if it's going to open up. There we
`05:45` See if it's going to open up. There we
`05:45` See if it's going to open up. There we go. And really beautiful, explained,
`05:47` go. And really beautiful, explained,
`05:47` go. And really beautiful, explained, "Hey, this skill basically turns things
`05:49` "Hey, this skill basically turns things
`05:49` "Hey, this skill basically turns things into a contained HTML page and breaks it
`05:52` into a contained HTML page and breaks it
`05:52` into a contained HTML page and breaks it down." And it makes frames for the
`05:54` down." And it makes frames for the
`05:54` down." And it makes frames for the animations, and it gives them examples
`05:56` animations, and it gives them examples
`05:56` animations, and it gives them examples of how to stage it, how to handle
`05:58` of how to stage it, how to handle
`05:58` of how to stage it, how to handle sprites, how to handle entry and exit
`06:00` sprites, how to handle entry and exit
`06:00` sprites, how to handle entry and exit times. Again, these are explanations of
`06:02` times. Again, these are explanations of
`06:02` times. Again, these are explanations of how to create a process. And those are
`06:04` how to create a process. And those are
`06:04` how to create a process. And those are what skills are at the end. Uh
`06:06` what skills are at the end. Uh
`06:07` what skills are at the end. Uh hopefully, for those of you who already
`06:08` hopefully, for those of you who already
`06:08` hopefully, for those of you who already understand skills, this wasn't annoying
`06:10` understand skills, this wasn't annoying
`06:10` understand skills, this wasn't annoying or boring. But that's important to know
`06:12` or boring. But that's important to know
`06:12` or boring. But that's important to know because design system Claude design is
`06:14` because design system Claude design is
`06:14` because design system Claude design is built entirely around organizing skills,
`06:17` built entirely around organizing skills,
`06:17` built entirely around organizing skills, organizing folders, and organizing
`06:19` organizing folders, and organizing
`06:19` organizing folders, and organizing components. Well, I have some older
`06:21` components. Well, I have some older
`06:21` components. Well, I have some older videos where I was doing this I think
`06:23` videos where I was doing this I think
`06:23` videos where I was doing this I think two or three months ago with my
`06:24` two or three months ago with my
`06:24` two or three months ago with my animations. Maybe I'll link it below or
`06:27` animations. Maybe I'll link it below or
`06:27` animations. Maybe I'll link it below or link it right here, where essentially I
`06:29` link it right here, where essentially I
`06:29` link it right here, where essentially I talk about creating animations with
`06:31` talk about creating animations with
`06:31` talk about creating animations with Remotion and Claude, and that organizing
`06:33` Remotion and Claude, and that organizing
`06:33` Remotion and Claude, and that organizing it in a folder structure allows it to
`06:35` it in a folder structure allows it to
`06:35` it in a folder structure allows it to create much better animations and save
`06:37` create much better animations and save
`06:37` create much better animations and save tokens. But we'll get to that here in a
`06:39` tokens. But we'll get to that here in a
`06:40` tokens. But we'll get to that here in a moment. Now, when you actually come in
`06:42` moment. Now, when you actually come in
`06:42` moment. Now, when you actually come in here, uh and you go and create this
`06:44` here, uh and you go and create this
`06:44` here, uh and you go and create this project, right? And you selected those.
`06:46` project, right? And you selected those.
`06:46` project, right? And you selected those. What you can actually do is import
`06:48` What you can actually do is import
`06:48` What you can actually do is import directly from GitHub, and I have my
`06:51` directly from GitHub, and I have my
`06:51` directly from GitHub, and I have my GitHub directly at connected. You can
`06:52` GitHub directly at connected. You can
`06:52` GitHub directly at connected. You can import Figma files, which is what I was
`06:54` import Figma files, which is what I was
`06:54` import Figma files, which is what I was just showing here. Or you can import
`06:57` just showing here. Or you can import
`06:57` just showing here. Or you can import just link a folder that you have on your
`06:58` just link a folder that you have on your
`06:58` just link a folder that you have on your desktop. So, if you've already designed
`07:00` desktop. So, if you've already designed
`07:00` desktop. So, if you've already designed a whole bunch of stuff, what I did for a
`07:02` a whole bunch of stuff, what I did for a
`07:02` a whole bunch of stuff, what I did for a prior video is not this one, but was
`07:05` prior video is not this one, but was
`07:05` prior video is not this one, but was actually for these. I already had been
`07:07` actually for these. I already had been
`07:07` actually for these. I already had been building animated videos for a client,
`07:09` building animated videos for a client,
`07:09` building animated videos for a client, and I already had a large code base with
`07:12` and I already had a large code base with
`07:12` and I already had a large code base with those videos and those aspects, right?
`07:15` those videos and those aspects, right?
`07:15` those videos and those aspects, right? So, if this is my
`07:17` So, if this is my
`07:17` So, if this is my local version of Claude design is a good
`07:19` local version of Claude design is a good
`07:19` local version of Claude design is a good way to look at it. I'm able to take my
`07:21` way to look at it. I'm able to take my
`07:21` way to look at it. I'm able to take my scripts and turn them into animations,
`07:23` scripts and turn them into animations,
`07:23` scripts and turn them into animations, and I'm able to organize them all. I
`07:25` and I'm able to organize them all. I
`07:25` and I'm able to organize them all. I already had component libraries. I had
`07:27` already had component libraries. I had
`07:27` already had component libraries. I had areas where you were able to come in and
`07:28` areas where you were able to come in and
`07:28` areas where you were able to come in and look at them. So, I think uh it was
`07:30` look at them. So, I think uh it was
`07:31` look at them. So, I think uh it was under this one right here. So, this was
`07:33` under this one right here. So, this was
`07:33` under this one right here. So, this was what uh a scene I had already created,
`07:36` what uh a scene I had already created,
`07:36` what uh a scene I had already created, except instead of using just HTML, I had
`07:38` except instead of using just HTML, I had
`07:38` except instead of using just HTML, I had used uh JavaScript and uh React
`07:41` used uh JavaScript and uh React
`07:41` used uh JavaScript and uh React essentially. Same concept, just
`07:43` essentially. Same concept, just
`07:43` essentially. Same concept, just different code. And this created various
`07:45` different code. And this created various
`07:45` different code. And this created various scenes for me to create an animated
`07:47` scenes for me to create an animated
`07:47` scenes for me to create an animated video, and Claude can read them, and so
`07:49` video, and Claude can read them, and so
`07:49` video, and Claude can read them, and so on. And if you really want to understand
`07:50` on. And if you really want to understand
`07:50` on. And if you really want to understand more about my folder structure, and you
`07:52` more about my folder structure, and you
`07:52` more about my folder structure, and you haven't already watched some of my
`07:54` haven't already watched some of my
`07:54` haven't already watched some of my previous videos, highly recommend it. I
`07:56` previous videos, highly recommend it. I
`07:56` previous videos, highly recommend it. I talk about building local folder
`07:57` talk about building local folder
`07:57` talk about building local folder structure and routing logic for Claude
`08:00` structure and routing logic for Claude
`08:00` structure and routing logic for Claude code or Codex or Gemini. Any agent that
`08:03` code or Codex or Gemini. Any agent that
`08:03` code or Codex or Gemini. Any agent that can read files can use this uh kind of
`08:05` can read files can use this uh kind of
`08:05` can read files can use this uh kind of context. It allows you to be a lot more
`08:07` context. It allows you to be a lot more
`08:07` context. It allows you to be a lot more agent agnostic. But anyway, I had
`08:09` agent agnostic. But anyway, I had
`08:09` agent agnostic. But anyway, I had already had this code base, so I just I
`08:11` already had this code base, so I just I
`08:11` already had this code base, so I just I didn't pull this whole code base in, but
`08:13` didn't pull this whole code base in, but
`08:13` didn't pull this whole code base in, but I went in, I found the animations that I
`08:15` I went in, I found the animations that I
`08:15` I went in, I found the animations that I liked from these videos, and I tossed it
`08:17` liked from these videos, and I tossed it
`08:17` liked from these videos, and I tossed it in there, and it was able to copy videos
`08:19` in there, and it was able to copy videos
`08:19` in there, and it was able to copy videos almost frame for frame, and then I could
`08:21` almost frame for frame, and then I could
`08:21` almost frame for frame, and then I could rebuild inside of it with new info. So,
`08:24` rebuild inside of it with new info. So,
`08:24` rebuild inside of it with new info. So, I uploaded a PowerPoint that had more
`08:26` I uploaded a PowerPoint that had more
`08:26` I uploaded a PowerPoint that had more brand assets in it, and I walked through
`08:28` brand assets in it, and I walked through
`08:28` brand assets in it, and I walked through and talked about it what I wanted, what
`08:30` and talked about it what I wanted, what
`08:30` and talked about it what I wanted, what those videos were. I even created a
`08:32` those videos were. I even created a
`08:32` those videos were. I even created a series of scripts and frames
`08:34` series of scripts and frames
`08:34` series of scripts and frames specifically around how I wanted the
`08:36` specifically around how I wanted the
`08:36` specifically around how I wanted the videos, and just pasted in. I said it a
`08:38` videos, and just pasted in. I said it a
`08:38` videos, and just pasted in. I said it a much more complicated version of this,
`08:40` much more complicated version of this,
`08:40` much more complicated version of this, "Based on all of those design templates,
`08:45` "Based on all of those design templates,
`08:45` "Based on all of those design templates, I need a video that does this based on
`08:48` I need a video that does this based on
`08:48` I need a video that does this based on this script." And oops. Imagine that
`08:53` this script." And oops. Imagine that
`08:53` this script." And oops. Imagine that I need a video that does this. Imagine
`08:55` I need a video that does this. Imagine
`08:55` I need a video that does this. Imagine this is a large prompt in itself, me
`08:57` this is a large prompt in itself, me
`08:57` this is a large prompt in itself, me describing what that video is based on
`09:00` describing what that video is based on
`09:00` describing what that video is based on this script. And then there's another
`09:02` this script. And then there's another
`09:02` this script. And then there's another file that has that script. And you can
`09:04` file that has that script. And you can
`09:04` file that has that script. And you can actually store those locally in here.
`09:06` actually store those locally in here.
`09:07` actually store those locally in here. Let me see if it'll let me I think this
`09:10` Let me see if it'll let me I think this
`09:10` Let me see if it'll let me I think this uh being at full screen makes this
`09:11` uh being at full screen makes this
`09:11` uh being at full screen makes this awkward. Let me come here. And so, you
`09:13` awkward. Let me come here. And so, you
`09:13` awkward. Let me come here. And so, you can see, Claude Anthropic is using a
`09:15` can see, Claude Anthropic is using a
`09:15` can see, Claude Anthropic is using a very similar folder structure than what
`09:17` very similar folder structure than what
`09:17` very similar folder structure than what I'm doing, and I guarantee you behind
`09:18` I'm doing, and I guarantee you behind
`09:18` I'm doing, and I guarantee you behind the scenes, it's very similar routing.
`09:20` the scenes, it's very similar routing.
`09:20` the scenes, it's very similar routing. And from there, it pulled in those
`09:22` And from there, it pulled in those
`09:22` And from there, it pulled in those components, those processes. It created
`09:24` components, those processes. It created
`09:24` components, those processes. It created themes out of those, and organized it.
`09:26` themes out of those, and organized it.
`09:26` themes out of those, and organized it. And these are my uploads. These are
`09:28` And these are my uploads. These are
`09:28` And these are my uploads. These are updates I'm working with an amazing
`09:30` updates I'm working with an amazing
`09:30` updates I'm working with an amazing company, NLP Logics. They're a machine
`09:32` company, NLP Logics. They're a machine
`09:32` company, NLP Logics. They're a machine learning company. Your guys are going to
`09:33` learning company. Your guys are going to
`09:33` learning company. Your guys are going to hear about them more if you're in my
`09:34` hear about them more if you're in my
`09:34` hear about them more if you're in my community. They're going to come in and
`09:35` community. They're going to come in and
`09:36` community. They're going to come in and talk. They've been doing machine
`09:37` talk. They've been doing machine
`09:37` talk. They've been doing machine learning since 2010. Love working with
`09:39` learning since 2010. Love working with
`09:39` learning since 2010. Love working with them. They are an awesome company. But
`09:41` them. They are an awesome company. But
`09:41` them. They are an awesome company. But they basically gave me PDFs, which I
`09:43` they basically gave me PDFs, which I
`09:43` they basically gave me PDFs, which I can't share because we have some, you
`09:45` can't share because we have some, you
`09:45` can't share because we have some, you know, important data that can't be out
`09:46` know, important data that can't be out
`09:46` know, important data that can't be out there like that. But a huge update on
`09:48` there like that. But a huge update on
`09:48` there like that. But a huge update on their finances, on what they're doing,
`09:50` their finances, on what they're doing,
`09:50` their finances, on what they're doing, where their work is, what they're trying
`09:51` where their work is, what they're trying
`09:51` where their work is, what they're trying to share. And this allows me to organize
`09:53` to share. And this allows me to organize
`09:53` to share. And this allows me to organize it a lot better. This could be the the
`09:55` it a lot better. This could be the the
`09:55` it a lot better. This could be the the for your company. If you have updates,
`09:57` for your company. If you have updates,
`09:57` for your company. If you have updates, PDFs, things, those can be contacts and
`09:59` PDFs, things, those can be contacts and
`09:59` PDFs, things, those can be contacts and ideas for your agents. Not just in
`10:02` ideas for your agents. Not just in
`10:02` ideas for your agents. Not just in design folders, but across any sort of
`10:05` design folders, but across any sort of
`10:05` design folders, but across any sort of flow. The idea is you're creating data
`10:07` flow. The idea is you're creating data
`10:07` flow. The idea is you're creating data in which the AI can build and expand off
`10:10` in which the AI can build and expand off
`10:10` in which the AI can build and expand off of. The better the core data it starts
`10:12` of. The better the core data it starts
`10:12` of. The better the core data it starts with, the more organized the data is,
`10:15` with, the more organized the data is,
`10:15` with, the more organized the data is, the easier it is for the AI to create
`10:16` the easier it is for the AI to create
`10:16` the easier it is for the AI to create what you want, what your alignment out
`10:19` what you want, what your alignment out
`10:19` what you want, what your alignment out of it is. But, anyway,
`10:21` of it is. But, anyway,
`10:21` of it is. But, anyway, that's something that I did there really
`10:22` that's something that I did there really
`10:22` that's something that I did there really great. But, what you really want to do,
`10:25` great. But, what you really want to do,
`10:25` great. But, what you really want to do, if you were starting from scratch and
`10:26` if you were starting from scratch and
`10:26` if you were starting from scratch and you were just diving in, what you
`10:28` you were just diving in, what you
`10:28` you were just diving in, what you actually want to go through, and if you
`10:29` actually want to go through, and if you
`10:30` actually want to go through, and if you know you're going to be using a system
`10:31` know you're going to be using a system
`10:31` know you're going to be using a system like this or you want to have a really
`10:33` like this or you want to have a really
`10:33` like this or you want to have a really core design system that AI can use well,
`10:35` core design system that AI can use well,
`10:35` core design system that AI can use well, you can actually come over here and you
`10:38` you can actually come over here and you
`10:38` you can actually come over here and you can look at examples of what people have
`10:39` can look at examples of what people have
`10:39` can look at examples of what people have done and how they've done it. And these
`10:41` done and how they've done it. And these
`10:41` done and how they've done it. And these are cool, but I'm going to be honest
`10:42` are cool, but I'm going to be honest
`10:42` are cool, but I'm going to be honest with you, they're very basic. They're
`10:43` with you, they're very basic. They're
`10:44` with you, they're very basic. They're just kind of cool stuff. They're not
`10:45` just kind of cool stuff. They're not
`10:45` just kind of cool stuff. They're not compiled together for business outcomes.
`10:48` compiled together for business outcomes.
`10:48` compiled together for business outcomes. You want to have repeatable processes
`10:50` You want to have repeatable processes
`10:50` You want to have repeatable processes that allow you to support a business
`10:52` that allow you to support a business
`10:52` that allow you to support a business outcome like creating slide decks
`10:54` outcome like creating slide decks
`10:54` outcome like creating slide decks because you get paid for it or
`10:56` because you get paid for it or
`10:57` because you get paid for it or maybe working together and creating
`10:58` maybe working together and creating
`10:58` maybe working together and creating animated videos that support your
`11:00` animated videos that support your
`11:00` animated videos that support your YouTube channel so that gets more
`11:01` YouTube channel so that gets more
`11:01` YouTube channel so that gets more marketing or if think of a thousand
`11:03` marketing or if think of a thousand
`11:03` marketing or if think of a thousand things, maybe even internal documents,
`11:05` things, maybe even internal documents,
`11:05` things, maybe even internal documents, making it easier to share internal
`11:07` making it easier to share internal
`11:07` making it easier to share internal documents.
`11:08` documents.
`11:08` documents. Well, you want to actually build your
`11:10` Well, you want to actually build your
`11:10` Well, you want to actually build your own design system. Now, it's immediately
`11:12` own design system. Now, it's immediately
`11:12` own design system. Now, it's immediately going to look a little complicated when
`11:13` going to look a little complicated when
`11:13` going to look a little complicated when you come in, right? Let me go back
`11:14` you come in, right? Let me go back
`11:15` you come in, right? Let me go back through this. You You're in Claude
`11:16` through this. You You're in Claude
`11:16` through this. You You're in Claude design, you come to design systems, you
`11:19` design, you come to design systems, you
`11:19` design, you come to design systems, you can come over and you can actually hit
`11:21` can come over and you can actually hit
`11:21` can come over and you can actually hit create new design. You probably won't
`11:22` create new design. You probably won't
`11:22` create new design. You probably won't see any of these here, right? And I'm
`11:24` see any of these here, right? And I'm
`11:24` see any of these here, right? And I'm going to have probably a hundred messing
`11:26` going to have probably a hundred messing
`11:26` going to have probably a hundred messing around with this in the next month, but
`11:27` around with this in the next month, but
`11:27` around with this in the next month, but we'll see how much usage I can get out
`11:28` we'll see how much usage I can get out
`11:28` we'll see how much usage I can get out of it.
`11:29` of it.
`11:29` of it. But, you can hit create. When you hit
`11:31` But, you can hit create. When you hit
`11:31` But, you can hit create. When you hit create, you can talk about your company,
`11:34` create, you can talk about your company,
`11:34` create, you can talk about your company, what it is, the name there. I actually
`11:35` what it is, the name there. I actually
`11:35` what it is, the name there. I actually just skipped that entirely and this is,
`11:38` just skipped that entirely and this is,
`11:38` just skipped that entirely and this is, again, a series of components and
`11:40` again, a series of components and
`11:40` again, a series of components and branding. It's a more complicated
`11:41` branding. It's a more complicated
`11:41` branding. It's a more complicated version of Figma files or Canva, right?
`11:43` version of Figma files or Canva, right?
`11:44` version of Figma files or Canva, right? We have the actual
`11:45` We have the actual
`11:45` We have the actual codebase of all of these. And I'm
`11:47` codebase of all of these. And I'm
`11:47` codebase of all of these. And I'm actually going to create a new design
`11:48` actually going to create a new design
`11:48` actually going to create a new design system cuz this is a cleaned-up one that
`11:50` system cuz this is a cleaned-up one that
`11:50` system cuz this is a cleaned-up one that we took from our original codebase that
`11:52` we took from our original codebase that
`11:52` we took from our original codebase that I used to create a brand system designed
`11:55` I used to create a brand system designed
`11:55` I used to create a brand system designed specifically for Claude to read and look
`11:58` specifically for Claude to read and look
`11:58` specifically for Claude to read and look at around our brand because we realized
`12:00` at around our brand because we realized
`12:00` at around our brand because we realized that that would make it way more
`12:01` that that would make it way more
`12:01` that that would make it way more efficient and it would use a lot less
`12:03` efficient and it would use a lot less
`12:03` efficient and it would use a lot less tokens. So, I can actually come in and
`12:05` tokens. So, I can actually come in and
`12:05` tokens. So, I can actually come in and just link that GitHub here. And I can
`12:07` just link that GitHub here. And I can
`12:07` just link that GitHub here. And I can hit add. Now, you're going to need to
`12:09` hit add. Now, you're going to need to
`12:09` hit add. Now, you're going to need to connect your GitHub, if you have a
`12:11` connect your GitHub, if you have a
`12:12` connect your GitHub, if you have a GitHub page, to it to give it access,
`12:14` GitHub page, to it to give it access,
`12:14` GitHub page, to it to give it access, but it's as simple as just it'll say
`12:15` but it's as simple as just it'll say
`12:15` but it's as simple as just it'll say connect right here and you'll just log
`12:17` connect right here and you'll just log
`12:17` connect right here and you'll just log in through GitHub, just normal process
`12:19` in through GitHub, just normal process
`12:19` in through GitHub, just normal process there. If you're not doing that, you can
`12:21` there. If you're not doing that, you can
`12:21` there. If you're not doing that, you can just drag a folder from your computer.
`12:23` just drag a folder from your computer.
`12:23` just drag a folder from your computer. So, if you download your codebase or
`12:26` So, if you download your codebase or
`12:26` So, if you download your codebase or whatever it is that has your assets, you
`12:27` whatever it is that has your assets, you
`12:27` whatever it is that has your assets, you can just upload it. Again, you can
`12:29` can just upload it. Again, you can
`12:29` can just upload it. Again, you can download a Figma file, right? Come in,
`12:31` download a Figma file, right? Come in,
`12:31` download a Figma file, right? Come in, and this is what's cool is that you can
`12:34` and this is what's cool is that you can
`12:34` and this is what's cool is that you can spend the time in Figma. Figma's not
`12:35` spend the time in Figma. Figma's not
`12:35` spend the time in Figma. Figma's not useless anymore. Everyone's like, "Oh,
`12:37` useless anymore. Everyone's like, "Oh,
`12:37` useless anymore. Everyone's like, "Oh, Figma's gone." Now, I get to come in and
`12:39` Figma's gone." Now, I get to come in and
`12:39` Figma's gone." Now, I get to come in and design exactly what I want down to the
`12:41` design exactly what I want down to the
`12:41` design exactly what I want down to the very specific thing. This is my older
`12:43` very specific thing. This is my older
`12:43` very specific thing. This is my older brand. We're not like this anymore, but
`12:44` brand. We're not like this anymore, but
`12:45` brand. We're not like this anymore, but I get to be the person that I want my
`12:46` I get to be the person that I want my
`12:46` I get to be the person that I want my design. Then, this design can then be
`12:49` design. Then, this design can then be
`12:49` design. Then, this design can then be downloaded and amplified exponentially
`12:53` downloaded and amplified exponentially
`12:53` downloaded and amplified exponentially by some systems like this. And that's
`12:54` by some systems like this. And that's
`12:54` by some systems like this. And that's where the real value is. You want to go
`12:56` where the real value is. You want to go
`12:56` where the real value is. You want to go in and spend the time making your first
`12:58` in and spend the time making your first
`12:58` in and spend the time making your first draft perfect, exactly what you want.
`13:00` draft perfect, exactly what you want.
`13:01` draft perfect, exactly what you want. All the assets are exactly how you want
`13:02` All the assets are exactly how you want
`13:02` All the assets are exactly how you want it. Then, you give it to this tool
`13:04` it. Then, you give it to this tool
`13:04` it. Then, you give it to this tool system. You do the creative process and
`13:06` system. You do the creative process and
`13:06` system. You do the creative process and it will amplify it into all the
`13:08` it will amplify it into all the
`13:08` it will amplify it into all the different versions that you want, which
`13:10` different versions that you want, which
`13:10` different versions that you want, which you'll see here. You can add fonts, you
`13:12` you'll see here. You can add fonts, you
`13:12` you'll see here. You can add fonts, you can add Figma files. In fact, I think a
`13:14` can add Figma files. In fact, I think a
`13:14` can add Figma files. In fact, I think a designer, someone who's been a designer,
`13:16` designer, someone who's been a designer,
`13:16` designer, someone who's been a designer, will use Claude design better than
`13:17` will use Claude design better than
`13:17` will use Claude design better than almost anyone else. But, if you don't
`13:18` almost anyone else. But, if you don't
`13:19` almost anyone else. But, if you don't have a design background, that's okay.
`13:20` have a design background, that's okay.
`13:20` have a design background, that's okay. You can still throw this stuff in there.
`13:22` You can still throw this stuff in there.
`13:22` You can still throw this stuff in there. You can also add some notes, maybe some
`13:24` You can also add some notes, maybe some
`13:24` You can also add some notes, maybe some nuance there, but again, just to show
`13:25` nuance there, but again, just to show
`13:25` nuance there, but again, just to show you the power of this, I'm just throwing
`13:27` you the power of this, I'm just throwing
`13:27` you the power of this, I'm just throwing my GitHub library in here.
`13:29` my GitHub library in here.
`13:29` my GitHub library in here. I'm going to go ahead and hit generate.
`13:31` I'm going to go ahead and hit generate.
`13:31` I'm going to go ahead and hit generate. Now, it does take some time, so I'm not
`13:34` Now, it does take some time, so I'm not
`13:34` Now, it does take some time, so I'm not going to make you wait. I know that my
`13:36` going to make you wait. I know that my
`13:36` going to make you wait. I know that my GitHub is going to take a lot longer
`13:37` GitHub is going to take a lot longer
`13:37` GitHub is going to take a lot longer than 5 minutes because of how much we
`13:39` than 5 minutes because of how much we
`13:39` than 5 minutes because of how much we have, but let me explain to you while it
`13:41` have, but let me explain to you while it
`13:41` have, but let me explain to you while it is doing this. Don't worry, I'm going to
`13:43` is doing this. Don't worry, I'm going to
`13:43` is doing this. Don't worry, I'm going to cut here shortly. It's going to
`13:44` cut here shortly. It's going to
`13:44` cut here shortly. It's going to immediately explore that GitHub. And so,
`13:47` immediately explore that GitHub. And so,
`13:47` immediately explore that GitHub. And so, what it's going through is it's read me,
`13:48` what it's going through is it's read me,
`13:48` what it's going through is it's read me, it's understanding the fundamentals,
`13:50` it's understanding the fundamentals,
`13:50` it's understanding the fundamentals, it's going through and it's seeing the
`13:52` it's going through and it's seeing the
`13:52` it's going through and it's seeing the files that we have. Oh, you have assets
`13:54` files that we have. Oh, you have assets
`13:54` files that we have. Oh, you have assets and SVGs. What does that SVG look like?
`13:56` and SVGs. What does that SVG look like?
`13:56` and SVGs. What does that SVG look like? What is it there? Oh, it's this little
`13:58` What is it there? Oh, it's this little
`13:58` What is it there? Oh, it's this little corner thing that we use, right? The
`13:59` corner thing that we use, right? The
`13:59` corner thing that we use, right? The more specific you can get with your
`14:02` more specific you can get with your
`14:02` more specific you can get with your codebase on assets that you like, that
`14:04` codebase on assets that you like, that
`14:04` codebase on assets that you like, that is your brand, and this is huge for
`14:06` is your brand, and this is huge for
`14:06` is your brand, and this is huge for enterprise companies, the better Claude
`14:08` enterprise companies, the better Claude
`14:09` enterprise companies, the better Claude will be able to generate something from
`14:10` will be able to generate something from
`14:10` will be able to generate something from this. Maybe we have animations that
`14:12` this. Maybe we have animations that
`14:12` this. Maybe we have animations that we're using on our website. Let me see
`14:14` we're using on our website. Let me see
`14:14` we're using on our website. Let me see if I actually have an example of this
`14:15` if I actually have an example of this
`14:15` if I actually have an example of this that I can throw for you real quick. And
`14:17` that I can throw for you real quick. And
`14:17` that I can throw for you real quick. And so, we're cleaning up this front one.
`14:19` so, we're cleaning up this front one.
`14:19` so, we're cleaning up this front one. This is an old placeholder right now,
`14:20` This is an old placeholder right now,
`14:20` This is an old placeholder right now, don't worry about that. But, the idea
`14:21` don't worry about that. But, the idea
`14:21` don't worry about that. But, the idea is, right? See those small little
`14:23` is, right? See those small little
`14:23` is, right? See those small little animations in there? We hand-coded
`14:25` animations in there? We hand-coded
`14:25` animations in there? We hand-coded those, right? We wanted those to be
`14:27` those, right? We wanted those to be
`14:27` those, right? We wanted those to be there for very specific reason. We're
`14:28` there for very specific reason. We're
`14:28` there for very specific reason. We're affecting the spacing. The spacing isn't
`14:30` affecting the spacing. The spacing isn't
`14:30` affecting the spacing. The spacing isn't right. But, this idea So, you see you
`14:32` right. But, this idea So, you see you
`14:32` right. But, this idea So, you see you can see folder structure and the idea
`14:34` can see folder structure and the idea
`14:34` can see folder structure and the idea behind folder structures is very much
`14:36` behind folder structures is very much
`14:36` behind folder structures is very much here. I figured that would be cool to
`14:37` here. I figured that would be cool to
`14:37` here. I figured that would be cool to add into our website since it's such a
`14:39` add into our website since it's such a
`14:39` add into our website since it's such a big part of it. But, like all of these
`14:41` big part of it. But, like all of these
`14:41` big part of it. But, like all of these are things that can grow. They can be
`14:43` are things that can grow. They can be
`14:43` are things that can grow. They can be components and processes that we
`14:45` components and processes that we
`14:45` components and processes that we actually are able to incorporate. And
`14:48` actually are able to incorporate. And
`14:48` actually are able to incorporate. And so, we can take all these assets and
`14:50` so, we can take all these assets and
`14:50` so, we can take all these assets and reuse them in a thousand different ways
`14:52` reuse them in a thousand different ways
`14:52` reuse them in a thousand different ways if we compile them somewhere, which is
`14:54` if we compile them somewhere, which is
`14:54` if we compile them somewhere, which is exactly what we did in our GitHub, um
`14:57` exactly what we did in our GitHub, um
`14:57` exactly what we did in our GitHub, um which I think is cool. So, it become our
`14:58` which I think is cool. So, it become our
`14:58` which I think is cool. So, it become our websites that we've built, the things
`15:00` websites that we've built, the things
`15:00` websites that we've built, the things that we've already spent time on, become
`15:02` that we've already spent time on, become
`15:02` that we've already spent time on, become an asset to then amplify our future
`15:04` an asset to then amplify our future
`15:04` an asset to then amplify our future work. Uh and that's exactly what it's
`15:06` work. Uh and that's exactly what it's
`15:06` work. Uh and that's exactly what it's going to go through. It's going to read
`15:08` going to go through. It's going to read
`15:08` going to go through. It's going to read all the JSX. This is why it used so many
`15:10` all the JSX. This is why it used so many
`15:10` all the JSX. This is why it used so many tokens because it is navigating all of
`15:13` tokens because it is navigating all of
`15:13` tokens because it is navigating all of the files deeply. It's using
`15:15` the files deeply. It's using
`15:15` the files deeply. It's using Essentially, it's Claude code behind the
`15:17` Essentially, it's Claude code behind the
`15:17` Essentially, it's Claude code behind the scenes with a series of good routing, uh
`15:20` scenes with a series of good routing, uh
`15:20` scenes with a series of good routing, uh a series of good tool calls, the ability
`15:22` a series of good tool calls, the ability
`15:22` a series of good tool calls, the ability to use GitHub files, to use the GitHub
`15:24` to use GitHub files, to use the GitHub
`15:25` to use GitHub files, to use the GitHub CLI. It's actually going through and
`15:27` CLI. It's actually going through and
`15:27` CLI. It's actually going through and listing any other repos that might be
`15:28` listing any other repos that might be
`15:28` listing any other repos that might be connected to it. Uh and it's reading
`15:30` connected to it. Uh and it's reading
`15:31` connected to it. Uh and it's reading every single file. And while it's taking
`15:32` every single file. And while it's taking
`15:32` every single file. And while it's taking these, it's taking notes. It's adding
`15:35` these, it's taking notes. It's adding
`15:35` these, it's taking notes. It's adding each of these to its own design folder
`15:37` each of these to its own design folder
`15:37` each of these to its own design folder that it thinks are important. So, it's
`15:38` that it thinks are important. So, it's
`15:38` that it thinks are important. So, it's actually going to skip a lot of the
`15:41` actually going to skip a lot of the
`15:41` actually going to skip a lot of the files that maybe aren't as important to
`15:45` files that maybe aren't as important to
`15:45` files that maybe aren't as important to what we're building here, right? So,
`15:46` what we're building here, right? So,
`15:46` what we're building here, right? So, there might be uh certain preview files
`15:49` there might be uh certain preview files
`15:49` there might be uh certain preview files that aren't useful, might not be what we
`15:51` that aren't useful, might not be what we
`15:51` that aren't useful, might not be what we want. And it's actually deciding which
`15:53` want. And it's actually deciding which
`15:53` want. And it's actually deciding which ones to ignore or vice versa. If you
`15:55` ones to ignore or vice versa. If you
`15:55` ones to ignore or vice versa. If you uploaded a slide, these are super old.
`15:57` uploaded a slide, these are super old.
`15:57` uploaded a slide, these are super old. This is years ago, so please ignore
`15:59` This is years ago, so please ignore
`15:59` This is years ago, so please ignore these. These were when I was testing
`16:01` these. These were when I was testing
`16:01` these. These were when I was testing with AI at earlier versions. This is
`16:03` with AI at earlier versions. This is
`16:03` with AI at earlier versions. This is like 2 or 3 years ago when I was trying
`16:04` like 2 or 3 years ago when I was trying
`16:04` like 2 or 3 years ago when I was trying to get uh GPT-3 to build slides for me.
`16:07` to get uh GPT-3 to build slides for me.
`16:07` to get uh GPT-3 to build slides for me. Which at time, this was next level that
`16:09` Which at time, this was next level that
`16:09` Which at time, this was next level that it could even generate a slide, which is
`16:10` it could even generate a slide, which is
`16:10` it could even generate a slide, which is crazy to think that 3 years ago this was
`16:12` crazy to think that 3 years ago this was
`16:12` crazy to think that 3 years ago this was crazy for AI to do. Uh we've moved so
`16:15` crazy for AI to do. Uh we've moved so
`16:15` crazy for AI to do. Uh we've moved so quickly, but it could take concepts from
`16:18` quickly, but it could take concepts from
`16:18` quickly, but it could take concepts from this, images from this and and
`16:19` this, images from this and and
`16:19` this, images from this and and sectionalize them away. I wouldn't use
`16:21` sectionalize them away. I wouldn't use
`16:21` sectionalize them away. I wouldn't use this cuz this is terrible compared to
`16:23` this cuz this is terrible compared to
`16:23` this cuz this is terrible compared to actual branding and processes, but the
`16:25` actual branding and processes, but the
`16:25` actual branding and processes, but the idea is there is it simplifies the
`16:28` idea is there is it simplifies the
`16:28` idea is there is it simplifies the process, right? It could pull from
`16:30` process, right? It could pull from
`16:30` process, right? It could pull from anything that you've already built in
`16:31` anything that you've already built in
`16:31` anything that you've already built in things.
`16:32` things.
`16:32` things. Funny enough, this is actually what K,
`16:34` Funny enough, this is actually what K,
`16:34` Funny enough, this is actually what K, my front-end developer, we were part of
`16:36` my front-end developer, we were part of
`16:36` my front-end developer, we were part of a a UK uh startup program when I was
`16:38` a a UK uh startup program when I was
`16:38` a a UK uh startup program when I was going to university there and we built
`16:40` going to university there and we built
`16:40` going to university there and we built an app called Sin Space as part of the
`16:42` an app called Sin Space as part of the
`16:42` an app called Sin Space as part of the competition, which was was funny.
`16:44` competition, which was was funny.
`16:44` competition, which was was funny. Um and this is a quick, man. If we had
`16:46` Um and this is a quick, man. If we had
`16:46` Um and this is a quick, man. If we had what the tools we had now back then, we
`16:48` what the tools we had now back then, we
`16:48` what the tools we had now back then, we could make such such great decks before.
`16:51` could make such such great decks before.
`16:51` could make such such great decks before. This was all built by hand uh back in
`16:53` This was all built by hand uh back in
`16:53` This was all built by hand uh back in the olden days before AI. Um but, I find
`16:56` the olden days before AI. Um but, I find
`16:56` the olden days before AI. Um but, I find that very funny.
`16:58` that very funny.
`16:58` that very funny. Anyway, and so that's what it's doing.
`16:59` Anyway, and so that's what it's doing.
`16:59` Anyway, and so that's what it's doing. And then it's also creating style
`17:01` And then it's also creating style
`17:01` And then it's also creating style sheets. And then it's creating its own
`17:03` sheets. And then it's creating its own
`17:03` sheets. And then it's creating its own skill documents. So, if we open this up,
`17:05` skill documents. So, if we open this up,
`17:05` skill documents. So, if we open this up, we can see it's designed This is a skill
`17:07` we can see it's designed This is a skill
`17:07` we can see it's designed This is a skill for Aduba's design. Use this skill to
`17:10` for Aduba's design. Use this skill to
`17:10` for Aduba's design. Use this skill to generate branded references for Aduba,
`17:13` generate branded references for Aduba,
`17:13` generate branded references for Aduba, what we're doing. First of all, here's
`17:15` what we're doing. First of all, here's
`17:15` what we're doing. First of all, here's the routing. So, it's doing my routing
`17:17` the routing. So, it's doing my routing
`17:17` the routing. So, it's doing my routing process. My routing process is a little
`17:18` process. My routing process is a little
`17:18` process. My routing process is a little bit more complicated, so I'm probably
`17:20` bit more complicated, so I'm probably
`17:20` bit more complicated, so I'm probably going to clean up these files myself.
`17:22` going to clean up these files myself.
`17:22` going to clean up these files myself. But, it's the idea in my older videos,
`17:24` But, it's the idea in my older videos,
`17:24` But, it's the idea in my older videos, it's going through and it's saying,
`17:25` it's going through and it's saying,
`17:26` it's going through and it's saying, "Hey, here's some important files that
`17:27` "Hey, here's some important files that
`17:27` "Hey, here's some important files that you want to look about." Here's
`17:29` you want to look about." Here's
`17:29` you want to look about." Here's non-negotiables. It's deciding, "These
`17:31` non-negotiables. It's deciding, "These
`17:31` non-negotiables. It's deciding, "These are the main colors you need to use.
`17:32` are the main colors you need to use.
`17:32` are the main colors you need to use. These are the main ideas you need to
`17:34` These are the main ideas you need to
`17:34` These are the main ideas you need to So, it's a skill on how to use the
`17:36` So, it's a skill on how to use the
`17:36` So, it's a skill on how to use the design files that it's extracting, which
`17:39` design files that it's extracting, which
`17:39` design files that it's extracting, which is very useful. I used to have to do
`17:41` is very useful. I used to have to do
`17:41` is very useful. I used to have to do this manually, and I still do do it
`17:42` this manually, and I still do do it
`17:42` this manually, and I still do do it manually. That's kind of how I created
`17:45` manually. That's kind of how I created
`17:45` manually. That's kind of how I created my my previous animation sets, but
`17:47` my my previous animation sets, but
`17:47` my my previous animation sets, but that's exactly what it's doing. So,
`17:48` that's exactly what it's doing. So,
`17:48` that's exactly what it's doing. So, after it's done importing and
`17:50` after it's done importing and
`17:50` after it's done importing and understanding these, sometimes it
`17:52` understanding these, sometimes it
`17:52` understanding these, sometimes it imports some of them, so it doesn't have
`17:53` imports some of them, so it doesn't have
`17:53` imports some of them, so it doesn't have to recreate it, right? Because it's
`17:55` to recreate it, right? Because it's
`17:55` to recreate it, right? Because it's importing actual code, actual design
`17:57` importing actual code, actual design
`17:57` importing actual code, actual design methodology, and adding it to these
`18:00` methodology, and adding it to these
`18:00` methodology, and adding it to these folders. Again, it's all folders and
`18:02` folders. Again, it's all folders and
`18:02` folders. Again, it's all folders and text documents at the end of the day
`18:03` text documents at the end of the day
`18:03` text documents at the end of the day referencing
`18:09` code and components. That's All the best
`18:09` code and components. That's All the best AI systems out there are this, which
`18:11` AI systems out there are this, which
`18:11` AI systems out there are this, which means you can rebuild this locally,
`18:14` means you can rebuild this locally,
`18:14` means you can rebuild this locally, which I will share here more. I know I
`18:15` which I will share here more. I know I
`18:15` which I will share here more. I know I said I was going to skip ahead, but
`18:17` said I was going to skip ahead, but
`18:17` said I was going to skip ahead, but honestly, I figured I could teach pretty
`18:19` honestly, I figured I could teach pretty
`18:19` honestly, I figured I could teach pretty well while it's doing this. And it's
`18:20` well while it's doing this. And it's
`18:20` well while it's doing this. And it's adding extra HTML, so these ones it
`18:22` adding extra HTML, so these ones it
`18:22` adding extra HTML, so these ones it decided it wanted to recreate. And so,
`18:25` decided it wanted to recreate. And so,
`18:25` decided it wanted to recreate. And so, looks like previews, so that might be
`18:26` looks like previews, so that might be
`18:26` looks like previews, so that might be under UI kits. Uh possibly. No, these
`18:28` under UI kits. Uh possibly. No, these
`18:29` under UI kits. Uh possibly. No, these are other components. And that's the
`18:30` are other components. And that's the
`18:30` are other components. And that's the thing is I can come in and look and it's
`18:32` thing is I can come in and look and it's
`18:32` thing is I can come in and look and it's sharing and storing certain things that
`18:34` sharing and storing certain things that
`18:34` sharing and storing certain things that it thinks are there. It downloaded this
`18:35` it thinks are there. It downloaded this
`18:35` it thinks are there. It downloaded this directly from what we were looking at,
`18:37` directly from what we were looking at,
`18:38` directly from what we were looking at, but it doesn't have the animations,
`18:39` but it doesn't have the animations,
`18:39` but it doesn't have the animations, right? Because this is just the HTML
`18:41` right? Because this is just the HTML
`18:41` right? Because this is just the HTML code. So, it's able to organize it into
`18:44` code. So, it's able to organize it into
`18:44` code. So, it's able to organize it into structures to save tokens in the future.
`18:47` structures to save tokens in the future.
`18:47` structures to save tokens in the future. Right now, it's burning a lot of tokens,
`18:49` Right now, it's burning a lot of tokens,
`18:49` Right now, it's burning a lot of tokens, and that's what you want to understand.
`18:51` and that's what you want to understand.
`18:51` and that's what you want to understand. This
`18:52` This
`18:52` This is allowing using a lot of tokens all at
`18:55` is allowing using a lot of tokens all at
`18:55` is allowing using a lot of tokens all at once to organize everything for you. And
`18:57` once to organize everything for you. And
`18:57` once to organize everything for you. And then eventually, you're going to be able
`18:59` then eventually, you're going to be able
`18:59` then eventually, you're going to be able to actually export this, which I'll show
`19:01` to actually export this, which I'll show
`19:01` to actually export this, which I'll show you here in a moment. It can't
`19:03` you here in a moment. It can't
`19:03` you here in a moment. It can't the whole process. You can download this
`19:05` the whole process. You can download this
`19:05` the whole process. You can download this as a zip, bring it onto your local file,
`19:07` as a zip, bring it onto your local file,
`19:08` as a zip, bring it onto your local file, and you don't even need to use Claude.
`19:09` and you don't even need to use Claude.
`19:09` and you don't even need to use Claude. You could use Gemma or these local
`19:11` You could use Gemma or these local
`19:11` You could use Gemma or these local models, which I'll actually This is a
`19:13` models, which I'll actually This is a
`19:13` models, which I'll actually This is a good time to go over to now. We'll hit
`19:14` good time to go over to now. We'll hit
`19:14` good time to go over to now. We'll hit two birds with one stone.
`19:16` two birds with one stone.
`19:16` two birds with one stone. So, it creates this huge design system,
`19:18` So, it creates this huge design system,
`19:18` So, it creates this huge design system, and it's going through and I get to go
`19:20` and it's going through and I get to go
`19:20` and it's going through and I get to go and review it, right? And this is what
`19:22` and review it, right? And this is what
`19:22` and review it, right? And this is what it's doing right here. It's as it's
`19:23` it's doing right here. It's as it's
`19:23` it's doing right here. It's as it's going through this, I get to say, "Is
`19:25` going through this, I get to say, "Is
`19:25` going through this, I get to say, "Is that a good read me, right? Is this what
`19:27` that a good read me, right? Is this what
`19:27` that a good read me, right? Is this what Aduba represents?" Usually, I'd edit
`19:29` Aduba represents?" Usually, I'd edit
`19:29` Aduba represents?" Usually, I'd edit these, but let's just say it looks good.
`19:30` these, but let's just say it looks good.
`19:31` these, but let's just say it looks good. Then, are these my colors? Is this what
`19:32` Then, are these my colors? Is this what
`19:32` Then, are these my colors? Is this what I really wanted? Do we want to edit
`19:34` I really wanted? Do we want to edit
`19:34` I really wanted? Do we want to edit these? I can say needs work and readjust
`19:36` these? I can say needs work and readjust
`19:36` these? I can say needs work and readjust it. Again, the whole idea is you want to
`19:38` it. Again, the whole idea is you want to
`19:38` it. Again, the whole idea is you want to refine the starting data so that in the
`19:41` refine the starting data so that in the
`19:41` refine the starting data so that in the future, you never have to refine it
`19:43` future, you never have to refine it
`19:43` future, you never have to refine it again. We've got different aspects here.
`19:45` again. We've got different aspects here.
`19:45` again. We've got different aspects here. I'm going to go ahead and just smash
`19:46` I'm going to go ahead and just smash
`19:46` I'm going to go ahead and just smash looks good. I do think we are changing
`19:49` looks good. I do think we are changing
`19:49` looks good. I do think we are changing some of the typography and whatnot in
`19:50` some of the typography and whatnot in
`19:50` some of the typography and whatnot in this, but this is cool. This is just for
`19:52` this, but this is cool. This is just for
`19:52` this, but this is cool. This is just for all of you to see. It even talks about
`19:54` all of you to see. It even talks about
`19:54` all of you to see. It even talks about labeling, how we're actually setting up
`19:56` labeling, how we're actually setting up
`19:56` labeling, how we're actually setting up where our indexes, what are the pixels,
`19:58` where our indexes, what are the pixels,
`19:58` where our indexes, what are the pixels, how many how large should the font be,
`20:01` how many how large should the font be,
`20:01` how many how large should the font be, where should the font be in that. Type
`20:03` where should the font be in that. Type
`20:03` where should the font be in that. Type case rules, what that actual type case
`20:05` case rules, what that actual type case
`20:05` case rules, what that actual type case is. It's breaking down our brand from
`20:08` is. It's breaking down our brand from
`20:08` is. It's breaking down our brand from our websites, from our branding
`20:10` our websites, from our branding
`20:10` our websites, from our branding documents, and organizing it like a
`20:12` documents, and organizing it like a
`20:12` documents, and organizing it like a brand designer would. And here's the
`20:14` brand designer would. And here's the
`20:14` brand designer would. And here's the thing, if it as a brand designer, if you
`20:17` thing, if it as a brand designer, if you
`20:17` thing, if it as a brand designer, if you think this is taking your job, you need
`20:19` think this is taking your job, you need
`20:19` think this is taking your job, you need to take a step back. This just made you
`20:21` to take a step back. This just made you
`20:21` to take a step back. This just made you more valuable because you know how to
`20:23` more valuable because you know how to
`20:23` more valuable because you know how to guide this even more. And now you can do
`20:26` guide this even more. And now you can do
`20:26` guide this even more. And now you can do quadruple the work for the same amount
`20:28` quadruple the work for the same amount
`20:28` quadruple the work for the same amount of time. You can charge more as a
`20:30` of time. You can charge more as a
`20:30` of time. You can charge more as a freelance designer if you're using this
`20:32` freelance designer if you're using this
`20:32` freelance designer if you're using this tool and get high-quality non-AI slop.
`20:35` tool and get high-quality non-AI slop.
`20:35` tool and get high-quality non-AI slop. People are going to come to you because
`20:37` People are going to come to you because
`20:37` People are going to come to you because you can use this tool well. It's very
`20:39` you can use this tool well. It's very
`20:39` you can use this tool well. It's very important that you all understand this,
`20:41` important that you all understand this,
`20:41` important that you all understand this, right? And it's doing this well. Again,
`20:43` right? And it's doing this well. Again,
`20:43` right? And it's doing this well. Again, all of these assets were built by my
`20:45` all of these assets were built by my
`20:45` all of these assets were built by my designer, my partner, K, who's looking
`20:47` designer, my partner, K, who's looking
`20:47` designer, my partner, K, who's looking in this area. What's also cool and what
`20:49` in this area. What's also cool and what
`20:49` in this area. What's also cool and what I think uses a lot of tokens is what you
`20:51` I think uses a lot of tokens is what you
`20:51` I think uses a lot of tokens is what you see here. There's a little mini thing.
`20:53` see here. There's a little mini thing.
`20:53` see here. There's a little mini thing. It's actually going through and looking
`20:55` It's actually going through and looking
`20:55` It's actually going through and looking at them. It's taking screenshots of it
`20:57` at them. It's taking screenshots of it
`20:57` at them. It's taking screenshots of it right now. So, as it's coming through
`20:59` right now. So, as it's coming through
`20:59` right now. So, as it's coming through and it just finished, which is cool,
`21:01` and it just finished, which is cool,
`21:01` and it just finished, which is cool, it's verifying that everything looks
`21:03` it's verifying that everything looks
`21:03` it's verifying that everything looks good itself, that it all got in there,
`21:05` good itself, that it all got in there,
`21:05` good itself, that it all got in there, and noticing any issues, right? And so,
`21:07` and noticing any issues, right? And so,
`21:07` and noticing any issues, right? And so, I'm just going to go through and say all
`21:08` I'm just going to go through and say all
`21:08` I'm just going to go through and say all of this looks good. I'm very happy with
`21:10` of this looks good. I'm very happy with
`21:11` of this looks good. I'm very happy with it. It's it's solid and again, this is
`21:12` it. It's it's solid and again, this is
`21:12` it. It's it's solid and again, this is for use cases. And again, you can go
`21:14` for use cases. And again, you can go
`21:14` for use cases. And again, you can go back and oop, I didn't mean to like
`21:15` back and oop, I didn't mean to like
`21:15` back and oop, I didn't mean to like that. But once it all looks good, you
`21:18` that. But once it all looks good, you
`21:18` that. But once it all looks good, you can go and publish it. But we're not
`21:19` can go and publish it. But we're not
`21:19` can go and publish it. But we're not going to do that yet because we want to
`21:21` going to do that yet because we want to
`21:21` going to do that yet because we want to double-check. So, it went through,
`21:23` double-check. So, it went through,
`21:23` double-check. So, it went through, again, it read GitHub files, it looked
`21:25` again, it read GitHub files, it looked
`21:25` again, it read GitHub files, it looked through scripts, it wrote its own
`21:27` through scripts, it wrote its own
`21:27` through scripts, it wrote its own skills, right? It came in and it said,
`21:29` skills, right? It came in and it said,
`21:29` skills, right? It came in and it said, "You know what? This is the whole
`21:31` "You know what? This is the whole
`21:31` "You know what? This is the whole project. So, here's your assets, here's
`21:33` project. So, here's your assets, here's
`21:33` project. So, here's your assets, here's all your SVGs, here's all of the main
`21:36` all your SVGs, here's all of the main
`21:36` all your SVGs, here's all of the main things that you might be using. But
`21:37` things that you might be using. But
`21:37` things that you might be using. But there's also icons that you might need
`21:39` there's also icons that you might need
`21:39` there's also icons that you might need to use, right?" Then there's also this
`21:41` to use, right?" Then there's also this
`21:41` to use, right?" Then there's also this skill. Every time it's adding a new
`21:43` skill. Every time it's adding a new
`21:43` skill. Every time it's adding a new folder, it's referencing where it is.
`21:46` folder, it's referencing where it is.
`21:46` folder, it's referencing where it is. The way you could make this more
`21:47` The way you could make this more
`21:47` The way you could make this more efficient is actually show the folder
`21:49` efficient is actually show the folder
`21:50` efficient is actually show the folder structure. That way when Claude is
`21:51` structure. That way when Claude is
`21:51` structure. That way when Claude is reading through it, it knows where those
`21:53` reading through it, it knows where those
`21:53` reading through it, it knows where those files are. It's not spending time to go
`21:56` files are. It's not spending time to go
`21:56` files are. It's not spending time to go find those files. It's looking through
`21:58` find those files. It's looking through
`21:58` find those files. It's looking through it, knows, "Oh, well, hey, that file
`22:01` it, knows, "Oh, well, hey, that file
`22:01` it, knows, "Oh, well, hey, that file that I'm looking for is in the script
`22:02` that I'm looking for is in the script
`22:02` that I'm looking for is in the script lab and it's two folders deep." versus
`22:04` lab and it's two folders deep." versus
`22:04` lab and it's two folders deep." versus it having to search through the folders
`22:06` it having to search through the folders
`22:06` it having to search through the folders to find that file. That's just something
`22:08` to find that file. That's just something
`22:08` to find that file. That's just something I would add personally. I'm sure Claude
`22:10` I would add personally. I'm sure Claude
`22:10` I would add personally. I'm sure Claude or Anthropic will add that that soon as
`22:12` or Anthropic will add that that soon as
`22:12` or Anthropic will add that that soon as long as they watch my videos. But that's
`22:14` long as they watch my videos. But that's
`22:14` long as they watch my videos. But that's the idea here. It's all just folders,
`22:16` the idea here. It's all just folders,
`22:16` the idea here. It's all just folders, texts, and components. That's all it's
`22:19` texts, and components. That's all it's
`22:19` texts, and components. That's all it's doing. It's very impressive and it even
`22:21` doing. It's very impressive and it even
`22:21` doing. It's very impressive and it even has voice MDs, right? These are just
`22:23` has voice MDs, right? These are just
`22:23` has voice MDs, right? These are just markdown files of how the concepts,
`22:25` markdown files of how the concepts,
`22:25` markdown files of how the concepts, "Hey, we're calm, we're useful, we're
`22:27` "Hey, we're calm, we're useful, we're
`22:27` "Hey, we're calm, we're useful, we're never theatrical." You can come in and
`22:29` never theatrical." You can come in and
`22:29` never theatrical." You can come in and edit these if you want. They go through.
`22:31` edit these if you want. They go through.
`22:31` edit these if you want. They go through. Where are these aspects? You could add
`22:33` Where are these aspects? You could add
`22:33` Where are these aspects? You could add case studies of these, right? Which
`22:35` case studies of these, right? Which
`22:35` case studies of these, right? Which there isn't any here cuz I didn't add
`22:37` there isn't any here cuz I didn't add
`22:37` there isn't any here cuz I didn't add case studies. But you could literally
`22:38` case studies. But you could literally
`22:38` case studies. But you could literally say, "Hey, this is when we did branding
`22:40` say, "Hey, this is when we did branding
`22:41` say, "Hey, this is when we did branding right and it got a lot of information.
`22:42` right and it got a lot of information.
`22:42` right and it got a lot of information. This is when we did something wrong,
`22:44` This is when we did something wrong,
`22:44` This is when we did something wrong, right?" In these aspects. All of these
`22:47` right?" In these aspects. All of these
`22:47` right?" In these aspects. All of these files are there. And it seems to have
`22:49` files are there. And it seems to have
`22:49` files are there. And it seems to have done that, right? Surface level UI
`22:51` done that, right? Surface level UI
`22:51` done that, right? Surface level UI exists. Yep, you're right. I didn't give
`22:53` exists. Yep, you're right. I didn't give
`22:53` exists. Yep, you're right. I didn't give it any other high-level UI aspects. It
`22:56` it any other high-level UI aspects. It
`22:56` it any other high-level UI aspects. It did look at our So, we do have this kind
`22:58` did look at our So, we do have this kind
`22:58` did look at our So, we do have this kind of core aspect for Scramble, which could
`23:00` of core aspect for Scramble, which could
`23:00` of core aspect for Scramble, which could be more complicated to make it better.
`23:02` be more complicated to make it better.
`23:03` be more complicated to make it better. So, it recognized issues with what it
`23:05` So, it recognized issues with what it
`23:05` So, it recognized issues with what it created. And if you're a designer,
`23:06` created. And if you're a designer,
`23:06` created. And if you're a designer, you'll be able to expand on these issues
`23:08` you'll be able to expand on these issues
`23:08` you'll be able to expand on these issues more. If you're not, it's okay. You got
`23:10` more. If you're not, it's okay. You got
`23:10` more. If you're not, it's okay. You got what you needed out of it.
`23:11` what you needed out of it.
`23:11` what you needed out of it. And then it's asking, "Hey, can you
`23:13` And then it's asking, "Hey, can you
`23:13` And then it's asking, "Hey, can you recalibrate? Maybe the voice needs to be
`23:15` recalibrate? Maybe the voice needs to be
`23:15` recalibrate? Maybe the voice needs to be better." which is what we were just
`23:16` better." which is what we were just
`23:16` better." which is what we were just looking at here. How do we want our
`23:18` looking at here. How do we want our
`23:18` looking at here. How do we want our voice to sound? Is this who we are?
`23:20` voice to sound? Is this who we are?
`23:20` voice to sound? Is this who we are? Immediately, this I'm going to change
`23:22` Immediately, this I'm going to change
`23:22` Immediately, this I'm going to change that. I don't like that voice. This is
`23:24` that. I don't like that voice. This is
`23:24` that. I don't like that voice. This is cool. I am a Marine. I did go engineer
`23:26` cool. I am a Marine. I did go engineer
`23:26` cool. I am a Marine. I did go engineer and governance research. And that's a
`23:28` and governance research. And that's a
`23:28` and governance research. And that's a cool vibe, but that sounds kind of
`23:29` cool vibe, but that sounds kind of
`23:29` cool vibe, but that sounds kind of salesy and and weird. I I have my own
`23:32` salesy and and weird. I I have my own
`23:32` salesy and and weird. I I have my own voice structures that I've spent a lot
`23:34` voice structures that I've spent a lot
`23:34` voice structures that I've spent a lot of time writing. Um actually, I think I
`23:36` of time writing. Um actually, I think I
`23:36` of time writing. Um actually, I think I have some right here that I can show
`23:38` have some right here that I can show
`23:38` have some right here that I can show you. Should be in my docs. I actually
`23:41` you. Should be in my docs. I actually
`23:41` you. Should be in my docs. I actually forgot where I put that one.
`23:43` forgot where I put that one.
`23:43` forgot where I put that one. Could it be brief notes?
`23:45` Could it be brief notes?
`23:45` Could it be brief notes? Nope. Uh
`23:47` Nope. Uh
`23:47` Nope. Uh is it in my script lab?
`23:49` is it in my script lab?
`23:49` is it in my script lab? Yes, my voice. So, I already have a
`23:51` Yes, my voice. So, I already have a
`23:51` Yes, my voice. So, I already have a voice document of how I like to speak,
`23:53` voice document of how I like to speak,
`23:53` voice document of how I like to speak, what we do. Here it is. I'm actually
`23:55` what we do. Here it is. I'm actually
`23:55` what we do. Here it is. I'm actually going to condense this even more. I even
`23:57` going to condense this even more. I even
`23:57` going to condense this even more. I even gave my own versions of what's wrong and
`23:59` gave my own versions of what's wrong and
`23:59` gave my own versions of what's wrong and right. And that's not even considering
`24:00` right. And that's not even considering
`24:00` right. And that's not even considering the AI side of things. No, I'd never say
`24:02` the AI side of things. No, I'd never say
`24:02` the AI side of things. No, I'd never say that. I say, "And that's just if you
`24:03` that. I say, "And that's just if you
`24:03` that. I say, "And that's just if you wrote the line yourself." I'm barely
`24:05` wrote the line yourself." I'm barely
`24:05` wrote the line yourself." I'm barely referencing AI. I'm referencing
`24:07` referencing AI. I'm referencing
`24:07` referencing AI. I'm referencing structures, concepts, right? And that's
`24:09` structures, concepts, right? And that's
`24:09` structures, concepts, right? And that's what you can do right here. You can just
`24:11` what you can do right here. You can just
`24:11` what you can do right here. You can just say, "Hey." Or you can leave it. Again,
`24:12` say, "Hey." Or you can leave it. Again,
`24:12` say, "Hey." Or you can leave it. Again, you don't have to get as complicated as
`24:13` you don't have to get as complicated as
`24:14` you don't have to get as complicated as me. I like to be nuanced. I like to dive
`24:15` me. I like to be nuanced. I like to dive
`24:15` me. I like to be nuanced. I like to dive in. That's where I see and get the most
`24:17` in. That's where I see and get the most
`24:17` in. That's where I see and get the most value. The ROI is my opinion. Uh
`24:20` value. The ROI is my opinion. Uh
`24:20` value. The ROI is my opinion. Uh everyone can make a decent thing now.
`24:22` everyone can make a decent thing now.
`24:22` everyone can make a decent thing now. Everyone can get all the answers. Now
`24:24` Everyone can get all the answers. Now
`24:24` Everyone can get all the answers. Now the questions are important. Things that
`24:26` the questions are important. Things that
`24:26` the questions are important. Things that are metrics of best uh or where best
`24:29` are metrics of best uh or where best
`24:29` are metrics of best uh or where best doesn't exist is what becomes valuable.
`24:31` doesn't exist is what becomes valuable.
`24:31` doesn't exist is what becomes valuable. And my opinion on who we are is now an
`24:34` And my opinion on who we are is now an
`24:34` And my opinion on who we are is now an active code choice because at the end of
`24:37` active code choice because at the end of
`24:37` active code choice because at the end of the day, everyone's going to be able to
`24:38` the day, everyone's going to be able to
`24:38` the day, everyone's going to be able to get the decent enough code. But is it
`24:40` get the decent enough code. But is it
`24:40` get the decent enough code. But is it going to be at that top 10%? When you
`24:42` going to be at that top 10%? When you
`24:42` going to be at that top 10%? When you get in the top 10% of design or code or
`24:44` get in the top 10% of design or code or
`24:44` get in the top 10% of design or code or even mathematics, opinions become the
`24:47` even mathematics, opinions become the
`24:47` even mathematics, opinions become the actual valuable thing. Uh you want to
`24:49` actual valuable thing. Uh you want to
`24:49` actual valuable thing. Uh you want to productionize your opinion, which I'm
`24:51` productionize your opinion, which I'm
`24:51` productionize your opinion, which I'm going to make a shirt that says that
`24:52` going to make a shirt that says that
`24:52` going to make a shirt that says that honestly for myself. I think that would
`24:54` honestly for myself. I think that would
`24:54` honestly for myself. I think that would be good. At the end of the day, you're
`24:56` be good. At the end of the day, you're
`24:56` be good. At the end of the day, you're left with a really big, beautiful design
`24:59` left with a really big, beautiful design
`24:59` left with a really big, beautiful design system. And you can just simply hit
`25:01` system. And you can just simply hit
`25:01` system. And you can just simply hit publish and use a new design method. But
`25:04` publish and use a new design method. But
`25:04` publish and use a new design method. But before I do that, I can actually come
`25:06` before I do that, I can actually come
`25:06` before I do that, I can actually come in. I can look at this whole project. I
`25:09` in. I can look at this whole project. I
`25:09` in. I can look at this whole project. I instead of using more tokens inside of
`25:11` instead of using more tokens inside of
`25:11` instead of using more tokens inside of design,
`25:12` design,
`25:13` design, I can come in, I can hit share,
`25:15` I can come in, I can hit share,
`25:15` I can come in, I can hit share, and I can either duplicate this project,
`25:17` and I can either duplicate this project,
`25:17` and I can either duplicate this project, I can download it as a zip, which is
`25:19` I can download it as a zip, which is
`25:19` I can download it as a zip, which is exactly what I'm going to do here, or I
`25:21` exactly what I'm going to do here, or I
`25:21` exactly what I'm going to do here, or I can export it to PowerPoint, HTML, and
`25:24` can export it to PowerPoint, HTML, and
`25:24` can export it to PowerPoint, HTML, and it'll create an entire briefing
`25:25` it'll create an entire briefing
`25:25` it'll create an entire briefing document, a design document that I can
`25:27` document, a design document that I can
`25:27` document, a design document that I can hand to other designers or my vendors or
`25:29` hand to other designers or my vendors or
`25:29` hand to other designers or my vendors or contractors. I can import it to Canda
`25:32` contractors. I can import it to Canda
`25:32` contractors. I can import it to Canda Canva, or I can go directly to Claude
`25:34` Canva, or I can go directly to Claude
`25:34` Canva, or I can go directly to Claude code. They know how I'm about to show
`25:36` code. They know how I'm about to show
`25:37` code. They know how I'm about to show you how to use this, right? You can
`25:38` you how to use this, right? You can
`25:38` you how to use this, right? You can literally import this project into
`25:40` literally import this project into
`25:40` literally import this project into Claude code, but I I'm going to show you
`25:42` Claude code, but I I'm going to show you
`25:42` Claude code, but I I'm going to show you how to do it simpler way, which is
`25:43` how to do it simpler way, which is
`25:43` how to do it simpler way, which is through the zip. But let's say, right?
`25:46` through the zip. But let's say, right?
`25:46` through the zip. But let's say, right? I've downloaded it, I have it there. Now
`25:47` I've downloaded it, I have it there. Now
`25:47` I've downloaded it, I have it there. Now I can hit new use a new design.
`25:50` I can hit new use a new design.
`25:50` I can hit new use a new design. Now I have Oh, crap. I should have named
`25:52` Now I have Oh, crap. I should have named
`25:52` Now I have Oh, crap. I should have named it something else, but that's okay. One
`25:54` it something else, but that's okay. One
`25:54` it something else, but that's okay. One of these is the proper Aduba design
`25:56` of these is the proper Aduba design
`25:56` of these is the proper Aduba design system. I'm going to assume it's this
`25:57` system. I'm going to assume it's this
`25:57` system. I'm going to assume it's this one.
`25:58` one.
`25:58` one. >> [laughter]
`25:58` >> [laughter]
`25:58` >> [laughter] >> That was a mistake on my part, but
`25:59` >> That was a mistake on my part, but
`25:59` >> That was a mistake on my part, but that's okay. And now I can go in and
`26:01` that's okay. And now I can go in and
`26:01` that's okay. And now I can go in and say, "I want to go make a slide deck
`26:04` say, "I want to go make a slide deck
`26:04` say, "I want to go make a slide deck pitch."
`26:05` pitch."
`26:05` pitch." And so, I can come in and let's say I'm
`26:07` And so, I can come in and let's say I'm
`26:07` And so, I can come in and let's say I'm creating a pitch for an investor or
`26:09` creating a pitch for an investor or
`26:09` creating a pitch for an investor or something like that. I can come in and
`26:12` something like that. I can come in and
`26:12` something like that. I can come in and say, "I want to make a pitch for Y
`26:16` say, "I want to make a pitch for Y
`26:16` say, "I want to make a pitch for Y Combinator." Now, generally speaking,
`26:18` Combinator." Now, generally speaking,
`26:18` Combinator." Now, generally speaking, you want to have a lot of info on your
`26:20` you want to have a lot of info on your
`26:20` you want to have a lot of info on your company. Sometimes what I do is if you
`26:22` company. Sometimes what I do is if you
`26:22` company. Sometimes what I do is if you use Claude or any other tools, you can
`26:25` use Claude or any other tools, you can
`26:25` use Claude or any other tools, you can create a briefing document, which I did
`26:27` create a briefing document, which I did
`26:27` create a briefing document, which I did recently. But I can literally just copy
`26:30` recently. But I can literally just copy
`26:30` recently. But I can literally just copy that and paste that into here. And so,
`26:33` that and paste that into here. And so,
`26:33` that and paste that into here. And so, not only does it have all of that info
`26:35` not only does it have all of that info
`26:35` not only does it have all of that info on my company, what I'm doing, what the
`26:37` on my company, what I'm doing, what the
`26:37` on my company, what I'm doing, what the kind of pitch is that I want,
`26:39` kind of pitch is that I want,
`26:39` kind of pitch is that I want, but it's also using the Aduba design
`26:41` but it's also using the Aduba design
`26:41` but it's also using the Aduba design system and making a slide deck. So, it's
`26:44` system and making a slide deck. So, it's
`26:44` system and making a slide deck. So, it's all those skills compiled into one
`26:45` all those skills compiled into one
`26:45` all those skills compiled into one place. I can trust that the assets it's
`26:48` place. I can trust that the assets it's
`26:48` place. I can trust that the assets it's pulling from, the folders it's pulling
`26:49` pulling from, the folders it's pulling
`26:50` pulling from, the folders it's pulling from, are going to work well. This Aduba
`26:52` from, are going to work well. This Aduba
`26:52` from, are going to work well. This Aduba design system is more than just a skill.
`26:54` design system is more than just a skill.
`26:54` design system is more than just a skill. It is a literal set of folders, right?
`26:57` It is a literal set of folders, right?
`26:57` It is a literal set of folders, right? It is all of our assets condensed into a
`27:00` It is all of our assets condensed into a
`27:00` It is all of our assets condensed into a folder structure, which actually, I'm
`27:03` folder structure, which actually, I'm
`27:03` folder structure, which actually, I'm going to go ahead and show you what that
`27:05` going to go ahead and show you what that
`27:05` going to go ahead and show you what that looks like locally and how my folder
`27:07` looks like locally and how my folder
`27:07` looks like locally and how my folder structure is literally that. Oh my god,
`27:09` structure is literally that. Oh my god,
`27:09` structure is literally that. Oh my god, I have so many things open.
`27:11` I have so many things open.
`27:11` I have so many things open. I already made a little folder cuz I
`27:12` I already made a little folder cuz I
`27:12` I already made a little folder cuz I knew I was going to do this. So, let's
`27:14` knew I was going to do this. So, let's
`27:14` knew I was going to do this. So, let's say I threw this folder really quickly.
`27:18` say I threw this folder really quickly.
`27:18` say I threw this folder really quickly. Just created a folder on my desktop,
`27:19` Just created a folder on my desktop,
`27:19` Just created a folder on my desktop, right? Through the This is the zip we
`27:21` right? Through the This is the zip we
`27:21` right? Through the This is the zip we just downloaded with our Aduba design
`27:23` just downloaded with our Aduba design
`27:23` just downloaded with our Aduba design process.
`27:24` process.
`27:24` process. Come in. I'm just going to go ahead and
`27:26` Come in. I'm just going to go ahead and
`27:26` Come in. I'm just going to go ahead and extract it here. Why not right-click it?
`27:29` extract it here. Why not right-click it?
`27:29` extract it here. Why not right-click it? Yeah, there we go. Extract all.
`27:32` Yeah, there we go. Extract all.
`27:32` Yeah, there we go. Extract all. Yes, I would like to extract it there. I
`27:34` Yes, I would like to extract it there. I
`27:34` Yes, I would like to extract it there. I think that's the right spot.
`27:35` think that's the right spot.
`27:35` think that's the right spot. Boom, cool. So, now I can just go ahead
`27:38` Boom, cool. So, now I can just go ahead
`27:38` Boom, cool. So, now I can just go ahead and move that out of it. Now this is the
`27:40` and move that out of it. Now this is the
`27:40` and move that out of it. Now this is the Claude design. So, what we're seeing
`27:42` Claude design. So, what we're seeing
`27:42` Claude design. So, what we're seeing right here
`27:44` right here
`27:44` right here when we're inside of this, right? This
`27:46` when we're inside of this, right? This
`27:46` when we're inside of this, right? This Aduba design system with all these
`27:47` Aduba design system with all these
`27:47` Aduba design system with all these folders and Claude being here,
`27:50` folders and Claude being here,
`27:50` folders and Claude being here, I technically have a similar version of
`27:52` I technically have a similar version of
`27:52` I technically have a similar version of it. If I open up, you can either use VS
`27:55` it. If I open up, you can either use VS
`27:55` it. If I open up, you can either use VS Code
`27:56` Code
`27:56` Code or I can use Claude Code Work or Claude
`27:59` or I can use Claude Code Work or Claude
`27:59` or I can use Claude Code Work or Claude Code in the app. So, if you have Claude
`28:01` Code in the app. So, if you have Claude
`28:01` Code in the app. So, if you have Claude downloaded, I can navigate to that
`28:05` downloaded, I can navigate to that
`28:05` downloaded, I can navigate to that folder, right? So, use a different
`28:07` folder, right? So, use a different
`28:07` folder, right? So, use a different folder, come in,
`28:09` folder, come in,
`28:09` folder, come in, right? Boom, select that folder. Should
`28:11` right? Boom, select that folder. Should
`28:11` right? Boom, select that folder. Should work. Now I'm inside of that folder. Or
`28:14` work. Now I'm inside of that folder. Or
`28:14` work. Now I'm inside of that folder. Or I can do the same thing with Claude
`28:16` I can do the same thing with Claude
`28:16` I can do the same thing with Claude Code, right? You come in, new session,
`28:20` Code, right? You come in, new session,
`28:20` Code, right? You come in, new session, I'm going to go and find the folder I
`28:23` I'm going to go and find the folder I
`28:23` I'm going to go and find the folder I want.
`28:24` want.
`28:24` want. Desktop, design. Again, this is where I
`28:26` Desktop, design. Again, this is where I
`28:26` Desktop, design. Again, this is where I just extracted the zip. I can now ask
`28:29` just extracted the zip. I can now ask
`28:29` just extracted the zip. I can now ask it, "Hey, I want to make a PowerPoint,
`28:33` it, "Hey, I want to make a PowerPoint,
`28:33` it, "Hey, I want to make a PowerPoint, right?"
`28:34` right?"
`28:34` right?" Trust this workspace. It's going to
`28:36` Trust this workspace. It's going to
`28:36` Trust this workspace. It's going to immediately read all of those files, all
`28:38` immediately read all of those files, all
`28:38` immediately read all of those files, all of those structures, and it's going to
`28:40` of those structures, and it's going to
`28:40` of those structures, and it's going to know because a skill was already created
`28:43` know because a skill was already created
`28:44` know because a skill was already created from this workspace.
`28:45` from this workspace.
`28:45` from this workspace. Use the themes in this workspace to make
`28:49` Use the themes in this workspace to make
`28:49` Use the themes in this workspace to make a test PowerPoint to show you understand
`28:54` a test PowerPoint to show you understand
`28:54` a test PowerPoint to show you understand branding here.
`28:56` branding here.
`28:56` branding here. And so, what it should read what is in
`28:59` And so, what it should read what is in
`28:59` And so, what it should read what is in this file locally. You could also do a
`29:01` this file locally. You could also do a
`29:01` this file locally. You could also do a \{{}slash} initiate command, right? So,
`29:03` \{{}slash} initiate command, right? So,
`29:03` \{{}slash} initiate command, right? So, then it'll read that file. It's going
`29:06` then it'll read that file. It's going
`29:06` then it'll read that file. It's going through the read me though, so that
`29:07` through the read me though, so that
`29:07` through the read me though, so that should work well. It sees what's in the
`29:09` should work well. It sees what's in the
`29:09` should work well. It sees what's in the contents, what's in the documents, what
`29:11` contents, what's in the documents, what
`29:11` contents, what's in the documents, what this design system is. It's doing what
`29:13` this design system is. It's doing what
`29:13` this design system is. It's doing what Claude design is doing, except it's
`29:15` Claude design is doing, except it's
`29:15` Claude design is doing, except it's using way less tokens. It's using it
`29:17` using way less tokens. It's using it
`29:17` using way less tokens. It's using it locally. Now I personally I'll let this
`29:19` locally. Now I personally I'll let this
`29:20` locally. Now I personally I'll let this run. I love Claude Code in this aspect.
`29:22` run. I love Claude Code in this aspect.
`29:22` run. I love Claude Code in this aspect. And as you can see it This is I didn't
`29:24` And as you can see it This is I didn't
`29:24` And as you can see it This is I didn't have to create all of this. This was
`29:25` have to create all of this. This was
`29:26` have to create all of this. This was already created by the Aduba design
`29:28` already created by the Aduba design
`29:28` already created by the Aduba design system. This is a skill, essentially.
`29:30` system. This is a skill, essentially.
`29:30` system. This is a skill, essentially. Again, markdown files with routing,
`29:33` Again, markdown files with routing,
`29:33` Again, markdown files with routing, where it came from, context, the paths
`29:36` where it came from, context, the paths
`29:36` where it came from, context, the paths of where to find it,
`29:37` of where to find it,
`29:37` of where to find it, embedded into it for me downloading it
`29:40` embedded into it for me downloading it
`29:40` embedded into it for me downloading it right here. By just uploading my GitHub
`29:42` right here. By just uploading my GitHub
`29:42` right here. By just uploading my GitHub or my Canvas, I'm getting the folder
`29:45` or my Canvas, I'm getting the folder
`29:45` or my Canvas, I'm getting the folder structure that I need, the folder
`29:46` structure that I need, the folder
`29:46` structure that I need, the folder structure that I've been teaching about
`29:48` structure that I've been teaching about
`29:48` structure that I've been teaching about in all of my videos and whatnot.
`29:50` in all of my videos and whatnot.
`29:50` in all of my videos and whatnot. And it's immediately going to do similar
`29:52` And it's immediately going to do similar
`29:52` And it's immediately going to do similar processes. The difference is for the
`29:54` processes. The difference is for the
`29:54` processes. The difference is for the animation videos and all of that stuff,
`29:56` animation videos and all of that stuff,
`29:56` animation videos and all of that stuff, you're going to need to download a
`29:57` you're going to need to download a
`29:57` you're going to need to download a couple extra tools like playwright or
`29:59` couple extra tools like playwright or
`29:59` couple extra tools like playwright or remotion, which I have videos on how to
`30:01` remotion, which I have videos on how to
`30:01` remotion, which I have videos on how to do that. But it's important to
`30:02` do that. But it's important to
`30:02` do that. But it's important to understand that.
`30:04` understand that.
`30:04` understand that. Now, you can also, instead of opening it
`30:06` Now, you can also, instead of opening it
`30:06` Now, you can also, instead of opening it there, is open it inside of VS Code,
`30:09` there, is open it inside of VS Code,
`30:09` there, is open it inside of VS Code, which is my personal favorite and I have
`30:11` which is my personal favorite and I have
`30:11` which is my personal favorite and I have videos on how to install VS Code with
`30:13` videos on how to install VS Code with
`30:13` videos on how to install VS Code with Claude and all that, so go check those
`30:15` Claude and all that, so go check those
`30:15` Claude and all that, so go check those out. But I can come in and go find the I
`30:18` out. But I can come in and go find the I
`30:18` out. But I can come in and go find the I know someone's going to say that I I I
`30:19` know someone's going to say that I I I
`30:19` know someone's going to say that I I I know design spelled wrong. I wrote it
`30:21` know design spelled wrong. I wrote it
`30:21` know design spelled wrong. I wrote it quickly.
`30:22` quickly.
`30:22` quickly. I'm going to open this one. Did I hit
`30:23` I'm going to open this one. Did I hit
`30:23` I'm going to open this one. Did I hit open folder? Don't hit open folder.
`30:25` open folder? Don't hit open folder.
`30:25` open folder? Don't hit open folder. That's important. Come here, click
`30:27` That's important. Come here, click
`30:27` That's important. Come here, click design, boom, right? And now, same
`30:30` design, boom, right? And now, same
`30:30` design, boom, right? And now, same thing. I'm working in here and while the
`30:33` thing. I'm working in here and while the
`30:33` thing. I'm working in here and while the other version of Claude Code is working
`30:35` other version of Claude Code is working
`30:35` other version of Claude Code is working in here, it's already creating that
`30:36` in here, it's already creating that
`30:36` in here, it's already creating that slide deck. My design system is here,
`30:39` slide deck. My design system is here,
`30:39` slide deck. My design system is here, too. I can open up Claude and do the
`30:41` too. I can open up Claude and do the
`30:41` too. I can open up Claude and do the same thing. And let me show you what the
`30:42` same thing. And let me show you what the
`30:42` same thing. And let me show you what the initiate command will do, right? So,
`30:44` initiate command will do, right? So,
`30:44` initiate command will do, right? So, it's going to go through and immediately
`30:46` it's going to go through and immediately
`30:46` it's going to go through and immediately read. Now, I have two agents creating
`30:48` read. Now, I have two agents creating
`30:48` read. Now, I have two agents creating sub agents working these. Uh-oh, I've
`30:50` sub agents working these. Uh-oh, I've
`30:50` sub agents working these. Uh-oh, I've hit my session limit. I have a current
`30:52` hit my session limit. I have a current
`30:52` hit my session limit. I have a current project that I'm running right now where
`30:53` project that I'm running right now where
`30:53` project that I'm running right now where we're
`30:54` we're
`30:54` we're beasting through tokens. Um I almost
`30:57` beasting through tokens. Um I almost
`30:57` beasting through tokens. Um I almost never hit my limit, but I've had it run
`30:59` never hit my limit, but I've had it run
`30:59` never hit my limit, but I've had it run straight for 3 days right now. Uh
`31:01` straight for 3 days right now. Uh
`31:01` straight for 3 days right now. Uh essentially, I'm creating websites for
`31:02` essentially, I'm creating websites for
`31:02` essentially, I'm creating websites for 350 companies in the matter of 24 hours.
`31:05` 350 companies in the matter of 24 hours.
`31:05` 350 companies in the matter of 24 hours. Uh we'll talk about that. I'll make a
`31:06` Uh we'll talk about that. I'll make a
`31:06` Uh we'll talk about that. I'll make a video on that here soon. But I have been
`31:08` video on that here soon. But I have been
`31:08` video on that here soon. But I have been eating through my usage, but it's still
`31:10` eating through my usage, but it's still
`31:10` eating through my usage, but it's still less than if I was doing API calls. Um
`31:12` less than if I was doing API calls. Um
`31:12` less than if I was doing API calls. Um and luckily, I have um I'm paying for
`31:14` and luckily, I have um I'm paying for
`31:14` and luckily, I have um I'm paying for extra right now because I wanted to show
`31:15` extra right now because I wanted to show
`31:16` extra right now because I wanted to show these aspects, but this is another
`31:17` these aspects, but this is another
`31:17` these aspects, but this is another reason why you might want to use local
`31:19` reason why you might want to use local
`31:19` reason why you might want to use local models and I'll show you here. I can
`31:20` models and I'll show you here. I can
`31:20` models and I'll show you here. I can actually have this convert over to
`31:22` actually have this convert over to
`31:22` actually have this convert over to local. But see, it's going through and
`31:23` local. But see, it's going through and
`31:23` local. But see, it's going through and it's getting ready. It's reading it.
`31:25` it's getting ready. It's reading it.
`31:25` it's getting ready. It's reading it. It's understanding it. And now that I
`31:27` It's understanding it. And now that I
`31:27` It's understanding it. And now that I have it initiated, it's going to create
`31:28` have it initiated, it's going to create
`31:28` have it initiated, it's going to create a Claude MD, which is based off of and
`31:30` a Claude MD, which is based off of and
`31:31` a Claude MD, which is based off of and might link to these readme files. But
`31:33` might link to these readme files. But
`31:33` might link to these readme files. But now it lets me go through and now, the
`31:35` now it lets me go through and now, the
`31:35` now it lets me go through and now, the reason I love it is if you are really
`31:37` reason I love it is if you are really
`31:37` reason I love it is if you are really wanting to get into it, you can look at
`31:39` wanting to get into it, you can look at
`31:39` wanting to get into it, you can look at your whole structure. This is everything
`31:41` your whole structure. This is everything
`31:41` your whole structure. This is everything Claude Design created. This is the whole
`31:43` Claude Design created. This is the whole
`31:43` Claude Design created. This is the whole process, the structure. This is your
`31:45` process, the structure. This is your
`31:45` process, the structure. This is your whole brand document. You can now give
`31:47` whole brand document. You can now give
`31:47` whole brand document. You can now give this folder structure to Codex, right? I
`31:50` this folder structure to Codex, right? I
`31:50` this folder structure to Codex, right? I have Codex installed. I can literally do
`31:53` have Codex installed. I can literally do
`31:53` have Codex installed. I can literally do the same thing. Read and understand this
`31:57` the same thing. Read and understand this
`31:57` the same thing. Read and understand this code base, right? Oh, I don't have it
`31:59` code base, right? Oh, I don't have it
`31:59` code base, right? Oh, I don't have it set up right now. I need to reconnect
`32:01` set up right now. I need to reconnect
`32:01` set up right now. I need to reconnect it. I'll set it up later, but you could
`32:02` it. I'll set it up later, but you could
`32:02` it. I'll set it up later, but you could do Codex in here. And this is a good
`32:04` do Codex in here. And this is a good
`32:05` do Codex in here. And this is a good point to double down on the I know my
`32:07` point to double down on the I know my
`32:07` point to double down on the I know my videos are always ADHD, so I hope you
`32:08` videos are always ADHD, so I hope you
`32:08` videos are always ADHD, so I hope you all get very good value out of this, but
`32:11` all get very good value out of this, but
`32:11` all get very good value out of this, but you could use local coding models as
`32:12` you could use local coding models as
`32:12` you could use local coding models as long as the model can read files and
`32:15` long as the model can read files and
`32:15` long as the model can read files and navigate a folder structure, you can use
`32:17` navigate a folder structure, you can use
`32:17` navigate a folder structure, you can use it to use these documents. It will read
`32:19` it to use these documents. It will read
`32:19` it to use these documents. It will read skill files. It will read these folders.
`32:21` skill files. It will read these folders.
`32:21` skill files. It will read these folders. It might not do it to the level that
`32:23` It might not do it to the level that
`32:23` It might not do it to the level that some models will, but one that I love is
`32:26` some models will, but one that I love is
`32:26` some models will, but one that I love is Qwen 3 Coder Next, specifically the next
`32:28` Qwen 3 Coder Next, specifically the next
`32:28` Qwen 3 Coder Next, specifically the next edition, because it allows you to use an
`32:30` edition, because it allows you to use an
`32:31` edition, because it allows you to use an 80 billion parameter model, but it only
`32:33` 80 billion parameter model, but it only
`32:33` 80 billion parameter model, but it only loads certain parameters at a time, so
`32:35` loads certain parameters at a time, so
`32:35` loads certain parameters at a time, so you can use it on smaller graphics
`32:36` you can use it on smaller graphics
`32:36` you can use it on smaller graphics cards. Uh but this is a really great.
`32:39` cards. Uh but this is a really great.
`32:39` cards. Uh but this is a really great. I'll make videos on installing and using
`32:41` I'll make videos on installing and using
`32:41` I'll make videos on installing and using local models. Another one that I like a
`32:43` local models. Another one that I like a
`32:43` local models. Another one that I like a lot is uh Code Gemma. This is from
`32:45` lot is uh Code Gemma. This is from
`32:45` lot is uh Code Gemma. This is from Google DeepMind. Um you can access the
`32:47` Google DeepMind. Um you can access the
`32:47` Google DeepMind. Um you can access the cloud version of it or download the
`32:49` cloud version of it or download the
`32:49` cloud version of it or download the smaller versions that will run locally
`32:51` smaller versions that will run locally
`32:51` smaller versions that will run locally on very not too powerful computers.
`32:53` on very not too powerful computers.
`32:53` on very not too powerful computers. Mistral has a local model called Devro,
`32:56` Mistral has a local model called Devro,
`32:56` Mistral has a local model called Devro, and you can even access it through your
`32:58` and you can even access it through your
`32:58` and you can even access it through your API if you don't have a strong computer.
`33:00` API if you don't have a strong computer.
`33:00` API if you don't have a strong computer. DeepSeek does as well. They have um B2,
`33:02` DeepSeek does as well. They have um B2,
`33:02` DeepSeek does as well. They have um B2, which is really good. Um you find here
`33:05` which is really good. Um you find here
`33:05` which is really good. Um you find here and it's open source and whatnot. Again,
`33:08` and it's open source and whatnot. Again,
`33:08` and it's open source and whatnot. Again, same thing. There's certain limitations
`33:10` same thing. There's certain limitations
`33:10` same thing. There's certain limitations and then some people argue that DeepSeek
`33:12` and then some people argue that DeepSeek
`33:12` and then some people argue that DeepSeek has some tracking that's being sent back
`33:15` has some tracking that's being sent back
`33:15` has some tracking that's being sent back even in their open source models, but
`33:17` even in their open source models, but
`33:17` even in their open source models, but there's a lot of arguments. We don't
`33:18` there's a lot of arguments. We don't
`33:18` there's a lot of arguments. We don't have to get into there.
`33:19` have to get into there.
`33:19` have to get into there. Um you are in government work,
`33:20` Um you are in government work,
`33:20` Um you are in government work, especially in the US, there's a lot of
`33:22` especially in the US, there's a lot of
`33:22` especially in the US, there's a lot of arguments about whether DeepSeek is
`33:24` arguments about whether DeepSeek is
`33:24` arguments about whether DeepSeek is allowed. Very great model, very powerful
`33:26` allowed. Very great model, very powerful
`33:26` allowed. Very great model, very powerful tool, but again,
`33:28` tool, but again,
`33:28` tool, but again, the reason you want to understand this,
`33:30` the reason you want to understand this,
`33:30` the reason you want to understand this, the reason I'm teaching folder structure
`33:33` the reason I'm teaching folder structure
`33:33` the reason I'm teaching folder structure is because if you understand the folder
`33:35` is because if you understand the folder
`33:35` is because if you understand the folder structure, if you can navigate it, you
`33:37` structure, if you can navigate it, you
`33:37` structure, if you can navigate it, you can remove the need to only use Claude,
`33:40` can remove the need to only use Claude,
`33:40` can remove the need to only use Claude, right? Like I hit my limits.
`33:43` right? Like I hit my limits.
`33:43` right? Like I hit my limits. I could just swap over to another model.
`33:44` I could just swap over to another model.
`33:44` I could just swap over to another model. I could swap over to a local one. Um and
`33:48` I could swap over to a local one. Um and
`33:48` I could swap over to a local one. Um and worry about being locked into a model
`33:50` worry about being locked into a model
`33:50` worry about being locked into a model and I get to tweak and control, right?
`33:52` and I get to tweak and control, right?
`33:52` and I get to tweak and control, right? I'm going to come through and rip this
`33:53` I'm going to come through and rip this
`33:53` I'm going to come through and rip this skill apart. I'm going to change this
`33:55` skill apart. I'm going to change this
`33:55` skill apart. I'm going to change this file structure. I'm going to give it my
`33:57` file structure. I'm going to give it my
`33:57` file structure. I'm going to give it my own version of the Claude that MD. See,
`33:59` own version of the Claude that MD. See,
`33:59` own version of the Claude that MD. See, this Claude that MD isn't even good in
`34:01` this Claude that MD isn't even good in
`34:01` this Claude that MD isn't even good in my opinion because it doesn't show um
`34:03` my opinion because it doesn't show um
`34:03` my opinion because it doesn't show um the actual structure of the folders.
`34:06` the actual structure of the folders.
`34:06` the actual structure of the folders. Even though it says where it goes, I
`34:08` Even though it says where it goes, I
`34:08` Even though it says where it goes, I find building it out like you saw in my
`34:10` find building it out like you saw in my
`34:11` find building it out like you saw in my other one.
`34:12` other one.
`34:12` other one. Um really does make a difference not
`34:15` Um really does make a difference not
`34:15` Um really does make a difference not just for other people, but for me.
`34:17` just for other people, but for me.
`34:17` just for other people, but for me. There's also the option of using
`34:18` There's also the option of using
`34:19` There's also the option of using Obsidian, which I haven't made a video
`34:20` Obsidian, which I haven't made a video
`34:20` Obsidian, which I haven't made a video on. I keep saying I'm going to, but
`34:22` on. I keep saying I'm going to, but
`34:22` on. I keep saying I'm going to, but Obsidian's a local file control
`34:24` Obsidian's a local file control
`34:24` Obsidian's a local file control structure app that you can download that
`34:27` structure app that you can download that
`34:27` structure app that you can download that lets you look at all These are the
`34:28` lets you look at all These are the
`34:28` lets you look at all These are the markdown files that you were just
`34:29` markdown files that you were just
`34:29` markdown files that you were just looking at, right?
`34:31` looking at, right?
`34:31` looking at, right? But it actually renders markdown and you
`34:34` But it actually renders markdown and you
`34:34` But it actually renders markdown and you can create dashboards around where
`34:37` can create dashboards around where
`34:37` can create dashboards around where everything is. So, where certain files
`34:39` everything is. So, where certain files
`34:39` everything is. So, where certain files are, where they're located. You create
`34:40` are, where they're located. You create
`34:40` are, where they're located. You create metadata and you can create mind maps
`34:43` metadata and you can create mind maps
`34:43` metadata and you can create mind maps with it, which
`34:44` with it, which
`34:44` with it, which I I have on this one.
`34:47` I I have on this one.
`34:47` I I have on this one. I think I have it. Yeah. You can create
`34:48` I think I have it. Yeah. You can create
`34:48` I think I have it. Yeah. You can create kind of maps. I haven't been spending a
`34:50` kind of maps. I haven't been spending a
`34:50` kind of maps. I haven't been spending a lot of time cleaning mine up, but it can
`34:52` lot of time cleaning mine up, but it can
`34:52` lot of time cleaning mine up, but it can show you how certain readmes connect to
`34:54` show you how certain readmes connect to
`34:54` show you how certain readmes connect to other workers or functions or processes
`34:57` other workers or functions or processes
`34:57` other workers or functions or processes and immediately click them. So, you can
`34:59` and immediately click them. So, you can
`34:59` and immediately click them. So, you can navigate your file structure a lot
`35:01` navigate your file structure a lot
`35:01` navigate your file structure a lot faster
`35:02` faster
`35:02` faster um by going through and clicking on
`35:04` um by going through and clicking on
`35:04` um by going through and clicking on these uh services and processes. Which
`35:06` these uh services and processes. Which
`35:06` these uh services and processes. Which So, Obsidian's really cool for creating
`35:08` So, Obsidian's really cool for creating
`35:08` So, Obsidian's really cool for creating mind maps. Again,
`35:10` mind maps. Again,
`35:10` mind maps. Again, it's cool and it's useful in certain
`35:12` it's cool and it's useful in certain
`35:12` it's cool and it's useful in certain situations. I don't think it's as
`35:14` situations. I don't think it's as
`35:14` situations. I don't think it's as important as people put it out there for
`35:16` important as people put it out there for
`35:16` important as people put it out there for most use cases or for early users. I
`35:19` most use cases or for early users. I
`35:19` most use cases or for early users. I think as you navigate these structures,
`35:22` think as you navigate these structures,
`35:22` think as you navigate these structures, as you get better in understanding um
`35:24` as you get better in understanding um
`35:24` as you get better in understanding um type of software engineering, quote
`35:26` type of software engineering, quote
`35:26` type of software engineering, quote unquote, then Obsidian becomes more
`35:28` unquote, then Obsidian becomes more
`35:28` unquote, then Obsidian becomes more useful, which is why I haven't been
`35:29` useful, which is why I haven't been
`35:29` useful, which is why I haven't been spending as much time sharing or talking
`35:31` spending as much time sharing or talking
`35:31` spending as much time sharing or talking about it. But it is really cool.
`35:33` about it. But it is really cool.
`35:33` about it. But it is really cool. Um anyway, once you've got this all set
`35:35` Um anyway, once you've got this all set
`35:35` Um anyway, once you've got this all set up, if you can install another local
`35:37` up, if you can install another local
`35:37` up, if you can install another local model, you can ask it to create these
`35:40` model, you can ask it to create these
`35:40` model, you can ask it to create these animations, create these slide decks,
`35:41` animations, create these slide decks,
`35:41` animations, create these slide decks, these processes, right? Have it come
`35:43` these processes, right? Have it come
`35:44` these processes, right? Have it come through. And right now, that's exactly
`35:45` through. And right now, that's exactly
`35:45` through. And right now, that's exactly what it's doing. And if I come in, I can
`35:48` what it's doing. And if I come in, I can
`35:48` what it's doing. And if I come in, I can even access it without VS Code, without
`35:50` even access it without VS Code, without
`35:50` even access it without VS Code, without any of that. I can just go and be like,
`35:52` any of that. I can just go and be like,
`35:52` any of that. I can just go and be like, "Oh, okay. These slides look Oh, that's
`35:55` "Oh, okay. These slides look Oh, that's
`35:55` "Oh, okay. These slides look Oh, that's a good slide." At the end, what Claude
`35:57` a good slide." At the end, what Claude
`35:57` a good slide." At the end, what Claude is going to do, um I Claude Code on my
`35:59` is going to do, um I Claude Code on my
`35:59` is going to do, um I Claude Code on my desktop, is it's generating each slide
`36:01` desktop, is it's generating each slide
`36:01` desktop, is it's generating each slide and then it's going to connect them
`36:03` and then it's going to connect them
`36:03` and then it's going to connect them together as one large HTML file or
`36:05` together as one large HTML file or
`36:05` together as one large HTML file or convert that HTML file to a PowerPoint.
`36:09` convert that HTML file to a PowerPoint.
`36:09` convert that HTML file to a PowerPoint. Um exactly what's happening right here.
`36:10` Um exactly what's happening right here.
`36:10` Um exactly what's happening right here. It's just generating each slide. That is
`36:12` It's just generating each slide. That is
`36:12` It's just generating each slide. That is exactly
`36:14` exactly
`36:14` exactly what
`36:15` what
`36:15` what Claude Design is doing. Literally, if
`36:18` Claude Design is doing. Literally, if
`36:18` Claude Design is doing. Literally, if you come in and we look at my last
`36:21` you come in and we look at my last
`36:21` you come in and we look at my last project where I had it create a slide
`36:23` project where I had it create a slide
`36:23` project where I had it create a slide deck, right? This is our new pitch. This
`36:26` deck, right? This is our new pitch. This
`36:26` deck, right? This is our new pitch. This pitch. Um it is all HTML, right? It's
`36:30` pitch. Um it is all HTML, right? It's
`36:30` pitch. Um it is all HTML, right? It's creating HTML briefings and then you can
`36:33` creating HTML briefings and then you can
`36:33` creating HTML briefings and then you can convert them to slide decks, download as
`36:37` convert them to slide decks, download as
`36:37` convert them to slide decks, download as slide decks, right? And I did that
`36:38` slide decks, right? And I did that
`36:38` slide decks, right? And I did that literally from Claude Design.
`36:41` literally from Claude Design.
`36:41` literally from Claude Design. Right.
`36:43` Right.
`36:43` Right. I'm able to download that and it
`36:45` I'm able to download that and it
`36:45` I'm able to download that and it converts it because of the skill for
`36:47` converts it because of the skill for
`36:47` converts it because of the skill for converting
`36:49` converting
`36:49` converting um
`36:49` um
`36:49` um and so then I took those HTMLs and then
`36:51` and so then I took those HTMLs and then
`36:51` and so then I took those HTMLs and then now this is a fully editable power deck,
`36:54` now this is a fully editable power deck,
`36:54` now this is a fully editable power deck, right? Um it convert the typology so
`36:57` right? Um it convert the typology so
`36:57` right? Um it convert the typology so that it could be um
`36:59` that it could be um
`36:59` that it could be um automated. If you have the typology
`37:01` automated. If you have the typology
`37:01` automated. If you have the typology downloaded, then you can actually have
`37:02` downloaded, then you can actually have
`37:03` downloaded, then you can actually have it transfer, which my brand's typology
`37:05` it transfer, which my brand's typology
`37:05` it transfer, which my brand's typology is, so it's much larger in how it's
`37:08` is, so it's much larger in how it's
`37:08` is, so it's much larger in how it's written and whatnot. But that's the
`37:09` written and whatnot. But that's the
`37:09` written and whatnot. But that's the concept here, right? Design is a way
`37:13` concept here, right? Design is a way
`37:13` concept here, right? Design is a way that Anthropic helps you navigate and
`37:16` that Anthropic helps you navigate and
`37:16` that Anthropic helps you navigate and control assets to creating folder
`37:19` control assets to creating folder
`37:19` control assets to creating folder structures. And this is just one aspect
`37:21` structures. And this is just one aspect
`37:21` structures. And this is just one aspect of it. I promise you, over the next 5
`37:23` of it. I promise you, over the next 5
`37:23` of it. I promise you, over the next 5 years, more tools and processes are
`37:25` years, more tools and processes are
`37:25` years, more tools and processes are going to come out like this. Less and
`37:27` going to come out like this. Less and
`37:27` going to come out like this. Less and less are you going to need to build
`37:29` less are you going to need to build
`37:29` less are you going to need to build agents that navigate folders and collect
`37:31` agents that navigate folders and collect
`37:31` agents that navigate folders and collect things. More and more you're going to
`37:32` things. More and more you're going to
`37:32` things. More and more you're going to need to condense your structures and
`37:34` need to condense your structures and
`37:34` need to condense your structures and processes into something that one or two
`37:37` processes into something that one or two
`37:37` processes into something that one or two agents or one really good coding agent
`37:39` agents or one really good coding agent
`37:39` agents or one really good coding agent can read and conform and make tool calls
`37:43` can read and conform and make tool calls
`37:43` can read and conform and make tool calls to create processes. And the reason you
`37:45` to create processes. And the reason you
`37:45` to create processes. And the reason you want to not waste your time building
`37:47` want to not waste your time building
`37:47` want to not waste your time building with one single company and focus on the
`37:49` with one single company and focus on the
`37:49` with one single company and focus on the fundamentals is because then you can
`37:51` fundamentals is because then you can
`37:51` fundamentals is because then you can have it locally. You can control it.
`37:53` have it locally. You can control it.
`37:54` have it locally. You can control it. This can cut costs or you at least
`37:56` This can cut costs or you at least
`37:56` This can cut costs or you at least understand how to edit it.
`37:58` understand how to edit it.
`37:58` understand how to edit it. But
`37:59` But
`37:59` But essentially, that's a really good way to
`38:01` essentially, that's a really good way to
`38:01` essentially, that's a really good way to dive into it. Um if you wanted to start
`38:03` dive into it. Um if you wanted to start
`38:03` dive into it. Um if you wanted to start creating animations in here, again, go
`38:06` creating animations in here, again, go
`38:06` creating animations in here, again, go check out my remotion video and you want
`38:08` check out my remotion video and you want
`38:08` check out my remotion video and you want to download the remotion library um at
`38:12` to download the remotion library um at
`38:12` to download the remotion library um at the skill for for remotion, but
`38:14` the skill for for remotion, but
`38:14` the skill for for remotion, but essentially, this lets you render
`38:16` essentially, this lets you render
`38:16` essentially, this lets you render locally on your computer.
`38:18` locally on your computer.
`38:18` locally on your computer. Um yes, you know what? This is a long
`38:19` Um yes, you know what? This is a long
`38:20` Um yes, you know what? This is a long video. Keep it longer. If I come into my
`38:23` video. Keep it longer. If I come into my
`38:23` video. Keep it longer. If I come into my content one, I have remotion installed
`38:26` content one, I have remotion installed
`38:26` content one, I have remotion installed here. So, we'll go ahead and terminal
`38:30` here. So, we'll go ahead and terminal
`38:30` here. So, we'll go ahead and terminal and you can see that I can just host a
`38:33` and you can see that I can just host a
`38:33` and you can see that I can just host a kind of artifact locally. So, Claude
`38:36` kind of artifact locally. So, Claude
`38:36` kind of artifact locally. So, Claude Design hosted as an HTML.
`38:39` Design hosted as an HTML.
`38:39` Design hosted as an HTML. Um I can actually render JSX and all of
`38:42` Um I can actually render JSX and all of
`38:42` Um I can actually render JSX and all of these animations and look at them here.
`38:44` these animations and look at them here.
`38:44` these animations and look at them here. Or, if you wanted to go really simple,
`38:46` Or, if you wanted to go really simple,
`38:46` Or, if you wanted to go really simple, you don't even need to download
`38:47` you don't even need to download
`38:48` you don't even need to download remotion. Do everything motion
`38:50` remotion. Do everything motion
`38:50` remotion. Do everything motion animations in HTML and then you can just
`38:53` animations in HTML and then you can just
`38:53` animations in HTML and then you can just open up those those HTML files, right?
`38:57` open up those those HTML files, right?
`38:57` open up those those HTML files, right? Um
`38:57` Um
`38:57` Um See if it'll let me do that here. Or
`39:00` See if it'll let me do that here. Or
`39:00` See if it'll let me do that here. Or Yeah, I can come here and I should be
`39:02` Yeah, I can come here and I should be
`39:02` Yeah, I can come here and I should be able to Now, I think I used JSX in this
`39:04` able to Now, I think I used JSX in this
`39:04` able to Now, I think I used JSX in this one, so yeah, it's going to work the
`39:06` one, so yeah, it's going to work the
`39:06` one, so yeah, it's going to work the same way. Um this is where you would
`39:08` same way. Um this is where you would
`39:08` same way. Um this is where you would want So, it's rendering JSX and HTML in
`39:11` want So, it's rendering JSX and HTML in
`39:11` want So, it's rendering JSX and HTML in a single environment. If I had both of
`39:13` a single environment. If I had both of
`39:13` a single environment. If I had both of these downloaded in a folder and then I
`39:15` these downloaded in a folder and then I
`39:15` these downloaded in a folder and then I open the HTML, I'd be able It would just
`39:17` open the HTML, I'd be able It would just
`39:17` open the HTML, I'd be able It would just be like opening a web page. Uh remotion
`39:20` be like opening a web page. Uh remotion
`39:20` be like opening a web page. Uh remotion lets you kind of in and look at each
`39:21` lets you kind of in and look at each
`39:21` lets you kind of in and look at each frame and actually break down where
`39:23` frame and actually break down where
`39:23` frame and actually break down where those frames are. And then I can even
`39:25` those frames are. And then I can even
`39:25` those frames are. And then I can even hook Claude up to this. And let me find
`39:28` hook Claude up to this. And let me find
`39:28` hook Claude up to this. And let me find my long form
`39:29` my long form
`39:29` my long form Um and Claude can actually come in here
`39:32` Um and Claude can actually come in here
`39:32` Um and Claude can actually come in here and edit these animated videos. These
`39:34` and edit these animated videos. These
`39:34` and edit these animated videos. These were all I built all of these way before
`39:37` were all I built all of these way before
`39:37` were all I built all of these way before Claude Design. I had videos like this
`39:38` Claude Design. I had videos like this
`39:38` Claude Design. I had videos like this months ago. Um I had been built using
`39:41` months ago. Um I had been built using
`39:41` months ago. Um I had been built using this folder structure. Again, this whole
`39:43` this folder structure. Again, this whole
`39:43` this folder structure. Again, this whole content design system was basically
`39:45` content design system was basically
`39:45` content design system was basically Claude design before Claude design came
`39:47` Claude design before Claude design came
`39:47` Claude design before Claude design came out. I'm sure they probably stole some
`39:49` out. I'm sure they probably stole some
`39:49` out. I'm sure they probably stole some of my ideas from me. Not stole, they
`39:50` of my ideas from me. Not stole, they
`39:50` of my ideas from me. Not stole, they used it. They understand it. Everyone
`39:51` used it. They understand it. Everyone
`39:51` used it. They understand it. Everyone gets upset, "Oh, they stole it from me."
`39:53` gets upset, "Oh, they stole it from me."
`39:53` gets upset, "Oh, they stole it from me." Look, you can have a million ideas.
`39:54` Look, you can have a million ideas.
`39:55` Look, you can have a million ideas. Implementation and reaching an audience
`39:57` Implementation and reaching an audience
`39:57` Implementation and reaching an audience is the only thing that matters.
`39:59` is the only thing that matters.
`39:59` is the only thing that matters. Um ideas are useless until they're
`40:00` Um ideas are useless until they're
`40:00` Um ideas are useless until they're implemented. Uh
`40:02` implemented. Uh
`40:02` implemented. Uh you can steal something without the
`40:04` you can steal something without the
`40:04` you can steal something without the effort of implementing it. Now, if you
`40:05` effort of implementing it. Now, if you
`40:05` effort of implementing it. Now, if you implemented it and you're getting value,
`40:07` implemented it and you're getting value,
`40:07` implemented it and you're getting value, then there's an issue there. But again,
`40:08` then there's an issue there. But again,
`40:08` then there's an issue there. But again, this is the future of a lot of design
`40:10` this is the future of a lot of design
`40:11` this is the future of a lot of design and processing and it's only going to
`40:12` and processing and it's only going to
`40:12` and processing and it's only going to get better. Again, I built this folder
`40:14` get better. Again, I built this folder
`40:14` get better. Again, I built this folder structure system. I have all of these
`40:15` structure system. I have all of these
`40:15` structure system. I have all of these animations. It now just got better
`40:17` animations. It now just got better
`40:17` animations. It now just got better because of this feature, not replaced.
`40:20` because of this feature, not replaced.
`40:20` because of this feature, not replaced. I'm not chasing, trying to be better or
`40:23` I'm not chasing, trying to be better or
`40:23` I'm not chasing, trying to be better or outcompete Anthropic. My systems are
`40:25` outcompete Anthropic. My systems are
`40:25` outcompete Anthropic. My systems are getting better because these tools keep
`40:28` getting better because these tools keep
`40:28` getting better because these tools keep growing. That's what you want to build.
`40:30` growing. That's what you want to build.
`40:30` growing. That's what you want to build. You want to build the systems that grow
`40:33` You want to build the systems that grow
`40:33` You want to build the systems that grow with time, not get replaced with time.
`40:35` with time, not get replaced with time.
`40:36` with time, not get replaced with time. And I know I'm growing a lot faster now.
`40:38` And I know I'm growing a lot faster now.
`40:38` And I know I'm growing a lot faster now. I've gotten 30,000 subscribers, I think,
`40:40` I've gotten 30,000 subscribers, I think,
`40:40` I've gotten 30,000 subscribers, I think, on YouTube in the last uh month. But I
`40:44` on YouTube in the last uh month. But I
`40:44` on YouTube in the last uh month. But I promise you, and this is me being
`40:45` promise you, and this is me being
`40:45` promise you, and this is me being delusional,
`40:47` delusional,
`40:47` delusional, in the next year, my teachings will
`40:49` in the next year, my teachings will
`40:49` in the next year, my teachings will become even more relevant. I'm teaching
`40:51` become even more relevant. I'm teaching
`40:52` become even more relevant. I'm teaching stuff that's useful in 5 years, not just
`40:54` stuff that's useful in 5 years, not just
`40:54` stuff that's useful in 5 years, not just now. So, I hope you all stay tuned and
`40:57` now. So, I hope you all stay tuned and
`40:57` now. So, I hope you all stay tuned and learn it. If this is one of your first
`40:58` learn it. If this is one of your first
`40:58` learn it. If this is one of your first YouTube videos that you're inside of, uh
`41:00` YouTube videos that you're inside of, uh
`41:00` YouTube videos that you're inside of, uh please come join my community, Cleef
`41:02` please come join my community, Cleef
`41:02` please come join my community, Cleef Notes. I have all sorts of classrooms
`41:04` Notes. I have all sorts of classrooms
`41:05` Notes. I have all sorts of classrooms and foundations where I talk about
`41:06` and foundations where I talk about
`41:06` and foundations where I talk about folder structure, full workflows on how
`41:09` folder structure, full workflows on how
`41:09` folder structure, full workflows on how to set up folder structures, the
`41:11` to set up folder structures, the
`41:11` to set up folder structures, the concepts around it, and not just folder
`41:13` concepts around it, and not just folder
`41:13` concepts around it, and not just folder structure, but like the history of
`41:15` structure, but like the history of
`41:15` structure, but like the history of coding and processing. What it actually
`41:17` coding and processing. What it actually
`41:18` coding and processing. What it actually means to think about this. I didn't just
`41:20` means to think about this. I didn't just
`41:20` means to think about this. I didn't just come to these conclusions on my own.
`41:22` come to these conclusions on my own.
`41:22` come to these conclusions on my own. This has all been written about over
`41:23` This has all been written about over
`41:23` This has all been written about over years, if not hundreds of years. I mean,
`41:26` years, if not hundreds of years. I mean,
`41:26` years, if not hundreds of years. I mean, 50 years ago, you can learn stuff that
`41:28` 50 years ago, you can learn stuff that
`41:28` 50 years ago, you can learn stuff that will help you today if you look at what
`41:31` will help you today if you look at what
`41:31` will help you today if you look at what people were developing over the last few
`41:33` people were developing over the last few
`41:33` people were developing over the last few years, break it down, and look at the
`41:35` years, break it down, and look at the
`41:35` years, break it down, and look at the fundamentals.
`41:36` fundamentals.
`41:36` fundamentals. But I think I am done with this video.
`41:40` But I think I am done with this video.
`41:40` But I think I am done with this video. We should be done there. Um I'll put all
`41:42` We should be done there. Um I'll put all
`41:42` We should be done there. Um I'll put all these links, um these local models and
`41:44` these links, um these local models and
`41:44` these links, um these local models and other things like that. This is going to
`41:46` other things like that. This is going to
`41:46` other things like that. This is going to be a video that's turned into a course,
`41:48` be a video that's turned into a course,
`41:48` be a video that's turned into a course, as well. Um probably add an extra video
`41:51` as well. Um probably add an extra video
`41:51` as well. Um probably add an extra video or two after once I get a chance or
`41:52` or two after once I get a chance or
`41:52` or two after once I get a chance or maybe a text page. Uh so, please stay
`41:55` maybe a text page. Uh so, please stay
`41:55` maybe a text page. Uh so, please stay tuned. I hope you like this. I hope
`41:57` tuned. I hope you like this. I hope
`41:57` tuned. I hope you like this. I hope you've learned a lot. And uh yeah, don't
`41:59` you've learned a lot. And uh yeah, don't
`41:59` you've learned a lot. And uh yeah, don't have to waste tokens on Claude design.
`42:01` have to waste tokens on Claude design.
`42:01` have to waste tokens on Claude design. Have fun.
`42:02` Have fun.
`42:02` Have fun. Have a good day, everyone.
`42:04` Have a good day, everyone.
`42:04` Have a good day, everyone. Oh, and happy learning.