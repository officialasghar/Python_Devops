from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(title="ZGEN Solutions")


CSS = """
:root{--ink:#07111f;--navy:#081526;--blue:#5b7cff;--cyan:#74e7ff;--lime:#b5ff6d;--paper:#f3f6fb;--muted:#6e7890;--line:#dce3ef}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,"Segoe UI",sans-serif;color:var(--ink);background:#fff;line-height:1.65}
a{text-decoration:none;color:inherit}.container{width:min(1180px,calc(100% - 40px));margin:auto}img{max-width:100%}
header{position:absolute;z-index:20;width:100%;color:#fff}.nav{height:82px;display:flex;align-items:center;justify-content:space-between}.logo{font-size:21px;font-weight:900;letter-spacing:-1px}.logo b{color:var(--cyan)}
.nav-links{display:flex;align-items:center;gap:32px;font-size:14px;font-weight:700}.nav-links a{color:#c6d0df;transition:.2s}.nav-links a:hover,.nav-links a.active{color:#fff}.nav-button{border:1px solid rgba(255,255,255,.18)!important;padding:9px 17px;border-radius:999px;color:#fff!important;background:rgba(255,255,255,.06)}
.menu{display:none;border:0;background:none;color:white;font-size:28px}
.hero{min-height:720px;color:#fff;background:radial-gradient(circle at 80% 20%,rgba(91,124,255,.24),transparent 28%),linear-gradient(135deg,#07111f 0%,#0c1d35 65%,#102a50 100%);overflow:hidden;position:relative}
.hero:before{content:"";position:absolute;width:680px;height:680px;border:1px solid rgba(116,231,255,.08);border-radius:50%;right:-180px;top:-240px;box-shadow:0 0 0 110px rgba(116,231,255,.018),0 0 0 220px rgba(116,231,255,.012)}
.hero-inner{min-height:720px;padding-top:82px;display:grid;grid-template-columns:1.1fr .9fr;align-items:center;gap:70px;position:relative}.hero h1{font-size:clamp(52px,7vw,86px);line-height:.94;letter-spacing:-5px;margin:18px 0 26px}.gradient-text{background:linear-gradient(100deg,#74e7ff,#a8b5ff 70%,#b5ff6d);background-clip:text;-webkit-background-clip:text;color:transparent}
.eyebrow{font-size:12px;text-transform:uppercase;letter-spacing:2.5px;font-weight:900;color:var(--cyan)}.hero-copy{max-width:590px;color:#b8c5d8;font-size:19px}.buttons{display:flex;gap:12px;margin-top:32px;flex-wrap:wrap}
.button{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:14px 22px;border-radius:9px;font-weight:800;font-size:14px;border:1px solid transparent;transition:.25s}.button-primary{background:var(--lime);color:#081526}.button-primary:hover{transform:translateY(-3px);box-shadow:0 16px 35px rgba(181,255,109,.18)}.button-dark{border-color:rgba(255,255,255,.17);color:white}.button-blue{background:var(--blue);color:white}
.tech-stage{height:440px;border:1px solid rgba(255,255,255,.1);border-radius:24px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(91,124,255,.035));position:relative;box-shadow:0 40px 90px rgba(0,0,0,.32);overflow:hidden;animation:float 6s ease-in-out infinite}
.tech-stage:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(116,231,255,.065) 1px,transparent 1px),linear-gradient(90deg,rgba(116,231,255,.065) 1px,transparent 1px);background-size:34px 34px}.core{position:absolute;width:144px;height:144px;left:calc(50% - 72px);top:calc(50% - 72px);border:1px solid rgba(116,231,255,.5);border-radius:50%;display:grid;place-items:center;font-weight:900;font-size:24px;box-shadow:0 0 70px rgba(91,124,255,.25);z-index:2}.core:after{content:"";position:absolute;width:190px;height:190px;border:1px dashed rgba(116,231,255,.18);border-radius:50%;animation:spin 18s linear infinite}
.status{position:absolute;z-index:3;border-radius:12px;padding:14px 18px;background:rgba(5,16,31,.92);border:1px solid rgba(255,255,255,.11);box-shadow:0 15px 35px rgba(0,0,0,.2)}.status strong{font-size:24px;display:block}.status small{color:#99aac3}.status-a{left:25px;top:42px}.status-b{right:22px;bottom:38px}
@keyframes float{50%{transform:translateY(-10px)}}@keyframes spin{to{transform:rotate(360deg)}}
section{padding:100px 0}.section-heading{max-width:690px;margin-bottom:48px}.section-heading h2,.split h2,.page-title h1,.cta h2{font-size:clamp(38px,5vw,58px);line-height:1.05;letter-spacing:-3px;margin:12px 0 18px}.section-heading p{font-size:18px;color:var(--muted)}.dark-eyebrow{color:#5175ff}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.card{position:relative;overflow:hidden;padding:34px;border-radius:16px;border:1px solid var(--line);background:#fff;transition:.25s}.card:hover{transform:translateY(-7px);box-shadow:0 24px 60px rgba(7,17,31,.09);border-color:#bbcafa}.card-number{font-size:12px;font-weight:900;color:var(--blue)}.card h3{font-size:22px;margin:48px 0 10px}.card p{color:var(--muted);margin-bottom:0}
.services-section{background:var(--paper)}.stats{display:grid;grid-template-columns:repeat(3,1fr);margin-top:60px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.stat{padding:28px;text-align:center;border-right:1px solid var(--line)}.stat:last-child{border-right:0}.stat strong{font-size:42px}.stat span{display:block;color:var(--muted)}
.split{display:grid;grid-template-columns:1fr 1fr;gap:75px;align-items:center}.visual-panel{min-height:440px;border-radius:22px;background:linear-gradient(145deg,#07111f,#225ae3);position:relative;overflow:hidden;color:white;padding:40px;display:flex;align-items:flex-end}.visual-panel:before{content:"";position:absolute;width:260px;height:260px;border:65px solid rgba(116,231,255,.08);border-radius:50%;right:-90px;top:-100px}.visual-panel strong{font-size:54px;line-height:1;position:relative}.visual-panel p{position:relative;max-width:330px;color:#c7d4e7}.split-copy p{color:var(--muted);font-size:17px}
.check-list{display:grid;gap:14px;margin-top:28px}.check{border-bottom:1px solid var(--line);padding-bottom:14px;font-weight:800}.check b{color:var(--blue);margin-right:12px}
.page-hero{padding:170px 0 90px;background:radial-gradient(circle at 85% 10%,rgba(91,124,255,.25),transparent 28%),var(--navy);color:white}.page-title{max-width:760px}.page-title h1{font-size:clamp(54px,8vw,88px)}.page-title p{font-size:19px;color:#bbc8da;max-width:650px}.white-section{background:white}
.process{counter-reset:step}.process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.process-card{border-top:2px solid var(--blue);padding-top:22px}.process-card span{color:var(--blue);font-weight:900}.process-card h3{margin-top:25px}.process-card p{color:var(--muted)}
.feature-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}.feature{padding:38px;border-radius:18px;background:var(--paper)}.feature h3{font-size:26px;margin:18px 0 8px}.feature p{color:var(--muted)}.feature-mark{width:48px;height:48px;border-radius:12px;background:#dde5ff;color:var(--blue);display:grid;place-items:center;font-weight:900}
.values-grid{grid-template-columns:repeat(3,1fr)}
.cta-wrap{padding:0 20px 20px}.cta{padding:72px 40px;text-align:center;border-radius:20px;background:linear-gradient(120deg,#07111f,#102c55);color:white}.cta p{max-width:590px;margin:0 auto 28px;color:#b7c5d8}
footer{padding:35px 0;border-top:1px solid var(--line);color:var(--muted)}footer .container{display:flex;justify-content:space-between;gap:20px}footer .logo{color:var(--ink)}footer .logo b{color:var(--blue)}
.contact-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:70px}.contact-panel{padding:38px;background:var(--navy);color:white;border-radius:18px}.contact-panel h3{font-size:28px}.contact-detail{border-top:1px solid rgba(255,255,255,.12);padding:18px 0;color:#c0cddd}.contact-detail small{display:block;color:#8291a8;text-transform:uppercase;letter-spacing:1px;font-size:11px}
.form{display:grid;grid-template-columns:1fr 1fr;gap:18px}.field{display:grid;gap:7px}.field.full{grid-column:1/-1}.field label{font-weight:800;font-size:13px}.field input,.field textarea,.field select{width:100%;border:1px solid var(--line);border-radius:9px;padding:14px;font:inherit;background:white}.field textarea{min-height:150px;resize:vertical}
@media(max-width:900px){.hero-inner{grid-template-columns:1fr;padding:130px 0 80px;min-height:auto}.hero{min-height:auto}.tech-stage{max-width:620px;width:100%}.cards,.values-grid{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:45px}.process-grid{grid-template-columns:1fr 1fr}.stats{grid-template-columns:1fr}.stat{border-right:0;border-bottom:1px solid var(--line)}.contact-grid{grid-template-columns:1fr}.nav-links{gap:18px}}
@media(max-width:680px){.container{width:calc(100% - 28px)}.nav{height:70px}.menu{display:block}.nav-links{display:none;position:absolute;left:14px;right:14px;top:70px;padding:20px;background:#101f34;border-radius:12px;flex-direction:column;align-items:stretch}.nav-links.open{display:flex}.nav-button{text-align:center}.hero-inner{padding-top:110px}.hero h1{font-size:52px;letter-spacing:-3px}.tech-stage{height:330px}.cards,.feature-grid,.values-grid,.process-grid{grid-template-columns:1fr}.stats{margin-top:40px}.visual-panel{min-height:350px}.page-hero{padding:145px 0 70px}.page-title h1{font-size:54px;letter-spacing:-3px}section{padding:70px 0}.form{grid-template-columns:1fr}.field.full{grid-column:auto}footer .container{flex-direction:column}}
"""


