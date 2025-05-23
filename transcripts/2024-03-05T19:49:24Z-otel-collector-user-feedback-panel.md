# OTel Collector User Feedback Panel

Published on 2024-03-05T19:49:24Z

## Description

In this panel presented by the OTel End User Working Group, Adriana Villela asks end users to share their thoughts and ...

URL: https://www.youtube.com/watch?v=LL8v_B417ok

## Summary

In this YouTube video, a panel of OpenTelemetry (OTEL) collector practitioners discusses their experiences and insights on using the OTEL collector. The panelists include Adriana Villela (the host), Iris (a senior observability engineer at Miro), Juraj Michalik (a senior logging and monitoring engineer at Swissery), Greg Eales (from Ocado Technology), and Joel (from Open Systems). The discussion covers various aspects of the OTEL collector, including usage, deployment challenges, debugging difficulties, scaling strategies, and desired features. Key points include the importance of debugging tools, the need for better handling of metrics, and the desire for specific features such as profiling and a Prometheus remote write receiver. The panelists share their experiences with scaling the collector using Kubernetes and HPA, and express a collective wish for the tool to mature and improve in usability. The session concludes with an invitation to an upcoming KubeCon event where further discussions will take place.

# OTEL Collector Panel Discussion Transcript

Thank you everyone for joining. This is a really great turnout, and we're excited to have assembled this panel of OTEL collector practitioners. One of the missions of the OTEL and User Working Group is to collect feedback on OTEL to deliver back to the SIGs. This started because Judah C, who works in the OTEL collector SIG, reached out to us to put together a survey to collect some information on the OTEL collector to see how it's being used and drive the roadmap and vision for the collector in the near future. We also thought it would be beneficial to have a panel for a lively discussion with a handful of OTEL collector practitioners.

## Introductions

Let’s introduce the panelists. I’ll start with myself. My name is **Adriana Villela**, and I work with Reese and Dan in the OTEL end user working group. Our group numbers are growing, which is exciting. We’re hosting this event today.

**Iris**, would you like to introduce yourself?

**Iris**: Hello everyone! My name is Iris. I'm a senior observability engineer at Miro. I've been working with OpenTelemetry for a little over a year now in two different companies, giving me a lot of experience and use cases, as my two experiences are completely different from each other. I'm happy to be here. Nice to meet you!

**Adriana**: Thank you, Iris. Next, we have **Juraj**. Did I pronounce that correctly?

**Juraj**: Yes, you did! Hi, my name is Juraj Michalik. I'm based in Madrid and recently started working for a company called Swissery in the insurance space. Before this, I worked for two different companies where we used OpenTelemetry. In the last one, we migrated fully to OpenTelemetry for the collection of logs, metrics, and traces. I'm a Senior Logging and Monitoring Engineer in my current role.

**Adriana**: Awesome, thanks! Next, we have **Greg**.

**Greg**: Hi! Can you hear me? My name is Greg Eales. I work for Ocado Technology, which started as an online supermarket and now sells online supermarket technology to other supermarkets. My team has been using the collector for just over a year, but I've only been on the team for less than a year.

**Adriana**: Great! And finally, we have **Joel**.

**Joel**: Hi, I'm Joel from a company called Open Systems. We're based in Switzerland but have a global presence with offices in San Francisco, London, and Germany. We offer managed SASE, which includes managed connectivity and VPN for our customers. I'm on the observability team, responsible for ensuring we get telemetry from our 10,000 devices worldwide. We have also started dealing with data from Kubernetes, like Prometheus metrics and logs. We’ve been using the collector for just under a year and have quickly decided to migrate everything to it as we’re consolidating different service teams.

Thank you all for joining us. Let’s get into the questions!

## How Are You Using the Collector?

**Adriana**: First things first, let's start in the order in which folks were introduced. Iris, can you tell us how you and your team are primarily using the Collector?

**Iris**: Sure! In my current company, we are using the Collector mostly as a transport layer. We have already migrated traces and are in the process of migrating logging and metrics. In my previous company, we were more advanced; we used the collector itself and the operator. Currently, we’re only using it for deployment, basically transporting from our legacy components while slowly moving to collect everything through OpenTelemetry Collector. We also heavily used the presets offered by the collector itself, running it as a daemon set in our Kubernetes cluster. Our goal is to have the collector take as much of the collecting of information as possible, moving away from legacy solutions like Jaeger and Prometheus.

**Adriana**: Great! Juraj, how is it that you and your company are using the collector?

**Juraj**: In my current role, which I just joined this month, we’re just starting with OpenTelemetry and traces. In my previous role, we were a SaaS startup that migrated from a vendor's proprietary collection pipeline to OpenTelemetry. We did a proof of concept for alternatives and settled on a self-hosted solution based on the Grafana stack. We used the collector in a Kubernetes deployment, utilizing daemon sets for collecting logs, metrics, and traces from everything running on the nodes, and also deployed it as sidecars for various services.

**Adriana**: Thank you! And Greg, how about you?

**Greg**: We use the collector for traces. We had a legacy system called request viewer, which was based on logs. We’re migrating to use the collector for sending traces. We do some processing and sanitization, adding attributes and doing tail sampling. We don’t do much with metrics beyond gathering our own metrics from the collector and forwarding them to Grafana through Prometheus remote write. We deploy it in ECS, and we have one central cluster that scales with the load of the collector.

**Adriana**: Interesting! And finally, Joel?

**Joel**: We have collectors deployed on all our hosts, acting as egress gateways for telemetry. The primary data we’re shipping is log data, but we have pipelines for metrics and traces as well. Most of the applications are not using traces yet, so we’re mainly using it as a log telemetry mesh and laying the groundwork for future migration. We have egress collectors running on our hosts and an ingress collector in our central Kubernetes cluster, along with multiple layers of collectors for different backends like Loki and Thanos.

## Collector Distribution

**Adriana**: Thank you all. Next question: are you using a vanilla collector, collector contrib, a custom-built one, or a vendor distro? Iris?

**Iris**: We’re using the vanilla one. So far, we haven't had the need for any custom builds, as the vanilla collector works great in our case.

