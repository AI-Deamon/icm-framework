# From Nazi Psychology to AI Auditing: Inside the System I Built

**Channel:** Jake Van Clief  
**Uploaded:** 2026-02-04  
**Duration:** 13:41  
**URL:** [https://www.youtube.com/watch?v=UGyTimVObus](https://www.youtube.com/watch?v=UGyTimVObus)  

---

## Transcript

`00:02` I took psychometric tests used to
`00:02` I took psychometric tests used to capture Nazis in the 50s and aimed them
`00:05` capture Nazis in the 50s and aimed them
`00:05` capture Nazis in the 50s and aimed them at AI models. Well, I did a little bit
`00:07` at AI models. Well, I did a little bit
`00:07` at AI models. Well, I did a little bit more than that. I created a data
`00:08` more than that. I created a data
`00:08` more than that. I created a data pipeline that allowed to take a lot of
`00:10` pipeline that allowed to take a lot of
`00:10` pipeline that allowed to take a lot of personality tests and aim them all
`00:12` personality tests and aim them all
`00:12` personality tests and aim them all across AI models. It can tell you where
`00:14` across AI models. It can tell you where
`00:14` across AI models. It can tell you where a model lands on moral foundations,
`00:17` a model lands on moral foundations,
`00:17` a model lands on moral foundations, authoritarianism scales, personality
`00:19` authoritarianism scales, personality
`00:19` authoritarianism scales, personality dimensions, and it can do this across
`00:21` dimensions, and it can do this across
`00:21` dimensions, and it can do this across personas, model variations, various
`00:23` personas, model variations, various
`00:23` personas, model variations, various providers, and so on. And from the
`00:25` providers, and so on. And from the
`00:25` providers, and so on. And from the outside, it looks like one intelligence
`00:27` outside, it looks like one intelligence
`00:27` outside, it looks like one intelligence studying another, like something that
`00:28` studying another, like something that
`00:28` studying another, like something that would require a team of researchers or
`00:30` would require a team of researchers or
`00:30` would require a team of researchers or grants. But the point I'm bringing this
`00:31` grants. But the point I'm bringing this
`00:32` grants. But the point I'm bringing this up is not to even show you that. I
`00:33` up is not to even show you that. I
`00:33` up is not to even show you that. I actually want to take this apart because
`00:35` actually want to take this apart because
`00:35` actually want to take this apart because it's going to help me explain APIs,
`00:38` it's going to help me explain APIs,
`00:38` it's going to help me explain APIs, research, coding in the modern era, what
`00:40` research, coding in the modern era, what
`00:40` research, coding in the modern era, what it means to do the fundamentals. And I
`00:42` it means to do the fundamentals. And I
`00:42` it means to do the fundamentals. And I don't want to show you how to build
`00:43` don't want to show you how to build
`00:44` don't want to show you how to build this. Rather, I'd deconstruct it because
`00:46` this. Rather, I'd deconstruct it because
`00:46` this. Rather, I'd deconstruct it because something becomes visible when you
`00:47` something becomes visible when you
`00:47` something becomes visible when you deconstruct systems rather than showing
`00:49` deconstruct systems rather than showing
`00:49` deconstruct systems rather than showing you how to assemble systems. And let me
`00:51` you how to assemble systems. And let me
`00:52` you how to assemble systems. And let me show you exactly what I mean. But before
`00:54` show you exactly what I mean. But before
`00:54` show you exactly what I mean. But before I do that, let's go into a kind of world
`00:57` I do that, let's go into a kind of world
`00:57` I do that, let's go into a kind of world of definitions. There's a word that has
`00:59` of definitions. There's a word that has
`01:00` of definitions. There's a word that has taken on a lot of weight in the last
`01:01` taken on a lot of weight in the last
`01:01` taken on a lot of weight in the last couple of years, and that word is agent.
`01:04` couple of years, and that word is agent.
`01:04` couple of years, and that word is agent. We hear about AI agents that can browse
`01:06` We hear about AI agents that can browse
`01:06` We hear about AI agents that can browse the web, write code, manage calendars,
`01:08` the web, write code, manage calendars,
`01:08` the web, write code, manage calendars, analyze documents, da da da da, all this
`01:10` analyze documents, da da da da, all this
`01:10` analyze documents, da da da da, all this hype, agentic world. And the word agent
`01:13` hype, agentic world. And the word agent
`01:13` hype, agentic world. And the word agent does mean something to our imagination.
`01:16` does mean something to our imagination.
`01:16` does mean something to our imagination. And not just from an AI perspective. It
`01:18` And not just from an AI perspective. It
`01:18` And not just from an AI perspective. It used to mean autonomy or separate or
`01:20` used to mean autonomy or separate or
`01:20` used to mean autonomy or separate or attached, right? this idea that there's
`01:23` attached, right? this idea that there's
`01:23` attached, right? this idea that there's decision-making going on. It implies
`01:24` decision-making going on. It implies
`01:24` decision-making going on. It implies that this thing can act on its own
`01:27` that this thing can act on its own
`01:27` that this thing can act on its own behalf. Uh, and I want to be careful
`01:30` behalf. Uh, and I want to be careful
`01:30` behalf. Uh, and I want to be careful here because I think this is one of
`01:32` here because I think this is one of
`01:32` here because I think this is one of those places where language is running
`01:34` those places where language is running
`01:34` those places where language is running ahead of the engineering. What we call
`01:37` ahead of the engineering. What we call
`01:37` ahead of the engineering. What we call an AI agent in the vast majority of
`01:40` an AI agent in the vast majority of
`01:40` an AI agent in the vast majority of cases is not a single entity making
`01:42` cases is not a single entity making
`01:42` cases is not a single entity making autonomous decisions. It is a collection
`01:44` autonomous decisions. It is a collection
`01:44` autonomous decisions. It is a collection of prompts structured and sequenced by
`01:47` of prompts structured and sequenced by
`01:47` of prompts structured and sequenced by traditional code that causes a model to
`01:50` traditional code that causes a model to
`01:50` traditional code that causes a model to behave differently at different stages
`01:52` behave differently at different stages
`01:52` behave differently at different stages of a workflow. The model itself is not
`01:54` of a workflow. The model itself is not
`01:54` of a workflow. The model itself is not deciding to take a next step. The
`01:56` deciding to take a next step. The
`01:56` deciding to take a next step. The orchestration layer, which is regular
`01:58` orchestration layer, which is regular
`01:58` orchestration layer, which is regular software, evaluates the model's output
`02:01` software, evaluates the model's output
`02:01` software, evaluates the model's output and determines what prompt to send next
`02:03` and determines what prompt to send next
`02:03` and determines what prompt to send next based on conditions that a human
`02:05` based on conditions that a human
`02:05` based on conditions that a human engineer defined. This is an important
`02:08` engineer defined. This is an important
`02:08` engineer defined. This is an important distinction and it maps onto something
`02:10` distinction and it maps onto something
`02:10` distinction and it maps onto something we already understand in computer
`02:11` we already understand in computer
`02:11` we already understand in computer science. Think about the difference
`02:13` science. Think about the difference
`02:13` science. Think about the difference between a function call and a running
`02:15` between a function call and a running
`02:15` between a function call and a running process. A function takes an input and
`02:17` process. A function takes an input and
`02:17` process. A function takes an input and returns an output. It doesn't decide
`02:20` returns an output. It doesn't decide
`02:20` returns an output. It doesn't decide what to do next. The program that called
`02:22` what to do next. The program that called
`02:22` what to do next. The program that called the function makes that decision. In the
`02:25` the function makes that decision. In the
`02:25` the function makes that decision. In the same way, each call to a language model
`02:28` same way, each call to a language model
`02:28` same way, each call to a language model is a function call. Prompt in, text out.
`02:31` is a function call. Prompt in, text out.
`02:31` is a function call. Prompt in, text out. The agentic behavior, the appearance of
`02:33` The agentic behavior, the appearance of
`02:33` The agentic behavior, the appearance of autonomy emerges from the orchestration
`02:35` autonomy emerges from the orchestration
`02:35` autonomy emerges from the orchestration code that wraps those calls. There are
`02:38` code that wraps those calls. There are
`02:38` code that wraps those calls. There are systems beginning to emerge where models
`02:40` systems beginning to emerge where models
`02:40` systems beginning to emerge where models genuinely operate in autonomous loops,
`02:43` genuinely operate in autonomous loops,
`02:43` genuinely operate in autonomous loops, right? Everyone can think about my good
`02:44` right? Everyone can think about my good
`02:44` right? Everyone can think about my good old Clawbot video, but or I think
`02:47` old Clawbot video, but or I think
`02:47` old Clawbot video, but or I think they're called moldbot now. No, open
`02:48` they're called moldbot now. No, open
`02:48` they're called moldbot now. No, open claw. That's the word that they are now.
`02:50` claw. That's the word that they are now.
`02:50` claw. That's the word that they are now. Yeah. Where the model itself decides the
`02:53` Yeah. Where the model itself decides the
`02:53` Yeah. Where the model itself decides the next action. That is a real and
`02:55` next action. That is a real and
`02:55` next action. That is a real and meaningful evolution, but it's not what
`02:57` meaningful evolution, but it's not what
`02:57` meaningful evolution, but it's not what we were looking at in the vast majority
`02:59` we were looking at in the vast majority
`02:59` we were looking at in the vast majority of the deployed systems we have today.
`03:01` of the deployed systems we have today.
`03:01` of the deployed systems we have today. And conflating the two makes it harder
`03:03` And conflating the two makes it harder
`03:03` And conflating the two makes it harder to understand what is actually happening
`03:04` to understand what is actually happening
`03:04` to understand what is actually happening when these systems work. So let us look
`03:07` when these systems work. So let us look
`03:07` when these systems work. So let us look at what is actually happening. And
`03:09` at what is actually happening. And
`03:09` at what is actually happening. And again, let's go into my ethics engine
`03:11` again, let's go into my ethics engine
`03:11` again, let's go into my ethics engine pipeline. The first thing we find when
`03:13` pipeline. The first thing we find when
`03:13` pipeline. The first thing we find when we open the system is not a model. It's
`03:15` we open the system is not a model. It's
`03:15` we open the system is not a model. It's actually more of a traffic controller,
`03:16` actually more of a traffic controller,
`03:16` actually more of a traffic controller, so to speak. My ethics engine needs to
`03:18` so to speak. My ethics engine needs to
`03:18` so to speak. My ethics engine needs to administer dozens of psychometric items
`03:21` administer dozens of psychometric items
`03:21` administer dozens of psychometric items across multiple models simultaneously.
`03:24` across multiple models simultaneously.
`03:24` across multiple models simultaneously. Claude, GPT, Llama, blah blah blah,
`03:26` Claude, GPT, Llama, blah blah blah,
`03:26` Claude, GPT, Llama, blah blah blah, Gemini, all these things. Each provider
`03:28` Gemini, all these things. Each provider
`03:28` Gemini, all these things. Each provider has different rate limits, different
`03:30` has different rate limits, different
`03:30` has different rate limits, different responses, formats, different failure
`03:32` responses, formats, different failure
`03:32` responses, formats, different failure modes. So there is an orchestration
`03:34` modes. So there is an orchestration
`03:34` modes. So there is an orchestration layer that manages all of this and it is
`03:36` layer that manages all of this and it is
`03:36` layer that manages all of this and it is written in Python and it is doing
`03:38` written in Python and it is doing
`03:38` written in Python and it is doing something that would be immediately
`03:40` something that would be immediately
`03:40` something that would be immediately recognizable to anyone who has built a
`03:42` recognizable to anyone who has built a
`03:42` recognizable to anyone who has built a web screener or a trading system or even
`03:44` web screener or a trading system or even
`03:44` web screener or a trading system or even just a ticket reservation platform. It
`03:46` just a ticket reservation platform. It
`03:46` just a ticket reservation platform. It manages concurrency. That's it. It
`03:49` manages concurrency. That's it. It
`03:49` manages concurrency. That's it. It handles retries when requests fails. It
`03:51` handles retries when requests fails. It
`03:51` handles retries when requests fails. It queries prompts and dispatches them in
`03:53` queries prompts and dispatches them in
`03:53` queries prompts and dispatches them in order. It tracks which items have been
`03:55` order. It tracks which items have been
`03:55` order. It tracks which items have been completed and which are still pending.
`03:58` completed and which are still pending.
`03:58` completed and which are still pending. Yet none of this is AI, right? There's
`04:00` Yet none of this is AI, right? There's
`04:00` Yet none of this is AI, right? There's no AI doing any of this work, or at
`04:02` no AI doing any of this work, or at
`04:02` no AI doing any of this work, or at least not the modern AI. This is just
`04:05` least not the modern AI. This is just
`04:05` least not the modern AI. This is just async programming, asynchronous
`04:07` async programming, asynchronous
`04:07` async programming, asynchronous programming. It's concurrency
`04:08` programming. It's concurrency
`04:08` programming. It's concurrency management. These are patterns that
`04:10` management. These are patterns that
`04:10` management. These are patterns that existed long before language models, and
`04:12` existed long before language models, and
`04:12` existed long before language models, and they work the same way as they do
`04:14` they work the same way as they do
`04:14` they work the same way as they do anywhere else. The model at the other
`04:16` anywhere else. The model at the other
`04:16` anywhere else. The model at the other end of each request has no awareness
`04:19` end of each request has no awareness
`04:19` end of each request has no awareness that any of this is happening. It
`04:21` that any of this is happening. It
`04:21` that any of this is happening. It receives a prompt, returns text. That is
`04:23` receives a prompt, returns text. That is
`04:23` receives a prompt, returns text. That is the full extent of its involvement in
`04:25` the full extent of its involvement in
`04:25` the full extent of its involvement in this layer of the system. Which raises a
`04:28` this layer of the system. Which raises a
`04:28` this layer of the system. Which raises a question that I think is worth sitting
`04:29` question that I think is worth sitting
`04:29` question that I think is worth sitting on for a moment. How does the prompt
`04:32` on for a moment. How does the prompt
`04:32` on for a moment. How does the prompt even get to the model? What is the
`04:34` even get to the model? What is the
`04:34` even get to the model? What is the actual mechanism by which one piece of
`04:36` actual mechanism by which one piece of
`04:36` actual mechanism by which one piece of software talks to another? When we say
`04:38` software talks to another? When we say
`04:38` software talks to another? When we say that an AI agent called an API or we
`04:41` that an AI agent called an API or we
`04:41` that an AI agent called an API or we called an API, there's a concept buried
`04:44` called an API, there's a concept buried
`04:44` called an API, there's a concept buried in that sentence that tends to get
`04:45` in that sentence that tends to get
`04:45` in that sentence that tends to get skipped over when people are kind of
`04:47` skipped over when people are kind of
`04:47` skipped over when people are kind of teaching about this stuff. And I think
`04:49` teaching about this stuff. And I think
`04:49` teaching about this stuff. And I think it's worth unpacking because it connects
`04:50` it's worth unpacking because it connects
`04:50` it's worth unpacking because it connects to something larger. An API or an
`04:53` to something larger. An API or an
`04:53` to something larger. An API or an application programming interface is a
`04:56` application programming interface is a
`04:56` application programming interface is a contract. Two pieces of software agree
`04:58` contract. Two pieces of software agree
`04:58` contract. Two pieces of software agree in advance on the shape of their
`05:00` in advance on the shape of their
`05:00` in advance on the shape of their conversation. What the request will look
`05:02` conversation. What the request will look
`05:02` conversation. What the request will look like, what the response will look like,
`05:04` like, what the response will look like,
`05:04` like, what the response will look like, what is allowed and what is not. Neither
`05:07` what is allowed and what is not. Neither
`05:07` what is allowed and what is not. Neither side needs to understand the other's
`05:08` side needs to understand the other's
`05:08` side needs to understand the other's internals. They just need to honor the
`05:11` internals. They just need to honor the
`05:11` internals. They just need to honor the agreement that was made. When the ethics
`05:13` agreement that was made. When the ethics
`05:13` agreement that was made. When the ethics engine sends a prompt to claude, what
`05:15` engine sends a prompt to claude, what
`05:15` engine sends a prompt to claude, what actually happens is an HTTP request
`05:18` actually happens is an HTTP request
`05:18` actually happens is an HTTP request carrying JSON, which is a structured
`05:20` carrying JSON, which is a structured
`05:20` carrying JSON, which is a structured text format, and that goes to an
`05:22` text format, and that goes to an
`05:22` text format, and that goes to an endpoint at Anthropic Servers, company
`05:24` endpoint at Anthropic Servers, company
`05:24` endpoint at Anthropic Servers, company that runs Claude. That JSON contains the
`05:27` that runs Claude. That JSON contains the
`05:27` that runs Claude. That JSON contains the prompt, the model name, and some
`05:29` prompt, the model name, and some
`05:29` prompt, the model name, and some parameters. The server processes it and
`05:32` parameters. The server processes it and
`05:32` parameters. The server processes it and returns JSON containing the models
`05:34` returns JSON containing the models
`05:34` returns JSON containing the models response. A structured text message goes
`05:36` response. A structured text message goes
`05:36` response. A structured text message goes out. A structured text message comes
`05:38` out. A structured text message comes
`05:38` out. A structured text message comes back and everything the ethics engine
`05:40` back and everything the ethics engine
`05:40` back and everything the ethics engine does with that response, the scoring,
`05:42` does with that response, the scoring,
`05:42` does with that response, the scoring, the analysis, the reliability
`05:44` the analysis, the reliability
`05:44` the analysis, the reliability calculations, the synchronous muse and
`05:46` calculations, the synchronous muse and
`05:46` calculations, the synchronous muse and so on. All of that happens locally in
`05:49` so on. All of that happens locally in
`05:49` so on. All of that happens locally in traditional code. This is how software
`05:52` traditional code. This is how software
`05:52` traditional code. This is how software has communicated for decades. Web
`05:54` has communicated for decades. Web
`05:54` has communicated for decades. Web browsers talk to servers this way.
`05:55` browsers talk to servers this way.
`05:55` browsers talk to servers this way. Payment systems talk to banks this way.
`05:57` Payment systems talk to banks this way.
`05:57` Payment systems talk to banks this way. Your weather app talks to a data
`05:59` Your weather app talks to a data
`05:59` Your weather app talks to a data provider this way. This pattern is not
`06:01` provider this way. This pattern is not
`06:01` provider this way. This pattern is not new. But here is where I think it gets a
`06:04` new. But here is where I think it gets a
`06:04` new. But here is where I think it gets a little interesting and where a familiar
`06:06` little interesting and where a familiar
`06:06` little interesting and where a familiar problem resurfaces. What happens when
`06:08` problem resurfaces. What happens when
`06:08` problem resurfaces. What happens when your system needs to talk to not just
`06:10` your system needs to talk to not just
`06:10` your system needs to talk to not just one service but 20? A database, a file
`06:13` one service but 20? A database, a file
`06:13` one service but 20? A database, a file system, a web browser, a code
`06:14` system, a web browser, a code
`06:14` system, a web browser, a code interpreter, a calendar, a search
`06:16` interpreter, a calendar, a search
`06:16` interpreter, a calendar, a search engine. If every connection is
`06:18` engine. If every connection is
`06:18` engine. If every connection is customuilt, you have a scaling problem.
`06:22` customuilt, you have a scaling problem.
`06:22` customuilt, you have a scaling problem. Every new tool requires a new
`06:23` Every new tool requires a new
`06:24` Every new tool requires a new integration. Every new AI application
`06:26` integration. Every new AI application
`06:26` integration. Every new AI application requires its own connectors to every
`06:28` requires its own connectors to every
`06:28` requires its own connectors to every tool it wants to use. The number of
`06:31` tool it wants to use. The number of
`06:31` tool it wants to use. The number of integrations grows as the product of the
`06:33` integrations grows as the product of the
`06:33` integrations grows as the product of the number of application times the number
`06:36` number of application times the number
`06:36` number of application times the number of tools. And that math gets unworkable
`06:39` of tools. And that math gets unworkable
`06:39` of tools. And that math gets unworkable real quickly. But we have fortunately
`06:42` real quickly. But we have fortunately
`06:42` real quickly. But we have fortunately seen this problem before. Well before AI
`06:46` seen this problem before. Well before AI
`06:46` seen this problem before. Well before AI and honestly with every iteration, we
`06:48` and honestly with every iteration, we
`06:48` and honestly with every iteration, we found a solution. Before USB, every
`06:51` found a solution. Before USB, every
`06:51` found a solution. Before USB, every peripheral device had its own connector.
`06:53` peripheral device had its own connector.
`06:53` peripheral device had its own connector. Printers, keyboards, mice, cameras, all
`06:55` Printers, keyboards, mice, cameras, all
`06:55` Printers, keyboards, mice, cameras, all different cables, all different
`06:57` different cables, all different
`06:57` different cables, all different protocols. The solution was to
`06:59` protocols. The solution was to
`06:59` protocols. The solution was to standardize the interface. One
`07:01` standardize the interface. One
`07:01` standardize the interface. One connector, one protocol, and any device
`07:04` connector, one protocol, and any device
`07:04` connector, one protocol, and any device that speaks it can connect to any
`07:06` that speaks it can connect to any
`07:06` that speaks it can connect to any computer that speaks it. Before HTTP,
`07:09` computer that speaks it. Before HTTP,
`07:09` computer that speaks it. Before HTTP, applications each had their own way of
`07:11` applications each had their own way of
`07:11` applications each had their own way of communicating. The solution was to
`07:13` communicating. The solution was to
`07:13` communicating. The solution was to standardize the protocol, one set of
`07:15` standardize the protocol, one set of
`07:15` standardize the protocol, one set of rules for how to request and deliver
`07:17` rules for how to request and deliver
`07:17` rules for how to request and deliver documents, and the web became possible.
`07:20` documents, and the web became possible.
`07:20` documents, and the web became possible. Before the language server protocol,
`07:22` Before the language server protocol,
`07:22` Before the language server protocol, every code editor needed a custom
`07:24` every code editor needed a custom
`07:24` every code editor needed a custom integration for every programming
`07:25` integration for every programming
`07:25` integration for every programming language. syntax highlighting, error
`07:27` language. syntax highlighting, error
`07:28` language. syntax highlighting, error checking, autocomplete, all built
`07:30` checking, autocomplete, all built
`07:30` checking, autocomplete, all built separately for each editor and each
`07:32` separately for each editor and each
`07:32` separately for each editor and each language. The solution was again
`07:35` language. The solution was again
`07:35` language. The solution was again standardize the interface. This is where
`07:37` standardize the interface. This is where
`07:37` standardize the interface. This is where MCP comes in and this is the more modern
`07:40` MCP comes in and this is the more modern
`07:40` MCP comes in and this is the more modern version of this uh history for AI. It's
`07:44` version of this uh history for AI. It's
`07:44` version of this uh history for AI. It's called model context protocol and is a
`07:46` called model context protocol and is a
`07:46` called model context protocol and is a standardized way for AI systems to
`07:48` standardized way for AI systems to
`07:48` standardized way for AI systems to connect to external tools and data
`07:50` connect to external tools and data
`07:50` connect to external tools and data sources. It was introduced by Anthropic
`07:52` sources. It was introduced by Anthropic
`07:52` sources. It was introduced by Anthropic in late 2024 and explicitly inspired by
`07:55` in late 2024 and explicitly inspired by
`07:55` in late 2024 and explicitly inspired by this language server protocol. The
`07:58` this language server protocol. The
`07:58` this language server protocol. The people who built it recognized the
`07:59` people who built it recognized the
`07:59` people who built it recognized the pattern. We already solved this problem
`08:01` pattern. We already solved this problem
`08:01` pattern. We already solved this problem for programming languages talking to
`08:02` for programming languages talking to
`08:02` for programming languages talking to editors. So let us solve it in the same
`08:05` editors. So let us solve it in the same
`08:05` editors. So let us solve it in the same way for AI talking to tools. The
`08:07` way for AI talking to tools. The
`08:07` way for AI talking to tools. The architecture has three parts. A host
`08:10` architecture has three parts. A host
`08:10` architecture has three parts. A host which is the AI application, a client
`08:12` which is the AI application, a client
`08:12` which is the AI application, a client which handles the connection and a
`08:14` which handles the connection and a
`08:14` which handles the connection and a server which wraps the external tool or
`08:15` server which wraps the external tool or
`08:16` server which wraps the external tool or data source and speaks MCP. The model
`08:18` data source and speaks MCP. The model
`08:18` data source and speaks MCP. The model does not call APIs directly. The
`08:20` does not call APIs directly. The
`08:20` does not call APIs directly. The orchestration layer determines what
`08:22` orchestration layer determines what
`08:22` orchestration layer determines what tools to use. The MCP client manages the
`08:24` tools to use. The MCP client manages the
`08:24` tools to use. The MCP client manages the connection and the MCP server translates
`08:27` connection and the MCP server translates
`08:27` connection and the MCP server translates between the protocol and whatever the
`08:29` between the protocol and whatever the
`08:30` between the protocol and whatever the actual tool needs internally. Let's get
`08:32` actual tool needs internally. Let's get
`08:32` actual tool needs internally. Let's get back to the ethics engine. The model
`08:34` back to the ethics engine. The model
`08:34` back to the ethics engine. The model returned a text after having this API
`08:36` returned a text after having this API
`08:36` returned a text after having this API call or tool call sent out. Right? Let's
`08:38` call or tool call sent out. Right? Let's
`08:38` call or tool call sent out. Right? Let's look at what happens next to this text
`08:41` look at what happens next to this text
`08:41` look at what happens next to this text because this is where the ratio becomes
`08:43` because this is where the ratio becomes
`08:43` because this is where the ratio becomes clear. The model's response is sent as a
`08:45` clear. The model's response is sent as a
`08:45` clear. The model's response is sent as a string. natural language, probabilistic
`08:48` string. natural language, probabilistic
`08:48` string. natural language, probabilistic language. The system needs to extract a
`08:50` language. The system needs to extract a
`08:50` language. The system needs to extract a number from that string. And this is a
`08:52` number from that string. And this is a
`08:52` number from that string. And this is a small thing, but it is worth noticing.
`08:54` small thing, but it is worth noticing.
`08:54` small thing, but it is worth noticing. The model operates in language. The
`08:56` The model operates in language. The
`08:56` The model operates in language. The scoring system operates in numbers.
`08:58` scoring system operates in numbers.
`08:58` scoring system operates in numbers. Something has to bridge that gap. And
`09:00` Something has to bridge that gap. And
`09:00` Something has to bridge that gap. And what bridges it is something called
`09:01` what bridges it is something called
`09:01` what bridges it is something called parsing, pattern matching, regular
`09:04` parsing, pattern matching, regular
`09:04` parsing, pattern matching, regular expressions. The same text processing in
`09:06` expressions. The same text processing in
`09:06` expressions. The same text processing in tools that have existed for quite
`09:08` tools that have existed for quite
`09:08` tools that have existed for quite literally decades. The number enters the
`09:11` literally decades. The number enters the
`09:11` literally decades. The number enters the scoring logic. Psychometric instruments
`09:13` scoring logic. Psychometric instruments
`09:13` scoring logic. Psychometric instruments actually have a specific scoring key
`09:15` actually have a specific scoring key
`09:15` actually have a specific scoring key developed and validated over years and
`09:17` developed and validated over years and
`09:17` developed and validated over years and years of clinical research. Some items
`09:19` years of clinical research. Some items
`09:20` years of clinical research. Some items are reverse scored, meaning a response
`09:21` are reverse scored, meaning a response
`09:21` are reverse scored, meaning a response of five gets recorded as a one. And
`09:23` of five gets recorded as a one. And
`09:24` of five gets recorded as a one. And because the question was phrased in a
`09:25` because the question was phrased in a
`09:25` because the question was phrased in a kind of negative direction. Subscales
`09:28` kind of negative direction. Subscales
`09:28` kind of negative direction. Subscales are calculated by aggregating specific
`09:30` are calculated by aggregating specific
`09:30` are calculated by aggregating specific items and creating a new number. And
`09:32` items and creating a new number. And
`09:32` items and creating a new number. And this is just basic arithmetic. All of
`09:34` this is just basic arithmetic. All of
`09:34` this is just basic arithmetic. All of this is validated, peer-reviewed
`09:36` this is validated, peer-reviewed
`09:36` this is validated, peer-reviewed arithmetic, but arithmetic nonetheless.
`09:40` arithmetic, but arithmetic nonetheless.
`09:40` arithmetic, but arithmetic nonetheless. From there you have reliability testing.
`09:41` From there you have reliability testing.
`09:41` From there you have reliability testing. Chromebox alpha for internal
`09:43` Chromebox alpha for internal
`09:43` Chromebox alpha for internal consistency. Test retest correlation for
`09:45` consistency. Test retest correlation for
`09:45` consistency. Test retest correlation for temporal stability. These are all
`09:47` temporal stability. These are all
`09:47` temporal stability. These are all statistical methods implemented in
`09:48` statistical methods implemented in
`09:48` statistical methods implemented in libraries like scypi numpy. Um and that
`09:52` libraries like scypi numpy. Um and that
`09:52` libraries like scypi numpy. Um and that predates large language models by
`09:54` predates large language models by
`09:54` predates large language models by decades as well. The math has not
`09:55` decades as well. The math has not
`09:56` decades as well. The math has not changed since these instruments were
`09:57` changed since these instruments were
`09:57` changed since these instruments were validated on human populations. So
`10:00` validated on human populations. So
`10:00` validated on human populations. So here's what the ethics engine actually
`10:01` here's what the ethics engine actually
`10:01` here's what the ethics engine actually looks like when you lay it out.
`10:03` looks like when you lay it out.
`10:03` looks like when you lay it out. Honestly, the AI sends prompts, receives
`10:05` Honestly, the AI sends prompts, receives
`10:05` Honestly, the AI sends prompts, receives texts, and honestly the actual AI
`10:08` texts, and honestly the actual AI
`10:08` texts, and honestly the actual AI calling is maybe 10% of the system
`10:10` calling is maybe 10% of the system
`10:10` calling is maybe 10% of the system volume. The orchestration, right, async
`10:13` volume. The orchestration, right, async
`10:13` volume. The orchestration, right, async coordination, the rate limming, retry
`10:15` coordination, the rate limming, retry
`10:15` coordination, the rate limming, retry logics, Q management, things like that,
`10:17` logics, Q management, things like that,
`10:17` logics, Q management, things like that, that's maybe 30%. The actual data
`10:20` that's maybe 30%. The actual data
`10:20` that's maybe 30%. The actual data processing, sending and collecting
`10:22` processing, sending and collecting
`10:22` processing, sending and collecting prompts, personas, parsing, scoring,
`10:24` prompts, personas, parsing, scoring,
`10:24` prompts, personas, parsing, scoring, analysis, reliability, that's actually
`10:26` analysis, reliability, that's actually
`10:26` analysis, reliability, that's actually like 60% of the actual code that's going
`10:28` like 60% of the actual code that's going
`10:28` like 60% of the actual code that's going on in this. The ratio is not unique to
`10:31` on in this. The ratio is not unique to
`10:31` on in this. The ratio is not unique to my ethics engine. I'm bringing this up
`10:33` my ethics engine. I'm bringing this up
`10:33` my ethics engine. I'm bringing this up because it's something I see in every
`10:34` because it's something I see in every
`10:34` because it's something I see in every good working AI system I work with. All
`10:37` good working AI system I work with. All
`10:37` good working AI system I work with. All the bad ones seem to ignore this ratio.
`10:39` the bad ones seem to ignore this ratio.
`10:39` the bad ones seem to ignore this ratio. And this is where, if you've been
`10:40` And this is where, if you've been
`10:40` And this is where, if you've been following along through the series, the
`10:42` following along through the series, the
`10:42` following along through the series, the connection starts to surface. We traced
`10:45` connection starts to surface. We traced
`10:45` connection starts to surface. We traced a line of Python down through seven
`10:47` a line of Python down through seven
`10:47` a line of Python down through seven layers of abstraction to electrons that
`10:49` layers of abstraction to electrons that
`10:49` layers of abstraction to electrons that are fundamentally probabilistic. We
`10:51` are fundamentally probabilistic. We
`10:51` are fundamentally probabilistic. We traced memory from registers and cache
`10:53` traced memory from registers and cache
`10:53` traced memory from registers and cache through to context windows and system
`10:55` through to context windows and system
`10:55` through to context windows and system prompts. And we found that the template
`10:57` prompts. And we found that the template
`10:57` prompts. And we found that the template pattern blanks filled according to rules
`11:00` pattern blanks filled according to rules
`11:00` pattern blanks filled according to rules holds at every level. Now, we've taken
`11:02` holds at every level. Now, we've taken
`11:02` holds at every level. Now, we've taken an AI agent apart from the top and found
`11:04` an AI agent apart from the top and found
`11:04` an AI agent apart from the top and found that most of its layers are traditional
`11:07` that most of its layers are traditional
`11:07` that most of its layers are traditional engineering APIs that follow the same
`11:10` engineering APIs that follow the same
`11:10` engineering APIs that follow the same request response pattern software has
`11:12` request response pattern software has
`11:12` request response pattern software has used for decades. Protocols that
`11:14` used for decades. Protocols that
`11:14` used for decades. Protocols that standardize interfaces the same way USB
`11:17` standardize interfaces the same way USB
`11:17` standardize interfaces the same way USB and HTTP did before them. Data
`11:20` and HTTP did before them. Data
`11:20` and HTTP did before them. Data processing that runs on statistical
`11:22` processing that runs on statistical
`11:22` processing that runs on statistical libraries older than the models they
`11:24` libraries older than the models they
`11:24` libraries older than the models they evaluate. Kind of funny when you think
`11:26` evaluate. Kind of funny when you think
`11:26` evaluate. Kind of funny when you think about it. There's this narrative that
`11:28` about it. There's this narrative that
`11:28` about it. There's this narrative that says AI changes everything and then
`11:30` says AI changes everything and then
`11:30` says AI changes everything and then there's this counternarrative that AI is
`11:32` there's this counternarrative that AI is
`11:32` there's this counternarrative that AI is just hype. And while honestly I think
`11:35` just hype. And while honestly I think
`11:35` just hype. And while honestly I think both of those myths what is actually
`11:37` both of those myths what is actually
`11:37` both of those myths what is actually happening and what is interesting in my
`11:39` happening and what is interesting in my
`11:39` happening and what is interesting in my head which is that AI simply extends
`11:41` head which is that AI simply extends
`11:41` head which is that AI simply extends what we've always been doing. It adds a
`11:44` what we've always been doing. It adds a
`11:44` what we've always been doing. It adds a layer where natural language becomes the
`11:46` layer where natural language becomes the
`11:46` layer where natural language becomes the interface and context becomes the
`11:48` interface and context becomes the
`11:48` interface and context becomes the program. But that layer sits on top of
`11:51` program. But that layer sits on top of
`11:51` program. But that layer sits on top of the same exact engineering tradition
`11:54` the same exact engineering tradition
`11:54` the same exact engineering tradition that has been building since we first
`11:56` that has been building since we first
`11:56` that has been building since we first figured out how to route electricity
`11:57` figured out how to route electricity
`11:58` figured out how to route electricity through logic gates. The new thing is
`12:00` through logic gates. The new thing is
`12:00` through logic gates. The new thing is real. The semantic layer, the ability to
`12:03` real. The semantic layer, the ability to
`12:03` real. The semantic layer, the ability to operate meaning rather than syntax. That
`12:05` operate meaning rather than syntax. That
`12:05` operate meaning rather than syntax. That is genuinely novel, but it does not
`12:08` is genuinely novel, but it does not
`12:08` is genuinely novel, but it does not replace the layers beneath it. It
`12:10` replace the layers beneath it. It
`12:10` replace the layers beneath it. It depends on them in certain cases. I'll
`12:12` depends on them in certain cases. I'll
`12:12` depends on them in certain cases. I'll make another video on where I think
`12:13` make another video on where I think
`12:13` make another video on where I think there's a grain of salt there. Here is
`12:15` there's a grain of salt there. Here is
`12:16` there's a grain of salt there. Here is where the word agent becomes interesting
`12:18` where the word agent becomes interesting
`12:18` where the word agent becomes interesting again because I think we're approaching
`12:20` again because I think we're approaching
`12:20` again because I think we're approaching a moment where genuine agentic behavior
`12:23` a moment where genuine agentic behavior
`12:23` a moment where genuine agentic behavior models operating in autonomous loops
`12:25` models operating in autonomous loops
`12:25` models operating in autonomous loops making decisions that were not
`12:26` making decisions that were not
`12:26` making decisions that were not predetermined even by orchestrating code
`12:29` predetermined even by orchestrating code
`12:29` predetermined even by orchestrating code starts to become real. And when that
`12:31` starts to become real. And when that
`12:31` starts to become real. And when that happens the engineer's challenge will
`12:32` happens the engineer's challenge will
`12:32` happens the engineer's challenge will not be making the AI smarter. It will be
`12:35` not be making the AI smarter. It will be
`12:35` not be making the AI smarter. It will be building the infrastructure around it,
`12:37` building the infrastructure around it,
`12:37` building the infrastructure around it, the reliability patterns, the error
`12:39` the reliability patterns, the error
`12:39` the reliability patterns, the error handling, the protocols for safe
`12:41` handling, the protocols for safe
`12:41` handling, the protocols for safe autonomous operation. the same work, in
`12:44` autonomous operation. the same work, in
`12:44` autonomous operation. the same work, in other words, that has accompanied every
`12:46` other words, that has accompanied every
`12:46` other words, that has accompanied every new layer of the stack since Gracehopper
`12:48` new layer of the stack since Gracehopper
`12:48` new layer of the stack since Gracehopper had a compiler that no one believed
`12:50` had a compiler that no one believed
`12:50` had a compiler that no one believed would work. And I'm simply just trying
`12:52` would work. And I'm simply just trying
`12:52` would work. And I'm simply just trying to build software at the top of this
`12:54` to build software at the top of this
`12:54` to build software at the top of this layer. My ethics engine can tell you the
`12:55` layer. My ethics engine can tell you the
`12:55` layer. My ethics engine can tell you the psychological profile of an AI model
`12:57` psychological profile of an AI model
`12:57` psychological profile of an AI model with about 90% reliability. That is a
`12:59` with about 90% reliability. That is a
`13:00` with about 90% reliability. That is a real and useful capability. And the
`13:01` real and useful capability. And the
`13:02` real and useful capability. And the reason it works is not because the AI is
`13:04` reason it works is not because the AI is
`13:04` reason it works is not because the AI is brilliant. The AI does what AI is good
`13:06` brilliant. The AI does what AI is good
`13:06` brilliant. The AI does what AI is good at, which is processing natural language
`13:09` at, which is processing natural language
`13:09` at, which is processing natural language and generating responses shaped by
`13:12` and generating responses shaped by
`13:12` and generating responses shaped by context. The traditional code does what
`13:15` context. The traditional code does what
`13:15` context. The traditional code does what traditional code has always been good
`13:16` traditional code has always been good
`13:16` traditional code has always been good at, which is orchestration, computation,
`13:19` at, which is orchestration, computation,
`13:19` at, which is orchestration, computation, and reliability. And the protocols
`13:21` and reliability. And the protocols
`13:21` and reliability. And the protocols connecting them do what protocols have
`13:23` connecting them do what protocols have
`13:23` connecting them do what protocols have always done, which is letting different
`13:25` always done, which is letting different
`13:25` always done, which is letting different systems communicate without needing to
`13:27` systems communicate without needing to
`13:27` systems communicate without needing to understand each other's internals. That
`13:29` understand each other's internals. That
`13:29` understand each other's internals. That is not less impressive than magic. In my
`13:31` is not less impressive than magic. In my
`13:31` is not less impressive than magic. In my opinion, it's more impressive because
`13:33` opinion, it's more impressive because
`13:33` opinion, it's more impressive because you can actually understand it and it
`13:36` you can actually understand it and it
`13:36` you can actually understand it and it actually works.
`13:39` actually works.
`13:39` actually works. Till next time, friends. Goodbye.