def shell(active: str, title: str, content: str, dark_header: bool = False) -> str:
    links = "".join(
        f'<a class="{"active" if active == name else ""}" href="/{path}"'
        f'>{name.capitalize()}</a>'
        for name, path in [("home", ""), ("services", "services"), ("about", "about"), ("contact", "contact")]
    )
    header_class = "" if dark_header else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="ZGEN Solutions engineers software, cloud platforms, and DevOps systems.">
<title>{title} | ZGEN Solutions</title><style>{CSS}</style></head>
<body><header class="{header_class}"><div class="container nav">
<a class="logo" href="/">ZGEN<b>Solutions</b></a><button class="menu" aria-label="Toggle navigation" aria-expanded="false">☰</button>
<nav class="nav-links">{links}<a class="nav-button" href="/contact">Start a project</a></nav></div></header>{content}
<footer><div class="container"><a class="logo" href="/">ZGEN<b>Solutions</b></a><div>© 2026 ZGEN Solutions. Built for what comes next.</div></div></footer>
<script>const m=document.querySelector('.menu'),n=document.querySelector('.nav-links');m.onclick=()=>{{const o=n.classList.toggle('open');m.setAttribute('aria-expanded',o)}};</script>
</body></html>"""


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    content = """
<main><div class="hero"><div class="container hero-inner"><div>
<div class="eyebrow">Strategy. Engineering. Velocity.</div><h1>Turn bold ideas into <span class="gradient-text">digital momentum.</span></h1>
<p class="hero-copy">ZGEN Solutions designs secure software, scalable cloud platforms, and automated delivery systems for ambitious teams.</p>
<div class="buttons"><a class="button button-primary" href="/contact">Start a project →</a><a class="button button-dark" href="/services">Explore our work</a></div></div>
<div class="tech-stage" aria-label="ZGEN technology platform"><div class="status status-a"><strong>99.9%</strong><small>Reliable uptime</small></div><div class="core">ZGEN</div><div class="status status-b"><strong>3.0×</strong><small>Faster delivery</small></div></div></div></div>
<section class="services-section" id="services"><div class="container"><div class="section-heading"><div class="eyebrow dark-eyebrow">Capabilities</div><h2>One team. Every layer of the stack.</h2><p>We bridge product thinking and technical execution, creating systems that work beautifully today and scale tomorrow.</p></div>
<div class="cards"><article class="card"><div class="card-number">01 / BUILD</div><h3>Software Engineering</h3><p>Fast, accessible web applications and resilient APIs shaped around real user and business needs.</p></article><article class="card"><div class="card-number">02 / SCALE</div><h3>Cloud & DevOps</h3><p>Cloud architecture, Kubernetes, CI/CD, security, monitoring, and automation that remove delivery friction.</p></article><article class="card"><div class="card-number">03 / TRANSFORM</div><h3>Technology Consulting</h3><p>Clear architecture reviews, technical strategy, and practical roadmaps that align technology with growth.</p></article></div>
<div class="stats"><div class="stat"><strong>End-to-end</strong><span>Product and platform delivery</span></div><div class="stat"><strong>Cloud-first</strong><span>Modern, resilient foundations</span></div><div class="stat"><strong>Built to evolve</strong><span>Quality that compounds</span></div></div></div></section>
<section><div class="container split"><div class="visual-panel"><div><strong>Clarity over complexity.</strong><p>Senior engineering focus, transparent communication, and no black-box handovers.</p></div></div><div class="split-copy"><div class="eyebrow dark-eyebrow">How we work</div><h2>A sharper path from challenge to launch.</h2><p>We join your team with curiosity, technical depth, and a bias toward measurable outcomes.</p><div class="check-list"><div class="check"><b>01</b>Discover the real problem</div><div class="check"><b>02</b>Design for change and scale</div><div class="check"><b>03</b>Ship, measure, and improve</div></div></div></div></section>
<div class="cta-wrap"><section class="cta"><div class="eyebrow">Your next move</div><h2>Build something that matters.</h2><p>Bring us the problem, the product, or the ambition. We’ll build a practical route forward.</p><a class="button button-primary" href="/contact">Talk to ZGEN →</a></section></div></main>"""
    return HTMLResponse(shell("home", "Home", content))


@app.get("/services", response_class=HTMLResponse)
def services(request: Request) -> HTMLResponse:
    content = """<main><section class="page-hero"><div class="container page-title"><div class="eyebrow">Services</div><h1>Technology with <span class="gradient-text">purpose.</span></h1><p>From architecture to operations, we provide the specialist skills and senior perspective to move complex work forward.</p></div></section>
