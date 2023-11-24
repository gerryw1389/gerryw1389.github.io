---
title: Lessons Learned
date: 2016-05-29T05:09:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/lessons-learned/
tags:
  - SysAdmin
---
<!--more-->

### Description:

Found this post the other day while browsing Reddit. Very good points!

### To Resolve:

1. If you're doing it more than once, automate. Any task that is worth doing more than once is worth automating. That means you should keep your scripting skills up to date on any platform you have to work on. This will also reduce the chance for mistakes the next time you accomplish this task.

2. Documentation is a process. Document everything. Don't wait until after the project is done to start documenting, do it during. It will be easier for you and more accurate if you don't have to remember things you've done a long time ago. Making documentation a daily part of your routine will lessen the chance you might forget.

3. Generalize as much as possible. Follow the Unix KISS philosophy. Your scripts should be kept simple and do one task well. They should be made generic enough to be reusable as often as possible. Similarly, your documentation should assume a minimum of previous knowledge. Think of someone who is new to the job and needs to be shown how to do something from the ground up.

4. Stay organized. You don't need to read a book about thought management to become more organized. Decide now on how where your scripts will be stored and ensure you always follow the same procedure. Documentation can take many forms, but often the simplest and oldest is best, such as a web portal running a wiki. You don't want to chase down your documentation across sticky notes, emails, text files and so on. Whether you use OneNote, Evernote, or any other solution, you should never have to Google for a solution twice.

5. Patch and monitor. Patching is something that should be a part of your automation. Whether it's desktop systems, servers or software applications, every part of the infrastructure should be automated, and you should have a way to verify that this is happening. If you can't tell at a glance how well the environment you're responsible for is doing, improve your process.

6. Handle security in layers. Security doesn't end at the firewall. Don't leave privileged account passwords in text files. Implementing a password vault is quick and will make a big impact, both in making sure credentials are kept secure, but also serve as part of your documentation. Segment your networks so privileged systems don't co-exist with regular ones. Find the weak points, sandbox your web apps so they don't put the host server at risk. Monitor your firewall rules and IDS/IPS to make sure no unwanted traffic goes through. Make sure your anti-virus software is up to date and educate your users on how to behave in a secure way.

7. Be prepared for the worst. Stay optimistic, but plan for the worst. This means doing proper backups using the 3-2-1 system, having three copies of any important data in two formats, making sure you always keep one copy off-site. Test your restore process, document that process and have a recovery plan that makes sense for your environment. Think up scenarios from software bugs to online attacks, physical breaches, power failures, flooding and fire, and find the best solution for them. People make mistakes, your procedures should keep those mistakes isolated.

8. Keep learning. Don't get set in your ways. Always strive to learn more, and keep a percentage of each year to learn new software, products, or get new certifications. Be ready to handle the next shiny thing or switch role at a moments notice as your business evolves. Take advantage of the incredible amount of free resources from YouTube videos to the Microsoft Virtual Academy, recorded talks at USENIX, DefCon and more.

9. Don't change for changes sake. Don't fall into the trap of wanting to change something just for changes sake. Hype is not a business case. That Perl app may be old, but if it fulfills its task, leave it be. Account for the inevitable delays, cost overruns and scope changes before undertaking any new project. Avoid feature creep and ask yourself if theres a simpler way to accomplish a goal before implementing an overly complex system.

10. Have fun. Don't get burned out. Be respectful to your users and colleagues, but learn to say no. Think about what is most important to you, and how you will think back on these days in 10 years.

### Others:

1. Backups and DR => All our backups are automated; with scripts/code we write. They pipe to postfix and contact us when complete. We have a QA environment which pretty much mirrors prod where we dump our backups into for validation and testing. This happens at the very least, once a month. We have systems in other data centers for DR, which have all the needed infrastructure in place.

2. Test Environment => we have one, it is almost a mirror of prod. All workflows, solutions, config changes, infrastructure changes get tested and validated in QA before they ever touch prod. We have a QA engineer that part of their job is to test out and document what we implement. If an issue is found it gets kicked back to engineering.

3. Monitoring => we have a full on monitoring solution with alerts that monitor all aspects of what we own in our Org. We graph and trend data across time to see the actual impact our changes have. For example, I can track how many queries per a second our databases run, graph it, trend it over time and correlate that to any other changes we make. So when the queries double or triple (hypothetically speaking) I can compare that things we have changed or other events that are being tracked too.

4. End User Experience (UX) => I eat all my own dog food. My client systems are managed by the same tools and solutions we deploy to all of our customers. If there is an experience I hate, I am pretty sure my customers hate it to. I don't build workflows I hate. Yes, I also refer to my end users as customers.

5. Team Building => this is more of a manager's job, but we build a team where there is trust. There is no one person does this, one person does that, we do things as a team. If we fail, we fail as a team, if we succeed we succeed as a team. Management needs to encourage this, and also needs to keep this in mind when adding people to a current team for new job openings.

6. Test everything => If something fails when going to prod we look immediately to how we tested in in QA. Are the results the same? What was different? Add this edge case or unknown to our test cases in QA. Everything gets tested in the test environment first, no matter what it is. In the event it is an emergency (security patch for example) it gets fast tracked to priority 1, but still gets tested first then changed in prod.

7. Create processes that are repeatable, with the same output => so you can automate them. Don't over engineer your solutions, build a process manually you can do, and get the desired result every time, and make sure it is repeatable. Once you build it like this, you automate it. Once you automate it, you monitor it with alerts.

8. Get involved with other teams => if Info Sec sends down a requirement to do X, hop on the phone and call them. Get their requirements, ask them questions, make sure you are all on the same page. Work together, not against each other. 1 billion time easier when everyone gets along.

9. Workflows matter => what works on 5,000 systems may not work on 50,000 systems. Your workflows always have a resource cost and it is multiplicative in regards to how many end points you are working with. Always try to be light weight and flexible when building solutions.

10. Read the manual => self-explanatory, also learn to Google search smarter.

11. Learn everything you can => I am always trying out new tools, products, frameworks, etc. Even if I only have 15 spare minutes in a day between meetings, that is what I do in my free time.

12. Don't Panic! => this does no one any good, and yes it will happen, you will have outages and major issues, but if you freak out and panic it makes it worse. Just accept the situation for what it is and move on toward getting it fixed.

13. Be Humble => don't be a jerk, remember you needed to learn all this stuff once too, nobody is born with this knowledge.

### References:

["What I have learned over the years"](https://www.reddit.com/r/sysadmin/comments/45ctx7/what_i_have_learned_over_the_years/)