**Adriana**: Same question, Juraj?

**Juraj**: We use a variety of custom distributions. We've built multiple custom distributions to minimize the size of the binary and the number of components, especially from a security perspective. Everything is based on the upstream OpenTelemetry collector contrib with custom configurations.

**Adriana**: Great! And Greg, what about you?

**Greg**: We build our own. We forked the contrib repo and based our version on that. We had specific features we needed, like adding ECS CloudMap service discovery to the load balancer exporter, which we contributed back to the community.

**Adriana**: And Joel?

**Joel**: We are running our custom build. The reason is that we have service teams who built their own processes, and it was one of the big draws for adopting OpenTelemetry. We use the builder and had a good experience getting it running in our build pipelines.

## Challenges with the Collector

**Adriana**: Moving on to challenges, starting with Iris, what’s the biggest challenge or challenges you’ve faced with the Collector?

**Iris**: Debugging is definitely a challenge. Deploying it is pretty straightforward, but debugging can be overwhelming. I had a situation where I was using the collector with ingress for the first time, and it took my coworker and me over two days to figure out an issue with passing the right paths. The debugging logs did not provide enough information, and we ended up deep in the code before we found the solution.

**Adriana**: Juraj, what about you?

**Juraj**: We ran into bugs that were hard to debug, especially under large loads. We had to build our own distribution with a debugger to see what was happening. It’s challenging to test complex pipelines without deploying them to full-blown environments.

**Adriana**: Greg?

**Greg**: Our biggest challenge has been the quality of the platform we provide to the organization. There have been bugs or misconfigurations causing traces and spans not to be available when users looked for them. Initially, there was also naivety about the collector’s reliability, and it caused anxiety among the team.

**Adriana**: And Joel?

**Joel**: I echo a lot of what has been said. One challenge is the handling of cumulative metrics. We heavily rely on logs, and there’s no general way to generate metrics from logs within the collector currently. This is something we’re working on internally.

## Wishlist for Improvements

**Adriana**: What’s on your collector wishlist for feature improvements? Iris?

**Iris**: I'm looking forward to profiling. I’ve seen some promising improvements and I believe it will be groundbreaking. The collector has been very complete for our use cases, so I’m excited about the future developments.

**Adriana**: Juraj?

**Juraj**: I’d like to see improvements around reducing network usage, like what Apache Arrow is promising. There are also some bugs that need fixing, especially around the gRPC layer.

**Adriana**: Greg?

**Greg**: I hope the collector matures more. I want features like a dead-letter queue for exporters and better handling of service discovery to avoid split traces when scaling.

**Adriana**: And Joel?

**Joel**: I would like to see a Prometheus remote write receiver. Additionally, a general connector for creating metrics from any telemetry would be beneficial.

## Scaling the Collector

**Adriana**: Lastly, let’s talk about scaling the collector. Starting with Iris, any feedback or pain points around scaling the collector?

**Iris**: We’ve used the HPA effectively for scaling, and in my previous company, we also explored KEDA, which worked well for auto-scaling based on queue size.

**Adriana**: Juraj?

**Juraj**: For our deployments, we also used HPA based on memory and CPU, and we looked at VPA for daemon sets.

**Adriana**: Greg?

**Greg**: We have a conservative auto-scaling policy based on memory as the tail sampler holds a lot of memory. We haven’t put much effort into optimization yet, as we’re focused on processing data properly.

**Adriana**: Joel?

**Joel**: We run everything on one cluster per environment and have been using HPA with no issues. I need to talk to Juraj about gRPC issues we’ve encountered with scaling.

## Conclusion

That brings us to the end of our panel discussion. Thank you to all our panelists for sharing their insights on the OTEL Collector and how you use it in the wild. This is incredibly valuable. Thank you to everyone else who joined today as well. 

Don’t forget to check out our OTEL YouTube channel for the recording of this session. For those attending KubeCon in Paris next month, many of us from the OTEL end user working group will be there. We’ll have various activities lined up, including user feedback sessions, demos, and more. Keep an eye on the OTEL blog for further details.

Thank you all for your time, and we hope to see many of you in Paris!

## Raw YouTube Transcript

