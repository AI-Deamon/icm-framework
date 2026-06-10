# Video as Code: My AI Animation Stack

**Channel:** Jake Van Clief  
**Uploaded:** 2026-02-07  
**Duration:** 13:12  
**URL:** [https://www.youtube.com/watch?v=yEa6dgh7wuc](https://www.youtube.com/watch?v=yEa6dgh7wuc)  

---

## Transcript

`00:02` The animations that you're going to see
`00:02` The animations that you're going to see in this video would have taken me
`00:04` in this video would have taken me
`00:04` in this video would have taken me probably a full week, if not a month, to
`00:05` probably a full week, if not a month, to
`00:06` probably a full week, if not a month, to make. And now I make them in under an
`00:08` make. And now I make them in under an
`00:08` make. And now I make them in under an hour. And honestly, they turn out pretty
`00:11` hour. And honestly, they turn out pretty
`00:11` hour. And honestly, they turn out pretty great. I've made all sorts of different
`00:13` great. I've made all sorts of different
`00:13` great. I've made all sorts of different types. And I know how that sounds,
`00:15` types. And I know how that sounds,
`00:15` types. And I know how that sounds, right? This idea that, okay, it's an AI
`00:17` right? This idea that, okay, it's an AI
`00:17` right? This idea that, okay, it's an AI video. AI promises this something
`00:19` video. AI promises this something
`00:19` video. AI promises this something revolutionary, gamechanging, the future
`00:22` revolutionary, gamechanging, the future
`00:22` revolutionary, gamechanging, the future of content, and then you try it and the
`00:24` of content, and then you try it and the
`00:24` of content, and then you try it and the output's mediocre, uncanny, or require
`00:26` output's mediocre, uncanny, or require
`00:26` output's mediocre, uncanny, or require so much cleanup that you wonder why you
`00:27` so much cleanup that you wonder why you
`00:27` so much cleanup that you wonder why you bothered. But that's exactly why. and
`00:29` bothered. But that's exactly why. and
`00:29` bothered. But that's exactly why. and how I want to show you this. It's not
`00:32` how I want to show you this. It's not
`00:32` how I want to show you this. It's not polish results, but the process and what
`00:33` polish results, but the process and what
`00:34` polish results, but the process and what you'll find isn't magic. It's
`00:35` you'll find isn't magic. It's
`00:35` you'll find isn't magic. It's infrastructure. It's documentation,
`00:37` infrastructure. It's documentation,
`00:37` infrastructure. It's documentation, specifications, component libraries.
`00:39` specifications, component libraries.
`00:39` specifications, component libraries. It's honestly software engineering
`00:41` It's honestly software engineering
`00:41` It's honestly software engineering applied to a creative problem. But let
`00:43` applied to a creative problem. But let
`00:43` applied to a creative problem. But let me go ahead and start with what you need
`00:46` me go ahead and start with what you need
`00:46` me go ahead and start with what you need if you wanted to do this yourself. I use
`00:48` if you wanted to do this yourself. I use
`00:48` if you wanted to do this yourself. I use cloud code, but you can use codeex or
`00:50` cloud code, but you can use codeex or
`00:50` cloud code, but you can use codeex or any other sort of coding agent. Um, on
`00:53` any other sort of coding agent. Um, on
`00:53` any other sort of coding agent. Um, on top of that, I also use some sort of
`00:55` top of that, I also use some sort of
`00:55` top of that, I also use some sort of IDE. You can use VS Code, cursor,
`00:57` IDE. You can use VS Code, cursor,
`00:57` IDE. You can use VS Code, cursor, anti-gravity, and just throw the plug in
`00:59` anti-gravity, and just throw the plug in
`00:59` anti-gravity, and just throw the plug in for each of those. Finally, I use a
`01:01` for each of those. Finally, I use a
`01:01` for each of those. Finally, I use a library called Remotion, uh, which
`01:03` library called Remotion, uh, which
`01:03` library called Remotion, uh, which generates most of the processes, and
`01:05` generates most of the processes, and
`01:05` generates most of the processes, and then I throw that all into some sort of
`01:07` then I throw that all into some sort of
`01:07` then I throw that all into some sort of video editing software, which I
`01:09` video editing software, which I
`01:09` video editing software, which I personally use, Cap Cut, cuz it's super
`01:11` personally use, Cap Cut, cuz it's super
`01:11` personally use, Cap Cut, cuz it's super easy to use. I'm not going to walk
`01:12` easy to use. I'm not going to walk
`01:12` easy to use. I'm not going to walk [clears throat] you through the
`01:13` [clears throat] you through the
`01:13` [clears throat] you through the installation because there's plenty of
`01:15` installation because there's plenty of
`01:15` installation because there's plenty of tutorials uh, for that and it would eat
`01:17` tutorials uh, for that and it would eat
`01:17` tutorials uh, for that and it would eat up time better spent on the actual
`01:19` up time better spent on the actual
`01:19` up time better spent on the actual process of moving between these. Just
`01:22` process of moving between these. Just
`01:22` process of moving between these. Just know if you have these tools set up and
`01:23` know if you have these tools set up and
`01:24` know if you have these tools set up and running, everything I'm about to
`01:25` running, everything I'm about to
`01:25` running, everything I'm about to describe to you is available to you. And
`01:26` describe to you is available to you. And
`01:26` describe to you is available to you. And again, it's not tool specific. The tools
`01:29` again, it's not tool specific. The tools
`01:29` again, it's not tool specific. The tools actually don't matter themselves. It's
`01:30` actually don't matter themselves. It's
`01:30` actually don't matter themselves. It's the process and how you use them, how
`01:33` the process and how you use them, how
`01:33` the process and how you use them, how they work together. And honestly, that's
`01:36` they work together. And honestly, that's
`01:36` they work together. And honestly, that's what you'll see in all of my videos. I'm
`01:37` what you'll see in all of my videos. I'm
`01:37` what you'll see in all of my videos. I'm not just doing basic tutorials. I'm
`01:39` not just doing basic tutorials. I'm
`01:39` not just doing basic tutorials. I'm giving you a framework to how to use
`01:42` giving you a framework to how to use
`01:42` giving you a framework to how to use tools like these, these new abstractions
`01:44` tools like these, these new abstractions
`01:44` tools like these, these new abstractions of AI all together in a way that
`01:47` of AI all together in a way that
`01:47` of AI all together in a way that actually works. Now, here's the part
`01:48` actually works. Now, here's the part
`01:48` actually works. Now, here's the part that surprised me when I started doing
`01:50` that surprised me when I started doing
`01:50` that surprised me when I started doing this. The hard work isn't the AI. It's
`01:51` this. The hard work isn't the AI. It's
`01:51` this. The hard work isn't the AI. It's not the code, it's the spec, it's the
`01:53` not the code, it's the spec, it's the
`01:53` not the code, it's the spec, it's the breakdown. It's the documents that
`01:55` breakdown. It's the documents that
`01:55` breakdown. It's the documents that describe what the video should be. And
`01:57` describe what the video should be. And
`01:57` describe what the video should be. And not vaguely, not make it look cool, but
`01:59` not vaguely, not make it look cool, but
`01:59` not vaguely, not make it look cool, but precisely. What's the structure? What
`02:01` precisely. What's the structure? What
`02:01` precisely. What's the structure? What happens in each scene? What's the
`02:03` happens in each scene? What's the
`02:03` happens in each scene? What's the timing? What's the visual elements
`02:05` timing? What's the visual elements
`02:05` timing? What's the visual elements appear? When should they appear? What do
`02:06` appear? When should they appear? What do
`02:06` appear? When should they appear? What do you want to emphasize? And what should
`02:08` you want to emphasize? And what should
`02:08` you want to emphasize? And what should stay in the background? If you ever
`02:10` stay in the background? If you ever
`02:10` stay in the background? If you ever worked with a designer or an animator,
`02:12` worked with a designer or an animator,
`02:12` worked with a designer or an animator, you know this is as a brief. And there's
`02:15` you know this is as a brief. And there's
`02:15` you know this is as a brief. And there's this quote from uh David Ugle. He said,
`02:18` this quote from uh David Ugle. He said,
`02:18` this quote from uh David Ugle. He said, "Give me the freedom of a tight brief."
`02:21` "Give me the freedom of a tight brief."
`02:21` "Give me the freedom of a tight brief." Which sounds like a contradiction, but
`02:23` Which sounds like a contradiction, but
`02:23` Which sounds like a contradiction, but it isn't. When the brief is clear, when
`02:25` it isn't. When the brief is clear, when
`02:25` it isn't. When the brief is clear, when it defines the problem precisely, the
`02:27` it defines the problem precisely, the
`02:27` it defines the problem precisely, the person executing it knows exactly where
`02:30` person executing it knows exactly where
`02:30` person executing it knows exactly where they're going. They can focus on solving
`02:32` they're going. They can focus on solving
`02:32` they're going. They can focus on solving the problem instead of just sitting
`02:33` the problem instead of just sitting
`02:33` the problem instead of just sitting there trying to figure out what the
`02:34` there trying to figure out what the
`02:34` there trying to figure out what the problem even is. My spec or the spec
`02:37` problem even is. My spec or the spec
`02:37` problem even is. My spec or the spec that you're making, the markdown file is
`02:39` that you're making, the markdown file is
`02:39` that you're making, the markdown file is the brief. It's where your ideas become
`02:43` the brief. It's where your ideas become
`02:43` the brief. It's where your ideas become concrete enough for the system for the
`02:45` concrete enough for the system for the
`02:45` concrete enough for the system for the AI to actually execute them. And this is
`02:47` AI to actually execute them. And this is
`02:47` AI to actually execute them. And this is where most of your creative thinking
`02:48` where most of your creative thinking
`02:48` where most of your creative thinking should be happening. What's the thesis
`02:51` should be happening. What's the thesis
`02:51` should be happening. What's the thesis of this video? What's the arc? What are
`02:52` of this video? What's the arc? What are
`02:52` of this video? What's the arc? What are the scripts? What are the moments that
`02:53` the scripts? What are the moments that
`02:53` the scripts? What are the moments that need to land? What should feel fast and
`02:55` need to land? What should feel fast and
`02:55` need to land? What should feel fast and what should feel slow? A loose spec or a
`02:58` what should feel slow? A loose spec or a
`02:58` what should feel slow? A loose spec or a poor spec means that Claude or your AI
`03:00` poor spec means that Claude or your AI
`03:00` poor spec means that Claude or your AI agent makes more interpretive choices or
`03:02` agent makes more interpretive choices or
`03:02` agent makes more interpretive choices or hallucinates more. A tight spec means
`03:04` hallucinates more. A tight spec means
`03:04` hallucinates more. A tight spec means you're directing it at every beat. And
`03:06` you're directing it at every beat. And
`03:06` you're directing it at every beat. And really, it allows you to do a lot more
`03:08` really, it allows you to do a lot more
`03:08` really, it allows you to do a lot more focused things. You can do both, and it
`03:10` focused things. You can do both, and it
`03:10` focused things. You can do both, and it depends on where you want your creative
`03:12` depends on where you want your creative
`03:12` depends on where you want your creative energy to go. But I'll show you what one
`03:14` energy to go. But I'll show you what one
`03:14` energy to go. But I'll show you what one of my specs look like. And again, as I
`03:17` of my specs look like. And again, as I
`03:17` of my specs look like. And again, as I said, it's actually just a markdown
`03:19` said, it's actually just a markdown
`03:19` said, it's actually just a markdown file, which is a type of file that
`03:21` file, which is a type of file that
`03:21` file, which is a type of file that organizes text in a very specific way.
`03:23` organizes text in a very specific way.
`03:24` organizes text in a very specific way. It has headings for each scene,
`03:25` It has headings for each scene,
`03:25` It has headings for each scene, descriptions of what happens, notes on
`03:27` descriptions of what happens, notes on
`03:27` descriptions of what happens, notes on timing and emphasis. It's really nothing
`03:30` timing and emphasis. It's really nothing
`03:30` timing and emphasis. It's really nothing too fancy, but it's the document that
`03:32` too fancy, but it's the document that
`03:32` too fancy, but it's the document that makes everything else possible. And this
`03:35` makes everything else possible. And this
`03:35` makes everything else possible. And this isn't just for creative processes. This
`03:37` isn't just for creative processes. This
`03:38` isn't just for creative processes. This is for code. This is for anything you're
`03:40` is for code. This is for anything you're
`03:40` is for code. This is for anything you're doing with AI agents. And you'll start
`03:42` doing with AI agents. And you'll start
`03:42` doing with AI agents. And you'll start to notice how powerful this process is.
`03:45` to notice how powerful this process is.
`03:45` to notice how powerful this process is. Once you have a spec, the building phase
`03:47` Once you have a spec, the building phase
`03:47` Once you have a spec, the building phase is where it becomes animation. And
`03:49` is where it becomes animation. And
`03:49` is where it becomes animation. And here's what actually is happening.
`03:51` here's what actually is happening.
`03:51` here's what actually is happening. Claude code or your agent is going to
`03:53` Claude code or your agent is going to
`03:53` Claude code or your agent is going to read through the spec, but it also reads
`03:56` read through the spec, but it also reads
`03:56` read through the spec, but it also reads your documentation if the spec is
`03:58` your documentation if the spec is
`03:58` your documentation if the spec is mentioning, which mentions maybe style
`04:00` mentioning, which mentions maybe style
`04:00` mentioning, which mentions maybe style guides. This is going to define your
`04:01` guides. This is going to define your
`04:01` guides. This is going to define your visual language. You're going to define
`04:03` visual language. You're going to define
`04:03` visual language. You're going to define minimal texts. You're going to define
`04:05` minimal texts. You're going to define
`04:05` minimal texts. You're going to define color pallets, animation timing. It's
`04:08` color pallets, animation timing. It's
`04:08` color pallets, animation timing. It's going to read through a component
`04:09` going to read through a component
`04:09` going to read through a component registry. Now, I created this, but it's
`04:11` registry. Now, I created this, but it's
`04:11` registry. Now, I created this, but it's basically just a list of reusable pieces
`04:13` basically just a list of reusable pieces
`04:13` basically just a list of reusable pieces that you've already built in previous
`04:15` that you've already built in previous
`04:15` that you've already built in previous videos or you're building with the AI
`04:17` videos or you're building with the AI
`04:17` videos or you're building with the AI before it even starts, right? Text
`04:19` before it even starts, right? Text
`04:19` before it even starts, right? Text animations, backgrounds, transitions,
`04:21` animations, backgrounds, transitions,
`04:21` animations, backgrounds, transitions, data visualizations. Then from there,
`04:23` data visualizations. Then from there,
`04:24` data visualizations. Then from there, you're actually having it build each
`04:25` you're actually having it build each
`04:25` you're actually having it build each scene one by one. And each scene is just
`04:28` scene one by one. And each scene is just
`04:28` scene one by one. And each scene is just a React component, right? This a
`04:30` a React component, right? This a
`04:30` a React component, right? This a front-end uh software. And Remotion
`04:33` front-end uh software. And Remotion
`04:33` front-end uh software. And Remotion takes those React components and
`04:34` takes those React components and
`04:34` takes those React components and actually allows you to render them frame
`04:36` actually allows you to render them frame
`04:36` actually allows you to render them frame by frame into a long video. And there's
`04:39` by frame into a long video. And there's
`04:39` by frame into a long video. And there's an insight from a man named Johnny
`04:41` an insight from a man named Johnny
`04:41` an insight from a man named Johnny Burgerer who actually created reotion. A
`04:43` Burgerer who actually created reotion. A
`04:43` Burgerer who actually created reotion. A video is just a function of images over
`04:46` video is just a function of images over
`04:46` video is just a function of images over time. If you change content every frame,
`04:49` time. If you change content every frame,
`04:49` time. If you change content every frame, you get animation. And React is already
`04:51` you get animation. And React is already
`04:52` you get animation. And React is already good at describing what should appear
`04:53` good at describing what should appear
`04:53` good at describing what should appear based on some state. So instead of the
`04:56` based on some state. So instead of the
`04:56` based on some state. So instead of the state being user input, the state is the
`04:58` state being user input, the state is the
`04:58` state being user input, the state is the current frame number. You tell React
`05:01` current frame number. You tell React
`05:01` current frame number. You tell React what frame 47 should look like and it
`05:03` what frame 47 should look like and it
`05:03` what frame 47 should look like and it renders it. Do that for every frame, you
`05:06` renders it. Do that for every frame, you
`05:06` renders it. Do that for every frame, you now have a video. What this means in
`05:08` now have a video. What this means in
`05:08` now have a video. What this means in practice is that anything that works in
`05:10` practice is that anything that works in
`05:10` practice is that anything that works in a web browser can be part of your
`05:12` a web browser can be part of your
`05:12` a web browser can be part of your animation. CSS, SVG, canvas, the entire
`05:15` animation. CSS, SVG, canvas, the entire
`05:15` animation. CSS, SVG, canvas, the entire ecosystem of JavaScript libraries can
`05:18` ecosystem of JavaScript libraries can
`05:18` ecosystem of JavaScript libraries can now be placed into your videos. You see,
`05:20` now be placed into your videos. You see,
`05:20` now be placed into your videos. You see, you're not learning a new tool from
`05:22` you're not learning a new tool from
`05:22` you're not learning a new tool from scratch. If you're a front-end
`05:23` scratch. If you're a front-end
`05:23` scratch. If you're a front-end developer, you're using tools that have
`05:25` developer, you're using tools that have
`05:25` developer, you're using tools that have already existed for a new purpose. So,
`05:29` already existed for a new purpose. So,
`05:29` already existed for a new purpose. So, the workflow actually looks more
`05:31` the workflow actually looks more
`05:31` the workflow actually looks more detailed like this. I give Claude the
`05:34` detailed like this. I give Claude the
`05:34` detailed like this. I give Claude the spec, point it at the documentation, I
`05:37` spec, point it at the documentation, I
`05:37` spec, point it at the documentation, I tell it which scene to build, it writes
`05:39` tell it which scene to build, it writes
`05:39` tell it which scene to build, it writes the code, I preview it in Remotion
`05:42` the code, I preview it in Remotion
`05:42` the code, I preview it in Remotion Studio, and if something isn't right, I
`05:44` Studio, and if something isn't right, I
`05:44` Studio, and if something isn't right, I literally just describe in natural
`05:45` literally just describe in natural
`05:45` literally just describe in natural language what needs to change, and it
`05:48` language what needs to change, and it
`05:48` language what needs to change, and it adjusts. We iterate until the scene
`05:51` adjusts. We iterate until the scene
`05:51` adjusts. We iterate until the scene matches what I had in mind. The
`05:53` matches what I had in mind. The
`05:53` matches what I had in mind. The component library matters at this point
`05:55` component library matters at this point
`05:55` component library matters at this point because I'm not building every single
`05:57` because I'm not building every single
`05:57` because I'm not building every single animation from scratch. It's not like
`05:59` animation from scratch. It's not like
`05:59` animation from scratch. It's not like every time I'm making a video, I'm just
`06:01` every time I'm making a video, I'm just
`06:01` every time I'm making a video, I'm just starting from fresh. I actually have
`06:02` starting from fresh. I actually have
`06:02` starting from fresh. I actually have building blocks that are traditional
`06:04` building blocks that are traditional
`06:04` building blocks that are traditional code, a text component that handles
`06:06` code, a text component that handles
`06:06` code, a text component that handles entrance animations or enforces readable
`06:08` entrance animations or enforces readable
`06:08` entrance animations or enforces readable sizes, a scene container that handles
`06:10` sizes, a scene container that handles
`06:10` sizes, a scene container that handles safe margins and backgrounds. Effects
`06:13` safe margins and backgrounds. Effects
`06:13` safe margins and backgrounds. Effects like glitch text or counting numbers.
`06:15` like glitch text or counting numbers.
`06:15` like glitch text or counting numbers. When Claude builds a scene, it assembles
`06:17` When Claude builds a scene, it assembles
`06:17` When Claude builds a scene, it assembles these pieces according to the spec. It's
`06:19` these pieces according to the spec. It's
`06:19` these pieces according to the spec. It's not inventing everything new, but rather
`06:21` not inventing everything new, but rather
`06:22` not inventing everything new, but rather this kind of aspect of like, hey, I
`06:24` this kind of aspect of like, hey, I
`06:24` this kind of aspect of like, hey, I should compose a new element that
`06:26` should compose a new element that
`06:26` should compose a new element that already works together in other
`06:27` already works together in other
`06:27` already works together in other elements. This is just separations of
`06:30` elements. This is just separations of
`06:30` elements. This is just separations of concerns. It's the same principle that
`06:32` concerns. It's the same principle that
`06:32` concerns. It's the same principle that makes any complex software manageable.
`06:34` makes any complex software manageable.
`06:34` makes any complex software manageable. The spec is separate from the
`06:36` The spec is separate from the
`06:36` The spec is separate from the implementation. The components are
`06:38` implementation. The components are
`06:38` implementation. The components are reusable. The style guide encodes
`06:41` reusable. The style guide encodes
`06:41` reusable. The style guide encodes decisions so you don't have to make them
`06:42` decisions so you don't have to make them
`06:42` decisions so you don't have to make them every time. Now, if anyone has written
`06:45` every time. Now, if anyone has written
`06:45` every time. Now, if anyone has written software before, this should actually
`06:47` software before, this should actually
`06:47` software before, this should actually seem very familiar. And even if you
`06:49` seem very familiar. And even if you
`06:49` seem very familiar. And even if you haven't, just know that this is the
`06:50` haven't, just know that this is the
`06:50` haven't, just know that this is the principle. Break complex things into
`06:53` principle. Break complex things into
`06:53` principle. Break complex things into smaller pieces that can be understood
`06:55` smaller pieces that can be understood
`06:55` smaller pieces that can be understood and changed independently. From there,
`06:58` and changed independently. From there,
`06:58` and changed independently. From there, once the scenes are relatively built, I
`07:01` once the scenes are relatively built, I
`07:01` once the scenes are relatively built, I just export it from Remotion or even
`07:03` just export it from Remotion or even
`07:03` just export it from Remotion or even just use OBS to record my screen, so I
`07:05` just use OBS to record my screen, so I
`07:05` just use OBS to record my screen, so I don't have to worry about render
`07:06` don't have to worry about render
`07:06` don't have to worry about render processes or codec errors. And this just
`07:09` processes or codec errors. And this just
`07:09` processes or codec errors. And this just is something I can upload straight into
`07:11` is something I can upload straight into
`07:11` is something I can upload straight into Cap Cut. Now, this is where the
`07:13` Cap Cut. Now, this is where the
`07:13` Cap Cut. Now, this is where the animation becomes much more of a video.
`07:15` animation becomes much more of a video.
`07:15` animation becomes much more of a video. I usually do a voice over. I cut and
`07:18` I usually do a voice over. I cut and
`07:18` I usually do a voice over. I cut and make sure that it actually syncs up. I
`07:20` make sure that it actually syncs up. I
`07:20` make sure that it actually syncs up. I maybe add some music. And there's some
`07:23` maybe add some music. And there's some
`07:23` maybe add some music. And there's some things that right now are a little bit
`07:25` things that right now are a little bit
`07:25` things that right now are a little bit easier to do by hand. So, I haven't
`07:26` easier to do by hand. So, I haven't
`07:26` easier to do by hand. So, I haven't really automated that process, but I'm
`07:28` really automated that process, but I'm
`07:28` really automated that process, but I'm working on it. Now, scrubbing through
`07:30` working on it. Now, scrubbing through
`07:30` working on it. Now, scrubbing through and nudging a transition to land exactly
`07:32` and nudging a transition to land exactly
`07:32` and nudging a transition to land exactly on a word is honestly faster in a video
`07:34` on a word is honestly faster in a video
`07:34` on a word is honestly faster in a video editor than describing it in the spec
`07:36` editor than describing it in the spec
`07:36` editor than describing it in the spec and waiting for code to regenerate. The
`07:38` and waiting for code to regenerate. The
`07:38` and waiting for code to regenerate. The animation is not the finished video.
`07:40` animation is not the finished video.
`07:40` animation is not the finished video. It's simply a starting point. Now, it is
`07:42` It's simply a starting point. Now, it is
`07:42` It's simply a starting point. Now, it is a substantial one. I still spend real
`07:44` a substantial one. I still spend real
`07:44` a substantial one. I still spend real time in this phase. I'm cutting so many
`07:46` time in this phase. I'm cutting so many
`07:46` time in this phase. I'm cutting so many sections that don't work when I hear
`07:47` sections that don't work when I hear
`07:47` sections that don't work when I hear them out loud. I'm re-recording lines
`07:49` them out loud. I'm re-recording lines
`07:49` them out loud. I'm re-recording lines that don't land. I'm adding photos or
`07:51` that don't land. I'm adding photos or
`07:51` that don't land. I'm adding photos or screenshots or footage to support the
`07:53` screenshots or footage to support the
`07:53` screenshots or footage to support the narration. The animations give me a
`07:55` narration. The animations give me a
`07:55` narration. The animations give me a foundation, but the finished video
`07:57` foundation, but the finished video
`07:57` foundation, but the finished video requires refinement. So when I say under
`07:59` requires refinement. So when I say under
`07:59` requires refinement. So when I say under an hour, I mean the animation, the part
`08:01` an hour, I mean the animation, the part
`08:01` an hour, I mean the animation, the part that would have taken a week if I was
`08:03` that would have taken a week if I was
`08:03` that would have taken a week if I was doing it frame by frame and After
`08:05` doing it frame by frame and After
`08:05` doing it frame by frame and After Effects. The finished video still takes
`08:07` Effects. The finished video still takes
`08:08` Effects. The finished video still takes time, but I'm spending that time on the
`08:09` time, but I'm spending that time on the
`08:09` time, but I'm spending that time on the parts I actually want to control. The
`08:11` parts I actually want to control. The
`08:11` parts I actually want to control. The pacing, the moments that need a real
`08:13` pacing, the moments that need a real
`08:13` pacing, the moments that need a real image instead of motion graphics. Now,
`08:15` image instead of motion graphics. Now,
`08:15` image instead of motion graphics. Now, the question isn't really about whether
`08:17` the question isn't really about whether
`08:17` the question isn't really about whether AI can make videos or anything like
`08:19` AI can make videos or anything like
`08:19` AI can make videos or anything like that. It's more where do you want to
`08:21` that. It's more where do you want to
`08:21` that. It's more where do you want to spend your creative energy? And for me,
`08:24` spend your creative energy? And for me,
`08:24` spend your creative energy? And for me, the answer is not automating from
`08:26` the answer is not automating from
`08:26` the answer is not automating from scratch, not animating everything.
`08:28` scratch, not animating everything.
`08:28` scratch, not animating everything. Honestly, I'd rather have something real
`08:30` Honestly, I'd rather have something real
`08:30` Honestly, I'd rather have something real to react and to shape to rather than
`08:33` to react and to shape to rather than
`08:33` to react and to shape to rather than start with a blank timeline or focus on
`08:35` start with a blank timeline or focus on
`08:35` start with a blank timeline or focus on the actual content itself. Now, that
`08:38` the actual content itself. Now, that
`08:38` the actual content itself. Now, that being said, let's zoom out for a second
`08:39` being said, let's zoom out for a second
`08:39` being said, let's zoom out for a second because I think what's happening here,
`08:41` because I think what's happening here,
`08:41` because I think what's happening here, as I mentioned earlier in the video, is
`08:43` as I mentioned earlier in the video, is
`08:43` as I mentioned earlier in the video, is part of a much larger pattern. When
`08:47` part of a much larger pattern. When
`08:47` part of a much larger pattern. When Garage Band came out in 2004, Steve says
`08:50` Garage Band came out in 2004, Steve says
`08:50` Garage Band came out in 2004, Steve says he wanted to democratize music making.
`08:52` he wanted to democratize music making.
`08:52` he wanted to democratize music making. And there's this statistic that stuck
`08:54` And there's this statistic that stuck
`08:54` And there's this statistic that stuck with me. Suddenly, every teenager with a
`08:56` with me. Suddenly, every teenager with a
`08:56` with me. Suddenly, every teenager with a Mac could produce music that would have
`08:58` Mac could produce music that would have
`08:58` Mac could produce music that would have required a $100,000 studio. 5 years
`09:00` required a $100,000 studio. 5 years
`09:00` required a $100,000 studio. 5 years earlier, Steve Lacy made tracks for
`09:02` earlier, Steve Lacy made tracks for
`09:02` earlier, Steve Lacy made tracks for Kendrick Lamar on a cracked iPhone with
`09:04` Kendrick Lamar on a cracked iPhone with
`09:04` Kendrick Lamar on a cracked iPhone with GarageBand and a $20 eye ring. That
`09:07` GarageBand and a $20 eye ring. That
`09:07` GarageBand and a $20 eye ring. That phone is now in the Smithsonian. Canva
`09:10` phone is now in the Smithsonian. Canva
`09:10` phone is now in the Smithsonian. Canva did something similar for visual design.
`09:12` did something similar for visual design.
`09:12` did something similar for visual design. Melanie Perkins was rejected by over a
`09:14` Melanie Perkins was rejected by over a
`09:14` Melanie Perkins was rejected by over a hundred investors who didn't think
`09:15` hundred investors who didn't think
`09:15` hundred investors who didn't think design tools for non-designers was a
`09:17` design tools for non-designers was a
`09:17` design tools for non-designers was a real market. Now 200 million people use
`09:19` real market. Now 200 million people use
`09:19` real market. Now 200 million people use it monthly. The pattern is always the
`09:21` it monthly. The pattern is always the
`09:21` it monthly. The pattern is always the same. A tool emerges that gives people
`09:23` same. A tool emerges that gives people
`09:23` same. A tool emerges that gives people access to execution they couldn't do
`09:25` access to execution they couldn't do
`09:25` access to execution they couldn't do before. Not replacing professionals, but
`09:27` before. Not replacing professionals, but
`09:28` before. Not replacing professionals, but letting people who have ideas actually
`09:29` letting people who have ideas actually
`09:30` letting people who have ideas actually realize them. And there's a really messy
`09:32` realize them. And there's a really messy
`09:32` realize them. And there's a really messy period early on which designers called
`09:34` period early on which designers called
`09:34` period early on which designers called the ransom note effect. When desktop
`09:36` the ransom note effect. When desktop
`09:36` the ransom note effect. When desktop publishing first appeared, everyone used
`09:39` publishing first appeared, everyone used
`09:39` publishing first appeared, everyone used 15 different fonts on one page, but it
`09:41` 15 different fonts on one page, but it
`09:42` 15 different fonts on one page, but it kind of went all over. And then over
`09:43` kind of went all over. And then over
`09:43` kind of went all over. And then over time, the floor kind of rose. More
`09:45` time, the floor kind of rose. More
`09:45` time, the floor kind of rose. More people creating means more good work in
`09:47` people creating means more good work in
`09:47` people creating means more good work in absolute terms. Even if the average
`09:50` absolute terms. Even if the average
`09:50` absolute terms. Even if the average quality takes time to catch up. I think
`09:53` quality takes time to catch up. I think
`09:53` quality takes time to catch up. I think we're in that motion or that moment for
`09:55` we're in that motion or that moment for
`09:55` we're in that motion or that moment for AI and animation and video. The tools
`09:57` AI and animation and video. The tools
`09:57` AI and animation and video. The tools exist. The quality can be good. And
`10:00` exist. The quality can be good. And
`10:00` exist. The quality can be good. And people who couldn't afford a motion
`10:01` people who couldn't afford a motion
`10:01` people who couldn't afford a motion graphics artist or couldn't justify a
`10:03` graphics artist or couldn't justify a
`10:03` graphics artist or couldn't justify a week of their own time can now make
`10:05` week of their own time can now make
`10:05` week of their own time can now make something real. And this might be kind
`10:07` something real. And this might be kind
`10:07` something real. And this might be kind of powerive, but I think this is the key
`10:10` of powerive, but I think this is the key
`10:10` of powerive, but I think this is the key to how all of this is going to work.
`10:12` to how all of this is going to work.
`10:12` to how all of this is going to work. It's that constraints enable creativity.
`10:15` It's that constraints enable creativity.
`10:15` It's that constraints enable creativity. There's actual research on this. An
`10:17` There's actual research on this. An
`10:17` There's actual research on this. An inverted U-shaped relationship between
`10:19` inverted U-shaped relationship between
`10:19` inverted U-shaped relationship between constraints and creative output. Too few
`10:22` constraints and creative output. Too few
`10:22` constraints and creative output. Too few constraints, you get paralysis, the
`10:24` constraints, you get paralysis, the
`10:24` constraints, you get paralysis, the blank canvas problem. Too many, you
`10:27` blank canvas problem. Too many, you
`10:27` blank canvas problem. Too many, you actually get stifled. But right in the
`10:28` actually get stifled. But right in the
`10:28` actually get stifled. But right in the middle, with the right boundaries,
`10:30` middle, with the right boundaries,
`10:30` middle, with the right boundaries, creativity actually increases. Dr. Zeus
`10:33` creativity actually increases. Dr. Zeus
`10:34` creativity actually increases. Dr. Zeus wrote Green Eggs and Ham because his
`10:36` wrote Green Eggs and Ham because his
`10:36` wrote Green Eggs and Ham because his editor bet him $50 he couldn't write a
`10:38` editor bet him $50 he couldn't write a
`10:38` editor bet him $50 he couldn't write a book with only 50 words. He made
`10:41` book with only 50 words. He made
`10:41` book with only 50 words. He made flowcharts on his walls to track his
`10:43` flowcharts on his walls to track his
`10:43` flowcharts on his walls to track his vocabulary. And the book sold 200
`10:46` vocabulary. And the book sold 200
`10:46` vocabulary. And the book sold 200 million copies, and it is his best
`10:49` million copies, and it is his best
`10:49` million copies, and it is his best selling work ever. Spielberg couldn't
`10:52` selling work ever. Spielberg couldn't
`10:52` selling work ever. Spielberg couldn't get the mechanical shark to work in
`10:54` get the mechanical shark to work in
`10:54` get the mechanical shark to work in Jaws, so he showed floating barrels and
`10:56` Jaws, so he showed floating barrels and
`10:56` Jaws, so he showed floating barrels and point off view shots instead. The shark
`10:59` point off view shots instead. The shark
`10:59` point off view shots instead. The shark doesn't fully appear until 80 minutes
`11:01` doesn't fully appear until 80 minutes
`11:01` doesn't fully appear until 80 minutes into the film. The constraint made it
`11:03` into the film. The constraint made it
`11:03` into the film. The constraint made it better somehow. The spec, the style
`11:06` better somehow. The spec, the style
`11:06` better somehow. The spec, the style guide, the component registry, these
`11:08` guide, the component registry, these
`11:08` guide, the component registry, these aren't limitations I work around.
`11:10` aren't limitations I work around.
`11:10` aren't limitations I work around. They're boundaries that make the output
`11:12` They're boundaries that make the output
`11:12` They're boundaries that make the output better. Instead, this case, Claude is
`11:14` better. Instead, this case, Claude is
`11:14` better. Instead, this case, Claude is now the one constrained. It knows the
`11:16` now the one constrained. It knows the
`11:16` now the one constrained. It knows the rules. It focuses on execution instead
`11:18` rules. It focuses on execution instead
`11:18` rules. It focuses on execution instead of wondering what I want. So let me come
`11:20` of wondering what I want. So let me come
`11:20` of wondering what I want. So let me come back to where we started. The animations
`11:22` back to where we started. The animations
`11:22` back to where we started. The animations that would have taken a week are now
`11:23` that would have taken a week are now
`11:23` that would have taken a week are now done in an hour. That part is true and I
`11:26` done in an hour. That part is true and I
`11:26` done in an hour. That part is true and I want you to understand what actually is
`11:28` want you to understand what actually is
`11:28` want you to understand what actually is behind that claim. AI is not magic. I
`11:31` behind that claim. AI is not magic. I
`11:31` behind that claim. AI is not magic. I built a system. The spec is where my
`11:33` built a system. The spec is where my
`11:33` built a system. The spec is where my creative thinking lives and the
`11:35` creative thinking lives and the
`11:35` creative thinking lives and the predefining constraints. The
`11:37` predefining constraints. The
`11:37` predefining constraints. The documentation encodes my preferences and
`11:39` documentation encodes my preferences and
`11:39` documentation encodes my preferences and my lessons from past mistakes. Claude
`11:42` my lessons from past mistakes. Claude
`11:42` my lessons from past mistakes. Claude executes within those boundaries,
`11:44` executes within those boundaries,
`11:44` executes within those boundaries, assembling components that already work
`11:46` assembling components that already work
`11:46` assembling components that already work together into scenes that match what I
`11:48` together into scenes that match what I
`11:48` together into scenes that match what I describe. Then I take that output and I
`11:51` describe. Then I take that output and I
`11:51` describe. Then I take that output and I refine it. I cut it. I add footage. I
`11:53` refine it. I cut it. I add footage. I
`11:53` refine it. I cut it. I add footage. I shape it into something finished. The
`11:55` shape it into something finished. The
`11:55` shape it into something finished. The creative work didn't disappear in the
`11:57` creative work didn't disappear in the
`11:58` creative work didn't disappear in the same way we would imagine it actually
`12:00` same way we would imagine it actually
`12:00` same way we would imagine it actually moving. The spec, the refinement, that
`12:03` moving. The spec, the refinement, that
`12:03` moving. The spec, the refinement, that whole area is actually where I want to
`12:05` whole area is actually where I want to
`12:05` whole area is actually where I want to spend my attention. Now, if you have
`12:07` spend my attention. Now, if you have
`12:07` spend my attention. Now, if you have ideas and want to visualize, but you're
`12:09` ideas and want to visualize, but you're
`12:09` ideas and want to visualize, but you're not an animator, this is probably
`12:11` not an animator, this is probably
`12:11` not an animator, this is probably something you want to focus on. Not
`12:13` something you want to focus on. Not
`12:13` something you want to focus on. Not easy. There's setup and learning and
`12:16` easy. There's setup and learning and
`12:16` easy. There's setup and learning and narration, but it's possible in a way
`12:17` narration, but it's possible in a way
`12:18` narration, but it's possible in a way that was never possible before. You can
`12:21` that was never possible before. You can
`12:21` that was never possible before. You can finally get ideas into a visual form
`12:24` finally get ideas into a visual form
`12:24` finally get ideas into a visual form that used to require skills most people
`12:26` that used to require skills most people
`12:26` that used to require skills most people don't have. Years of After Effects or
`12:29` don't have. Years of After Effects or
`12:29` don't have. Years of After Effects or money to hire someone who did. Now it
`12:32` money to hire someone who did. Now it
`12:32` money to hire someone who did. Now it requires a process, right? Tools that
`12:34` requires a process, right? Tools that
`12:34` requires a process, right? Tools that are freely available, a way of thinking
`12:36` are freely available, a way of thinking
`12:36` are freely available, a way of thinking about constraints and separations of
`12:39` about constraints and separations of
`12:39` about constraints and separations of concerns. And honestly, most of those
`12:41` concerns. And honestly, most of those
`12:41` concerns. And honestly, most of those constraints are just software
`12:42` constraints are just software
`12:42` constraints are just software engineering but applied to creative
`12:44` engineering but applied to creative
`12:44` engineering but applied to creative work. This process can be learned and I
`12:47` work. This process can be learned and I
`12:47` work. This process can be learned and I really recommend each of you try it.
`12:49` really recommend each of you try it.
`12:49` really recommend each of you try it. Everything I've described, I have
`12:50` Everything I've described, I have
`12:50` Everything I've described, I have documented. The tools are [music] there.
`12:52` documented. The tools are [music] there.
`12:52` documented. The tools are [music] there. If you want any of these specs or these
`12:53` If you want any of these specs or these
`12:53` If you want any of these specs or these scripts or these designs, just comment
`12:55` scripts or these designs, just comment
`12:55` scripts or these designs, just comment and and ask for them. I'll happy to
`12:57` and and ask for them. I'll happy to
`12:57` and and ask for them. I'll happy to email them to you. But if you have ideas
`12:59` email them to you. But if you have ideas
`12:59` email them to you. But if you have ideas that have been stuck in your head
`13:00` that have been stuck in your head
`13:00` that have been stuck in your head because you couldn't figure out how to
`13:02` because you couldn't figure out how to
`13:02` because you couldn't figure out how to make them visible,
`13:04` make them visible,
`13:04` make them visible, maybe now you can. Other than that, I
`13:06` maybe now you can. Other than that, I
`13:06` maybe now you can. Other than that, I hope this helps out everyone. As always,
`13:09` hope this helps out everyone. As always,
`13:09` hope this helps out everyone. As always, stay curious.