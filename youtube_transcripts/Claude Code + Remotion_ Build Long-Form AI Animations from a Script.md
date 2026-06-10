# Claude Code + Remotion: Build Long-Form AI Animations from a Script

**Channel:** Jake Van Clief  
**Uploaded:** 2026-03-06  
**Duration:** 22:31  
**URL:** [https://www.youtube.com/watch?v=vyN7ITKcGXU](https://www.youtube.com/watch?v=vyN7ITKcGXU)  

---

## Transcript

`00:02` the video you've all been waiting for.
`00:02` the video you've all been waiting for. How to make animations with Claude or
`00:04` How to make animations with Claude or
`00:04` How to make animations with Claude or any other coding bot for that matter
`00:06` any other coding bot for that matter
`00:06` any other coding bot for that matter that really look great. And what for
`00:08` that really look great. And what for
`00:08` that really look great. And what for those of you who don't know what I'm
`00:09` those of you who don't know what I'm
`00:09` those of you who don't know what I'm talking about, I mean specifically
`00:11` talking about, I mean specifically
`00:11` talking about, I mean specifically animations that can be 20, 30 minutes
`00:13` animations that can be 20, 30 minutes
`00:13` animations that can be 20, 30 minutes long aligned from a script in a
`00:15` long aligned from a script in a
`00:15` long aligned from a script in a relatively automated process where I
`00:17` relatively automated process where I
`00:17` relatively automated process where I say, "Hey, look at this script. Make me
`00:19` say, "Hey, look at this script. Make me
`00:20` say, "Hey, look at this script. Make me some animations on it." It's a little
`00:21` some animations on it." It's a little
`00:21` some animations on it." It's a little bit more complicated to set up, but once
`00:24` bit more complicated to set up, but once
`00:24` bit more complicated to set up, but once it's there, you're able to create
`00:25` it's there, you're able to create
`00:25` it's there, you're able to create automated scripts from all sorts of
`00:27` automated scripts from all sorts of
`00:27` automated scripts from all sorts of things and not just long form full
`00:29` things and not just long form full
`00:29` things and not just long form full shorts. And they don't have to look like
`00:30` shorts. And they don't have to look like
`00:30` shorts. And they don't have to look like this. They can look completely
`00:32` this. They can look completely
`00:32` this. They can look completely different. It's all whatever uh you know
`00:34` different. It's all whatever uh you know
`00:34` different. It's all whatever uh you know Claude can create uh within React
`00:37` Claude can create uh within React
`00:37` Claude can create uh within React framework which I'll explain here
`00:39` framework which I'll explain here
`00:39` framework which I'll explain here shortly. But let's go ahead and actually
`00:41` shortly. But let's go ahead and actually
`00:41` shortly. But let's go ahead and actually understand that what this will look
`00:43` understand that what this will look
`00:43` understand that what this will look like. [snorts] So essentially how I make
`00:47` like. [snorts] So essentially how I make
`00:47` like. [snorts] So essentially how I make these animations is more of a workflow
`00:49` these animations is more of a workflow
`00:49` these animations is more of a workflow that I've developed over the last few
`00:51` that I've developed over the last few
`00:51` that I've developed over the last few months. And it's off this idea that you
`00:54` months. And it's off this idea that you
`00:54` months. And it's off this idea that you don't need to necessarily build apps for
`00:56` don't need to necessarily build apps for
`00:56` don't need to necessarily build apps for everything.
`00:58` everything.
`00:58` everything. All I do is build an English in a
`01:01` All I do is build an English in a
`01:01` All I do is build an English in a document in a folder file and claude
`01:04` document in a folder file and claude
`01:04` document in a folder file and claude codes follows a series of processes uses
`01:07` codes follows a series of processes uses
`01:07` codes follows a series of processes uses libraries to create those animations
`01:09` libraries to create those animations
`01:09` libraries to create those animations that you just saw. I can use natural
`01:11` that you just saw. I can use natural
`01:11` that you just saw. I can use natural language to edit them. I can not even
`01:14` language to edit them. I can not even
`01:14` language to edit them. I can not even touch any of the files or I can edit
`01:16` touch any of the files or I can edit
`01:16` touch any of the files or I can edit every single process along the way. Now,
`01:19` every single process along the way. Now,
`01:19` every single process along the way. Now, the main things that you're going to
`01:21` the main things that you're going to
`01:21` the main things that you're going to need to do this is Claude Code,
`01:24` need to do this is Claude Code,
`01:24` need to do this is Claude Code, Remotion, NodeJS, and some Remotion
`01:27` Remotion, NodeJS, and some Remotion
`01:28` Remotion, NodeJS, and some Remotion skills from GitHub, which you can also
`01:29` skills from GitHub, which you can also
`01:30` skills from GitHub, which you can also just download those last two things from
`01:32` just download those last two things from
`01:32` just download those last two things from Claude Code. Actually, those three
`01:34` Claude Code. Actually, those three
`01:34` Claude Code. Actually, those three things, Remotion, Node.js, and Remotion
`01:36` things, Remotion, Node.js, and Remotion
`01:36` things, Remotion, Node.js, and Remotion skills, you can all have Claude do for
`01:38` skills, you can all have Claude do for
`01:38` skills, you can all have Claude do for you. If you don't know how to install
`01:41` you. If you don't know how to install
`01:41` you. If you don't know how to install Claude or Claude Code on your desktop, I
`01:43` Claude or Claude Code on your desktop, I
`01:43` Claude or Claude Code on your desktop, I have another free video that you can go
`01:45` have another free video that you can go
`01:45` have another free video that you can go check out that shows you how to get up
`01:46` check out that shows you how to get up
`01:46` check out that shows you how to get up to speed there. But this video is based
`01:48` to speed there. But this video is based
`01:48` to speed there. But this video is based under the understanding that you have
`01:49` under the understanding that you have
`01:49` under the understanding that you have already done that.
`01:51` already done that.
`01:51` already done that. Now, Remotion is essentially a library
`01:55` Now, Remotion is essentially a library
`01:55` Now, Remotion is essentially a library that allows you to take uh animations
`01:59` that allows you to take uh animations
`01:59` that allows you to take uh animations and build them with code. Now, what does
`02:02` and build them with code. Now, what does
`02:02` and build them with code. Now, what does that actually look like? So, there's a
`02:04` that actually look like? So, there's a
`02:04` that actually look like? So, there's a couple things here that I want to show
`02:06` couple things here that I want to show
`02:06` couple things here that I want to show you. Uh Remotion itself is essentially
`02:10` you. Uh Remotion itself is essentially
`02:10` you. Uh Remotion itself is essentially um this really great library. And what
`02:12` um this really great library. And what
`02:12` um this really great library. And what they realized is that React, which is
`02:14` they realized is that React, which is
`02:14` they realized is that React, which is the same stuff you program websites,
`02:17` the same stuff you program websites,
`02:17` the same stuff you program websites, this web page can be programmed in
`02:18` this web page can be programmed in
`02:18` this web page can be programmed in Typescript, React, things like that, can
`02:21` Typescript, React, things like that, can
`02:21` Typescript, React, things like that, can actually be lined up and you can create
`02:23` actually be lined up and you can create
`02:23` actually be lined up and you can create frames from each little animation that
`02:25` frames from each little animation that
`02:25` frames from each little animation that actually creates videos or animations or
`02:28` actually creates videos or animations or
`02:28` actually creates videos or animations or things like that. They also realized
`02:30` things like that. They also realized
`02:30` things like that. They also realized that Claude was really good at doing it.
`02:33` that Claude was really good at doing it.
`02:33` that Claude was really good at doing it. So, they went ahead and actually created
`02:35` So, they went ahead and actually created
`02:35` So, they went ahead and actually created uh skills for Claude to be able to use.
`02:38` uh skills for Claude to be able to use.
`02:38` uh skills for Claude to be able to use. So, if I go here and I go straight to
`02:40` So, if I go here and I go straight to
`02:40` So, if I go here and I go straight to their agent skills, they actually show
`02:43` their agent skills, they actually show
`02:43` their agent skills, they actually show you you can install them directly. Now,
`02:45` you you can install them directly. Now,
`02:45` you you can install them directly. Now, what they're doing is using an npx
`02:47` what they're doing is using an npx
`02:47` what they're doing is using an npx command, which if you don't have
`02:49` command, which if you don't have
`02:49` command, which if you don't have something called NodeJS installed, and
`02:51` something called NodeJS installed, and
`02:51` something called NodeJS installed, and don't worry, I create other courses
`02:53` don't worry, I create other courses
`02:53` don't worry, I create other courses diving into computer literacy. And what
`02:55` diving into computer literacy. And what
`02:55` diving into computer literacy. And what all this is, essentially, it's a way to
`02:57` all this is, essentially, it's a way to
`02:57` all this is, essentially, it's a way to use commands that download stuff from
`03:00` use commands that download stuff from
`03:00` use commands that download stuff from the internet without you having to
`03:01` the internet without you having to
`03:01` the internet without you having to interact with browsers. You don't
`03:03` interact with browsers. You don't
`03:03` interact with browsers. You don't necessarily have to do this. Claude can
`03:05` necessarily have to do this. Claude can
`03:05` necessarily have to do this. Claude can do this for you or you can download the
`03:08` do this for you or you can download the
`03:08` do this for you or you can download the actual GitHub itself. They have all of
`03:10` actual GitHub itself. They have all of
`03:10` actual GitHub itself. They have all of the skills. For those of you who don't
`03:12` the skills. For those of you who don't
`03:12` the skills. For those of you who don't know what a skills is, what skills are
`03:15` know what a skills is, what skills are
`03:15` know what a skills is, what skills are essentially think of them as large sets
`03:17` essentially think of them as large sets
`03:18` essentially think of them as large sets of prompts and instructions that someone
`03:20` of prompts and instructions that someone
`03:20` of prompts and instructions that someone else figured out how to do and realized,
`03:23` else figured out how to do and realized,
`03:23` else figured out how to do and realized, hey, let's just package this and let
`03:25` hey, let's just package this and let
`03:25` hey, let's just package this and let other people download it. So, Remotion
`03:27` other people download it. So, Remotion
`03:27` other people download it. So, Remotion has a skill that says, hey, this is how
`03:29` has a skill that says, hey, this is how
`03:29` has a skill that says, hey, this is how you use it. And then they created a
`03:31` you use it. And then they created a
`03:31` you use it. And then they created a bunch of subfiles so that claw doesn't
`03:33` bunch of subfiles so that claw doesn't
`03:33` bunch of subfiles so that claw doesn't have to read it all at once that handle
`03:35` have to read it all at once that handle
`03:36` have to read it all at once that handle 3D content or check if a video can be
`03:38` 3D content or check if a video can be
`03:38` 3D content or check if a video can be decoded or DOM elements or tailwind. All
`03:41` decoded or DOM elements or tailwind. All
`03:41` decoded or DOM elements or tailwind. All these concepts of design and
`03:43` these concepts of design and
`03:43` these concepts of design and visualization all packaged inside of a
`03:46` visualization all packaged inside of a
`03:46` visualization all packaged inside of a single, you know, section here, right?
`03:48` single, you know, section here, right?
`03:48` single, you know, section here, right? And you can actually come in and see and
`03:50` And you can actually come in and see and
`03:50` And you can actually come in and see and read all of these. They're all just
`03:52` read all of these. They're all just
`03:52` read all of these. They're all just natural language with some code, right?
`03:54` natural language with some code, right?
`03:54` natural language with some code, right? But the code doesn't run. The code is an
`03:57` But the code doesn't run. The code is an
`03:57` But the code doesn't run. The code is an explanation that Claude is reading. And
`03:59` explanation that Claude is reading. And
`03:59` explanation that Claude is reading. And we're going to dive into a little bit of
`04:00` we're going to dive into a little bit of
`04:00` we're going to dive into a little bit of that later. Again, you don't need to
`04:02` that later. Again, you don't need to
`04:02` that later. Again, you don't need to know what any of this is. You can just
`04:04` know what any of this is. You can just
`04:04` know what any of this is. You can just have Claude install this package and
`04:08` have Claude install this package and
`04:08` have Claude install this package and it'll run it. It'll know how to do it.
`04:11` it'll run it. It'll know how to do it.
`04:11` it'll run it. It'll know how to do it. And I'm going to walk through that a
`04:12` And I'm going to walk through that a
`04:12` And I'm going to walk through that a little bit now. So, option A is just add
`04:15` little bit now. So, option A is just add
`04:16` little bit now. So, option A is just add it to an existing project. You can tell
`04:18` it to an existing project. You can tell
`04:18` it to an existing project. You can tell Claude to run this. You can give it the
`04:19` Claude to run this. You can give it the
`04:19` Claude to run this. You can give it the GitHub repo. You can literally come in
`04:22` GitHub repo. You can literally come in
`04:22` GitHub repo. You can literally come in and you can say, you know, if you have
`04:25` and you can say, you know, if you have
`04:25` and you can say, you know, if you have Claude download, you can either do it
`04:26` Claude download, you can either do it
`04:26` Claude download, you can either do it through the app itself. Uh if you don't
`04:29` through the app itself. Uh if you don't
`04:29` through the app itself. Uh if you don't have Co-work the Pro Edition, that's
`04:31` have Co-work the Pro Edition, that's
`04:31` have Co-work the Pro Edition, that's okay. It can walk you through it, but I
`04:33` okay. It can walk you through it, but I
`04:33` okay. It can walk you through it, but I highly recommend using Claude code.
`04:34` highly recommend using Claude code.
`04:34` highly recommend using Claude code. You're going to need to do that. You can
`04:35` You're going to need to do that. You can
`04:36` You're going to need to do that. You can say, "Hey, hey, help me install uh
`04:40` say, "Hey, hey, help me install uh
`04:40` say, "Hey, hey, help me install uh Remotion." Give it the GitHub link.
`04:43` Remotion." Give it the GitHub link.
`04:43` Remotion." Give it the GitHub link. Literally, you can just come here. You
`04:45` Literally, you can just come here. You
`04:45` Literally, you can just come here. You can just take this or you can come here
`04:48` can just take this or you can come here
`04:48` can just take this or you can come here and take this website which is also the
`04:51` and take this website which is also the
`04:51` and take this website which is also the same thing and just basically say help
`04:55` same thing and just basically say help
`04:55` same thing and just basically say help me install remotion. Whoops.
`04:59` me install remotion. Whoops.
`04:59` me install remotion. Whoops. I also need NodeJS.
`05:03` I also need NodeJS.
`05:03` I also need NodeJS. It can walk you through how to install
`05:04` It can walk you through how to install
`05:04` It can walk you through how to install that but it's actually way simpler than
`05:06` that but it's actually way simpler than
`05:06` that but it's actually way simpler than you think. Just type in NodeJS
`05:10` you think. Just type in NodeJS
`05:10` you think. Just type in NodeJS and it looks something like this. And
`05:12` and it looks something like this. And
`05:12` and it looks something like this. And all you have to do is download this.
`05:14` all you have to do is download this.
`05:14` all you have to do is download this. What this is is essentially a framework
`05:17` What this is is essentially a framework
`05:17` What this is is essentially a framework for you to run JavaScript on your
`05:19` for you to run JavaScript on your
`05:19` for you to run JavaScript on your computer in a specific way. It gives you
`05:21` computer in a specific way. It gives you
`05:21` computer in a specific way. It gives you a couple of commands to be able to do
`05:24` a couple of commands to be able to do
`05:24` a couple of commands to be able to do things on your computer. And I actually
`05:26` things on your computer. And I actually
`05:26` things on your computer. And I actually recommend downloading this in general if
`05:28` recommend downloading this in general if
`05:28` recommend downloading this in general if you're getting into vibe coding or using
`05:30` you're getting into vibe coding or using
`05:30` you're getting into vibe coding or using AI in business because this allows you
`05:32` AI in business because this allows you
`05:32` AI in business because this allows you to download packages from GitHub and
`05:35` to download packages from GitHub and
`05:35` to download packages from GitHub and other places with a simple command
`05:36` other places with a simple command
`05:36` other places with a simple command rather than having to go there, download
`05:38` rather than having to go there, download
`05:38` rather than having to go there, download it, install it, and it just allows for a
`05:40` it, install it, and it just allows for a
`05:40` it, install it, and it just allows for a lot cleaner execution and installation.
`05:43` lot cleaner execution and installation.
`05:43` lot cleaner execution and installation. Um, but that's, you know, side note. So,
`05:46` Um, but that's, you know, side note. So,
`05:46` Um, but that's, you know, side note. So, you can add do it. You can install it
`05:48` you can add do it. You can install it
`05:48` you can add do it. You can install it manually. There's also a bunch of
`05:49` manually. There's also a bunch of
`05:49` manually. There's also a bunch of installations on YouTube you can check
`05:50` installations on YouTube you can check
`05:50` installations on YouTube you can check out and you can just comment and ask in
`05:53` out and you can just comment and ask in
`05:53` out and you can just comment and ask in the main hub if you're still having
`05:54` the main hub if you're still having
`05:54` the main hub if you're still having trouble building that. Once you have
`05:57` trouble building that. Once you have
`05:57` trouble building that. Once you have NodeJS installed and you have Remotion
`06:00` NodeJS installed and you have Remotion
`06:00` NodeJS installed and you have Remotion just installed to a basic folder, I
`06:02` just installed to a basic folder, I
`06:02` just installed to a basic folder, I mean, literally, you can come in, create
`06:06` mean, literally, you can come in, create
`06:06` mean, literally, you can come in, create a new folder, animations, wherever you
`06:09` a new folder, animations, wherever you
`06:09` a new folder, animations, wherever you want, on your desktop, anything like
`06:11` want, on your desktop, anything like
`06:11` want, on your desktop, anything like that. You can open it up. And now for
`06:13` that. You can open it up. And now for
`06:13` that. You can open it up. And now for me, I like to run all of this in VS
`06:15` me, I like to run all of this in VS
`06:16` me, I like to run all of this in VS Code. Again, watch my other video so you
`06:18` Code. Again, watch my other video so you
`06:18` Code. Again, watch my other video so you can see how I use Claude. But all VS
`06:20` can see how I use Claude. But all VS
`06:20` can see how I use Claude. But all VS Code is doing is it's a type of coding
`06:22` Code is doing is it's a type of coding
`06:22` Code is doing is it's a type of coding IDE that lets you see your folders a lot
`06:24` IDE that lets you see your folders a lot
`06:24` IDE that lets you see your folders a lot better. Right? This folder is literally
`06:28` better. Right? This folder is literally
`06:28` better. Right? This folder is literally just this one right here, right?
`06:29` just this one right here, right?
`06:30` just this one right here, right? Everything you're looking at here,
`06:31` Everything you're looking at here,
`06:31` Everything you're looking at here, right? Front end. Front end. It's all
`06:34` right? Front end. Front end. It's all
`06:34` right? Front end. Front end. It's all just letting me see the folder as a file
`06:37` just letting me see the folder as a file
`06:37` just letting me see the folder as a file tree rather than having to, you know,
`06:39` tree rather than having to, you know,
`06:39` tree rather than having to, you know, click through, click here, then click
`06:41` click through, click here, then click
`06:41` click through, click here, then click here, and so on and so forth. But
`06:43` here, and so on and so forth. But
`06:43` here, and so on and so forth. But basically, you just have Claude install
`06:45` basically, you just have Claude install
`06:45` basically, you just have Claude install it to a basic folder. Remotion will get
`06:47` it to a basic folder. Remotion will get
`06:47` it to a basic folder. Remotion will get installed. What it looks like for me
`06:49` installed. What it looks like for me
`06:49` installed. What it looks like for me now, I have a lot of extra skills and
`06:52` now, I have a lot of extra skills and
`06:52` now, I have a lot of extra skills and processes and things that I'm going to
`06:53` processes and things that I'm going to
`06:53` processes and things that I'm going to show you here shortly. Um, but
`06:56` show you here shortly. Um, but
`06:56` show you here shortly. Um, but essentially it's just going to actually
`06:58` essentially it's just going to actually
`06:58` essentially it's just going to actually install a couple of basic templates and
`07:00` install a couple of basic templates and
`07:00` install a couple of basic templates and like processes that Remotion will help
`07:03` like processes that Remotion will help
`07:03` like processes that Remotion will help you do and have a skill or it'll install
`07:05` you do and have a skill or it'll install
`07:05` you do and have a skill or it'll install the skill directly to Claude. Again,
`07:07` the skill directly to Claude. Again,
`07:07` the skill directly to Claude. Again, don't get overwhelmed by this if you're
`07:09` don't get overwhelmed by this if you're
`07:09` don't get overwhelmed by this if you're not a programmer. You don't need to use
`07:10` not a programmer. You don't need to use
`07:10` not a programmer. You don't need to use VS Code, but I have an intro video on
`07:13` VS Code, but I have an intro video on
`07:13` VS Code, but I have an intro video on how to install it and what that looks
`07:15` how to install it and what that looks
`07:15` how to install it and what that looks like. Again, you don't need to use these
`07:17` like. Again, you don't need to use these
`07:17` like. Again, you don't need to use these commands. You can have Claude help you
`07:18` commands. You can have Claude help you
`07:18` commands. You can have Claude help you install that, but it's good to learn
`07:21` install that, but it's good to learn
`07:21` install that, but it's good to learn because this is a skill that you will
`07:22` because this is a skill that you will
`07:22` because this is a skill that you will learn over time to actually help you do
`07:25` learn over time to actually help you do
`07:25` learn over time to actually help you do more things in the future with AI.
`07:28` more things in the future with AI.
`07:28` more things in the future with AI. Now, the main way I run with this is I
`07:31` Now, the main way I run with this is I
`07:31` Now, the main way I run with this is I have two main workspaces. And the
`07:33` have two main workspaces. And the
`07:33` have two main workspaces. And the workspaces are just folders. Again, this
`07:36` workspaces are just folders. Again, this
`07:36` workspaces are just folders. Again, this is just folders. No crazy apps or
`07:39` is just folders. No crazy apps or
`07:39` is just folders. No crazy apps or anything. I have a folder for my script
`07:42` anything. I have a folder for my script
`07:42` anything. I have a folder for my script lab which hosts all my long- form
`07:44` lab which hosts all my long- form
`07:44` lab which hosts all my long- form scripts as well as all of my short form
`07:47` scripts as well as all of my short form
`07:47` scripts as well as all of my short form scripts and then I also have a folder
`07:50` scripts and then I also have a folder
`07:50` scripts and then I also have a folder that has my animation studio. So it's
`07:52` that has my animation studio. So it's
`07:52` that has my animation studio. So it's like okay this is going to host my
`07:54` like okay this is going to host my
`07:54` like okay this is going to host my workflow. Right? So I bring my scripts
`07:56` workflow. Right? So I bring my scripts
`07:56` workflow. Right? So I bring my scripts in here which then is brought into
`07:59` in here which then is brought into
`07:59` in here which then is brought into creating a spec or specification file.
`08:02` creating a spec or specification file.
`08:02` creating a spec or specification file. Don't worry, I'm going to go detail what
`08:03` Don't worry, I'm going to go detail what
`08:03` Don't worry, I'm going to go detail what that is. But basically, think about it
`08:05` that is. But basically, think about it
`08:05` that is. But basically, think about it like a storyboard, right? Hey, you know,
`08:09` like a storyboard, right? Hey, you know,
`08:09` like a storyboard, right? Hey, you know, at 4 seconds in, this is what I'm
`08:11` at 4 seconds in, this is what I'm
`08:11` at 4 seconds in, this is what I'm saying. I want to make sure I have a
`08:13` saying. I want to make sure I have a
`08:13` saying. I want to make sure I have a visual philosophy here. There's key
`08:15` visual philosophy here. There's key
`08:15` visual philosophy here. There's key moments that I want. There's certain
`08:17` moments that I want. There's certain
`08:17` moments that I want. There's certain elements. The AI can build all of these.
`08:19` elements. The AI can build all of these.
`08:19` elements. The AI can build all of these. By the way, the reason you're doing this
`08:21` By the way, the reason you're doing this
`08:21` By the way, the reason you're doing this is because you can break it down into
`08:23` is because you can break it down into
`08:23` is because you can break it down into steps, right? This is super easy to
`08:26` steps, right? This is super easy to
`08:26` steps, right? This is super easy to edit. I can have the AI automate from
`08:28` edit. I can have the AI automate from
`08:28` edit. I can have the AI automate from script to animation or I can get deeply
`08:31` script to animation or I can get deeply
`08:31` script to animation or I can get deeply involved in editing the script and
`08:33` involved in editing the script and
`08:33` involved in editing the script and messing with it. And now you're starting
`08:35` messing with it. And now you're starting
`08:35` messing with it. And now you're starting to see why it's so nice to have this
`08:36` to see why it's so nice to have this
`08:36` to see why it's so nice to have this here because I can navigate the folders
`08:39` here because I can navigate the folders
`08:39` here because I can navigate the folders much simpler. I can go to my long form,
`08:41` much simpler. I can go to my long form,
`08:41` much simpler. I can go to my long form, have it opened up here and read it
`08:43` have it opened up here and read it
`08:43` have it opened up here and read it instead of just having to like go
`08:44` instead of just having to like go
`08:44` instead of just having to like go through, open it separately, read it,
`08:47` through, open it separately, read it,
`08:47` through, open it separately, read it, then close it. VS Code lets you just
`08:49` then close it. VS Code lets you just
`08:49` then close it. VS Code lets you just have it all on one screen. So that's
`08:51` have it all on one screen. So that's
`08:51` have it all on one screen. So that's another reason why you might want to do
`08:52` another reason why you might want to do
`08:52` another reason why you might want to do it. Again, not required. You can even do
`08:54` it. Again, not required. You can even do
`08:54` it. Again, not required. You can even do all of this through the main app by
`08:57` all of this through the main app by
`08:57` all of this through the main app by literally just se selecting your uh
`09:00` literally just se selecting your uh
`09:00` literally just se selecting your uh folder that you're operating in and it
`09:02` folder that you're operating in and it
`09:02` folder that you're operating in and it will work roughly the same.
`09:06` will work roughly the same.
`09:06` will work roughly the same. But anyway, so this is just a way for me
`09:08` But anyway, so this is just a way for me
`09:08` But anyway, so this is just a way for me to organize it. It also allows me to
`09:10` to organize it. It also allows me to
`09:10` to organize it. It also allows me to organize extra prompts, which I'm going
`09:12` organize extra prompts, which I'm going
`09:12` organize extra prompts, which I'm going to go into here shortly, but I want to
`09:15` to go into here shortly, but I want to
`09:15` to go into here shortly, but I want to think about the stages real quick.
`09:17` think about the stages real quick.
`09:17` think about the stages real quick. Essentially, what I do is I write a
`09:18` Essentially, what I do is I write a
`09:18` Essentially, what I do is I write a script or I have AI write a hundred
`09:20` script or I have AI write a hundred
`09:20` script or I have AI write a hundred scripts and then pick a couple out of
`09:22` scripts and then pick a couple out of
`09:22` scripts and then pick a couple out of it. Then I have the AI or myself take
`09:25` it. Then I have the AI or myself take
`09:25` it. Then I have the AI or myself take that script and might write a
`09:26` that script and might write a
`09:26` that script and might write a specification. Again, all of this in
`09:28` specification. Again, all of this in
`09:28` specification. Again, all of this in just basic English saying this is the
`09:31` just basic English saying this is the
`09:31` just basic English saying this is the kind of colors I want. This is what I
`09:33` kind of colors I want. This is what I
`09:33` kind of colors I want. This is what I want there. The AI can automate all four
`09:35` want there. The AI can automate all four
`09:35` want there. The AI can automate all four of these steps or it can touch none of
`09:37` of these steps or it can touch none of
`09:37` of these steps or it can touch none of the steps except for one. That's the
`09:39` the steps except for one. That's the
`09:39` the steps except for one. That's the whole beauty about my workspace here.
`09:42` whole beauty about my workspace here.
`09:42` whole beauty about my workspace here. Now, the build is where it actually
`09:44` Now, the build is where it actually
`09:44` Now, the build is where it actually starts writing code. And the code is
`09:46` starts writing code. And the code is
`09:46` starts writing code. And the code is just React, which is the front-end
`09:49` just React, which is the front-end
`09:49` just React, which is the front-end language, or it could be JavaScript and
`09:51` language, or it could be JavaScript and
`09:51` language, or it could be JavaScript and a couple other things for animations.
`09:54` a couple other things for animations.
`09:54` a couple other things for animations. So, when you look at an animation that
`09:56` So, when you look at an animation that
`09:56` So, when you look at an animation that looks like, whoopsie, that looks like
`09:58` looks like, whoopsie, that looks like
`09:58` looks like, whoopsie, that looks like this. Let's go here. Right? There's
`10:01` this. Let's go here. Right? There's
`10:01` this. Let's go here. Right? There's individual frames. Every single one of
`10:03` individual frames. Every single one of
`10:03` individual frames. Every single one of these frames requires some sort of
`10:06` these frames requires some sort of
`10:06` these frames requires some sort of little bit of code to create those
`10:08` little bit of code to create those
`10:08` little bit of code to create those animations, those dots. There's
`10:10` animations, those dots. There's
`10:10` animations, those dots. There's different sequences and scenes. And so
`10:14` different sequences and scenes. And so
`10:14` different sequences and scenes. And so AI the claude is going to break those
`10:16` AI the claude is going to break those
`10:16` AI the claude is going to break those down. What that actually looks like when
`10:19` down. What that actually looks like when
`10:19` down. What that actually looks like when it starts building from a script, right?
`10:21` it starts building from a script, right?
`10:21` it starts building from a script, right? And again, all I have to say literally
`10:24` And again, all I have to say literally
`10:24` And again, all I have to say literally is let's build
`10:27` is let's build
`10:27` is let's build a animation from a spec. And it
`10:32` a animation from a spec. And it
`10:32` a animation from a spec. And it immediately because of I how I have all
`10:34` immediately because of I how I have all
`10:34` immediately because of I how I have all these folders set up because of how I'm
`10:36` these folders set up because of how I'm
`10:36` these folders set up because of how I'm doing this. You don't necessarily need
`10:37` doing this. You don't necessarily need
`10:37` doing this. You don't necessarily need to do it this way. You can do it much
`10:39` to do it this way. You can do it much
`10:39` to do it this way. You can do it much more manually. But I have automated
`10:42` more manually. But I have automated
`10:42` more manually. But I have automated processes where I have a folder map in a
`10:45` processes where I have a folder map in a
`10:45` processes where I have a folder map in a context file which lets the cloud code
`10:47` context file which lets the cloud code
`10:47` context file which lets the cloud code be able to run through it. And this same
`10:49` be able to run through it. And this same
`10:49` be able to run through it. And this same exact thing I can say inside of the
`10:52` exact thing I can say inside of the
`10:52` exact thing I can say inside of the normal app as well. Let me actually just
`10:54` normal app as well. Let me actually just
`10:54` normal app as well. Let me actually just show you that right here. Uh let's see.
`11:00` show you that right here. Uh let's see.
`11:00` show you that right here. Uh let's see. Oops. Content writing select folder. If
`11:03` Oops. Content writing select folder. If
`11:04` Oops. Content writing select folder. If I ask the same thing, it's going to
`11:06` I ask the same thing, it's going to
`11:06` I ask the same thing, it's going to roughly give the same answer, right?
`11:07` roughly give the same answer, right?
`11:07` roughly give the same answer, right? It's this just a different UI. That's
`11:09` It's this just a different UI. That's
`11:09` It's this just a different UI. That's all this is. It's the same cloud code.
`11:11` all this is. It's the same cloud code.
`11:11` all this is. It's the same cloud code. And that's the beautiful part behind
`11:13` And that's the beautiful part behind
`11:13` And that's the beautiful part behind this is the software, the app is the
`11:16` this is the software, the app is the
`11:16` this is the software, the app is the folders and claude code is the running
`11:19` folders and claude code is the running
`11:19` folders and claude code is the running time. It's the thing that's actually
`11:20` time. It's the thing that's actually
`11:20` time. It's the thing that's actually running the software. And it's able to
`11:22` running the software. And it's able to
`11:22` running the software. And it's able to go through and find all my
`11:23` go through and find all my
`11:23` go through and find all my specifications, my pro like my animation
`11:26` specifications, my pro like my animation
`11:26` specifications, my pro like my animation things that I made from scripts. That
`11:28` things that I made from scripts. That
`11:28` things that I made from scripts. That easy. This is how I'm able to control
`11:29` easy. This is how I'm able to control
`11:30` easy. This is how I'm able to control all of this. It's just natural language.
`11:32` all of this. It's just natural language.
`11:32` all of this. It's just natural language. Then from there, I can say, hey, let's
`11:34` Then from there, I can say, hey, let's
`11:34` Then from there, I can say, hey, let's go ahead and build it. Now, I'm not
`11:37` go ahead and build it. Now, I'm not
`11:37` go ahead and build it. Now, I'm not going to do this in front of or for this
`11:39` going to do this in front of or for this
`11:39` going to do this in front of or for this one. just because I don't want to build
`11:40` one. just because I don't want to build
`11:40` one. just because I don't want to build any of these right now. But if you look
`11:42` any of these right now. But if you look
`11:42` any of these right now. But if you look at maybe this one that I have up here,
`11:45` at maybe this one that I have up here,
`11:45` at maybe this one that I have up here, right? I read my script for writing and
`11:48` right? I read my script for writing and
`11:48` right? I read my script for writing and tone understand it. We I gave it a
`11:50` tone understand it. We I gave it a
`11:50` tone understand it. We I gave it a transcript from a video as well and it
`11:52` transcript from a video as well and it
`11:52` transcript from a video as well and it was like, hey, I want to read this
`11:54` was like, hey, I want to read this
`11:54` was like, hey, I want to read this transcript. I literally just copy and
`11:56` transcript. I literally just copy and
`11:56` transcript. I literally just copy and pasted it. Let's go ahead think about
`11:58` pasted it. Let's go ahead think about
`11:58` pasted it. Let's go ahead think about this and think about actually building
`12:00` this and think about actually building
`12:00` this and think about actually building it. We kind of talked back and forth. I
`12:03` it. We kind of talked back and forth. I
`12:03` it. We kind of talked back and forth. I did something similar here as well. Um
`12:05` did something similar here as well. Um
`12:05` did something similar here as well. Um where I was like, "Hey, I want you to
`12:07` where I was like, "Hey, I want you to
`12:07` where I was like, "Hey, I want you to understand this and build this process."
`12:09` understand this and build this process."
`12:09` understand this and build this process." We can even go to other ones, right? Um
`12:12` We can even go to other ones, right? Um
`12:12` We can even go to other ones, right? Um is it going to show it? It's not going
`12:13` is it going to show it? It's not going
`12:13` is it going to show it? It's not going to show it right now. And all then is
`12:15` to show it right now. And all then is
`12:15` to show it right now. And all then is saying, "Hey, let's go for it. Go ahead
`12:17` saying, "Hey, let's go for it. Go ahead
`12:17` saying, "Hey, let's go for it. Go ahead and start building." And it's going to
`12:19` and start building." And it's going to
`12:19` and start building." And it's going to start thinking about the structure, what
`12:20` start thinking about the structure, what
`12:20` start thinking about the structure, what it's going to do, how it wants to work
`12:22` it's going to do, how it wants to work
`12:22` it's going to do, how it wants to work with it. Once in a while, I'm saying
`12:24` with it. Once in a while, I'm saying
`12:24` with it. Once in a while, I'm saying something here, you know, what's the
`12:25` something here, you know, what's the
`12:26` something here, you know, what's the value question? I'm actually writing the
`12:27` value question? I'm actually writing the
`12:27` value question? I'm actually writing the script in this process. We finally came
`12:30` script in this process. We finally came
`12:30` script in this process. We finally came to a decision. Let's go ahead and write
`12:32` to a decision. Let's go ahead and write
`12:32` to a decision. Let's go ahead and write the spec for it. Right? And then it just
`12:34` the spec for it. Right? And then it just
`12:34` the spec for it. Right? And then it just goes through. It knows what to do. You
`12:36` goes through. It knows what to do. You
`12:36` goes through. It knows what to do. You don't even need to see all of this. You
`12:37` don't even need to see all of this. You
`12:37` don't even need to see all of this. You could just do this in here in cloud code
`12:39` could just do this in here in cloud code
`12:39` could just do this in here in cloud code and it's really going to dive into all
`12:41` and it's really going to dive into all
`12:41` and it's really going to dive into all of that. From there, it actually builds
`12:44` of that. From there, it actually builds
`12:44` of that. From there, it actually builds the animations. And those animations are
`12:47` the animations. And those animations are
`12:47` the animations. And those animations are going to be stored in a separate file.
`12:49` going to be stored in a separate file.
`12:49` going to be stored in a separate file. It does this automatically. But just to
`12:51` It does this automatically. But just to
`12:51` It does this automatically. But just to give you an idea of what's going on
`12:52` give you an idea of what's going on
`12:52` give you an idea of what's going on behind the scenes, let's say I looked at
`12:55` behind the scenes, let's say I looked at
`12:55` behind the scenes, let's say I looked at my AI paradox kind of one. It's a very
`12:57` my AI paradox kind of one. It's a very
`12:57` my AI paradox kind of one. It's a very long YouTube video. I have a whole bunch
`12:59` long YouTube video. I have a whole bunch
`12:59` long YouTube video. I have a whole bunch of scenes that it's creating a bunch of
`13:01` of scenes that it's creating a bunch of
`13:01` of scenes that it's creating a bunch of React code for. Again, you don't know
`13:03` React code for. Again, you don't know
`13:03` React code for. Again, you don't know have to know how to do React. I'm just
`13:05` have to know how to do React. I'm just
`13:05` have to know how to do React. I'm just showing you this so you understand
`13:06` showing you this so you understand
`13:06` showing you this so you understand what's going on. Each of these are
`13:08` what's going on. Each of these are
`13:08` what's going on. Each of these are beats, animations that are going on that
`13:11` beats, animations that are going on that
`13:11` beats, animations that are going on that you're seeing right here. Right? So,
`13:13` you're seeing right here. Right? So,
`13:13` you're seeing right here. Right? So, that was scene one. Um, and that's the
`13:16` that was scene one. Um, and that's the
`13:16` that was scene one. Um, and that's the velocity gauge. So, what that is
`13:18` velocity gauge. So, what that is
`13:18` velocity gauge. So, what that is essentially is right here, right? That's
`13:21` essentially is right here, right? That's
`13:21` essentially is right here, right? That's that animation we're looking at. So,
`13:23` that animation we're looking at. So,
`13:23` that animation we're looking at. So, when I go through, we hit frames 800ish
`13:26` when I go through, we hit frames 800ish
`13:26` when I go through, we hit frames 800ish roughly. And next thing you know, boop,
`13:29` roughly. And next thing you know, boop,
`13:29` roughly. And next thing you know, boop, you're gonna go ahead and get this
`13:31` you're gonna go ahead and get this
`13:31` you're gonna go ahead and get this velocity gauge that's made there and
`13:33` velocity gauge that's made there and
`13:33` velocity gauge that's made there and animated. And all that is is right here,
`13:35` animated. And all that is is right here,
`13:35` animated. And all that is is right here, right? It's just a gauge, how big it is,
`13:37` right? It's just a gauge, how big it is,
`13:37` right? It's just a gauge, how big it is, what it's doing. This is great because
`13:39` what it's doing. This is great because
`13:39` what it's doing. This is great because then I can say, "Oh, I want to make that
`13:40` then I can say, "Oh, I want to make that
`13:40` then I can say, "Oh, I want to make that gauge bigger." And instead of me having
`13:42` gauge bigger." And instead of me having
`13:42` gauge bigger." And instead of me having to code and edit it, the AI is going to
`13:45` to code and edit it, the AI is going to
`13:45` to code and edit it, the AI is going to do that for me. And again, you don't
`13:46` do that for me. And again, you don't
`13:46` do that for me. And again, you don't even need to touch any of that. You
`13:48` even need to touch any of that. You
`13:48` even need to touch any of that. You don't have to look at it. It's just
`13:49` don't have to look at it. It's just
`13:49` don't have to look at it. It's just again understanding how I've created
`13:52` again understanding how I've created
`13:52` again understanding how I've created this automation to be editable at a
`13:54` this automation to be editable at a
`13:54` this automation to be editable at a professional level so you can start
`13:56` professional level so you can start
`13:56` professional level so you can start controlling it and maybe even making
`13:58` controlling it and maybe even making
`13:58` controlling it and maybe even making money from this process. Right? So
`14:01` money from this process. Right? So
`14:01` money from this process. Right? So that's kind of what happens in the build
`14:03` that's kind of what happens in the build
`14:03` that's kind of what happens in the build stage. Then finally, I just ask it to
`14:05` stage. Then finally, I just ask it to
`14:05` stage. Then finally, I just ask it to render it. And this is just like if
`14:06` render it. And this is just like if
`14:06` render it. And this is just like if you've used any video editor or you've
`14:08` you've used any video editor or you've
`14:08` you've used any video editor or you've just downloaded a video, it's kind of
`14:10` just downloaded a video, it's kind of
`14:10` just downloaded a video, it's kind of the same thing. It just renders it out
`14:12` the same thing. It just renders it out
`14:12` the same thing. It just renders it out and essentially creates a video that you
`14:15` and essentially creates a video that you
`14:15` and essentially creates a video that you can then just throw into Cap Cut or
`14:16` can then just throw into Cap Cut or
`14:16` can then just throw into Cap Cut or something like that, right? Um, it takes
`14:19` something like that, right? Um, it takes
`14:19` something like that, right? Um, it takes that video, renders all the frames, and
`14:21` that video, renders all the frames, and
`14:21` that video, renders all the frames, and puts it into something. So, like you can
`14:22` puts it into something. So, like you can
`14:22` puts it into something. So, like you can come in, right? Um, and this is a a uh
`14:26` come in, right? Um, and this is a a uh
`14:26` come in, right? Um, and this is a a uh one that I'm actually working on right
`14:28` one that I'm actually working on right
`14:28` one that I'm actually working on right now. And it you can just upload it in,
`14:31` now. And it you can just upload it in,
`14:31` now. And it you can just upload it in, right? I've got the animation here. And
`14:33` right? I've got the animation here. And
`14:33` right? I've got the animation here. And then boom, you can attach sound to it.
`14:35` then boom, you can attach sound to it.
`14:35` then boom, you can attach sound to it. You can do voiceovers, you can do
`14:36` You can do voiceovers, you can do
`14:36` You can do voiceovers, you can do captions, all that good jazz. And do all
`14:39` captions, all that good jazz. And do all
`14:39` captions, all that good jazz. And do all your normal video editing uh if you want
`14:41` your normal video editing uh if you want
`14:41` your normal video editing uh if you want as well, which is very strong in that
`14:43` as well, which is very strong in that
`14:43` as well, which is very strong in that aspect.
`14:45` aspect.
`14:45` aspect. Most people think the code is the hard
`14:46` Most people think the code is the hard
`14:46` Most people think the code is the hard part, but again, it's actually the spec,
`14:49` part, but again, it's actually the spec,
`14:49` part, but again, it's actually the spec, the specifications for what the agent is
`14:52` the specifications for what the agent is
`14:52` the specifications for what the agent is building, what is actually being built.
`14:55` building, what is actually being built.
`14:55` building, what is actually being built. The spec is specifically, I know I just
`14:58` The spec is specifically, I know I just
`14:58` The spec is specifically, I know I just described it a bit, a contract between
`15:00` described it a bit, a contract between
`15:00` described it a bit, a contract between the voice over recording and the
`15:02` the voice over recording and the
`15:02` the voice over recording and the animation. It's the thing that's making
`15:04` animation. It's the thing that's making
`15:04` animation. It's the thing that's making sure that the timing of the script is
`15:06` sure that the timing of the script is
`15:06` sure that the timing of the script is carried over into when the animations
`15:09` carried over into when the animations
`15:09` carried over into when the animations are. And again, it's just written in
`15:11` are. And again, it's just written in
`15:11` are. And again, it's just written in plain English. You can you can edit
`15:13` plain English. You can you can edit
`15:13` plain English. You can you can edit anything you want about it. my specs uh
`15:16` anything you want about it. my specs uh
`15:16` anything you want about it. my specs uh for like let's look at this you know the
`15:18` for like let's look at this you know the
`15:18` for like let's look at this you know the one we were just talking about uh it's a
`15:21` one we were just talking about uh it's a
`15:21` one we were just talking about uh it's a long form one uh which is the AI paradox
`15:24` long form one uh which is the AI paradox
`15:24` long form one uh which is the AI paradox again it's talking about timestamps it's
`15:27` again it's talking about timestamps it's
`15:27` again it's talking about timestamps it's looking at duration I'm able to edit
`15:29` looking at duration I'm able to edit
`15:29` looking at duration I'm able to edit this like oh wait hold on I think we're
`15:31` this like oh wait hold on I think we're
`15:31` this like oh wait hold on I think we're off by 20 seconds here or I can have the
`15:33` off by 20 seconds here or I can have the
`15:33` off by 20 seconds here or I can have the AI read through it I can write what I
`15:35` AI read through it I can write what I
`15:35` AI read through it I can write what I want my visual philosophy to be and
`15:37` want my visual philosophy to be and
`15:37` want my visual philosophy to be and that's it that's all it is is a timeline
`15:40` that's it that's all it is is a timeline
`15:40` that's it that's all it is is a timeline of what it looks like and the timestamps
`15:42` of what it looks like and the timestamps
`15:42` of what it looks like and the timestamps and again the AI can just build that.
`15:45` and again the AI can just build that.
`15:45` and again the AI can just build that. And I do have spec templates that
`15:47` And I do have spec templates that
`15:47` And I do have spec templates that already have this all set up and in a in
`15:50` already have this all set up and in a in
`15:50` already have this all set up and in a in a certain way. Make sure to um hit me up
`15:52` a certain way. Make sure to um hit me up
`15:52` a certain way. Make sure to um hit me up if you want this. I will say I am
`15:54` if you want this. I will say I am
`15:54` if you want this. I will say I am charging for this. I'm sorry. I've put a
`15:57` charging for this. I'm sorry. I've put a
`15:57` charging for this. I'm sorry. I've put a lot of work into this. But again, it
`15:58` lot of work into this. But again, it
`15:58` lot of work into this. But again, it comes with the $7 a month um fee that
`16:01` comes with the $7 a month um fee that
`16:01` comes with the $7 a month um fee that I'm charging. So that's it. I'm not
`16:03` I'm charging. So that's it. I'm not
`16:03` I'm charging. So that's it. I'm not charging like hundreds of dollars. I'm
`16:04` charging like hundreds of dollars. I'm
`16:04` charging like hundreds of dollars. I'm just seven bucks, bro. That's all I'm
`16:06` just seven bucks, bro. That's all I'm
`16:06` just seven bucks, bro. That's all I'm asking for all this is a lot of hard
`16:08` asking for all this is a lot of hard
`16:08` asking for all this is a lot of hard work. You know what I mean? Um, but if
`16:10` work. You know what I mean? Um, but if
`16:10` work. You know what I mean? Um, but if you want any of these files, also I'm
`16:12` you want any of these files, also I'm
`16:12` you want any of these files, also I'm going to have a much deeper video that
`16:14` going to have a much deeper video that
`16:14` going to have a much deeper video that is going to be behind the $7 a month
`16:16` is going to be behind the $7 a month
`16:16` is going to be behind the $7 a month payw wall going into how you can build
`16:18` payw wall going into how you can build
`16:18` payw wall going into how you can build your own versions of these or take these
`16:20` your own versions of these or take these
`16:20` your own versions of these or take these and turn them into someone else. But
`16:22` and turn them into someone else. But
`16:22` and turn them into someone else. But again, I have access to all this. Just
`16:24` again, I have access to all this. Just
`16:24` again, I have access to all this. Just either message me or um yeah, actually,
`16:26` either message me or um yeah, actually,
`16:26` either message me or um yeah, actually, yeah, just message me before you
`16:28` yeah, just message me before you
`16:28` yeah, just message me before you subscribe. Let me know that you're going
`16:30` subscribe. Let me know that you're going
`16:30` subscribe. Let me know that you're going to I'll get them to you and we'll
`16:32` to I'll get them to you and we'll
`16:32` to I'll get them to you and we'll actually create a more automated process
`16:33` actually create a more automated process
`16:33` actually create a more automated process for that in the future. But anyway,
`16:36` for that in the future. But anyway,
`16:36` for that in the future. But anyway, continuing, right? Let's say you don't
`16:37` continuing, right? Let's say you don't
`16:37` continuing, right? Let's say you don't want to do that. You just kind of build
`16:39` want to do that. You just kind of build
`16:39` want to do that. You just kind of build this all on your own. You take the
`16:40` this all on your own. You take the
`16:40` this all on your own. You take the transcript from this video. Pretty much
`16:43` transcript from this video. Pretty much
`16:43` transcript from this video. Pretty much the spec is just containing these four
`16:45` the spec is just containing these four
`16:45` the spec is just containing these four things. A beat map, so every moment,
`16:47` things. A beat map, so every moment,
`16:47` things. A beat map, so every moment, visual philosophy, what the viewer
`16:50` visual philosophy, what the viewer
`16:50` visual philosophy, what the viewer should understand, key moments, and
`16:52` should understand, key moments, and
`16:52` should understand, key moments, and audio sync points. Those are the key
`16:54` audio sync points. Those are the key
`16:54` audio sync points. Those are the key parts of all of it. What it doesn't
`16:56` parts of all of it. What it doesn't
`16:56` parts of all of it. What it doesn't contain is like specific frame numbers.
`16:58` contain is like specific frame numbers.
`16:58` contain is like specific frame numbers. There's no talks of pixel positions, no
`17:00` There's no talks of pixel positions, no
`17:00` There's no talks of pixel positions, no component props, and no code. I did that
`17:03` component props, and no code. I did that
`17:03` component props, and no code. I did that before and I actually found that
`17:05` before and I actually found that
`17:05` before and I actually found that constricted the model and made it not do
`17:07` constricted the model and made it not do
`17:08` constricted the model and made it not do enough right it actually made the
`17:09` enough right it actually made the
`17:09` enough right it actually made the animations worse by controlling it
`17:11` animations worse by controlling it
`17:12` animations worse by controlling it giving cloud code a little bit of
`17:14` giving cloud code a little bit of
`17:14` giving cloud code a little bit of creativism is a really great thing so
`17:17` creativism is a really great thing so
`17:17` creativism is a really great thing so from end to end it's script what needs
`17:20` from end to end it's script what needs
`17:20` from end to end it's script what needs to be said spec generate from the script
`17:24` to be said spec generate from the script
`17:24` to be said spec generate from the script output and uh I kind of gave a live demo
`17:27` output and uh I kind of gave a live demo
`17:27` output and uh I kind of gave a live demo I made it in this slide point where I
`17:28` I made it in this slide point where I
`17:28` I made it in this slide point where I give you one but I decided just to do
`17:30` give you one but I decided just to do
`17:30` give you one but I decided just to do live demos throughout the entire thing.
`17:32` live demos throughout the entire thing.
`17:32` live demos throughout the entire thing. Um, again, Claude is just building it.
`17:35` Um, again, Claude is just building it.
`17:35` Um, again, Claude is just building it. It's just pulling in creating sequences
`17:37` It's just pulling in creating sequences
`17:37` It's just pulling in creating sequences and you can actually watch it happening
`17:39` and you can actually watch it happening
`17:39` and you can actually watch it happening right here. It's sitting here and it's
`17:41` right here. It's sitting here and it's
`17:41` right here. It's sitting here and it's reading all the files and then it's
`17:43` reading all the files and then it's
`17:43` reading all the files and then it's writing something. It's like, oh, let me
`17:44` writing something. It's like, oh, let me
`17:44` writing something. It's like, oh, let me write a transition. Let me write some
`17:47` write a transition. Let me write some
`17:47` write a transition. Let me write some sort of uh frames and constants. Let me
`17:49` sort of uh frames and constants. Let me
`17:49` sort of uh frames and constants. Let me actually import React and actually write
`17:51` actually import React and actually write
`17:51` actually import React and actually write these in every single file. And then
`17:54` these in every single file. And then
`17:54` these in every single file. And then from there, you can actually see it
`17:55` from there, you can actually see it
`17:55` from there, you can actually see it building all of these. And again, the
`17:57` building all of these. And again, the
`17:57` building all of these. And again, the same thing in here if you wanted to
`17:59` same thing in here if you wanted to
`17:59` same thing in here if you wanted to watch it actually do that. I wonder if I
`18:02` watch it actually do that. I wonder if I
`18:02` watch it actually do that. I wonder if I have um Hold on, let me look and see.
`18:05` have um Hold on, let me look and see.
`18:06` have um Hold on, let me look and see. Here we go. Is this uh No. Uh this
`18:09` Here we go. Is this uh No. Uh this
`18:09` Here we go. Is this uh No. Uh this remote control session. Yeah. So, right
`18:11` remote control session. Yeah. So, right
`18:11` remote control session. Yeah. So, right here, it's the same exact thing. I'm
`18:12` here, it's the same exact thing. I'm
`18:12` here, it's the same exact thing. I'm just saying um let's do this specific
`18:16` just saying um let's do this specific
`18:16` just saying um let's do this specific script, right? Agents 20 bucks. I like
`18:18` script, right? Agents 20 bucks. I like
`18:18` script, right? Agents 20 bucks. I like that hook. Cool. I don't like what you
`18:21` that hook. Cool. I don't like what you
`18:21` that hook. Cool. I don't like what you changed on it. Um we're just kind of
`18:23` changed on it. Um we're just kind of
`18:23` changed on it. Um we're just kind of talking back and forth on what the
`18:25` talking back and forth on what the
`18:25` talking back and forth on what the script is and what the spec could be. it
`18:27` script is and what the spec could be. it
`18:27` script is and what the spec could be. it finally came up with the script that I'm
`18:29` finally came up with the script that I'm
`18:29` finally came up with the script that I'm like, "Hey, I'm actually using this
`18:31` like, "Hey, I'm actually using this
`18:31` like, "Hey, I'm actually using this through my phone here." So, I set up
`18:33` through my phone here." So, I set up
`18:33` through my phone here." So, I set up remote access so I can pick up my phone
`18:35` remote access so I can pick up my phone
`18:35` remote access so I can pick up my phone and actually message my computer. Uh,
`18:38` and actually message my computer. Uh,
`18:38` and actually message my computer. Uh, again, I'm making a whole course on
`18:39` again, I'm making a whole course on
`18:40` again, I'm making a whole course on that. That is something you should
`18:41` that. That is something you should
`18:41` that. That is something you should subscribe to as well to to build it.
`18:43` subscribe to as well to to build it.
`18:43` subscribe to as well to to build it. We're building it slowly. I'm setting it
`18:45` We're building it slowly. I'm setting it
`18:45` We're building it slowly. I'm setting it all up, but super good there. Then from
`18:47` all up, but super good there. Then from
`18:48` all up, but super good there. Then from there, I'm just kind of messing around
`18:50` there, I'm just kind of messing around
`18:50` there, I'm just kind of messing around with it and seeing it and actually
`18:51` with it and seeing it and actually
`18:51` with it and seeing it and actually having it build these and build out that
`18:53` having it build these and build out that
`18:53` having it build these and build out that animation. And that's how I'm able to
`18:55` animation. And that's how I'm able to
`18:55` animation. And that's how I'm able to build all of these animations that you
`18:58` build all of these animations that you
`18:58` build all of these animations that you just saw. Literally, every single one of
`18:59` just saw. Literally, every single one of
`18:59` just saw. Literally, every single one of these was built that way, edited that
`19:02` these was built that way, edited that
`19:02` these was built that way, edited that way. Some of them are good, some of them
`19:04` way. Some of them are good, some of them
`19:04` way. Some of them are good, some of them are better than others. I'm learning new
`19:05` are better than others. I'm learning new
`19:05` are better than others. I'm learning new animations, right? This one I really
`19:07` animations, right? This one I really
`19:07` animations, right? This one I really loved how it turned out. You can create
`19:09` loved how it turned out. You can create
`19:09` loved how it turned out. You can create all sorts of fun stuff. So, yeah, that's
`19:11` all sorts of fun stuff. So, yeah, that's
`19:12` all sorts of fun stuff. So, yeah, that's kind of how that all works. Now, there's
`19:14` kind of how that all works. Now, there's
`19:14` kind of how that all works. Now, there's also, uh, you know, I was just saying
`19:16` also, uh, you know, I was just saying
`19:16` also, uh, you know, I was just saying that I'm going to be creating a bunch
`19:17` that I'm going to be creating a bunch
`19:17` that I'm going to be creating a bunch more courses and classes all on this
`19:20` more courses and classes all on this
`19:20` more courses and classes all on this one. I do have a GitHub repo called
`19:22` one. I do have a GitHub repo called
`19:22` one. I do have a GitHub repo called model workspace protocol. This describes
`19:24` model workspace protocol. This describes
`19:24` model workspace protocol. This describes my reasoning behind this method and not
`19:26` my reasoning behind this method and not
`19:26` my reasoning behind this method and not only how it makes animations, but how
`19:28` only how it makes animations, but how
`19:28` only how it makes animations, but how it's actually able to create entire uh
`19:32` it's actually able to create entire uh
`19:32` it's actually able to create entire uh you know the very thing that you're
`19:33` you know the very thing that you're
`19:33` you know the very thing that you're looking at right now this PowerPoint
`19:35` looking at right now this PowerPoint
`19:35` looking at right now this PowerPoint this same process allowed me to create
`19:38` this same process allowed me to create
`19:38` this same process allowed me to create powerpoints from my thinking my work.
`19:41` powerpoints from my thinking my work.
`19:41` powerpoints from my thinking my work. The PowerPoint that you're watching was
`19:42` The PowerPoint that you're watching was
`19:42` The PowerPoint that you're watching was made by Claude Code in let's see one,
`19:46` made by Claude Code in let's see one,
`19:46` made by Claude Code in let's see one, two, three, four prompts. Four prompts
`19:50` two, three, four prompts. Four prompts
`19:50` two, three, four prompts. Four prompts made this whole beautiful thing from my
`19:52` made this whole beautiful thing from my
`19:52` made this whole beautiful thing from my method. And it's all from my writing, my
`19:54` method. And it's all from my writing, my
`19:54` method. And it's all from my writing, my tones, the colors that I actually want
`19:57` tones, the colors that I actually want
`19:57` tones, the colors that I actually want and the edits that I want. And I am
`20:00` and the edits that I want. And I am
`20:00` and the edits that I want. And I am writing a research paper on this that I
`20:01` writing a research paper on this that I
`20:02` writing a research paper on this that I will be sharing as well because there's
`20:03` will be sharing as well because there's
`20:03` will be sharing as well because there's a lot of effects and deepness behind
`20:05` a lot of effects and deepness behind
`20:05` a lot of effects and deepness behind this that goes back into the 70s about
`20:07` this that goes back into the 70s about
`20:07` this that goes back into the 70s about software. and I'm very happy to share
`20:09` software. and I'm very happy to share
`20:09` software. and I'm very happy to share that with all of you for free. That
`20:10` that with all of you for free. That
`20:10` that with all of you for free. That one's going to be free. Um, and I'm
`20:13` one's going to be free. Um, and I'm
`20:13` one's going to be free. Um, and I'm creating a workspace protocol course on
`20:15` creating a workspace protocol course on
`20:15` creating a workspace protocol course on all of this. So, I'd love your feedback
`20:17` all of this. So, I'd love your feedback
`20:17` all of this. So, I'd love your feedback on that as well. So, again, for you, I
`20:20` on that as well. So, again, for you, I
`20:20` on that as well. So, again, for you, I think what a great way to start out with
`20:21` think what a great way to start out with
`20:21` think what a great way to start out with this is come up with a script and a
`20:24` this is come up with a script and a
`20:24` this is come up with a script and a topic. Map out what you want that topic
`20:27` topic. Map out what you want that topic
`20:27` topic. Map out what you want that topic to be, what you want it to look like,
`20:28` to be, what you want it to look like,
`20:28` to be, what you want it to look like, and just ask Claude, "Hey, can you go
`20:31` and just ask Claude, "Hey, can you go
`20:31` and just ask Claude, "Hey, can you go ahead and write me out a markdown file?"
`20:34` ahead and write me out a markdown file?"
`20:34` ahead and write me out a markdown file?" Right? literally come in and say, "Hey,
`20:38` Right? literally come in and say, "Hey,
`20:38` Right? literally come in and say, "Hey, Claude,"
`20:40` Claude,"
`20:40` Claude," and you're working inside a folder that
`20:42` and you're working inside a folder that
`20:42` and you're working inside a folder that you've actually installed Remotion in.
`20:44` you've actually installed Remotion in.
`20:44` you've actually installed Remotion in. Can you write me a script or give Claude
`20:49` Can you write me a script or give Claude
`20:49` Can you write me a script or give Claude a script and then a spec and just
`20:52` a script and then a spec and just
`20:52` a script and then a spec and just describe what it is? Or if you've gotten
`20:54` describe what it is? Or if you've gotten
`20:54` describe what it is? Or if you've gotten these specs from me, do that. But just
`20:56` these specs from me, do that. But just
`20:56` these specs from me, do that. But just like video animation beat by beat, you
`21:00` like video animation beat by beat, you
`21:00` like video animation beat by beat, you can literally just start with that for
`21:03` can literally just start with that for
`21:03` can literally just start with that for that script.
`21:05` that script.
`21:05` that script. Right. And make sure you're inside of a
`21:08` Right. And make sure you're inside of a
`21:08` Right. And make sure you're inside of a folder that helps you with that. And
`21:11` folder that helps you with that. And
`21:11` folder that helps you with that. And then literally just say, "Let's go."
`21:12` then literally just say, "Let's go."
`21:12` then literally just say, "Let's go." That's what you want to practice first.
`21:14` That's what you want to practice first.
`21:14` That's what you want to practice first. Oops, I forgot to mount my my file, but
`21:16` Oops, I forgot to mount my my file, but
`21:16` Oops, I forgot to mount my my file, but that's this isn't a problem you're going
`21:18` that's this isn't a problem you're going
`21:18` that's this isn't a problem you're going to encounter necessarily. This is my
`21:20` to encounter necessarily. This is my
`21:20` to encounter necessarily. This is my fault. I I messed it up. Uh I'll show
`21:22` fault. I I messed it up. Uh I'll show
`21:22` fault. I I messed it up. Uh I'll show you on here instead. Um and it's just
`21:24` you on here instead. Um and it's just
`21:24` you on here instead. Um and it's just just do that, right? Just send it in. Um
`21:27` just do that, right? Just send it in. Um
`21:27` just do that, right? Just send it in. Um and it should be able to help you out
`21:29` and it should be able to help you out
`21:29` and it should be able to help you out pretty well with that aspect. If you
`21:31` pretty well with that aspect. If you
`21:31` pretty well with that aspect. If you don't, again, I'm going to be doing a
`21:33` don't, again, I'm going to be doing a
`21:33` don't, again, I'm going to be doing a much more deep inline course on all of
`21:36` much more deep inline course on all of
`21:36` much more deep inline course on all of this and you can always reach out and
`21:37` this and you can always reach out and
`21:37` this and you can always reach out and we're going to be doing kind of virtual
`21:39` we're going to be doing kind of virtual
`21:39` we're going to be doing kind of virtual things, but that's something that I
`21:41` things, but that's something that I
`21:41` things, but that's something that I think you would should dive into. Some
`21:43` think you would should dive into. Some
`21:43` think you would should dive into. Some of our community members have already
`21:44` of our community members have already
`21:44` of our community members have already been doing this from what I've shown you
`21:46` been doing this from what I've shown you
`21:46` been doing this from what I've shown you all here. So, if we actually come in, we
`21:49` all here. So, if we actually come in, we
`21:49` all here. So, if we actually come in, we can see some amazing ones that David has
`21:51` can see some amazing ones that David has
`21:51` can see some amazing ones that David has already made from this kind of process.
`21:53` already made from this kind of process.
`21:53` already made from this kind of process. Um, he did a really great one on N8N.
`21:55` Um, he did a really great one on N8N.
`21:55` Um, he did a really great one on N8N. Um, and I gave him some suggestions as
`21:58` Um, and I gave him some suggestions as
`21:58` Um, and I gave him some suggestions as well. So, please share them in here and
`21:59` well. So, please share them in here and
`21:59` well. So, please share them in here and any trouble you have, please dive into
`22:02` any trouble you have, please dive into
`22:02` any trouble you have, please dive into it. Uh, this will probably be posted
`22:04` it. Uh, this will probably be posted
`22:04` it. Uh, this will probably be posted after this afternoon tea talk, but every
`22:06` after this afternoon tea talk, but every
`22:06` after this afternoon tea talk, but every two weeks we do a little afternoon tea
`22:09` two weeks we do a little afternoon tea
`22:09` two weeks we do a little afternoon tea where I invite some CEOs in. So, I
`22:11` where I invite some CEOs in. So, I
`22:11` where I invite some CEOs in. So, I please recommend all of you to dive into
`22:13` please recommend all of you to dive into
`22:13` please recommend all of you to dive into that. But other than that, that is the
`22:15` that. But other than that, that is the
`22:15` that. But other than that, that is the end of all of this. I very much
`22:17` end of all of this. I very much
`22:17` end of all of this. I very much appreciate you all being a part of this.
`22:19` appreciate you all being a part of this.
`22:19` appreciate you all being a part of this. I hope this is great. This is part of my
`22:21` I hope this is great. This is part of my
`22:21` I hope this is great. This is part of my free series. I'm going to be doing much
`22:23` free series. I'm going to be doing much
`22:23` free series. I'm going to be doing much more long-term courses to help you all
`22:25` more long-term courses to help you all
`22:25` more long-term courses to help you all out with this in the future. Um, and I
`22:28` out with this in the future. Um, and I
`22:28` out with this in the future. Um, and I can't wait to talk and build with all of
`22:30` can't wait to talk and build with all of
`22:30` can't wait to talk and build with all of you.