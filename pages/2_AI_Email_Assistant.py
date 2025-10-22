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
# Load workflow data
# ------------------------------
def load_workflow_data():
    workflow_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "streamlit_app", "workflow_ai_email_assistant.json")
    if not os.path.exists(workflow_path):
        st.warning("⚠️ workflow_ai_email_assistant.json not found in streamlit_app/")
        return {"name": "AI Email Assistant", "nodes": [], "id": "N/A", "active": False, "versionId": "N/A"}
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        st.error(f"❌ Error parsing workflow JSON: {e}")
        return {"name": "AI Email Assistant", "nodes": [], "id": "N/A", "active": False, "versionId": "N/A"}

def extract_description(workflow_data):
    """Extract description from Sticky Note node"""
    for node in workflow_data.get('nodes', []):
        if node.get('type') == 'n8n-nodes-base.stickyNote' and 'content' in node.get('parameters', {}):
            return node['parameters']['content']
    return "No description provided."

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

    # Load workflow
    workflow_data = load_workflow_data()
    workflow_name = workflow_data.get('name', 'AI Email Assistant')
    description = extract_description(workflow_data)

    # Workflow card
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="workflow-title">{workflow_name}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI Email Automation")
        image_path = "ai_email_assistant.png"
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True, caption="AI Email Assistant - Gmail Auto-Response System")
        else:
            st.info("🖼️ Product image will appear here")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">📝 Workflow Overview</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="description-content">This {workflow_name} is an intelligent automation system that handles customer emails, transfers calls, and sends SMS messages automatically. Leveraging AI ensures 24/7 instant communication and smarter business operations. Never miss an important email again with intelligent categorization, priority detection, and context-aware responses.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<div class="description-title">🚀 Key Features</div>', unsafe_allow_html=True)
        st.markdown('''<div class="description-content">• AI-powered email analysis and categorization
• Intelligent auto-response generation
• Priority email detection and routing
• Multi-language support for global communication
• Sentiment analysis for customer satisfaction
• Automated follow-up scheduling
• Integration with CRM and ticketing systems
• Smart email threading and conversation tracking</div>''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Business Benefits")
    
    col_benefit1, col_benefit2, col_benefit3 = st.columns(3)
    
    with col_benefit1:
        st.markdown("""
        <div class="description-box">
            <h4>⚡ Instant Response</h4>
            <p>Respond to customer emails within seconds, not hours. Improve customer satisfaction with immediate acknowledgment and intelligent routing.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_benefit2:
        st.markdown("""
        <div class="description-box">
            <h4>💰 Cost Savings</h4>
            <p>Reduce support team workload by 60-80%. Automate routine inquiries and let your team focus on complex issues that require human touch.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_benefit3:
        st.markdown("""
        <div class="description-box">
            <h4>📈 Scalability</h4>
            <p>Handle unlimited email volume without additional staff. Scale your customer communication effortlessly as your business grows.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎯 Common Use Cases")
    
    use_cases = [
        ("Customer Support", "Automatically categorize and respond to common support inquiries, route complex issues to appropriate team members"),
        ("Sales Inquiries", "Qualify leads, schedule demos, and provide product information instantly to potential customers"),
        ("Order Status", "Provide real-time order updates, tracking information, and delivery notifications automatically"),
        ("Appointment Booking", "Schedule meetings, send confirmations, and manage calendar availability without manual intervention"),
        ("FAQ Responses", "Answer frequently asked questions instantly with accurate, context-aware information"),
        ("Follow-up Automation", "Send timely follow-ups based on customer interactions and engagement patterns")
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

    # Workflow statistics
    st.markdown("---")
    st.markdown("### 📊 Workflow Statistics")
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    col_stat1.metric("Total Nodes", len(workflow_data.get('nodes', [])))
    col_stat2.metric("Workflow ID", workflow_data.get('id', 'N/A')[:8] + "...")
    col_stat3.metric("Status", "Active" if workflow_data.get('active', False) else "Inactive")
    col_stat4.metric("Version", workflow_data.get('versionId', 'N/A')[:8] + "...")

    st.markdown("---")
    st.markdown("### 🛠️ Setup Instructions")
    st.markdown('<div class="description-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="description-content">{description}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Download section
    st.markdown("---")
    st.markdown('<div class="download-section">', unsafe_allow_html=True)
    st.markdown("### 📥 Download Workflow")
    st.markdown("Click the button below to download the complete workflow JSON file for n8n.", unsafe_allow_html=True)
    workflow_json = json.dumps(workflow_data, indent=2)
    st.download_button(
        label="⬇️ Download Workflow JSON",
        data=workflow_json,
        file_name=f"{workflow_name.replace(' ', '_')}.json",
        mime="application/json"
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
