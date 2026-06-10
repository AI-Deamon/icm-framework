# How One Line of Python Triggers 12,000 Lines of Code

**Channel:** Jake Van Clief  
**Uploaded:** 2026-02-01  
**Duration:** 13:23  
**URL:** [https://www.youtube.com/watch?v=5B6W2OGfxq0](https://www.youtube.com/watch?v=5B6W2OGfxq0)  

---

## Transcript

`00:03` I typed seven words into an AI. Write
`00:03` I typed seven words into an AI. Write hello world in Python. And it gave me
`00:04` hello world in Python. And it gave me
`00:04` hello world in Python. And it gave me this in perfect syntax. Print hello
`00:07` this in perfect syntax. Print hello
`00:07` this in perfect syntax. Print hello world. That's it. One line, 22
`00:10` world. That's it. One line, 22
`00:10` world. That's it. One line, 22 characters. But what most people don't
`00:11` characters. But what most people don't
`00:11` characters. But what most people don't realize is that single line of Python
`00:13` realize is that single line of Python
`00:13` realize is that single line of Python triggers roughly 12,000 lines of code
`00:16` triggers roughly 12,000 lines of code
`00:16` triggers roughly 12,000 lines of code across seven distinct layers of
`00:17` across seven distinct layers of
`00:17` across seven distinct layers of abstraction, millions of transistor
`00:19` abstraction, millions of transistor
`00:19` abstraction, millions of transistor state changes, and billions of electron
`00:22` state changes, and billions of electron
`00:22` state changes, and billions of electron movements. And every single one of those
`00:23` movements. And every single one of those
`00:23` movements. And every single one of those electrons probabilistic. But we'll come
`00:26` electrons probabilistic. But we'll come
`00:26` electrons probabilistic. But we'll come back to that later. Let's go ahead and
`00:28` back to that later. Let's go ahead and
`00:28` back to that later. Let's go ahead and start at the top of this stack. Hello
`00:31` start at the top of this stack. Hello
`00:31` start at the top of this stack. Hello world. This is what you write. It's
`00:35` world. This is what you write. It's
`00:35` world. This is what you write. It's clean. It's readable. A child could
`00:38` clean. It's readable. A child could
`00:38` clean. It's readable. A child could understand what it's supposed to do
`00:39` understand what it's supposed to do
`00:39` understand what it's supposed to do after a few lessons. But Python doesn't
`00:41` after a few lessons. But Python doesn't
`00:41` after a few lessons. But Python doesn't run this. Your computer doesn't
`00:43` run this. Your computer doesn't
`00:43` run this. Your computer doesn't understand English or Python or anything
`00:45` understand English or Python or anything
`00:45` understand English or Python or anything resembling human language. So what
`00:48` resembling human language. So what
`00:48` resembling human language. So what actually happens?
`00:50` actually happens?
`00:50` actually happens? First, if you look at the top, Python
`00:53` First, if you look at the top, Python
`00:53` First, if you look at the top, Python reads your text and builds something
`00:55` reads your text and builds something
`00:55` reads your text and builds something called an abstract syntax tree. It's
`00:58` called an abstract syntax tree. It's
`00:58` called an abstract syntax tree. It's exactly what it sounds like, a tree
`01:00` exactly what it sounds like, a tree
`01:00` exactly what it sounds like, a tree structure representing the grammar of
`01:03` structure representing the grammar of
`01:03` structure representing the grammar of your code. Your one line becomes
`01:05` your code. Your one line becomes
`01:05` your code. Your one line becomes something like this. Every keyword,
`01:09` something like this. Every keyword,
`01:09` something like this. Every keyword, every function, every string actually
`01:12` every function, every string actually
`01:12` every function, every string actually gets a node. And Python is basically
`01:14` gets a node. And Python is basically
`01:14` gets a node. And Python is basically diagramming your sentence the way you
`01:16` diagramming your sentence the way you
`01:16` diagramming your sentence the way you might have diagrammed sentences in grade
`01:18` might have diagrammed sentences in grade
`01:18` might have diagrammed sentences in grade school. subject, verb, object. Except
`01:21` school. subject, verb, object. Except
`01:21` school. subject, verb, object. Except here, it's function, argument, and
`01:24` here, it's function, argument, and
`01:24` here, it's function, argument, and value. This tree is how Python
`01:27` value. This tree is how Python
`01:27` value. This tree is how Python understands structure. But it still
`01:30` understands structure. But it still
`01:30` understands structure. But it still can't actually run anything on your
`01:32` can't actually run anything on your
`01:32` can't actually run anything on your computer. Next, what Python does is it
`01:36` computer. Next, what Python does is it
`01:36` computer. Next, what Python does is it compiles all of your code into something
`01:39` compiles all of your code into something
`01:39` compiles all of your code into something called byte code. These are simple
`01:41` called byte code. These are simple
`01:41` called byte code. These are simple instructions for Python's virtual
`01:44` instructions for Python's virtual
`01:44` instructions for Python's virtual machine. Load the function called print.
`01:47` machine. Load the function called print.
`01:47` machine. Load the function called print. Load the string called hello world. Call
`01:50` Load the string called hello world. Call
`01:50` Load the string called hello world. Call the function with that string. Three
`01:52` the function with that string. Three
`01:52` the function with that string. Three instructions, still abstract, still not
`01:55` instructions, still abstract, still not
`01:55` instructions, still abstract, still not running on your actual hardware. By code
`01:58` running on your actual hardware. By code
`01:58` running on your actual hardware. By code is like sheet music. It tells you what
`02:00` is like sheet music. It tells you what
`02:00` is like sheet music. It tells you what notes to play, but it's not sound.
`02:02` notes to play, but it's not sound.
`02:02` notes to play, but it's not sound. Someone still has to perform it. And
`02:04` Someone still has to perform it. And
`02:04` Someone still has to perform it. And here's where things get interesting.
`02:06` here's where things get interesting.
`02:06` here's where things get interesting. Python itself is written in another
`02:08` Python itself is written in another
`02:08` Python itself is written in another language, C. When you run Python, you're
`02:11` language, C. When you run Python, you're
`02:11` language, C. When you run Python, you're actually running a C program that reads
`02:14` actually running a C program that reads
`02:14` actually running a C program that reads bite code and executes it. So the call
`02:17` bite code and executes it. So the call
`02:17` bite code and executes it. So the call instruction, it triggers something like
`02:19` instruction, it triggers something like
`02:20` instruction, it triggers something like this in C. This is simplified. The
`02:23` this in C. This is simplified. The
`02:23` this in C. This is simplified. The actual implementation spans literally
`02:25` actual implementation spans literally
`02:25` actual implementation spans literally thousands of lines. But notice
`02:26` thousands of lines. But notice
`02:26` thousands of lines. But notice something. There's error handling in
`02:28` something. There's error handling in
`02:28` something. There's error handling in there. If call equal equals null. What
`02:32` there. If call equal equals null. What
`02:32` there. If call equal equals null. What happens if you try to call something
`02:34` happens if you try to call something
`02:34` happens if you try to call something that isn't a function? The code catches
`02:36` that isn't a function? The code catches
`02:36` that isn't a function? The code catches it, handles it gracefully. Every layer
`02:39` it, handles it gracefully. Every layer
`02:39` it, handles it gracefully. Every layer has error handling. Every layer has
`02:42` has error handling. Every layer has
`02:42` has error handling. Every layer has rules. This becomes very important later
`02:45` rules. This becomes very important later
`02:45` rules. This becomes very important later as we come to talk about AI in this
`02:47` as we come to talk about AI in this
`02:47` as we come to talk about AI in this giant stack. Now, the C compiler itself
`02:51` giant stack. Now, the C compiler itself
`02:51` giant stack. Now, the C compiler itself transforms that code into something
`02:53` transforms that code into something
`02:53` transforms that code into something called assembly language. You see, C
`02:57` called assembly language. You see, C
`02:57` called assembly language. You see, C can't actually fully compile that code
`02:59` can't actually fully compile that code
`02:59` can't actually fully compile that code to run it either. Assembly is a step
`03:02` to run it either. Assembly is a step
`03:02` to run it either. Assembly is a step away from the hardware itself. Each line
`03:06` away from the hardware itself. Each line
`03:06` away from the hardware itself. Each line maps almost directly to something the
`03:08` maps almost directly to something the
`03:08` maps almost directly to something the CPU can do. Uh you'll see a lot of
`03:12` CPU can do. Uh you'll see a lot of
`03:12` CPU can do. Uh you'll see a lot of statements like push RBP means save the
`03:15` statements like push RBP means save the
`03:15` statements like push RBP means save the current base pointer, move RBP. RSP
`03:19` current base pointer, move RBP. RSP
`03:19` current base pointer, move RBP. RSP means set the base pointer to the stack
`03:21` means set the base pointer to the stack
`03:21` means set the base pointer to the stack pointer. These are operations on
`03:24` pointer. These are operations on
`03:24` pointer. These are operations on registers, tiny pieces of memory inside
`03:27` registers, tiny pieces of memory inside
`03:27` registers, tiny pieces of memory inside the CPU itself. And finally, with all of
`03:30` the CPU itself. And finally, with all of
`03:30` the CPU itself. And finally, with all of that, we're actually getting close to
`03:32` that, we're actually getting close to
`03:32` that, we're actually getting close to the metal now, or at least closer to
`03:34` the metal now, or at least closer to
`03:34` the metal now, or at least closer to where everything's going on. And this is
`03:37` where everything's going on. And this is
`03:37` where everything's going on. And this is where we find a very interesting
`03:39` where we find a very interesting
`03:39` where we find a very interesting transition where assembly becomes
`03:42` transition where assembly becomes
`03:42` transition where assembly becomes machine code. Machine code is raw bytes,
`03:46` machine code. Machine code is raw bytes,
`03:46` machine code. Machine code is raw bytes, hexadesimal. And this is what the actual
`03:49` hexadesimal. And this is what the actual
`03:49` hexadesimal. And this is what the actual CPU, the brain of your computer reads.
`03:52` CPU, the brain of your computer reads.
`03:52` CPU, the brain of your computer reads. The number 55 means push RBP. The bytes
`03:57` The number 55 means push RBP. The bytes
`03:57` The number 55 means push RBP. The bytes 4889E5
`03:58` 4889E5
`03:58` 4889E5 mean move RBP RSP. This is the bottom of
`04:03` mean move RBP RSP. This is the bottom of
`04:03` mean move RBP RSP. This is the bottom of the software stack. Technically, we're
`04:06` the software stack. Technically, we're
`04:06` the software stack. Technically, we're actually not done here. There's
`04:08` actually not done here. There's
`04:08` actually not done here. There's something deeper than even this. Those
`04:12` something deeper than even this. Those
`04:12` something deeper than even this. Those bytes all get decoded by the CPU in
`04:16` bytes all get decoded by the CPU in
`04:16` bytes all get decoded by the CPU in something called micro operations at the
`04:18` something called micro operations at the
`04:18` something called micro operations at the hardware level. A single MOV instruction
`04:23` hardware level. A single MOV instruction
`04:23` hardware level. A single MOV instruction triggers a whole cascade. You have to
`04:26` triggers a whole cascade. You have to
`04:26` triggers a whole cascade. You have to fetch the instructions from memory,
`04:29` fetch the instructions from memory,
`04:29` fetch the instructions from memory, decode the op code, calculate the
`04:32` decode the op code, calculate the
`04:32` decode the op code, calculate the effective address, read from the
`04:33` effective address, read from the
`04:33` effective address, read from the register file, write to memory, wait for
`04:35` register file, write to memory, wait for
`04:35` register file, write to memory, wait for the cache coherency, commit. And each of
`04:37` the cache coherency, commit. And each of
`04:37` the cache coherency, commit. And each of these involves transistors switching
`04:39` these involves transistors switching
`04:39` these involves transistors switching states. Billions of transistors. And
`04:41` states. Billions of transistors. And
`04:42` states. Billions of transistors. And each transistor works by controlling the
`04:44` each transistor works by controlling the
`04:44` each transistor works by controlling the flow of electrons. Here's where things
`04:47` flow of electrons. Here's where things
`04:47` flow of electrons. Here's where things get philosophically interesting, or at
`04:49` get philosophically interesting, or at
`04:49` get philosophically interesting, or at least in my opinion, they do. And before
`04:53` least in my opinion, they do. And before
`04:53` least in my opinion, they do. And before we go deeper, I kind of want to go
`04:55` we go deeper, I kind of want to go
`04:55` we go deeper, I kind of want to go backward actually uh back in time to
`04:59` backward actually uh back in time to
`04:59` backward actually uh back in time to 1804
`05:01` 1804
`05:01` 1804 when we look into the kind of beginning
`05:03` when we look into the kind of beginning
`05:03` when we look into the kind of beginning stages of algorithms. We find ourselves
`05:06` stages of algorithms. We find ourselves
`05:06` stages of algorithms. We find ourselves in France, specifically a place in
`05:09` in France, specifically a place in
`05:09` in France, specifically a place in France where a man by the name Joseph
`05:12` France where a man by the name Joseph
`05:12` France where a man by the name Joseph Marie Jakard was living in Leyon. He was
`05:16` Marie Jakard was living in Leyon. He was
`05:16` Marie Jakard was living in Leyon. He was a French weaver and he invented
`05:18` a French weaver and he invented
`05:18` a French weaver and he invented something remarkable. It was a loom that
`05:20` something remarkable. It was a loom that
`05:20` something remarkable. It was a loom that could use punch carts to control which
`05:23` could use punch carts to control which
`05:23` could use punch carts to control which threads were raised and lowered, hole or
`05:26` threads were raised and lowered, hole or
`05:26` threads were raised and lowered, hole or no hole, up or down. Binary logic.
`05:31` no hole, up or down. Binary logic.
`05:31` no hole, up or down. Binary logic. Before Jakard, creating patterned fabric
`05:33` Before Jakard, creating patterned fabric
`05:33` Before Jakard, creating patterned fabric required a skilled weaver, an assistant
`05:36` required a skilled weaver, an assistant
`05:36` required a skilled weaver, an assistant called a draw boy, who manually raised
`05:39` called a draw boy, who manually raised
`05:39` called a draw boy, who manually raised threads according to the pattern. It was
`05:42` threads according to the pattern. It was
`05:42` threads according to the pattern. It was slow, expensive, and honestly limited in
`05:45` slow, expensive, and honestly limited in
`05:45` slow, expensive, and honestly limited in complexity. With punched cards, an
`05:48` complexity. With punched cards, an
`05:48` complexity. With punched cards, an unskilled worker could produce intricate
`05:50` unskilled worker could produce intricate
`05:50` unskilled worker could produce intricate patterns automatically. The same loom
`05:53` patterns automatically. The same loom
`05:53` patterns automatically. The same loom could produce unlimited designs just by
`05:56` could produce unlimited designs just by
`05:56` could produce unlimited designs just by changing cards. In 1839, someone used a
`06:00` changing cards. In 1839, someone used a
`06:00` changing cards. In 1839, someone used a jakard loom to weave a silk portrait of
`06:03` jakard loom to weave a silk portrait of
`06:03` jakard loom to weave a silk portrait of Jakard himself. It required 24,000
`06:06` Jakard himself. It required 24,000
`06:06` Jakard himself. It required 24,000 cards, and each card had over a thousand
`06:09` cards, and each card had over a thousand
`06:09` cards, and each card had over a thousand whole positions. Adah Love Lace, often
`06:12` whole positions. Adah Love Lace, often
`06:12` whole positions. Adah Love Lace, often called the first programmer, saw the
`06:14` called the first programmer, saw the
`06:14` called the first programmer, saw the connection immediately. She wrote that
`06:17` connection immediately. She wrote that
`06:17` connection immediately. She wrote that Charles Babage analytical engine,
`06:19` Charles Babage analytical engine,
`06:19` Charles Babage analytical engine, another pre-elect electrical era
`06:21` another pre-elect electrical era
`06:21` another pre-elect electrical era machine, weaves algebraic patterns just
`06:24` machine, weaves algebraic patterns just
`06:24` machine, weaves algebraic patterns just as the chicard lom weaves flowers and
`06:28` as the chicard lom weaves flowers and
`06:28` as the chicard lom weaves flowers and leaves. The punch card, hole or no hole,
`06:31` leaves. The punch card, hole or no hole,
`06:31` leaves. The punch card, hole or no hole, one or zero. This is where it all began.
`06:33` one or zero. This is where it all began.
`06:34` one or zero. This is where it all began. And here's the thing, those early looms
`06:35` And here's the thing, those early looms
`06:35` And here's the thing, those early looms had errors. Cards would tear, holes
`06:37` had errors. Cards would tear, holes
`06:37` had errors. Cards would tear, holes would be punched wrong, the silk would
`06:39` would be punched wrong, the silk would
`06:39` would be punched wrong, the silk would come out mangled. So they built systems
`06:41` come out mangled. So they built systems
`06:41` come out mangled. So they built systems to catch mistakes. They created
`06:43` to catch mistakes. They created
`06:43` to catch mistakes. They created standards for card sizes. They developed
`06:45` standards for card sizes. They developed
`06:45` standards for card sizes. They developed processes for verifying patterns before
`06:48` processes for verifying patterns before
`06:48` processes for verifying patterns before weaving. Error handling at the very
`06:51` weaving. Error handling at the very
`06:51` weaving. Error handling at the very foundation.
`06:52` foundation.
`06:52` foundation. And you see this is what brings us into
`06:54` And you see this is what brings us into
`06:54` And you see this is what brings us into the modern era. The reason I'm bringing
`06:57` the modern era. The reason I'm bringing
`06:57` the modern era. The reason I'm bringing into all this, every layer of our modern
`07:00` into all this, every layer of our modern
`07:00` into all this, every layer of our modern computing stack has the same story. In
`07:02` computing stack has the same story. In
`07:02` computing stack has the same story. In 1947,
`07:04` 1947,
`07:04` 1947, engineers at Harvard found a moth stuck
`07:07` engineers at Harvard found a moth stuck
`07:07` engineers at Harvard found a moth stuck in the relay of the Mark 2 computer.
`07:09` in the relay of the Mark 2 computer.
`07:09` in the relay of the Mark 2 computer. They taped it into the log book with one
`07:11` They taped it into the log book with one
`07:11` They taped it into the log book with one note. First actual case of bug being
`07:13` note. First actual case of bug being
`07:13` note. First actual case of bug being found. The term debugging stuck. In
`07:16` found. The term debugging stuck. In
`07:16` found. The term debugging stuck. In 1994, a professor named Thomas Nicely
`07:19` 1994, a professor named Thomas Nicely
`07:19` 1994, a professor named Thomas Nicely discovered that Intel's Pentium
`07:21` discovered that Intel's Pentium
`07:21` discovered that Intel's Pentium processor sometimes gave wrong answers
`07:23` processor sometimes gave wrong answers
`07:23` processor sometimes gave wrong answers for division. The cause, five entries
`07:25` for division. The cause, five entries
`07:25` for division. The cause, five entries were missing from a lookup table in the
`07:27` were missing from a lookup table in the
`07:27` were missing from a lookup table in the chip's floatingoint unit. Just five
`07:29` chip's floatingoint unit. Just five
`07:29` chip's floatingoint unit. Just five values out of over a thousand. Intel had
`07:32` values out of over a thousand. Intel had
`07:32` values out of over a thousand. Intel had to recall processors. It cost them 475
`07:36` to recall processors. It cost them 475
`07:36` to recall processors. It cost them 475 million. At every layer, from punch card
`07:39` million. At every layer, from punch card
`07:39` million. At every layer, from punch card to silicon, humans have made mistakes.
`07:43` to silicon, humans have made mistakes.
`07:43` to silicon, humans have made mistakes. And at every layer, we've built systems
`07:44` And at every layer, we've built systems
`07:44` And at every layer, we've built systems to catch them, correct them, work around
`07:47` to catch them, correct them, work around
`07:47` to catch them, correct them, work around them. This is engineering. This is what
`07:49` them. This is engineering. This is what
`07:49` them. This is engineering. This is what we do. But let's go back to the
`07:51` we do. But let's go back to the
`07:51` we do. But let's go back to the beginning. Remember when I said
`07:53` beginning. Remember when I said
`07:53` beginning. Remember when I said electrons are probabilistic and then
`07:54` electrons are probabilistic and then
`07:54` electrons are probabilistic and then that was important. Here's something
`07:57` that was important. Here's something
`07:57` that was important. Here's something most people don't know. Your computer
`08:00` most people don't know. Your computer
`08:00` most people don't know. Your computer experiences random bit flips. Not from
`08:03` experiences random bit flips. Not from
`08:03` experiences random bit flips. Not from software bugs, but from cosmic rays.
`08:06` software bugs, but from cosmic rays.
`08:06` software bugs, but from cosmic rays. High energy particles from space collide
`08:09` High energy particles from space collide
`08:09` High energy particles from space collide with atoms in the atmosphere, creating
`08:11` with atoms in the atmosphere, creating
`08:11` with atoms in the atmosphere, creating showers of secondary particles. Some of
`08:14` showers of secondary particles. Some of
`08:14` showers of secondary particles. Some of those particles hit your RAM. When they
`08:16` those particles hit your RAM. When they
`08:16` those particles hit your RAM. When they do, they can flip a bit. A zero becomes
`08:18` do, they can flip a bit. A zero becomes
`08:18` do, they can flip a bit. A zero becomes a one. A one becomes a zero. In 2003, an
`08:23` a one. A one becomes a zero. In 2003, an
`08:23` a one. A one becomes a zero. In 2003, an electron in Sharik, Belgium, gave one
`08:26` electron in Sharik, Belgium, gave one
`08:26` electron in Sharik, Belgium, gave one candidate exactly 4,96
`08:29` candidate exactly 4,96
`08:29` candidate exactly 4,96 extra votes. That's 2 to the 12th power.
`08:33` extra votes. That's 2 to the 12th power.
`08:33` extra votes. That's 2 to the 12th power. A perfect power of two. The difference
`08:36` A perfect power of two. The difference
`08:36` A perfect power of two. The difference of exactly one flipped bit. A cosmic ray
`08:40` of exactly one flipped bit. A cosmic ray
`08:40` of exactly one flipped bit. A cosmic ray had altered the vote count. In 2013, a
`08:44` had altered the vote count. In 2013, a
`08:44` had altered the vote count. In 2013, a speedrunner playing Super Mario 64
`08:47` speedrunner playing Super Mario 64
`08:47` speedrunner playing Super Mario 64 watched Mario suddenly teleport through
`08:50` watched Mario suddenly teleport through
`08:50` watched Mario suddenly teleport through the floor. analysis showed a single bit
`08:53` the floor. analysis showed a single bit
`08:53` the floor. analysis showed a single bit had flipped at memory address 05837800,
`09:01` changing Mario's vertical position, a
`09:01` changing Mario's vertical position, a cosmic ray in the middle of a video
`09:03` cosmic ray in the middle of a video
`09:03` cosmic ray in the middle of a video game. IBM estimated in 1996 that a
`09:07` game. IBM estimated in 1996 that a
`09:07` game. IBM estimated in 1996 that a desktop computer with 256 MGB of RAM
`09:10` desktop computer with 256 MGB of RAM
`09:10` desktop computer with 256 MGB of RAM would experience about one cosmic ray
`09:13` would experience about one cosmic ray
`09:13` would experience about one cosmic ray bit flip per month. And now we reach the
`09:17` bit flip per month. And now we reach the
`09:17` bit flip per month. And now we reach the real foundation. Electrons are not
`09:19` real foundation. Electrons are not
`09:19` real foundation. Electrons are not little balls orbiting a nucleus. In
`09:23` little balls orbiting a nucleus. In
`09:23` little balls orbiting a nucleus. In fact, they're probability clouds, wave
`09:25` fact, they're probability clouds, wave
`09:25` fact, they're probability clouds, wave functions. You can never know exactly
`09:27` functions. You can never know exactly
`09:27` functions. You can never know exactly where an electron is. You can only know
`09:29` where an electron is. You can only know
`09:29` where an electron is. You can only know the probability of finding it in a
`09:31` the probability of finding it in a
`09:31` the probability of finding it in a particular location. This isn't
`09:34` particular location. This isn't
`09:34` particular location. This isn't uncertainty due to our instruments being
`09:36` uncertainty due to our instruments being
`09:36` uncertainty due to our instruments being imprecise. This is fundamental to
`09:38` imprecise. This is fundamental to
`09:38` imprecise. This is fundamental to reality. The electron generally does not
`09:41` reality. The electron generally does not
`09:41` reality. The electron generally does not have a definite position until measured.
`09:44` have a definite position until measured.
`09:44` have a definite position until measured. Transistors work by controlling the flow
`09:47` Transistors work by controlling the flow
`09:47` Transistors work by controlling the flow of these probabilistic particles. When
`09:50` of these probabilistic particles. When
`09:50` of these probabilistic particles. When you shrink transistors small enough,
`09:51` you shrink transistors small enough,
`09:52` you shrink transistors small enough, quantum tunneling becomes a problem.
`09:54` quantum tunneling becomes a problem.
`09:54` quantum tunneling becomes a problem. Electrons can tunnel through barriers
`09:56` Electrons can tunnel through barriers
`09:56` Electrons can tunnel through barriers they shouldn't be able to cross purely
`09:58` they shouldn't be able to cross purely
`09:58` they shouldn't be able to cross purely due to their wavelike nature. The entire
`10:01` due to their wavelike nature. The entire
`10:01` due to their wavelike nature. The entire deterministic computing stack,
`10:03` deterministic computing stack,
`10:03` deterministic computing stack, everything from your Python code down to
`10:05` everything from your Python code down to
`10:05` everything from your Python code down to the machine instructions, is built on
`10:08` the machine instructions, is built on
`10:08` the machine instructions, is built on particles that are fundamentally
`10:11` particles that are fundamentally
`10:11` particles that are fundamentally irreducibly probabilistic.
`10:14` irreducibly probabilistic.
`10:14` irreducibly probabilistic. So how does it work then? How do we make
`10:17` So how does it work then? How do we make
`10:17` So how does it work then? How do we make these things work so deterministically?
`10:19` these things work so deterministically?
`10:19` these things work so deterministically? We engineered our way around it.
`10:21` We engineered our way around it.
`10:22` We engineered our way around it. Transistors are designed with tolerances
`10:24` Transistors are designed with tolerances
`10:24` Transistors are designed with tolerances and we use enough electrons that the
`10:25` and we use enough electrons that the
`10:26` and we use enough electrons that the statistical behavior becomes
`10:27` statistical behavior becomes
`10:27` statistical behavior becomes predictable. We build error correcting
`10:29` predictable. We build error correcting
`10:29` predictable. We build error correcting memory. We implement check sums and
`10:31` memory. We implement check sums and
`10:31` memory. We implement check sums and parody bits and we create redundancy.
`10:35` parody bits and we create redundancy.
`10:35` parody bits and we create redundancy. When a cosmic ray flips a bit in server
`10:37` When a cosmic ray flips a bit in server
`10:38` When a cosmic ray flips a bit in server RAM, ECC memory ces it and fixes it. You
`10:41` RAM, ECC memory ces it and fixes it. You
`10:41` RAM, ECC memory ces it and fixes it. You never know it happened. The entire
`10:43` never know it happened. The entire
`10:43` never know it happened. The entire history of computing is the history of
`10:45` history of computing is the history of
`10:45` history of computing is the history of taking something unreliable and making
`10:47` taking something unreliable and making
`10:47` taking something unreliable and making it reliable through architecture,
`10:49` it reliable through architecture,
`10:49` it reliable through architecture, through redundancy, through error
`10:51` through redundancy, through error
`10:51` through redundancy, through error handling, hole or no hole in a punch
`10:53` handling, hole or no hole in a punch
`10:53` handling, hole or no hole in a punch card, moth in a relay, missing entries
`10:56` card, moth in a relay, missing entries
`10:56` card, moth in a relay, missing entries in lookup tables, cosmic rays flipping
`10:59` in lookup tables, cosmic rays flipping
`10:59` in lookup tables, cosmic rays flipping bits, electrons tunneling through
`11:00` bits, electrons tunneling through
`11:00` bits, electrons tunneling through barriers, every layer uncertainty has
`11:04` barriers, every layer uncertainty has
`11:04` barriers, every layer uncertainty has engineering, engineering, engineering.
`11:08` engineering, engineering, engineering.
`11:08` engineering, engineering, engineering. Which brings us back to where we
`11:10` Which brings us back to where we
`11:10` Which brings us back to where we started. I typed write hello world in
`11:13` started. I typed write hello world in
`11:13` started. I typed write hello world in Python into AI and it gave me code.
`11:16` Python into AI and it gave me code.
`11:16` Python into AI and it gave me code. People say AI is different. They say
`11:18` People say AI is different. They say
`11:18` People say AI is different. They say it's probabilistic, not deterministic.
`11:19` it's probabilistic, not deterministic.
`11:20` it's probabilistic, not deterministic. They say you can't trust it because it
`11:21` They say you can't trust it because it
`11:21` They say you can't trust it because it might give different answers to the same
`11:22` might give different answers to the same
`11:22` might give different answers to the same question. But think about what we just
`11:25` question. But think about what we just
`11:25` question. But think about what we just walked through. The punch card loom was
`11:27` walked through. The punch card loom was
`11:27` walked through. The punch card loom was deterministic, but the cards tore and
`11:29` deterministic, but the cards tore and
`11:29` deterministic, but the cards tore and the holes were punched wrong. Early
`11:30` the holes were punched wrong. Early
`11:30` the holes were punched wrong. Early computers were deterministic, but Moss
`11:32` computers were deterministic, but Moss
`11:32` computers were deterministic, but Moss got stuck in relays. The Pentium was
`11:34` got stuck in relays. The Pentium was
`11:34` got stuck in relays. The Pentium was deterministic, but someone forgot five
`11:36` deterministic, but someone forgot five
`11:36` deterministic, but someone forgot five entries in a table. Your RAM is
`11:38` entries in a table. Your RAM is
`11:38` entries in a table. Your RAM is deterministic, but cosmic rays flip bits
`11:41` deterministic, but cosmic rays flip bits
`11:41` deterministic, but cosmic rays flip bits anyway. Electrons are fundamentally
`11:43` anyway. Electrons are fundamentally
`11:43` anyway. Electrons are fundamentally probabilistic. Yet, we engineered our
`11:46` probabilistic. Yet, we engineered our
`11:46` probabilistic. Yet, we engineered our way around that, too. Every layer
`11:48` way around that, too. Every layer
`11:48` way around that, too. Every layer started with unreliability. Every layer
`11:52` started with unreliability. Every layer
`11:52` started with unreliability. Every layer becomes reliable through architecture.
`11:55` becomes reliable through architecture.
`11:55` becomes reliable through architecture. AI is no different. It's just the new
`11:58` AI is no different. It's just the new
`11:58` AI is no different. It's just the new layer. Right now, we're in the era of
`12:01` layer. Right now, we're in the era of
`12:01` layer. Right now, we're in the era of moths in relays. We're finding the
`12:03` moths in relays. We're finding the
`12:03` moths in relays. We're finding the errors. We're tapping them into log
`12:05` errors. We're tapping them into log
`12:05` errors. We're tapping them into log books. We're building systems to catch
`12:07` books. We're building systems to catch
`12:07` books. We're building systems to catch mistakes and verify outputs or just
`12:09` mistakes and verify outputs or just
`12:09` mistakes and verify outputs or just create redundancy. The criticism that AI
`12:11` create redundancy. The criticism that AI
`12:11` create redundancy. The criticism that AI is merely probabilistic misses the point
`12:13` is merely probabilistic misses the point
`12:13` is merely probabilistic misses the point entirely. The critics aren't thinking
`12:15` entirely. The critics aren't thinking
`12:15` entirely. The critics aren't thinking about the full stack. They're not seeing
`12:17` about the full stack. They're not seeing
`12:17` about the full stack. They're not seeing that everything beneath their feet is
`12:18` that everything beneath their feet is
`12:18` that everything beneath their feet is probabistic, too. We just did the
`12:21` probabistic, too. We just did the
`12:21` probabistic, too. We just did the engineering work already. When you type
`12:23` engineering work already. When you type
`12:23` engineering work already. When you type print hello, you're not just running one
`12:25` print hello, you're not just running one
`12:26` print hello, you're not just running one line of code. You're invoking decades of
`12:28` line of code. You're invoking decades of
`12:28` line of code. You're invoking decades of accumulated engineering. Thousands of
`12:31` accumulated engineering. Thousands of
`12:31` accumulated engineering. Thousands of people who solved thousands of problems.
`12:34` people who solved thousands of problems.
`12:34` people who solved thousands of problems. error handlers built on error handlers
`12:36` error handlers built on error handlers
`12:36` error handlers built on error handlers all the way down to the quantum phone.
`12:39` all the way down to the quantum phone.
`12:39` all the way down to the quantum phone. Lovely saw it. The loom weaves the
`12:41` Lovely saw it. The loom weaves the
`12:41` Lovely saw it. The loom weaves the patterns. The engine weaves the algebra.
`12:43` patterns. The engine weaves the algebra.
`12:43` patterns. The engine weaves the algebra. The computer weaves the logic. And now
`12:46` The computer weaves the logic. And now
`12:46` The computer weaves the logic. And now AI weaves the language. Same pattern,
`12:50` AI weaves the language. Same pattern,
`12:50` AI weaves the language. Same pattern, different layer. The only question is
`12:53` different layer. The only question is
`12:53` different layer. The only question is how long it takes us to build the
`12:55` how long it takes us to build the
`12:56` how long it takes us to build the architecture that makes it reliable. And
`12:58` architecture that makes it reliable. And
`12:58` architecture that makes it reliable. And based on history, I'm pretty sure we're
`13:00` based on history, I'm pretty sure we're
`13:00` based on history, I'm pretty sure we're going to figure it out. I mean, we
`13:02` going to figure it out. I mean, we
`13:02` going to figure it out. I mean, we always do.
`13:04` always do.
`13:04` always do. But that brings us all the way back to
`13:06` But that brings us all the way back to
`13:06` But that brings us all the way back to the beginning. That one line of Python,
`13:10` the beginning. That one line of Python,
`13:10` the beginning. That one line of Python, 22 characters built on the shoulders of
`13:13` 22 characters built on the shoulders of
`13:13` 22 characters built on the shoulders of every engineer who ever taped a moth
`13:15` every engineer who ever taped a moth
`13:15` every engineer who ever taped a moth into a log book. Stay curious, my
`13:18` into a log book. Stay curious, my
`13:18` into a log book. Stay curious, my friends, and until next time, goodbye.