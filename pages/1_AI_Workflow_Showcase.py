import streamlit as st
import json
import os

# Page configuration
st.set_page_config(
    page_title="AI Workflow Showcase",
    page_icon="⚙️",
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
    workflow_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workflow.json")
    if not os.path.exists(workflow_path):
        st.warning("⚠️ workflow.json not found in the parent directory.")
        return {"name": "Untitled Workflow", "nodes": [], "id": "N/A", "active": False, "versionId": "N/A"}
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        st.error(f"❌ Error parsing workflow.json: {e}")
        return {"name": "Untitled Workflow", "nodes": [], "id": "N/A", "active": False, "versionId": "N/A"}

def extract_description(workflow_data):
    """Extract description from Sticky Note node"""
    for node in workflow_data.get('nodes', []):
        if node.get('type') == 'n8n-nodes-base.stickyNote' and 'content' in node.get('parameters', {}):
            return node['parameters']['content']
    return "No description provided."

# Main app
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>⚙️ AI Workflow Showcase</h1>
        <p style="font-size: 1.2rem; margin-top: 0.5rem;">Discover Our Featured Automation Workflow</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load workflow
    workflow_data = load_workflow_data()
    workflow_name = workflow_data.get('name', 'Untitled Workflow')
    description = extract_description(workflow_data)
    
    # Workflow card
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    
    # Workflow title
    st.markdown(f'<div class="workflow-title">{workflow_name}</div>', unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Image section
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI Employee Automation")
        
        # Check if product image exists
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "streamlit_app", "product_image.webp")
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True, caption="AI-Powered Workflow Automation")
        else:
            st.info("🖼️ Product image will be displayed here")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Description 1: Overview
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">📝 Workflow Overview</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="description-content">This {workflow_name} is an advanced automation solution designed to streamline your business processes. Leveraging the power of AI and intelligent automation, this workflow connects multiple services to automate repetitive tasks, saving you time and reducing manual errors while improving overall efficiency.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Description 2: Setup Instructions
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">🚀 Setup Instructions</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="description-content">{description}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Workflow statistics
    st.markdown("---")
    st.markdown("### 📊 Workflow Statistics")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.metric("Total Nodes", len(workflow_data.get('nodes', [])))
    
    with col_stat2:
        st.metric("Workflow ID", workflow_data.get('id', 'N/A')[:8] + "...")
    
    with col_stat3:
        active_status = "Active" if workflow_data.get('active', False) else "Inactive"
        st.metric("Status", active_status)
    
    with col_stat4:
        st.metric("Version", workflow_data.get('versionId', 'N/A')[:8] + "...")
    
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
            use_column_width=True
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
