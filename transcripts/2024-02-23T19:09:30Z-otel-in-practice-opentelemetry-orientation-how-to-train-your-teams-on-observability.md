# OTEL in Practice: OpenTelemetry Orientation - How to Train Your Teams on Observability

Published on 2024-02-23T19:09:30Z

## Description

Train the trainer! Whether you've already been training teams on Observability for a while, or are brand new to it, you may find ...

URL: https://www.youtube.com/watch?v=o-1UE67l9q4

## Summary

In this YouTube video, Paige Cruz, a developer advocate at Chronosphere, discusses the importance of effective training in observability, particularly focusing on tracing and OpenTelemetry (OTEL). She shares her experiences transitioning from Site Reliability Engineer (SRE) to advocating for open-source observability solutions, emphasizing the need to bridge knowledge gaps between developers and observability practices. Paige outlines her successful strategies for training, including hands-on workshops tailored to specific tech stacks, and the importance of engaging learners through clear goals and practical exercises. She highlights the challenges of ensuring developers take ownership of observability practices and how to create a culture of responsibility within teams. The session concludes with resources for further learning and a call to action for more inclusive observability practices.

# Observability Training Workshop Transcript

Thank you so much for having me, OTEL in Practice. I have been attending the last few sessions and I am excited to present a little bit about my world. I am Paige Cruz, and I work at Chronosphere. This is my third observability company. When I wasn't working for observability companies, I was an SRE at customers of those observability companies, working on observability. If you can't tell, I have thought about this stuff for a very long time and from many different perspectives.

**A Quick Tale from the Field**

I have retired from SRE today and I am a developer advocate focused on the open source side of observability. In my previous role, my team was always tasked with leading big observability initiatives. This included migrating from one vendor to another, transitioning from self-hosted open source to managed services from our cloud providers, and rolling out tracing. The logging bill was so high that we had to address it immediately. 

There are many things that fall under the observability umbrella that my team was tasked to manage. During these initiatives, which impacted every team, we had to re-instrument either to add traces or to switch from a proprietary protocol to open source. 

Yes, technically, if the development teams were too busy, my team could focus on this work for three or four quarters and deliver a migration by the end. However, we were then seen as the owners of observability and treated like "Ask Jeeves." It felt like the line of responsibility between ops and dev had become skewed. This was fair considering we moved everything to a new platform with a new UI and new libraries, resulting in many knowledge gaps to cover.

I have steered quite a few migrations and tried many tactics to delegate the re-instrumentation work and pass the baton of ownership from solely ops to app devs. Out of everything I tried—linking documentation, sharing conference talks—the best tactic was hands-on workshops tailored specifically to my organization's tech stack. This approach highlighted the value of what we were trying to achieve.

**Train the Trainer**

This led me to bring forth the concept of "train the trainer," particularly in the context of tracing training, which requires participation from devs across the stack. To quote a famous work, "We’re all in this together." 

**Why Training Matters**

Now, let's talk about why training matters. There are several layers of complexity when introducing tracing. Observability is still an emerging field, and much of what we learn is done informally on the job. This varies based on the tech stack a company uses, the vendors or protocols they are using, and the companies they've worked for. 

Even two developers with the same years of experience could possess completely different sets of knowledge about observability. We must teach this stuff. While informal approaches are important for developing operational skills, we need to find a way to bridge the gap between informal knowledge and a strong foundation.

This foundation is crucial so that developers can add tracing, manage costs, and understand how sampling affects viewing aggregate trace data. There is a lot of complicated information in this space, and we need to consider where our learners are, what they know, and what they might have seen.

In the realm of observability, we have open telemetry, which has evolved from just being known for tracing. However, many developers I speak with are unaware of OTEL unless they are specifically tasked with bringing it into their organization. While we are excited about new features and advancements, there remains a segment of our colleagues who may not have even heard of OTEL. 

If we simply tell them, "Hey, add tracing to this service," and link to the OTEL docs, it won’t be helpful if they don’t understand what a span is or how to navigate OTEL’s components. Observability is new, OTEL is new and rapidly evolving, and tracing, in particular, is often seen as a tool for power users or the elite engineers.

**The Challenge with Tracing**

As someone who has worked on tracing products at New Relic and LightStep, I know tracing well. However, this is not a repeatable experience for everyone. We need all types of people to develop all sorts of things. This was the problem I focused on for my workshop: I want more people to use tracing. One barrier is that while partial traces can be helpful, the best scenario involves having a full trace from end to end across the system, which requires every service owner to do their part. 

I aim to help people understand how to send and use trace data. Having the information on how to instrument isn’t enough if they don’t know what to do when they get to a trace waterfall. Some may argue that the documentation has everything they need, but while the OTEL documentation site is fantastic, people often have questions like, "Is this library instrumented with OTEL?" 

**Finding the Aha Moments**

We need to provide more than just knowledge; we need to equip learners with skills. Many of us have experienced training that felt like a waste of time—training that was not tailored to our specific needs. Good training differs significantly from bad training, which may not match your expertise level or be relevant to your use case.

So, why does training matter? Because many learners, as an anonymous user on Reddit said, "I don’t even know what I don’t know," making it difficult to answer their questions. This highlights the necessity of training: not everyone is at the same level of understanding.

To develop effective training, we need to identify the gap between where learners are and where we want them to be. This involves understanding what knowledge they need and what skills they must acquire.

**Creating Effective Training**

When designing a training program, consider the problem you are trying to solve. Define the main drivers of the initiative, such as better visibility or ownership of data. Avoid the temptation to include everything you know about observability; focus on the essential aspects relevant to your audience.

Engage a representative sample of your learners by conducting surveys or informal chats to gauge their backgrounds and current knowledge. It’s crucial to understand where they are coming from and tailor the training accordingly.

Once you have a draft, have both a novice and an expert go through it. Observing their experiences can reveal stumbling blocks and areas that need clarification. 

**Delivery and Modalities**

When it comes to delivering your training, utilize existing resources and adapt them to your needs. Don’t reinvent the wheel; there are plenty of tutorials and workshops available. 

