import base64
import re
import smtplib
import time
from email.message import EmailMessage
from pathlib import Path
from urllib.parse import quote

import streamlit as st

import content as c
from styles import CSS

BASE = Path(__file__).parent
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}

st.set_page_config(page_title=f"{c.NAME} | Data Analyst Portfolio", page_icon="📊",
                   layout="wide", initial_sidebar_state="collapsed")
st.markdown(CSS, unsafe_allow_html=True)


# ───────────────────────── helpers ─────────────────────────
@st.cache_data(show_spinner=False)
def image_uri(name: str):
    
    path = BASE / name
    if not path.exists():
        return None
    mime = MIME.get(path.suffix.lower(), "image/png")
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def file_bytes(name: str):
    path = BASE / name
    return path.read_bytes() if path.exists() else None


def section(title: str, anchor: str, subtitle: str = ""):
    sub = f"<small>{subtitle}</small>" if subtitle else ""
    
    st.markdown(f'<div id="{anchor}" class="anchor"></div><div class="sec h2">{title}{sub}</div>',
                unsafe_allow_html=True)


def chips(items, kind: str = "") -> str:
    return "".join(f'<span class="chip {kind}">{i}</span>' for i in items)


def bullets(points) -> str:
    return "<ul>" + "".join(f"<li>{p}</li>" for p in points) + "</ul>"


def send_email(name: str, email: str, subject: str, message: str) -> bool:
    
    try:
        cfg = st.secrets["smtp"]
        msg = EmailMessage()
        msg["Subject"] = f"[Portfolio] {subject} - {name}"
        msg["From"], msg["To"], msg["Reply-To"] = cfg["user"], cfg.get("to", cfg["user"]), email
        msg.set_content(f"From: {name} <{email}>\nSubject: {subject}\n\n{message}")
        with smtplib.SMTP(cfg.get("host", "smtp.gmail.com"), int(cfg.get("port", 587)), timeout=15) as server:
            server.starttls()
            server.login(cfg["user"], cfg["password"])
            server.send_message(msg)
        return True
    except Exception:
        return False


def validate_contact(name: str, email: str, message: str) -> list[str]:
    errors = []
    if not re.fullmatch(r"[A-Za-z][A-Za-z .'\-]{1,59}", name):
        errors.append("Enter your full name (2–60 letters).")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", email) or len(email) > 120:
        errors.append("Enter a valid email address, e.g. name@example.com.")
    if len(message) < 20:
        errors.append(f"Message is too short ({len(message)}/20 characters minimum).")
    elif len(message) > 1000:
        errors.append("Message is too long (1000 characters maximum).")
    return errors


@st.dialog("Dashboard preview", width="large")
def preview_dialog(image_path: str):
    st.image(image_path, width="stretch")


# ───────────────────────── sections ─────────────────────────
def navbar():
    items = [("Home", "top"), ("About", "about"), ("Skills", "skills"), ("Projects", "projects"),
             ("Experience", "experience"), ("Certifications", "certifications"),
             ("Education", "education"), ("Contact", "contact")]
    links = "".join(f'<a href="#{anchor}" target="_self">{label}</a>' for label, anchor in items)
    st.markdown(f'<div class="nav">{links}</div>'
                '<a class="to-top" href="#top" target="_self" title="Back to top">'
                '<i class="fa-solid fa-arrow-up"></i></a>', unsafe_allow_html=True)


