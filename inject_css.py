#!/usr/bin/env python3
"""
Script to inject custom CSS into nbconvert-generated HTML slides.
Run this after: jupyter nbconvert --to slides NLP_Lecture.ipynb
"""

import re
import sys

css_content = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

body .reveal,
html .reveal {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
  background-color: #f0f4f8 !important;
  background: #f0f4f8 !important;
}

body .reveal .slides,
html .reveal .slides {
  background-color: #f0f4f8 !important;
  background: #f0f4f8 !important;
}

body .reveal .slides section,
html .reveal .slides section {
  background-color: #f5f8fa !important;
  background: #f5f8fa !important;
  color: #333333 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
}

body .reveal h1, body .reveal h2, body .reveal h3, body .reveal h4, body .reveal h5, body .reveal h6,
html .reveal h1, html .reveal h2, html .reveal h3, html .reveal h4, html .reveal h5, html .reveal h6 {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
  font-weight: 600 !important;
  color: #1a1a1a !important;
}

body .reveal p, body .reveal li, body .reveal td, body .reveal th,
html .reveal p, html .reveal li, html .reveal td, html .reveal th {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
  color: #333333 !important;
}

body .reveal pre, body .reveal code,
html .reveal pre, html .reveal code {
  font-family: 'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace !important;
  background-color: #ffffff !important;
}

body .reveal table,
html .reveal table {
  background-color: #ffffff !important;
  border-collapse: collapse;
}

body .reveal table th,
html .reveal table th {
  background-color: #e3f2fd !important;
  color: #1a1a1a !important;
}

body .reveal table td,
html .reveal table td {
  background-color: #ffffff !important;
}

body .reveal a,
html .reveal a {
  color: #1976d2 !important;
}

body .reveal a:hover,
html .reveal a:hover {
  color: #1565c0 !important;
}
</style>"""

def inject_css(html_file):
    """Inject CSS into the HTML file."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {html_file} not found")
        return False
    
    # Remove any existing custom CSS first
    content = re.sub(r'<style>.*?@import url.*?Inter.*?</style>', '', content, flags=re.DOTALL)
    
    # Find the </head> tag and insert CSS before it
    if '</head>' in content:
        content = content.replace('</head>', css_content + '\n</head>')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ CSS injected into {html_file}")
        return True
    else:
        print(f"Error: Could not find </head> tag in {html_file}")
        return False

if __name__ == '__main__':
    html_file = sys.argv[1] if len(sys.argv) > 1 else 'NLP_Lecture.slides.html'
    inject_css(html_file)

