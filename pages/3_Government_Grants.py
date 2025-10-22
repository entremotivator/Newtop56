import streamlit as st
import json
import os

# Page configuration
st.set_page_config(
    page_title="Government Grants Finder",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .workflow-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .workflow-title {
        color: #2c3e50;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .description-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .description-title {
        color: #667eea;
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .description-content {
        color: #495057;
        line-height: 1.8;
        white-space: pre-line;
    }
    .image-container {
        text-align: center;
        padding: 2rem;
        background: #f8f9fa;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .download-section {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin: 2rem 0;
    }
    .stDownloadButton button {
        background-color: white !important;
        color: #667eea !important;
        font-weight: bold !important;
        padding: 0.75rem 2rem !important;
        border-radius: 25px !important;
        border: 2px solid white !important;
        font-size: 1.1rem !important;
    }
    .stDownloadButton button:hover {
        background-color: #f8f9fa !important;
        transform: scale(1.05);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Load workflow data
def load_workflow_data():
    workflow_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workflow_government_grants.json")
    with open(workflow_path, 'r') as f:
        return json.load(f)

# Main app
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>💰 Government Grants Finder</h1>
        <p style="font-size: 1.2rem; margin-top: 0.5rem;">Grant Finder 24/7 - Instant Access, Secure Your Future</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load workflow
    workflow_data = load_workflow_data()
    workflow_name = workflow_data.get('name', 'Government Grants Finder')
    
    # Workflow card
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    
    # Workflow title
    st.markdown(f'<div class="workflow-title">{workflow_name}</div>', unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Image section
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.markdown("### 💰 Grant Discovery Automation")
        
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "streamlit_app", "government_grants.png")
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True, caption="Government Grants - Grant Finder System")
        else:
            st.info("🖼️ Product image will be displayed here")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Description 1: Overview
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">📝 Workflow Overview</div>', unsafe_allow_html=True)
        st.markdown(f'''<div class="description-content">The Government Grants Finder is an automated system that continuously searches for and identifies relevant government grants and funding opportunities. Operating 24/7, this workflow provides instant access to grant information, helping businesses and organizations secure their financial future through automated grant discovery and notification.</div>''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Description 2: Key Features
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">🚀 Key Features</div>', unsafe_allow_html=True)
        st.markdown(f'''<div class="description-content">• Automated grant opportunity discovery
• Real-time monitoring of government databases
• Intelligent matching based on eligibility criteria
• Instant notifications for new grants
• Deadline tracking and reminders
• Application status monitoring
• Comprehensive grant database
• Customizable search filters and alerts</div>''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Business Benefits section
    st.markdown("---")
    st.markdown("### 💡 Business Benefits")
    
    col_benefit1, col_benefit2, col_benefit3 = st.columns(3)
    
    with col_benefit1:
        st.markdown("""
        <div class="description-box">
            <h4>💰 Funding Access</h4>
            <p>Never miss a grant opportunity. Get instant alerts for new funding programs that match your business profile and eligibility criteria.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_benefit2:
        st.markdown("""
        <div class="description-box">
            <h4>⏰ Time Savings</h4>
            <p>Save hundreds of hours manually searching grant databases. Automated monitoring ensures you're always aware of relevant opportunities.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_benefit3:
        st.markdown("""
        <div class="description-box">
            <h4>🎯 Smart Matching</h4>
            <p>AI-powered eligibility matching ensures you only see grants you qualify for, increasing your success rate and reducing wasted effort.</p>
        </div>
        """, unsafe_allow_html=True)

    # Grant Categories section
    st.markdown("---")
    st.markdown("### 🏆 Grant Categories Covered")
    
    grant_categories = [
        ("Small Business Grants", "SBA loans, innovation grants, minority-owned business funding, startup capital programs"),
        ("Research & Development", "R&D tax credits, innovation funding, technology development grants, patent assistance"),
        ("Green Energy", "Renewable energy incentives, sustainability grants, carbon reduction programs, clean tech funding"),
        ("Education & Training", "Workforce development, employee training programs, educational institution grants"),
        ("Healthcare", "Medical research funding, healthcare facility grants, public health initiatives"),
        ("Agriculture", "Farm subsidies, agricultural innovation, rural development, sustainable farming grants")
    ]
    
    for i in range(0, len(grant_categories), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(grant_categories):
                title, desc = grant_categories[i + j]
                with col:
                    st.markdown(f"""
                    <div class="description-box">
                        <div class="description-title">✓ {title}</div>
                        <div class="description-content">{desc}</div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Workflow statistics
    st.markdown("---")
    st.markdown("### 📊 Workflow Statistics")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.metric("Total Nodes", len(workflow_data.get('nodes', [])))
    
    with col_stat2:
        st.metric("Workflow ID", workflow_data.get('id', 'N/A')[:20] + "...")
    
    with col_stat3:
        active_status = "Active" if workflow_data.get('active', False) else "Inactive"
        st.metric("Status", active_status)
    
    with col_stat4:
        st.metric("Version", workflow_data.get('versionId', 'N/A')[:20])
    
    # Download section
    st.markdown("---")
    st.markdown('<div class="download-section">', unsafe_allow_html=True)
    st.markdown("### 📥 Download Workflow")
    st.markdown("Click the button below to download the complete workflow JSON file and import it into your n8n instance", unsafe_allow_html=True)
    
    # Create download button
    workflow_json = json.dumps(workflow_data, indent=2)
    
    col_download1, col_download2, col_download3 = st.columns([1, 2, 1])
    with col_download2:
        st.download_button(
            label="⬇️ Download Workflow JSON",
            data=workflow_json,
            file_name=f"{workflow_name.replace(' ', '_')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 1rem;">
        <p>Built with ❤️ using Streamlit | Powered by n8n Workflow Automation</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