def hero():
    left, right = st.columns([1.6, 1], gap="large", vertical_alignment="center")
    with left:
        icons = "".join(f'<a href="{url}" target="_blank" rel="noopener" title="{n}"><i class="{ico}"></i></a>'
                        for n, (url, ico) in c.LINKS.items())
        icons += f'<a href="mailto:{c.EMAIL}" title="Email"><i class="fa-solid fa-envelope"></i></a>'
        st.markdown(f'<div id="top" class="anchor"></div><div class="hero"><p class="role">Data Analyst · {c.LOCATION}</p>'
                    f'<div class="h1">{c.HEADLINE}</div><p class="lead">{c.SUMMARY}</p>'
                    f'<div class="icons">{icons}</div></div>', unsafe_allow_html=True)
        st.write("")
        resume = file_bytes(c.RESUME)
        if resume:
            st.download_button("Download resume", resume, file_name=c.RESUME,
                               mime="application/pdf", icon=":material/download:")
        else:
            st.caption(f"Add {c.RESUME} next to app.py to enable the resume download.")
    with right:
        photo = image_uri(c.PHOTO)
        inner = (f'<div class="photo"><img src="{photo}" alt="{c.NAME}"></div>' if photo
                 else '<div class="photo empty"><i class="fa-solid fa-user"></i></div>')
        st.markdown(inner, unsafe_allow_html=True)

    skill_count = sum(len(v) for v in c.SKILLS.values())
    stats = [(len(c.PROJECTS), "Projects"), (f"{skill_count}+", "Skills & tools"),
             (len(c.EXPERIENCE), "Internships"), (len(c.CERTS), "Certifications")]
    st.write("")
    for col, (value, label) in zip(st.columns(4), stats):
        col.markdown(f'<div class="stat"><b>{value}</b><span>{label}</span></div>', unsafe_allow_html=True)


def about():
    section("About", "about", "Who I am and how I work")
    left, right = st.columns(2, gap="large")
    with left:
        for paragraph in c.ABOUT:
            st.write(paragraph)
        st.info("Focus: turning complex data into clear insight for decision-making.")
    with right:
        what, how = st.tabs(["What I do", "How I work"])
        with what:
            st.markdown("".join(f'<div class="do"><b>{t}</b><br><span>{d}</span></div>'
                                for t, d in c.WHAT_I_DO), unsafe_allow_html=True)
        with how:
            st.markdown("".join(f'<div class="step"><i>{n}</i><span>{s}</span></div>'
                                for n, s in enumerate(c.PROCESS, 1)), unsafe_allow_html=True)


def skill_tile(label: str, image: str, icon: str) -> str:
    uri = image_uri(image)
    visual = f'<img src="{uri}" alt="{label}">' if uri else f'<i class="{icon}"></i>'
    return f'<div class="tile"><span class="ico">{visual}</span><span>{label}</span></div>'


def skills():
    section("Skills", "skills", "Tools and techniques I work with")
    choice = st.pills("Category", ["All", *c.SKILLS], default="All", label_visibility="collapsed") or "All"
    groups = c.SKILLS if choice == "All" else {choice: c.SKILLS[choice]}
    for group, items in groups.items():
        tiles = "".join(skill_tile(*item) for item in items)
        st.markdown(f'<div class="group">{group}</div><div class="tiles">{tiles}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="group">Strengths</div>{chips(c.STRENGTHS, "tool")}', unsafe_allow_html=True)


def projects():
    section("Projects", "projects", "Dashboards and analyses I've built")
    tools = sorted({t for p in c.PROJECTS for t in p["tools"]})
    choice = st.segmented_control("Tool", ["All", *tools], default="All", label_visibility="collapsed") or "All"
    shown = [p for p in c.PROJECTS if choice == "All" or choice in p["tools"]]
    if not shown:
        st.info("No projects match this filter.")
        return
    for col, p in zip(st.columns(2, gap="large"), shown):
        with col:
            uri = image_uri(p["image"])
            thumb = (f'<div class="thumb"><img src="{uri}" alt="{p["title"]}"></div>' if uri
                     else '<div class="thumb"><i class="fa-solid fa-chart-column fa-2x"></i></div>')
            st.markdown(f'<div class="card">{thumb}<div class="h3">{p["title"]}</div>{chips(p["tools"], "tool")}'
                        f'{bullets(p["points"])}</div>', unsafe_allow_html=True)
            st.write("")
            b1, b2 = st.columns(2)
            if uri and b1.button("View dashboard", key=f"dash_{p['title']}",
                                 icon=":material/dashboard:", width="stretch"):
                preview_dialog(str(BASE / p["image"]))
            b2.link_button("View on GitHub", p["github"], icon=":material/code:", width="stretch")


