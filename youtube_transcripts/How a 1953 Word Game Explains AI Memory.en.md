# How a 1953 Word Game Explains AI Memory

**Channel:** Jake Van Clief  
**Uploaded:** 2026-02-02  
**Duration:** 14:22  
**URL:** [https://www.youtube.com/watch?v=S3fXSc5z2n4](https://www.youtube.com/watch?v=S3fXSc5z2n4)  

---

## Transcript

`00:03` Picture this. It's 1953 and a television
`00:03` Picture this. It's 1953 and a television writer named Leonard Stern was stuck on
`00:05` writer named Leonard Stern was stuck on
`00:05` writer named Leonard Stern was stuck on an adjective. [music] He was writing a
`00:06` an adjective. [music] He was writing a
`00:06` an adjective. [music] He was writing a script for the honeymooners and he
`00:08` script for the honeymooners and he
`00:08` script for the honeymooners and he needed the right word to describe his
`00:10` needed the right word to describe his
`00:10` needed the right word to describe his boss's nose. His friend Roger Price
`00:12` boss's nose. His friend Roger Price
`00:12` boss's nose. His friend Roger Price walked in and impatient to work on
`00:14` walked in and impatient to work on
`00:14` walked in and impatient to work on something else, Stern said, "I need an
`00:15` something else, Stern said, "I need an
`00:15` something else, Stern said, "I need an adjective that." And before he could
`00:17` adjective that." And before he could
`00:17` adjective that." And before he could finish, Price said, "Clumsy and naked."
`00:20` finish, Price said, "Clumsy and naked."
`00:20` finish, Price said, "Clumsy and naked." Stern laughed because now his boss had a
`00:23` Stern laughed because now his boss had a
`00:23` Stern laughed because now his boss had a clumsy nose or a naked nose. But the
`00:26` clumsy nose or a naked nose. But the
`00:26` clumsy nose or a naked nose. But the words were completely wrong for the
`00:27` words were completely wrong for the
`00:27` words were completely wrong for the context yet somehow still worked and
`00:30` context yet somehow still worked and
`00:30` context yet somehow still worked and they had stumbled onto something. Though
`00:31` they had stumbled onto something. Though
`00:32` they had stumbled onto something. Though it took them five more years to figure
`00:33` it took them five more years to figure
`00:33` it took them five more years to figure out what to call it, they ended up
`00:34` out what to call it, they ended up
`00:34` out what to call it, they ended up calling it Mad Libs. But what they
`00:37` calling it Mad Libs. But what they
`00:37` calling it Mad Libs. But what they actually did is stumble upon something
`00:40` actually did is stumble upon something
`00:40` actually did is stumble upon something that may be the oldest pattern in
`00:42` that may be the oldest pattern in
`00:42` that may be the oldest pattern in computing. You see, what they discovered
`00:45` computing. You see, what they discovered
`00:45` computing. You see, what they discovered was something extremely fundamental to
`00:47` was something extremely fundamental to
`00:47` was something extremely fundamental to how we code and more importantly how we
`00:49` how we code and more importantly how we
`00:49` how we code and more importantly how we use AI today. But before we dive into
`00:52` use AI today. But before we dive into
`00:52` use AI today. But before we dive into that, I think it's important to look at
`00:54` that, I think it's important to look at
`00:54` that, I think it's important to look at how Mad Libs works. And I promise this
`00:56` how Mad Libs works. And I promise this
`00:56` how Mad Libs works. And I promise this is important for discovering and
`00:58` is important for discovering and
`00:58` is important for discovering and understanding computing in general. Just
`01:01` understanding computing in general. Just
`01:01` understanding computing in general. Just stick with me for a second here. You
`01:03` stick with me for a second here. You
`01:03` stick with me for a second here. You see, this is how Mad Lib works. You have
`01:05` see, this is how Mad Lib works. You have
`01:05` see, this is how Mad Lib works. You have a template. The template has blanks.
`01:07` a template. The template has blanks.
`01:07` a template. The template has blanks. Each blank has a type, noun, verb,
`01:09` Each blank has a type, noun, verb,
`01:09` Each blank has a type, noun, verb, adjective. Someone who cannot see the
`01:11` adjective. Someone who cannot see the
`01:11` adjective. Someone who cannot see the template provides words that fit those
`01:13` template provides words that fit those
`01:13` template provides words that fit those types and then you read the results. The
`01:15` types and then you read the results. The
`01:15` types and then you read the results. The comedy comes from the mismatch. The
`01:17` comedy comes from the mismatch. The
`01:17` comedy comes from the mismatch. The person filling in the blanks doesn't
`01:18` person filling in the blanks doesn't
`01:18` person filling in the blanks doesn't know the context. They're providing
`01:20` know the context. They're providing
`01:20` know the context. They're providing semantically correct input without
`01:22` semantically correct input without
`01:22` semantically correct input without semantic awareness. They give you a noun
`01:24` semantic awareness. They give you a noun
`01:24` semantic awareness. They give you a noun and it is in fact a noun, but it's the
`01:26` and it is in fact a noun, but it's the
`01:26` and it is in fact a noun, but it's the wrong noun for the sentence that the
`01:28` wrong noun for the sentence that the
`01:28` wrong noun for the sentence that the wrongness is actually funny. Now, here's
`01:31` wrongness is actually funny. Now, here's
`01:31` wrongness is actually funny. Now, here's something that might reframe how you
`01:32` something that might reframe how you
`01:32` something that might reframe how you think about software. When you write a
`01:35` think about software. When you write a
`01:35` think about software. When you write a line of Python, let's say, you are not
`01:37` line of Python, let's say, you are not
`01:37` line of Python, let's say, you are not talking to the computer. You are filling
`01:39` talking to the computer. You are filling
`01:39` talking to the computer. You are filling in a template. This is called [music] an
`01:42` in a template. This is called [music] an
`01:42` in a template. This is called [music] an abstract syntax tree. It's the structure
`01:45` abstract syntax tree. It's the structure
`01:46` abstract syntax tree. It's the structure your code becomes before anything
`01:47` your code becomes before anything
`01:47` your code becomes before anything executes. And if you look at it, really
`01:49` executes. And if you look at it, really
`01:49` executes. And if you look at it, really look at it, you'll notice something. It
`01:51` look at it, you'll notice something. It
`01:51` look at it, you'll notice something. It has blanks, [music] typed blanks. This
`01:53` has blanks, [music] typed blanks. This
`01:53` has blanks, [music] typed blanks. This node expects an expression. Another node
`01:57` node expects an expression. Another node
`01:57` node expects an expression. Another node actually [music] expects an identifier
`01:59` actually [music] expects an identifier
`01:59` actually [music] expects an identifier and another a value. You, the
`02:01` and another a value. You, the
`02:01` and another a value. You, the programmer, are providing words that fit
`02:04` programmer, are providing words that fit
`02:04` programmer, are providing words that fit those types. The interpreter takes your
`02:06` those types. The interpreter takes your
`02:06` those types. The interpreter takes your input and fills in a much larger
`02:08` input and fills in a much larger
`02:08` input and fills in a much larger template that you never see. Thousands
`02:11` template that you never see. Thousands
`02:11` template that you never see. Thousands of lines of C code with slots for your
`02:13` of lines of C code with slots for your
`02:13` of lines of C code with slots for your variables, your function names, your
`02:15` variables, your function names, your
`02:15` variables, your function names, your values, and [music] that template gets
`02:17` values, and [music] that template gets
`02:17` values, and [music] that template gets filled into another template at the
`02:19` filled into another template at the
`02:19` filled into another template at the assembly level. And that one gets filled
`02:21` assembly level. And that one gets filled
`02:21` assembly level. And that one gets filled into machine code all the way down. Mad
`02:24` into machine code all the way down. Mad
`02:24` into machine code all the way down. Mad Libs isn't a metaphor for programming.
`02:26` Libs isn't a metaphor for programming.
`02:26` Libs isn't a metaphor for programming. It is at a structural level what
`02:29` It is at a structural level what
`02:29` It is at a structural level what programming is. templates [music] with
`02:31` programming is. templates [music] with
`02:31` programming is. templates [music] with type slots filled according to rules
`02:33` type slots filled according to rules
`02:33` type slots filled according to rules composed into larger templates until
`02:35` composed into larger templates until
`02:35` composed into larger templates until eventually something executes. But
`02:37` eventually something executes. But
`02:37` eventually something executes. But templates need to be filled with
`02:39` templates need to be filled with
`02:39` templates need to be filled with something and that something has to be
`02:41` something and that something has to be
`02:41` something and that something has to be stored somewhere. Which brings us to
`02:44` stored somewhere. Which brings us to
`02:44` stored somewhere. Which brings us to memory. In traditional computing, memory
`02:46` memory. In traditional computing, memory
`02:46` memory. In traditional computing, memory is a hierarchy. At the top, closest to
`02:50` is a hierarchy. At the top, closest to
`02:50` is a hierarchy. At the top, closest to the processor, you have registers. Tiny,
`02:53` the processor, you have registers. Tiny,
`02:53` the processor, you have registers. Tiny, incredibly fast, maybe 64 bits each. a
`02:56` incredibly fast, maybe 64 bits each. a
`02:56` incredibly fast, maybe 64 bits each. a handful of values that CPU can access in
`02:59` handful of values that CPU can access in
`02:59` handful of values that CPU can access in a single cycle. [music] However, when
`03:01` a single cycle. [music] However, when
`03:01` a single cycle. [music] However, when you look a little bit up the chain here,
`03:04` you look a little bit up the chain here,
`03:04` you look a little bit up the chain here, you have something called the cache.
`03:06` you have something called the cache.
`03:06` you have something called the cache. Still fast, still small, measured in
`03:09` Still fast, still small, measured in
`03:09` Still fast, still small, measured in kilobytes or megabytes. This is where
`03:11` kilobytes or megabytes. This is where
`03:11` kilobytes or megabytes. This is where the machine keeps data it thinks it will
`03:13` the machine keeps data it thinks it will
`03:13` the machine keeps data it thinks it will need against. The principle is called
`03:16` need against. The principle is called
`03:16` need against. The principle is called locality. But if you accessed something
`03:18` locality. But if you accessed something
`03:18` locality. But if you accessed something once, you'll probably access it again.
`03:21` once, you'll probably access it again.
`03:21` once, you'll probably access it again. If you accessed this address, you'll
`03:23` If you accessed this address, you'll
`03:23` If you accessed this address, you'll probably access a nearby address. Cache
`03:26` probably access a nearby address. Cache
`03:26` probably access a nearby address. Cache exploits that pattern. Then you finally
`03:28` exploits that pattern. Then you finally
`03:28` exploits that pattern. Then you finally move into the main memory or what I
`03:31` move into the main memory or what I
`03:31` move into the main memory or what I would consider the main memory RAM.
`03:33` would consider the main memory RAM.
`03:33` would consider the main memory RAM. Random access memory. Larger, slower,
`03:36` Random access memory. Larger, slower,
`03:36` Random access memory. Larger, slower, often in gigabytes. This is what most
`03:38` often in gigabytes. This is what most
`03:38` often in gigabytes. This is what most people think of when they think of
`03:39` people think of when they think of
`03:39` people think of when they think of computer memory. It holds the working
`03:41` computer memory. It holds the working
`03:41` computer memory. It holds the working state of programs. When you open an
`03:44` state of programs. When you open an
`03:44` state of programs. When you open an application, its code and data load from
`03:46` application, its code and data load from
`03:46` application, its code and data load from the disk into the RAM so the processor
`03:49` the disk into the RAM so the processor
`03:49` the disk into the RAM so the processor can access them without waiting for the
`03:51` can access them without waiting for the
`03:51` can access them without waiting for the slow mechanical process of reading from
`03:54` slow mechanical process of reading from
`03:54` slow mechanical process of reading from storage like discs or archives. Speaking
`03:57` storage like discs or archives. Speaking
`03:57` storage like discs or archives. Speaking of discs, you can have solid state or
`03:59` of discs, you can have solid state or
`03:59` of discs, you can have solid state or even spinning magnetic platters,
`04:01` even spinning magnetic platters,
`04:01` even spinning magnetic platters, terabytes, persistent, and when you save
`04:03` terabytes, persistent, and when you save
`04:03` terabytes, persistent, and when you save a file, this is where it goes. Even
`04:06` a file, this is where it goes. Even
`04:06` a file, this is where it goes. Even below that, you have archival storage.
`04:08` below that, you have archival storage.
`04:08` below that, you have archival storage. This is on tape or cold [music] storage,
`04:10` This is on tape or cold [music] storage,
`04:10` This is on tape or cold [music] storage, the stuff that you back up and and
`04:11` the stuff that you back up and and
`04:11` the stuff that you back up and and rarely touch. Personally, I prefer
`04:14` rarely touch. Personally, I prefer
`04:14` rarely touch. Personally, I prefer solidstate drives. However, hard disk
`04:16` solidstate drives. However, hard disk
`04:16` solidstate drives. However, hard disk drives have their, you know, benefits,
`04:18` drives have their, you know, benefits,
`04:18` drives have their, you know, benefits, that [music] mostly being cheaper. I'm
`04:20` that [music] mostly being cheaper. I'm
`04:20` that [music] mostly being cheaper. I'm not going to go too deep into the
`04:21` not going to go too deep into the
`04:21` not going to go too deep into the differences between these. However, if
`04:23` differences between these. However, if
`04:23` differences between these. However, if anyone wants a video on building
`04:24` anyone wants a video on building
`04:24` anyone wants a video on building computers, I've been building them since
`04:25` computers, I've been building them since
`04:26` computers, I've been building them since I was a teenager, and I'm happy to make
`04:27` I was a teenager, and I'm happy to make
`04:27` I was a teenager, and I'm happy to make some cool ones on that as well. Just
`04:29` some cool ones on that as well. Just
`04:29` some cool ones on that as well. Just please comment below like, "Build me a
`04:31` please comment below like, "Build me a
`04:31` please comment below like, "Build me a computer or something like that." I
`04:32` computer or something like that." I
`04:32` computer or something like that." I don't know. Anyway, the whole system is
`04:34` don't know. Anyway, the whole system is
`04:34` don't know. Anyway, the whole system is a trade-off between speed [music] and
`04:36` a trade-off between speed [music] and
`04:36` a trade-off between speed [music] and capacity. Fast memory is expensive,
`04:39` capacity. Fast memory is expensive,
`04:39` capacity. Fast memory is expensive, small, and cheap memory is slow but
`04:41` small, and cheap memory is slow but
`04:41` small, and cheap memory is slow but large. So we build hierarchies. We move
`04:44` large. So we build hierarchies. We move
`04:44` large. So we build hierarchies. We move data between levels based on how often
`04:46` data between levels based on how often
`04:46` data between levels based on how often it's accessed. We predict what we'll
`04:48` it's accessed. We predict what we'll
`04:48` it's accessed. We predict what we'll need and stage it closer to the
`04:50` need and stage it closer to the
`04:50` need and stage it closer to the processor based on those prediction. But
`04:53` processor based on those prediction. But
`04:53` processor based on those prediction. But here's the part that matters for what
`04:55` here's the part that matters for what
`04:55` here's the part that matters for what comes next. In all of this, there is a
`04:57` comes next. In all of this, there is a
`04:58` comes next. In all of this, there is a hard boundary between code and data. The
`05:01` hard boundary between code and data. The
`05:01` hard boundary between code and data. The instructions that tell the machine what
`05:03` instructions that tell the machine what
`05:03` instructions that tell the machine what to do are kept separate from the
`05:05` to do are kept separate from the
`05:06` to do are kept separate from the information this machine operates on. In
`05:09` information this machine operates on. In
`05:09` information this machine operates on. In fact, mixing them is considered a
`05:12` fact, mixing them is considered a
`05:12` fact, mixing them is considered a security vulnerability. It's how buffer
`05:14` security vulnerability. It's how buffer
`05:14` security vulnerability. It's how buffer overflow attacks work. You trick the
`05:15` overflow attacks work. You trick the
`05:16` overflow attacks work. You trick the machine into treating data as code. The
`05:20` machine into treating data as code. The
`05:20` machine into treating data as code. The separation is seemingly foundational.
`05:22` separation is seemingly foundational.
`05:22` separation is seemingly foundational. It's baked into the architecture until
`05:25` It's baked into the architecture until
`05:25` It's baked into the architecture until it isn't.
`05:27` it isn't.
`05:27` it isn't. When people talk about AI memory, they
`05:29` When people talk about AI memory, they
`05:29` When people talk about AI memory, they usually mean one of two things. Either
`05:32` usually mean one of two things. Either
`05:32` usually mean one of two things. Either they mean the model's training, the
`05:34` they mean the model's training, the
`05:34` they mean the model's training, the patterns baked into the weight through
`05:36` patterns baked into the weight through
`05:36` patterns baked into the weight through its exposure to data, or they mean the
`05:38` its exposure to data, or they mean the
`05:38` its exposure to data, or they mean the context window, the text the model can
`05:40` context window, the text the model can
`05:40` context window, the text the model can see during a single conversation. But if
`05:42` see during a single conversation. But if
`05:42` see during a single conversation. But if you're actually building with these
`05:43` you're actually building with these
`05:44` you're actually building with these systems, you know there's a lot more
`05:45` systems, you know there's a lot more
`05:45` systems, you know there's a lot more going on. And for those of you don't,
`05:47` going on. And for those of you don't,
`05:47` going on. And for those of you don't, there's a hierarchy here, too. And it
`05:49` there's a hierarchy here, too. And it
`05:49` there's a hierarchy here, too. And it rhymes with the one we just talked
`05:50` rhymes with the one we just talked
`05:50` rhymes with the one we just talked about, but the differences really do
`05:52` about, but the differences really do
`05:52` about, but the differences really do matter. At the base, you have the model
`05:55` matter. At the base, you have the model
`05:55` matter. At the base, you have the model weights. This is the closest analog to
`05:57` weights. This is the closest analog to
`05:57` weights. This is the closest analog to ROM, read only memory. It's fixed at
`06:00` ROM, read only memory. It's fixed at
`06:00` ROM, read only memory. It's fixed at training time. It encodes patterns,
`06:02` training time. It encodes patterns,
`06:02` training time. It encodes patterns, knowledge, capabilities. You can't
`06:04` knowledge, capabilities. You can't
`06:04` knowledge, capabilities. You can't change it during inference. It's just
`06:07` change it during inference. It's just
`06:07` change it during inference. It's just what the model knows. From there, you
`06:10` what the model knows. From there, you
`06:10` what the model knows. From there, you can look at another part called the
`06:11` can look at another part called the
`06:11` can look at another part called the context window. This is more like
`06:13` context window. This is more like
`06:13` context window. This is more like working memory. It's everything the
`06:14` working memory. It's everything the
`06:14` working memory. It's everything the model can attend to when generating a
`06:17` model can attend to when generating a
`06:17` model can attend to when generating a response. The system prompt, its
`06:19` response. The system prompt, its
`06:19` response. The system prompt, its conversation history, any documents or
`06:20` conversation history, any documents or
`06:20` conversation history, any documents or data that have been included. It's
`06:22` data that have been included. It's
`06:22` data that have been included. It's temporary and it exists only for this
`06:24` temporary and it exists only for this
`06:24` temporary and it exists only for this interaction. When the conversation ends,
`06:27` interaction. When the conversation ends,
`06:27` interaction. When the conversation ends, it's gone. Now, the rest of these
`06:29` it's gone. Now, the rest of these
`06:29` it's gone. Now, the rest of these memories are kind of stored within all
`06:31` memories are kind of stored within all
`06:31` memories are kind of stored within all of those two. In that context, you have
`06:33` of those two. In that context, you have
`06:33` of those two. In that context, you have a system prompt functions something like
`06:35` a system prompt functions something like
`06:35` a system prompt functions something like a firmware almost. It sets the operating
`06:38` a firmware almost. It sets the operating
`06:38` a firmware almost. It sets the operating parameters. It tells the model what it
`06:39` parameters. It tells the model what it
`06:39` parameters. It tells the model what it is, who it is, what it should do, what
`06:41` is, who it is, what it should do, what
`06:41` is, who it is, what it should do, what constraints to follow, and often the
`06:43` constraints to follow, and often the
`06:43` constraints to follow, and often the user or an outside user typically
`06:45` user or an outside user typically
`06:45` user or an outside user typically doesn't see it, but it does shape
`06:47` doesn't see it, but it does shape
`06:47` doesn't see it, but it does shape everything in the conversation or
`06:49` everything in the conversation or
`06:49` everything in the conversation or process. Then you have retrieved context
`06:52` process. Then you have retrieved context
`06:52` process. Then you have retrieved context things that are pulled dynamically based
`06:54` things that are pulled dynamically based
`06:54` things that are pulled dynamically based on a query, a relevant document or a
`06:56` on a query, a relevant document or a
`06:56` on a query, a relevant document or a skill file that contains specialized
`06:58` skill file that contains specialized
`06:58` skill file that contains specialized instructions. This is like loading from
`07:00` instructions. This is like loading from
`07:00` instructions. This is like loading from a disk into RAM. It happens on demand.
`07:04` a disk into RAM. It happens on demand.
`07:04` a disk into RAM. It happens on demand. However, there's another version of this
`07:06` However, there's another version of this
`07:06` However, there's another version of this that is still the same, but I think is
`07:09` that is still the same, but I think is
`07:09` that is still the same, but I think is important to separate. It's called
`07:11` important to separate. It's called
`07:11` important to separate. It's called persistent memory. And this is
`07:12` persistent memory. And this is
`07:12` persistent memory. And this is information stored between conversations
`07:15` information stored between conversations
`07:15` information stored between conversations and selectively loaded when relevant.
`07:17` and selectively loaded when relevant.
`07:17` and selectively loaded when relevant. Almost like summaries. It's not
`07:18` Almost like summaries. It's not
`07:18` Almost like summaries. It's not everything, just what seems useful for
`07:21` everything, just what seems useful for
`07:21` everything, just what seems useful for every single conversation. And it's
`07:23` every single conversation. And it's
`07:23` every single conversation. And it's retrieved in the same way as the
`07:25` retrieved in the same way as the
`07:25` retrieved in the same way as the previous method, but just is a slightly
`07:27` previous method, but just is a slightly
`07:27` previous method, but just is a slightly different concept around it. But if you
`07:29` different concept around it. But if you
`07:29` different concept around it. But if you squint, this looks like a traditional
`07:31` squint, this looks like a traditional
`07:31` squint, this looks like a traditional hierarchy. Speed versus capacity
`07:33` hierarchy. Speed versus capacity
`07:33` hierarchy. Speed versus capacity trade-offs, data moving between levels,
`07:36` trade-offs, data moving between levels,
`07:36` trade-offs, data moving between levels, locality patterns [music] determining
`07:37` locality patterns [music] determining
`07:37` locality patterns [music] determining what gets loaded. But there is a
`07:40` what gets loaded. But there is a
`07:40` what gets loaded. But there is a difference, and it's not a small one. In
`07:42` difference, and it's not a small one. In
`07:42` difference, and it's not a small one. In this system with AI, code and data end
`07:45` this system with AI, code and data end
`07:46` this system with AI, code and data end up being the same thing. The system
`07:48` up being the same thing. The system
`07:48` up being the same thing. The system prompt is not compiled separately from
`07:50` prompt is not compiled separately from
`07:50` prompt is not compiled separately from the user's message. The skill file is
`07:52` the user's message. The skill file is
`07:52` the user's message. The skill file is not executed through a different pathway
`07:53` not executed through a different pathway
`07:53` not executed through a different pathway than the conversation history. They are
`07:55` than the conversation history. They are
`07:55` than the conversation history. They are all just text. All processed
`07:57` all just text. All processed
`07:57` all just text. All processed identically, all tokens in a sequence
`08:00` identically, all tokens in a sequence
`08:00` identically, all tokens in a sequence that the model attends to and continues.
`08:03` that the model attends to and continues.
`08:03` that the model attends to and continues. When you write an instruction in a
`08:05` When you write an instruction in a
`08:05` When you write an instruction in a system prompt, you're not giving the
`08:06` system prompt, you're not giving the
`08:06` system prompt, you're not giving the model a command that it executes. You're
`08:08` model a command that it executes. You're
`08:08` model a command that it executes. You're adding words to a document that the
`08:10` adding words to a document that the
`08:10` adding words to a document that the model will read and then continue. The
`08:14` model will read and then continue. The
`08:14` model will read and then continue. The instructions become part of the context.
`08:16` instructions become part of the context.
`08:16` instructions become part of the context. reading it is the execution. And this is
`08:19` reading it is the execution. And this is
`08:19` reading it is the execution. And this is why prompt injection works. If someone
`08:21` why prompt injection works. If someone
`08:21` why prompt injection works. If someone puts text in a document that says ignore
`08:23` puts text in a document that says ignore
`08:23` puts text in a document that says ignore your previous instructions, and that
`08:25` your previous instructions, and that
`08:25` your previous instructions, and that document gets loaded into the context,
`08:27` document gets loaded into the context,
`08:27` document gets loaded into the context, the model reads those [music] words the
`08:29` the model reads those [music] words the
`08:29` the model reads those [music] words the same way it reads everything else. There
`08:31` same way it reads everything else. There
`08:31` same way it reads everything else. There is no separate layer that validates code
`08:34` is no separate layer that validates code
`08:34` is no separate layer that validates code versus data. There is no boundary to
`08:36` versus data. There is no boundary to
`08:36` versus data. There is no boundary to cross. It's all just text. But this is
`08:39` cross. It's all just text. But this is
`08:39` cross. It's all just text. But this is not a bug. It is the architecture. And
`08:42` not a bug. It is the architecture. And
`08:42` not a bug. It is the architecture. And when I say that, I think it's important
`08:44` when I say that, I think it's important
`08:44` when I say that, I think it's important for us to go back in time. Back into
`08:46` for us to go back in time. Back into
`08:46` for us to go back in time. Back into 1952,
`08:48` 1952,
`08:48` 1952, Grace Hopper had a working compiler. It
`08:51` Grace Hopper had a working compiler. It
`08:51` Grace Hopper had a working compiler. It could take instructions written in
`08:52` could take instructions written in
`08:52` could take instructions written in something closer to English and
`08:54` something closer to English and
`08:54` something closer to English and translate them into machine code.
`08:57` translate them into machine code.
`08:57` translate them into machine code. However, nobody believed her. She said,
`09:00` However, nobody believed her. She said,
`09:00` However, nobody believed her. She said, "I had a running compiler and nobody
`09:02` "I had a running compiler and nobody
`09:02` "I had a running compiler and nobody would touch it. They told me computers
`09:03` would touch it. They told me computers
`09:03` would touch it. They told me computers could only do arithmetic." She spent
`09:06` could only do arithmetic." She spent
`09:06` could only do arithmetic." She spent years trying to convince people that her
`09:08` years trying to convince people that her
`09:08` years trying to convince people that her compiler was truly possible, or at least
`09:10` compiler was truly possible, or at least
`09:10` compiler was truly possible, or at least this type of process and abstraction.
`09:12` this type of process and abstraction.
`09:12` this type of process and abstraction. But she said people were allergic to
`09:14` But she said people were allergic to
`09:14` But she said people were allergic to change. Now the skepticism came from a
`09:17` change. Now the skepticism came from a
`09:17` change. Now the skepticism came from a genuine place. Compilers did arithmetic.
`09:20` genuine place. Compilers did arithmetic.
`09:20` genuine place. Compilers did arithmetic. That was the foundational truth.
`09:22` That was the foundational truth.
`09:22` That was the foundational truth. However, a compiler seemed to violate
`09:24` However, a compiler seemed to violate
`09:24` However, a compiler seemed to violate that truth by claiming computers could
`09:26` that truth by claiming computers could
`09:26` that truth by claiming computers could process language. However, Hopper wasn't
`09:29` process language. However, Hopper wasn't
`09:29` process language. However, Hopper wasn't claiming that computers had stopped
`09:31` claiming that computers had stopped
`09:31` claiming that computers had stopped doing arithmetic. She had simply built a
`09:34` doing arithmetic. She had simply built a
`09:34` doing arithmetic. She had simply built a layer on top of that that translated
`09:36` layer on top of that that translated
`09:36` layer on top of that that translated human readable instructions into the
`09:38` human readable instructions into the
`09:38` human readable instructions into the arithmetic the machine already
`09:41` arithmetic the machine already
`09:41` arithmetic the machine already understood. The machine still did what
`09:43` understood. The machine still did what
`09:43` understood. The machine still did what it always did. The abstractions just
`09:45` it always did. The abstractions just
`09:45` it always did. The abstractions just made it accessible to more people in new
`09:47` made it accessible to more people in new
`09:48` made it accessible to more people in new ways. And this pattern repeated.
`09:50` ways. And this pattern repeated.
`09:50` ways. And this pattern repeated. Assembly gave way to higher level
`09:52` Assembly gave way to higher level
`09:52` Assembly gave way to higher level languages. Those gave way to interpreted
`09:54` languages. Those gave way to interpreted
`09:54` languages. Those gave way to interpreted languages. Each time skeptics pointed to
`09:56` languages. Each time skeptics pointed to
`09:56` languages. Each time skeptics pointed to the layer below and said, "This is
`09:58` the layer below and said, "This is
`09:58` the layer below and said, "This is what's really happening and you're
`09:59` what's really happening and you're
`09:59` what's really happening and you're adding unreliability by abstracting it.
`10:02` adding unreliability by abstracting it.
`10:02` adding unreliability by abstracting it. And each time engineers built the
`10:04` And each time engineers built the
`10:04` And each time engineers built the infrastructure to make the new layer
`10:06` infrastructure to make the new layer
`10:06` infrastructure to make the new layer reliable enough to trust." Now, I talked
`10:09` reliable enough to trust." Now, I talked
`10:09` reliable enough to trust." Now, I talked a whole bunch about this in a previous
`10:11` a whole bunch about this in a previous
`10:11` a whole bunch about this in a previous video. Please go check it out. But if
`10:13` video. Please go check it out. But if
`10:13` video. Please go check it out. But if you trace a single line of Python from
`10:15` you trace a single line of Python from
`10:15` you trace a single line of Python from all the way down through the
`10:17` all the way down through the
`10:17` all the way down through the interpreter, through the C code, through
`10:19` interpreter, through the C code, through
`10:19` interpreter, through the C code, through the assembly, through the machine code,
`10:21` the assembly, through the machine code,
`10:21` the assembly, through the machine code, through transistors, you eventually hit
`10:23` through transistors, you eventually hit
`10:23` through transistors, you eventually hit electrons, particles that at the quantum
`10:25` electrons, particles that at the quantum
`10:25` electrons, particles that at the quantum level are genuinely probabilistic, not
`10:28` level are genuinely probabilistic, not
`10:28` level are genuinely probabilistic, not deterministic. They don't have definite
`10:30` deterministic. They don't have definite
`10:30` deterministic. They don't have definite positions until measured. The entire
`10:33` positions until measured. The entire
`10:33` positions until measured. The entire supposedly deterministic computing stack
`10:35` supposedly deterministic computing stack
`10:35` supposedly deterministic computing stack is built on quantum uncertainty. We made
`10:38` is built on quantum uncertainty. We made
`10:38` is built on quantum uncertainty. We made it reliable through architecture,
`10:41` it reliable through architecture,
`10:41` it reliable through architecture, through error correction, through
`10:43` through error correction, through
`10:43` through error correction, through redundancy, through engineering that
`10:46` redundancy, through engineering that
`10:46` redundancy, through engineering that handles the failures we can't prevent.
`10:49` handles the failures we can't prevent.
`10:49` handles the failures we can't prevent. When people say AI can't be trusted
`10:51` When people say AI can't be trusted
`10:51` When people say AI can't be trusted because it's probabilistic, they're not
`10:53` because it's probabilistic, they're not
`10:53` because it's probabilistic, they're not wrong at one level, but they're missing
`10:56` wrong at one level, but they're missing
`10:56` wrong at one level, but they're missing the pattern. Every layer of the stack
`10:58` the pattern. Every layer of the stack
`10:58` the pattern. Every layer of the stack was probabilistic or unreliable at
`11:01` was probabilistic or unreliable at
`11:01` was probabilistic or unreliable at first. Grace Hopper's compiler was
`11:04` first. Grace Hopper's compiler was
`11:04` first. Grace Hopper's compiler was unreliable until it wasn't. Highle
`11:07` unreliable until it wasn't. Highle
`11:07` unreliable until it wasn't. Highle languages were toys until they weren't.
`11:09` languages were toys until they weren't.
`11:09` languages were toys until they weren't. The reliability came from building the
`11:11` The reliability came from building the
`11:12` The reliability came from building the infrastructure, from doing the
`11:13` infrastructure, from doing the
`11:13` infrastructure, from doing the engineering work. That work is happening
`11:16` engineering work. That work is happening
`11:16` engineering work. That work is happening now. It just looks different because the
`11:18` now. It just looks different because the
`11:18` now. It just looks different because the abstraction layer is different. And if
`11:21` abstraction layer is different. And if
`11:21` abstraction layer is different. And if it is different, let's go look at all
`11:23` it is different, let's go look at all
`11:23` it is different, let's go look at all this but from the perspective of
`11:25` this but from the perspective of
`11:25` this but from the perspective of prompting. And you see, most people
`11:28` prompting. And you see, most people
`11:28` prompting. And you see, most people think of right, write me a poem, be
`11:30` think of right, write me a poem, be
`11:30` think of right, write me a poem, be specific, add examples, use personas
`11:32` specific, add examples, use personas
`11:32` specific, add examples, use personas compared to what we were just looking at
`11:34` compared to what we were just looking at
`11:34` compared to what we were just looking at a little bit ago, right? this idea of
`11:35` a little bit ago, right? this idea of
`11:35` a little bit ago, right? this idea of memory. How is memory being used to move
`11:38` memory. How is memory being used to move
`11:38` memory. How is memory being used to move all these things around? Right? Most
`11:40` all these things around? Right? Most
`11:40` all these things around? Right? Most people just talk about tips [music]
`11:42` people just talk about tips [music]
`11:42` people just talk about tips [music] and tricks. And this is really just
`11:44` and tricks. And this is really just
`11:44` and tricks. And this is really just surface level. It's like telling someone
`11:45` surface level. It's like telling someone
`11:45` surface level. It's like telling someone that programming is about knowing which
`11:47` that programming is about knowing which
`11:47` that programming is about knowing which words to type, which technically it is,
`11:49` words to type, which technically it is,
`11:49` words to type, which technically it is, but it's much more than that. And I see
`11:51` but it's much more than that. And I see
`11:51` but it's much more than that. And I see a lot of engineers completely ignoring
`11:53` a lot of engineers completely ignoring
`11:53` a lot of engineers completely ignoring this difference and people just getting
`11:55` this difference and people just getting
`11:55` this difference and people just getting into the AI world. Production looks
`11:58` into the AI world. Production looks
`11:58` into the AI world. Production looks completely different. We ask a lot of
`12:00` completely different. We ask a lot of
`12:00` completely different. We ask a lot of different questions. Architectural
`12:02` different questions. Architectural
`12:02` different questions. Architectural design decisions, things like that, like
`12:04` design decisions, things like that, like
`12:04` design decisions, things like that, like how to structure memory files, when to
`12:05` how to structure memory files, when to
`12:05` how to structure memory files, when to retrieve additional information, how do
`12:07` retrieve additional information, how do
`12:07` retrieve additional information, how do we manage the interaction between system
`12:09` we manage the interaction between system
`12:09` we manage the interaction between system level instructions and user input, how
`12:11` level instructions and user input, how
`12:11` level instructions and user input, how do we handle the fact that all this gets
`12:13` do we handle the fact that all this gets
`12:13` do we handle the fact that all this gets flattened into a single stream where
`12:15` flattened into a single stream where
`12:15` flattened into a single stream where code and data are indistinguishable.
`12:18` code and data are indistinguishable.
`12:18` code and data are indistinguishable. This is the same discipline. It's not
`12:21` This is the same discipline. It's not
`12:21` This is the same discipline. It's not anything different than the last 100,
`12:23` anything different than the last 100,
`12:23` anything different than the last 100, 200 years. It's what prompting looks
`12:25` 200 years. It's what prompting looks
`12:25` 200 years. It's what prompting looks like when you actually go deeper. And
`12:28` like when you actually go deeper. And
`12:28` like when you actually go deeper. And you see this is programming. It's at the
`12:31` you see this is programming. It's at the
`12:31` you see this is programming. It's at the highest abstraction layer we've built so
`12:33` highest abstraction layer we've built so
`12:33` highest abstraction layer we've built so far. [music]
`12:33` far. [music]
`12:34` far. [music] It's natural language as an interface
`12:36` It's natural language as an interface
`12:36` It's natural language as an interface and meaning as the mechanism. In prior
`12:39` and meaning as the mechanism. In prior
`12:39` and meaning as the mechanism. In prior lower languages, syntax was compiling
`12:42` lower languages, syntax was compiling
`12:42` lower languages, syntax was compiling into machine code. But now we're looking
`12:45` into machine code. But now we're looking
`12:45` into machine code. But now we're looking at context that shapes probability
`12:48` at context that shapes probability
`12:48` at context that shapes probability distributions over continuations. The
`12:50` distributions over continuations. The
`12:50` distributions over continuations. The Mad [music] Libs pattern template still
`12:52` Mad [music] Libs pattern template still
`12:52` Mad [music] Libs pattern template still holds. You're filling type slots in a
`12:55` holds. You're filling type slots in a
`12:55` holds. You're filling type slots in a structure you can't fully see and the
`12:57` structure you can't fully see and the
`12:57` structure you can't fully see and the output depends on what you provide and
`13:00` output depends on what you provide and
`13:00` output depends on what you provide and [music] where it goes. The difference is
`13:03` [music] where it goes. The difference is
`13:03` [music] where it goes. The difference is what we're optimizing for. In Mad Libs,
`13:06` what we're optimizing for. In Mad Libs,
`13:06` what we're optimizing for. In Mad Libs, the wrong word is funny. In programming,
`13:09` the wrong word is funny. In programming,
`13:09` the wrong word is funny. In programming, the wrong word is a bug. In prompting,
`13:12` the wrong word is a bug. In prompting,
`13:12` the wrong word is a bug. In prompting, the wrong context is a hallucination, a
`13:15` the wrong context is a hallucination, a
`13:15` the wrong context is a hallucination, a jailbreak, a failure to understand what
`13:18` jailbreak, a failure to understand what
`13:18` jailbreak, a failure to understand what you actually need. And we're [music]
`13:19` you actually need. And we're [music]
`13:19` you actually need. And we're [music] still in the early days of figuring out
`13:22` still in the early days of figuring out
`13:22` still in the early days of figuring out what the right abstractions are, what
`13:24` what the right abstractions are, what
`13:24` what the right abstractions are, what structures make this reliable, what
`13:26` structures make this reliable, what
`13:26` structures make this reliable, what architectural patterns let us trust the
`13:29` architectural patterns let us trust the
`13:29` architectural patterns let us trust the output. The way we eventually learn to
`13:31` output. The way we eventually learn to
`13:31` output. The way we eventually learn to trust compilers, learn to trust garbage
`13:34` trust compilers, learn to trust garbage
`13:34` trust compilers, learn to trust garbage collection and all these other layers of
`13:36` collection and all these other layers of
`13:36` collection and all these other layers of abstraction between our code and the
`13:38` abstraction between our code and the
`13:38` abstraction between our code and the electrons underneath.
`13:41` electrons underneath.
`13:41` electrons underneath. Grace Hopper once said that the most
`13:43` Grace Hopper once said that the most
`13:43` Grace Hopper once said that the most dangerous phrase in the e- language is
`13:45` dangerous phrase in the e- language is
`13:45` dangerous phrase in the e- language is we've always done it this way. We're at
`13:48` we've always done it this way. We're at
`13:48` we've always done it this way. We're at a moment where the patterns are
`13:49` a moment where the patterns are
`13:49` a moment where the patterns are repeating, but the medium looks
`13:51` repeating, but the medium looks
`13:51` repeating, but the medium looks different enough that it's easy to miss.
`13:53` different enough that it's easy to miss.
`13:53` different enough that it's easy to miss. The skepticism sounds reasonable. The
`13:55` The skepticism sounds reasonable. The
`13:55` The skepticism sounds reasonable. The concerns about reliability are real, but
`13:58` concerns about reliability are real, but
`13:58` concerns about reliability are real, but the path forward is the same path it's
`14:01` the path forward is the same path it's
`14:01` the path forward is the same path it's always been. Build the infrastructure.
`14:03` always been. Build the infrastructure.
`14:03` always been. Build the infrastructure. Do the engineering. Make the unreliable
`14:06` Do the engineering. Make the unreliable
`14:06` Do the engineering. Make the unreliable thing reliable enough to trust. That is
`14:08` thing reliable enough to trust. That is
`14:08` thing reliable enough to trust. That is what prompting is at this level at
`14:10` what prompting is at this level at
`14:10` what prompting is at this level at least. Not tips for talking to a
`14:13` least. Not tips for talking to a
`14:13` least. Not tips for talking to a chatbot, not tricks for getting better
`14:15` chatbot, not tricks for getting better
`14:15` chatbot, not tricks for getting better outputs. It's the next layer of the
`14:17` outputs. It's the next layer of the
`14:18` outputs. It's the next layer of the stack. Until next time, my friends, have
`14:21` stack. Until next time, my friends, have
`14:21` stack. Until next time, my friends, have a good day.