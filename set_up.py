import os

def create_project_structure(base_dir="medical_incident_report"):
    # Define folder structure
    folders = [
        base_dir,
        f"{base_dir}/env",
        f"{base_dir}/app",
        f"{base_dir}/app/assets",
        f"{base_dir}/data",
        f"{base_dir}/tests",
    ]
    files = {
        f"{base_dir}/requirements.txt": "# Add your dependencies here\n",
        f"{base_dir}/README.md": "# Medical Incident Report\n\n## Description\nA Streamlit app for reporting medical incidents.\n",
        f"{base_dir}/.gitignore": "env/\ndata/medical_incidents.csv\n__pycache__/\n*.pyc\n",
        f"{base_dir}/LICENSE": "MIT License\n\nCopyright (c) 2025",
        f"{base_dir}/app/incident_form.py": "# Main Streamlit app\n\nimport streamlit as st\n\nst.title('Medical Incident Report')\n",
        f"{base_dir}/app/utils.py": "# Utility functions\n\n",
        f"{base_dir}/tests/test_incident_form.py": "# Tests for the incident form\n\nimport unittest\n\nclass TestIncidentForm(unittest.TestCase):\n    def test_placeholder(self):\n        self.assertTrue(True)\n\nif __name__ == '__main__':\n    unittest.main()\n",
    }
    
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Create files
    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    
    print(f"Project structure created at: {os.path.abspath(base_dir)}")

# Run the function to create the structure
create_project_structure()
