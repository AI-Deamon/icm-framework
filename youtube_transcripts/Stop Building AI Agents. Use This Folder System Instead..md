# Stop Building AI Agents. Use This Folder System Instead.

**Channel:** Jake Van Clief  
**Uploaded:** 2026-03-10  
**Duration:** 23:18  
**URL:** [https://www.youtube.com/watch?v=MkN-ss2Nl10](https://www.youtube.com/watch?v=MkN-ss2Nl10)  

---

## Transcript

`00:01` Hi everyone. In this video, we're going
`00:01` Hi everyone. In this video, we're going to dive into my concepts around folder
`00:04` to dive into my concepts around folder
`00:04` to dive into my concepts around folder as a workspace and architecture. What it
`00:07` as a workspace and architecture. What it
`00:07` as a workspace and architecture. What it means to use AI in a way that will
`00:09` means to use AI in a way that will
`00:09` means to use AI in a way that will actually probably last the next decade
`00:12` actually probably last the next decade
`00:12` actually probably last the next decade and what I think the industry is
`00:13` and what I think the industry is
`00:13` and what I think the industry is actually moving towards.
`00:15` actually moving towards.
`00:15` actually moving towards. Now, if you've seen any of my other
`00:17` Now, if you've seen any of my other
`00:17` Now, if you've seen any of my other videos, I'm sure you've seen screenshots
`00:19` videos, I'm sure you've seen screenshots
`00:19` videos, I'm sure you've seen screenshots or snippets of crazy folder structure
`00:21` or snippets of crazy folder structure
`00:21` or snippets of crazy folder structure I'm doing where I'm routing Claude to
`00:23` I'm doing where I'm routing Claude to
`00:23` I'm doing where I'm routing Claude to different folders, my markdown files,
`00:25` different folders, my markdown files,
`00:25` different folders, my markdown files, using skills at certain times, creating
`00:28` using skills at certain times, creating
`00:28` using skills at certain times, creating animations or code with it. I have all
`00:30` animations or code with it. I have all
`00:30` animations or code with it. I have all sorts of different ways I'm doing it,
`00:32` sorts of different ways I'm doing it,
`00:32` sorts of different ways I'm doing it, but I don't think I have a video out
`00:34` but I don't think I have a video out
`00:34` but I don't think I have a video out there that really dives into how I
`00:36` there that really dives into how I
`00:36` there that really dives into how I structure it and teaching you to do
`00:38` structure it and teaching you to do
`00:38` structure it and teaching you to do that. And I decided to go ahead and
`00:41` that. And I decided to go ahead and
`00:41` that. And I decided to go ahead and create a kind of template folder to walk
`00:43` create a kind of template folder to walk
`00:43` create a kind of template folder to walk you through all of this. This is
`00:45` you through all of this. This is
`00:45` you through all of this. This is something you could use to be able to
`00:47` something you could use to be able to
`00:47` something you could use to be able to apply to any of your workflows, build
`00:50` apply to any of your workflows, build
`00:50` apply to any of your workflows, build through it, understand it, and kind of
`00:51` through it, understand it, and kind of
`00:51` through it, understand it, and kind of explore, you know, building your own
`00:54` explore, you know, building your own
`00:54` explore, you know, building your own version of this. Now, throughout this
`00:56` version of this. Now, throughout this
`00:56` version of this. Now, throughout this video, I'm actually going to teach some
`00:58` video, I'm actually going to teach some
`00:58` video, I'm actually going to teach some concepts along the way for people who
`01:00` concepts along the way for people who
`01:00` concepts along the way for people who are not familiar with maybe VS Code,
`01:02` are not familiar with maybe VS Code,
`01:02` are not familiar with maybe VS Code, which is the workspace I'm working in.
`01:04` which is the workspace I'm working in.
`01:04` which is the workspace I'm working in. Don't worry, you don't need VS Code to
`01:05` Don't worry, you don't need VS Code to
`01:05` Don't worry, you don't need VS Code to do the things I'm showing you. You can
`01:07` do the things I'm showing you. You can
`01:07` do the things I'm showing you. You can do it within Claude, but I just want to
`01:09` do it within Claude, but I just want to
`01:09` do it within Claude, but I just want to describe like what markdown is, what it
`01:12` describe like what markdown is, what it
`01:12` describe like what markdown is, what it means to have an IDE, all of these
`01:14` means to have an IDE, all of these
`01:14` means to have an IDE, all of these things. And if you are familiar with
`01:15` things. And if you are familiar with
`01:15` things. And if you are familiar with these, you're software engineer, you
`01:16` these, you're software engineer, you
`01:16` these, you're software engineer, you probably are, don't worry, I'm still
`01:18` probably are, don't worry, I'm still
`01:18` probably are, don't worry, I'm still going to be diving into the specifics
`01:20` going to be diving into the specifics
`01:20` going to be diving into the specifics and I think you're going to get a lot of
`01:21` and I think you're going to get a lot of
`01:21` and I think you're going to get a lot of out of this either way. However,
`01:23` out of this either way. However,
`01:23` out of this either way. However, sometimes it's also nice to just dive
`01:25` sometimes it's also nice to just dive
`01:25` sometimes it's also nice to just dive back into the fundamentals. So, let me
`01:27` back into the fundamentals. So, let me
`01:27` back into the fundamentals. So, let me paint a little scene for you. Right now,
`01:29` paint a little scene for you. Right now,
`01:29` paint a little scene for you. Right now, most people, if they are even I which
`01:31` most people, if they are even I which
`01:31` most people, if they are even I which fun fact about 84% of the nation is
`01:33` fun fact about 84% of the nation is
`01:33` fun fact about 84% of the nation is still not fully using it, but log in and
`01:36` still not fully using it, but log in and
`01:36` still not fully using it, but log in and use Claude or ChatGPT or Gemini and
`01:38` use Claude or ChatGPT or Gemini and
`01:38` use Claude or ChatGPT or Gemini and they're typing things. They're diving
`01:40` they're typing things. They're diving
`01:40` they're typing things. They're diving in.
`01:41` in.
`01:41` in. Um, maybe they get something back, they
`01:43` Um, maybe they get something back, they
`01:43` Um, maybe they get something back, they start another conversation, start over,
`01:46` start another conversation, start over,
`01:46` start another conversation, start over, and sometimes they're able to share
`01:47` and sometimes they're able to share
`01:47` and sometimes they're able to share context between conversations, right?
`01:49` context between conversations, right?
`01:49` context between conversations, right? Like ChatGPT and Claude can do that. I
`01:51` Like ChatGPT and Claude can do that. I
`01:51` Like ChatGPT and Claude can do that. I can say, you know, tell me a software
`01:53` can say, you know, tell me a software
`01:53` can say, you know, tell me a software stack for Vigilore, which is a software
`01:55` stack for Vigilore, which is a software
`01:55` stack for Vigilore, which is a software that I was working on for another
`01:56` that I was working on for another
`01:57` that I was working on for another company, and it's able to go and look
`01:59` company, and it's able to go and look
`01:59` company, and it's able to go and look through our older conversations, which
`02:00` through our older conversations, which
`02:00` through our older conversations, which is nice. That's a little bit of extra
`02:02` is nice. That's a little bit of extra
`02:02` is nice. That's a little bit of extra there, but it's still not, you know,
`02:04` there, but it's still not, you know,
`02:04` there, but it's still not, you know, it's not able to look at files, have
`02:06` it's not able to look at files, have
`02:06` it's not able to look at files, have persistence, things like that. And
`02:08` persistence, things like that. And
`02:08` persistence, things like that. And you're constantly having to make these
`02:09` you're constantly having to make these
`02:10` you're constantly having to make these huge prompts. Maybe you have some sort
`02:11` huge prompts. Maybe you have some sort
`02:11` huge prompts. Maybe you have some sort of prompts that you save and throw in or
`02:13` of prompts that you save and throw in or
`02:13` of prompts that you save and throw in or documents. And you're throwing it in,
`02:16` documents. And you're throwing it in,
`02:16` documents. And you're throwing it in, and then you have to start a new
`02:17` and then you have to start a new
`02:17` and then you have to start a new conversation. Throw it in, start a new
`02:19` conversation. Throw it in, start a new
`02:19` conversation. Throw it in, start a new conversation. You hit a wall, there's
`02:20` conversation. You hit a wall, there's
`02:20` conversation. You hit a wall, there's too many tokens, right? All sorts of
`02:22` too many tokens, right? All sorts of
`02:22` too many tokens, right? All sorts of problems there. And don't get me wrong,
`02:24` problems there. And don't get me wrong,
`02:24` problems there. And don't get me wrong, there's some really good prompt
`02:26` there's some really good prompt
`02:26` there's some really good prompt engineering techniques out there, but at
`02:28` engineering techniques out there, but at
`02:28` engineering techniques out there, but at the end of the day, AI can only hold so
`02:30` the end of the day, AI can only hold so
`02:30` the end of the day, AI can only hold so much in a single information or chat
`02:33` much in a single information or chat
`02:33` much in a single information or chat area. And even further, that's not your
`02:35` area. And even further, that's not your
`02:35` area. And even further, that's not your workflow. Having to have it create a
`02:37` workflow. Having to have it create a
`02:37` workflow. Having to have it create a whole bunch of stuff and then re-edit it
`02:39` whole bunch of stuff and then re-edit it
`02:39` whole bunch of stuff and then re-edit it again, it's it's not sustainable, it's
`02:41` again, it's it's not sustainable, it's
`02:42` again, it's it's not sustainable, it's not scalable.
`02:43` not scalable.
`02:43` not scalable. Now, for those of you who don't
`02:44` Now, for those of you who don't
`02:44` Now, for those of you who don't understand why they struggle so much,
`02:47` understand why they struggle so much,
`02:47` understand why they struggle so much, essentially, AI reads everything, all of
`02:50` essentially, AI reads everything, all of
`02:50` essentially, AI reads everything, all of your sentence, and measures it by
`02:51` your sentence, and measures it by
`02:51` your sentence, and measures it by something called tokens. A token is
`02:54` something called tokens. A token is
`02:54` something called tokens. A token is roughly three quarters of a word or a
`02:57` roughly three quarters of a word or a
`02:57` roughly three quarters of a word or a single word sometimes. The word
`02:59` single word sometimes. The word
`02:59` single word sometimes. The word hamburger could be three tokens.
`03:01` hamburger could be three tokens.
`03:01` hamburger could be three tokens. Ham-bur-ger,
`03:02` Ham-bur-ger,
`03:02` Ham-bur-ger, hamburger. The term comes from NLP
`03:05` hamburger. The term comes from NLP
`03:05` hamburger. The term comes from NLP research in the '90s. A bunch of
`03:08` research in the '90s. A bunch of
`03:08` research in the '90s. A bunch of researchers needed a unit smaller than a
`03:10` researchers needed a unit smaller than a
`03:10` researchers needed a unit smaller than a word because language doesn't all break
`03:13` word because language doesn't all break
`03:13` word because language doesn't all break the same way, right? So, they borrowed
`03:15` the same way, right? So, they borrowed
`03:15` the same way, right? So, they borrowed token from linguistics, which borrowed
`03:17` token from linguistics, which borrowed
`03:17` token from linguistics, which borrowed it from Old English token, which means a
`03:20` it from Old English token, which means a
`03:20` it from Old English token, which means a sign or a symbol. A token is just the
`03:22` sign or a symbol. A token is just the
`03:22` sign or a symbol. A token is just the smallest meaningful chunk of a sentence
`03:25` smallest meaningful chunk of a sentence
`03:26` smallest meaningful chunk of a sentence or a word. There's only so much tokens
`03:28` or a word. There's only so much tokens
`03:28` or a word. There's only so much tokens an AI can have in its context window
`03:32` an AI can have in its context window
`03:32` an AI can have in its context window before it starts failing. When people
`03:34` before it starts failing. When people
`03:34` before it starts failing. When people say context window, they mean how many
`03:35` say context window, they mean how many
`03:36` say context window, they mean how many tokens the AI can see at once, and that
`03:38` tokens the AI can see at once, and that
`03:38` tokens the AI can see at once, and that window is in fact finite. So, if you
`03:40` window is in fact finite. So, if you
`03:40` window is in fact finite. So, if you dump everything into one file, an AI
`03:42` dump everything into one file, an AI
`03:42` dump everything into one file, an AI writing a blog post is also reading your
`03:44` writing a blog post is also reading your
`03:44` writing a blog post is also reading your video production notes. You're burning
`03:46` video production notes. You're burning
`03:46` video production notes. You're burning tokens on stuff that doesn't matter. So,
`03:49` tokens on stuff that doesn't matter. So,
`03:49` tokens on stuff that doesn't matter. So, instead of building one big file, you
`03:51` instead of building one big file, you
`03:51` instead of building one big file, you want to separate your thoughts, your
`03:52` want to separate your thoughts, your
`03:52` want to separate your thoughts, your ideas, your work into separate areas.
`03:55` ideas, your work into separate areas.
`03:55` ideas, your work into separate areas. This is something I created for all of
`03:57` This is something I created for all of
`03:57` This is something I created for all of us. It's called a workspace blueprint.
`03:59` us. It's called a workspace blueprint.
`03:59` us. It's called a workspace blueprint. Here, you have three workspaces. And
`04:01` Here, you have three workspaces. And
`04:01` Here, you have three workspaces. And again, this is an example. You don't
`04:02` again, this is an example. You don't
`04:02` again, this is an example. You don't always have to do this, but each one
`04:04` always have to do this, but each one
`04:04` always have to do this, but each one handles a different kind of work. One
`04:06` handles a different kind of work. One
`04:06` handles a different kind of work. One for the community, right? Maybe I have
`04:07` for the community, right? Maybe I have
`04:07` for the community, right? Maybe I have this one for working on content and docs
`04:10` this one for working on content and docs
`04:10` this one for working on content and docs in the community. Production, right?
`04:12` in the community. Production, right?
`04:12` in the community. Production, right? What am I building? What are scripts?
`04:13` What am I building? What are scripts?
`04:13` What am I building? What are scripts? Maybe I'm creating animations. Writing
`04:16` Maybe I'm creating animations. Writing
`04:16` Maybe I'm creating animations. Writing room. Maybe I need to have some sort of
`04:18` room. Maybe I need to have some sort of
`04:18` room. Maybe I need to have some sort of process of thinking or I have a client
`04:21` process of thinking or I have a client
`04:21` process of thinking or I have a client list or insert as many things as I have
`04:23` list or insert as many things as I have
`04:23` list or insert as many things as I have there. And we're going to dive deeper
`04:24` there. And we're going to dive deeper
`04:24` there. And we're going to dive deeper into it. This is a space that does the
`04:27` into it. This is a space that does the
`04:27` into it. This is a space that does the job well because you can circumnavigate
`04:31` job well because you can circumnavigate
`04:31` job well because you can circumnavigate an AI seeing everything and only direct
`04:33` an AI seeing everything and only direct
`04:33` an AI seeing everything and only direct it to what you want. Let me explain how
`04:35` it to what you want. Let me explain how
`04:35` it to what you want. Let me explain how that actually works, though. So, I'm
`04:37` that actually works, though. So, I'm
`04:37` that actually works, though. So, I'm going to show you inside of VS Code,
`04:39` going to show you inside of VS Code,
`04:39` going to show you inside of VS Code, which is an IDE, basically a developer
`04:42` which is an IDE, basically a developer
`04:42` which is an IDE, basically a developer environment that allows people to kind
`04:44` environment that allows people to kind
`04:44` environment that allows people to kind of look at folders in a different way.
`04:47` of look at folders in a different way.
`04:47` of look at folders in a different way. So, instead of having to click into the
`04:49` So, instead of having to click into the
`04:49` So, instead of having to click into the folders like you just saw here, I can
`04:51` folders like you just saw here, I can
`04:51` folders like you just saw here, I can just open the folders and see everything
`04:53` just open the folders and see everything
`04:53` just open the folders and see everything and open the files without having to
`04:55` and open the files without having to
`04:55` and open the files without having to double-click the files, right? So,
`04:57` double-click the files, right? So,
`04:57` double-click the files, right? So, instead of having to double-click this
`04:58` instead of having to double-click this
`04:58` instead of having to double-click this text document and opens another window,
`05:00` text document and opens another window,
`05:00` text document and opens another window, I can just bounce between them. It's
`05:02` I can just bounce between them. It's
`05:02` I can just bounce between them. It's much cleaner, much easier. Even if
`05:04` much cleaner, much easier. Even if
`05:04` much cleaner, much easier. Even if you're not into code, it looks
`05:05` you're not into code, it looks
`05:05` you're not into code, it looks overwhelming. I promise you all of this
`05:07` overwhelming. I promise you all of this
`05:07` overwhelming. I promise you all of this is just natural language. This literally
`05:09` is just natural language. This literally
`05:09` is just natural language. This literally reads like a document. So, this is a
`05:11` reads like a document. So, this is a
`05:11` reads like a document. So, this is a markdown file. If you haven't seen them
`05:12` markdown file. If you haven't seen them
`05:12` markdown file. If you haven't seen them before, markdown is just a text file
`05:15` before, markdown is just a text file
`05:15` before, markdown is just a text file with some lightweight formatting, right?
`05:17` with some lightweight formatting, right?
`05:17` with some lightweight formatting, right? You have dashes for bullets. You have
`05:20` You have dashes for bullets. You have
`05:20` You have dashes for bullets. You have hashtags or pound symbols if everyone
`05:23` hashtags or pound symbols if everyone
`05:23` hashtags or pound symbols if everyone else remembers when they were just
`05:24` else remembers when they were just
`05:24` else remembers when they were just called that for headers. Um you have all
`05:27` called that for headers. Um you have all
`05:27` called that for headers. Um you have all sorts of stuff like asterisks for
`05:29` sorts of stuff like asterisks for
`05:29` sorts of stuff like asterisks for bolding or doing things in that way. And
`05:31` bolding or doing things in that way. And
`05:31` bolding or doing things in that way. And there's a lot of programs that it can
`05:32` there's a lot of programs that it can
`05:32` there's a lot of programs that it can actually run this to look a certain way.
`05:35` actually run this to look a certain way.
`05:35` actually run this to look a certain way. In fact, your Claude does exactly that.
`05:38` In fact, your Claude does exactly that.
`05:38` In fact, your Claude does exactly that. If you look, when you're talking to an
`05:40` If you look, when you're talking to an
`05:40` If you look, when you're talking to an AI, it's writing in markdown already.
`05:42` AI, it's writing in markdown already.
`05:42` AI, it's writing in markdown already. These boldings, these lines, all of
`05:44` These boldings, these lines, all of
`05:44` These boldings, these lines, all of these things. Watch what happens when I
`05:46` these things. Watch what happens when I
`05:46` these things. Watch what happens when I copy this. All of that formatting
`05:49` copy this. All of that formatting
`05:49` copy this. All of that formatting disappears when I paste it into here,
`05:51` disappears when I paste it into here,
`05:51` disappears when I paste it into here, and it turns into markdown because
`05:53` and it turns into markdown because
`05:53` and it turns into markdown because that's how it's making it look like
`05:55` that's how it's making it look like
`05:55` that's how it's making it look like that. Markdown is just a good way to
`05:57` that. Markdown is just a good way to
`05:57` that. Markdown is just a good way to format text. If you're curious, there's
`05:59` format text. If you're curious, there's
`05:59` format text. If you're curious, there's a man named John Gruber. He actually
`06:01` a man named John Gruber. He actually
`06:01` a man named John Gruber. He actually created this in 2004. The whole idea was
`06:04` created this in 2004. The whole idea was
`06:04` created this in 2004. The whole idea was write something that's readable as plain
`06:06` write something that's readable as plain
`06:06` write something that's readable as plain text, but can also render into a
`06:09` text, but can also render into a
`06:09` text, but can also render into a formatted document. He named it markdown
`06:13` formatted document. He named it markdown
`06:13` formatted document. He named it markdown as a play on markup language, which is
`06:16` as a play on markup language, which is
`06:16` as a play on markup language, which is the same stuff that HTML, right? The
`06:18` the same stuff that HTML, right? The
`06:18` the same stuff that HTML, right? The stuff that builds websites, hypertext
`06:21` stuff that builds websites, hypertext
`06:21` stuff that builds websites, hypertext markdown language. And all it does is
`06:22` markdown language. And all it does is
`06:22` markdown language. And all it does is mark stuff down with tags. Markdown
`06:25` mark stuff down with tags. Markdown
`06:25` mark stuff down with tags. Markdown strips all the tags and absurdity away
`06:27` strips all the tags and absurdity away
`06:27` strips all the tags and absurdity away and makes it look like something simple
`06:30` and makes it look like something simple
`06:30` and makes it look like something simple like this. But again, you're probably
`06:32` like this. But again, you're probably
`06:32` like this. But again, you're probably not here for this. You're here for the
`06:33` not here for this. You're here for the
`06:33` not here for this. You're here for the file system. So, let's move on to that
`06:35` file system. So, let's move on to that
`06:35` file system. So, let's move on to that next step. So, in this specific folder,
`06:37` next step. So, in this specific folder,
`06:38` next step. So, in this specific folder, which is an example, it runs on
`06:40` which is an example, it runs on
`06:40` which is an example, it runs on essentially three layers, and there's a
`06:43` essentially three layers, and there's a
`06:43` essentially three layers, and there's a reason for each one. If you look at my
`06:45` reason for each one. If you look at my
`06:45` reason for each one. If you look at my AGENTS.md,
`06:47` AGENTS.md,
`06:47` AGENTS.md, my Claude markdown file, this is
`06:48` my Claude markdown file, this is
`06:49` my Claude markdown file, this is something that my AI will read every
`06:51` something that my AI will read every
`06:51` something that my AI will read every time it's in any one of these folders.
`06:53` time it's in any one of these folders.
`06:53` time it's in any one of these folders. So, this is something that the AI will
`06:55` So, this is something that the AI will
`06:55` So, this is something that the AI will always have and always read. So, imagine
`06:57` always have and always read. So, imagine
`06:57` always have and always read. So, imagine it's you're just copying and pasting
`06:59` it's you're just copying and pasting
`06:59` it's you're just copying and pasting this into Claude code or into Claude
`07:02` this into Claude code or into Claude
`07:03` this into Claude code or into Claude every time you open it. Now, you can
`07:04` every time you open it. Now, you can
`07:04` every time you open it. Now, you can actually just type in to Claude read the
`07:07` actually just type in to Claude read the
`07:07` actually just type in to Claude read the AGENTS.md. In this case, it's Claude
`07:09` AGENTS.md. In this case, it's Claude
`07:09` AGENTS.md. In this case, it's Claude code. You could be working inside of
`07:11` code. You could be working inside of
`07:11` code. You could be working inside of Claude co-work as well, which is again a
`07:14` Claude co-work as well, which is again a
`07:14` Claude co-work as well, which is again a video I have on how to install, and it
`07:16` video I have on how to install, and it
`07:16` video I have on how to install, and it can operate inside of folders in case
`07:18` can operate inside of folders in case
`07:18` can operate inside of folders in case the VS code is too much for you. Um but
`07:21` the VS code is too much for you. Um but
`07:21` the VS code is too much for you. Um but just read the AGENTS.md and tell me what
`07:23` just read the AGENTS.md and tell me what
`07:23` just read the AGENTS.md and tell me what this is. Before you had to copy and
`07:25` this is. Before you had to copy and
`07:25` this is. Before you had to copy and paste, do all these things. It had to
`07:26` paste, do all these things. It had to
`07:26` paste, do all these things. It had to read the every file that's in here. In
`07:29` read the every file that's in here. In
`07:29` read the every file that's in here. In this case, it reads the AGENTS.md and
`07:32` this case, it reads the AGENTS.md and
`07:32` this case, it reads the AGENTS.md and immediately, without having to read
`07:33` immediately, without having to read
`07:33` immediately, without having to read everything else, understands the
`07:35` everything else, understands the
`07:35` everything else, understands the product, the process, what's going on,
`07:37` product, the process, what's going on,
`07:38` product, the process, what's going on, my writing room, my production, my
`07:39` my writing room, my production, my
`07:39` my writing room, my production, my community. It knows where to find it,
`07:41` community. It knows where to find it,
`07:41` community. It knows where to find it, what the file names are. All from just a
`07:43` what the file names are. All from just a
`07:43` what the file names are. All from just a single text prompt that allows it to
`07:46` single text prompt that allows it to
`07:46` single text prompt that allows it to understand where to go, what to do, what
`07:49` understand where to go, what to do, what
`07:49` understand where to go, what to do, what are these areas. But, let me describe
`07:51` are these areas. But, let me describe
`07:51` are these areas. But, let me describe this a little simpler for those of you
`07:53` this a little simpler for those of you
`07:53` this a little simpler for those of you who might, you know, feel like this is a
`07:55` who might, you know, feel like this is a
`07:55` who might, you know, feel like this is a bit overwhelming. Layer one in this is
`07:58` bit overwhelming. Layer one in this is
`07:58` bit overwhelming. Layer one in this is the map. This is what loads
`08:00` the map. This is what loads
`08:00` the map. This is what loads automatically, right? It's looking at
`08:02` automatically, right? It's looking at
`08:02` automatically, right? It's looking at it. So, you put the stuff the agent
`08:05` it. So, you put the stuff the agent
`08:05` it. So, you put the stuff the agent always needs to think about, folder
`08:07` always needs to think about, folder
`08:07` always needs to think about, folder structure, naming conventions, where
`08:09` structure, naming conventions, where
`08:09` structure, naming conventions, where files go. Think of this as the floor
`08:12` files go. Think of this as the floor
`08:12` files go. Think of this as the floor plan. You walk into any room, the floor
`08:15` plan. You walk into any room, the floor
`08:15` plan. You walk into any room, the floor plan is on the wall, and the agent knows
`08:17` plan is on the wall, and the agent knows
`08:17` plan is on the wall, and the agent knows where to go. Now, layer two is where the
`08:21` where to go. Now, layer two is where the
`08:21` where to go. Now, layer two is where the floor plan tells you to go. It's the
`08:23` floor plan tells you to go. It's the
`08:23` floor plan tells you to go. It's the actual rooms. What is your task? Go
`08:27` actual rooms. What is your task? Go
`08:27` actual rooms. What is your task? Go here. I want to write a blog post, well,
`08:30` here. I want to write a blog post, well,
`08:30` here. I want to write a blog post, well, then you need to go to here and read
`08:32` then you need to go to here and read
`08:32` then you need to go to here and read this context or this markdown file. If
`08:35` this context or this markdown file. If
`08:35` this context or this markdown file. If you want to build a demo or a video, you
`08:37` you want to build a demo or a video, you
`08:37` you want to build a demo or a video, you need to go here and read this context or
`08:40` need to go here and read this context or
`08:40` need to go here and read this context or markdown file. And this could be one
`08:42` markdown file. And this could be one
`08:42` markdown file. And this could be one that you wrote by hand, or it could be
`08:44` that you wrote by hand, or it could be
`08:44` that you wrote by hand, or it could be one that you told Claude to wrote. And
`08:46` one that you told Claude to wrote. And
`08:46` one that you told Claude to wrote. And we're going to dive into that here
`08:47` we're going to dive into that here
`08:47` we're going to dive into that here shortly. Layer three is the actual
`08:50` shortly. Layer three is the actual
`08:50` shortly. Layer three is the actual workspace itself. Where do you want your
`08:52` workspace itself. Where do you want your
`08:52` workspace itself. Where do you want your files going? What content are you doing?
`08:55` files going? What content are you doing?
`08:55` files going? What content are you doing? If you're writing stuff, where do you
`08:57` If you're writing stuff, where do you
`08:57` If you're writing stuff, where do you want the events to be? Where do you want
`08:59` want the events to be? Where do you want
`08:59` want the events to be? Where do you want newsletters to be? Where do you want
`09:00` newsletters to be? Where do you want
`09:00` newsletters to be? Where do you want social to be? And it's just a file
`09:02` social to be? And it's just a file
`09:02` social to be? And it's just a file system. Again, if you don't want to work
`09:04` system. Again, if you don't want to work
`09:04` system. Again, if you don't want to work inside of here, you can actually just go
`09:06` inside of here, you can actually just go
`09:06` inside of here, you can actually just go straight into the folder and just create
`09:09` straight into the folder and just create
`09:09` straight into the folder and just create new folders, new text document. That can
`09:12` new folders, new text document. That can
`09:12` new folders, new text document. That can be a prompt, that can be a context,
`09:14` be a prompt, that can be a context,
`09:14` be a prompt, that can be a context, right? It's that simple, and you can
`09:16` right? It's that simple, and you can
`09:16` right? It's that simple, and you can just you can just edit it without any of
`09:18` just you can just edit it without any of
`09:18` just you can just edit it without any of this. Look, my my AGENTS.md, this is
`09:21` this. Look, my my AGENTS.md, this is
`09:21` this. Look, my my AGENTS.md, this is what it looks like in if you open up
`09:22` what it looks like in if you open up
`09:22` what it looks like in if you open up notepad. Same thing. And nothing breaks
`09:24` notepad. Same thing. And nothing breaks
`09:24` notepad. Same thing. And nothing breaks when you edit it. You can type whatever
`09:26` when you edit it. You can type whatever
`09:26` when you edit it. You can type whatever you want in here. It's just English.
`09:28` you want in here. It's just English.
`09:29` you want in here. It's just English. Now, it's good to have it uniform and
`09:30` Now, it's good to have it uniform and
`09:30` Now, it's good to have it uniform and well, but that's the idea here. Most
`09:33` well, but that's the idea here. Most
`09:33` well, but that's the idea here. Most people are only doing one one these
`09:35` people are only doing one one these
`09:35` people are only doing one one these layers, maybe two. The reason you want
`09:38` layers, maybe two. The reason you want
`09:38` layers, maybe two. The reason you want to actually have these three layers is
`09:41` to actually have these three layers is
`09:41` to actually have these three layers is it stops the narrow funnel of AI doing
`09:44` it stops the narrow funnel of AI doing
`09:44` it stops the narrow funnel of AI doing too much all at once without allowing
`09:46` too much all at once without allowing
`09:46` too much all at once without allowing you to edit every single part, but still
`09:49` you to edit every single part, but still
`09:49` you to edit every single part, but still give you the ability to automate the
`09:51` give you the ability to automate the
`09:51` give you the ability to automate the entire process. So, again, the router,
`09:54` entire process. So, again, the router,
`09:54` entire process. So, again, the router, the initial Claude at MD or whatever
`09:57` the initial Claude at MD or whatever
`09:57` the initial Claude at MD or whatever you're naming it, is loaded when you
`09:59` you're naming it, is loaded when you
`09:59` you're naming it, is loaded when you start any task. The workspace is loaded
`10:02` start any task. The workspace is loaded
`10:02` start any task. The workspace is loaded when you're in the workspace, when you
`10:04` when you're in the workspace, when you
`10:04` when you're in the workspace, when you want to do production, it's only reading
`10:06` want to do production, it's only reading
`10:06` want to do production, it's only reading stuff that's in production as it needs
`10:08` stuff that's in production as it needs
`10:08` stuff that's in production as it needs to. When you're doing stuff in the
`10:09` to. When you're doing stuff in the
`10:09` to. When you're doing stuff in the writing room, it's only writing it when
`10:11` writing room, it's only writing it when
`10:11` writing room, it's only writing it when you're in the writing room. For example,
`10:13` you're in the writing room. For example,
`10:13` you're in the writing room. For example, go to writing room, let's start making
`10:18` go to writing room, let's start making
`10:18` go to writing room, let's start making something. Very little prompting, almost
`10:22` something. Very little prompting, almost
`10:22` something. Very little prompting, almost terrible prompting, yet the agent,
`10:24` terrible prompting, yet the agent,
`10:24` terrible prompting, yet the agent, without wasting a whole bunch of
`10:26` without wasting a whole bunch of
`10:26` without wasting a whole bunch of co-tokens and going through everything,
`10:27` co-tokens and going through everything,
`10:27` co-tokens and going through everything, immediately goes to the context file
`10:30` immediately goes to the context file
`10:30` immediately goes to the context file that I have in writing room that
`10:32` that I have in writing room that
`10:32` that I have in writing room that describes what it is, describes what to
`10:34` describes what it is, describes what to
`10:34` describes what it is, describes what to load and what not to load, and just
`10:36` load and what not to load, and just
`10:36` load and what not to load, and just describes the folder structure and what
`10:38` describes the folder structure and what
`10:38` describes the folder structure and what the process is. First, I understand the
`10:40` the process is. First, I understand the
`10:40` the process is. First, I understand the topic, then I find the angle, then I
`10:42` topic, then I find the angle, then I
`10:42` topic, then I find the angle, then I write it, then I catch problems. You can
`10:44` write it, then I catch problems. You can
`10:44` write it, then I catch problems. You can also incorporate skills into this,
`10:46` also incorporate skills into this,
`10:46` also incorporate skills into this, right? So, you can download the
`10:47` right? So, you can download the
`10:47` right? So, you can download the humanizer skill, which is an actual
`10:49` humanizer skill, which is an actual
`10:49` humanizer skill, which is an actual GitHub, I recommend you all check out,
`10:51` GitHub, I recommend you all check out,
`10:51` GitHub, I recommend you all check out, or like doc co-authoring skill, which is
`10:54` or like doc co-authoring skill, which is
`10:54` or like doc co-authoring skill, which is another set of markdown files or even
`10:56` another set of markdown files or even
`10:56` another set of markdown files or even Python scripts and tutorials that
`10:59` Python scripts and tutorials that
`10:59` Python scripts and tutorials that someone else build to do a certain task.
`11:02` someone else build to do a certain task.
`11:02` someone else build to do a certain task. And this is where this whole process is
`11:04` And this is where this whole process is
`11:04` And this is where this whole process is different than just running skills.
`11:06` different than just running skills.
`11:06` different than just running skills. You're putting skills inside of a
`11:08` You're putting skills inside of a
`11:08` You're putting skills inside of a thought process. And as you can see,
`11:09` thought process. And as you can see,
`11:10` thought process. And as you can see, right here, we're in the writing room.
`11:11` right here, we're in the writing room.
`11:11` right here, we're in the writing room. Clean slate, no drafts in progress.
`11:13` Clean slate, no drafts in progress.
`11:13` Clean slate, no drafts in progress. Voice is loaded, style is block host.
`11:15` Voice is loaded, style is block host.
`11:15` Voice is loaded, style is block host. What do you want me to make? From one
`11:16` What do you want me to make? From one
`11:16` What do you want me to make? From one single prompt, we've gotten it in there.
`11:19` single prompt, we've gotten it in there.
`11:19` single prompt, we've gotten it in there. But while that's going on, I can open up
`11:21` But while that's going on, I can open up
`11:21` But while that's going on, I can open up another Claude, and I can say, "Hey,
`11:24` another Claude, and I can say, "Hey,
`11:24` another Claude, and I can say, "Hey, I want to do some work in production."
`11:28` I want to do some work in production."
`11:28` I want to do some work in production." And it's going to go in there, and I can
`11:29` And it's going to go in there, and I can
`11:29` And it's going to go in there, and I can do whatever work I want to do in
`11:31` do whatever work I want to do in
`11:31` do whatever work I want to do in production, right? I want to maybe make
`11:32` production, right? I want to maybe make
`11:32` production, right? I want to maybe make some designs, I want to create some sort
`11:35` some designs, I want to create some sort
`11:35` some designs, I want to create some sort of code for workflows in there. But the
`11:37` of code for workflows in there. But the
`11:37` of code for workflows in there. But the real fun happens is when you're building
`11:39` real fun happens is when you're building
`11:39` real fun happens is when you're building stuff in production with one of your
`11:41` stuff in production with one of your
`11:41` stuff in production with one of your Claude Code instances. You're writing a
`11:43` Claude Code instances. You're writing a
`11:43` Claude Code instances. You're writing a script and you can say, "Hey, take the
`11:46` script and you can say, "Hey, take the
`11:46` script and you can say, "Hey, take the script from writing room and let's make
`11:50` script from writing room and let's make
`11:50` script from writing room and let's make an animation out of it in production."
`11:54` an animation out of it in production."
`11:54` an animation out of it in production." It's moving that file. It's going to go
`11:56` It's moving that file. It's going to go
`11:56` It's moving that file. It's going to go there. Now, it's going to notice that I
`11:58` there. Now, it's going to notice that I
`11:58` there. Now, it's going to notice that I don't have any scripts in there when I
`11:59` don't have any scripts in there when I
`11:59` don't have any scripts in there when I send this out. But if I did have a final
`12:01` send this out. But if I did have a final
`12:01` send this out. But if I did have a final in there, it's going to go look for it,
`12:03` in there, it's going to go look for it,
`12:03` in there, it's going to go look for it, right? There's no scripts. Boom, it
`12:04` right? There's no scripts. Boom, it
`12:04` right? There's no scripts. Boom, it didn't waste a whole bunch of tokens, it
`12:06` didn't waste a whole bunch of tokens, it
`12:06` didn't waste a whole bunch of tokens, it didn't do anything, but it immediately
`12:07` didn't do anything, but it immediately
`12:07` didn't do anything, but it immediately knew, "Oh, well, we have to write a
`12:08` knew, "Oh, well, we have to write a
`12:08` knew, "Oh, well, we have to write a script first." Or if you have a script
`12:10` script first." Or if you have a script
`12:10` script first." Or if you have a script somewhere else, you can upload it. You
`12:11` somewhere else, you can upload it. You
`12:11` somewhere else, you can upload it. You see, most apps or frameworks or agentic
`12:14` see, most apps or frameworks or agentic
`12:14` see, most apps or frameworks or agentic things require you to build an agent for
`12:16` things require you to build an agent for
`12:16` things require you to build an agent for each of these. I need a writing room
`12:18` each of these. I need a writing room
`12:18` each of these. I need a writing room agent, I need this agent, I need this
`12:19` agent, I need this agent, I need this
`12:19` agent, I need this agent, I need this agent. But the way in which you approach
`12:21` agent. But the way in which you approach
`12:21` agent. But the way in which you approach each task is always different. Why not
`12:24` each task is always different. Why not
`12:24` each task is always different. Why not just have Claude Code become the agent
`12:27` just have Claude Code become the agent
`12:27` just have Claude Code become the agent you need when you're working in the work
`12:29` you need when you're working in the work
`12:29` you need when you're working in the work space. And you see from there, you get
`12:32` space. And you see from there, you get
`12:32` space. And you see from there, you get the most important part of this process
`12:35` the most important part of this process
`12:35` the most important part of this process is just good routing in English
`12:37` is just good routing in English
`12:37` is just good routing in English language. Again, this is all just
`12:39` language. Again, this is all just
`12:39` language. Again, this is all just English, right? File folder names,
`12:41` English, right? File folder names,
`12:41` English, right? File folder names, titles. It's describing what you want,
`12:43` titles. It's describing what you want,
`12:44` titles. It's describing what you want, right? This right here is the most
`12:45` right? This right here is the most
`12:45` right? This right here is the most important pattern in the whole system.
`12:47` important pattern in the whole system.
`12:47` important pattern in the whole system. It's just a simple table that tells the
`12:50` It's just a simple table that tells the
`12:50` It's just a simple table that tells the AI, "For this task, read these files,
`12:53` AI, "For this task, read these files,
`12:53` AI, "For this task, read these files, skip those files, you might need these
`12:56` skip those files, you might need these
`12:56` skip those files, you might need these skills." Without this, the AI either
`12:58` skills." Without this, the AI either
`12:58` skills." Without this, the AI either reads everything and runs out of the
`13:00` reads everything and runs out of the
`13:00` reads everything and runs out of the room and just does all sorts of stuff
`13:02` room and just does all sorts of stuff
`13:02` room and just does all sorts of stuff you don't want it to do using way too
`13:03` you don't want it to do using way too
`13:03` you don't want it to do using way too many tokens, or it guesses wrong about
`13:06` many tokens, or it guesses wrong about
`13:06` many tokens, or it guesses wrong about what matters or just doesn't hit what
`13:08` what matters or just doesn't hit what
`13:08` what matters or just doesn't hit what you need, or you can't edit what it
`13:10` you need, or you can't edit what it
`13:10` you need, or you can't edit what it creates along the process. This table
`13:13` creates along the process. This table
`13:13` creates along the process. This table eliminates all of those problems. This
`13:15` eliminates all of those problems. This
`13:15` eliminates all of those problems. This This system here gets rid of all of
`13:17` This system here gets rid of all of
`13:17` This system here gets rid of all of that. Now, let's go ahead and zoom in a
`13:18` that. Now, let's go ahead and zoom in a
`13:18` that. Now, let's go ahead and zoom in a little bit here and actually really look
`13:21` little bit here and actually really look
`13:21` little bit here and actually really look at this kind of folder structure. Walk
`13:23` at this kind of folder structure. Walk
`13:23` at this kind of folder structure. Walk through this pipeline. Imagine you're
`13:24` through this pipeline. Imagine you're
`13:24` through this pipeline. Imagine you're sitting here and you open up production
`13:27` sitting here and you open up production
`13:27` sitting here and you open up production and you go to workflows, right? So, you
`13:29` and you go to workflows, right? So, you
`13:29` and you go to workflows, right? So, you know you're doing some sort of animation
`13:31` know you're doing some sort of animation
`13:31` know you're doing some sort of animation production or insert whatever it is that
`13:33` production or insert whatever it is that
`13:33` production or insert whatever it is that this folder is as a separate workspace
`13:36` this folder is as a separate workspace
`13:36` this folder is as a separate workspace as part of a larger tasks flow that
`13:38` as part of a larger tasks flow that
`13:38` as part of a larger tasks flow that you're doing. Production has a pipeline
`13:41` you're doing. Production has a pipeline
`13:41` you're doing. Production has a pipeline in itself as well. Four stages. You have
`13:44` in itself as well. Four stages. You have
`13:44` in itself as well. Four stages. You have to do a brief, you need a spec, which a
`13:46` to do a brief, you need a spec, which a
`13:46` to do a brief, you need a spec, which a specification, a build, and an output. I
`13:49` specification, a build, and an output. I
`13:49` specification, a build, and an output. I have a brief, some sort of script that I
`13:51` have a brief, some sort of script that I
`13:51` have a brief, some sort of script that I want to do. I have a spec that's
`13:53` want to do. I have a spec that's
`13:53` want to do. I have a spec that's generated from that brief, and then goes
`13:55` generated from that brief, and then goes
`13:55` generated from that brief, and then goes into the builds, and it builds out the
`13:56` into the builds, and it builds out the
`13:56` into the builds, and it builds out the animations, and then finally you have
`13:58` animations, and then finally you have
`13:58` animations, and then finally you have the output. More importantly, this
`14:01` the output. More importantly, this
`14:01` the output. More importantly, this allows me to have one MD file, right?
`14:03` allows me to have one MD file, right?
`14:03` allows me to have one MD file, right? So, for my production, I can have a ton
`14:05` So, for my production, I can have a ton
`14:05` So, for my production, I can have a ton text for this file system that is
`14:07` text for this file system that is
`14:08` text for this file system that is generating different types of sub agents
`14:10` generating different types of sub agents
`14:10` generating different types of sub agents or ways to look at it. Again, I'm not
`14:11` or ways to look at it. Again, I'm not
`14:11` or ways to look at it. Again, I'm not even worried about agents. I'm just
`14:13` even worried about agents. I'm just
`14:13` even worried about agents. I'm just worried about what the workspace is,
`14:15` worried about what the workspace is,
`14:15` worried about what the workspace is, what I want to do in these workspace. If
`14:17` what I want to do in these workspace. If
`14:17` what I want to do in these workspace. If I want to understand, look up technical
`14:19` I want to understand, look up technical
`14:19` I want to understand, look up technical standards, look up design rules, I can
`14:21` standards, look up design rules, I can
`14:21` standards, look up design rules, I can find that because I might have that in a
`14:24` find that because I might have that in a
`14:24` find that because I might have that in a doc, right? So, I have components or
`14:27` doc, right? So, I have components or
`14:27` doc, right? So, I have components or maybe some way I like to design these
`14:29` maybe some way I like to design these
`14:29` maybe some way I like to design these systems with my color designs, my
`14:31` systems with my color designs, my
`14:31` systems with my color designs, my headers, my quality. And again, these
`14:34` headers, my quality. And again, these
`14:34` headers, my quality. And again, these are all just generated from English
`14:35` are all just generated from English
`14:35` are all just generated from English super short docs. These are visual
`14:37` super short docs. These are visual
`14:37` super short docs. These are visual philosophy or what type of tech you want
`14:39` philosophy or what type of tech you want
`14:39` philosophy or what type of tech you want to use. And it doesn't always have to
`14:41` to use. And it doesn't always have to
`14:41` to use. And it doesn't always have to read that, but maybe during the brief
`14:43` read that, but maybe during the brief
`14:43` read that, but maybe during the brief stage, it does, right? When you're
`14:46` stage, it does, right? When you're
`14:46` stage, it does, right? When you're sitting there and you're going through
`14:47` sitting there and you're going through
`14:47` sitting there and you're going through and you're loading the brief, well, I
`14:49` and you're loading the brief, well, I
`14:49` and you're loading the brief, well, I need to make sure you look at the tech
`14:51` need to make sure you look at the tech
`14:51` need to make sure you look at the tech standards when you're making the brief.
`14:52` standards when you're making the brief.
`14:52` standards when you're making the brief. If it's loading the spec, I need to make
`14:54` If it's loading the spec, I need to make
`14:54` If it's loading the spec, I need to make sure it looks at the design system and
`14:56` sure it looks at the design system and
`14:56` sure it looks at the design system and our component library, and then maybe it
`14:58` our component library, and then maybe it
`14:58` our component library, and then maybe it doesn't need to load the deck as well.
`14:59` doesn't need to load the deck as well.
`14:59` doesn't need to load the deck as well. And you can swap this around super
`15:02` And you can swap this around super
`15:02` And you can swap this around super easily just by looking at it. This is
`15:04` easily just by looking at it. This is
`15:04` easily just by looking at it. This is traditional function calling software
`15:06` traditional function calling software
`15:06` traditional function calling software routing. This has existed for decades
`15:09` routing. This has existed for decades
`15:09` routing. This has existed for decades and decades, but now it gets to be
`15:11` and decades, but now it gets to be
`15:11` and decades, but now it gets to be natural language, English. Now, at this
`15:14` natural language, English. Now, at this
`15:14` natural language, English. Now, at this point, many of you are like, "Oh, well,
`15:16` point, many of you are like, "Oh, well,
`15:16` point, many of you are like, "Oh, well, you're just making a bunch of skills."
`15:17` you're just making a bunch of skills."
`15:17` you're just making a bunch of skills." Technically, yes. Now, for those of you
`15:19` Technically, yes. Now, for those of you
`15:19` Technically, yes. Now, for those of you who don't know what skills are, again, I
`15:21` who don't know what skills are, again, I
`15:21` who don't know what skills are, again, I mentioned them earlier. I I talked about
`15:23` mentioned them earlier. I I talked about
`15:23` mentioned them earlier. I I talked about this idea that you can download them
`15:24` this idea that you can download them
`15:25` this idea that you can download them from everywhere. There's PowerPoint
`15:27` from everywhere. There's PowerPoint
`15:27` from everywhere. There's PowerPoint skills, and I have other um videos on
`15:29` skills, and I have other um videos on
`15:29` skills, and I have other um videos on this. But, at the end of the day, skills
`15:32` this. But, at the end of the day, skills
`15:32` this. But, at the end of the day, skills are a process that someone else figured
`15:34` are a process that someone else figured
`15:34` are a process that someone else figured out and designed a set of packages or
`15:36` out and designed a set of packages or
`15:37` out and designed a set of packages or folders, just like I'm doing here, to
`15:39` folders, just like I'm doing here, to
`15:40` folders, just like I'm doing here, to tell Claude how to do something. The
`15:41` tell Claude how to do something. The
`15:41` tell Claude how to do something. The thing is, skills aren't just markdown
`15:43` thing is, skills aren't just markdown
`15:43` thing is, skills aren't just markdown files with instructions. Some are just
`15:45` files with instructions. Some are just
`15:45` files with instructions. Some are just that, but skills work best when they're
`15:48` that, but skills work best when they're
`15:48` that, but skills work best when they're wired into a system. One important note,
`15:50` wired into a system. One important note,
`15:50` wired into a system. One important note, too, is this is where the difference
`15:52` too, is this is where the difference
`15:52` too, is this is where the difference between it's just skills we're creating
`15:54` between it's just skills we're creating
`15:54` between it's just skills we're creating here and it's a system. You're actually
`15:57` here and it's a system. You're actually
`15:57` here and it's a system. You're actually putting skills inside of your MD. So, in
`16:00` putting skills inside of your MD. So, in
`16:00` putting skills inside of your MD. So, in this case, I have in my context for
`16:04` this case, I have in my context for
`16:04` this case, I have in my context for production, I have the fire outlook,
`16:05` production, I have the fire outlook,
`16:05` production, I have the fire outlook, what I want to do, but also, right? This
`16:09` what I want to do, but also, right? This
`16:09` what I want to do, but also, right? This is where you can talk to call skills or
`16:12` is where you can talk to call skills or
`16:12` is where you can talk to call skills or MCP servers. If you don't know what an
`16:14` MCP servers. If you don't know what an
`16:14` MCP servers. If you don't know what an MCP, it's model context protocol. I
`16:17` MCP, it's model context protocol. I
`16:17` MCP, it's model context protocol. I think that deserves an entire video in
`16:19` think that deserves an entire video in
`16:19` think that deserves an entire video in itself, but just think of it as a way
`16:20` itself, but just think of it as a way
`16:21` itself, but just think of it as a way that the AI can talk to other apps and
`16:23` that the AI can talk to other apps and
`16:23` that the AI can talk to other apps and services easier. It's designed to just
`16:26` services easier. It's designed to just
`16:26` services easier. It's designed to just kind of plug and play it in, rather than
`16:27` kind of plug and play it in, rather than
`16:28` kind of plug and play it in, rather than you have to create all these custom
`16:29` you have to create all these custom
`16:29` you have to create all these custom integrations. At certain points, we
`16:31` integrations. At certain points, we
`16:31` integrations. At certain points, we might want the front-end design skill or
`16:33` might want the front-end design skill or
`16:33` might want the front-end design skill or a web app testing skill or PDF skill.
`16:35` a web app testing skill or PDF skill.
`16:35` a web app testing skill or PDF skill. Or, I might want to give Claude the
`16:38` Or, I might want to give Claude the
`16:38` Or, I might want to give Claude the opportunity to look up a skill, find a
`16:41` opportunity to look up a skill, find a
`16:42` opportunity to look up a skill, find a new skill, or even possibly create one.
`16:44` new skill, or even possibly create one.
`16:44` new skill, or even possibly create one. You can wire up to 15 skills, 20 skills,
`16:48` You can wire up to 15 skills, 20 skills,
`16:48` You can wire up to 15 skills, 20 skills, 100 skills into a workspace. Or, you can
`16:51` 100 skills into a workspace. Or, you can
`16:51` 100 skills into a workspace. Or, you can perfectly add the skills where you would
`16:54` perfectly add the skills where you would
`16:54` perfectly add the skills where you would need them inside the workspace, rather
`16:57` need them inside the workspace, rather
`16:57` need them inside the workspace, rather than having them loaded at all times.
`17:00` than having them loaded at all times.
`17:00` than having them loaded at all times. That's the whole idea here is about plug
`17:02` That's the whole idea here is about plug
`17:02` That's the whole idea here is about plug and play and routing. One other sneaky
`17:05` and play and routing. One other sneaky
`17:05` and play and routing. One other sneaky thing I do to like completely ignore
`17:07` thing I do to like completely ignore
`17:07` thing I do to like completely ignore like databases or anything like that, in
`17:10` like databases or anything like that, in
`17:10` like databases or anything like that, in my Claude MD, the main file at the
`17:13` my Claude MD, the main file at the
`17:13` my Claude MD, the main file at the beginning that shows, you know, every AI
`17:15` beginning that shows, you know, every AI
`17:15` beginning that shows, you know, every AI or every agent that comes into this
`17:16` or every agent that comes into this
`17:16` or every agent that comes into this workspace can see my entire folder
`17:18` workspace can see my entire folder
`17:18` workspace can see my entire folder structure navigation, I just add naming
`17:21` structure navigation, I just add naming
`17:21` structure navigation, I just add naming conventions, right? So, if a file's
`17:24` conventions, right? So, if a file's
`17:24` conventions, right? So, if a file's going to be outputted a certain way, it
`17:26` going to be outputted a certain way, it
`17:26` going to be outputted a certain way, it needs to name it. For blog drafts, it
`17:28` needs to name it. For blog drafts, it
`17:28` needs to name it. For blog drafts, it needs to be like file name, where it's
`17:30` needs to be like file name, where it's
`17:30` needs to be like file name, where it's at. Is it draft? Is it V2? Is it V3?
`17:33` at. Is it draft? Is it V2? Is it V3?
`17:33` at. Is it draft? Is it V2? Is it V3? Example, API off guide draft, right? Or
`17:36` Example, API off guide draft, right? Or
`17:36` Example, API off guide draft, right? Or same for newsletters. Here's the year
`17:38` same for newsletters. Here's the year
`17:38` same for newsletters. Here's the year and day, and then here's what it's kind
`17:40` and day, and then here's what it's kind
`17:40` and day, and then here's what it's kind of is, right? 2026 03 launch week.md.
`17:44` of is, right? 2026 03 launch week.md.
`17:44` of is, right? 2026 03 launch week.md. So, the AI knows to organize and move
`17:47` So, the AI knows to organize and move
`17:47` So, the AI knows to organize and move stuff, which comes in handy when instead
`17:49` stuff, which comes in handy when instead
`17:49` stuff, which comes in handy when instead of having to navigate through these
`17:50` of having to navigate through these
`17:50` of having to navigate through these files or have an agent that's connected
`17:52` files or have an agent that's connected
`17:52` files or have an agent that's connected to some sort of, you know, SQL database
`17:55` to some sort of, you know, SQL database
`17:55` to some sort of, you know, SQL database or vector database or query or Postgres
`17:58` or vector database or query or Postgres
`17:58` or vector database or query or Postgres or anything like that, I could just say,
`17:59` or anything like that, I could just say,
`17:59` or anything like that, I could just say, "Hey,
`18:00` "Hey,
`18:01` "Hey, pull
`18:02` pull
`18:02` pull my
`18:04` my
`18:04` my uh off demo
`18:07` uh off demo
`18:07` uh off demo demo V2 and build a spec from it. It
`18:11` demo V2 and build a spec from it. It
`18:11` demo V2 and build a spec from it. It immediately knows, without me doing
`18:12` immediately knows, without me doing
`18:12` immediately knows, without me doing anything, to look where that V2 demo
`18:16` anything, to look where that V2 demo
`18:16` anything, to look where that V2 demo script would be, because it knows how to
`18:18` script would be, because it knows how to
`18:18` script would be, because it knows how to find it. It knows to pull it. Then it
`18:20` find it. It knows to pull it. Then it
`18:20` find it. It knows to pull it. Then it knows to read the docs associated with
`18:24` knows to read the docs associated with
`18:24` knows to read the docs associated with specs and then start building it.
`18:27` specs and then start building it.
`18:27` specs and then start building it. I have zero code, technically speaking,
`18:30` I have zero code, technically speaking,
`18:30` I have zero code, technically speaking, running any sort of Python injection or
`18:33` running any sort of Python injection or
`18:33` running any sort of Python injection or framework or database. This is tools
`18:36` framework or database. This is tools
`18:36` framework or database. This is tools that people are building right now.
`18:38` that people are building right now.
`18:38` that people are building right now. They're building apps and crazy Python
`18:40` They're building apps and crazy Python
`18:40` They're building apps and crazy Python stuff, which in some very bespoke cases
`18:42` stuff, which in some very bespoke cases
`18:42` stuff, which in some very bespoke cases might be useful, but most of the time
`18:44` might be useful, but most of the time
`18:44` might be useful, but most of the time for most people, you don't need all that
`18:46` for most people, you don't need all that
`18:46` for most people, you don't need all that extra stuff to get the process and the
`18:49` extra stuff to get the process and the
`18:49` extra stuff to get the process and the job done. The job to be done is more
`18:52` job done. The job to be done is more
`18:52` job done. The job to be done is more important than this kind of rigid
`18:54` important than this kind of rigid
`18:54` important than this kind of rigid architecture that so many people are
`18:56` architecture that so many people are
`18:56` architecture that so many people are building. You see, the folder becomes
`18:59` building. You see, the folder becomes
`18:59` building. You see, the folder becomes your app. This is your UI. What simpler
`19:01` your app. This is your UI. What simpler
`19:02` your app. This is your UI. What simpler UI than a folder? And the best part is,
`19:04` UI than a folder? And the best part is,
`19:04` UI than a folder? And the best part is, I don't even need to technically click
`19:05` I don't even need to technically click
`19:06` I don't even need to technically click on anything. I could just talk with my
`19:07` on anything. I could just talk with my
`19:07` on anything. I could just talk with my voice to AI, have it do all the text
`19:10` voice to AI, have it do all the text
`19:10` voice to AI, have it do all the text work for me. The next stage of this, I
`19:13` work for me. The next stage of this, I
`19:13` work for me. The next stage of this, I promise you, within 6 months everyone's
`19:15` promise you, within 6 months everyone's
`19:15` promise you, within 6 months everyone's going to be doing this, is just talking
`19:17` going to be doing this, is just talking
`19:17` going to be doing this, is just talking to your folder setup. It's going to be
`19:20` to your folder setup. It's going to be
`19:20` to your folder setup. It's going to be designed and set up to be this way. It's
`19:22` designed and set up to be this way. It's
`19:22` designed and set up to be this way. It's going to be around yours, which leads
`19:24` going to be around yours, which leads
`19:24` going to be around yours, which leads into a good final point. How do you make
`19:27` into a good final point. How do you make
`19:27` into a good final point. How do you make this yours? This template uses a fake
`19:30` this yours? This template uses a fake
`19:30` this yours? This template uses a fake idea with fake process, right? Fake blog
`19:33` idea with fake process, right? Fake blog
`19:33` idea with fake process, right? Fake blog posts and demos.
`19:35` posts and demos.
`19:35` posts and demos. If you're a content creator, writing
`19:37` If you're a content creator, writing
`19:37` If you're a content creator, writing room might become your script lab.
`19:39` room might become your script lab.
`19:39` room might become your script lab. Production becomes your edit bay,
`19:41` Production becomes your edit bay,
`19:41` Production becomes your edit bay, uh
`19:42` uh
`19:42` uh whatever. Community becomes a
`19:43` whatever. Community becomes a
`19:43` whatever. Community becomes a distribution hub, and you're going to
`19:45` distribution hub, and you're going to
`19:45` distribution hub, and you're going to remove and change these rules to edit
`19:48` remove and change these rules to edit
`19:48` remove and change these rules to edit your platform, maybe your tone and voice
`19:52` your platform, maybe your tone and voice
`19:52` your platform, maybe your tone and voice inside of these, right? So, what is your
`19:54` inside of these, right? So, what is your
`19:54` inside of these, right? So, what is your audience? That's what you want to hear.
`19:56` audience? That's what you want to hear.
`19:56` audience? That's what you want to hear. It's working developers, 2 to 8 years of
`19:58` It's working developers, 2 to 8 years of
`19:58` It's working developers, 2 to 8 years of experience, technical decision-makers,
`20:00` experience, technical decision-makers,
`20:00` experience, technical decision-makers, developer advocates. It might be
`20:02` developer advocates. It might be
`20:02` developer advocates. It might be something completely different. You
`20:03` something completely different. You
`20:03` something completely different. You might be in construction or real estate.
`20:05` might be in construction or real estate.
`20:05` might be in construction or real estate. But, this is roughly what you would be
`20:08` But, this is roughly what you would be
`20:08` But, this is roughly what you would be doing across all of them. And the best
`20:10` doing across all of them. And the best
`20:10` doing across all of them. And the best part is, all you need is one
`20:12` part is, all you need is one
`20:12` part is, all you need is one subscription to Claude Code, and you can
`20:14` subscription to Claude Code, and you can
`20:14` subscription to Claude Code, and you can generate 100, \{{}quote} \{{}unquote}, apps
`20:17` generate 100, \{{}quote} \{{}unquote}, apps
`20:17` generate 100, \{{}quote} \{{}unquote}, apps that are just folders creating what you
`20:19` that are just folders creating what you
`20:19` that are just folders creating what you need. Obviously, it's much more
`20:22` need. Obviously, it's much more
`20:22` need. Obviously, it's much more complicated once you get into breaking
`20:24` complicated once you get into breaking
`20:24` complicated once you get into breaking down your workflow, but if you're a
`20:26` down your workflow, but if you're a
`20:26` down your workflow, but if you're a developer, if you're a freelancer,
`20:28` developer, if you're a freelancer,
`20:28` developer, if you're a freelancer, right? Just swap design for engineering
`20:31` right? Just swap design for engineering
`20:31` right? Just swap design for engineering and docs, or intake and production and
`20:33` and docs, or intake and production and
`20:33` and docs, or intake and production and delivery, right? This workspace changes
`20:36` delivery, right? This workspace changes
`20:36` delivery, right? This workspace changes lately, but the three-layer routing
`20:39` lately, but the three-layer routing
`20:39` lately, but the three-layer routing system, the idea that you go from, "Hey,
`20:43` system, the idea that you go from, "Hey,
`20:43` system, the idea that you go from, "Hey, look at this area. This is what you're
`20:45` look at this area. This is what you're
`20:45` look at this area. This is what you're going to." to lower-level context ones,
`20:49` going to." to lower-level context ones,
`20:49` going to." to lower-level context ones, to lower-level skills, is the idea here.
`20:53` to lower-level skills, is the idea here.
`20:53` to lower-level skills, is the idea here. It's just layers. This isn't a prompt
`20:55` It's just layers. This isn't a prompt
`20:55` It's just layers. This isn't a prompt trick. This isn't some sort of crazy
`20:58` trick. This isn't some sort of crazy
`20:58` trick. This isn't some sort of crazy infrastructure. It's folders and
`21:00` infrastructure. It's folders and
`21:00` infrastructure. It's folders and markdown files with the understanding of
`21:03` markdown files with the understanding of
`21:03` markdown files with the understanding of advanced software engineering. Every
`21:06` advanced software engineering. Every
`21:06` advanced software engineering. Every conversation after that, the AI knows
`21:08` conversation after that, the AI knows
`21:08` conversation after that, the AI knows where it is, what to load, what tools to
`21:10` where it is, what to load, what tools to
`21:11` where it is, what to load, what tools to use, and where to put the work in. Now,
`21:13` use, and where to put the work in. Now,
`21:13` use, and where to put the work in. Now, there is a lot of history behind my
`21:15` there is a lot of history behind my
`21:15` there is a lot of history behind my thinking. I didn't just randomly come up
`21:17` thinking. I didn't just randomly come up
`21:17` thinking. I didn't just randomly come up with this, and there's a lot of people
`21:18` with this, and there's a lot of people
`21:18` with this, and there's a lot of people who are already doing this. And the
`21:20` who are already doing this. And the
`21:20` who are already doing this. And the reason they're doing this is because it
`21:22` reason they're doing this is because it
`21:22` reason they're doing this is because it works. I'm writing a very large research
`21:24` works. I'm writing a very large research
`21:24` works. I'm writing a very large research paper right now that goes into the
`21:26` paper right now that goes into the
`21:26` paper right now that goes into the history of programming, rules of
`21:27` history of programming, rules of
`21:27` history of programming, rules of transparency, rules of composition,
`21:30` transparency, rules of composition,
`21:30` transparency, rules of composition, um all the way back down to 1972, and
`21:32` um all the way back down to 1972, and
`21:32` um all the way back down to 1972, and then I'm bringing it forward and
`21:34` then I'm bringing it forward and
`21:34` then I'm bringing it forward and applying all this stuff to modern-day
`21:36` applying all this stuff to modern-day
`21:36` applying all this stuff to modern-day AI, what it means to have humans in it.
`21:39` AI, what it means to have humans in it.
`21:39` AI, what it means to have humans in it. And I specifically talk about the layers
`21:41` And I specifically talk about the layers
`21:41` And I specifically talk about the layers that we could actually have. And I
`21:42` that we could actually have. And I
`21:42` that we could actually have. And I actually go into a five-layer
`21:44` actually go into a five-layer
`21:44` actually go into a five-layer architecture in the paper, but
`21:45` architecture in the paper, but
`21:45` architecture in the paper, but realistically, most of you just need to
`21:47` realistically, most of you just need to
`21:47` realistically, most of you just need to understand the three main layers that we
`21:48` understand the three main layers that we
`21:48` understand the three main layers that we talked about here. I will be making
`21:50` talked about here. I will be making
`21:50` talked about here. I will be making videos on this. However, it is in the
`21:52` videos on this. However, it is in the
`21:52` videos on this. However, it is in the main chat. Um if you want to download
`21:55` main chat. Um if you want to download
`21:55` main chat. Um if you want to download this and give it to Claude so that it
`21:57` this and give it to Claude so that it
`21:57` this and give it to Claude so that it can tell you about it rather than having
`21:59` can tell you about it rather than having
`21:59` can tell you about it rather than having to read through it, I highly recommend
`22:01` to read through it, I highly recommend
`22:01` to read through it, I highly recommend that. In fact, I urge you to do it
`22:03` that. In fact, I urge you to do it
`22:03` that. In fact, I urge you to do it because some of this is kind of
`22:04` because some of this is kind of
`22:04` because some of this is kind of technical information. I'm being nerdy.
`22:06` technical information. I'm being nerdy.
`22:06` technical information. I'm being nerdy. I'm being structured in it. But, this is
`22:08` I'm being structured in it. But, this is
`22:08` I'm being structured in it. But, this is layering out what the next decade is
`22:11` layering out what the next decade is
`22:11` layering out what the next decade is looking like. And this isn't because I'm
`22:12` looking like. And this isn't because I'm
`22:12` looking like. And this isn't because I'm predicting the future, it's because I'm
`22:15` predicting the future, it's because I'm
`22:15` predicting the future, it's because I'm learning from the past, from the last
`22:17` learning from the past, from the last
`22:17` learning from the past, from the last 200 years of software engineering, and I
`22:20` 200 years of software engineering, and I
`22:20` 200 years of software engineering, and I mean 200 when I say that, and applying
`22:23` mean 200 when I say that, and applying
`22:23` mean 200 when I say that, and applying it to AI. I want to teach the concepts
`22:26` it to AI. I want to teach the concepts
`22:26` it to AI. I want to teach the concepts that last, not the concepts that are
`22:28` that last, not the concepts that are
`22:28` that last, not the concepts that are replaced next month. I understand that
`22:30` replaced next month. I understand that
`22:30` replaced next month. I understand that some of this might be a little fast. It
`22:32` some of this might be a little fast. It
`22:32` some of this might be a little fast. It might be a little confusing. I'll keep
`22:34` might be a little confusing. I'll keep
`22:34` might be a little confusing. I'll keep making deeper dives. Give me feedback on
`22:37` making deeper dives. Give me feedback on
`22:37` making deeper dives. Give me feedback on what you didn't understand. How? Did I
`22:39` what you didn't understand. How? Did I
`22:39` what you didn't understand. How? Did I move too fast? I want to make these
`22:41` move too fast? I want to make these
`22:41` move too fast? I want to make these better every day. Again, I'm making
`22:42` better every day. Again, I'm making
`22:42` better every day. Again, I'm making these on my own. So, hopefully, this all
`22:44` these on my own. So, hopefully, this all
`22:44` these on my own. So, hopefully, this all gave you a good idea. If you do want
`22:47` gave you a good idea. If you do want
`22:47` gave you a good idea. If you do want access to any of these files or worker
`22:50` access to any of these files or worker
`22:50` access to any of these files or worker templates, um I am giving them already
`22:52` templates, um I am giving them already
`22:53` templates, um I am giving them already to my VIP and my uh premium accounts.
`22:56` to my VIP and my uh premium accounts.
`22:56` to my VIP and my uh premium accounts. It's my one way of like the work, right,
`22:58` It's my one way of like the work, right,
`22:58` It's my one way of like the work, right, to be able to support this. So, if
`23:00` to be able to support this. So, if
`23:00` to be able to support this. So, if you're able to subscribe, amazing. If it
`23:02` you're able to subscribe, amazing. If it
`23:02` you're able to subscribe, amazing. If it actually is that much of a financial
`23:04` actually is that much of a financial
`23:04` actually is that much of a financial challenge, please reach out to me. I can
`23:06` challenge, please reach out to me. I can
`23:06` challenge, please reach out to me. I can try to see if I can get you something,
`23:08` try to see if I can get you something,
`23:08` try to see if I can get you something, you know, quick and easy for you. But at
`23:10` you know, quick and easy for you. But at
`23:10` you know, quick and easy for you. But at the end of the day, go go check it out.
`23:12` the end of the day, go go check it out.
`23:12` the end of the day, go go check it out. Go check out all my other courses that
`23:13` Go check out all my other courses that
`23:13` Go check out all my other courses that I'll be doing. And again, as always,
`23:16` I'll be doing. And again, as always,
`23:16` I'll be doing. And again, as always, happy learning.