<section><div class="container"><div class="feature-grid">
<article class="feature"><div class="feature-mark">01</div><h3>Product Engineering</h3><p>Discovery, UX collaboration, modern Python and JavaScript development, APIs, integrations, and quality engineering.</p></article>
<article class="feature"><div class="feature-mark">02</div><h3>Cloud Architecture</h3><p>Cloud-native platforms designed around availability, cost control, security, and future growth.</p></article>
<article class="feature"><div class="feature-mark">03</div><h3>DevOps Automation</h3><p>Infrastructure as code, container platforms, CI/CD pipelines, monitoring, incident readiness, and release automation.</p></article>
<article class="feature"><div class="feature-mark">04</div><h3>Technical Advisory</h3><p>Independent assessments, architecture workshops, modernization plans, and delivery guidance for leadership teams.</p></article>
</div></div></section>
<section class="services-section"><div class="container"><div class="section-heading"><div class="eyebrow dark-eyebrow">Our process</div><h2>Focused work, visible progress.</h2></div><div class="process-grid"><article class="process-card"><span>01</span><h3>Understand</h3><p>We align on users, constraints, risk, and business outcomes.</p></article><article class="process-card"><span>02</span><h3>Shape</h3><p>We turn complexity into an actionable architecture and roadmap.</p></article><article class="process-card"><span>03</span><h3>Build</h3><p>We deliver in small increments with clear demos and feedback.</p></article><article class="process-card"><span>04</span><h3>Improve</h3><p>We measure, automate, document, and keep raising the baseline.</p></article></div></div></section>
<div class="cta-wrap"><section class="cta"><h2>Need the right team for the next phase?</h2><p>Let’s match the right expertise to your most important technical challenge.</p><a class="button button-primary" href="/contact">Plan a project</a></section></div></main>"""
    return HTMLResponse(shell("services", "Services", content))


@app.get("/about", response_class=HTMLResponse)
def about(request: Request) -> HTMLResponse:
    content = """<main><section class="page-hero"><div class="container page-title"><div class="eyebrow">About ZGEN</div><h1>Small enough to care. <span class="gradient-text">Built to deliver.</span></h1><p>We combine senior technical thinking with hands-on execution to help organizations make better technology decisions.</p></div></section>
