"""Global CSS and fonts for the portfolio (modern indigo / cyan / emerald / amber theme)."""

CSS = """
<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
:root{--ink:#0F172A;--text:#334155;--muted:#64748B;--line:#E2E8F0;--paper:#F8FAFC;--card:#fff;
  --indigo:#4F46E5;--violet:#7C3AED;--cyan:#0891B2;--emerald:#059669;--amber:#F59E0B;--rose:#E11D48;
  --g-indigo:linear-gradient(135deg,#4F46E5,#7C3AED);--g-cyan:linear-gradient(135deg,#0891B2,#4F46E5);
  --g-emerald:linear-gradient(135deg,#059669,#0891B2);--g-amber:linear-gradient(135deg,#F59E0B,#E11D48);
  --shadow:0 10px 30px rgba(15,23,42,.08);--shadow-lg:0 18px 44px rgba(79,70,229,.18);}
html{scroll-behavior:smooth;}
html,body,[class*="css"],.stApp{font-family:'Plus Jakarta Sans',sans-serif;color:var(--text);}
.stApp{background:radial-gradient(1100px 480px at 8% -8%,#E0E7FF 0,transparent 60%),radial-gradient(900px 420px at 100% 0,#CFFAFE 0,transparent 55%),var(--paper);}
#MainMenu,footer,header[data-testid="stHeader"],[data-testid="stSidebar"],[data-testid="collapsedControl"]{display:none !important;}
.block-container{max-width:1100px;padding:0 1.25rem 3rem;}
.h1,.h2,.h3,h1,h2,h3{font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;color:var(--ink);letter-spacing:-.02em;}
.h1,.h2,.h3{display:block;}
.anchor{scroll-margin-top:80px;height:0;margin-top:3.4rem;}
#top.anchor{scroll-margin-top:400px;margin-top:0;}

/* navigation: floating glass pill */
[data-testid="stElementContainer"]:has(.nav){position:sticky;top:0;z-index:50;text-align:center;}
.nav{display:inline-flex;gap:.2rem;flex-wrap:wrap;justify-content:center;margin:.7rem auto 1.6rem;padding:.35rem;
  background:rgba(255,255,255,.82);backdrop-filter:blur(14px);border:1px solid var(--line);border-radius:999px;box-shadow:var(--shadow);}
.nav a{color:var(--text);text-decoration:none;font-weight:600;font-size:.88rem;padding:.45rem .95rem;border-radius:999px;transition:.2s;}
.nav a:hover{color:#fff;background:var(--g-indigo);transform:translateY(-1px);}
.to-top{position:fixed;right:1.2rem;bottom:1.2rem;z-index:60;width:46px;height:46px;border-radius:50%;background:var(--g-indigo);
  color:#fff !important;display:flex;align-items:center;justify-content:center;text-decoration:none;box-shadow:var(--shadow-lg);transition:.25s;}
.to-top:hover{transform:translateY(-4px) scale(1.06);}

/* hero panel */
@keyframes rise{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:none;}}
[data-testid="stHorizontalBlock"]:has(.hero){background:radial-gradient(600px 300px at 90% 0,rgba(8,145,178,.45),transparent 70%),
  linear-gradient(135deg,#0F172A 0%,#1E1B4B 55%,#312E81 100%);border-radius:28px;padding:2.6rem 2.4rem;box-shadow:var(--shadow-lg);}
.hero{animation:rise .7s ease both;}
.hero .role{display:inline-block;color:#A5F3FC;background:rgba(165,243,252,.12);border:1px solid rgba(165,243,252,.3);
  font-weight:700;font-size:.85rem;padding:.3rem .85rem;border-radius:999px;margin:0 0 .8rem;}
.hero .h1{font-size:clamp(2.2rem,4.6vw,3.5rem);line-height:1.1;margin:.1rem 0 .9rem;color:#fff;}
.hero .lead{color:#CBD5E1;font-size:1.05rem;line-height:1.75;max-width:34rem;}
.icons a{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:12px;
  border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.08);color:#fff;margin-right:.55rem;font-size:1.1rem;transition:.25s;}
.icons a:hover{background:#fff;color:var(--indigo);transform:translateY(-4px);}
[data-testid="stHorizontalBlock"]:has(.hero) .stDownloadButton>button{background:#fff;color:var(--ink);border:0;}
[data-testid="stHorizontalBlock"]:has(.hero) .stDownloadButton>button:hover{background:#A5F3FC;}
[data-testid="stHorizontalBlock"]:has(.hero) [data-testid="stCaptionContainer"]{color:#94A3B8;}
.photo{width:100%;max-width:320px;aspect-ratio:1/1;margin:0 auto;border-radius:30px;overflow:hidden;padding:5px;
  background:linear-gradient(135deg,#22D3EE,#818CF8,#F472B6);box-shadow:0 20px 50px rgba(0,0,0,.4);transition:.4s;}
.photo img{width:100%;height:100%;object-fit:cover;display:block;border-radius:26px;transition:transform .5s;}
.photo:hover{transform:rotate(-2.5deg) translateY(-6px) scale(1.02);}
.photo:hover img{transform:scale(1.07);}
.photo.empty{display:flex;align-items:center;justify-content:center;color:#fff;font-size:4rem;}

/* stats: one colour each */
.stat{--c:var(--indigo);background:var(--card);border:1px solid var(--line);border-top:4px solid var(--c);border-radius:16px;
  padding:1rem 1.2rem;transition:.25s;box-shadow:0 2px 8px rgba(15,23,42,.04);}
[data-testid="stColumn"]:nth-child(2) .stat{--c:var(--cyan);}
[data-testid="stColumn"]:nth-child(3) .stat{--c:var(--emerald);}
[data-testid="stColumn"]:nth-child(4) .stat{--c:var(--amber);}
.stat:hover{transform:translateY(-5px);box-shadow:var(--shadow);}
.stat b{display:block;font-size:2.1rem;font-weight:800;color:var(--c);line-height:1.1;}
.stat span{color:var(--muted);font-size:.9rem;font-weight:500;}

/* section titles */
.sec{font-size:2.1rem;margin:.4rem 0 1.4rem;color:var(--ink);}
.sec:after{content:"";display:block;width:64px;height:5px;border-radius:9px;background:var(--g-indigo);margin-top:.6rem;}
.sec small{display:block;font-size:.95rem;font-weight:500;letter-spacing:0;color:var(--muted);margin-top:.25rem;}

/* cards: coloured top bar per section */
.card{--grad:var(--g-indigo);position:relative;overflow:hidden;background:var(--card);border:1px solid var(--line);border-radius:18px;
  padding:1.5rem 1.55rem;height:100%;transition:.3s;box-shadow:0 2px 8px rgba(15,23,42,.04);}
.card:before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:var(--grad);}
.card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:#C7D2FE;}
.card:has(.thumb){--grad:var(--g-cyan);min-height:545px;}
.tl-item .card{--grad:var(--g-amber);}
.card:has(.cert-ico){--grad:var(--g-indigo);}
.card:has(.edu-ico){--grad:var(--g-emerald);}
.card:has(.info){--grad:var(--g-cyan);}
.card .h3{font-size:1.35rem;margin:0 0 .3rem;line-height:1.25;}
.card ul{margin:.7rem 0 0;padding-left:1.1rem;color:var(--text);line-height:1.7;font-size:.95rem;}
.card li::marker{color:var(--indigo);}
.meta{color:var(--muted);font-size:.9rem;margin:0;font-weight:500;}
.lbl{font-size:.74rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--indigo);margin:1.1rem 0 .15rem;}
.chip{display:inline-block;padding:.28rem .8rem;margin:.22rem .3rem .22rem 0;border-radius:999px;font-size:.8rem;font-weight:600;
  background:#EEF2FF;color:#4338CA;border:1px solid #C7D2FE;transition:.2s;}
.chip.tool{background:#ECFEFF;color:#0E7490;border-color:#A5F3FC;}
.chip:hover{transform:translateY(-2px);box-shadow:0 4px 10px rgba(15,23,42,.08);}
.badge{display:inline-block;padding:.3rem .8rem;border-radius:10px;font-size:.78rem;font-weight:700;background:#FEF3C7;color:#92400E;border:1px solid #FDE68A;}

/* about */
.step{display:flex;gap:.8rem;align-items:center;padding:.55rem .7rem;border-radius:12px;transition:.2s;}
.step:hover{background:#EEF2FF;transform:translateX(5px);}
.step i{flex:none;width:30px;height:30px;border-radius:50%;background:var(--g-indigo);color:#fff;font-style:normal;font-size:.8rem;
  font-weight:700;display:flex;align-items:center;justify-content:center;}
.do{padding:.75rem 0;border-bottom:1px solid var(--line);}
.do b{color:var(--ink);}
.do span{color:var(--muted);}

/* skills: tile icons cycle through the palette */
.group{font-weight:800;color:var(--ink);margin:1.5rem 0 .7rem;display:flex;align-items:center;gap:.6rem;}
.group:before{content:"";width:6px;height:20px;border-radius:4px;background:var(--g-cyan);}
.group:after{content:"";flex:1;height:1px;background:var(--line);}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:.85rem;}
.tile{--c:var(--indigo);display:flex;align-items:center;gap:.8rem;padding:.75rem .95rem;background:var(--card);border:1px solid var(--line);
  border-radius:14px;font-weight:600;font-size:.92rem;color:var(--ink);transition:.25s;}
.tile:nth-child(5n+2){--c:var(--cyan);}
.tile:nth-child(5n+3){--c:var(--emerald);}
.tile:nth-child(5n+4){--c:#D97706;}
.tile:nth-child(5n+5){--c:var(--rose);}
.tile .ico{flex:none;width:38px;height:38px;display:flex;align-items:center;justify-content:center;border-radius:11px;
  background:color-mix(in srgb,var(--c) 12%,white);color:var(--c);font-size:1.05rem;overflow:hidden;}
.tile .ico img{width:26px;height:26px;object-fit:contain;transition:transform .3s;}
.tile .ico i{transition:transform .3s;}
.tile:hover{transform:translateY(-5px);box-shadow:var(--shadow);border-color:var(--c);}
.tile:hover .ico img,.tile:hover .ico i{transform:scale(1.25) rotate(-6deg);}

/* projects */
.thumb{height:200px;overflow:hidden;border-radius:12px;margin-bottom:1.1rem;background:#E0E7FF;display:flex;align-items:center;
  justify-content:center;color:var(--indigo);}
.thumb img{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .5s;}
.card:hover .thumb img{transform:scale(1.08);}

/* experience timeline */
.timeline{border-left:3px solid #FDE68A;margin-left:.6rem;padding-left:1.7rem;}
.tl-item{position:relative;margin-bottom:1.5rem;}
.tl-item:before{content:"";position:absolute;left:-2.43rem;top:1.8rem;width:16px;height:16px;border-radius:50%;background:var(--g-amber);
  border:3px solid var(--paper);box-shadow:0 0 0 2px #F59E0B;}
.tl-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.6rem;flex-wrap:wrap;}
.tl-head .h3{margin:0;}

/* certificates & education */
.cert-ico,.edu-ico{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:var(--g-indigo);
  color:#fff;font-size:1.25rem;margin:.3rem 0 .9rem;transition:.3s;box-shadow:0 8px 18px rgba(79,70,229,.3);}
.edu-ico{background:var(--g-emerald);box-shadow:0 8px 18px rgba(5,150,105,.3);}
.card:hover .cert-ico,.card:hover .edu-ico{transform:rotate(-8deg) scale(1.12);}
.card.eq{min-height:215px;}
.score{display:inline-block;margin-top:.7rem;font-weight:800;color:var(--emerald);background:#ECFDF5;border:1px solid #A7F3D0;
  padding:.2rem .7rem;border-radius:8px;}

/* contact */
.info{display:flex;gap:.9rem;align-items:center;padding:.75rem 0;border-bottom:1px solid var(--line);}
.info:last-child{border:0;}
.info .ico{flex:none;width:42px;height:42px;border-radius:12px;background:#ECFEFF;color:var(--cyan);display:flex;align-items:center;
  justify-content:center;transition:.25s;}
.info:hover .ico{background:var(--g-cyan);color:#fff;transform:scale(1.1) rotate(-5deg);}
.info a{color:var(--ink);text-decoration:none;font-weight:600;word-break:break-all;}
.info a:hover{color:var(--indigo);}
[data-testid="stForm"]{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--indigo);border-radius:18px;
  padding:1.5rem;box-shadow:var(--shadow);}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="select"]>div{border-radius:10px !important;}
.foot{text-align:center;color:var(--muted);font-size:.85rem;margin-top:3.2rem;padding:1.3rem;border-top:1px solid var(--line);}

/* streamlit widgets */
.stButton>button,.stDownloadButton>button,.stFormSubmitButton>button,[data-testid="stLinkButton"] a{border-radius:12px;font-weight:700;
  border:1px solid var(--line);transition:.25s;}
.stButton>button:hover,.stDownloadButton>button:hover,[data-testid="stLinkButton"] a:hover{transform:translateY(-3px);box-shadow:var(--shadow);
  border-color:var(--indigo);color:var(--indigo);}
.stFormSubmitButton>button{background:var(--g-indigo);color:#fff;border:0;padding:.55rem 1.4rem;}
.stFormSubmitButton>button:hover{filter:brightness(1.1);color:#fff;transform:translateY(-3px);box-shadow:var(--shadow-lg);}
button[data-baseweb="tab"]{font-weight:700;}
@media (max-width:640px){.sec{font-size:1.7rem;}.nav a{padding:.4rem .6rem;font-size:.8rem;}
  [data-testid="stHorizontalBlock"]:has(.hero){padding:1.6rem 1.2rem;}}
</style>
"""

# Markdown ends an HTML block at the first blank line, so strip them.
CSS = "\n".join(line for line in CSS.splitlines() if line.strip())