Thank you everyone for joining. This is a really great turnout and
we're excited to have assembled this panel of OTEL collector practitioners. So one of the missions of the OTEL
and User Working Group is to collect. Feedback on OTEL to
deliver back to the SIGs. And I think this started because, Judah
C, who works in the OTEL collector, SIG, he reached out to us to put together a
survey to collect some information on the OTEL collector, to see how it's being
used to sort of drive what the, what the roadmap and vision is going to be for
the collector in the next little while. And then we thought, well, Okay. You know, let's extend this and
also have a panel and have a nice lively discussion with a handful
of OTEL collector practitioners. So here we are. So, why don't we introduce the panelists? I'll introduce myself 1st. My name is Adriana Villela. I work with Reese and Dan in
the OTEL end user working group. Our groups are, our numbers are
getting a little bit bigger. So I'm, I'm very excited to see that. and, yeah, so we're,
we're hosting this event. let's go over to our panelists. I'm going to, I'm going to pick names. Iris, how about you go first. Hello everyone. My name is Iris. I'm a senior observability engineer
at Miro and I've been working with OpenTelemetry for a little bit more
than a year now, in two companies. So I have a lot of experience and use
cases, that I've worked because the, my two experiences are completely different
from each other and I'm happy to be here. Nice to meet you. Thank you. Okay, next we have, Juraj. Did I pronounce that correctly? Please correct me if I'm wrong. So, hi, my name is Juraj, Michalik. I'm based in Madrid, currently working
very recently for a company called Swissery in the, I guess, insurance space. And, Before I worked for like two
different companies where we used, in the last one in the, in the older
one, although very sparingly and in the previous one, we basically
fully migrated to open telemetry for collection of logs, metrics, and traces. And, I'm, Senior Logging and
Monitoring Engineer in this current, in the current role. Awesome, thanks. next we have Greg. Hi, can you hear me? my name is Greg Eales. I work for Ocado Technology, which is
started out as an online supermarket and now sells online supermarket
technology to other supermarkets. we've been using the collector
for over a bit over a year, my team, but I've only been on the
team for a bit less than a year. Oh, awesome. And finally we have Joel. Hi, I'm Joel. I'm from a company called Open Systems. We're based in Switzerland, but we
have a presence sort of say globally. we have offices in, San
Francisco, actually. I've never been there. Also in, I think, London and Germany. So this is where we're based. But, we offer managed SASE. So managed, connectivity
and VPN for our customers. And I'm on the observability team. So I'm responsible for making sure that
we get telemetry from our devices, which we have 10, 000 of, All across the world. and also we're now having to deal
with, data coming from Kubernetes. So met, you know, Prometheus
metrics, logs, all this nice telemetry, which we need to handle. we've been using the collector
since about a year now, I think just under a year, I would say probably
April last year was when we started. and we've really underground. Yeah, we really decided very quickly that
we want to fully, fully migrate everything to it because at the moment we kind
of had a big mass of different service teams doing things in their own way so
we're kind of consolidating everything now and we found that the collector
and open telemetry in general was a very nice way which we could do that. Awesome, well thank you again
all of you for for joining us. So let us get into the questions. So first things first, and we'll
start, let's Let's start in the order in which folks were introduced. So, Iris, how about you start with
telling us how you and your team are primarily using the Collector? Okay, so, I could talk a little bit
about how we're using it now and in my previous company as well, since, I,
I am very new at my current position. But we are using the Collector
mostly in my current company mostly as a transport layer at the moment. We already migrated traces. We're in the process of
migrating logging and metrics. In my previous company we were
a bit more advanced than that. We were using the collector
itself and the operator. Currently we are only using it
for As a deployment, basically all it's doing is transporting from
our legacy components and we're slowly moving to collect everything
through OpenTelemetry Collector. and in the past we actually, used
the presets a lot, the presets that are offered by the collector itself. So we were running it as a daemon set
and the collectors were collecting everything, especially in our
Kubernetes, Kubernetes cluster. So that is the goal right
now to have a collector. take as much of the collecting of
the information as possible and get rid of the legacy ones like
Jaeger, for example, Prometheus. Awesome. same question, Yudai, please. how, how is it that you're, you and
your company are using the collector? So in this, in my current role, which
I just joined this month, they're just starting with open telemetry and
traces in general, but in my previous role, we basically, it was a SaaS, a
SaaS, startup where early on, there was some concern about the costs. So one of the things we started to work on
was migrating from a vendor's proprietary, collection pipeline and client libraries
to open telemetry, which then enabled us to do a POC of other alternatives, where
we basically just use the concept of the pipelines to take the data we were already
gathering and just send it to a different vendor and also a self hosted solution. It was mostly, we ended up settling on the
self hosted solution, which was basically the Grafana looks good to me stack. So hosted in, in Kubernetes, the
way we are on open telemetry, there was a couple of modes. there was the, the typical Kubernetes
deployment where we had the demon set for collecting logs, metrics, and traces
from everything running on the nodes. There was a couple of like, stateful sets. One was for like dedicated to
collecting Kubernetes related metadata. And there are a couple of
different stateful sets for, pulling data from AWS CloudWatch. We also had, deployed it as, sidecars to
various things still running in ECS, which were being, migrated to, to Kubernetes. And then we also had a couple of
auto collector, deployments with, ingresses, for either interesting
the data from the sidecars. in the ECS into the, into Kubernetes, or
we even had, sort of a, like there was a hybrid mode of our product where you
would, the execution layer would run in customers VPCs, this was written in Java
and had the Java agent instrument included in, and that would also send back metrics
and traces, To our ingress behind which we had the open telemetry deployment and then
in front of the looks good to me stack. We had another layer of open telemetry
collectors to do some unified transformation to ensure some some
labels were common things like that. Awesome, and how about you, Greg? so we use the collector. for traces, we had a sort of legacy,
kind of trace like thing called request viewer, which was based
on logs, which was very heavy. And we're migrating now everybody, I
think we've just started to delete the cluster for the old request viewer. So now everybody should be
sending traces, via the collector. We do some processing, do some
sanitization, add some attributes, and do tail sampling as well to, so
that we can sample by whole traces. we don't do anything with metrics
apart from our own metrics, so we gather the metrics from the collector
and forward them, Prometheus remote write them out to Grafana. We use Grafana Cloud as the
backend for all the telemetry. We so it's, we deploy it in ECS. Not kubernetes. and that's kind of been interesting. And we have one central cluster. We don't have a sidecar. We have one central cluster that scales
in and out with load of the collector. Okay. Interesting. Interesting. I definitely have some follow up
questions, on that, which I'm, we'll, we'll save that for a little bit later. and then, finally, Joel. So, we have collectors
deployed all over the place. we've run collectors on all of our hosts. They are kind of egress
gateways for telemetry. primarily the, the, the data which
we're shipping is actually fully, well not fully, but, it's mainly log data. We have pipelines enabled for metrics
and traces, but currently it's just the collector's own metrics, which we ship. and there's very few applications
which are using traces at the moment. So primarily we're using it as
a kind of log telemetry mesh. and we're using that as a, as a way
to sort of, lay the groundwork for the full migration in the future. So we have the, let's say the egress
collectors running on our hosts. We have an ingress collector running
in our central Kubernetes cluster. And then we have, multiple
layers of collectors behind that. So we have a routing collector. And then we have a collector
which is specific for each backend which we're interested in. So for example, for Loki,
for Thanos, and for Tempo. Those are the main, backends which
we're shipping to at the moment. We self host everything. and the, yeah, the reason we've done
it like that is to sort of try and keep the configuration overhead,
simple because those pipelines can get quite complicated when you try and
stuff everything into one, collector. yeah, so we have this sort of,
egress and ingress, concept. And the goal really that we have is,
we're trying to ensure that all telemetry in the future will have a uniform set
of labels of metadata attached to it. So we're starting with logs, and then
we're going to roll that out also to metrics and traces in the future,
that you can really actually start to correlate between signals in the backends. we also, if I can quickly say, we
also do some custom processing. So we have, we actually
build our own collector. and so we, some of our teams, for
example, have built, you know, processes, which, do things to proxy logs. For example, with proxy logs, which come
through, they need special processing. so it's been quite well adopted also by
the service teams when they see the, the power of, of building a custom processor. That's great. next question is, are you, So starting
with, with Iris, are you using a vanilla collector, collector contributor,
a custom built one, vendor distro? Like what, We're using, sorry. Yeah. We're using the vanilla one. so far we haven't had the need
to use, any, any custom that is already not, there, no new, nothing
new, or the, or a vendor one we're currently fully open source. So yeah, the vanilla one
worked great in our case. So I, I'm assuming that's like
collector contrib as is kind of thing. Yeah, exactly. Of course we have our own
configurations, internally, but, yeah, it's the same, the base image. Okay. Perfect. same question, Yudai. I honestly do wonder if anybody's
actually running the, like, not the contrib one, because the, the, the
main one just does only old DLP. And I think that's kind of like, I
have seen very few workloads that. Produce LPLP and can also
interest LPLP on the other side. Anyway, we use a variety. we have Multiple custom distributions
built on one of the reasons behind that is being, for example, the OTEL collectors
that are sort of exposed to the Internet. We wanted to minimize. Well, first of all, we wanted to
minimize the size of the binary, but also minimize the number of. components just to have the only necessary
ones, even from security perspective, especially around exposing it to internet. We had another special distribution,
which contained, the gold debugger in case we needed to debug some, some
issues, were like, There was, for example, issue with the Datadog exporter, which
was not exporting properly certain labels and logs, things like that. And, all of it is based on the,
upstream, open telemetry collector contrib with just custom configuration. And so I, I'm assuming though, since
you're, you talk about like, having, having a collector with like just
the things that you need with the reduced binary, I'm assuming then
use the builder then to, Then we have like, renovate, bought to, submit
pull requests with, with updates. We also had some, I mean, we, we also
contributed a bit back to total collector. So we also used it, so we could test,
Changes before they were merged changes on processors on other components
before they were merged into upstream. Awesome. And, since you did, so since you've
done contributions back to the Collector and since you've used the Collector
Builder, what have your experiences been around both of these things? I guess let's start with, like,
has the OTEL Collector Builder, like, did you find it a, a useful,
intuitive tool to use when you were building your, your own distribution? Yeah, I think the one, like, once we got
the initial configuration going, then it's really easy to, that's why we have,
like, six or seven different builds, because it's, it's just, you, you, Copy
paste the config once, edit it a bit, remove, add what you need, and then just
run the builds in parallel, basically, and just, just give them different names. And it, it was also quite easy to
then just point at like your fork of a specific processor to test it. so you can, so we can test things
even before they get merged. Also with, the one thing I think
the, the bit where there's that like replaces at the bottom, that's, that's
something we, we ran into a couple of times where we needed to update that
because the, the builds broke, but that was, just looking at what, what the
upstream was doing and updating that. With that information, yeah,
so the second question was on the contribution process, or? Yeah, yeah, how did you find
the contribution process to be? I think it's, it's okay, like, it's kind
of sort of nice that things get, because of the pretty frequent releases, you don't
have to wait that long for your changes to go live after you There's, there's,
I think there's decent documentation around like, how you can, how you can
contribute like things out, like how to format your code, things like that. And I think there's a world of
pretty timely response to like well written issues where they tell you
like, Oh yeah, that's, that's cool. Like if you have time, you can
contribute and fix a certain thing. So that was, well, the only, the, the
only like slight frustration I found was, at times it can take a bit for
like, there's a label on the, on the pull request, which is like ready to merge. And even after that gets assigned, it
can take, like up to like week or two for somebody to finally merge it, which
can be, Frustrating because then like the pipeline starts failing because
something broke upstream and somebody Merged upstream into the branch and it
broke the pipeline like there's there's things like that But other than that,
it feels pretty good All right, great. Thank you. next, Greg, what, what collector
distribution do you use? Do you, use contrib? Do you build your own? So we, we, yeah, we build our own. We use the builder. we forked the contrib
repo and, based off that. so we do that because, well, initially
we had a feature that we needed. which was to add ECS, well, AWS cloud
map service discovery to the load balancer exporter, so we could get a
list of targets for the load balancer. so we forked that, did that locally,
and we've actually contributed that back, or there's an open pull request
at the moment that's taken quite a long time, it still hasn't been merged. I think it's getting there. I think it's near now. but that's taken that's been quite
slow and then we've discovered quite a few either missing features or bugs
So it's been quite nice to both be able to debug the code locally and
actually step through and find out Is this how it's supposed to work? And also then to be able to go and fix
it Although we've had about five or six different bugs that we've got to the point
of almost fixing them And then we've seen that it's been fixed in the upstream repo
Somebody else has worked on it and has parachuted in and has fixed it Which is
obviously nicer because you know, they presumably are doing it better than us. None of us are Go developers where i'm
got a java background and we have various other sort of developer backgrounds,
but nobody's a go developer So we're kind of a bit nervous about contributing
and a bit nervous about making changes and quite slow about that as well
but it's been a very good opportunity to learn more about go awesome. And and then same question around
the builder How did you find your experience in using the collector
builder to build your own distros? the builders, find no complaints. It's quite, quite, I mean, as I'm
new to the go, ecosystem or, you know, I don't really know how any
other go project large project works, but it seems to work quite well. My one complaint made
is it about the builder? Or about the repo there's a there's
like two or three components in the core project right not the contrib
like the otlp receiver the batch processor the memory limiter And i've
been wanting to work on those and it's really painful that they are not in
the contrib repo It's really painful to be able to like make changes to
them and get them even running locally. I don't even know how i'd managed
to build another distribution of the main thing, and I don't know how that
would work, but like, so with the builder, you just do the replace and
point it to your local directory. So as long as the component
is in that repo that we're building from, it works fine. Yeah, but for these other components,
it's, I would be much happier if they were in the contrib because
it would make my life much simpler. Okay, that's, that's definitely a
good, good piece of information. We'll, we'll be sure to pass that on. and then finally, Joel. So, we are running, our custom build. the reason is actually because we
have, like I mentioned, service teams who built their own processes. That was the, actually one
of the big draws for why we should adopt OpenTelemetry. so that, I mean, that has been pretty,
very, very well adopted, I would say. We use the builder, it was not a problem
to get it running in our, build pipelines. very, very good experience there. It's always quite fun. We, you know, I think, you'd have, you'd
have mentioned, it's quite a fast release cadence, which is a good thing, but if
it's very easy to let a few versions slip by, and when you're maintaining
your own distro, sometimes you get some nasty surprises when, you know, if you
were to just build and deploy, some config with, deprecated or completely
removed without, you know, you have to chase down those errors and be very kind
of on guard, even when you do a product deployment and you've checked everything
in dev, it's always a little bit on your mind, Hey, something could have
changed, which is going to blindside me. but I mean, that's just kind of, it
comes to the territory because a lot of the, you know, the, the processes and
modules that we're using are in, you know, alpha or beta stability level. I think it's kind of expected,
and it's, it's one of the sort of things we're happy to pay for with
the flexibility of the solution. so this is good. yeah, but the overall really,
really positive experience. Awesome. next question, starting with Iris, what's
the biggest challenge or challenges that you've faced with the, with the Collector? And it can be stuff like deployment,
configuration, monitoring it, debugging it, or Debugging, for sure. yeah, I think, deploying it is pretty
straightforward, but debugging, I had a situation recently. It's kind of, embarrassing to say now
after finding out what the issue was. It was the first time that I was
actually using the collector with the ingress, enabling the ingress. Usually it was all, taken care
of inside the Kubernetes cluster. and of course, having to pass the
right paths and, yeah, I kept, kept sending, spans to try and see if
it's going to work, but nothing, I just got an error message. and nothing else. I did try something else,
just, not an error, but like a status code and that's it. And it took me, me and my coworker, more
than two days to figure out that, what the issue was because, yeah, we tried
to, to, to enable debug logs, debug exporter, everything, but there was
just not enough information for this. And in general, it has happened like this. After a lot of. time spent, we figured it out, but yeah,
it could have been a bit easier for us. What did you end up doing
for, for like troubleshooting? Did you have to like
go deep in the code or? Yeah, deep in the code. And it's at this point, it became
like a brainstorming session. Everything that we ever knew about
IT, we're like, okay, this could be, this could be, this could be,
this could be that, you know, and we finally got to it after a long time. But yeah, checking the
code definitely helped. And then we realized,
okay, you actually need. the path in the receiver itself
to, to explicitly add it. Yeah. That's why I say that after it's
been solved, it's like such a silly thing, but at the moment of debugging,
it can get pretty overwhelming. And now, did you have like a Go
background for, to aid in the troubleshooting or like, what? I didn't work with Go before actually
working with, with Open Telemetry, but now I'm, I I I'm learning, that's the thing. open telemetry and debugging, and
checking everything has, has become my experience in learning Go, and
I'm also learning independently. So, yeah, it was a good excuse. Oh, that's great. how about you? What's, what's your biggest challenge,
that you faced around the collector? I think when we ran into a couple
of bugs, it was, it was kind of hard to debug because like they
were sort of like happening only with large loads of data at times. So you, that's when we ended up having
to build our own distribution to deploy with the gold debugger attached to it. At least a lot of decently used
dev environment to actually see, okay, why is this happening? And then we only figured out, Oh,
this is like a bug in the like Datadog exporter, for example, where like
it was not doing something properly. And I think that like, if you have a bit
more complex pipeline, especially if you manipulate a lot with like the research
attributes, things like that, it's kind of hard to test locally or even, you
know, like when you, when Basically just sort of need to roll it out to some lower
environments and see if it works properly. But then if you have some of
your like your own local testing environment, we don't have that
much data going through it. And it's probably maybe slightly
different than what like the actual business applications produce. So, I mean, there's a, it would be, it
might be nice to be able to, to have some sort of capability to test that
bit better without having to actually deploy to like full blown environments. And then, you know, like the,
there are, there were a lot of late breaking changes at times, so always
need to be careful read through the changelog before running out things. And, in the later stages of the migration,
we had an incident, for example, where we stopped sending some data to Datadog
or like some of the labels changed. And we didn't code it in the lower
environments because we were no longer sending those to data docs. So we'd only, we realized that in
production and then like SRE team started to like scream at us, like,
where's the data, where's the data? Oh, this label changed. Why did they change things like that? I mean, one other thing we ended
up doing was because we had multiple sources of the data going. Like different types of auto collectors
doing different type of things we ended up attaching the label to all the
metrics logs and traces coming through it basically Telling us like which
which auto collector Type it came from. So like demon set for the demon said,
something like, Kubernetes for the one that collected Kubernetes metrics. And then like, we had like internal
slash external interest, which was for some of it, the internal force
for ECS, the external was for. Metrics and traces coming from,
from the external customers, just so we could easily track down, okay,
where is this data even coming from? Right, right. And, I'm just out of curiosity. So, you know, you, you mentioned, like
debugging, debugging issues in the collector also was a pain point for you. is, is, do you have a, go background? I'm not really a software engineer. I'm more of a on the upside, but
I have been using things like Prometheus and Kubernetes for years
before adapting open telemetry. So a bit. Gotcha. Gotcha. Okay. same question, Greg. I mean, I would, our biggest
challenge has been, like the quality of the platform we're providing
to the rest of the organization, especially kind of coming from this
other system, which kind of worked. To rolling out the collector and maybe
our configuration being wrong or maybe they're being bugs or whatever for some
whatever reason Traces and spans not being available in the back end when our users
were looking for them And as having gone out and said hey, this is the future. This is the great new technology It's much
better than this thing We made in house for them their actual experience of them
going and looking for the requests that they were trying to debug and it's not
there That probably initially was just naivety on our part, like we didn't know
how to monitor the collector properly, we didn't know at which point along
the pipeline from the trace or the span being created in the application to it. Arriving in the, in Grafana, in
Tempo, where we should be looking. And I think we've improved on that, but
there are still kind of areas of doubt. And we've got a couple of things
which we're struggling to know how, in principle, we can even
monitor it, or how we should do it. And it just doesn't seem to
be possible at the moment. So that would be our kind of biggest
Thing that's caused us anxiety and the second thing would be there's just the
sort of bugs or the things not working as expected in the collector and I I
joined the team a little bit later a bit more senior than some of the other
people and I think when they adopted it they Kind of drank the Kool Aid. They thought this is great. It's going to work. It's going to solve all of our
problems and For a long time they were struggling thinking that
they were doing something wrong. Whereas as I'm a bit more senior,
I'm very cynical I'm like, oh, there's probably rubbish code. Let's go and have a look at like the code. Oh, look, it doesn't work You know,
they didn't like think to ask those sorts of questions But you know once
you've been around for a while you realize that all code is rubbish code
and everything's got a bug somewhere Yeah, so some examples
of that service graph. At the moment, retry. There's, I don't know if you're aware,
but, I think the gRPC receiver will now return a retry code, but the HTTP
Receiver, OTLP receiver will not return a proper retryable code, it will just return
a server, a 500, no matter what it is. Whereas a transient error should be like
a 503 or something, so the client retries. So we turned on retries in our,
in the agent, and we're like, hey, everything's going to retry, we're
not going to lose these spans anymore. And like, we're still losing
them, what's going on? And it's just not implemented. In the collector, right? Retriable, transient errors. So stuff like that, it's like, oh,
right, okay, don't assume that it works. We've just switched from using
the OpenCensus metrics, internal metrics, to the sort of native
OTLP, or whatever you would call it. And that all seemed great, but then
some of them have disappeared for the tail sampler, because the tail sampler
has not yet been migrated to OTLP, and it's only publishing OpenCensus metrics. Which is fine and we'll probably be
quite happy to go and fix that because it's quite easy and submit a pull
request for it but it's just like somebody spent a week thinking that
they've done something wrong right and actually like oh, it's just not Yeah. And, you know, you mentioned like, yeah,
you could submit a pull request to fix it. have you like submitted any
issues, around, around these items that you've identified? so it's a similar story to
earlier that like I'm maybe not. As good as my job as I should be so What
I do is I go and try and mess around with the code and fix it And then I go and see
if there's an open issue And then I find out there is an open issue and somebody's
already working on it And I should have been doing something else with my time. so pretty much Yeah, everything
that we've seen so far. There was one thing,
there was one other thing. We use the count connector
and that produces like a stream of delta data, points. And we needed to export them
to a Prometheus remote, right? So I actually created a,
like a delta to cumulative. processor and opened up a merger,
an issue for that and got sponsored, but then somebody else had the same
issue and now they're working on it. I haven't had time to actually, my,
mine was a very much a proof of concept and we've got it running in production
and it works, but it's like, it only meets our very particular use case. It's not like a generic and it's
probably written wrong and everything. Right. So yeah, we opened up that issue and yeah. It got some attention, so that's,
that's how it should work. We're happy with that. Awesome. That's great. And finally, Joel. It's really interesting. You mentioned that I was going to
be my, my point that I was going to make is that I think the handling of
cumulative metrics is really missing. so that's something which we kind of miss
with very sort of Prometheus focused. so all of our metrics are in Thanos. We want to ship them through. Which I, which I think is working,
but, for example, like we ran into exactly the same issue with the
count connector and we just figured out, yeah, that's going to be easy. Just plug it in and Bob's your uncle. You can ship that to Prometheus
and it didn't work like that. And it was sort of once you're so
deep into the topic, you kind of know. Yeah, sure. That's not going to work. but. You have to get quite deep into it to,
to, to get to that point of understanding, which I think was disappointing to
our users when we turned around and said to them, ah, yeah, by the way,
that solution we proposed last week definitely isn't going to work. We sort of, we need to wait on some
upstream, development to go on there. so I would say, yeah, that's the, the
hardest part of the moment actually is, planning how we're going to bring
metrics into our sort of unified pipeline. Because at the moment, it's, yeah, it's
just a, just a tricky, a tricky part. We also have a sort of outstanding
use case, I would say, which is a, you know, generic, I mean, we, we, we
have, like I mentioned, a lot of logs. So we're very logs based at the
moment, kind of a very old school, which trying to change it internally,
but that takes a long time. so we have like a lot of use cases where
we want to build metrics out of logs. And currently, there's no, you know,
general way to do that in the, in the. we're actually working on that as a, as
a sort of internal use case currently. So to build like a logs
to metrics connector. but there's a few sort of, let's say
functionalities I would have expected to be there, which aren't there yet,
which, yeah, it's, it's also very good to see, I mean, I see Dan is here. We. Dan is sponsoring, I think,
the, cumulative to Delta or Delta to cumulative, processor. So it's very good to see that
the, you know, the community is working on it upstream. It just can be a surprise sometimes when
you think, ah, for sure, that feature must be there when actually, oh, no, you
can't generate metrics in the collector and remote write them to Prometheus. That's not not there yet. yeah, so a few surprises like that. Basically, that's, let's say the
hardest thing you can never be too sure when you're talking to other
teams in your organization that what you're promising is actually. achievable until you sort of dive in
and get your hands messy with the code. All right. Well, thank you all right next question. What what's kind of it? On your, for Iris, what's on your
collector wishlist as, like, something you'd like to see, feature improvements? I am looking forward for profiling. I've been following it as a project and I,
I've seen some, some groundbreaking things and I'm really looking forward to it. the collector, honestly, so far
in, in both my experiences working with it has been very complete
and it has worked well for us. We really didn't need to have custom
builds because it had everything. So now, since we are talking
about the good stuff, profiling is the next big thing and I'm
really looking forward to it. I saw that there was a version two
model already merged yesterday. So yeah, it's going to be great. Juraj, how about you? I'm looking forward to seeing. Bigger potential like the Apache Arrow
project getting more ready to use because there were some promising, very promising
improvements around reducing the network usage when the data is being transported
and then like I have just like to do list of things that need fixing like. We, we found a silent way you can lose
data is for example, with metrics, at least the Java agent basically sends
them like once per minute, regardless of like how many metrics you have. So it's, basically ever growing with
the number of metrics you have until you hit like the max size of a gRPC
message and the, unless you, unless you collect the logs of the collector. Which you might not want to do if you
use the Altel Collector to collect the logs because you can get like a feedback
loop because of that with issues. You won't see in any of the metrics that
you're chopping data because it's chopped in the gRPC layer so it doesn't get to
the part where metrics are implemented. so, there's things like Altel to
Altel, gRPC is basically an unusable in Kubernetes right now because, even
when you configure it to do client side load balancing, You like it doesn't
very clearly refresh the targets So it basically will keep using the first
set of targets it discovered until like all of them are gone So if you have
any auto scaling there, it will not pick up the new pods things like that. So, Potentially maybe getting to a
point when there's With like with the new releases very frequently. I think it's double edged sword
Like it's great that things are moving quickly, but then it's also
like a lot to keep up upgrading. Otherwise, you will get Behind
and then you have like 10, 15 versions to upgrade by. And that can be quite challenging. yeah. And I'm like, maybe overall. It's kind of like mixed, like there's
some compatibility issues with, with the Prometheus ecosystem and
it, that, that sort of feels like a missed opportunity there because
it didn't have to be that way. Like if, if, if the, like with the, for
example, the cumulative versus Delta. I think that kind of, it comes down
to like the, the open telemetry project decided to support both. And now they have to deal with a lot
of the complexities of like something produces, some things produce Delta,
something produce cumulative life. If it just picked one. It would be a lot, a lot simpler to
support things like that, I guess. And then especially I think around
the receivers for things like, you know, in, in Prometheus, you have
quite nice ecosystem of exporters. And I guess that like in Delta
collector, you have receivers that are sort of trying to, to, mirror that. But I think the maturity of
them is nowhere near, Prometheus ecosystem, like that, that is. Also feels like a missed opportunity, like
why not just reuse the existing ecosystem? Sorry, instead, like, as far as
I understand it, we're basically implementing very much similar things. The Prometheus ecosystem already did,
just in a slightly different way. So as a follow up to that, do you
see, does that mean that you're having to still do things in Prometheus
that you would have liked to have shifted to OpenTelemetry, or is
something altogether different? Like, it's some of the trade offs we
took, like there's, compared to deep state metrics, there's still some missing data. For example, there is no, there's no
metric which would tell you, what was the reason for your container restart,
which I think is kind of important. With, with, the container
metrics, there's like the CPU throttling is completely missing. So things like that, like you can live
with them, but it also feels like, you know, like if they're like, why not just. If it just adopted the Prometheus
ecosystem, these things wouldn't be an issue in the first place. Gotcha, gotcha. Greg, same question. what's on your, what's on your wish list? So I mean, yeah, I would just
like it to mature a bit more. So some of these things we've been
talking about where you expect something to work, like retry to
work or Delta cumulative to be there. Or, you know, just there
not be like these bugs. These things will be fixed
in the future, right? So i'm looking forward to that time when
the sort of pace of change slows down It gets a bit more mature a bit more
sort of battle tested and as joel was saying, you know, you can You can read
the docs, see there's a feature, and tell your user, yeah, this is probably
going to work, rather than always having to like, actually, until we've got it
working, I'm not going to tell anybody, because it might be a nasty surprise. And then two specific features I
would like to see, I'd like to see an integration point, extension
point for the exporters, so we can have a dead letter queue. I'd like to be able to like,
if something can't, is a permanent error trying to export. a span, let's say, then be able to
send that to another pipeline and go write that to S3 or something, right? So that I could actually see
what, what went wrong with that. We get some errors with, like, trace
too long when we're sending to Grafana, and we don't know which traces they are. There's no way of finding out. so that would be nice. And also, we use, like, the load
balancer, and as I said, we have an extension for ECS, for, sorry, CloudMap. so I have this anxiety that I'm
sure at some point, when we scale in and out, And that, that consistent
list of, routing targets changes. Then when we were sending a trace to one
target, we're now sending it to another target, and we're gonna get a split trace. And that tail sampler that's running
downstream is gonna, there's gonna be two different nodes, both processing half. So I would like to see some
sort of solution to that. I don't know what that solution
would if it's like caching the target or writing to it until you
get like, refused or something. I'm sure there's some technical
solution, but I don't actually know if that is a big problem because we
don't have any way of measuring that. There's not an explicit error there,
we don't have, we've thought about maybe having some sort of synthetics,
where we're sending, like I said, a straight astroptosis, and seeing how
many have actually arrived downstream. But we don't have a way of measuring that. I don't know if it's a big
problem, but I worry about it. So I would like to see that solved. That's it. All right, and Joel Yeah, I think I can
actually echo a lot of this One thing where I would really look forward to would
be a Prometheus remote right receiver I know this is actually I'm not sure
what the current status is I know it was worked on about a year ago or so and then
I think the project kind of lost steam a bit First I can tell nobody's working
on it Participate in the Prometheus working group and it was brought up as
one of the things that would be nice for somebody to get to it's in my to
do list, but it's, it's deep in there. Yeah, definitely. And I think this is, it's exactly like
Greg said, this is something which I was, just when you discover the
product, you kind of assume for sure you could remote write to Prometheus. And of course, the technical
specifics of why you cannot. Let's say beyond me at the moment. maybe one day I will be able to
understand, and I'd love to understand. but yeah, this, this would be a very
big feature that, would be on my wish list if I could have it tomorrow. just in terms of sort of my goals
and in, in our team, for unifying our telemetry, this would be, yeah, the, the
sort of the golden ticket, if you like. yeah, I had another point,
but I think I've forgotten it. Yeah, and again, sort of maybe a general
connector again on the metrics topic, so a general connector with which you
could take sort of any telemetry and build metrics within, the collector. I think this is a, let's
say, a gap in the market. and we're currently. Working internally on just the logs
part of that, so maybe in the future, we can sort of bring that to the
community and contribute it and expand it to to other sources of telemetry. but that's for sure. It's it's, those would
be top of my wish list. Awesome. Thanks. I did have a final question for everyone. because I, I think especially
as we see open telemetry pick up more in the community. I want to talk just very briefly
in the 8 minutes that we have about, scaling the collector. any, any, like, feedback pain
points around scaling the collector, starting with Iris. so, so far about scaling, we have
used, at my current company, because we only are using for traces,
we're using just normal horizontal auto scaler, it, it works great. in the past, we were also after KEDA,
and I remember we even opened an issue in the OpenTelemetry, my colleague opened
an issue to support it on the original chart, but I don't think it is supported
right now, but we did do it, out of the box for our own obligation, and. That worked very well for us, especially,
considering that the, okay, so, HPA works because, most of the, the queue is memory
based, but, yeah, using KEDA, based on the, on the queue size was, was a great
move for us, to, to do the auto scaling. But, yeah, even the HPA works great and
depending on the load that you have. All right. Thanks, Juraj. For all the deployments, we were using
HPA, also just based on memory and CPU. That worked very nicely, I think. and then for, for the daemons that we
were looking at doing, VPA, just because, they're like, yeah, if you, if you have
a single node with bit higher load, you, you need to bump the resources and
there's nothing you can do about that. All right, great. and Greg? so we're kind of like quite. Relatively early in our journey still
with this, and we're at the moment happier to spend money than to lose data. So we've got like quite a, what's
the word, conservative, we over provisioned basically, and we've
got a simple auto scaling policy. Based on, memory because the
biggest thing is the tail sampler, which holds all the memory. we do scale out quite far and then back,
back, back down again, especially in our load test environment, obviously. So like that goes to almost nothing
overnight and then during the load test, we get like 30, 40 instances sometimes. but we haven't put a lot of effort
into trying to like actually. optimize that because we're much more
worried about making sure that we've got, we're properly processing all that data. And because we're not sure what we're
supposed to be monitoring, we're kind of very nervous about changing anything. But we're in AWS, so I would like to
see, exporting the system metrics that we've got, the internal metrics, to, you
can write them to, to CloudWatch logs and then turn them into metrics somehow,
it's called EMF or something, because you need the metrics to be within CloudWatch
so that you can hit the AWS autoscaler. So we can't use any Prometheus metrics,
which is what we're normally doing. So there's quite a lot of Stuff in my
head that we could do there that i'm interested to look at but apart from
like getting it working on my machine. I haven't had anything deployed anything
actually Running, but yeah, that's because we're we've been a bit burnt by losing
data So we're just like very cautious about that at the moment Fair enough. And finally, Joel. So, essentially we run everything,
on one cluster per environment. and these are all deployments. And we found that just HPA with
the memory limited processor has been no problems at all. I think it's even just the out of
the box config for the processor. I've never seen a collector OOM
actually, which I find quite impressive. yeah, that seems to
work very, very nicely. actually, I need to talk to Juraj after
this call, because I was suspicious of gRPC on Kubernetes, because I have
run into the issue where parts will scale out or deployment will scale out. but some of those parts just
don't receive any telemetry and we are using gRPC on, Kubernetes. So that sounds like an
issue I need to dig into. Definitely. If you, you can find me on the CNC
of Slack and if you ping me there, I can send you the link for the, I
don't know if there's an open issue about it, but I discussed it already. With another person I can send
you the link for the thread. Yeah, that's great. Thanks. so that's something very useful I
take away from this panel at least. Thanks for that. Can I mention, you you mentioned that
somebody mentioned the memory limiter so I was Enthusiastic to my team another
one of these things where like i've read the docs and I tell everybody let's just
do this Like the memory limiter there is going to give you transient errors, right? If you get near when you're
scaling out, it's fine because the client will just retry Right. And then the fact that retries don't
work, we started losing this telemetry. So that was like, that
was a scaling problem. So now we never hit the memory limiter. We always scale well before we're going
to get anywhere near that, because it basically doesn't work, right? I mean, it's going to stop it out of
memory, but it's not gonna, the client isn't going to retry and resend that span. And that's a much bigger problem for
us than spending money on memory. Yeah, that's a really great point. well, I guess we are at time. We've got two, two minutes
before, before we wrap up. So, thank you to all of our panelists
for showing up today and sharing their thoughts on the OTEL Collector and
how, how you use it, out in the wild. This is super valuable and thank
you everyone else who joined to, to give this a listen. We definitely really appreciate it. Tell all your friends who were not able
to make it today that we will have this recording up on the OTEL YouTube channel. Our channel, in case you're not
aware, it's called OTEL Official. Also, for anyone who is going to
be at KubeCon in Paris next month, a number of us from the OTEL end
user working group will be there, including, Reese, Dan, Hope. And Rynn, I don't think Rynn is on
this call, and I will be there as well, we're going to be hanging out in the
OTEL Observatory, which, if you were at KubeCon North America in, last fall,
it was the happening place for all things OTEL, and we've got a lot of cool
things lined up at the OTEL observatory. We're actually going to be doing
some more user feedback sessions. we're going to be
recording Humans of OTEL. They're going to be SIG meetings,
OTEL demos are going to be running. So, we're going to have signups
also for some of these things. So if you want to participate in a
different, in another, feedback session for another SIG, or if you want to
be interviewed for Humans of OTEL, we'll have the schedule posted up. I think there was a blog post
on the OTEL blog, but just. came out with the sign up
links for various things. Now our feedback sessions are still TBD. but keep an eye out for that post in the
OTEL blog, as we finalize the details. so yeah, hope to see, a number
of you in Paris and thank you so much for joining us here today. Appreciate everyone taking the time today. Yes. Thank you so much. And we will see you on Slack. Yep. Thank you so much. Bye. Thanks everyone. Bye. Bye.