<section><div class="container split"><div class="visual-panel"><div><strong>People, process, technology.</strong><p>Three disciplines aligned around one outcome: lasting value for your business.</p></div></div><div class="split-copy"><div class="eyebrow dark-eyebrow">Our belief</div><h2>Good technology should create momentum.</h2><p>That means understandable systems, dependable delivery, and partners who communicate clearly. We avoid unnecessary layers and focus engineering energy where it creates the greatest impact.</p><p>Whether we are designing from scratch, rescuing a release process, or modernizing legacy infrastructure, our approach stays practical and outcome-led.</p></div></div></section>
<section class="services-section"><div class="container"><div class="section-heading"><div class="eyebrow dark-eyebrow">What guides us</div><h2>Principles in every engagement.</h2></div><div class="cards values-grid"><article class="card"><div class="card-number">VALUE 01</div><h3>Earn trust</h3><p>Be direct, transparent, and accountable from the first conversation onward.</p></article><article class="card"><div class="card-number">VALUE 02</div><h3>Choose clearly</h3><p>Explain trade-offs simply and make decisions with evidence, not theatre.</p></article><article class="card"><div class="card-number">VALUE 03</div><h3>Build quality in</h3><p>Security, reliability, testing, and maintainability are part of the design.</p></article></div></div></section>
<div class="cta-wrap"><section class="cta"><h2>Technology partnership without the noise.</h2><p>Meet an engineering team that stays close to the problem and invested in the outcome.</p><a class="button button-primary" href="/contact">Connect with us</a></section></div></main>"""
    return HTMLResponse(shell("about", "About", content))


@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request) -> HTMLResponse:
    content = """<main><section class="page-hero"><div class="container page-title"><div class="eyebrow">Contact</div><h1>Let’s build what’s <span class="gradient-text">next.</span></h1><p>Share a challenge, idea, or project. We’ll help you turn it into a clear and achievable engineering plan.</p></div></section>
