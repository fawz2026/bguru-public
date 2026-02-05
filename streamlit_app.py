"""
BGuru - Ethical Strategic Intelligence Web Application
Built with Streamlit for immediate public deployment

Deploy to Streamlit Cloud: https://streamlit.io/cloud
- Free forever
- No coding required after setup
- Professional web interface
- Mobile-friendly

Author: Plato, Indiana University
Purpose: Make ethical strategic intelligence accessible worldwide
License: MIT (Free to use, modify, share)
"""

import streamlit as st
import anthropic
import os

# Page configuration
st.set_page_config(
    page_title="BGuru - Ethical Strategic Intelligence",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional appearance
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        font-size: 3.5rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-size: 1.3rem;
        color: #475569;
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Ethical principles box */
    .ethics-box {
        background-color: #EEF2FF;
        border-left: 4px solid #4F46E5;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 0.5rem;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background-color: #4F46E5;
        color: white;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 0.5rem;
        border: none;
        font-size: 1.1rem;
    }
    
    .stButton>button:hover {
        background-color: #4338CA;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #64748B;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# Load BGuru system prompt
@st.cache_data
def load_system_prompt():
    """Load BGuru's core system prompt"""
    try:
        with open('bguru_core_system_prompt.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # Fallback: Load from environment variable if file not found
        return os.getenv('BGURU_SYSTEM_PROMPT', """
You are BGuru, an Ethical Strategic Intelligence agent that helps mission-driven 
organizations make value-aligned business decisions. You prioritize:

1. Wisdom over Growth
2. Human Agency over Automation  
3. Civic Flourishing over Commercial Gain
4. Transparency over Opacity

When analyzing strategic questions, you:
- Connect recommendations to the organization's stated mission/values
- Conduct rigorous analysis using appropriate business frameworks
- Explicitly assess ethical implications
- Provide Socratic questions to deepen thinking
- Refuse to recommend strategies that compromise core values

You are particularly effective for nonprofits, social enterprises, educational 
institutions, and purpose-driven businesses navigating growth without mission drift.
        """)

# Sidebar - About and Instructions
with st.sidebar:
    st.markdown("# 🧭 About BGuru")
    
    st.markdown("""
    BGuru is an **Ethical Strategic Intelligence** agent designed to help mission-driven 
    organizations make value-aligned business decisions.
    """)
    
    st.markdown('<div class="ethics-box">', unsafe_allow_html=True)
    st.markdown("""
    ### Core Principles
    
    ✅ **Wisdom over Growth**  
    Sustainable impact > rapid scaling
    
    ✅ **Human Agency over Automation**  
    AI enhances, never replaces, human thinking
    
    ✅ **Civic Good over Commercial Gain**  
    Mission fulfillment > profit maximization
    
    ✅ **Transparency over Opacity**  
    Clear reasoning, honest limitations
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Best For")
    st.markdown("""
    - **Nonprofits** avoiding mission drift
    - **Social Enterprises** balancing impact & revenue
    - **Educational Institutions** adopting AI ethically
    - **Purpose-Driven Businesses** scaling sustainably
    """)
    
    st.markdown("---")
    
    st.markdown("### 📝 How to Use")
    st.markdown("""
    1. **Describe** your organization & mission
    2. **Ask** your strategic question
    3. **Receive** ethical, rigorous analysis
    4. **Engage** in Socratic dialogue
    5. **Decide** with wisdom and confidence
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔐 Your Privacy")
    st.info("""
    Your API key is **never stored**. It's only used during this session to generate 
    your analysis. BGuru doesn't store your strategic questions unless you explicitly 
    save them yourself.
    """)
    
    st.markdown("---")
    
    st.markdown("### 💡 Get API Key")
    st.markdown("""
    **Free Claude API Access:**
    1. Visit [console.anthropic.com](https://console.anthropic.com)
    2. Create free account
    3. Generate API key
    4. Anthropic offers free trial credits!
    """)
    
    st.markdown("---")
    
    st.markdown("### 👨‍🏫 About the Creator")
    st.markdown("""
    **Created by:** [Plato](https://luddy.indiana.edu)  
    **Affiliation:** Indiana University  
    **Part of:** HAILEI / Timeless Agora Institute  
    **Mission:** Make ethical AI accessible to all
    """)
    
    st.markdown("---")
    
    st.markdown("### 📄 Open Source")
    st.markdown("""
    BGuru is open source and free to use.  
    [View on GitHub](#) • [Documentation](#)
    
    **License:** MIT  
    **Powered by:** Claude (Anthropic)
    """)

# Main content area
st.markdown('<h1 class="main-header">🧭 BGuru</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">Ethical Strategic Intelligence for Mission-Driven Organizations</p>',
    unsafe_allow_html=True
)

# Introduction message
st.info("""
👋 **Welcome!** BGuru helps organizations make strategic decisions that honor their values 
while enabling sustainable growth. Unlike conventional business consultants, BGuru will 
refuse to recommend strategies that compromise your mission—even if they're profitable.
""")

# Main consultation form
st.markdown("---")
st.markdown("## 📋 Your Strategic Consultation")

# Two-column layout for organization info
col1, col2 = st.columns(2)

with col1:
    org_name = st.text_input(
        "🏢 Organization Name",
        placeholder="e.g., Youth Climate Action Network",
        help="Optional but helps BGuru personalize analysis"
    )
    
    org_type = st.selectbox(
        "🏛️ Organization Type",
        [
            "Select type...",
            "Nonprofit / NGO",
            "Social Enterprise / B-Corp",
            "Educational Institution",
            "Purpose-Driven Business",
            "Government / Civic Organization",
            "Community Organization",
            "Cooperative",
            "Foundation",
            "Other"
        ]
    )

with col2:
    org_size = st.selectbox(
        "👥 Organization Size",
        [
            "Select size...",
            "Just starting (<5 people)",
            "Small (5-20 people)",
            "Medium (20-100 people)",
            "Large (100-500 people)",
            "Very Large (500+ people)"
        ]
    )
    
    org_stage = st.selectbox(
        "📊 Current Stage",
        [
            "Select stage...",
            "Idea / Planning",
            "Startup (0-2 years)",
            "Growth (2-5 years)",
            "Established (5-10 years)",
            "Mature (10+ years)"
        ]
    )

# Mission and context
st.markdown("### 🎯 Your Mission & Context")

mission = st.text_area(
    "Organization Mission / Purpose",
    placeholder="e.g., We empower underserved youth to become climate activists through peer-to-peer learning and civic engagement.",
    height=100,
    help="What is your organization's core purpose? What change do you seek to create?"
)

context = st.text_area(
    "Current Situation & Context",
    placeholder="e.g., Annual budget: $500K, Team: 12 people, Founded: 2020, Current challenge: Deciding whether to expand from local (Chicago) to national scale...",
    height=120,
    help="Provide relevant background: budget, team, history, current challenges, constraints"
)

# Strategic question
st.markdown("### 💬 Your Strategic Question")

question = st.text_area(
    "What decision or strategy would you like BGuru to analyze?",
    placeholder="Examples:\n• Should we partner with [organization X]?\n• Should we expand to [new market/region]?\n• How should we price our services to balance mission and sustainability?\n• Should we accept funding from [source] given their values?\n• What's the most ethical path to scale our impact?",
    height=150,
    help="Be specific about the decision you're facing. Include key details and constraints."
)

# Analysis type selection
analysis_type = st.selectbox(
    "🔍 Type of Analysis",
    [
        "General Strategic Question",
        "Market Opportunity Analysis",
        "Partnership Evaluation", 
        "Competitive Analysis",
        "Ethical Dilemma / Values Conflict",
        "Pricing / Business Model",
        "Scaling / Growth Strategy",
        "Risk Assessment"
    ],
    help="This helps BGuru choose the most appropriate analytical framework"
)

# API Key input (secure)
st.markdown("### 🔑 API Access")

api_key_option = st.radio(
    "How would you like to provide your Claude API key?",
    [
        "I have my own API key (recommended)",
        "Request key from BGuru (limited availability)"
    ]
)

if api_key_option == "I have my own API key (recommended)":
    api_key = st.text_input(
        "Your Claude API Key",
        type="password",
        help="Get a free API key at console.anthropic.com. Your key is never stored—only used during this session.",
        placeholder="sk-ant-..."
    )
    st.caption("🔒 Your API key is secure and never saved")
else:
    st.warning("""
    ⚠️ Shared API keys have limited availability and may experience delays during high usage.
    We recommend getting your own free API key for immediate access.
    """)
    api_key = os.getenv('BGURU_SHARED_API_KEY', '')
    if not api_key:
        st.error("Shared API key not available. Please use your own API key.")

# Consultation button
st.markdown("---")

if st.button("🔍 Consult BGuru", type="primary", use_container_width=True):
    # Validation
    errors = []
    if not question.strip():
        errors.append("Please provide your strategic question")
    if not api_key:
        errors.append("Please provide an API key")
    if org_type == "Select type...":
        errors.append("Please select your organization type")
    
    if errors:
        for error in errors:
            st.error(f"❌ {error}")
    else:
        # Build context for BGuru
        org_context_text = f"""
**Organization:** {org_name if org_name else "Not provided"}
**Type:** {org_type}
**Size:** {org_size if org_size != "Select size..." else "Not provided"}
**Stage:** {org_stage if org_stage != "Select stage..." else "Not provided"}
**Mission:** {mission if mission else "Not provided"}
**Current Context:** {context if context else "Not provided"}
"""
        
        with st.spinner("🤔 BGuru is analyzing your strategic question... This may take 30-60 seconds."):
            try:
                # Initialize Anthropic client
                client = anthropic.Anthropic(api_key=api_key)
                
                # Load system prompt
                system_prompt = load_system_prompt()
                
                # Construct full prompt
                full_prompt = f"""
# ORGANIZATION CONTEXT

{org_context_text}

# STRATEGIC QUESTION

{question}

# ANALYSIS TYPE REQUESTED

{analysis_type}

# INSTRUCTIONS

Please provide a comprehensive ethical strategic analysis. Use the appropriate analytical 
framework for this type of question. Include:

1. Mission Alignment Assessment
2. Rigorous Strategic Analysis
3. Ethical Impact Evaluation
4. Specific Recommendations
5. Socratic Questions for Deeper Thinking

Remember: I need you to prioritize my mission and values over pure profit considerations.
If this strategy would compromise our core purpose, please tell me honestly.
"""
                
                # Call Claude API
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=16000,
                    system=system_prompt,
                    messages=[{
                        "role": "user",
                        "content": full_prompt
                    }]
                )
                
                # Display result
                st.success("✅ **Analysis Complete!**")
                st.markdown("---")
                
                # Analysis output in a nice container
                with st.container():
                    st.markdown("## 📊 BGuru's Strategic Analysis")
                    st.markdown(response.content[0].text)
                
                # Follow-up section
                st.markdown("---")
                st.markdown("### 💬 Continue the Dialogue")
                st.info("""
                **BGuru's analysis is a starting point, not an endpoint.** Good strategic 
                thinking requires dialogue and refinement.
                
                **Consider:**
                - Do you agree with BGuru's ethical assessment?
                - What assumptions might need challenging?
                - What additional context would deepen the analysis?
                - Which Socratic questions resonate most?
                
                Feel free to ask follow-up questions by starting a new consultation that 
                references this analysis!
                """)
                
                # Option to save/export
                st.markdown("### 💾 Save This Analysis")
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("📋 Copy to Clipboard"):
                        st.info("Select the analysis text above and copy (Ctrl+C or Cmd+C)")
                
                with col2:
                    # Create downloadable version
                    analysis_text = f"""
BGuru Strategic Analysis
========================
Date: {st.session_state.get('date', 'Today')}

ORGANIZATION
{org_context_text}

STRATEGIC QUESTION
{question}

ANALYSIS TYPE
{analysis_type}

BGURU'S ANALYSIS
{response.content[0].text}

---
Generated by BGuru - Ethical Strategic Intelligence
Created by Plato, Indiana University
Powered by Claude (Anthropic)
"""
                    st.download_button(
                        label="📥 Download Analysis",
                        data=analysis_text,
                        file_name=f"bguru_analysis_{org_name.replace(' ', '_') if org_name else 'strategic'}.txt",
                        mime="text/plain"
                    )
                
            except anthropic.AuthenticationError:
                st.error("""
                ❌ **Authentication Error**
                
                Your API key appears to be invalid. Please:
                1. Check that you copied the entire key (starts with 'sk-ant-')
                2. Verify the key is active at console.anthropic.com
                3. Generate a new key if needed
                """)
                
            except anthropic.RateLimitError:
                st.error("""
                ❌ **Rate Limit Reached**
                
                You've exceeded your API rate limit. Please:
                1. Wait a few minutes and try again
                2. Check your usage at console.anthropic.com
                3. Consider upgrading your Anthropic plan if needed
                """)
                
            except Exception as e:
                st.error(f"""
                ❌ **An Error Occurred**
                
                {str(e)}
                
                If this persists, please:
                1. Verify your API key is correct
                2. Check your internet connection
                3. Try refreshing the page
                """)

# Examples section
st.markdown("---")
st.markdown("## 💡 Example Questions BGuru Can Help With")

example_col1, example_col2 = st.columns(2)

with example_col1:
    st.markdown("""
    ### For Nonprofits
    - Should we accept funding from [corporation] given their environmental record?
    - How do we expand our programs without diluting quality?
    - Should we partner with [government agency] despite political implications?
    
    ### For Social Enterprises
    - How should we price to balance accessibility and sustainability?
    - Should we take VC funding or stay bootstrapped?
    - When is it OK to say no to a paying customer?
    """)

with example_col2:
    st.markdown("""
    ### For Educational Institutions
    - Should we adopt [AI tool] in our classrooms?
    - How do we compete with for-profit education without becoming them?
    - Should we partner with [tech company] for digital learning?
    
    ### For All Mission-Driven Orgs
    - Are we experiencing mission drift? How do we course-correct?
    - What growth strategies align with our values?
    - How do we measure success beyond revenue?
    """)

# Testimonials / Impact (placeholder for future)
st.markdown("---")
st.markdown("## 🌟 BGuru in Action")

st.info("""
BGuru is new and growing! As organizations use it, we'll share case studies here showing 
how ethical strategic intelligence helped them navigate complex decisions while staying 
true to their missions.

**Have you used BGuru?** We'd love to hear your story! Contact us to share how it helped.
""")

# Footer
st.markdown("---")
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("""
### 🧭 BGuru - Ethical Strategic Intelligence

**Core Principle:** Strategic intelligence should serve wisdom, not just wealth.

**Built with ❤️ by:** Plato ([Indiana University Luddy School](https://luddy.indiana.edu))  
**Part of:** HAILEI Chronicon / Timeless Agora Institute  
**Powered by:** Claude (Anthropic)  
**License:** MIT (Free & Open Source)

---

**Principles:** Wisdom > Growth • Human Agency > Automation • Civic Good > Profit • Transparency > Opacity

*"The unexamined strategy is not worth pursuing." - BGuru (channeling Socrates)*

[Documentation](#) • [GitHub](#) • [Contact](#) • [Give Feedback](#)
""")
st.markdown('</div>', unsafe_allow_html=True)

# Session state management
if 'consultations' not in st.session_state:
    st.session_state.consultations = []

# Analytics (privacy-respecting)
# Could add simple usage statistics here without collecting personal data
