import streamlit as st
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="AI Employee Showcase",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Locate the image properly ---
# Build path relative to current file directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(CURRENT_DIR, "streamlit_app", "Image123.png")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 3rem;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        opacity: 0.95;
    }
    .hero-image {
        display: block;
        margin: 2rem auto;
        border-radius: 20px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        width: 60%;
    }
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .feature-title {
        color: #2c3e50;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .feature-description {
        color: #6c757d;
        line-height: 1.6;
    }
    .cta-section {
        text-align: center;
        padding: 3rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin: 3rem 0;
        color: white;
    }
    .cta-button {
        background: white;
        color: #667eea;
        padding: 1rem 3rem;
        border-radius: 30px;
        font-size: 1.2rem;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header section
    st.markdown("""
    <div class="main-header">
        <div class="hero-title">🤖 AI Employee Showcase</div>
        <div class="hero-subtitle">Revolutionize Your Business with Intelligent Automation</div>
    </div>
    """, unsafe_allow_html=True)

    # Display image correctly
    if os.path.exists(IMAGE_PATH):
        image = Image.open(IMAGE_PATH)
        st.image(image, caption="AI-Powered Automation", use_column_width=True)
    else:
        st.error(f"⚠️ Image not found at: {IMAGE_PATH}")

    # Intro
    st.markdown("""
    Welcome to the **AI Employee Showcase** — your gateway to discovering powerful automation workflows 
    that transform how businesses operate. Our AI-powered solutions help you automate repetitive tasks, 
    improve efficiency, and scale your operations effortlessly.
    """)
    
    st.markdown("---")
    st.markdown("## 🌟 What We Offer")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Smart Automation</div>
            <div class="feature-description">
                Automate complex workflows with AI-powered intelligence that learns and adapts to your business needs.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔗</div>
            <div class="feature-title">Seamless Integration</div>
            <div class="feature-description">
                Connect with your favorite tools and services including Gmail, Google Sheets, and AI models like Gemini.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Data-Driven Insights</div>
            <div class="feature-description">
                Make informed decisions with real-time analytics and comprehensive workflow monitoring.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 💼 Use Cases")
    
    col_use1, col_use2 = st.columns(2)
    with col_use1:
        st.markdown("""
        ### 📧 Automated Outreach
        Streamline your sales and marketing efforts with personalized, AI-generated outreach campaigns 
        that engage prospects and drive conversions.
        """)
        
        st.markdown("""
        ### 📋 Lead Management
        Automatically capture, qualify, and nurture leads through intelligent workflows that save time 
        and improve conversion rates.
        """)
    with col_use2:
        st.markdown("""
        ### 🤝 Customer Engagement
        Deliver exceptional customer experiences with automated responses, follow-ups, and personalized 
        communication at scale.
        """)
        
        st.markdown("""
        ### 📈 Business Intelligence
        Transform raw data into actionable insights with automated reporting and analytics workflows.
        """)
    
    st.markdown("---")
    st.markdown("""
    <div class="cta-section">
        <h2>Ready to Transform Your Business?</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">
            Explore our AI-powered workflows and discover how automation can revolutionize your operations.
        </p>
        <p style="font-size: 1.1rem; margin-top: 2rem;">
            👈 Navigate to the workflow pages in the sidebar to view our featured automation workflows!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 2rem;">
        <p style="font-size: 0.9rem;">
            Built with ❤️ using Streamlit | Powered by n8n Workflow Automation
        </p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">
            © 2025 AI Employee Showcase. All rights reserved.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
