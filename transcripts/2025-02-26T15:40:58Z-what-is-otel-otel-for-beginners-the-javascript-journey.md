# What is OTel? | OTel for Beginners - The JavaScript Journey

Published on 2025-02-26T15:40:58Z

## Description

Want to learn more about OTel but have no idea where to get started? OTel for Beginners - The JavaScript Journey series is ...

URL: https://www.youtube.com/watch?v=iEEIabOha8U

## Summary

In this video titled "Otel for Beginners," Lisa Jung introduces OpenTelemetry (otel) as a crucial framework for observability in modern software systems. She emphasizes the importance of turning complex, opaque systems into transparent ones by effectively collecting and managing telemetry data—metrics, logs, and traces. Lisa explains how otel mitigates vendor lock-in by establishing an open standard for instrumentation, allowing developers to easily switch between observability backends without the need to learn new proprietary systems. The video also outlines resources for beginners, including official documentation, a YouTube channel, and a community on Slack for support. The next episode promises to focus on starting the JavaScript journey with otel.

# OpenTelemetry for Beginners

Hi, welcome to OpenTelemetry (Otel) for Beginners! My name is Lisa Jung, and I'm a member of the OpenTelemetry Communication SIG and End User SIG. I recently began my journey with OpenTelemetry, and as a new user, I had a tough time figuring out how to get started. I want you to have a different experience, so I'll learn alongside you and share what I'm discovering through this series. 

Depending on which programming language you're working with, you'll follow a language-specific journey. In this series, I'll focus on the JavaScript journey to get you started with OpenTelemetry. 

## What is OpenTelemetry?

Before we get our hands dirty, let’s discuss what OpenTelemetry is, why you should consider using it, and the resources to get started. 

OpenTelemetry (Otel) stands for **OpenTelemetry** and plays an important role in observing your systems. First, let's talk about observability and how OpenTelemetry fits into this concept.

### Observability

Modern software systems can consist of complex, multi-layered, and distributed architectures with many interdependencies. A system without observability is like a black box; we have no idea what’s going on inside. If something goes wrong, it becomes more difficult and time-consuming to solve the problem. 

With observability, we can turn this black box into a glass box. Observability helps you collect data necessary to visualize and understand what’s happening in your system. 

### How Does It Work?

To make this possible, you first have your infrastructure or applications that you want to observe. You’ll collect data from it and send that data to the observability backend of your choice. Then, you connect the backend to a visualization frontend where you can query and use the data that interests you. 

The most common types of data collected for observability are **metrics, logs,** and **traces**—these are known as telemetry data. Getting the telemetry data into the backend is crucial for understanding your infrastructure or applications, and this is where OpenTelemetry comes in.

### OpenTelemetry's Role

OpenTelemetry is an open-source framework that allows you to add software to your applications or systems to generate telemetry data. This process is known as **instrumentation**. OpenTelemetry collects, manages, and exports telemetry data to an observability backend for storage.

Different aspects of OpenTelemetry make this process possible, and we will discuss them in detail as we go through the JavaScript journey. For now, remember that OpenTelemetry focuses on the generation, collection, management, and export of telemetry data. You can easily instrument your applications or systems, regardless of their language, infrastructure, or runtime environment. The storage and visualization of telemetry are intentionally left to other tools.

## Why Use OpenTelemetry?

Now, why should we consider using OpenTelemetry? 

Let's first discuss something that many of us have experienced. If we dig through our drawers at home, we could probably find a bunch of cables of different types. Why? Because the devices we own come from different vendors, and each vendor has a specific type of cable and port to charge or connect their gadgets. 

We are all familiar with buying multiple products from the same vendor and investing in additional accessories and apps specifically designed for that product. Before we know it, we get so used to using a line of products that switching to another vendor can become quite difficult. The product from another vendor may operate differently, which will take time to learn and adapt to, costing us more money because our additional accessories or apps won’t work with the new product. 

This issue is known as **vendor lock-in,** where the costs of switching vendors are so high that customers feel stuck with what they have. 

### The Shift Towards Standards

Things are slowly changing with USB-C ports becoming the universal standard. For example, it doesn’t matter if you’re using an iPhone or an Android phone; you can charge or connect many of these phones with a USB-C cable. Because a universal standard has been set, users can use the same cable regardless of the brand of phone they have.

OpenTelemetry has similar implications in observability as USB-C does for phones. 

### Vendor Flexibility with OpenTelemetry

