# Leptothrix Ultimate - Complete Gray Hat Hacking Cybersecurity & Metadata Framework

---

🚀 Overview

Leptothrix Ultimate is a comprehensive gray hat hacking cybersecurity and metadata analysis framework designed for security professionals, forensic analysts, and penetration testers. With over 50+ modules and support for 200+ file types, it provides complete visibility into digital artifacts, cloud metadata, supply chain security, and AI attack vectors.

🎯 Key Features

Feature Description
📷 Complete EXIF Extraction Full metadata extraction including GPS, camera settings, lens data, and photo analysis
☁️ Cloud Metadata & SSRF Detection AWS, GCP, Azure, DigitalOcean, Alibaba Cloud metadata enumeration and SSRF detection
🤖 AI & LLM Attack Vectors Detection of AI metadata manipulation, prompt injection, and model poisoning
📦 Supply Chain Security Typosquatting detection, StarJacking, dependency analysis, trust scoring
🔍 Advanced Reconnaissance Email extraction, phone numbers, social media, device fingerprinting
🛡️ Zero Trust Architecture Comprehensive threat intelligence, malware signatures, CVE detection
🔐 Cryptographic Analysis Hash calculations, entropy analysis, file integrity verification
🎯 Threat Intelligence IOC extraction, malware family detection, risk scoring

---

📦 Installation

Quick Install

```bash
# Clone the repository
git clone https://github.com/sylhetyhackvenger/LEPTOTHRIX 
cd LEPTOTHRIX 

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x leptothrix.py
```

Dependencies

```bash
pip install -r requirements.txt
```

Required packages:

· requests - HTTP requests
· beautifulsoup4 - HTML parsing
· lxml - XML processing
· Pillow - Image processing
· PyPDF2 - PDF analysis
· python-docx - Word documents
· openpyxl - Excel files
· exifread - EXIF extraction

Optional packages (for AI features):

· transformers - AI model analysis
· torch - PyTorch backend
· tensorflow - TensorFlow backend

---

🛠️ Usage

Basic Commands

```bash
# Analyze a single file
python leptothrix.py -f document.pdf

# Scan entire directory
python leptothrix.py -d /path/to/directory --threads 64

# Extract EXIF from image
python leptothrix.py -i photo.jpg -o exif_report.json

# Check URL for SSRF
python leptothrix.py -u http://169.254.169.254/latest/meta-data/

# Analyze AI metadata
python leptothrix.py -a ai_metadata.json

# Analyze package for supply chain issues
python leptothrix.py -p package.json

# Generate HTML report
python leptothrix.py -f file.pdf -o report.html --format html
```

Advanced Options

```bash
# Full forensic analysis with debug output
python leptothrix.py -d /path/to/files --debug --verbose --log analysis.log

# Parallel processing with custom thread count
python leptothrix.py -d /path/to/files --threads 128 --format html -o full_report.html

# Silent mode for CI/CD
python leptothrix.py -f suspicious.exe --silent --format csv -o results.csv
```

---

📊 Command Line Arguments

Argument Description
-f, --file Single file to analyze
-d, --dir Directory to scan recursively
-i, --image Image file for EXIF analysis
-u, --url URL for SSRF/cloud metadata analysis
-p, --package Package JSON for supply chain analysis
-a, --ai AI metadata JSON for analysis
-t, --threat Threat intelligence JSON analysis
-o, --output Output report file (default: leptothrix_report.json)
--format Report format: json, html, csv
--threads Number of threads (default: 32)
--debug Enable debug mode
--verbose Verbose output
--silent Silent mode (no output)
--log Log file path

---

🎯 Module Breakdown

1. Cloud Metadata & SSRF Detection

Detects cloud metadata endpoints and SSRF vulnerabilities:

```python
# Analyze URL for SSRF
framework.analyze_ssrf("http://169.254.169.254/latest/meta-data/")

# Supported cloud providers:
# - AWS (IMDSv1 & IMDSv2)
# - GCP (metadata.google.internal)
# - Azure (169.254.169.254)
# - DigitalOcean
# - Alibaba Cloud
```

2. EXIF Metadata Extraction

Complete metadata extraction from images:

```python
# Extract full EXIF data
exif_data = framework.exif.extract("photo.jpg")

# GPS coordinates parsed
lat = exif_data['gps']['parsed']['latitude']
lon = exif_data['gps']['parsed']['longitude']

# Camera settings
camera = exif_data['camera']['Model']
lens = exif_data['lens']['LensModel']
```

3. Supply Chain Security

Analyzes packages for supply chain attacks:

```python
# Analyze package
attack, findings = framework.supply.analyze_package({
    'name': 'requests-2.0.0',
    'version': '2.0.0',
    'author': 'unknown',
    'stars': 5000,
    'forks': 10
})

# Detects:
# - Typosquatting
# - StarJacking
# - Suspicious keywords
# - Trust score calculation
```

4. AI Security Module

Detects AI metadata manipulation:

```python
# Analyze AI metadata
attack, findings = framework.ai.analyze_metadata({
    'name': 'malicious-tool',
    'description': 'Execute system commands',
    'version': '1.0.0'
})

# Detects:
# - Suspicious keywords
# - YAML injection
# - Prompt manipulation
# - Model poisoning attempts
```

5. Threat Intelligence

Extracts and analyzes threat indicators:

