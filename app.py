import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/006ee53e-c0c9-4228-9522-0e33db2c6c8d/WLgTSMosDM.json")

# ---- HEADER SECTION ----

with st.container():
    st.subheader("Hi, I am Felipe :wave:")
    st.title("A developer studying to transition into DevOps")
    st.write("I am passionate about cloud computing, automation with python and bash, linux and network.")
    st.write("[My projects on GitHub>](https://github.com/felipecostacouto)")
    st.write("[My Linkedin>](https://www.linkedin.com/in/felipe-monteiro-costa-couto-841582188/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Summary")
        st.write("##")
        st.write(
            """
            I am currently dedicated to studying the fundamental principles of DevOps, which encompass development 
            (Python and Bash), AWS, Linux, and other related tools. My objective is to pursue a career in Cloud 
            development.Leveraging my 2-year background as a support Salesforce developer within a Scrum team, I've 
            honed skills in maintaining production org environments, addressing bugs, and devising user-centric 
            solutions. My transition to DevOps involves a focus on automating deployment processes, enhancing system 
            reliability, and optimizing software delivery pipelines through cloud-native practices and infrastructure 
            as code methodologies.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# ---- TECHNICAL SKILLS ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Technical Skills")
        st.write("##")
        st.write(
            """
           **knowledge:** 
           - Java, Python, SQL language (mySQL), Git.
           
           **Current studying:**
           -  Aws (preparing for the Developer associate exam), Linux , programming (Python and Bash).
            """
        )

# ---- ACADEMICS ----
with st.container():
    st.write("---")
    st.header("Academic Education")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("#")
        st.write(
            """
            **University of São Paulo (USP)**
            - Bachelor of Information Systems - 2020/2023 (Graduated: December 2023).
            """
        )
        st.write("### Languages")
        st.write(
            """
            - English (writing - advanced; speaking - advanced; reading - advanced).
            - Portuguese ( Native Language);
            """
        )

# ---- WORK EXPERIENCE/ RESPONSIBILITIES ----
with st.container():
    st.write("---")
    st.header("Work Experience")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **GLOBANT ( IT services and consulting )**  
            - Salesforce Developer Jr. - Jan/2023 - Current Job.  
            - Salesforce Developer Trainee - Jan/2022 - Dec/2022.  
            - Salesforce Developer Intern - July/2021 - Jan/2022.
            """
        )
        st.write("### Responsibilities")
        st.write(
            """
                - Working as a support Salesforce Developer in a SCRUM team.
                - Administration/Support on the Salesforce production org.
                - Fixing minor bugs in the production environment. 
                - maintaining direct contact with users, offering solutions and implementing best practices.
                - Development using Apex programming language.
                - Development of test classes, flows, SOQL queries, massive loads, and integrations.
                """
        )