Consider the modalities of learning. Many people learn in different ways, so provide options for live guided sessions, self-guided learning, and recorded sessions. This increases the likelihood that more individuals will engage with the content.

In summary, think about the problem you are trying to solve, understand where your learners are, and narrow the training gap as much as possible. 

**Final Thoughts and Resources**

I want to share resources that can help you on your journey. Two recommended books are **"Design for How People Learn"** and **"Better Onboarding"** from A Book Apart. Both provide valuable insights into learning and training.

For open observability resources, the OTEL documentation has a section specifically for developers. The CNCF Glossary is also helpful for understanding acronyms and terminology.

Lastly, the OpenTelemetry demo is an excellent resource for those seeking a more realistic example. 

Thank you for your attention! If you have any questions or want to discuss your training needs, feel free to reach out. I’m here to help, and I’m excited to see more people embracing tracing!

## Raw YouTube Transcript

Thank you so much for
having me, OTEL in Practice. I have been attending the last few
sessions and excited to present a little bit about my world. So I am Paige Cruz. I work at Chronosphere. It is my third observability company. When I wasn't working for observability
companies, I I was an SRE at customers of those observability
companies working on observability. So if you can't tell, I have thought
about this stuff for a very long time and from lots of different perspectives. And just a kind of a
quick tale from the field. I have retired from SRE today. I'm a dev advocate that really
focuses on the open source side of observability, but in my day when
I was practicing, I had to lead. My team was always tasked with leading
big observability initiatives, whether that's migrating from one vendor to
another off of self hosted open source onto maybe a managed service from one of
our cloud providers rolling out tracing. Oh, my God, the logging bill
so high, you got to get on it. There's just a lot of things that kind
of fall under the answer observability umbrella that were kind of targeted
for my team to be the stewards of. And what I found when we had to do these
initiatives that touched every team, like re instrumenting either to add traces
or away from a proprietary protocol onto beautiful open source hotel that. Yes, technically, if the dev teams were
too busy, my team could do heads down work for like three or four quarters and yeah,
we could deliver something and we could be migrated by the end of that session. However then we were really seen
as like the owners of observability and we were kind of treated as like. Ask Jeeves. And it just really felt like the
line of responsibility between ops and dev kind of went out of whack. And that's totally fair. We moved everything. It was a new platform,
new UI, new libraries. Of course there was going to be
a lot of knowledge gaps to cover. And so I have, I have steered quite a
few migrations and I can say I've got to try lots of different tactics to be
able to delegate that re instrumentation work or to really pass that baton
of ownership rightfully from solely on ops over to app devs as well. And the best tactics. Out of everything. I tried linking the docs,
sending conference talks. The best was hands-on workshops that
were specifically tailored to my org's tech stack, what we were trying
to get developers to do, the value that it brings at the end of the day. So this is why I wanted to bring
train the trainer, trainer how to train specifically, we're talking
about tracing training today, and that just requires participation from
devs across the stack up and down. And to quote the Seminole work high school
musical, we are all in this together. So let's talk about why
train doesn't matter. Yes. Let's talk about how are you
actually going to develop a training? These aha moments, unless you were
a teacher in a previous career, you probably don't have a strong
background in learning theory or delivering trainings and teaching. So let's just get into what you
need to know to train folks. And then I'll kind of look, walk through
Some really specific decisions that I made when developing the KubeCon workshop. And then probably the favorite
part of anything that I put together is the further resources. So please, I will share these
slides books, talks, things that can help you along your journey. So why does training matter? Well, there are a few layers of
complexity that we're talking about when it comes to, say, introducing tracing. And the first thing is like, Full
stop, observability is still emerging. It is something that today we have learned
basically on the job pretty informally. It kind of depends on what tech
stack your company has, what vendors or protocols that your company is
using, how many companies you've worked for, what you've seen. So even two developers with the
same amount of years of experience could have totally different sets
of knowledge about this space. And so. You know, yeah, like a baby is not
sitting there thinking about like the milestones that we have been reaching. Like that is just not happening. We have to teach this stuff. And while it is done, and while I think
the informal approach is important for developing like operational skills and
sort of how do you use this data in the heat of an incident to decide on
mitigations you still have to find some sort of way to bridge that gap between
the formal patchwork knowledge And a strong foundation that you can build
on so that your developers can say, add tracing or maybe bring down the
bill or understand how sampling effects like viewing aggregate trace data. There's like a lot of
complicated stuff in this space. And so you really got to think about. where your learners are, what they
know, what they might have seen. And specifically, so we've got
observability, kind of new emerging domain, we're kind of bringing some
things from monitoring but we're also discovering a lot of new stuff. Within observability, we've got
open telemetry, which totally used to just be known for tracing. I'm like so happy that OTEL has now, like,
subsumed, like, I think the collector is the more popular, like, Most well
known component at this point, which is kind of cool, but unless you have
been really interested in observability or specifically tasked with bringing
OTEL into your org, like a lot of my like developer friends that I talked to
don't, they're like, Oh, that's cool. OTEL exists, you know, we're on. You know, some vendor, it's not
really something I'm looking into. So while we are like, Oh my god,
exponential histograms, logs are GA, like, all this stuff is happening, it's real. There's still a whole, like,
segment of our colleagues that maybe haven't even heard of OTEL. And if you were to just say,
Hey, add tracing to this service. Here's a link to the OTEL docs. It's got everything you need to know. If they don't know what a span is,
if they don't know how to navigate or the different components of OTEL,
like maybe y'all are using a vendors collector versus the OTEL, like there
are just a lot of ways that you could get lost within the OTEL project. And so observability, new, open
telemetry, new and rapidly evolving. And, finally, the nugget is for tracing,
in particular, the problem that I have seen is that it is, like, really has
this reputation as a tool for, like, power users, the super set of engineers,
and to be fair, like, if I reflect on, like, how I got to my tracing knowledge,
I literally, like, worked building the tracing product at New Relic and then went
to LightStep to go be an SRE and support the, like, tracing infrastructure there. And so I've, like, had to think about
tracing a lot, I've had to work on these systems, and that is just,
like, not a repeatable experience for everybody, nor should it be. We need all types of people to
develop all sorts of things. And so this was the problem that I
really honed in on for my My workshop was like, I think tracing is really
a super valuable type of telemetry. I want more people to use tracing. One of the barriers that I see is that
yes, partial traces still can be helpful, but the best case is that you've got a
full complete trace end to end throughout your system, which requires every service
owner along the way to do their part in instrumenting and then using that data. So. I said, this is the problem that I want
to solve, and I want to help people both know how to send trace data, oh
my god, and how to use trace data. Because just having the information
alone of how to instrument isn't enough if you don't know what to do
when you get to a trace waterfall. So the, like, counterpoints that
I've heard, the doc site has everything they need to know. I wrote the exact instructions down. They just have to follow them. But While I will say the OTEL
documentation site is absolutely fabulous, I rely on it all the time I still see
things a lot of questions like, is this library instrumented with OTEL? Is this, is the Ruby, like, log
spec, like, where is that at? And those are, like, very
easily answered questions. If you know where to look at the doc
site, just linking to OpenTelemetry. io is not going to necessarily
help someone navigate through our set of projects. yEah, so yes, plug for the OTEL doc site,
it is fabulous, but people need more than just the knowledge, they need the skills. So very quickly, who here, you
can maybe raise your hand or throw it in the chat, who here has
taken a training course at work? You don't have to tell me where or what,
but you've taken a training course that just felt like a total waste of time. You really could have used those
extra two hours and actually done something productive. I will raise my hand. I have sat through a couple of those. It's okay. I know it's been out there. Even our mandatory trainings that we've
got to take sometimes are like eye roll. So bad training is very
different than good training. It could be that the training course you
took, you were already an expert and it was just covering stuff you already knew. It could be it wasn't
tailored to your use case. Like, Your company signed up for generic
Kafka training, but actually you needed to know how to tune and specifically
like level up the operations for your cluster with your configurations and
everything within the context of your org. So the like generic 101 Kafka training
wasn't going to do anything for you. It wasn't tailored to your use case. And then also it could just be the format
and the delivery was totally mismatched. Like for me, I'm not a morning person. So anything that's before 9am, good luck. My brain is not firing at full capacity. And so there's a lot of, if you've
encountered bad training, this is not what I'm advising you to do. We're going to talk about how
you avoid some of those things and have effective training. So to answer with kind
of this, this section. Why does it matter? Why does training matter? Well, I came across this quote
that made me so sad, but like is totally exemplifies this. I don't even know what I don't know,
which makes it pretty hard to get started answering my own questions. And this was some
anonymous user on Reddit. Who's trying to find out
things about open telemetry. And that is the case. Like this is where we need to start. This is where our learners are. There are some people for
whom OTEL is this like. mystical black box that they
don't know anything about. And if you're on this call, I'm pretty
sure you have, you know, your way around the projects, you know, the architecture,
you know, what's up, but we've got to keep in mind that we are kind of a
select group here and the observability and OTEL knowledge needs to be very
widely distributed, democratized. And that is why training is
important because not everybody is here where we are yet. And we need them here. For full traces, for better
observability across companies, across industries that's the why. Let's just talk about the how now. We don't want to replicate the bad, awful
trainings that we have been through, but what I kind of shortened this as, you want
to find these aha moments of discovery. You want to have these learners engaged,
and really the whole point of training is that you are trying to change
behavior or get learners to take actions. So just giving them a rote so for
my workshop, if I had just given them, here's the step by steps of
how to instrument specifically a Python Flask application with traces. Cool. They could leave and they would know,
for that text stack, like, where to go, where to find that information,
and how to get traces out of that. Maybe they work at a place that has
Ruby, or works on Ruby on Rails. If I didn't do the work to
explain The higher level concepts or here's the OTEL registry. You can use it to check any
language instrumentation library. If you don't include the like
actionable pieces in the takeaways, people can still get really lost. Even if your instructions were
so beautiful and so detailed. Believe me, I have tried that route. So when, really where you want to
start with training is finding the gap, which is between where your developers
are today, what they know, what they understand, what they've seen, and where
you want them to be, what actions do they need to take, do they need to re
instrument from proprietary format to OTEL metrics format. Do they need to add spans? Do they need to take away spans? Because maybe the auto
instrumentation they turned on is like totally blowing up the bill. Like, think, really think concretely about
what should happen after this training. What are you expecting to see
the results and the change? And then that, that gap
between where they are. where you want them to be. That is where your training needs to fill. And we're not going to get deep into
learning theory, but really two things. What do they need to know? Knowledge, what info? And then skills. What do they need to be able
to do with that knowledge? Together, that is the recipe
for a successful training. And so when you're identifying
the gap get clear on the problem you're trying to solve. What is the main driver of the initiative? Better visibility? Are there a problem area in like the
profitable part of your system and you really need deeper level visibility there? Do you want to own your data? If you think about the motivations,
that can help you really scope down. Because for us, Observability experts,
it is very tempting to include the whole world, be like, well, let's
start with OpenTracing and OpenCensus and, you know, before OpenTelemetry,
and like, you will lose people. I promise you. I promise you, you will
lose people if you do that. So getting really crystal clear on these,
answering these questions for yourself will set you up to really hone down. The exact things you need to train on. And if you don't know your learners or
you don't know what they already know or what they're exposed to, send a survey, do
some informal coffee chats, and make sure that you're including a variety of roles. Grab front end engineers, grab security
engineers, back end, edge, network, you know, because it does take everybody. You need a representative
sample to, to really be able to understand your learner base. aNd sometimes it helps to
think about the flip side. So, like, where do I want them to be? If you're having trouble answering
that, think about what is the consequence if they get this wrong? What is the consequence if we don't
reduce the bill or add tracing in this next quarter in order to evaluate,
you know, Companies or whatever. Sometimes you can just flip the script
because you can get a little bit lost. In this wide world. So as a small, small exercise to
think about who our learners are. And so I can make the point that learning
and knowledge gaps are totally separate. Understandable and expected, no
matter your seniority when it comes to observability and monitoring,
let's maybe consider a few learners. We've got like a new grad, they are
probably like maybe first job, probably were exposed to logging at some point
in their education and maybe if they did an internship or something, but excited
to learn doesn't know where to start. needs both the knowledge and the skills. Kind of best case to have
somebody like excited to learn. Cause you will encounter resistant
adult learners sometimes. Even thinking about a senior developer
thinking about the background, did they work at a mega corporation where
there were so many teams that handled developer productivity and platform
engineering that they Are used to the amazing capabilities and benefits of
observability, but going to a smaller org. Oh, I like I've got to
add instrumentation. We don't have a wrapper library
that covers that is always up to date and covers what I need to know. Even with senior engineering,
it's tempting to say, oh, they should know what to do. Send them the docs, like, send them
the ticket, let them do the work. But, it really depends on where you've
worked and what you've been exposed to. If you've worked at a small startup, you
know that you've touched almost every part of an observability stack, from the
bill to setting up collectors, to doing instrumentation within applications. So really think through, yeah,
what people's backgrounds are. That's why this is so, like,
individualized and contextualized. It's why a generic 101 Like basic, basic
training won't meet everybody's needs because everybody's kind of coming and
bringing to the table like a different set of knowledge and like, you know,
by the time you're a staff engineer, I guess I would assume maybe you shouldn't
assume you've seen a lot of systems. You've seen what works. You've seen what doesn't work. You've seen, you know, You've seen the
rise of observable of observability within monitoring, and you probably got, like, a
lot of opinions on how things should go. That is awesome. And developing a training to
meet both the staff engineers needs and the new grads needs. Is probably a stretch. So you that is why we want
to think about our learners. However, I will say 1 of the tips is to
have once you've got a training kind of sketched out, you've got your 1st draft
having both a novice walk through it. And an expert walk through it and
kind of watching what they do kind of seeing where the stumbling blocks are. That is a very powerful exercise. So tap into that expertise
when it exists in your org. Okay, so when it comes to actually,
like, let's create our material, like, what is this course going to be on? Again, the reason I keep saying you've
got to scope it to, like, what do they actually need to do with this information? Because what I was making the 101
instrumentation workshop, Oh my God, all I had to cut so much out. I did not know how much I
wanted to include in there. And so I had to get really crystal
clear on at the end of this workshop. I want attendees to leave and be
able to bring open telemetry, tracing instrumentation into their own projects. I wanted them to be independent. I wanted them to be able to take this
knowledge and use it in Their daily life. So that meant , that was my guiding star. Anytime I, I was like,
should I put this in? This feels like it's too long. I went back to say, would
this help them independently? Instrument traces in
the future, yes or no? If no, cut it out. So grounding experiences in the real
world context, that is where you will have a huge leg up if you're
developing it for just your organization or business because you are sharing
like common organizational goals of. selling the product or the service
or whatever it is that you do. So you already have kind of a
shared context and community. You're all working within
the same tech stack. So while I had to make a choice of
like, what is going to be the most easy to read language minimal framework
that I could kind of take any, any developer and walk them through
instrumentation, you would get to say, Oh, we do go and Java, and these are our
frameworks and you can really create. The, like, dev environment and the
exercises to mimic what your developers would be doing in the real world. That being said, if you're developing
it for an org, I would say your best bet is to host an instrument a
thon where you have folks actually bring their real service that
you're asking them to instrument and working through it with them. Sandboxes and tutorials are Great. When you have sort of a wider,
more generic use case, but always get as specific as you possibly
can be and scope things down. So, you have a leg up if you're
working on one for your org. And then, again, like, what is
the absolute minimum, minimum setup and dev environment? I mean, I think I talk about it later,
but I really was torn on whether or not I should introduce the collector. Because you think about the
collector is this big component of OTEL, surely people are going to
be running into this in the future. Wouldn't it benefit them to
know, kind of, really that full path that telemetry takes? However, when I saw that the Jaeger all
in one image had a native OTLP endpoint, I was like, oh my god, Collector, bye
bye we only have two things to run. That is only two things to
have to debug if something goes wrong during the workshop. That is much better than
three, and it cut out a whole. You know, part of, like, configuring
the collector, running the collector. And it wasn't, my workshop wasn't
about production, production ready tracing system infrastructure. It was, how can you get traces today? And do you know what to do with them? So you, again, like, major benefits if
you're working with a group of people with a shared mission, working on the
same, like, system and tech stack. And then when it comes to
delivering, really tap into what already exists in your network. Like, yes, a standalone
training can do the job. But if your organization has communities
of practice or like sometimes they're called chapters, like chapter back end
or chapter front end times and places to exchange ideas and learn on the job,
tap into that and ask the organizers if you can host the next meeting and do the
workshop or get their help in advertising. Because with these organization
wide initiatives just sending one slack about a training is not going
to get many people showing up. Maybe you've got people who can
make it mandatory, that's cool, but forcing learning is also kind
of, comes with its own battles. So the second thing you want
to consider is the modalities. Lots of people learn different ways. A lot of us work in distributed
remote organizations. So you can't even count on being
in the same time zone as somebody. So make sure that you provide both
like a live guided session for people to, you know, that mimics more of
a classroom, self guided, but make sure that you've got office hours
for people to check in with you. And then, you know, you can
always record a live session and make that available as well. But having these multiple ways
means you're going to have. More luck getting more people actually
getting through this content, learning the things they need to learn, and doing
what Doing whatever you need them to do to increase system observability. So, I guess, like, to recap, you
want to, like, really think about what is the problem you're trying
to solve with this training. You've got to learn, you've got to
figure out where your learners are today. Where you then you've got where you
want them to go and then just really narrow that training gap and scope it as
small as possible for the best success. So we'll take a quick look at some of the
choices that I made for this workshop. And the 1st is. Do not reinvent the wheel. Like, I did not start with a
blank page and I said, okay, instrumentation, let's go. Like, no the beauty of working with
open source and working with OTEL is that my friends, like, Reese has
fabulous, like, I look at Reese's metrics workshops all the time. And the talks that she's
done and Adriana, like. Everybody across the vendors and
our open source community members have already contributed a ton of
interesting tutorials and knowledge, and it's really about shaping and
scoping that down for your use case. And yeah, making sure that it fits and so. You're not starting from scratch. You weren't hired to be a teacher
or instructional designer. Please borrow. Particularly the way that we,
that folks organize information. You could take my Python flask workshop
and totally rewrite it in whatever language and framework you want,
while keeping the same structure and sort of curriculum and lesson flow. Because that's where I
spent a lot of my time. So it doesn't need to be a
cut, copy pasta thing, but it's really like, Use what exists. This is the beauty of having an
open and sharing environment. The other thing is vendors often have. Provide training on their
specific platform and products. What I will say is sometimes if you take
those trainings, you're introduced to all of the features and all of the products on
the platform that your org maybe doesn't even pay for or use or has interest in. And so that can contribute
to learners being like, this synthetics turned on or whatever? And so I think. Borrowing the curriculum, borrowing the
phrases, the links, the resources, how concepts are mapped out one by one, great. And if you, I mean, if you're
all in on one platform, go ahead and use the vendor training. But that is just my, my
word of advice there. So, what was the problem
I was trying to solve? I believe tracing is an
underutilized telemetry type. And I think a major
barrier to implementation. is purely getting useful data
out, getting to that complete trace as a starting point. And so in my opinion, the best way to
tackle that was to teach application developers, because a lot of us
in ops and a lot of us in SRE have been talking about tracing forever. It's the app devs we've got to reach. They're the ones we need
to do the instrumentation. So that was My guiding light app,
getting app devs to instrument traces and actually use trace data. My learners were apt as
interested in open source who are running cloud native systems. I think tracing is useful. Always? Well, I shouldn't say always. I think tracing is very, very helpful
no matter the size of your system. However, specifically working
at KubeCon and CNCF I was targeting cloud native systems. And what did they already know? I did not have the benefit of having
access to my attendees ahead of time. And so, the assumptions I made
were that they were likely familiar with metrics and logs. That they might have had exposure
to APM, application performance monitoring, and that they were curious
about tracing in OpenTelemetry. Because no one signs up for an
OpenTelemetry workshop if they don't know what it already is,
even at like the highest level. So that's what I started. How did I scope down? What was our minimum, like,
local dev environment? I chose Flask and Python. Python for its very welcoming community
on just like as a language as the whole. Flask because it is a framework that
doesn't do magic stuff behind the scenes. You don't really need to know the
ins and outs of Flask in order to, to just like look at it. It's a very basic like web app. And If learners wanted to continue
on and maybe, like, extend the workshop, the Python, specifically
the Python OpenTelemetry cookbook section and the documentations
for the Python Instrumentation Libraries or Tracing are excellent. So I knew if people wanted to go
further, that, that those resources would be available to them. Obviously, OTEL APIs and
SDKs for instrumenting. And then, yeah, where did I want to
store and visualize these traces? Well, this was a workshop focused
on local development of traces. So, the Jaeger all in one where
you're holding those traces in memory was a fine Fine, totally
acceptable use case for this. We were only going to be generating a
few requests at once and kind of, it was mostly building up the feedback
loop of adding instrumentation code, running the services, verifying that
the data matched what we wanted, and like over and over again. So, We didn't need to hold
stuff long term, so JaegerFIT. And because this was an open source for
open source conferences it needed to be all open source up and down the stack. So JaegerFIT, although I'm really excited
to see some other, I think is it, hotel desktop viewer, I hope is getting revived. I, I see murmurs of that. I, I would like to have lots of
options but this is what I went with. And then. I kicked off, it feels silly, but you,
I always kick off with a definition of observability because I think if you
asked like five developers to define it, you would get 10 different answers. Actually, I think you'd get more
than five different answers back. And so when you're. conducting this training, it's important
that you start with like, these are the terms we use, this is what it means
for this org, or for this project, or this is what they mean here. You may have a different idea,
let's talk about that, but like, for this session, here's where
we're, here's where we're grounding. Doesn't need to be long, literally one
sentence definitions, we don't want to overwhelm or bore people, especially
at the beginning of a training. And then from there, I had
talked about my big debate, do I include the collector, do I not? Here's what I decided to do. I thought it will serve
people to know about it. I'm going to include the big
OTEL diagram from the docs. Again, doc site showing up here. Love it. It's not a knock on the doc site. We just got to help people learn
where to go to find the info. So I talked about the collector briefly. I kind of said, here's where it sits
in the overall OTEL, like kind of architecture and the project landscape. Here's when you would use it. Today, we're going to be using we're
using a more simplified version where you don't, it had, the purpose of putting
the slide is they know what it is. They can connect it to some
other ideas within OTEL. And the next time they hear it in the
wild in a conversation, they go, Oh, okay. It was like the pro, you know, we
can send telemetry data through that. That is a fine place for beginners to be,
especially app devs who are likely not going to be like tuning collector configs. And so the hardest thing I
think to do is to introduce new concepts and skills one at a time. Because if you've been working for this,
with this stuff for a while, you have like the cursive knowledge where you just don't
even know what it's like to be a beginner. You don't even know what would be a
fire hose of information versus like this beautiful, nice breadcrumbs. So, like, if you think back to
your first day on the job, you probably, your job you probably had. HR benefits, then IT laptop setup. And then maybe like a session with the
CEO about the history of the company. And then you're like with stuff to lunch. And then by the end of the afternoon,
you finally get to your laptop, you get to your desk and you've got like
a hundred emails and you're like missed meetings you didn't know about. And like, all of that is just so
overwhelming when you're getting started. So really, really focusing on
just one little concept at a time. Like also should be a guiding principle. So the way I broke instrumentation up,
I looked at a lot of different tutorials and I even got, I will admit I got a
little bit confused because I would be looking at the same tech stack that
they were trying to instrument and the code samples would, would kind of vary. And I. I looked at a bunch and I said, what
is this, like, missing concept here? What is this missing link? And what it turned out to be was people
were up front deciding whether they wanted to do automatic, programmatic, or manual
instrumentation without explicitly saying, hey, this is what I'm doing and why. And so that meant if you were to
just take one of those tutorials that maybe did all automatic, you might
be really confused when someone asks you to manually add a span attribute
because you were like, I, the hotel agent is like wrapping my service call. Like it's doing everything. What do you mean? And so that for me was the, that was the
gap that I wanted to fill is to know when and where to use automatic programmatic. And manual and there's no like bearing
the lead, like show everything up front. And this is in module one. I'm like, here's automatic
programmatic manual. Here's the differences. No surprises. aNd one note on the automatic,
it is really nice to get a quick win in very early for learners. I decided to use for automatic
instrumentation, just the console span exporter. Because for a lot of these folks, it
was their first time even like, Thinking of a span, knowing what a span is and
the textual representation I thought was kind of nice to look at and become
familiar with what I could have done was like, put up an example span and
like, blah, blah, blah, lectured through all the trace ID and parent ID or. We could set up auto instrumentation,
they could get their first span in front of them, and then I could
say, hey, do you notice this thing? And then they're looking at their
laptop, they're engaged, it's their data. This is sort of the aha
moment I'm talking about. We don't want to lecture at people, but
we want them to discover on their own because that just goes so much further. We, we do learn by doing. Programmatic manual. So the other thing I did
was break up how and why. So after we, we do the different, we do
automatic, we move on to programmatic. And once we have traces that have
multiple spans, like the textual representation, like techno we got to
start looking at this in a waterfall. So I took the time to do a quick tour
of Jaeger, of each of the different visualizations and kind of talk through,
here's how you analyze them, here's what you're looking for, here's how to
search and filter and I ended that how section with this slide on why, because
traces I think are very different from metrics and logs, and so I was like,
Why do we have so many visualizations? Why did I just show you like 10
slides of different ways that you can interact with and manipulate this data? And it's like, well, the power of
tracing, you know, the zoom out, the zoom in, the telescope, the microscope. But combining, separating, but
following up the how to with the why was a really key component for
people's like light bulbs to go off. So, with that, I wanted to share a few
more resources and then kind of dive into hearing what training needs y'all have. These two books, highly recommend,
Design for How People Learn. It is hilarious, it is funny,
it is a book on learning that, like, It is not boring at all. She talks, she walks the walk
in this book as well as better onboarding from a book apart, which
is also a fantastic publisher. When with all of the talk about
internal development platforms and platform engineering and treating
your platform like a product, like. Let's just borrow the good books
they're using already, like, that are onboarding and think about how to bring
that into onboarding to observability. Open observability resources. I love that the OTEL Docs have a specific
section that's like, Are you a developer? Like, and you want to learn more? Start here. Versus, are you ops? Start here. Like, that really speaks to who,
knowing who the audience is. The CNCF Glossary. It's helpful to have bookmarks. Sometimes people ask you about acronyms
and maybe you don't remember or you want sort of an official resource
to turn to that one is nice, plain text, like small, like it is just very
plainly defined and then finally while my workshop Not real world, right? It was a very small Flask app. It had three endpoints. If you wanted something more
realistic to look at, the OpenTelemetry demo is your choice. It's got, I think, I
believe all the languages. It's, it exercises almost every
part of OTEL that is like GA now. Super helpful resource. That would be the one that I would use
if I knew what hardware my learners had. Cause it was a little bit of a
mouth breather last time I ran it. Okay, and then learning experiences. So there is the tracing workshop that
I gave at KubeCon is self guided. It's up, it's on GitLab but you can, it's
set up as like a slideshow, so you just kind of work through it at your own pace. There's a recorded session, which
is sort of where I'm teaching the workshop, and I'm able to use more
words than I put on, on the slides. And then sort of related, I developed a
different learning experience for on call onboarding when I was at LightStep, and
I presented on how and why to do your own on call onboarding at SREcon last year. That is a great talk, and it is a
practice that has evolved to multiple companies past LightStep, so it has
kind of proven itself out in the world. So I believe we are Yes. Gotta do my attributions. Thank you to slides. Go for the slide templates, flat
icon and free pick and story set for all of the beautiful things. I am not an artist. I'm not a teacher, , I'm just a
developer advocate who wants people to trace more things, . So with
that, I'm really curious to learn. Does, does this resonate with folks? Do you, do you have training needs today? Do you want to talk through
some tactics or ways to learn your, about your learners? Let's talk. I actually have a couple questions, Paige. The first is, are you able to
share, do you have a shareable copy of your slide deck? Yes, let me. Our Google workspace is really locked
down, so I will need 5 minutes after this meeting to get that over to you. But yeah, no worries. And then I was also curious, how
do you measure results or, like, what are some strategies to measure
results from your workshops? Yeah, so my workshop in particular, I
looked at the attendee feedback and I talked to folks afterwards and especially
the folks that had raised hands and had questions or hit a stumbling block. I wanted to make sure because
somebody had an issue PIP installing something in a virtual environment
and it was like, not something I'd seen before and it was not something
I could troubleshoot on the spot. So I walked them through. Okay. This is what I was
trying to teach you here. Here's another way that
you can get at this. What else would you, what
do you need to go forward? So there's a little bit of that
personal one on one and then the, they send out a survey. And so I always look at survey
results mostly not the numbers. Not a social scientist. I know people like the Likert scale,
but I really care more about what people took the time to type and say. And so folks had said, like,
this was a great introduction. This was my favorite tutorial. Like, thank you so much. And so I'm like, okay, we did good. If I was developing this for my company,
so say say you have an initiative that you need to re instrument
away from proprietary onto hotel metrics by the end of next quarter. Okay. So what you where you want your
learners to be is to well, what you want at the end of the day is maybe. All of your services
instrumented with OTELmetrics. Cool. What's standing in the way? Where are your learners today? Well, half of them, half of them are
using Vendor A, the other half are on Vendor B, and then maybe the ops team
is, like, secretly running Prometheus somewhere, and you're like, oh my god. So, in that case, I would say, like,
okay, well, for the Prometheus folks, There's like a bit of education to do
with the interoperability between prom and hotel metrics and kind of talking
through which approach do we want. Do we want to use the pull based
or do we want to do the push based? That is kind of the training
and the knowledge and the skills that we need there. For each of the vendors, like I do
think it is helpful to have this is how you would do it in vendor A and
this is how it needs to be, this is how you need to change your behavior. Sort of a Use this library, not that
library, the contrasting from where they are in the context of what they know to
here's the hotel metrics like cookbook for, oh my God, the cookbook for Python. Here's the, it'll go away. Here's. And even a really basic like primer
on metrics again, because I, even with like, yes, observability is great when
we talk about monitoring, really, we talk a lot about metrics and thresholds
and alerts, and that is still an area that I see is like under serves as we
like through the page at the developers and ran away, we like kind of forgot
to teach them all the stuff we learned after years of like fighting with
incidents and trying to understand our systems better and measure them. So I think in that case. Yeah. Yeah, I would just really get as
specific as you can on what these groups would have in common, and
then map from there to the goal. So I would measure the success of like,
okay, two weeks after the workshop, or one week after the workshop,
how many PRs did I see get through? How many services? Either started their re instrumentation,
finished their re instrumentation. I would kind of use that to track
the progress of the project. Which is sort of the lagging indicator
of like did they learn the thing or not. Yeah, but those are great questions. Thank you. Do you have a favorite training that
you've, you've held or you've led? Do you want to share how,
like, I love your metric stuff. So you want to talk a little bit
about how you made choices there? I mean, so it's interesting
because I did the metrics. I did a metrics talk twice, and so I
changed up the second, change it up the second time just based on like,
you know questions that people had and stuff that I had wanted to kind of
put in but didn't have time or hadn't quite figured out how to put into it. But, you know, I think what you're
talking about is not applicable just for workshops, but like really
anything that involves like a wider audience, because, you know, I think
I frequently am like, Oh, you know, what kind of level do I need to assume
that people are at so that I know. Yeah. And, you know, you can make like
general assumptions about, you know, okay, well, this event, you
know, whatever, but sometimes it's. Yeah, I don't know. Sometimes you just guess and hope
if it's the most people, you know, sometimes, yeah, there'll be like one
or two people that were like, oh, this was like way too beginner or like two
people that would say the opposite. Like, this is, you know, way over my head. And yeah, that's I think scoping
like, does it need to be novice? Does it need to be mid level where
I assume some things or am I talking to the expert that probably wrote
a system like this in the past that it is you can't stretch one training
to fit all those groups for sure. Yeah, I know. And yeah, I'm, I'm always like, I feel
like on the verge of, oh, I want to, you know, because I always appreciate, you
know, people who explain things very well. And so trying to, you know, fit that
for the people that are there, but also like not wanting to piss them
off, but like, you know, kind of have to be like, oh no, this is like,
this is more basic than I wanted. So yeah. Yes, absolutely. Yeah, it's hard. And I, when I write blog posts and
stuff that people who edit are always like, you don't need to include
the whole history of observability. You could kind of just
like, start with your topic. I'm like, well, people still don't know. You know, I work a lot of booth
duty and I can go, oh, you know, are you happy with, you know,
observability at your company today? And they go, what's that? And I'm like, yeah. Okay, all right. Let's start up. Let's start at not the beginning,
but let's start at do a monitoring. Oh, okay And yeah, just finding those
ways to to meet people where they are because we do use a lot of insider
academic terms telemetry There's just no shortage of them in this in this space. So yes, I and I do think the The
quality of the questions that you get asked maybe in your Slack help channels
can really tell you if your training was a hit or a miss because if you're
continuing to get, Hey, is this random JavaScript library instrumented with OTEL? It's like, I don't want to be rude and
like point you to the registry, but also like, did you take the training? Making sure you track who takes, takes
the training is also huge because I have been on tiny teams that have kind of
manpowered through migrations and we would get developers kind of treating us like we
were the owners of their own CI pipelines. And we would say, Oh, so and so we noticed
you haven't taken the training yet. I totally get why, you know,
this is a confusing thing. Why don't you check out lesson two? Here's the link. And then it's like, Okay, this is,
we're, we're, we're negotiating the boundaries of responsibility
between operators and developers. I think we're still, even though like
DevOps movement has, we're like many years past that, it does still feel like
we are negotiating these boundaries when it comes to monitoring and observability. No one team should be in charge of this. You should be the, as experts, you
should be the advisors, the consultants, the guides, but not The, like, total
tyrannical, like, owners of the thing. It's exhausting to be
responsible at that level. So, yeah. Or does anybody have good trainings
that they've taken that they want to share or, uh, ideas for courses? I'm, yeah, like Rhys said, sometimes
we can get in our head about, like, what do people even want to know? Go ahead, Dan. Hi, thanks. And thanks for the talk that
resonated very well with me. Sort of just on your last point,
specifically, I was going to ask. So, so 1 of the things. I think we struggle with is like this
ownership boundary of, of we provide some training or maybe not even training. I don't know if we do that. Well, but we teams are like,
we need observability in our, in our app or not even our app. Like, I'm a team that owns a framework
that dozens of teams that my org uses and we help them implement. Sort of, you know, tracing
let's say at the root of that. So the app developer
doesn't even need to know. But then like, you know, a month
passes, three months passes and they, something's not working properly,
they want to add something and they're always like looking to us to be the
ones to like do the work or, or, or, you know, again, advising them is my role. So it's, it's like, that's okay, but
like, I, I just feel like they don't really end up ever taking ownership. Like it's a, it's a common pattern. And I guess what I'm asking for,
or opening a discussion on is, is just, like, how would you drive
the connection between, like, the training and the knowledge transfers,
et cetera, and then, like, defining where that that boundary lies because. I always feel like people treat
observability as like a third class citizen when I feel like it needs
to be their first class citizen. Like, we get all these incidents,
the directors talk about it, et cetera, but they don't take the
ownership at the end of the day. So I'm just curious about
your experience in that. Relationship. I'm hoping somebody on the call has
experience working at a like midsize or larger companies because unfortunately
I have been at startups where I didn't I have not had like a director of SRE
or or really even like, I do think it. Comes down to engineering
leadership needing to explicitly like, say, here are, here is what
platform or ops or SRE provides. And here's what you're responsible
for sort of like the, what is it? The cloud security, the shared
responsibility model between the cloud provider and you like,
and yes, there's like the fuzzy boundary in the middle, which is
where you would do some consulting. But I, I have not been able
to successfully win the owner, like get ownership. Successfully established because of
the kind of the nature of the companies I worked out, but I'm really curious. Like Adriana, I know you've worked at some
big shops, you've seen a lot in the past. Yeah, yeah, I mean, I can say that like
from personal experience, like I worked at an organization that was like, they
hired me in to do observability, like to lead an observability practices team. And yet when it came time to like,
okay, let's get the developers to instrument their code, they're like, huh? Why can't you do it? So it really, and then similarly, like or,
or I should say an opposite story to that. We had last year Iris De, De
Mirschi who she was at Farfetch. I forget where she's at now, but
she was talking about how she came from an organization that was an
observability first organization. And. They're like, because executives,
like, mandated observability and that, you know, their team wasn't
responsible for for instrumenting code, even though, like, she was, she was
part of an observability team, like, they were helping with practices. They were like, managing infrastructure,
like the collectors, but. But application instrumentation was
to be done by the application teams. And so it was a very different
sort of outcome as a result, right? Because it's almost like,
what are you going to say? Like, leadership has basically said that
this is the way you're going to do it. So that's the way you're going
to do it compared to where I was at before, where I was at before. I was trying to shape what
observability for the org looked like, but unfortunately, leadership was
like, they kind of half dipped their toes into the observability water. So they're like, eh, not really. Oh no. Does this mean we all need to get
promos to engineering leadership to make observability happen? Oh no. Or be very persuasive. Do you feel that like, I hear what you're
saying, but like, I also feel like. In the spirit of the goal of
observability and the goal of like pushing these responsibilities downward. It's like this. These top level mandates are really like,
sure, maybe the team will do it at the end of the day, but they're never really. They're never really
like, caring about it. Like, do you think those
2 are like competing. You have to have a convergence
at the end of the day, right? Cause like you need the mandate from
the top, but like, you have to be, you have to have the folks willing to do it. And I think like to Paige's points in
her talk, like, you know, having people who are excited about observability
and, and having a proper training program in place as well to get the,
you know, the individual contributors, the ones who are, who have an actual. Stake in this who are, who are going
to be doing the work, like, because if you don't, if you don't have like that
convergence from top and bottom, like it's just going to be a half assed thing. Yeah, go ahead. Yeah, I was just going
to chime in quickly. So the one experience I had or the recent
experience that when, when, when teams start facing issues, like when, when they
are trying to figure out one particular issue, they are fixing like the incident. I guess like even in not in each day,
but they are trying to find a particular. Issue with the application and
then they need help, right? Like they don't know they haven't
done the training or I don't know how to use the observability tool. I think that I kind of use that as
a leverage, whether then have you done your have you instrumented
your application correctly? Have you added the correct labels
on your on your telemetry data? And then having having to like having
used that kind of work as well. Like, Okay, you want something that
you want to have with identifying or figuring out this issue. I also want you to do your part as well. Make sure that you have done your part. Then it will make it make it easier. So I think that was one
tactic used in the past. Yeah, I think, like, from what I'm
hearing so far we I had similar experience in my previous org. We were building our brand new platform,
and luckily it was all written in Java, which meant that, like, we
just kind of utilized the Java Auto Instrumentation, built out the kind
of generic dashboard and had all that kind of semantic convention baked
into it which meant that like all of the telemetry Was easily identified. And and we went just like we just went
in all the application and then because it was not that much effort on our part
to then make that change rather than Like manually instrumenting everything and
then we had other teams which are like all the services were returning lambdas
and goes in that case, like, yeah, I had, like, nine months project with them
trying to kind of pursue them and slowly, like kind of building set of all kind
of POC and like, based on the water. The extension layer building out like like
custom version of that all configured. They like just add this layer. At least that part is sorted for you. But then you just have to do the
instrumentation part on your. So, yeah, I guess it depends on the
situation, but it's a mixed bag. Yeah, Dan, it sounds like you've
already got you're working within sort of that entrenched pattern where
you're already seen as the owners and that maybe like you've been able to be
able to do these tickets for them in the past, but now you want to change. I remember 2 things I've tried 1. We'll do this 1st 1 together. We'll pair on this. Then you will know and this will be great. Or I find an example PR that's like
exactly like instrumenting the, whatever the counter or the gauge you need. And like here, use this as a guide. So it, it is hard to come out of a
already established pattern like that, but DoorDash did a talk at KubeCon about how
they rolled out service mesh and sort of the challenges with giving people out of
the box dashboards, I can find that and put it in the slide deck they would be
great to talk to cause they kind of had a similar problem of being the owners. But we're out of time. Oh my gosh, that went by quick. If you have any more questions
you can reach Paige on the socials that she shared, or you can just
search Paige Cruz in CNCF Slack. We will have this recording edited
and up, I think, hopefully in the next couple weeks it'll be on the
OpenTelemetry YouTube channel. And Yeah, it's called OTEL Official. Yes, so, you know, it's official real. Yes. Give it a follow. Give it a follow so that you
can get all the latest updates. And yeah, thank you all so
much for being here Paige. Thank you so much. This was like really great. I love your slides. I screenshotted a couple. And it's all, I all work out
in the open, so take, borrow whatever you need, adapt, extend. Let's bring more people to tracing. And please, yeah, email me and
get in touch if you want to talk about this stuff more. I have spent a lot of time, a
lot of time thinking about it. Awesome. We will see you all next time. All right. Thank you.

