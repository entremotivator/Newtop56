import streamlit as st
import json
import os

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Custom CSS
# ------------------------------
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


# ------------------------------
# Load Workflow Data
# ------------------------------
def load_workflow_data():
    """
    Loads workflow JSON from streamlit_app/workflow_ai_email_assistant.json.
    Returns default placeholder if missing or invalid.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    workflow_path = os.path.join(base_path, "streamlit_app", "workflow_ai_email_assistant.json")

    if not os.path.exists(workflow_path):
        st.warning("⚠️ streamlit_app/workflow_ai_email_assistant.json not found.")
        return {
            "name": "AI Email Assistant",
            "nodes": [],
            "id": "N/A",
            "active": False,
            "versionId": "N/A"
        }

    try:
        with open(workflow_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        st.error(f"❌ Error parsing workflow JSON: {e}")
        return {
            "name": "AI Email Assistant",
            "nodes": [],
            "id": "N/A",
            "active": False,
            "versionId": "N/A"
        }


# ------------------------------
# Main App
# ------------------------------
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📧 AI Email Assistant</h1>
        <p style="font-size: 1.2rem; margin-top: 0.5rem;">Gmail Auto-Response System 24/7</p>
    </div>
    """, unsafe_allow_html=True)

    # Load workflow JSON
    workflow_data = load_workflow_data()
    workflow_name = workflow_data.get("name", "AI Email Assistant")

    # Workflow card
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="workflow-title">{workflow_name}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # ------------------------------
    # Left Column (Image)
    # ------------------------------
    with col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.markdown("### 📧 AI Email Automation")

        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "streamlit_app", "ai_email_assistant.png")
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True, caption="AI Email Assistant - Gmail Auto-Response System")
        else:
            st.info("🖼️ Product image (streamlit_app/ai_email_assistant.png) will appear here")

        st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------
    # Right Column (Descriptions)
    # ------------------------------
    with col2:
        # Overview
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">📝 Workflow Overview</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="description-content">
        The **AI Email Assistant** is an intelligent automation system that manages customer emails,
        transfers calls, and sends SMS messages automatically. This 24/7 AI-powered assistant ensures
        instant communication, smarter workflows, and personalized engagement across all channels.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Key Features
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">🚀 Key Features</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="description-content">
        • Automated AI email responses  
        • Smart classification & routing  
        • Gmail integration for seamless workflow  
        • 24/7 customer communication  
        • Custom response templates  
        • Multi-channel (Email, SMS, Calls)  
        • Real-time notifications  
        • Analytics and performance reports  
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------
    # Workflow Stats
    # ------------------------------
    st.markdown("---")
    st.markdown("### 📊 Workflow Statistics")

    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    with col_stat1:
        st.metric("Total Nodes", len(workflow_data.get("nodes", [])))
    with col_stat2:
        st.metric("Workflow ID", workflow_data.get("id", "N/A")[:20] + "...")
    with col_stat3:
        st.metric("Status", "Active" if workflow_data.get("active", False) else "Inactive")
    with col_stat4:
        st.metric("Version", workflow_data.get("versionId", "N/A")[:20])

    # ------------------------------
    # Download JSON
    # ------------------------------
    st.markdown("---")
    st.markdown('<div class="download-section">', unsafe_allow_html=True)
    st.markdown("### 📥 Download Workflow")
    st.markdown("Click below to download your workflow JSON file for import into n8n.", unsafe_allow_html=True)

    workflow_json = json.dumps(workflow_data, indent=2)
    st.download_button(
        label="⬇️ Download Workflow JSON",
        data=workflow_json,
        file_name=f"{workflow_name.replace(' ', '_')}.json",
        mime="application/json"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------
    # Footer
    # ------------------------------
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 1rem;">
        <p>Built with ❤️ using Streamlit | Powered by n8n Workflow Automation</p>
    </div>
    """, unsafe_allow_html=True)


# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    main()
