import streamlit as st
import json
import os

# Page configuration
st.set_page_config(
    page_title="Google Maps Local Leads",
    page_icon="🗺️",
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
    workflow_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workflow_google_maps_leads.json")
    if not os.path.exists(workflow_path):
        st.warning("⚠️ workflow_google_maps_leads.json not found.")
        return {"name": "Google Maps Local Leads", "nodes": [], "id": "N/A", "active": False, "versionId": "N/A"}
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        st.error(f"❌ Error parsing workflow JSON: {e}")
        return {"name": "Google Maps Local Leads", "nodes": [], "id": "N/A", "active": False, "versionId": "N/A"}

# Main app
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🗺️ Google Maps Local Leads</h1>
        <p style="font-size: 1.2rem; margin-top: 0.5rem;">Uncover Prospects, Grow Your Business 24/7</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load workflow
    workflow_data = load_workflow_data()
    workflow_name = workflow_data.get('name', 'Google Maps Local Leads')
    
    # Workflow card
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    
    # Workflow title
    st.markdown(f'<div class="workflow-title">{workflow_name}</div>', unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Image section
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.markdown("### 🗺️ Local Lead Generation")
        
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "streamlit_app", "google_maps_leads.png")
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True, caption="Google Maps Local Leads - Prospect Discovery System")
        else:
            st.info("🖼️ Product image will be displayed here")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Description 1: Overview
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">📝 Workflow Overview</div>', unsafe_allow_html=True)
        st.markdown(f'''<div class="description-content">The Google Maps Local Leads system is an intelligent automation platform that discovers and qualifies local business prospects using Google Maps data. Operating 24/7, this workflow automatically uncovers potential customers in your target area, extracts contact information, and helps you grow your business by connecting with local prospects at scale.</div>''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Description 2: Key Features
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">🚀 Key Features</div>', unsafe_allow_html=True)
        st.markdown(f'''<div class="description-content">• Automated Google Maps scraping
• Location-based lead discovery
• Business contact information extraction
• Industry and category filtering
• Lead qualification and scoring
• CRM integration and export
• Duplicate detection and removal
• Real-time data enrichment</div>''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Benefits section
    st.markdown("---")
    st.markdown("### 💡 Business Benefits")
    
    col_benefit1, col_benefit2, col_benefit3 = st.columns(3)
    
    with col_benefit1:
        st.markdown("""
        <div class="description-box">
            <h4>🎯 Targeted Prospecting</h4>
            <p>Find businesses in specific locations, industries, and categories. Build highly targeted prospect lists for maximum conversion rates.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_benefit2:
        st.markdown("""
        <div class="description-box">
            <h4>⚡ Speed & Scale</h4>
            <p>Generate thousands of qualified leads in hours, not weeks. Automate what used to take entire sales teams days to accomplish.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_benefit3:
        st.markdown("""
        <div class="description-box">
            <h4>📈 Higher ROI</h4>
            <p>Focus on local businesses ready to buy. Geographic targeting ensures your outreach reaches the most relevant prospects.</p>
        </div>
        """, unsafe_allow_html=True)

    # Use Cases section
    st.markdown("---")
    st.markdown("### 🎯 Ideal For")
    
    use_cases = [
        ("B2B Sales Teams", "Find local businesses needing your services, build targeted prospect lists, identify decision makers"),
        ("Marketing Agencies", "Discover businesses without websites, identify poor online presence, offer digital marketing services"),
        ("Software Companies", "Target businesses by industry, find companies using competitor tools, identify technology gaps"),
        ("Service Providers", "Locate businesses in service area, identify maintenance needs, build recurring service contracts"),
        ("Wholesale Suppliers", "Find retail businesses, identify purchasing managers, build distribution networks"),
        ("Franchise Development", "Identify potential franchise locations, analyze market density, competitive intelligence")
    ]
    
    for i in range(0, len(use_cases), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(use_cases):
                title, desc = use_cases[i + j]
                with col:
                    st.markdown(f"""
                    <div class="description-box">
                        <div class="description-title">✓ {title}</div>
                        <div class="description-content">{desc}</div>
                    </div>
                    """, unsafe_allow_html=True)

    # Data Points section
    st.markdown("---")
    st.markdown("### 📋 Extracted Data Points")
    
    st.markdown("""
    <div class="description-box">
        <div class="description-content">
        <strong>Business Information:</strong> Name, address, phone number, website, email, business hours, rating, review count<br><br>
        <strong>Location Data:</strong> GPS coordinates, neighborhood, city, state, zip code, service area<br><br>
        <strong>Business Details:</strong> Category, industry, services offered, price range, years in business<br><br>
        <strong>Engagement Metrics:</strong> Response rate, popular times, customer photos, Q&A activity<br><br>
        <strong>Competitive Intel:</strong> Nearby competitors, market density, rating comparison, service gaps
        </div>
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