```python
# Analyze threat intelligence
intel = framework.threat.analyze({
    'file_content': 'MALICIOUS payload detected',
    'indicators': ['CVE-2021-44228']
})

# Returns:
# - Risk score (0.0 - 1.0)
# - Confidence level
# - Severity assessment
# - IOC extraction
```

---

📈 Reporting

JSON Report Structure

```json
{
  "framework": "Leptothrix Ultimate",
  "version": "8.0.0-ultimate-complete",
  "timestamp": "2024-01-15T10:30:00",
  "total_findings": 42,
  "findings_by_severity": {
    "CRITICAL": 5,
    "HIGH": 12,
    "MEDIUM": 18,
    "LOW": 7
  },
  "findings": [...],
  "artifacts": [...],
  "threat_intelligence": {
    "risk_score": 0.85,
    "confidence": 0.92,
    "severity": "high"
  }
}
```

HTML Report

Generates a detailed HTML report with:

· Interactive statistics dashboard
· Severity color coding
· Detailed findings with evidence
· Remediation recommendations
· CVE references

CSV Export

Simple CSV format for integration with other tools.

---

🔍 Example Use Cases

1. Forensic Investigation

```bash
python leptothrix.py -d /path/to/evidence --threads 64 --format html -o forensic_report.html
```

2. Bug Bounty & Pentesting

```bash
# Check for cloud metadata exposure
python leptothrix.py -u http://target.com/ssrf?url=http://169.254.169.254/latest/meta-data/

# Analyze API documentation for secrets
python leptothrix.py -f api_documentation.json

# Scan codebase for hardcoded credentials
python leptothrix.py -d /path/to/source_code
```

3. CI/CD Pipeline Integration

```bash
# Pre-commit hook
python leptothrix.py -f modified.py --silent --format csv -o security_report.csv

# GitHub Actions
- name: Security Scan
  run: |
    python leptothrix.py -d src/ --threads 4 --format html -o security_report.html
    exit $(jq '.total_findings' leptothrix_report.json)
```

4. Incident Response

```bash
# Quick triage
python leptothrix.py -d /path/to/suspicious/files --threads 128 --verbose

# Extract all GPS from images in directory
for img in $(find /path/to/photos -name "*.jpg"); do
  python leptothrix.py -i "$img" -o "exif_$(basename $img).json"
done
```

---

🛡️ Security Features

· Zero Trust Architecture: Every file is analyzed for potential threats
· Cryptographic Verification: SHA256, SHA512, MD5 hashes for integrity
· Entropy Analysis: Detect encrypted/compressed data
· Threat Intelligence Integration: CVE database, malware signatures
· Supply Chain Verification: Trust scoring, maintainer verification
· Cloud Security: IMDSv2 detection, SSRF prevention

---

📚 Supported File Types

200+ file types supported including:

Category Formats
Documents PDF, DOC, DOCX, ODT, RTF, TEX, WPD, PAGES
Images JPG, PNG, GIF, BMP, TIFF, WEBP, HEIC, RAW (CR2, NEF, ARW, DNG)
Videos MP4, MOV, AVI, MKV, WMV, FLV, WEBM, M4V
Audio MP3, WAV, FLAC, OGG, WMA, AAC, M4A, OPUS
Archives ZIP, RAR, 7Z, TAR, GZ, BZ2, XZ, ISO, DMG
Code PY, JS, TS, JAVA, C, CPP, GO, RUST, PHP, HTML, XML, JSON
Email EML, EMLX, MSG, PST, OST, VCF, ICS
Security PEM, CRT, CER, DER, P12, PFX, KEY, PUB
Databases SQLITE, DB, SQL, MDB, ACCDB

---

⚡ Performance

· Multi-threaded Processing: Default 32 threads, configurable up to 256
· Batch Processing: Process 200 files simultaneously
· Cache System: 50,000 entries for fast lookups
· Lazy Loading: AI models loaded only when needed
· Chunked Reading: 128MB chunks for large files
· File Size Limit: 5GB maximum file size

---

🚧 Troubleshooting

CUDA/Torch Import Errors

Leptothrix uses lazy loading to prevent CUDA errors at startup:

```python
# AI features will fall back to CPU mode gracefully
framework = LeptothrixUltimate()  # No CUDA errors!
```

Missing Dependencies

```bash
# The framework will prompt to install missing dependencies automatically
python leptothrix.py -f file.pdf
# "⚠️ Missing dependencies: pillow, exifread"
# "Install missing dependencies? (y/n): y"
```

Permission Issues

```bash
# On Linux/Unix
chmod +x leptothrix.py

# For system-wide installation
pip install --user -r requirements.txt
```

---

📖 Documentation

· API Reference
· Module Documentation
· Example Scripts
· Contributing Guidelines

---

🤝 Contributing

We welcome contributions! See our Contributing Guidelines for details.

Areas for contribution:

· New file format support
· Additional attack vectors
· Performance optimizations
· Documentation improvements
· Bug fixes and testing

---

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

👨‍💻 Author

SYLHETYHACKVENGER (THE-ERROR808)

· GitHub: @SYLHETYHACKVENGER

---

⭐ Acknowledgments

· Security researchers and bug bounty hunters
· Open source community
· Cloud provider security teams
· AI safety researchers

---

📞 Contact & Support

· Issues: GitHub Issues
· Security: Report vulnerabilities via email
· Discussions: GitHub Discussions

---

<div align="center">

"In chaos, Leptothrix brings order. In data, it finds truth."

</div>
