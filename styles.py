"""Global CSS for the portfolio: navy / blue / teal / violet / amber palette.
Every Streamlit widget gets explicit colours so text never blends into its box,
whatever light or dark theme the visitor's device uses."""

CSS = """
<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
:root{color-scheme:light;--navy:#0B1F3A;--ink:#0F172A;--text:#1E293B;--muted:#475569;--line:#CBD5E1;--paper:#E8EEF6;--card:#fff;
  --blue:#2563EB;--teal:#0D9488;--violet:#7C3AED;--amber:#D97706;--emerald:#059669;--rose:#E11D48;
  --g-blue:linear-gradient(135deg,#2563EB,#1D4ED8);--g-violet:linear-gradient(135deg,#7C3AED,#2563EB);
  --g-teal:linear-gradient(135deg,#0D9488,#2563EB);--g-green:linear-gradient(135deg,#059669,#0D9488);
  --g-amber:linear-gradient(135deg,#F59E0B,#E11D48);--shadow:0 8px 24px rgba(11,31,58,.12);--shadow-lg:0 18px 40px rgba(37,99,235,.22);}
html{scroll-behavior:smooth;}
html,body,[class*="css"],.stApp{font-family:'Plus Jakarta Sans',sans-serif;color:var(--text);}
.stApp{background:radial-gradient(1000px 460px at 5% -8%,#C7D8FA 0,transparent 60%),radial-gradient(800px 400px at 100% 0,#BDF0EA 0,transparent 55%),var(--paper);}
#MainMenu,footer,header[data-testid="stHeader"],[data-testid="stSidebar"],[data-testid="collapsedControl"]{display:none !important;}
.block-container{max-width:1100px;padding:0 1.25rem 3rem;}
:where([data-testid="stMarkdownContainer"]) :is(p,li,span,b){color:var(--text);}
.h1,.h2,.h3,h1,h2,h3{font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;color:var(--ink);letter-spacing:-.02em;}
.h1,.h2,.h3{display:block;}
.anchor{scroll-margin-top:80px;height:0;margin-top:3.4rem;}
#top.anchor{scroll-margin-top:400px;margin-top:0;}

/* navigation pill */
[data-testid="stElementContainer"]:has(.nav){position:sticky;top:0;z-index:50;text-align:center;}
.nav{display:inline-flex;gap:.2rem;flex-wrap:wrap;justify-content:center;margin:.7rem auto 1.6rem;padding:.35rem;background:#fff;
  border:1.5px solid var(--line);border-radius:999px;box-shadow:var(--shadow);}
.nav a{color:var(--navy);text-decoration:none;font-weight:700;font-size:.88rem;padding:.45rem .95rem;border-radius:999px;transition:.2s;}
.nav a:hover{color:#fff;background:var(--navy);transform:translateY(-1px);}
.to-top{position:fixed;right:1.2rem;bottom:1.2rem;z-index:60;width:46px;height:46px;border-radius:50%;background:var(--g-blue);
  color:#fff !important;display:flex;align-items:center;justify-content:center;text-decoration:none;box-shadow:var(--shadow-lg);transition:.25s;}
.to-top:hover{transform:translateY(-4px) scale(1.06);}

/* hero */
@keyframes rise{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:none;}}
[data-testid="stHorizontalBlock"]:has(.hero){background:radial-gradient(600px 300px at 92% 0,rgba(13,148,136,.55),transparent 70%),
  linear-gradient(135deg,#0B1F3A 0%,#12306A 60%,#1E40AF 100%);border-radius:28px;padding:2.6rem 2.4rem;box-shadow:var(--shadow-lg);}
.hero{animation:rise .7s ease both;}
.hero .role{display:inline-block;color:#99F6E4 !important;background:rgba(153,246,228,.14);border:1px solid rgba(153,246,228,.4);
  font-weight:700;font-size:.85rem;padding:.3rem .85rem;border-radius:999px;margin:0 0 .8rem;}
.hero .h1{font-size:clamp(2.2rem,4.6vw,3.5rem);line-height:1.1;margin:.1rem 0 .9rem;color:#fff;}
.hero .lead{color:#DBEAFE !important;font-size:1.05rem;line-height:1.75;max-width:34rem;}
.icons a{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:12px;
  border:1.5px solid rgba(255,255,255,.35);background:rgba(255,255,255,.1);color:#fff;margin-right:.55rem;font-size:1.1rem;transition:.25s;}
.icons a:hover{background:#fff;color:var(--blue);transform:translateY(-4px);}
.photo{width:100%;max-width:320px;aspect-ratio:1/1;margin:0 auto;border-radius:30px;overflow:hidden;padding:5px;
  background:linear-gradient(135deg,#2DD4BF,#60A5FA,#A78BFA);box-shadow:0 20px 50px rgba(0,0,0,.45);transition:.4s;}
.photo img{width:100%;height:100%;object-fit:cover;display:block;border-radius:26px;transition:transform .5s;}
.photo:hover{transform:rotate(-2.5deg) translateY(-6px) scale(1.02);}
.photo:hover img{transform:scale(1.07);}
.photo.empty{display:flex;align-items:center;justify-content:center;color:#fff;font-size:4rem;}

/* stats */
.stat{--c:var(--blue);background:var(--card);border:1.5px solid var(--line);border-top:5px solid var(--c);border-radius:16px;
  padding:1rem 1.2rem;transition:.25s;box-shadow:var(--shadow);}
[data-testid="stColumn"]:nth-child(2) .stat{--c:var(--teal);}
[data-testid="stColumn"]:nth-child(3) .stat{--c:var(--violet);}
[data-testid="stColumn"]:nth-child(4) .stat{--c:var(--amber);}
.stat:hover{transform:translateY(-5px);}
.stat b{display:block;font-size:2.1rem;font-weight:800;color:var(--c);line-height:1.1;}
.stat span{color:var(--muted);font-size:.9rem;font-weight:600;}

/* section titles: one accent colour per section */
.sec{--a:var(--blue);font-size:2.1rem;margin:.4rem 0 1.4rem;color:var(--ink);}
.sec:after{content:"";display:block;width:70px;height:6px;border-radius:9px;background:var(--a);margin-top:.6rem;}
#skills+.sec{--a:var(--teal);}
#projects+.sec{--a:var(--violet);}
#experience+.sec{--a:var(--amber);}
#education+.sec{--a:var(--emerald);}
#contact+.sec{--a:var(--rose);}
.sec small{display:block;font-size:.95rem;font-weight:500;letter-spacing:0;color:var(--muted);margin-top:.25rem;}

/* cards */
.card{--grad:var(--g-blue);position:relative;overflow:hidden;background:var(--card);border:1.5px solid var(--line);border-radius:18px;
  padding:1.5rem 1.55rem;height:100%;transition:.3s;box-shadow:var(--shadow);}
.card:before{content:"";position:absolute;inset:0 0 auto 0;height:6px;background:var(--grad);}
.card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:#93C5FD;}
.card:has(.thumb){--grad:var(--g-violet);min-height:560px;}
.tl-item .card{--grad:var(--g-amber);}
.card:has(.cert-ico){--grad:var(--g-blue);}
.card:has(.edu-ico){--grad:var(--g-green);}
.card:has(.info){--grad:var(--g-teal);}
.card .h3{font-size:1.35rem;margin:.2rem 0 .3rem;line-height:1.25;}
.card ul{margin:.7rem 0 0;padding-left:1.1rem;line-height:1.7;font-size:.95rem;}
.card li::marker{color:var(--blue);}
.meta{color:var(--muted) !important;font-size:.9rem;margin:0;font-weight:600;}
.lbl{font-size:.74rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--blue) !important;margin:1.1rem 0 .15rem;}
.chip{display:inline-block;padding:.28rem .8rem;margin:.22rem .3rem .22rem 0;border-radius:999px;font-size:.8rem;font-weight:700;
  background:#DBEAFE;color:#1E3A8A !important;border:1px solid #93C5FD;transition:.2s;}
.chip.tool{background:#CCFBF1;color:#115E59 !important;border-color:#5EEAD4;}
.chip:hover{transform:translateY(-2px);box-shadow:0 4px 10px rgba(11,31,58,.15);}
.badge{display:inline-block;padding:.3rem .8rem;border-radius:10px;font-size:.78rem;font-weight:700;background:#FEF3C7;color:#92400E !important;border:1px solid #FCD34D;}

/* about */
.step{display:flex;gap:.8rem;align-items:center;padding:.55rem .7rem;border-radius:12px;transition:.2s;color:var(--text);font-weight:600;}
.step:hover{background:#DBEAFE;transform:translateX(5px);}
.step i{flex:none;width:30px;height:30px;border-radius:50%;background:var(--navy);color:#fff;font-style:normal;font-size:.8rem;
  font-weight:700;display:flex;align-items:center;justify-content:center;}
.do{padding:.75rem 0;border-bottom:1.5px solid var(--line);}
.do b{color:var(--ink) !important;}
.do span{color:var(--muted) !important;}

/* skills */
.group{font-weight:800;color:var(--ink);margin:1.5rem 0 .7rem;display:flex;align-items:center;gap:.6rem;}
.group:before{content:"";width:6px;height:20px;border-radius:4px;background:var(--teal);}
.group:after{content:"";flex:1;height:1.5px;background:var(--line);}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:.85rem;}
.tile{--c:var(--blue);display:flex;align-items:center;gap:.8rem;padding:.75rem .95rem;background:var(--card);border:1.5px solid var(--line);
  border-left:6px solid var(--c);border-radius:14px;font-weight:700;font-size:.92rem;color:var(--ink);transition:.25s;box-shadow:0 2px 6px rgba(11,31,58,.06);}
.tile:nth-child(5n+2){--c:var(--teal);}
.tile:nth-child(5n+3){--c:var(--violet);}
.tile:nth-child(5n+4){--c:var(--amber);}
.tile:nth-child(5n+5){--c:var(--rose);}
.tile .ico{flex:none;width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:11px;background:var(--c);
  color:#fff;font-size:1.05rem;overflow:hidden;}
.tile .ico:has(img){background:#fff;border:1.5px solid var(--line);}
.tile .ico img{width:28px;height:28px;object-fit:contain;transition:transform .3s;}
.tile .ico i{transition:transform .3s;}
.tile:hover{transform:translateY(-5px);box-shadow:var(--shadow);}
.tile:hover .ico img,.tile:hover .ico i{transform:scale(1.2) rotate(-6deg);}

/* projects */
.thumb{height:200px;overflow:hidden;border-radius:12px;margin:.3rem 0 1.1rem;background:#DBEAFE;display:flex;align-items:center;
  justify-content:center;color:var(--blue);border:1.5px solid var(--line);}
.thumb img{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .5s;}
.card:hover .thumb img{transform:scale(1.08);}

/* experience timeline */
.timeline{border-left:4px solid #FCD34D;margin-left:.6rem;padding-left:1.7rem;}
.tl-item{position:relative;margin-bottom:1.5rem;}
.tl-item:before{content:"";position:absolute;left:-2.5rem;top:1.9rem;width:16px;height:16px;border-radius:50%;background:var(--amber);
  border:3px solid var(--paper);box-shadow:0 0 0 2px var(--amber);}
.tl-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.6rem;flex-wrap:wrap;}
.tl-head .h3{margin:.2rem 0 0;}

/* certificates & education */
.cert-ico,.edu-ico{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:var(--g-blue);
  color:#fff;font-size:1.25rem;margin:.4rem 0 .9rem;transition:.3s;box-shadow:0 8px 18px rgba(37,99,235,.35);}
.edu-ico{background:var(--g-green);box-shadow:0 8px 18px rgba(5,150,105,.35);}
.card:hover .cert-ico,.card:hover .edu-ico{transform:rotate(-8deg) scale(1.12);}
.card.eq{min-height:250px;}
.stDownloadButton{margin-top:.7rem;}
.score{display:inline-block;margin-top:.7rem;font-weight:800;color:#065F46 !important;background:#D1FAE5;border:1px solid #6EE7B7;padding:.2rem .7rem;border-radius:8px;}

/* contact */
.info{display:flex;gap:.9rem;align-items:center;padding:.75rem 0;border-bottom:1.5px solid var(--line);}
.info:last-child{border:0;}
.info .ico{flex:none;width:42px;height:42px;border-radius:12px;background:var(--g-teal);color:#fff;display:flex;align-items:center;
  justify-content:center;transition:.25s;}
.info:hover .ico{transform:scale(1.1) rotate(-5deg);}
.info a{color:var(--ink) !important;text-decoration:none;font-weight:700;word-break:break-all;}
.info a:hover{color:var(--blue) !important;}
[data-testid="stForm"]{background:var(--card);border:1.5px solid var(--line);border-top:6px solid var(--rose);border-radius:18px;padding:1.5rem;box-shadow:var(--shadow);}
.foot{text-align:center;color:var(--muted);font-size:.85rem;margin-top:3.2rem;padding:1.3rem;border-top:1.5px solid var(--line);}

/* ===== Streamlit widgets: explicit colours (fixes invisible text) ===== */
[data-testid="stWidgetLabel"],[data-testid="stWidgetLabel"] *{color:var(--ink) !important;font-weight:700;}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="select"]>div{background:#fff !important;border:1.5px solid #94A3B8 !important;border-radius:10px !important;}
[data-baseweb="input"] input,[data-baseweb="textarea"] textarea,[data-baseweb="select"] *{color:var(--ink) !important;background:transparent !important;}
input::placeholder,textarea::placeholder{color:#64748B !important;}
[data-baseweb="popover"] [role="listbox"],[data-baseweb="menu"]{background:#fff !important;}
[data-baseweb="popover"] li,[data-baseweb="popover"] li *{color:var(--ink) !important;}
/* solid buttons: View dashboard, Download certificate */
[data-testid^="stBaseButton-secondary"],[data-testid^="stBaseButton-primary"]{background:var(--navy) !important;border:2px solid var(--navy) !important;
  border-radius:12px;font-weight:700;transition:.25s;}
[data-testid^="stBaseButton-secondary"] *,[data-testid^="stBaseButton-primary"] *{color:#fff !important;}
[data-testid^="stBaseButton-secondary"]:hover,[data-testid^="stBaseButton-primary"]:hover{background:var(--blue) !important;border-color:var(--blue) !important;
  transform:translateY(-3px);box-shadow:var(--shadow-lg);}
/* outline buttons: GitHub, open in email */
[data-testid^="stBaseLinkButton"]{background:#fff !important;border:2px solid var(--navy) !important;border-radius:12px;font-weight:700;transition:.25s;}
[data-testid^="stBaseLinkButton"] *{color:var(--navy) !important;}
[data-testid^="stBaseLinkButton"]:hover{background:var(--navy) !important;transform:translateY(-3px);box-shadow:var(--shadow);}
[data-testid^="stBaseLinkButton"]:hover *{color:#fff !important;}
/* send button */
[data-testid*="FormSubmit"]{background:var(--g-blue) !important;border:0 !important;padding:.55rem 1.5rem;}
/* hero resume button */
[data-testid="stHorizontalBlock"]:has(.hero) [data-testid^="stBaseButton"]{background:#fff !important;border-color:#fff !important;}
[data-testid="stHorizontalBlock"]:has(.hero) [data-testid^="stBaseButton"] *{color:var(--navy) !important;}
[data-testid="stHorizontalBlock"]:has(.hero) [data-testid^="stBaseButton"]:hover{background:#99F6E4 !important;border-color:#99F6E4 !important;}
[data-testid="stHorizontalBlock"]:has(.hero) [data-testid="stCaptionContainer"] *{color:#BFDBFE !important;}
/* filter pills and segmented control */
[data-testid="stButtonGroup"] button,[data-testid^="stBaseButton-pills"],[data-testid^="stBaseButton-segmented_control"]{background:#fff !important;border:1.5px solid #94A3B8 !important;}
[data-testid="stButtonGroup"] button *,[data-testid^="stBaseButton-pills"] *,[data-testid^="stBaseButton-segmented_control"] *{color:var(--navy) !important;font-weight:700;}
[data-testid="stButtonGroup"] button:hover{border-color:var(--blue) !important;background:#DBEAFE !important;}
[data-testid="stButtonGroup"] button[aria-checked="true"],[data-testid="stButtonGroup"] button[data-selected="true"],[data-testid$="Active"][data-testid^="stBaseButton-pills"],[data-testid$="Active"][data-testid^="stBaseButton-segmented_control"]{background:var(--navy) !important;border-color:var(--navy) !important;}
[data-testid="stButtonGroup"] button[aria-checked="true"] *,[data-testid="stButtonGroup"] button[data-selected="true"] *,[data-testid$="Active"][data-testid^="stBaseButton-pills"] *,[data-testid$="Active"][data-testid^="stBaseButton-segmented_control"] *{color:#fff !important;}
/* tabs */
button[data-baseweb="tab"]{background:transparent !important;font-weight:700;}
button[data-baseweb="tab"] *{color:var(--muted) !important;}
button[data-baseweb="tab"][aria-selected="true"] *{color:var(--blue) !important;}
[data-baseweb="tab-highlight"]{background:var(--blue) !important;height:3px;}
[data-baseweb="tab-border"]{background:var(--line) !important;}
[data-testid="stTab"]{background:transparent !important;}
[data-testid="stTab"] *{color:var(--muted) !important;font-weight:700;font-size:1rem;}
[data-testid="stTab"][aria-selected="true"] *{color:var(--blue) !important;}
.react-aria-SelectionIndicator{background:var(--blue) !important;}
/* alerts */
[data-testid="stAlertContainer"]{border-radius:12px;border:1.5px solid #93C5FD;background:#DBEAFE;}
[data-testid="stAlertContainer"] *{color:#1E3A8A !important;font-weight:600;}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]){background:#D1FAE5;border-color:#6EE7B7;}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) *{color:#065F46 !important;}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"]){background:#FEE2E2;border-color:#FCA5A5;}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"]) *{color:#991B1B !important;}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"]){background:#FEF3C7;border-color:#FCD34D;}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"]) *{color:#92400E !important;}
@media (max-width:640px){.sec{font-size:1.7rem;}.nav a{padding:.4rem .6rem;font-size:.8rem;}
  [data-testid="stHorizontalBlock"]:has(.hero){padding:1.6rem 1.2rem;}}
</style>
"""

# Markdown ends an HTML block at the first blank line, so strip them.
CSS = "\n".join(line for line in CSS.splitlines() if line.strip())