def experience():
    section("Experience", "experience", "Internships and what I worked on")
    items = ""
    for e in c.EXPERIENCE:
        items += (f'<div class="tl-item"><div class="card">'
                  f'<div class="tl-head"><div><div class="h3">{e["role"]}</div><p class="meta"><b>{e["org"]}</b></p></div>'
                  f'<span class="badge">{e["when"]}</span></div>'
                  f'<p style="margin:.8rem 0 0;color:#2B3446">{e["overview"]}</p>'
                  f'<div class="lbl">What I did</div>{bullets(e["points"])}'
                  f'<div class="lbl">Tools used</div>{chips(e["tools"], "tool")}</div></div>')
    st.markdown(f'<div class="timeline">{items}</div>', unsafe_allow_html=True)


def certifications():
    section("Certifications", "certifications", "Verified learning and training")
    for col, (title, issuer, filename, icon) in zip(st.columns(len(c.CERTS), gap="medium"), c.CERTS):
        with col:
            st.markdown(f'<div class="card eq"><div class="cert-ico"><i class="{icon}"></i></div>'
                        f'<div class="h3" style="font-size:1.1rem">{title}</div><p class="meta">{issuer}</p></div>',
                        unsafe_allow_html=True)
            data = file_bytes(filename)
            if data:
                st.download_button("Download certificate", data, file_name=filename, mime="application/pdf",
                                   key=f"cert_{filename}", icon=":material/download:", width="stretch")


def education():
    section("Education", "education", "Academic background")
    for col, (degree, school, score, icon) in zip(st.columns(len(c.EDUCATION), gap="large"), c.EDUCATION):
        col.markdown(f'<div class="card eq"><div class="edu-ico"><i class="{icon}"></i></div>'
                     f'<div class="h3" style="font-size:1.2rem">{degree}</div><p class="meta">{school}</p>'
                     f'<span class="score">{score}</span></div>', unsafe_allow_html=True)


def contact():
    section("Contact", "contact", "Open to full-time Data Analyst roles")
    form_col, info_col = st.columns([1.3, 1], gap="large")
    with form_col:
        with st.form("contact"):
            name = st.text_input("Full name *", placeholder="Your name", max_chars=60)
            email = st.text_input("Email *", placeholder="you@example.com", max_chars=120)
            subject = st.selectbox("Subject", c.SUBJECTS)
            message = st.text_area("Message * (20–1000 characters)", placeholder="How can I help?",
                                   height=140, max_chars=1000)
            submitted = st.form_submit_button("Send message", icon=":material/send:")
        if submitted:
            name, email, message = name.strip(), email.strip(), message.strip()
            errors = validate_contact(name, email, message)
            if time.time() - st.session_state.get("last_sent", 0) < 60:
                errors.append("Please wait a minute before sending another message.")
            if errors:
                st.error("Please fix the following:\n\n" + "\n".join(f"- {e}" for e in errors))
            elif send_email(name, email, subject, message):
                st.session_state["last_sent"] = time.time()
                st.success(f"Thanks {name.split()[0]}, your message was sent. I'll reply soon.")
            else:
                mailto = f"mailto:{c.EMAIL}?subject={quote(f'{subject} - {name}')}&body={quote(message)}"
                st.warning("Direct sending isn't set up, so send it from your email app instead.")
                st.link_button("Open in email app", mailto, icon=":material/mail:")
    with info_col:
        rows = [(f"mailto:{c.EMAIL}", c.EMAIL, "fa-solid fa-envelope"),
                ("#contact", c.LOCATION, "fa-solid fa-location-dot")]
        rows += [(url, n, ico) for n, (url, ico) in c.LINKS.items()]
        html = "".join(f'<div class="info"><span class="ico"><i class="{ico}"></i></span>'
                       f'<a href="{url}" target="{"_self" if url.startswith(("#", "mailto")) else "_blank"}">{label}</a></div>'
                       for url, label, ico in rows)
        st.markdown(f'<div class="card"><div class="h3">Let\'s connect</div>{html}</div>', unsafe_allow_html=True)


def footer():
    st.markdown(f'<div class="foot">© 2026 {c.NAME}. Built with Streamlit.</div>', unsafe_allow_html=True)


# ───────────────────────── page ─────────────────────────
navbar()
hero()
about()
skills()
projects()
experience()
certifications()
education()
contact()
footer()