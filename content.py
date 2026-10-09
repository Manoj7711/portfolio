"""All portfolio text lives here. Edit this file to update the site."""

NAME = "Manoj"
EMAIL = "manojnyol77@gmail.com"  
LOCATION = "Jaipur, India"
RESUME = "Manoj_Resume.pdf"
PHOTO = "me.png"

LINKS = {
    "LinkedIn": ("https://www.linkedin.com/in/manoj2903/", "fa-brands fa-linkedin"),
    "GitHub": ("https://github.com/Manoj7711", "fa-brands fa-github"),
    "Instagram": ("https://www.instagram.com/manojnyol01/", "fa-brands fa-instagram"),
}

HEADLINE = "I turn raw data into decisions people can act on."
SUMMARY = ("Information Technology graduate who cleans, explores and visualizes data with "
           "Python, SQL, Excel and Power BI, then explains what it means in plain language.")

ABOUT = [
    "I like to understand the problem first, then let the data answer it. My work combines "
    "analytical thinking, technical skills and clear visualization so findings are easy to use.",
    "I work with Python, SQL, Excel, Power BI and Streamlit, and I'm building my skills in "
    "business intelligence and machine learning.",
]

WHAT_I_DO = [
    ("Data analysis", "Find patterns, trends and KPIs that answer real business questions."),
    ("Cleaning & preparation", "Fix missing values, duplicates and inconsistent formats."),
    ("Exploratory analysis", "Explore distributions and compare segments with Python, SQL and Excel."),
    ("Dashboards", "Build KPI reports in Power BI, Excel and Streamlit."),
    ("Communication", "Explain what the data shows and why it matters."),
]

PROCESS = ["Understand the problem", "Prepare the data", "Clean & validate",
           "Analyze & explore", "Visualize & build", "Communicate insights"]

# (label, local icon file, Font Awesome fallback used when the file is missing)
SKILLS = {
    "Programming": [("Python", "python.jpg", "fa-brands fa-python"), ("C++", "c++.png", "fa-solid fa-code"),
                    ("NumPy", "numpy.png", "fa-solid fa-calculator"), ("Pandas", "pandas.png", "fa-solid fa-table")],
    "Databases": [("MySQL", "mysql.png", "fa-solid fa-database"),
                  ("MySQL Workbench", "workbench.png", "fa-solid fa-server")],
    "Analysis": [("Data Cleaning", "dataclean.png", "fa-solid fa-broom"),
                 ("Exploratory Data Analysis", "eda.png", "fa-solid fa-magnifying-glass-chart"),
                 ("Statistical Analysis", "stats.jpg", "fa-solid fa-chart-simple"),
                 ("Trend Analysis", "trend.jpg", "fa-solid fa-arrow-trend-up"),
                 ("KPI Tracking", "kpi.png", "fa-solid fa-bullseye")],
    "BI & Visualization": [("Power BI", "bi.jpg", "fa-solid fa-chart-column"),
                           ("Advanced Excel", "excel.jpg", "fa-solid fa-file-excel"),
                           ("Matplotlib", "matplotlib.png", "fa-solid fa-chart-line"),
                           ("Seaborn", "seaborn.png", "fa-solid fa-chart-area"),
                           ("Streamlit", "streamlit.png", "fa-solid fa-layer-group"),
                           ("Dashboard Development", "dashdevelopment.png", "fa-solid fa-gauge"),
                           ("Data Storytelling", "storytelling.png", "fa-solid fa-book-open")],
    "Tools": [("Jupyter Notebook", "jupyter.png", "fa-solid fa-book"), ("VS Code", "vs.jpg", "fa-solid fa-laptop-code"),
              ("Git / GitHub", "git.png", "fa-brands fa-git-alt"), ("Spreadsheets", "spreadsheet.jpg", "fa-solid fa-table-cells")],
}

STRENGTHS = ["Analytical thinking", "Problem solving", "Attention to detail",
             "Data-driven decisions", "Communicating insights", "Fast, self-driven learner"]

PROJECTS = [
    {
        "title": "Superstore Sales Analysis",
        "tools": ["Excel", "Power BI", "Python", "Jupyter"],
        "points": [
            "Cleaned and transformed raw sales data for reliable analysis.",
            "Ran EDA on sales, profit and customer purchasing trends.",
            "Compared category and region performance to surface growth opportunities.",
            "Built an interactive Power BI dashboard of KPIs for stakeholder reporting.",
        ],
        "image": "Superstore.png",
        "github": "https://github.com/Manoj7711/Superstore-Sales-Analysis",
    },
    {
        "title": "HR Attrition Analysis",
        "tools": ["Excel", "MySQL", "Python", "Power BI"],
        "points": [
            "Cleaned and preprocessed employee data for accurate analysis.",
            "Ran EDA on attrition, job satisfaction and workforce trends.",
            "Wrote SQL queries to consolidate insights across departments and job roles.",
            "Built a Power BI dashboard tracking attrition rate, headcount and other HR metrics.",
        ],
        "image": "Attrition.png",
        "github": "https://github.com/Manoj7711/HR-Attrition-Dashboard",
    },
]

EXPERIENCE = [
    {
        "role": "Data Analytics Intern", "org": "Unified Mentor", "when": "Mar 2026 – Jun 2026 · 60 days",
        "overview": "Hands-on analytics projects covering the full workflow, from raw data to reporting.",
        "points": [
            "Cleaned, preprocessed and explored real datasets.",
            "Found patterns, trends and business insights through EDA.",
            "Built visualizations and Power BI dashboards to communicate findings.",
            "Turned raw datasets into clear, decision-ready insights.",
        ],
        "tools": ["Python", "Pandas", "NumPy", "Excel", "SQL", "Power BI"],
    },
    {
        "role": "Web Developer Intern", "org": "Excellence Technology", "when": "Jun 2025 – Jul 2025 · 45 days",
        "overview": "Practical internship building a database-driven web application.",
        "points": [
            "Built a Hotel Management System with PHP and MySQL.",
            "Designed pages in HTML and CSS and added interactivity with JavaScript.",
            "Handled server-side logic in PHP and stored application data in MySQL.",
            "Developed, tested and debugged the application on a local XAMPP environment.",
        ],
        "tools": ["PHP", "MySQL", "HTML", "CSS", "JavaScript", "XAMPP"],
    },
]

CERTS = [
    ("Data Analytics Internship", "Unified Mentor", "unified_mentor.pdf", "fa-solid fa-chart-pie"),
    ("Web Development Internship", "Excellence Technology", "excellence.pdf", "fa-solid fa-code"),
    ("IBM Data Science Professional Certificate", "IBM", "IBM_Data_Science.pdf", "fa-solid fa-flask"),
    ("Microsoft Azure SQL", "Microsoft", "Microsoft_Azure_SQL.pdf", "fa-solid fa-database"),
]

EDUCATION = [
    ("B.Tech, Information Technology", "SKIT College, Jaipur", "CGPA 7.40", "fa-solid fa-graduation-cap"),
    ("Intermediate (PCM)", "Prince High School, Sikar", "78.80%", "fa-solid fa-school"),
    ("Matriculation", "Sai Discovery Sr. Sec. School", "83.30%", "fa-solid fa-book-open-reader"),
]

SUBJECTS = ["Job opportunity", "Project collaboration", "Feedback", "Other"]