To summarize, we have our infrastructure or applications that we want to observe. We want to collect telemetry data and send it to an observability backend for storage, so this data can be queried and visualized with an observability frontend. 

Imagine you have three observability backends to choose from: vendors A, B, and C. Each vendor often has proprietary instrumentation agents or collectors. Let’s say you picked vendor A. You're using their proprietary instrumentation agents or collectors and sending the data to its backend. But what if your needs change later, and you want to switch to vendor B? 

Switching vendors is not as simple as it might seem. You can’t just send the existing data from vendor A to B because vendor B requires its own instrumentation agents or collectors, which means you cannot accept data from vendor A's proprietary instrumentation. Your development team would need to change their instrumentation, possibly to a new proprietary solution from vendor B. 

Now, imagine doing this for thousands of Linux machines or dozens of applications. Is the cost of money, time, and effort worth the benefits of changing vendors? As you can see, with this setup, the cost of switching vendors can be so high that customers can feel effectively locked in by their choices.

### The OpenTelemetry Advantage

Now, imagine if all vendors accepted the same standard for sending or receiving telemetry data, similar to many phone companies accepting USB-C as a standard. When you switch a vendor, you wouldn’t need to learn proprietary instrumentation agents or collectors each time. You would only need to learn one technology and a single set of APIs and conventions associated with it. Whatever data you generate with this technology is yours, and you could send it to any observability backend that accepts the standard. This would make switching vendors substantially easier and reduce costs, time, and effort.

This is exactly what OpenTelemetry does for you. It creates an open standard—a set of guidelines, rules, or specifications for sending and receiving data. 

There’s a significant incentive for vendors to accept OpenTelemetry. Many customers prefer OpenTelemetry to avoid vendor lock-in; they want to learn a single set of APIs and conventions instead of having to learn new ones every time they change a vendor. They also want to own their data and send it to any observability backend that accepts these standards.

Vendors benefit from accepting OpenTelemetry as well. Customers may already be familiar with it, and there is a vibrant OpenTelemetry community that serves as a great resource. By accepting OpenTelemetry, vendors can reduce their support and implementation costs. Moreover, there is more demand for innovation since vendors are receiving the same data, prompting them to innovate to stand out from competitors.

As you can see, there are many benefits to accepting open standards, and you can take advantage of these benefits by using OpenTelemetry.

## Getting Started with OpenTelemetry

Now that we've covered what OpenTelemetry is and why you should use it, let’s go over the resources to get started. 

The links to all the resources are included in the description of the video. The best place to begin is the **OpenTelemetry documentation**. The documentation is continuously being improved, so the page may look different by the time you watch this video. Be sure to use the link in the description to check out the latest page. 

The first place in the documentation you should start with is the **language APIs and SDKs**. As I mentioned earlier, your OpenTelemetry journey will differ depending on the programming language you’re working with. Select the language of your choice, and you should end up on a page that lists all the resources to get started.

Next, we have the **official OpenTelemetry YouTube channel**, where you'll find helpful videos along with the OpenTelemetry for Beginners series.

Lastly, as you start your OpenTelemetry journey, you may have many questions. We have a huge community of OpenTelemetry users on Slack. Join the CNCF Slack Channel, post your questions in the OpenTelemetry Channel, and connect with other community members. Again, check the description of this video to access all these resources.

In the next episode, we’ll talk about how to get started with the JavaScript journey, so stay tuned for that! 

Thank you for watching, and I’ll see you in the next episode.

## Raw YouTube Transcript

