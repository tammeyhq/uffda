"""Builds the Uffda Academy static site into ../uffda-site."""
import os, json, html, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
U = "wp-content/uploads/"  # images keep their old WordPress paths

FB_SQUAD = "https://www.facebook.com/ImpossibleTaskSquad/"
FB = "https://www.facebook.com/UffdaAcademy"
IG = "https://www.instagram.com/uffdaacademy/"
LI = "https://www.linkedin.com/company/uffdaacademy"
EMAIL = "events@uffdaacademy.com"

NAV = [("index.html", "Home"), ("classes.html", "Classes"), ("resources.html", "Resources"),
       ("get-help.html", "Get Help"), ("about.html", "About")]


def page(fname, title, desc, body, current=None, og_image=None):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    full_title = "Uffda Academy" if title == "Uffda Academy" else f"{title} · Uffda Academy"
    og = f'<meta property="og:image" content="https://uffdaacademy.com/{og_image}">' if og_image else ""
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(full_title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:site_name" content="Uffda Academy">
{og}
<link rel="icon" href="{U}2022/08/cropped-cropped-Uffda-Academy-ICON-1-270x270.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Graduate&family=Kaushan+Script&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html"><img src="{U}2022/08/UffdaAcademy-Horizontal.svg" alt="Uffda Academy" width="260" height="53"></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="stack">
      <a class="logo" href="index.html"><img src="{U}2023/01/cropped-UFFDA-Logo-White-lettering2.png" alt="Uffda Academy" width="210" height="80"></a>
      <p style="color:#CFCFCF">Learn something new. Do something amazing. Technology, creativity, and practical skills made easier, one step at a time.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="classes.html">Classes</a></li>
        <li><a href="resources.html">Free resources</a></li>
        <li><a href="squad.html">Impossible Task Squad</a></li>
      </ul>
    </div>
    <div>
      <h4>Get in touch</h4>
      <ul>
        <li>{EMAIL}</li>
        <li><a href="get-help.html">Get help</a></li>
        <li><a href="{FB}">Facebook</a> · <a href="{IG}">Instagram</a> · <a href="{LI}">LinkedIn</a></li>
        <li><a href="privacy-policy.html">Privacy policy</a></li>
      </ul>
    </div>
    <p class="fine">© <span data-year>2026</span> Uffda Academy · Fargo–Moorhead · Site managed by <a href="https://tammeybrown.com">Tammey Brown</a></p>
  </div>
</footer>
<script src="site.js"></script>
<script>document.querySelectorAll('[data-year]').forEach(function(e){{e.textContent=new Date().getFullYear()}})</script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(doc)


MEETUP = f"""<section class="band-ink on-ink" aria-label="Next Impossible Task Squad meetup"><div class="wrap meetup">
  <div class="cal"><div class="mon" data-meetup-mon>Nov</div><div class="day" data-meetup-day>13</div><div class="dow">Friday</div></div>
  <div class="stack" style="gap:8px">
    <span class="eyebrow">Next Squad meetup</span>
    <h2 style="font-size:clamp(1.4rem,3.4vw,2rem)" data-meetup-long>Friday, November 13</h2>
    <p style="color:#CFCFCF">The Impossible Task Squad meets the 2nd Friday of every month. Time and place are posted in the Squad on Facebook.</p>
  </div>
  <div class="actions"><a class="btn btn-gold" href="{FB_SQUAD}">Join the Squad</a></div>
</div></section>"""

# ---------- Posts ----------
TAMMEY, SUE = "Tammey", "Sue"

POSTS = [
 dict(slug="quiz-social-media-type"),  # handled separately
 dict(slug="10-essential-steps-to-launching-your-small-business-successfully",
      title="10 Steps to Launching Your Small Business Successfully", author=TAMMEY, date="October 30, 2023",
      img=U+"2023/10/10-Steps-to-Launch-Your-Small-Business.jpg",
      desc="Ten steps to launching your small business, with real-world examples from idea incubation to customer care.",
      body=f"""
<p>Starting a small business is like embarking on a thrilling adventure. You're the captain of your own ship, charting a course through uncharted waters. To ensure a smooth voyage, it's important to have a solid plan in place. Here are <strong><em>10 Steps to Launching Your Small Business Successfully</em></strong>, sprinkled with a touch of humor and some real-world examples. When you approach something with an attitude of <strong><em>this will be fun</em></strong> instead of <em>this is impossible</em>, it makes it so much easier to achieve! So have fun, and we're here for you if you have any questions or we can be of assistance.</p>
<h2>1. Idea Incubation: Hatch Your Great Idea!</h2>
<img src="{U}2023/10/bird-eggs-nest-1541297-1024x682.jpg" alt="Bird eggs in a nest">
<p>Just like a baby bird breaking out of its shell, your business idea needs room to grow.</p>
<p>Whether it's a revolutionary product or a unique service, give it time to incubate. Taking the time to plan and prepare in the beginning saves hours, days or even weeks of time later fixing what you rushed through in the planning stage.</p>
<p>Take the example of the <a href="https://en.wikipedia.org/wiki/Airbnb">Airbnb founders</a>, who turned an air mattress in their living room into a billion-dollar empire. Trust your idea(s)!</p>
<h2>2. Market Research: Spy Like James Bond!</h2>
<p>James Bond wouldn't enter a mission blindfolded, and neither should you. Conduct thorough market research to understand your <a href="https://en.wikipedia.org/wiki/Target_audience">target audience</a>, competition, and industry trends. It's the secret sauce that sets you up for success.</p>
<h2>3. Business Plan: It's Your Treasure Map!</h2>
<p>A business plan is like your treasure map, guiding you through the ups and downs of entrepreneurship. Detail your mission, vision, target market, and financial projections. Need inspiration? Look at how <a href="https://www.benjerry.com/about-us">Ben &amp; Jerry's</a> turned a passion for ice cream into a global phenomenon.</p>
<h2>4. Legal Eagles: Get Your Ducks in a Row!</h2>
<img src="{U}2023/10/chick-duckling-ducks-3743558-1024x682.jpg" alt="A chick and ducklings in a row">
<p>Registering your business (for most small businesses) is as simple as registering your business name with state and local governments.</p>
<p>Legalities may seem like a labyrinth, but they're crucial. Register your business, secure necessary licenses, and protect your intellectual property.</p>
<p>The <a href="https://www.sba.gov/business-guide/launch-your-business/register-your-business"><strong>SBA website</strong></a> can help you find out whether you need to register your business.</p>
<p>Where your business is located and what you do may impact how you need to register, so understanding what you do and how you do it is important.</p>
<p>Even if you don't need to register your business, be aware that if you don't, you could miss out on legal and/or tax benefits and personal liability protection.</p>
<h2>5. Finances: Budget Like a Pro (Or Batman)!</h2>
<p>Batman didn't build the Batmobile without a budget. Manage your finances wisely. Keep track of expenses, set a budget, and explore funding options. Even Batman wouldn't launch a business without financial vigilance. (Yep, my kids taught me to love all the superheroes 😉)</p>
<h2>6. Build Your Brand: Make Your Mark!</h2>
<p>Your brand is your cape; wear it proudly. Create a memorable logo, establish a unique voice, and craft a compelling story. Think about how Apple's sleek logo and "Think Different" mantra transformed the tech industry.</p>
<p><a href="https://www.designsthatdo.com">Be sure to contact Sue for your branding needs!</a></p>
<h2>7. Set Up Shop: Virtual or Brick-and-Mortar?</h2>
<img src="{U}2023/07/welcome-front-store-305504-1024x971.png" alt="A welcoming storefront">
<p>Choosing between an online presence and a physical store is like deciding between teleportation and a scenic road trip.</p>
<p>By considering your product and target audience, you can make a choice that aligns with your business vision.</p>
<p>Take inspiration from the journey of Etsy, which began as an online haven for handmade goods.</p>
<h2>8. Tech Tools: Become a Digital Superhero!</h2>
<p>Embrace technology like your superpower! Utilize tools for accounting, marketing, and customer relationship management.</p>
<p>Just as Iron Man relies on his suit, you'll rely on tech to streamline operations.</p>
<p><a href="http://tammeybrown.com">Tammey</a> specializes in helping creatives get over their fear of tech. Be sure to contact her if you need help in this area.</p>
<img src="{U}2023/01/F10ABE06-908D-435C-99EB-B521F9DD8BC0-1024x768.jpg" alt="">
<h2>9. Spread the Word: Marketing Magic!</h2>
<p>Launching a business is like hosting a party: you want people to know about it! Utilize social media, content marketing, and even old-fashioned flyers to spread the word. Take inspiration from <a href="https://www.youtube.com/watch?v=7dgfk6K5nP0">Dollar Shave Club's viral video</a> that catapulted them into the limelight! <a href="navigating-linkedin-for-business.html">LinkedIn</a>, <a href="smart-hacks-to-reduce-reuse-and-recycle-digital-content-across-social-media.html">Facebook</a>, Instagram and other social media platforms are great ways to reach people.</p>
<h2>10. Customer Care: Treat Them Like Royalty!</h2>
<p>Your customers are your kingdom; treat them accordingly. Provide exceptional service, gather feedback, and build a loyal customer base.</p>
<p>We have many local businesses that are great examples of how to launch a successful small business. Look at <strong><a href="https://chezy.com/">Chezy</a>, <a href="https://thunder.coffee/">Thunder Coffee</a>, <a href="https://www.helloartandsoul.com/">Art &amp; Soul</a>, <a href="https://www.massage-alchemy.com/">Massage Alchemy</a></strong>, and one of our favorite venues in Fargo, <strong><a href="https://cellar624.com/">Cellar 624</a></strong>!</p>
<p>Launching a small business is an exhilarating journey, full of twists and turns. With these 10 steps and a sprinkle of humor, you'll be well prepared to navigate the entrepreneurial seas. Why the humor? Because starting a business takes a lot of time, effort, and YOU!</p>
<h2>Just Getting Started?</h2>
<p>If you haven't begun your journey yet, there are several simple things you can do before diving into business planning. Here are a few to consider:</p>
<ol>
<li><strong>Identify your passion and skills:</strong> Start by reflecting on what you are truly passionate about and the skills you possess. Consider how you can align these with a potential business idea.</li>
<li><strong>Conduct market research:</strong> Understand the market you are entering. Analyze your target audience, competitors, and industry trends. This will help you identify opportunities and potential challenges. Research local businesses to see what's already there and what's missing!</li>
<li><strong>Define your unique value proposition:</strong> Determine what sets your business apart from competitors. Identify your unique selling points and how you can provide value to your customers.</li>
<li><strong>Build a strong network:</strong> Surround yourself with like-minded individuals, mentors, and professionals who can offer guidance and support. Attend networking events, join relevant communities, and connect with industry experts.</li>
<li><strong>Develop a business plan:</strong> Create a comprehensive business plan that outlines your goals, strategies, target market, financial projections, and marketing approaches. This will serve as a roadmap for your business.</li>
<li><strong>Financial preparation:</strong> Understand the financial aspects of starting a business. Evaluate your budget, determine startup costs, and explore funding options such as loans, grants, or crowdfunding.</li>
<li><strong>Reach out to successful business owners</strong> and ask them what their top ten steps would be and what advice they would have for someone starting out like you.</li>
</ol>
<p>Remember, starting a business requires careful planning and dedication. By considering the points above, you can set a strong foundation for your superhero role!</p>
<h2>Top 10 Resources for Small Business</h2>
<p>I did a little research to get you started. Here are ten potential options to help you on your journey (in no particular order). Please feel free to reach out if you know of one that I should add.</p>
<ol>
<li><strong><a href="https://www.sba.gov/district/north-dakota">Small Business Development Center (SBDC)</a>:</strong> Provides guidance, training, and resources for small business owners.</li>
<li><strong><a href="https://www.score.org/prairieandlakes">SCORE</a>:</strong> Offers free mentoring and counseling services by experienced business professionals.</li>
<li><strong><a href="https://www.fmwfchamber.com/">The Chamber: Fargo, Moorhead &amp; West Fargo Chamber of Commerce</a>:</strong> Provides networking events, business resources, and advocacy.</li>
<li><strong><a href="https://www.emergingprairie.com/">Emerging Prairie</a>:</strong> Supports entrepreneurship and innovation through events, resources, and community building.</li>
<li><strong><a href="https://www.emergingprairie.com/startupbrew-fargo/">StartupBREW Fargo</a>:</strong> A morning meetup for entrepreneurs, innovators, creatives, and community members to come together and explore the entrepreneurial journey.</li>
<li><strong><a href="https://www.ndwbc.com/">North Dakota Women's Business Center</a>:</strong> Focuses on empowering women entrepreneurs through training, counseling, and resources.</li>
<li><strong><a href="https://www.sba.gov/">Small Business Administration (SBA)</a>:</strong> Offers various programs, loans, and resources to support small businesses.</li>
<li><strong><a href="https://gfmedc.com/">Economic Development Corporation (EDC)</a>:</strong> Provides assistance, incentives, and resources for business expansion and relocation.</li>
<li><strong>Local universities and colleges:</strong> Many institutions offer entrepreneurship programs, business incubators, and resources for startups.</li>
<li><strong>Professional associations:</strong> Industry-specific associations can provide networking opportunities, resources, and support for small businesses.</li>
</ol>
<p>This isn't an exhaustive list, so research each organization to see which ones align best with your specific needs and goals.</p>
<p>Remember, every business hero had to start somewhere. So put on your entrepreneur's cape and fly!</p>
"""),
 dict(slug="navigating-linkedin-for-business", title="Navigating LinkedIn for Business", author=SUE, date="April 3, 2023",
      img=U+"2023/04/Navigating-LinkedIn-Uffda-Blog.png",
      desc="LinkedIn isn't just for job hunting anymore. Set up and use your business page to build local awareness and real connections.",
      body="""
<h2>Is Your Business on LinkedIn?</h2>
<p><strong><em>LinkedIn isn't just about finding a new job anymore.</em></strong></p>
<p>It's become a networking platform to make business-focused human connections within your company, peers, or vendors.</p>
<p><strong>There are 2 parts to representing your business online:</strong></p>
<ol>
<li>A personal page to represent you, your skills, and your career.</li>
<li>A business page to represent your business brand, culture, events, products &amp; services.</li>
</ol>
<p>You may be starting from scratch on both, or you may need to do an overhaul on your pages.</p>
<p>Either way, when you interact with anyone (like, share, or post), all of your followers will see your interactions.</p>
<p><strong>Pro tip:</strong> If you are responsible for your business page, make sure you are interacting with authenticity, clarity, and staying true to your company's values. That way no one can find fault with your page's content when comparing it with your interactions. Being consistent in the way you represent yourself and your brand is key.</p>
<h3>Checklist for Setting Up Your Business Page</h3>
<ul>
<li>Create or gain access to your company page (<a href="https://www.linkedin.com/help/linkedin/answer/a569092/request-admin-access-to-a-linkedin-page?lang=en">if you don't have access, here's how to get it</a>)</li>
<li>Add company name</li>
<li>Add your logo</li>
<li>Add your location</li>
<li>Add a description of your company or venue</li>
<li><a href="https://www.linkedin.com/help/linkedin/answer/a570177">Choose a custom URL</a></li>
<li>Add a cover photo (not your logo)</li>
<li>Company description (include keywords)</li>
<li>Showcase your services</li>
<li>Contact info (phone, email, website)</li>
</ul>
<h2>3 Ways To Use Your LinkedIn Business Page for Business</h2>
<h3>Build Local Brand Awareness</h3>
<p>Your LinkedIn business page is a free billboard. LinkedIn is a great platform to showcase your brand, culture, and mission. What hours do you have? How many employees? You can also highlight any company achievements or recognition you receive. This helps to build your brand and increase your visibility.</p>
<h3>Connect With Your Communities</h3>
<h4>Internal community = employees</h4>
<p>When your leadership team, employees, and staff have a central, trusted source of public info to share with others, they will!</p>
<h4>External community = potential clients, other local businesses, industry peers, vendors</h4>
<p>LinkedIn allows you to connect with your audience and build relationships with your customers. Share industry news, insights, and tips that your audience will find valuable. You can also engage with your followers by responding to comments and messages. This helps to build trust and loyalty with your customers.</p>
<h3>Connect Your Online Content</h3>
<p><strong>LinkedIn is a powerful tool to drive traffic to your website, to your events, and to your door (if you're a brick-and-mortar store).</strong></p>
<p>Make sure your business page includes links to your website in your posts and in the "About" section of your LinkedIn business page. You can also use LinkedIn's advertising platform to promote your products or services and drive traffic to your website. By increasing your website traffic, you can generate more leads and ultimately increase your sales.</p>
<h3>Checklist for LinkedIn Content</h3>
<ul>
<li>Link your LinkedIn page to your website</li>
<li>Add the About Us section, with your services &amp; industry keywords</li>
<li>Link to your Google reviews</li>
<li>Ask clients for LinkedIn reviews</li>
<li>Post &amp; share relevant and trustworthy content</li>
<li>Add connections that make the most sense (co-workers, vendors, clients, industry peers)</li>
<li>Don't feel pressured to add people if you don't know them or they seem spammy</li>
<li>Like or share your clients' posts to celebrate their wins or insights</li>
<li>Consistent posting is key</li>
<li>Consider scheduling your LinkedIn business posts with a third-party scheduler (Hootsuite, CoSchedule) or schedule within LinkedIn</li>
</ul>
"""),
 dict(slug="smart-hacks-to-reduce-reuse-and-recycle-digital-content-across-social-media",
      title="Smart Hacks to Reduce, Reuse, And Recycle Digital Content Across Social Media", author=SUE, date="January 24, 2023",
      img=U+"2023/01/Smart-Hacks-Uffda-Blog--1024x576.png",
      desc="Don't start from a blank page. Reduce, reuse, and recycle the content you already have across social media.",
      body="""
<h2>Is there anything more terrifying than creating original content?</h2>
<p>Do you ever wonder "What the heck am I going to write for my social media this month?"</p>
<p>Don't panic. Chances are you've already got some GOLD that you can reuse in a new and interesting way.</p>
<p>You have a message. And different people will be looking at your content every day. Some of them are your KEY DEMOGRAPHIC, some of them will be your biggest fans, and some of them will need converting. It's OK to repurpose your message for different times, reframe it for different audiences, and reintroduce the same concepts with different ways of saying the same thing.</p>
<h3>First, LOOK at all the different types of content platforms out there:</h3>
<p><strong>Traditional:</strong> TV, magazines, radio, billboards</p>
<p><strong>Digital:</strong> Blogs, forums, websites, social media, and video or audio streaming sites.</p>
<p><strong>Focusing on the digital side, what kind of things live on those content platforms?</strong></p>
<p>Stories, posts, podcasts, songs, discussions, polls, videos, how-tos, behind-the-scenes, illustrations, graphics, photos, screenshots, reviews, &amp; reactions. WHEW. That's a ton of digital content that already exists!</p>
<h3>Second, LISTEN to Austin Kleon and "Steal Like an Artist."</h3>
<p>That is, if you're sharing someone else's work, credit them. Don't steal a single person's idea (bad). Instead, steal LOTS of people's ideas, mix them all together, and create something NEW (good).</p>
<blockquote>"Every new idea is just a mashup or a remix of one or more previous ideas." – Austin Kleon, <em>Steal Like an Artist</em></blockquote>
<h3>Third, START with a non-blank page or canvas.</h3>
<p>It's so easy to fear writing or creating content when you're faced with that pristine blank nothingness.</p>
<p>What can you do to start with something instead of that nothingness?</p>
<h4>Starter Hack #1</h4>
<p>Set a timer and scroll through your own blogs or other people's posts. Then, for anything that sparks your interest, take notes or copy/paste it into your Google Doc, spreadsheet, or Word doc. You've got a ton of interesting ideas ready to take apart and put back together, like a collage of something new.</p>
<h4>Starter Hack #2</h4>
<p>Already have an idea?</p>
<p>Record a conversation with a friend about your idea. Have them ask you questions, and talk it out. Now you've got the basic structure for your new blog post (or audio) ready to go!</p>
<h4>Starter Hack #3</h4>
<p>Do a Google search for "What [Millennials] Need to Solve for [Career Advancement] by [Personal Branding]" (replace the brackets with your target audience, their problem, and your service or product).</p>
<p>What questions are people asking? What is their end goal? What do other experts say? What are your experiences? How does your product or service help solve the problem in a different way?</p>
<h4>Hack #4</h4>
<p>Create a "reaction video," review, or blog post about someone else's idea, product, or method. Do you have a very expressive face? Perfect. Film that. Here's a great <a href="https://clipchamp.com/en/blog/youtube-reaction-videos/">how-to from Clipchamp</a>.</p>
<h2>When it comes to content writing: REDUCE, REUSE, RECYCLE</h2>
<h3>Reduce</h3>
<p>You don't have to reinvent the wheel every time you create posts for social media.</p>
<p>The social media golden ratio is 30, 60, 10:</p>
<p>30% owned (original thought)<br>60% curated<br>10% promotional</p>
<p>When you create, think: this is less about what I have to say than what I can show, tell, or ask.</p>
<h4>Reduce Hack #1</h4>
<p><strong>ASK:</strong> Create social media polls. Use questions from your blog posts or webinars to create polls on social media platforms.</p>
<h4>Reduce Hack #2</h4>
<p><strong>SHOW:</strong> The process is the product. Share behind-the-scenes photos or videos of the process of creating your digital content.</p>
<h4>Reduce Hack #3</h4>
<p><strong>TELL:</strong> Share testimonials or positive feedback you've received about your digital content on social media. (<em>Psst… this makes easy video content.</em>)</p>
<h3>Reuse</h3>
<h4>Reuse Hack #1</h4>
<p>Create social media graphics: Take screenshots of key points from your blog posts or webinars and turn them into shareable graphics.</p>
<h4>Reuse Hack #2</h4>
<p>Use quotes from your content: Share quotes from your blog posts, webinars, or videos as standalone social media posts.</p>
<h4>Reuse Hack #3</h4>
<p>Use excerpts from your content: Share a short excerpt from your blog post or webinar as a teaser to encourage people to read or watch the full content.</p>
<h4>Reuse Hack #4</h4>
<p>Use snippets from your video content: Share short clips from your videos as Instagram Reels, YouTube Shorts, or TikToks.</p>
<h3>Recycle</h3>
<h4>Recycle Hack #1</h4>
<p>Repurpose your own blog posts: Take the main points or key takeaways from your blog posts and share them as a series of short posts.</p>
<h4>Recycle Hack #2</h4>
<p>Create infographics: Take key data or statistics from your blog posts or research and turn them into shareable infographics.</p>
<h4>Recycle Hack #3</h4>
<p>Create a series: Break your longer brochure, blog, or web info into smaller chunks and share it as a series of social media posts.</p>
<h2>Quick Recap</h2>
<p>Creating content for the upcoming year doesn't have to be scary when you don't start with a blank page.</p>
<ul>
<li>Remember the 30, 60, 10 golden ratio of digital content: 30% owned content, 60% curated (shared or reshared), 10% promotional.</li>
<li>If you share someone's content, credit or link to them.</li>
<li>If you steal, steal like an artist (collage multiple influences to make something new).</li>
<li>Repurpose your message for different audiences, at different times, or using different mediums across different platforms.</li>
<li>Start with a non-blank page: use screenshots, snippets, and stories to rewrite, review, and react.</li>
<li>Reduce, reuse, and recycle.</li>
</ul>
"""),
 dict(slug="write-when-feeling-inspired", title="Overcoming Writer's Block", author=TAMMEY, date="January 10, 2023",
      img=U+"2022/08/telework-technology-laptop-6795505.jpg",
      desc="Overcoming writer's block is easy once you know the tricks: when and where to write, and five ways to get inspired.",
      body=f"""
<h2>Write When Inspired!</h2>
<p>Overcoming writer's block is easy, once you know the tricks! There are many sources of inspiration for writing!</p>
<p>You can be inspired by music, nature, art, conversations, commercials, billboards, or even what others are writing about!</p>
<p>Even conversations you have with friends can spark an idea. Finding what inspires you personally is the key to unlocking your creativity!</p>
<h2>Knowing What to Write</h2>
<p>Coming up with blog posts can be a challenge, but there are a few things you can do to make the process easier. First, brainstorm topics that are relevant to your audience. Research popular trends and topics in your industry, and think of ways you can provide your unique perspective. Once you have some ideas, it's time to get creative!</p>
<p>Take those ideas and fill in your <a href="what-is-a-content-calendar.html">content calendar</a>!</p>
<p>Brainstorm headlines, titles, and visuals that will make your post stand out. Finally, take the time to craft a well-written, engaging post that will captivate your readers. If you need help getting started, try using templates or other examples to guide your ideas and structure. With a little bit of effort and creativity, you can come up with great blog posts that your readers will love!</p>
<p><strong>Techie answer:</strong> Monitor your analytics to determine what types of posts your audience is most attracted to.</p>
<p><strong>Non-techie answer:</strong> Write about what inspires you within the guidelines of your niche (topic/area/interest).</p>
<h2>Knowing When and Where to Write</h2>
<p>Where do you work the best? Do you like it quiet? Maybe you'd prefer going to the library.</p>
<p>Do you like it busy? Perhaps a coffee shop or the mall is a better place for you.</p>
<p>Are you a morning person or a night owl?</p>
<p>No matter what your best place and time is, don't fight it! Embrace it instead. Know what's best for you and act on it.</p>
<p>Set a time and place, grab your writing utensil and content calendar, and get to work. If you PLAN AHEAD, you can scour your content calendar for what you feel inspired to write about and get to writing.</p>
<p>It's OK if what you end up writing about isn't due until later; just schedule it out.</p>
<p>Did you have something scheduled that doesn't feel right now? That's OK. What does? The calendar is meant to give direction and focus, but it's not set in stone. If you write something different, just change it in your calendar.</p>
<p>If you have the perfect place and the right time but nothing is coming, try free writing (write whatever comes to mind) or write about the topic as if you were describing it to a specific person. Sometimes that will spark an idea and you'll be inspired to create your content!</p>
<h2>Overcoming Writer's Block</h2>
<p>Some excel under pressure while others don't. Either way, knowing what you're going to write about is very helpful and half the battle!</p>
<p>A <a href="what-is-a-content-calendar.html"><strong>content calendar</strong></a> is a great way to keep organized, know what's coming, and find inspiration! Once you have all of your important dates in, you can fill in the other dates with ideas to make it easy when it comes time to write!</p>
<p>Even with all of this great planning, sometimes you may not feel inspired to write. Stress, being overly tired or hungry, or overwhelm may get in the way. There are a few tricks I've learned to help get over the block.</p>
<h2>5 Tricks to Inspire</h2>
<img src="{U}2023/04/Feedback-and-support-canva-workshop-1024x640.jpg" alt="A group working together at a Canva workshop">
<p><strong>1) Brainstorm with others.</strong> It's an amazing way to develop ideas easily and creatively! Even gathering with others in the same field as you will help inspire new ideas, as each of you will add your own flair to the topic. Networking events and the <a href="squad.html">Impossible Task Squad</a> are great ways to connect and be inspired!</p>
<p><strong>2) Take a break</strong> from writing and do something else creative or fun. This can help spark your creativity and motivation.</p>
<p><strong>3) Keep a voice recorder or notebook</strong> to capture those thoughts, ideas, and inspirations while on the go! You can also use talk-to-text in Google Docs and other programs.</p>
<p><strong>4) What have you written before?</strong> Read through the material you've already written. You may find something you can use, or something that leads you to a new idea.</p>
<p><strong>5) Change your environment.</strong> Take a walk outside, go swimming, dance wildly, sing loudly, call a friend, vacuum, or do that task you've been putting off. Fresh air can help you clear your head and refocus your energy, and stepping away may give you the break you need to feel refreshed.</p>
<h2>Still Need Help?</h2>
<p>Have you heard of <a href="https://partner.canva.com/c/2644198/1559937/10068"><strong>Canva</strong></a>? It's more than just a graphic and image powerhouse. Its writing assistant, <a href="https://partner.canva.com/c/2644198/1559937/10068">Magic Write</a>, is great for brainstorming first ideas and rough drafts of social posts, business plans, product descriptions, and more, which you can then proof and edit in your own voice.</p>
<h2>Look Through What You Wrote</h2>
<a href="https://www.creativefabrica.com/product/calendar-42/ref/237596/"><img src="{U}2022/12/1-01-1024x768.png" alt="Printable content calendar"></a>
<p>Keeping a list of content is a great way to easily recall what you've written about, and it also makes it easy to link back to that information from other sources.</p>
<p>Scan through what you've written before to get new ideas using the who, what, when, where, and why trick. If you wrote about HOW to do something, could you write about WHY?</p>
<h2>Quick Recap</h2>
<p><strong>PLAN:</strong> Know the best place for you to create content, and use it.</p>
<p><strong>TIME:</strong> Set aside time to create your content.</p>
<p><strong>WRITE:</strong> If you feel like writing about something, do!</p>
"""),
 dict(slug="what-is-a-content-calendar", title="What is a Content Calendar?", author=TAMMEY, date="December 31, 2022",
      img=U+"2023/03/Title-Page-1024x576.jpg",
      desc="A content calendar helps you stay organized and plan content in advance. Here's what it is and five tips for creating one.",
      body=f"""

<h2>What is a Content Calendar?</h2>
<img src="{U}2022/12/Content-Calendar-Planning-Image-1.jpg" alt="Content calendar planning">
<p>A content calendar is a great way to stay organized and plan out your content in advance. It's a tool that allows you to map out the topics, mediums, and dates you plan to use to create and distribute content.</p>
<h2>Plan Ahead, Make Deadlines</h2>
<p>By having a content calendar, you can ensure that you are regularly creating and sharing content that is relevant to your audience.</p>
<p>Additionally, it allows you to plan ahead and ensure that you don't miss any deadlines.</p>
<p><strong>Techie answer:</strong> A tool to help keep you organized and focused on what you want to share.</p>
<p><strong>Non-techie answer:</strong> A calendar of topics and themes to use as a guideline when creating social media and blog posts.</p>
<h2>5 Tips for Content Creation</h2>
<p>There are 5 easy tips to help you create your content calendar.</p>
<ol>
<li>Create a consistent posting schedule</li>
<li>Brainstorm ideas before you sit down to your calendar to offer more choices</li>
<li>Understand what content resonates with your audience</li>
<li>Tailor your content to your audience</li>
<li>Keep your content fresh and created by you</li>
</ol>
<img src="{U}2022/12/Content-Calendar-Planning-Image-2-Calendars.jpg" alt="Calendars for content calendar planning">
<p>I recommend creating your content calendar on paper to allow easy viewing, changes, and updates, and to clearly see what you have planned for the month.</p>
<p>Be sure to include personal and professional dates that impact your calendar.</p>
<h2>Any calendar will work. It just needs to be accessible and easy to read.</h2>
<a href="https://www.creativefabrica.com/product/calendar-42/ref/237596/"><img src="{U}2022/12/1-01-1024x768.png" alt="Printable content calendar"></a>
<p>Have you ever worked for hours on a blog post only to find out later you'd already written about that?</p>
<p>Keeping a list of topics and categories is a great way to easily recall what you've written about, and it also makes it easy to link back to that information from other sources.</p>
<h2>Brainstorm Ideas</h2>
<p>Brainstorm ideas for your posts, shares, and blogs. What do you want your audience to get from your sharing? Keep a list of your categories to help keep you focused.</p>
<p>Do you belong to a networking group? This is a great time to get together with other like-minded people and brainstorm content ideas. It's OK if you all end up with a few of the same ideas on your calendars, as you'll each create unique content for your audiences.</p>
<h2>Recap</h2>
<p>A content calendar is simply a planning tool to keep you on track for what you want to share and to get it scheduled to avoid scattered posting.</p>
<p>Brainstorm and fill in your calendar. The calendar helps you plan, focus, and see what you have coming up and what you've shared in the past.</p>
<p>Keep a list of previous blog posts, vlogs, and podcasts to make it easier to link back to related content. This gives your current content a better ranking with search engines (like Google).</p>
<p>When you feel inspired to write or create, look at your content calendar for upcoming topics and create based on what's on there.</p>
<p><strong>BOOM!</strong> Easy-peasy content creation.</p>
<p>Need help brainstorming ideas or filling in your calendar? Bring it to the <a href="squad.html">Impossible Task Squad</a>!</p>
"""),
 dict(slug="what-is-a-vector-graphic", title="What is a Vector Graphic?", author=TAMMEY, date="June 28, 2022",
      img=U+"2022/06/Vector-Graphic.jpg",
      desc="What a vector graphic is, why it can be resized without losing quality, and why your brand kit should use them.",
      body=f"""
<h2>What is a Vector Graphic? Do I need one?</h2>
<p>If you've done any marketing or graphic design, you've no doubt come across the term "<strong>vector graphic</strong>," but what exactly is it?</p>
<p>Why do you need one? Where do you get one? What is it?</p>
<p><strong>Techie answer:</strong> A vector graphic is a type of image that is composed of mathematical points, making it resolution-independent and very scalable.</p>
<p><strong>Non-techie answer:</strong> A vector graphic is a type of digital image created using mathematical points to create an object (like the ones in this image).</p>
<p>This makes them perfect for use in print and digital media, where high quality and clarity are essential.</p>
<p>Many people consider vector graphics just for high-end marketing gurus or gamers. That's not true. They are <strong>easy-to-create images</strong> that allow you to scale, edit, and customize your image. Let's take a closer look at vector graphics and explore some of the best ways to use them in your marketing.</p>
<h2>Vector Graphics Offer Clarity and Customization</h2>
<img src="{U}2022/06/Vector-Graphic-1.jpg" alt="Examples of simple vector graphics: a tree, a peacock feather and a cityscape">
<p>A vector graphic is a computer-generated image made up of points, lines, and curves called "<strong>vectors</strong>."</p>
<p>Vectors and pixels are not the same. Other file types may cause <a href="https://en.wikipedia.org/wiki/Pixel">pixelation</a> when you try to scale the image.</p>
<p>Vectors are created by applying mathematical equations to points in a two-dimensional (2D) or three-dimensional (3D) space. Images made up of vectors can be scaled (sized) up or down <em>without losing quality</em>, making them a popular choice for logos and other graphics that need to be resized often. In contrast, raster images, such as JPEGs and PNGs, consist of millions of tiny squares called pixels, which can become blurry when enlarged.</p>
<p>Vector graphics can also be easily edited and customized, making them a versatile tool for marketing materials. If you're looking for clean, high-quality visuals for your next campaign, consider using vector graphics!</p>
<h2>Did you catch that? Vector graphics can be resized up or down WITHOUT losing quality!</h2>
<img src="{U}2022/06/Vector-Graphic-2-1024x682.jpg" alt="Vector graphic example">
<p>Have you ever worked for hours on an image, only to find when you needed to use it for something else that you couldn't size it?</p>
<p>Or you used an image you thought would be OK, but your printer said it didn't display correctly?</p>
<h2>Brand Kits Prefer Vector Graphics</h2>
<p>A brand kit takes the guesswork out of branding, and vector versions of your logo and graphics are what keep it looking sharp everywhere, from a social post to a banner.</p>
"""),
]

for p in POSTS:
    if "body" in p:
        p["body"] = p["body"].replace("{U}", U)

CARD_ORDER = ["10-essential-steps-to-launching-your-small-business-successfully", "navigating-linkedin-for-business",
              "smart-hacks-to-reduce-reuse-and-recycle-digital-content-across-social-media", "write-when-feeling-inspired",
              "what-is-a-content-calendar", "what-is-a-vector-graphic"]
BY = {p["slug"]: p for p in POSTS if "body" in p}


def card(p):
    return f"""<a class="post-card" href="{p['slug']}.html">
  <div class="thumb"><img src="{p['img']}" alt="" loading="lazy"></div>
  <h3>{html.escape(p['title'])}</h3>
  <span class="by">By {p['author']}</span>
</a>"""


SQUAD_CTA = f"""<div class="post-cta">
  <span class="eyebrow">Uffda Academy</span>
  <h3>Want help with this?</h3>
  <p>Learn at your own pace with a short class, or get one-on-one help with your own project.</p>
  <div class="actions"><a class="btn btn-gold" href="get-help.html">Get help</a><a class="btn" href="classes.html">Browse classes</a></div>
  <p class="note">Need help creating your logo? <a href="https://www.designsthatdo.com/logos">DesignsThatDo.com</a> is your answer!</p>
</div>"""

# Post pages
for i, slug in enumerate(CARD_ORDER):
    p = BY[slug]
    prev_p = BY[CARD_ORDER[i - 1]] if i > 0 else None
    next_p = BY[CARD_ORDER[i + 1]] if i + 1 < len(CARD_ORDER) else None
    nav = '<nav class="post-nav" aria-label="More posts">'
    nav += f'<a href="{prev_p["slug"]}.html">← {html.escape(prev_p["title"])}</a>' if prev_p else "<span></span>"
    nav += f'<a href="{next_p["slug"]}.html">{html.escape(next_p["title"])} →</a>' if next_p else '<a href="resources.html">All resources →</a>'
    nav += "</nav>"
    body = f"""<header class="article-head band-ink on-ink inked" data-ink="edge" data-ink-seed="{i+3}"><div class="wrap"><div class="stack">
    <a class="eyebrow" href="resources.html" style="background:none">Free guide</a>
    <h1>{html.escape(p['title'])}</h1>
    <p class="meta">By {p['author']} · {p['date']}</p>
  </div></div></header>
<article><div class="wrap" style="padding-block:0 72px">
  <div class="article-hero"><img src="{p['img']}" alt=""></div>
  <div class="prose">{p['body']}</div>
  {SQUAD_CTA}
  {nav}
</div></article>"""
    page(f"{slug}.html", p["title"], p["desc"], body, current="resources.html", og_image=p["img"])

# ---------- Quiz ----------
QUIZ = [
 ("When you share about your business, what feels most natural?", [
   ("Snapping a quick photo or short video", ["instagram", "tiktok"]),
   ("Writing a few thoughtful paragraphs", ["linkedin", "facebook"]),
   ("Recording a longer video that explains how to do something", ["youtube"]),
   ("Creating pretty, saveable graphics and idea boards", ["pinterest"])]),
 ("How do you feel about being on camera?", [
   ("Love it, put me in front of the camera", ["tiktok", "youtube"]),
   ("Fine in small doses", ["instagram", "facebook"]),
   ("I'd rather stay behind the scenes", ["linkedin", "pinterest", "facebook"])]),
 ("Who are your customers, mostly?", [
   ("Local folks: neighbors, families, my community", ["facebook"]),
   ("Other businesses and professionals", ["linkedin"]),
   ("Shoppers who love visuals: home, food, fashion, crafts", ["instagram", "pinterest"]),
   ("A younger crowd, mostly under 35", ["tiktok", "instagram"]),
   ("People searching for how to do something", ["youtube", "pinterest"])]),
 ("How much time can you give social media each week?", [
   ("Under an hour", ["pinterest", "linkedin"]),
   ("One to three hours", ["facebook", "instagram", "linkedin"]),
   ("Three or more, and I'd enjoy it", ["tiktok", "youtube"])]),
 ("Which part would you enjoy most?", [
   ("Chatting in the comments and building relationships", ["facebook", "linkedin"]),
   ("Making things look beautiful", ["pinterest", "instagram"]),
   ("Teaching and explaining", ["youtube", "linkedin"]),
   ("Being playful and trying what's trending", ["tiktok"])]),
 ("What's your main goal right now?", [
   ("Bring people to my door or my events", ["facebook"]),
   ("Win clients, partners, or referrals", ["linkedin"]),
   ("Sell products", ["instagram", "pinterest"]),
   ("Get discovered by lots of new people quickly", ["tiktok"]),
   ("Become the go-to expert in my field", ["youtube", "linkedin"])]),
 ("How long should a post keep working for you?", [
   ("A day in the spotlight is fine", ["tiktok", "instagram"]),
   ("A few days of good conversation", ["facebook", "linkedin"]),
   ("I want it found for months, even years", ["pinterest", "youtube"])]),
 ("What would your best content be?", [
   ("Before-and-after photos", ["instagram", "pinterest"]),
   ("Tips and lessons I've learned", ["linkedin", "facebook"]),
   ("Behind-the-scenes moments and personality", ["tiktok", "instagram"]),
   ("Step-by-step tutorials", ["youtube", "pinterest"])]),
 ("Trends, music, and memes are…", [
   ("So fun, count me in", ["tiktok", "instagram"]),
   ("OK once in a while", ["facebook", "instagram"]),
   ("Not my thing", ["linkedin", "pinterest", "youtube"])]),
 ("If you had to pick one, you're a…", [
   ("Writer", ["linkedin", "facebook"]),
   ("Photographer or designer", ["instagram", "pinterest"]),
   ("Talker or performer", ["tiktok", "youtube"])]),
]
PLATFORMS = {
 "facebook": dict(name="Facebook", why="You're a relationship builder with a local heart. Facebook is where communities, neighbors, and groups gather, and it rewards conversation more than polish.",
   start=["Set up a business Page with your hours, location, and a clear cover photo.", "Post two or three times a week: local news, customer stories, and what's coming up.", "Create Events for anything people can attend, and join a local group or two to be helpful in."],
   time="1–2 hours a week", guide=None),
 "instagram": dict(name="Instagram", why="You think in pictures and like things to look good. Instagram is built for visual storytelling, from polished posts to quick behind-the-scenes Stories.",
   start=["Write a bio that says who you help and add a link to your website.", "Post your best photos and short Reels a few times a week.", "Use Stories for everyday behind-the-scenes moments; they don't need to be perfect."],
   time="2–3 hours a week", guide=None),
 "linkedin": dict(name="LinkedIn", why="You're thoughtful, professional, and good with words. LinkedIn rewards expertise and real relationships, and a few good posts go a long way.",
   start=["Polish your personal profile first, then set up a company Page.", "Share one helpful tip or lesson learned each week.", "Connect with clients, vendors, and local peers, and comment on their posts."],
   time="1 hour a week", guide=("navigating-linkedin-for-business.html", "Navigating LinkedIn for Business")),
 "tiktok": dict(name="TikTok", why="You're playful, comfortable on camera, and happy to try new things. TikTok can put a brand-new account in front of thousands of people quickly.",
   start=["Watch for a week to learn the style before you post.", "Film short, real videos: tips, behind-the-scenes, quick before-and-afters.", "Post consistently and reply to comments with new videos."],
   time="3+ hours a week", guide=None),
 "pinterest": dict(name="Pinterest", why="You're a visual planner who'd rather create once and let it keep working. Pinterest is really a search engine, and good pins send people to your website for months.",
   start=["Set up a business account and claim your website.", "Create boards for the topics your customers search for.", "Make tall, clear pin graphics (Canva is perfect) that link back to your site."],
   time="Under an hour a week", guide=None),
 "youtube": dict(name="YouTube", why="You love to teach and explain. YouTube is the world's how-to library, and a good tutorial can bring you new people for years.",
   start=["Make a list of the questions customers ask you most; each one is a video.", "Start simple: your phone, good light, and clear audio.", "Use titles that match what people type into search."],
   time="2–4 hours a week", guide=None),
}
ORDER = ["facebook", "instagram", "linkedin", "pinterest", "youtube", "tiktok"]

qs = []
for i, (q, opts) in enumerate(QUIZ, 1):
    o = "".join(
        f'<input type="radio" id="q{i}-{j}" name="q{i}" value="{" ".join(pl)}"><label for="q{i}-{j}">{html.escape(t)}</label>'
        for j, (t, pl) in enumerate(opts))
    qs.append(f'<fieldset class="q"><legend>{html.escape(q)}</legend><div class="choices">{o}</div></fieldset>')
quiz_body = f"""<header class="article-head band-ink on-ink inked" data-ink="edge" data-ink-seed="21"><div class="wrap"><div class="stack">
    <span class="eyebrow">Free quiz · 10 questions · about 3 minutes</span>
    <h1>Which social media <span class="script gold" style="font-size:1.05em">fits you?</span></h1>
    <p style="color:#CFCFCF;max-width:62ch">You don't need to be everywhere. Answer 10 quick questions about your personality and your business, and find the platform that suits you best, plus exactly where to start.</p>
  </div></div></header>
<section><div class="wrap stack-lg">
  <form class="quiz" id="quiz-form" novalidate>
    {''.join(qs)}
    <div class="quiz-bar">
      <span id="quiz-progress" aria-live="polite">0 of {len(QUIZ)} answered</span>
      <div class="actions"><button type="reset" class="btn">Start over</button><button type="submit" class="btn btn-gold">Show my platform</button></div>
    </div>
  </form>
  <div class="result" id="quiz-result" hidden aria-live="polite">
    <span class="eyebrow">Your best fit</span>
    <div class="type" data-type></div>
    <p data-why></p>
    <h3>Start here</h3>
    <ol data-start></ol>
    <p><strong>Time to plan for:</strong> <span data-time></span></p>
    <p data-guide hidden></p>
    <div class="runner"><span class="eyebrow">Runner-up</span> <strong data-runner></strong> <span data-runner-why></span></div>
    <p class="note">Start with one platform and do it well before adding another. Want help getting set up? <a href="get-help.html">Get help</a>, or read <a href="smart-hacks-to-reduce-reuse-and-recycle-digital-content-across-social-media.html">how to reuse your content across platforms</a>.</p>
  </div>
</div></section>
<script type="application/json" id="quiz-platforms">{json.dumps(dict(order=ORDER, platforms=PLATFORMS))}</script>"""
page("quiz-social-media-type.html", "Which Social Media Fits You?",
     "A free 10-question quiz that matches your personality and business to the social media platform that suits you best, with steps to get started.",
     quiz_body, current="resources.html")

# ---------- Home ----------
cards3 = "".join(card(BY[s]) for s in CARD_ORDER[:3])
POSTER = f"""<section class="hero-logo band-ink"><div class="wrap">
  <h1 class="sr-only">Uffda Academy</h1>
  <img class="hero-mark" src="{U}2023/01/UFFDA-Logo-White-lettering2.png" alt="Uffda Academy" width="1200" height="600">
</div></section>
<section class="hero-sub"><div class="wrap hero-under">
  <h2 class="hero-line">Learn something new. <span class="accent">Do something amazing.</span></h2>
  <p class="tagline">Technology, creativity, and practical skills made easier, one step at a time.</p>
</div></section>"""
CATS = [
 dict(id="everyday-tech", name="Everyday Technology", paths=["everyday"],
      blurb="File organization, email management, digital photos, basic computer skills, and everyday AI tools.",
      topics=["Organize your files and folders", "Tame your email inbox", "Manage your digital photos", "Computer basics with confidence", "Everyday AI tools"]),
 dict(id="creative-tech", name="Creative Technology", paths=["everyday", "business"],
      blurb="Canva, AI for crafters, printables, journaling projects, and digital creative tools.",
      topics=["Canva basics", "AI for crafters", "Make your own printables", "Digital journaling projects", "Creative tools roundup"]),
 dict(id="business-skills", name="Small Business Skills", paths=["business"],
      blurb="Social media, business organization, website basics, digital marketing, and practical automation.",
      topics=["Social media that fits your business", "Get your business organized", "Website basics", "Digital marketing made simple", "Practical automation"]),
 dict(id="ai-simple", name="AI Made Simple", paths=["everyday", "business"],
      blurb="ChatGPT basics, effective prompts, AI assistants, content creation, and using AI to save time.",
      topics=["ChatGPT basics", "Writing prompts that work", "AI assistants for everyday tasks", "Creating content with AI", "Save time with AI"]),
]
PATHLBL = {"everyday": "Everyday Learning", "business": "Small Business"}

def cat_tile(c):
    tags = "".join(f'<span class="tag">{PATHLBL[p]}</span>' for p in c["paths"])
    return f"""<a class="cat-tile" href="classes.html#{c['id']}"><div class="tags">{tags}</div><h3>{c['name']}</h3><p>{c['blurb']}</p><span class="more">Coming soon</span></a>"""

res_cards3 = "".join(card(BY[s_]) for s_ in CARD_ORDER[:3])
home = f"""{POSTER}
<section class="paths-sec"><div class="wrap stack-lg">
  <div class="stack" style="justify-items:center;text-align:center"><span class="eyebrow">Start here</span><h2>What brings you <span class="accent">here?</span></h2></div>
  <div class="paths">
    <a class="path" href="classes.html#everyday">
      <span class="path-k caps">Path 1</span>
      <h3 class="varsity">Everyday Learning</h3>
      <p>Build confidence with technology and creative tools.</p>
      <span class="btn btn-gold">Start learning</span>
    </a>
    <a class="path path-dark" href="classes.html#business">
      <span class="path-k caps">Path 2</span>
      <h3 class="varsity">Small Business</h3>
      <p>Make technology work for your business.</p>
      <span class="btn btn-gold">Grow my business</span>
    </a>
  </div>
</div></section>
<section><div class="wrap split" style="align-items:center">
  <div class="stack"><span class="eyebrow">Free quiz</span><h2>Which <span class="accent">social media</span> fits you?</h2></div>
  <div class="stack">
    <p>Not sure where to spend your time? Answer 10 quick questions and find the social media platform that fits your personality and your business, plus where to start.</p>
    <div class="actions"><a class="btn btn-gold" href="quiz-social-media-type.html">Take the quiz</a><a class="btn" href="resources.html">More free resources</a></div>
  </div>
</div></section>
<section class="band-gold"><div class="wrap split" style="align-items:center">
  <div class="stack"><span class="eyebrow" style="color:var(--ink)">Get help</span><h2>Rather have someone walk you <span class="accent">through it?</span></h2></div>
  <div class="stack">
    <p>Request personalized help or training for you or your team, one step at a time, at your pace.</p>
    <div class="actions"><a class="btn" href="get-help.html">Get help</a></div>
  </div>
</div></section>"""
page("index.html", "Uffda Academy",
     "Learn something new. Do something amazing. Technology, creativity, and practical skills made easier, one step at a time, for everyday learners and small business owners.",
     home, current="index.html")

# ---------- Squad ----------
squad = f"""<section class="hero-img"><div class="wrap">
  <h1 class="sr-only">The Impossible Task Squad</h1>
  <img src="{U}2023/07/FacebookCover-1-web.jpg" alt="Impossible Task Squad Challenges" width="1640" height="924">
  <div class="hero-under">
    <p class="bt-tag caps">A networking group sponsored by Uffda Academy</p>
    <p class="tagline">Tammey and Sue started the Squad in the summer of 2023 after their in-person workshops in Fargo–Moorhead showed how much people wanted a community to connect with and find support.</p>
    <div class="actions"><a class="btn btn-gold" href="{FB_SQUAD}">Join on Facebook</a><a class="btn" href="get-help.html">Ask a question</a></div>
  </div>
</div></section>
{MEETUP}
<section><div class="wrap split">
  <div class="stack"><span class="eyebrow">What happens at a meetup</span><h2>Challenges, support &amp; real progress</h2></div>
  <div class="stack measure">
    <p>Each month the Squad gets together to share challenges, tips and tools, and to connect with people who are looking for support and willing to offer it.</p>
    <ul style="margin:0;padding-left:1.2em;display:grid;gap:10px">
      <li><strong>Bring a task</strong> you've been putting off. Saying it out loud is half the battle.</li>
      <li><strong>Brainstorm</strong> with people who understand the difficulties of being a solopreneur.</li>
      <li><strong>Leave with a next step</strong> and someone who'll ask how it went.</li>
    </ul>
    <p class="muted">Meetups are the 2nd Friday of each month. Time and location are posted in the Squad's Facebook group, so follow along there to be the first to know.</p>
  </div>
</div></section>"""
page("squad.html", "The Impossible Task Squad",
     "The Impossible Task Squad meets the 2nd Friday of every month in Fargo–Moorhead to share challenges, support, and tips.",
     squad, current="squad.html")

# ---------- Resources ----------
quiz_card = f"""<a class="post-card" href="quiz-social-media-type.html">
  <div class="thumb"><div class="quiz-thumb"><span>QUIZ</span></div></div>
  <h3>Which Social Media Fits You?</h3><span class="by">Free quiz</span></a>"""
def rcard(p):
    return f"""<a class="post-card" href="{p['slug']}.html">
  <div class="thumb"><img src="{p['img']}" alt="" loading="lazy"></div>
  <h3>{html.escape(p['title'])}</h3>
  <span class="by">Free guide · By {p['author']}</span>
</a>"""
resources = f"""<header class="article-head band-ink on-ink inked" data-ink="edge" data-ink-seed="17"><div class="wrap"><div class="stack">
  <span class="eyebrow">Resources</span><h1>Templates, guides &amp; <span class="script gold">downloads</span></h1>
  <p style="color:#CFCFCF;max-width:60ch">Free guides you can use today, with templates and downloads on the way.</p>
</div></div></header>
<section><div class="wrap stack-lg">
  <div class="stack"><span class="eyebrow">Free</span><h2>Guides &amp; a quiz</h2></div>
  <div class="post-grid">{quiz_card}{''.join(rcard(BY[x]) for x in CARD_ORDER)}</div>
</div></section>
<section class="band-mist"><div class="wrap split" style="align-items:center">
  <div class="stack"><span class="eyebrow">Coming soon</span><h2>Templates &amp; <span class="accent">printables</span></h2></div>
  <div class="stack">
    <p>Ready-to-use templates and downloads, free and paid, are on the way. Have something you'd love to see? Let us know.</p>
    <div class="actions"><a class="btn" href="get-help.html">Suggest a resource</a></div>
  </div>
</div></section>"""
page("resources.html", "Resources", "Free guides, a quiz, and templates from Uffda Academy for everyday learners and small business owners.",
     resources, current="resources.html")

# ---------- Classes ----------
def cat_block(c):
    tags = "".join(f'<span class="tag">{PATHLBL[p]}</span>' for p in c["paths"])
    return f"""<section class="cat" id="{c['id']}" data-paths="{' '.join(c['paths'])}"><div class="cat-head"><div class="tags">{tags}</div><h2>{c['name']}</h2></div><div class="cat-body"><p>{c['blurb']}</p><span class="pill">Classes coming soon</span></div></section>"""
classes = f"""<header class="article-head band-ink on-ink inked" data-ink="edge" data-ink-seed="23"><div class="wrap"><div class="stack">
  <span class="eyebrow">Classes</span><h1>Short lessons, at your <span class="script gold">own pace</span></h1>
  <p style="color:#CFCFCF;max-width:60ch">Self-paced classes organized around what you want to accomplish. The first classes are in the works. Here's what's coming.</p>
</div></div></header>
<section style="padding-block:32px 8px"><div class="wrap">
  <div class="path-filter" role="group" aria-label="Show classes for">
    <a href="#all" data-filter="all" class="pf">Everything</a>
    <a href="#everyday" data-filter="everyday" class="pf">Everyday Learning</a>
    <a href="#business" data-filter="business" class="pf">Small Business</a>
  </div>
</div></section>
<div class="wrap cats">{''.join(cat_block(c) for c in CATS)}</div>
<section class="band-gold"><div class="wrap split" style="align-items:center">
  <div class="stack"><span class="eyebrow" style="color:var(--ink)">Your vote counts</span><h2>What should we teach <span class="accent">first?</span></h2></div>
  <div class="stack">
    <p>Tell us what you'd like to learn, and we'll let you know when the first classes are ready.</p>
    <div class="actions"><a class="btn" href="get-help.html">Tell us</a></div>
  </div>
</div></section>"""
page("classes.html", "Classes", "Short, self-paced classes in everyday technology, creative tools, small business skills, and AI made simple.",
     classes, current="classes.html")

# ---------- About ----------
about = f"""<header class="article-head band-ink on-ink inked" data-ink="edge" data-ink-seed="9"><div class="wrap"><div class="stack">
  <span class="eyebrow">About</span><h1>Where creativity &amp; technology <span class="script gold">intersect</span></h1>
</div></div></header>
<section><div class="wrap split">
  <div class="stack">
    <h2>It started over <span class="accent">coffee</span></h2>
    <img src="{U}2022/08/Tammey-Sue-Photo-770x1024.png" alt="Sue and Tammey take a quick selfie during their weekly board meeting at Red River Coffee in Fargo, ND" style="max-width:320px;border:3px solid var(--ink)">
    <p class="photo-note">Sue and Tammey at Red River Coffee during one of their weekly board meetings.</p>
  </div>
  <div class="stack measure">
    <p><strong>It started over coffee in 2017.</strong> Tammey and Sue began scheduling weekly "board meetings," time blocked on their calendars to meet, connect, share what was going on in their lives, and brainstorm. They called them board meetings because seeing them on the calendar reminded them of the importance of their time together.</p>
    <p>Along the way, they started helping each other with the tasks that felt impossible. One week Sue had a client task that felt overwhelming, so Tammey simply did it for her. A few months later Tammey had one of her own, and Sue took it on. Done and done!</p>
    <p>Then one day the conversation turned to what they could bring to their community. <strong>In the summer of 2022, Uffda Academy was born.</strong></p>
  </div>
</div></section>
<section class="band-mist"><div class="wrap stack-lg">
  <div class="person">
    <img src="{U}2022/12/UA22-30-scaled.jpg" alt="Tammey">
    <div class="stack measure">
      <h2>Meet Tammey</h2>
      <p>I'm a problem solver, technology enthusiast, and teacher at heart with over 30 years of experience in business systems, organization, training, and finding better ways to get things done.</p>
      <p>I love turning complicated processes into practical solutions, whether that means building websites, improving workflows, exploring new technology, or helping someone master a new skill.</p>
      <p>That passion inspired me to co-create Uffda Academy.</p>
      <p>I believe technology should make life easier, not more complicated. My favorite moments are when someone goes from "I have no idea how to do this" to "Look what I just did!"</p>
      <p>A little patience, a little humor, and a willingness to try can take us a long way!</p>
      <p>More about me at <a href="https://tammeybrown.com">tammeybrown.com</a></p>
      <div class="actions"><a class="btn btn-gold" href="https://calendar.app.google/PtwzU3Zmm2dFBqB67">Book a 15-minute call</a></div>
    </div>
  </div>
  <div class="person">
    <img src="{U}2022/12/UA22-21-scaled.jpg" alt="Sue">
    <div class="stack measure">
      <h2>Sue Skavlem (Burke)</h2>
      <p>Sue's mission at <a href="https://www.designsthatdo.com">DesignsThatDo.com</a>: to create designs that aren't just pretty, but designs that do. Designs that amplify your message, empower your growth, and generate opportunities. She finds joy in co-creating.</p>
      <dl class="facts">
        <dt>Designer since</dt><dd>1999</dd>
        <dt>Specializes in</dt><dd><a href="https://www.designsthatdo.com/branding-focused-consultations">Branding</a>, <a href="https://www.designsthatdo.com/writing">writing</a> &amp; <a href="https://www.designsthatdo.com/design">design</a></dd>
        <dt>Loves</dt><dd>Books</dd>
        <dt>Brakes for</dt><dd>Mountain scenic views</dd>
      </dl>
      <div class="actions"><a class="btn" href="https://www.designsthatdo.com/contact">Contact Sue</a></div>
    </div>
  </div>
</div></section>"""
about += f"""<section><div class="wrap split">
  <div class="stack"><span class="eyebrow">Our mission</span><h2>Learn something new. <span class="accent">Do something amazing.</span></h2></div>
  <div class="stack measure">
    <p>Uffda Academy is a practical, friendly place for everyday people, creatives, and small business owners to learn useful skills. Technology, creativity, and practical skills, made easier one step at a time.</p>
    <p>We also sponsor the <a href="squad.html">Impossible Task Squad</a>, a local networking group that meets the 2nd Friday of every month.</p>
    <div class="actions"><a class="btn btn-gold" href="classes.html">Browse classes</a><a class="btn" href="get-help.html">Get help</a></div>
  </div>
</div></section>"""
page("about.html", "About", "Meet Tammey and Sue, the friends behind Uffda Academy and the Impossible Task Squad.", about, current="about.html")

# ---------- Get Help ----------
gethelp = f"""<header class="article-head band-ink on-ink inked" data-ink="edge" data-ink-seed="13"><div class="wrap"><div class="stack">
  <span class="eyebrow">Get help</span><h1>Help that fits <span class="script gold">you</span></h1>
  <p style="color:#CFCFCF;max-width:58ch">Personalized help or training for you, your business, or your team, step by step and at your pace.</p>
</div></div></header>
<section><div class="wrap stack-lg">
  <div class="help-grid">
    <div class="help-card"><h3>One-on-one help</h3><p>Stuck on a tool, a project, or your tech? Work through it together, with your own files and your own questions.</p></div>
    <div class="help-card"><h3>Training for your team</h3><p>Hands-on sessions for your staff on social media, Canva, AI tools, or getting organized.</p></div>
    <div class="help-card"><h3>Not sure yet?</h3><p>Tell us what you're trying to do and we'll point you to the right class, resource, or next step.</p></div>
  </div>
</div></section>
<section class="band-mist"><div class="wrap stack-lg">
  <div class="stack"><span class="eyebrow">Request help</span><h2>Who would you like to <span class="accent">work with?</span></h2></div>
  <div class="helpers">
    <div class="helper">
      <img src="{U}2022/12/UA22-30-scaled.jpg" alt="Tammey" loading="lazy">
      <div class="stack">
        <h3>Tammey</h3>
        <p><strong>Technology, social media, and getting organized.</strong> Struggling with tech, or feel like you're spinning your wheels? Let's brainstorm a plan and move into action.</p>
        <div class="actions"><a class="btn btn-gold" href="https://calendar.app.google/PtwzU3Zmm2dFBqB67">Book a 15-minute call</a></div>
      </div>
    </div>
    <div class="helper">
      <img src="{U}2022/12/UA22-21-scaled.jpg" alt="Sue" loading="lazy">
      <div class="stack">
        <h3>Sue</h3>
        <p><strong>Branding, writing, and design.</strong> Designs that aren't just pretty, but designs that do, from logos to your brand's message.</p>
        <div class="actions"><a class="btn btn-gold" href="https://www.designsthatdo.com/contact">Contact Sue</a></div>
      </div>
    </div>
  </div>
  <div class="stack">
    <h3>Not sure who to ask? Email us</h3>
    <div class="copy-row"><code>{EMAIL}</code><button type="button" class="btn" data-copy="{EMAIL}">Copy</button></div>
    <p><a href="mailto:{EMAIL}">Open in your email app</a></p>
  </div>
</div></section>"""
page("get-help.html", "Get Help", "Request personalized help or training from Uffda Academy.", gethelp, current="get-help.html")

# ---------- Privacy ----------
privacy = f"""<header class="article-head band-ink on-ink"><div class="wrap"><div class="stack"><span class="eyebrow">Legal</span><h1>Privacy Policy</h1></div></div></header>
<section><div class="wrap"><div class="prose" style="margin-top:0">
    <p>Uffda Academy respects your privacy. This page explains what information we collect through uffdaacademy.com and how we use it.</p>
    <h2>Information we collect</h2>
    <p>This website doesn't require an account and doesn't collect personal information unless you choose to send it to us, for example by emailing us or signing up for updates.</p>
    <p>The Social Media Type Quiz runs entirely in your browser. Your answers and score are not sent to us or stored.</p>
    <h2>How we use your information</h2>
    <p>If you email us or sign up for updates, we use your information only to respond to you and to send the updates you asked for. We don't sell or rent your information.</p>
    <h2>Third-party services</h2>
    <p>Our website is hosted by a third-party provider that may keep standard technical logs (such as IP addresses and browser type) for security and performance. Links to other websites, such as Facebook, LinkedIn, Instagram, and Google Calendar, are governed by those sites' own privacy policies.</p>
    <h2>Contact</h2>
    <p>Questions about this policy? Email {EMAIL}.</p>
</div></div></section>"""
page("privacy-policy.html", "Privacy Policy", "How Uffda Academy handles your information.", privacy)

# ---------- 404 ----------
nf = """<section class="poster inked" data-ink="poster" data-ink-seed="3"><div class="wrap stack" style="justify-items:center">
  <span class="script" style="font-size:3rem">Uffda!</span><h1>Page not found</h1>
  <p>It may have moved when we refreshed the site.</p>
  <div class="actions"><a class="btn btn-gold" href="index.html">Go home</a><a class="btn" href="resources.html">Browse resources</a></div>
</div></section>"""
page("404.html", "Page not found", "Page not found.", nf)

print("built", len(os.listdir(OUT)), "files")
