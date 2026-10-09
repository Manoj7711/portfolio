"""Global CSS and fonts for the portfolio."""

CSS = """
<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
:root{--ink:#14213D;--teal:#0F766E;--amber:#D98E04;--paper:#F6F7F9;--card:#fff;--line:#DFE3EA;--muted:#5B6474;
  --shadow:0 10px 26px rgba(20,33,61,.10);}
html{scroll-behavior:smooth;}
html,body,[class*="css"],.stApp{font-family:'Plus Jakarta Sans',sans-serif;color:var(--ink);}
.stApp{background:var(--paper);}
#MainMenu,footer,header[data-testid="stHeader"],[data-testid="stSidebar"],[data-testid="collapsedControl"]{display:none !important;}
.block-container{max-width:1080px;padding:0 1.25rem 3rem;}
.h1,.h2,.h3,h1,h2,h3{font-family:'DM Serif Display',serif;color:var(--ink);letter-spacing:-.01em;}
.h1,.h2,.h3{display:block;}
.anchor{scroll-margin-top:70px;height:0;margin-top:3rem;}

/* navigation */
[data-testid="stElementContainer"]:has(.nav){position:sticky;top:0;z-index:50;}
.nav{display:flex;gap:.3rem;justify-content:center;flex-wrap:wrap;
  padding:.6rem 1rem;background:rgba(246,247,249,.94);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);margin:0 -1.25rem 2rem;}
.nav a{color:var(--muted);text-decoration:none;font-weight:600;font-size:.9rem;padding:.4rem .85rem;
  border-radius:999px;transition:.2s;}
.nav a:hover{color:#fff;background:var(--ink);}
.to-top{position:fixed;right:1.2rem;bottom:1.2rem;z-index:60;width:44px;height:44px;border-radius:50%;
  background:var(--ink);color:#fff !important;display:flex;align-items:center;justify-content:center;
  text-decoration:none;box-shadow:var(--shadow);transition:.2s;}
.to-top:hover{background:var(--teal);transform:translateY(-3px);}

/* hero */
@keyframes rise{from{opacity:0;transform:translateY(14px);}to{opacity:1;transform:none;}}
.hero{animation:rise .7s ease both;}
.hero .h1{font-size:clamp(2.4rem,5vw,3.8rem);line-height:1.08;margin:.2rem 0 .6rem;}
.hero .role{color:var(--teal);font-weight:700;margin:0;}
.hero .lead{color:var(--muted);font-size:1.08rem;line-height:1.7;max-width:34rem;}
.icons a{display:inline-flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:50%;
  border:1px solid var(--line);background:var(--card);color:var(--ink);margin-right:.5rem;font-size:1.1rem;transition:.2s;}
.icons a:hover{background:var(--ink);color:#fff;transform:translateY(-3px);}
.photo{width:100%;max-width:340px;aspect-ratio:1/1;margin:0 auto;border-radius:28px;overflow:hidden;
  border:6px solid #fff;box-shadow:var(--shadow);transition:.4s;}
.photo img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s;}
.photo:hover{transform:rotate(-2deg) translateY(-4px);box-shadow:0 18px 40px rgba(20,33,61,.22);}
.photo:hover img{transform:scale(1.07);}
.photo.empty{display:flex;align-items:center;justify-content:center;background:#E6F2F1;color:var(--teal);font-size:4rem;}

/* generic blocks */
.stat{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1rem 1.2rem;transition:.25s;}
.stat:hover{transform:translateY(-4px);box-shadow:var(--shadow);}
.stat b{display:block;font-family:'DM Serif Display',serif;font-size:2rem;color:var(--teal);line-height:1.1;}
.stat span{color:var(--muted);font-size:.9rem;}
.sec{font-size:2rem;margin:.6rem 0 1.2rem;padding-bottom:.6rem;border-bottom:2px solid var(--ink);}
.sec small{display:block;font-family:'Plus Jakarta Sans',sans-serif;font-size:.9rem;color:var(--muted);margin-top:.2rem;}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1.4rem 1.5rem;
  height:100%;transition:.25s;}
.card:hover{transform:translateY(-4px);box-shadow:var(--shadow);border-color:#C9CFDA;}
.card .h3{font-size:1.4rem;margin:0 0 .3rem;}
.card ul{margin:.7rem 0 0;padding-left:1.1rem;color:#2B3446;line-height:1.65;font-size:.95rem;}
.meta{color:var(--muted);font-size:.9rem;margin:0;}
.lbl{font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin:1rem 0 .1rem;}
.chip{display:inline-block;padding:.28rem .8rem;margin:.22rem .3rem .22rem 0;border-radius:999px;font-size:.82rem;
  font-weight:600;background:#E6F2F1;color:#0B5B55;border:1px solid #C5E0DD;}
.chip.tool{background:#FBF1DC;color:#8A5A00;border-color:#F0DBAA;}
.badge{display:inline-block;padding:.25rem .75rem;border-radius:8px;font-size:.8rem;font-weight:700;
  background:var(--ink);color:#fff;}

/* about */
.step{display:flex;gap:.8rem;align-items:center;padding:.5rem .6rem;border-radius:10px;transition:.2s;}
.step:hover{background:#fff;transform:translateX(4px);}
.step i{flex:none;width:28px;height:28px;border-radius:50%;background:var(--ink);color:#fff;
  font-style:normal;font-size:.8rem;font-weight:700;display:flex;align-items:center;justify-content:center;}
.do{padding:.7rem 0;border-bottom:1px solid var(--line);}
.do b{color:var(--ink);}
.do span{color:var(--muted);}

/* skills */
.group{font-weight:700;margin:1.4rem 0 .6rem;display:flex;align-items:center;gap:.5rem;}
.group:after{content:"";flex:1;height:1px;background:var(--line);}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:.8rem;}
.tile{display:flex;align-items:center;gap:.75rem;padding:.7rem .9rem;background:var(--card);
  border:1px solid var(--line);border-radius:12px;font-weight:600;font-size:.92rem;transition:.25s;}
.tile .ico{flex:none;width:36px;height:36px;display:flex;align-items:center;justify-content:center;
  border-radius:9px;background:#E6F2F1;color:var(--teal);font-size:1.05rem;overflow:hidden;}
.tile .ico img{width:26px;height:26px;object-fit:contain;transition:transform .3s;}
.tile:hover{transform:translateY(-4px);box-shadow:var(--shadow);border-color:var(--teal);}
.tile:hover .ico img,.tile:hover .ico i{transform:scale(1.25) rotate(-6deg);}
.tile .ico i{transition:transform .3s;}

/* projects */
.thumb{height:190px;overflow:hidden;border-radius:10px;margin-bottom:1rem;background:#E9EDF3;
  display:flex;align-items:center;justify-content:center;color:var(--muted);}
.thumb img{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .5s;}
.card:hover .thumb img{transform:scale(1.08);}

/* experience timeline */
.timeline{border-left:2px solid var(--line);margin-left:.6rem;padding-left:1.6rem;}
.tl-item{position:relative;margin-bottom:1.4rem;}
.tl-item:before{content:"";position:absolute;left:-2.25rem;top:1.7rem;width:14px;height:14px;border-radius:50%;
  background:var(--amber);border:3px solid var(--paper);box-shadow:0 0 0 2px var(--amber);}
.tl-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.6rem;flex-wrap:wrap;}
.tl-head .h3{margin:0;}

/* certificates & education */
.cert-ico,.edu-ico{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;
  background:var(--ink);color:#fff;font-size:1.2rem;margin-bottom:.9rem;transition:.3s;}
.card:hover .cert-ico,.card:hover .edu-ico{background:var(--teal);transform:rotate(-8deg) scale(1.1);}
.card.eq{min-height:215px;}
#top.anchor{scroll-margin-top:400px;}
.score{display:inline-block;margin-top:.6rem;font-weight:700;color:var(--teal);}

/* contact */
.info{display:flex;gap:.9rem;align-items:center;padding:.7rem 0;border-bottom:1px solid var(--line);}
.info:last-child{border:0;}
.info .ico{flex:none;width:40px;height:40px;border-radius:10px;background:#E6F2F1;color:var(--teal);
  display:flex;align-items:center;justify-content:center;transition:.25s;}
.info:hover .ico{background:var(--teal);color:#fff;transform:scale(1.1);}
.info a{color:var(--ink);text-decoration:none;font-weight:600;word-break:break-all;}
.info a:hover{color:var(--teal);}
.foot{text-align:center;color:var(--muted);font-size:.85rem;margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);}

/* streamlit widgets */
.stButton>button,.stDownloadButton>button,.stFormSubmitButton>button,[data-testid="stLinkButton"] a{
  border-radius:10px;font-weight:600;border:1px solid var(--ink);transition:.2s;}
.stButton>button:hover,.stDownloadButton>button:hover,[data-testid="stLinkButton"] a:hover{
  transform:translateY(-2px);box-shadow:var(--shadow);}
.stFormSubmitButton>button{background:var(--ink);color:#fff;}
.stFormSubmitButton>button:hover{background:var(--teal);border-color:var(--teal);color:#fff;}
button[data-baseweb="tab"]{font-weight:600;}
@media (max-width:640px){.sec{font-size:1.6rem;}.nav a{padding:.35rem .6rem;font-size:.82rem;}}
</style>
"""

# Markdown ends an HTML block at the first blank line, so strip them.
CSS = "\n".join(line for line in CSS.splitlines() if line.strip())