hi welcome to otel for beginners my name is Lisa Jung and I'm a member of the otel communication Sig and end user Sig I recently began my journey with otel and as a new V I had a tough time figuring out how to get started I want you to have a different experience so I'll learn alongside you and share what I'm learning through the series depending on which programming language you're working with you'll follow a language specific journey in this series I'll go through the JavaScript journey to get you started with otel before we get our hand dirty let's talk about what otel is why you should consider using it and the resources to get started otel stands for open Telemetry and it plays an important role in observing your system so let's talk about observability first then delve into how otel fits into all of this our modern software systems can consist of complex multi-layered and distributed systems with many interdependent icies a system without observability is like a black box we have no idea what's going on inside so if something goes wrong it's going to be more difficult and more timec consuming to solve the problem with observability we turn this black box into a glass box as a matter of fact it helps you collect the data necessary to visualize and understand what's going on in your system how do we make this possible first you have your infr structure or applications that you want to observe you'll collect data from it and send the data to the observability backend of your choosing then connect the back end to a visualization front end where you can query and use the data that you're interested in the most common types of data collected for observability are metrics logs and traces these are known as Telemetry data getting the Telemetry data into the back end is an important part of understanding your infrastructure or applications and this is where otel comes in otel is an open-source framework using otel you can add software to your applications or systems to generate Telemetry data this process is known as instrumentation then it collects manages and exports Telemetry data to an observability backend the database for storage different aspects of otel makes this process possible and we're going to talk about that more in detail as we go through the JavaScript Journey for now remember that otel is focused on the generation collection management and export of telemetry data you can easily instrument your applications or systems no matter their language infrastructure or runtime environment and the storage and visualization of telemetry are intentionally left to other tools so why should we consider using otel before we answer this question let's talk about something that almost all of us have experienced now if we dig through our doors at home we could probably find a bunch of cables of different types why because the devices we own come from different vendors and each vendor has a specific type of cable and port to charge or connect your Gadget we're all familiar with buying multiple products from the same vendor and investing in additional accessories and apps specifically designed for that product before we know it we get so used to using the line of products that switching over to another vendor could get pretty difficult the product from another vendor May operate differently which will take some time to learn and get used to it would also cost us more money because the additional accessories or apps we invested in don't work with a product from a new vendor this is a problem known as vendor lockin where the costs of switching vendors are so high that customers feel stuck with what they have then things are slowly changing with USBC ports becoming the universal standard let's take the newest model of phones as an example it doesn't matter if you're using an iPhone or an Android you could charge or connect many of these phones with a USBC cable because a universal standard has been set users can use the same cable regardless of how many times they charge their phones otel has similar implications in observability as a USBC does for phones let's do a quick review we have our infrastructure or applications we want to observe we want to collect Telemetry data and send it to an observability backend for storage so this data could be queried and visualized with an observability front end say you have three observability backends to choose from vendors a b and c each vendor often has proprietary instrumentations agents and or collectors now let's say you picked vendor a you're using their proprietary instrumentations agents or collectors and sending the data to its back end but your needs change down the road you want to switch your back end to vendor B but switching vendors is not as simple as you might think you can't just send the existing data from vendor A to B Because vendor B requires its own instrumentation agents or collectors so you can't accept data from vendor A's proprietary instrumentation now your development team has to change their instrumentation possibly to a new proprietary instrumentation of vendor B now imagine doing this for thousands of Linux machines or dozens of applications is a cost of money time and effort worth the benefits of changing vendors as you could see with this setup the cost of switching vendors can get so high that customers can be effectively Locked In by their choices now imagine if all vendors accepted the same standard to send or receive Telemetry data similar to many phone companies accepting USBC as a standard when you switch a vendor you don't need to learn proprietary instrumentations agents or collectors each time you just need one technology and learn a single set of apis and conventions associated with it whatever data you generate with this technology is yours you could send the data to any obser durability back end that accepts the standard so you could easily switch vendors with substantially reduce cost time and effort this is exactly what otel does for you it creates an open standard a set of guidelines rules or specifications to send and receive data there's quite an incentive for the vendors to accept otel many customers now prefer otel to avoid vendor lock in they want to learn a single set of apis and conventions rather than having to learn new on once every time they change a vendor they also want to own their data and send the data to any observability backend that accepts these standards now the vendors benefit from accepting hotel as well customers may be already familiar with using otel there's a Vibrant otel Community who serves as a great resource because of that accepting otel helps the vendors reduce their support and implementation costs on top of that there is even more d for Innovation vendors are receiving the same data so they got to innovate to stand out from the competitors as you can see there are many benefits to accepting Open Standards and you can take advantage of these benefits by using otel now that we covered what otel is and why you should use it let's go over the resources to get started the links to all the resources are included in the description of the video the best place to get started is the otel documentation the the documentation is continuously being improved so the page may look different by the time you watch this video so use a link in the description to check out the latest page the first place in the dog you should start with is the language apis and sdks as I mentioned earlier your otel journey will differ depending on the programming language you're working with select the language of your choice and you should end up on a page that lists all the resources to get started next we have the official otel YouTube channel you'll find helpful videos along with the otel for beginners series on this channel last but not least as you start your otel journey you'll come across a lot of questions we have a huge community of otel users on slack so join the cncf slack Channel post your questions on the open Telemetry Channel and connect with other community members again check the description of this video to access all these resources in the next episode we'll talk about how to get started started with a JavaScript Journey so stay tuned for that thank you for watching and I'll see you in the next episode