<section><div class="container contact-grid"><aside class="contact-panel"><h3>Start a conversation</h3><p>Tell us where you want to go and how we can help.</p><div class="contact-detail"><small>Email</small>hello@zgensolutions.com</div><div class="contact-detail"><small>Typical response</small>Within one business day</div><div class="contact-detail"><small>Working with</small>Startups, scale-ups, and enterprise teams</div></aside>
<form class="form" action="mailto:hello@zgensolutions.com" method="get"><div class="field"><label for="name">Your name</label><input id="name" name="name" required placeholder="Alex Morgan"></div><div class="field"><label for="email">Work email</label><input id="email" name="email" type="email" required placeholder="alex@company.com"></div><div class="field full"><label for="company">Company</label><input id="company" name="company" placeholder="Company name"></div><div class="field full"><label for="service">How can we help?</label><select id="service" name="service"><option>Software Engineering</option><option>Cloud & DevOps</option><option>Technology Consulting</option><option>Something else</option></select></div><div class="field full"><label for="message">Project details</label><textarea id="message" name="body" required placeholder="A little about your goals, timeline, and technical challenge..."></textarea></div><div class="field full"><button class="button button-blue" type="submit">Send project enquiry →</button></div></form></div></section></main>"""
    return HTMLResponse(shell("contact", "Contact", content))


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}
