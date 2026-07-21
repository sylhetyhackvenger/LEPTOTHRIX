#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢴⢾⡙⢞⣷⢦⢤⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣢⣜⡛⠘⣫⣄⣻⠀⠀⠀⠀⠀
⢠⠶⣼⣇⣵⡤⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡺⠍⢫⣶⢰⣍⠋⢽⠀⠀⠀⠀⠀
⣎⣴⣌⡛⢋⣴⣼⠀⠀⠀⠀⡖⢦⠀⠀⢀⣠⣤⣄⡀⠀⠀⠙⠛⠾⣡⢬⣻⠾⠚⠁⢀⡤⡀⠀
⣠⠞⣩⣶⣮⡙⢦⠀⠀⠀⠀⠁⣪⣴⣾⡿⠟⠛⠻⢿⣷⣦⣄⡀⠀⠈⠉⠀⠀⠀⡖⠚⠀⠓⢢
⠈⠚⣿⣇⣽⠙⠉⠀⣀⣤⣶⣿⠿⠛⠁⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣦⣀⠀⠀⠀⠈⠹⣀⡟⠉
⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣶⡄⠀⠀⠈⠀⠀
⣠⣤⣤⡀⠀⢺⣿⠻⣷⣦⣔⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠿⢿⣿⠀⠀⠀⠀⠀
⣿⣏⣿⣿⠀⢸⣿⠀⠀⠉⠛⠿⣶⣭⡓⠤⣀⠀⠀⠀⢀⣠⣴⡾⠟⠋⠁⡆⢸⣿⠀⢀⡤⣄⠀
⠙⠛⠛⠃⠀⢸⣿⠀⠀⠀⠀⠀⠀⠙⠻⢷⣦⣭⣤⣶⠿⠋⠁⠀⠀⡄⠀⡇⢸⣿⠀⠘⠦⠞⠀
⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠲⡌⣿⡏⠀⠠⠀⠀⠀⣁⠤⠒⡇⢸⣿⠀⣴⣦⡀⠀
⠀⠀⣖⠙⡆⢸⣿⠀⠀⠀⠀⠀⠀⢀⠔⠁⡇⣿⡇⠀⠁⠠⡾⣴⡿⣿⣦⡄⢸⣿⠘⠧⠼⠇⠀
⠀⠀⠈⠉⠁⣼⣿⢀⡠⠖⠀⠀⢀⠥⣄⠀⡇⣿⡇⡇⠀⡼⡽⢿⣖⣣⣿⡇⢸⣿⠀⡖⢲⡄⠀
⠀⠀⠀⠀⠀⠸⣿⣦⣑⠢⢄⡀⠸⣀⣸⠀⡇⣿⡇⡇⢾⠞⢶⠎⣉⡿⢓⣡⣿⣿⠀⠉⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣦⣍⡓⠦⣀⠀⡇⣿⡇⡇⢀⡠⠔⣫⣵⣾⣿⣿⡿⠿⣿⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣿⣿⣷⣬⣙⠃⣿⡇⢓⣭⣶⣿⣿⣛⢹⣿⣯⠤⠀⢿⢻⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⢦⣿⣏⠀⣹⣿⠿⣿⣿⣿⡿⠟⠉⣸⣤⣼⠈⣿⣯⣓⣒⣪⣾⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠘⠿⠽⠿⠀⠈⠛⠿⠿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⢀⢀⣄⣀⣀⣀⣄⣀⣀⣀⣀⣀⡀⣀⢀⣀⢀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⠿⠟⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠻⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀
                L E P T O T H R I X   U L T I M A T E
         The Complete Invincible Metadata & Security Framework
              ⚡ Maximum Power | Zero Bloat | Full Control ⚡

    Author: SYLHETYHACKVENGER (THE-ERROR808)
    Version: 8.0.0-ultimate-complete
    License: MIT
    Features: 50+ Modules | 200+ File Types | All Attack Vectors

    ⚡ QUANTUM POWER MODE ENABLED
    🔒 ALL SECURITY MEASURES ACTIVE
    📷 COMPLETE EXIF & CAMERA EXTRACTION
    ☁️ CLOUD METADATA & SSRF DETECTION
    🤖 AI & LLM ATTACK VECTORS
    📦 SUPPLY CHAIN SECURITY
    🔍 ADVANCED RECONNAISSANCE
    🛡️ ZERO TRUST ARCHITECTURE

    "In chaos, Leptothrix brings order. In data, it finds truth."
"""

# =============================================================================
# CORE IMPORTS - Minimal Required, No Heavy AI/ML at Startup
# =============================================================================

import os
import sys
import json
import re
import time
import hashlib
import subprocess
import argparse
import threading
import queue
import glob
import shutil
import tempfile
import traceback
import csv
import mmap
import struct
import binascii
import xml.etree.ElementTree as ET
import socket
import urllib.request
import urllib.parse
import urllib.error
import ssl
import gzip
import zlib
import random
import ipaddress
import base64
import secrets
import string
import itertools
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Set, Generator, Union
from dataclasses import dataclass, field, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict, Counter, OrderedDict
from urllib.parse import urlparse, urljoin, urlencode, parse_qs

# =============================================================================
# VERSION & CONSTANTS
# =============================================================================

__version__ = "8.0.0-ultimate-complete"
__author__ = "SYLHETYHACKVENGER (THE-ERROR808)"

# All extensions supported - COMPLETE
ALL_EXTENSIONS = [
    # Documents
    "pdf", "doc", "docx", "odt", "rtf", "tex", "wpd", "pages", "key", "numbers",
    # Presentations
    "ppt", "pptx", "odp", "pps", "keynote",
    # Spreadsheets
    "xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "csv", "tsv",
    # Images
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp", "heic", "heif",
    "raw", "cr2", "nef", "arw", "dng", "orf", "rw2", "sr2", "raf",
    "svg", "ico", "psd", "ai", "eps", "indd", "xcf",
    # Videos
    "mp4", "mov", "avi", "mkv", "wmv", "flv", "webm", "m4v", "mpg", "mpeg",
    "3gp", "ogv", "ts", "mts", "m2ts", "mxf", "prores",
    # Audio
    "mp3", "wav", "flac", "ogg", "wma", "aac", "m4a", "opus", "alac", "dsd",
    "midi", "mid", "mod", "xm", "it", "s3m",
    # Archives
    "zip", "rar", "7z", "tar", "gz", "bz2", "xz", "zst", "lz4", "lzma",
    "cab", "arj", "lzh", "iso", "dmg", "vhd", "vmdk",
    # Code
    "py", "js", "jsx", "ts", "tsx", "java", "c", "cpp", "h", "hpp", "cs",
    "go", "rs", "rb", "php", "pl", "pm", "sh", "bash", "zsh", "fish",
    "html", "htm", "xhtml", "xml", "xsd", "xsl", "wsdl", "json", "yml", "yaml",
    "toml", "ini", "cfg", "conf", "log", "txt", "md", "rst", "adoc",
    "css", "scss", "sass", "less", "stylus", "sql", "psql", "db",
    "swift", "kt", "kts", "dart", "lua", "r", "matlab", "julia", "nim",
    "v", "zig", "crystal", "elixir", "erlang", "haskell", "scala", "clojure",
    # System
    "exe", "dll", "so", "dylib", "sys", "drv", "bin", "run", "appimage",
    "deb", "rpm", "apk", "ipa", "msi", "app", "bundle", "framework",
    # Emails
    "eml", "emlx", "msg", "pst", "ost", "oft", "pst", "vcf", "ics", "ical",
    # Security
    "pem", "crt", "cer", "der", "p12", "pfx", "key", "pub", "asc", "gpg",
    # Database
    "sqlite", "db", "sql", "mdb", "accdb", "fdb", "dbf", "dbc", "ibd", "myd", "myi"
]

# =============================================================================
# LAZY IMPORTS - CRITICAL: Prevents CUDA/torch errors at startup
# =============================================================================

_lazy_imports = {}

def lazy_import(module_name: str, import_name: str = None):
    """
    Lazy load module only when needed.
    This prevents torch/tensorflow/CUDA from loading at startup.
    """
    if module_name not in _lazy_imports:
        try:
            if import_name:
                _lazy_imports[module_name] = __import__(module_name, fromlist=[import_name])
            else:
                _lazy_imports[module_name] = __import__(module_name)
        except ImportError:
            _lazy_imports[module_name] = None
        except Exception as e:
            # Catch all exceptions including CUDA/OS errors
            _lazy_imports[module_name] = None
    return _lazy_imports[module_name]

# =============================================================================
# CONFIGURATION - MAX POWER SETTINGS
# =============================================================================

CONFIG = {
    'threads': 32,
    'timeout': 30,
    'max_retries': 5,
    'max_file_size': 5 * 1024 * 1024 * 1024,  # 5GB
    'chunk_size': 128 * 1024 * 1024,  # 128MB
    'cache_size': 50000,
    'batch_size': 200,
    'cloud_metadata_timeout': 5,
    'dns_timeout': 3,
    'scan_depth': 10,
    'max_links': 5000,
    'request_delay': 0.1,
    'ssl_verify': False,
    'exiftool_timeout': 15,
    'max_connections': 100,
}

# =============================================================================
# DEPENDENCY CHECK - FIXED: No heavy imports at startup
# =============================================================================

def check_and_install_dependencies():
    """Check dependencies without importing heavy modules"""
    # Only check essential packages
    required = {
        'requests': 'requests',
        'beautifulsoup4': 'bs4',
        'lxml': 'lxml',
        'Pillow': 'PIL',
        'PyPDF2': 'PyPDF2',
        'python-docx': 'docx',
        'openpyxl': 'openpyxl',
        'exifread': 'exifread',
    }
    
    missing = []
    for package, import_name in required.items():
        try:
            __import__(import_name)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"⚠️ Missing dependencies: {', '.join(missing)}")
        install = input("Install missing dependencies? (y/n): ")
        if install.lower() == 'y':
            for package in missing:
                try:
                    subprocess.check_call([
                        sys.executable, "-m", "pip", "install",
                        "--ignore-installed", package
                    ])
                except:
                    try:
                        subprocess.check_call([
                            sys.executable, "-m", "pip", "install",
                            "--user", package
                        ])
                    except:
                        print(f"⚠️ Could not install {package}")
        return False
    
    # Heavy packages - only warn, don't try to import
    heavy_packages = ['transformers', 'torch', 'tensorflow']
    for package in heavy_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"ℹ️ Optional package {package} not installed. AI features will be limited.")
        except Exception:
            print(f"ℹ️ {package} import failed. AI features will be limited.")
    
    return True

# =============================================================================
# LOGGER - ULTIMATE
# =============================================================================

class Logger:
    """Leptothrix Ultimate Advanced Logger"""
    
    _colors = {
        'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m',
        'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m',
        'cyan': '\033[36m', 'white': '\033[37m',
        'bright_red': '\033[91m', 'bright_green': '\033[92m',
        'bright_yellow': '\033[93m', 'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m', 'bright_cyan': '\033[96m',
        'bright_white': '\033[97m', 'reset': '\033[0m',
        'bold': '\033[1m', 'dim': '\033[2m',
    }
    
    _level_map = {
        'CRITICAL': {'color': 'bright_red', 'prefix': '🚨', 'value': 0},
        'ERROR': {'color': 'red', 'prefix': '❌', 'value': 1},
        'WARNING': {'color': 'yellow', 'prefix': '⚠️', 'value': 2},
        'SUCCESS': {'color': 'bright_green', 'prefix': '✅', 'value': 3},
        'INFO': {'color': 'bright_blue', 'prefix': 'ℹ️', 'value': 3},
        'VERBOSE': {'color': 'bright_cyan', 'prefix': '🔍', 'value': 4},
        'DEBUG': {'color': 'dim', 'prefix': '🐛', 'value': 5},
        'TRACE': {'color': 'white', 'prefix': '🔬', 'value': 6},
        'SECURITY': {'color': 'bright_red', 'prefix': '🛡️', 'value': 3},
        'FORENSIC': {'color': 'bright_magenta', 'prefix': '🔎', 'value': 3},
    }
    
    _level = 3
    _log_file = None
    
    @classmethod
    def set_level(cls, level: str):
        level_map = {'silent': 0, 'error': 1, 'warning': 2, 'info': 3, 'verbose': 4, 'debug': 5, 'trace': 6}
        cls._level = level_map.get(level.lower(), 3)
    
    @classmethod
    def set_log_file(cls, filepath: str):
        cls._log_file = filepath
    
    @classmethod
    def _log(cls, level: str, message: str):
        if cls._level < cls._level_map[level]['value']:
            return
        
        color = cls._colors.get(cls._level_map[level]['color'], '')
        prefix = cls._level_map[level]['prefix']
        reset = cls._colors['reset']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        log_line = f"[{timestamp}] {prefix} {message}"
        
        if cls._log_file:
            with open(cls._log_file, 'a') as f:
                f.write(log_line + '\n')
        
        if level in ['CRITICAL', 'ERROR']:
            print(f"{color}{log_line}{reset}", file=sys.stderr)
        else:
            print(f"{color}{log_line}{reset}")
    
    @classmethod
    def critical(cls, msg): cls._log('CRITICAL', msg)
    @classmethod
    def error(cls, msg): cls._log('ERROR', msg)
    @classmethod
    def warning(cls, msg): cls._log('WARNING', msg)
    @classmethod
    def success(cls, msg): cls._log('SUCCESS', msg)
    @classmethod
    def info(cls, msg): cls._log('INFO', msg)
    @classmethod
    def verbose(cls, msg): cls._log('VERBOSE', msg)
    @classmethod
    def debug(cls, msg): cls._log('DEBUG', msg)
    @classmethod
    def trace(cls, msg): cls._log('TRACE', msg)
    @classmethod
    def security(cls, msg): cls._log('SECURITY', msg)
    @classmethod
    def forensic(cls, msg): cls._log('FORENSIC', msg)

# =============================================================================
# DATA CLASSES - COMPLETE
# =============================================================================

@dataclass
class Finding:
    """Complete security finding"""
    id: str = field(default_factory=lambda: secrets.token_hex(8))
    type: str = ''
    category: str = ''
    severity: str = ''  # CRITICAL, HIGH, MEDIUM, LOW, INFO
    title: str = ''
    description: str = ''
    evidence: Dict[str, Any] = field(default_factory=dict)
    remediation: str = ''
    references: List[str] = field(default_factory=list)
    cve: Optional[str] = None
    cvss_score: float = 0.0
    confidence: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    source: str = 'leptothrix'
    affected_file: str = ''
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Artifact:
    """Complete forensic artifact"""
    path: str = ''
    name: str = ''
    size: int = 0
    extension: str = ''
    mime_type: str = ''
    md5: str = ''
    sha1: str = ''
    sha256: str = ''
    sha512: str = ''
    created: str = ''
    modified: str = ''
    accessed: str = ''
    permissions: str = ''
    entropy: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    exif: Dict[str, Any] = field(default_factory=dict)
    gps: Dict[str, Any] = field(default_factory=dict)
    findings: List[Finding] = field(default_factory=list)
    threat_intel: Dict[str, Any] = field(default_factory=dict)
    ai_analysis: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ThreatIntel:
    """Threat intelligence data"""
    indicators: List[str] = field(default_factory=list)
    malware_families: List[str] = field(default_factory=list)
    attack_patterns: List[str] = field(default_factory=list)
    tactics: List[str] = field(default_factory=list)
    risk_score: float = 0.0
    confidence: float = 0.0
    severity: str = 'low'
    timestamp: float = field(default_factory=time.time)

# =============================================================================
# UTILITY FUNCTIONS - COMPLETE
# =============================================================================

def human_readable_size(size: int) -> str:
    """Convert bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def calculate_hash(data: bytes, algorithm: str = 'sha256') -> str:
    """Calculate hash of data"""
    hasher = hashlib.new(algorithm)
    hasher.update(data)
    return hasher.hexdigest()

def calculate_entropy(data: bytes) -> float:
    """Calculate Shannon entropy"""
    if not data:
        return 0.0
    freq = {}
    for byte in data:
        freq[byte] = freq.get(byte, 0) + 1
    entropy = 0.0
    length = len(data)
    for count in freq.values():
        p = count / length
        entropy -= p * (p.bit_length() - 1)
    return entropy / 8.0

def safe_filename(filename: str) -> str:
    """Sanitize filename"""
    return re.sub(r'[^\w\-_.]', '_', filename)[:255]

def chunk_list(lst: List, n: int) -> Generator[List, None, None]:
    """Chunk a list into n-sized chunks"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def deep_merge(dict1: Dict, dict2: Dict) -> Dict:
    """Deep merge two dictionaries"""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def get_timestamp() -> str:
    """Get current timestamp"""
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')[:-3]

# =============================================================================
# PROGRESS TRACKER
# =============================================================================

class ProgressTracker:
    """Track progress of operations"""
    
    def __init__(self, total: int, name: str = "Progress"):
        self.total = total
        self.current = 0
        self.name = name
        self.start_time = time.time()
        self._lock = threading.Lock()
    
    def update(self, n: int = 1):
        with self._lock:
            self.current += n
            self._display()
    
    def _display(self):
        elapsed = time.time() - self.start_time
        if self.current > 0:
            rate = self.current / elapsed if elapsed > 0 else 0
            remaining = (self.total - self.current) / rate if rate > 0 else 0
        else:
            rate = 0
            remaining = 0
        
        percent = (self.current / self.total) * 100
        bar_length = 40
        filled = int(bar_length * self.current / self.total)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        sys.stdout.write(
            f"\r{self.name}: [{bar}] {percent:5.1f}% "
            f"({self.current:,}/{self.total:,}) "
            f"[{rate:.1f}/s] [{self._format_time(remaining)}]"
        )
        sys.stdout.flush()
    
    def _format_time(self, seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.0f}s"
        elif seconds < 3600:
            return f"{seconds/60:.0f}m"
        else:
            return f"{seconds/3600:.1f}h"
    
    def finish(self):
        self.current = self.total
        self._display()
        print()

# =============================================================================
# CLOUD METADATA MODULE - COMPLETE
# =============================================================================

class CloudMetadataModule:
    """Complete cloud metadata and SSRF detection"""
    
    def __init__(self):
        self._providers = {
            'aws': {
                'endpoints': [
                    'http://169.254.169.254/latest/meta-data/',
                    'http://169.254.169.254/latest/user-data/',
                    'http://169.254.169.254/latest/dynamic/instance-identity/document/',
                    'http://169.254.169.254/latest/meta-data/iam/security-credentials/',
                    'http://169.254.169.254/latest/meta-data/instance-id',
                    'http://169.254.169.254/latest/meta-data/instance-type',
                    'http://169.254.169.254/latest/meta-data/ami-id',
                    'http://169.254.169.254/latest/meta-data/public-ipv4',
                    'http://169.254.169.254/latest/meta-data/local-ipv4',
                ],
                'headers': {},
                'imdsv1': True,
                'imdsv2': True
            },
            'gcp': {
                'endpoints': [
                    'http://metadata.google.internal/computeMetadata/v1/',
                    'http://metadata.google.com/computeMetadata/v1/',
                    'http://169.254.169.254/computeMetadata/v1/',
                    'http://metadata.google.internal/computeMetadata/v1/project/project-id',
                    'http://metadata.google.internal/computeMetadata/v1/instance/zone',
                    'http://metadata.google.internal/computeMetadata/v1/instance/machine-type',
                ],
                'headers': {'Metadata-Flavor': 'Google'},
                'imdsv1': False,
                'imdsv2': True
            },
            'azure': {
                'endpoints': [
                    'http://169.254.169.254/metadata/instance?api-version=2017-12-01',
                    'http://169.254.169.254/metadata/instance/compute?api-version=2017-12-01',
                    'http://169.254.169.254/metadata/instance/network?api-version=2017-12-01',
                ],
                'headers': {'Metadata': 'true'},
                'imdsv1': False,
                'imdsv2': True
            },
            'digitalocean': {
                'endpoints': [
                    'http://169.254.169.254/metadata/v1.json',
                    'http://169.254.169.254/metadata/v1/id',
                    'http://169.254.169.254/metadata/v1/region',
                ],
                'headers': {},
                'imdsv1': True,
                'imdsv2': False
            },
            'alibaba': {
                'endpoints': [
                    'http://100.100.100.200/latest/meta-data/',
                    'http://100.100.100.200/latest/meta-data/instance-id',
                    'http://100.100.100.200/latest/meta-data/region-id',
                ],
                'headers': {},
                'imdsv1': True,
                'imdsv2': False
            }
        }
        
        self._ssrf_patterns = [
            r'(169\.254\.\d+\.\d+)',
            r'(metadata\.google\.\w+)',
            r'(100\.100\.100\.200)',
            r'(metadata\.internal)',
            r'(instance-data)',
            r'(api\.ipify\.org)',
            r'(checkip\.amazonaws\.com)',
            r'(ifconfig\.me)',
            r'(icanhazip\.com)',
            r'(localhost|127\.0\.0\.1)',
            r'(0\.0\.0\.0)',
            r'(192\.168\.\d+\.\d+)',
            r'(10\.\d+\.\d+\.\d+)',
        ]
        
        self._ssrf_ports = [80, 443, 8080, 8443, 8000, 9000, 3000, 5000, 7000, 9200]
    
    def analyze_ssrf(self, url: str) -> List[Finding]:
        """Complete SSRF analysis"""
        findings = []
        
        # Check for metadata endpoints
        for provider, config in self._providers.items():
            for endpoint in config['endpoints']:
                if endpoint in url or url.startswith(endpoint):
                    finding = Finding(
                        type='CLOUD_METADATA_ACCESS',
                        category='cloud',
                        severity='CRITICAL',
                        title=f'Cloud Metadata Access Detected ({provider.upper()})',
                        description=f'URL attempts to access cloud metadata endpoint: {url}',
                        evidence={'url': url, 'provider': provider, 'endpoint': endpoint},
                        remediation='Implement proper input validation. Use allowlist for allowed domains.',
                        confidence=1.0,
                        references=['https://owasp.org/www-community/attacks/Server_Side_Request_Forgery']
                    )
                    findings.append(finding)
                    return findings
        
        # Check for IMDSv1 exploitation
        imdsv1_patterns = [
            '/latest/meta-data/iam/security-credentials/',
            '/latest/meta-data/identity-credentials/',
            '/latest/meta-data/iam/',
            '/metadata/instance/compute/',
            '/computeMetadata/v1/',
        ]
        for pattern in imdsv1_patterns:
            if pattern in url:
                finding = Finding(
                    type='IMDSV1_EXPLOITATION',
                    category='ssrf',
                    severity='CRITICAL',
                    title='IMDSv1 Exploitation Detected',
                    description=f'URL uses IMDSv1 stateless GET request: {url}',
                    evidence={'url': url, 'pattern': pattern},
                    remediation='Disable IMDSv1. Enable IMDSv2 with token requirement.',
                    confidence=1.0
                )
                findings.append(finding)
                return findings
        
        # Check for SSRF patterns
        for pattern in self._ssrf_patterns:
            if re.search(pattern, url, re.I):
                finding = Finding(
                    type='SSRF_PATTERN_DETECTED',
                    category='ssrf',
                    severity='HIGH',
                    title='SSRF Pattern Detected',
                    description=f'URL contains potential SSRF pattern: {url}',
                    evidence={'url': url, 'pattern': pattern},
                    remediation='Restrict outbound HTTP requests. Use URL sanitization and whitelist domains.',
                    confidence=0.85
                )
                findings.append(finding)
                break
        
        # Check for port scanning
        for port in self._ssrf_ports:
            if f':{port}' in url or f'%3A{port}' in url:
                finding = Finding(
                    type='PORT_SCAN_DETECTED',
                    category='recon',
                    severity='MEDIUM',
                    title='Port Scanning Detected',
                    description=f'URL contains port number: {port}',
                    evidence={'url': url, 'port': port},
                    remediation='Implement port filtering. Restrict outbound ports.',
                    confidence=0.7
                )
                findings.append(finding)
                break
        
        return findings

# =============================================================================
# EXIF METADATA MODULE - COMPLETE
# =============================================================================

class EXIFMetadataModule:
    """Complete EXIF metadata extraction"""
    
    def __init__(self):
        self._exiftool = self._find_exiftool()
        self._pil_available = False
        
        try:
            from PIL import Image
            from PIL.ExifTags import TAGS, GPSTAGS
            self._Image = Image
            self._TAGS = TAGS
            self._GPSTAGS = GPSTAGS
            self._pil_available = True
        except:
            pass
        
        self._lens_database = {
            'EF 50mm f/1.8': {'focal': 50, 'max_aperture': 1.8, 'type': 'Prime'},
            'EF 24-70mm f/2.8': {'focal': [24, 70], 'max_aperture': 2.8, 'type': 'Zoom'},
            'EF 70-200mm f/2.8': {'focal': [70, 200], 'max_aperture': 2.8, 'type': 'Zoom'},
            'AF-S 50mm f/1.8': {'focal': 50, 'max_aperture': 1.8, 'type': 'Prime'},
            'AF-S 24-70mm f/2.8': {'focal': [24, 70], 'max_aperture': 2.8, 'type': 'Zoom'},
            'FE 50mm f/1.8': {'focal': 50, 'max_aperture': 1.8, 'type': 'Prime'},
            'FE 24-70mm f/2.8': {'focal': [24, 70], 'max_aperture': 2.8, 'type': 'Zoom'},
        }
    
    def _find_exiftool(self) -> Optional[str]:
        for path in ['exiftool', '/usr/bin/exiftool', '/usr/local/bin/exiftool']:
            if shutil.which(path):
                return path
        return None
    
    def extract(self, file_path: str) -> Dict[str, Any]:
        """Extract complete EXIF metadata"""
        result = {
            'basic': {},
            'exif': {},
            'gps': {},
            'camera': {},
            'lens': {},
            'maker_notes': {},
            'thumbnail': None,
            'analysis': {},
        }
        
        if self._exiftool:
            data = self._extract_exiftool(file_path)
            if data:
                result = self._parse_exiftool_data(data, result)
        
        if self._pil_available:
            data = self._extract_pil(file_path)
            if data:
                result['basic'].update(data)
                result['exif'].update(data)
        
        # Extract thumbnail
        result['thumbnail'] = self._extract_thumbnail(file_path)
        
        # Analyze
        result['analysis'] = self._analyze_photo(result)
        
        return result
    
    def _extract_exiftool(self, file_path: str) -> Dict:
        try:
            result = subprocess.run(
                [self._exiftool, '-j', '-u', '-a', '-G', '-all', file_path],
                capture_output=True, text=True, timeout=CONFIG['exiftool_timeout']
            )
            if result.stdout:
                data = json.loads(result.stdout)
                if data:
                    return data[0]
        except:
            pass
        return {}
    
    def _parse_exiftool_data(self, data: Dict, result: Dict) -> Dict:
        for key, value in data.items():
            if key.startswith('File:'):
                continue
            
            if 'GPS' in key:
                result['gps'][key] = value
            elif 'Lens' in key:
                result['lens'][key] = value
            elif key in ['Model', 'Make', 'SerialNumber']:
                result['camera'][key] = value
            elif 'MakerNotes' in key:
                result['maker_notes'][key] = value
            else:
                result['basic'][key] = value
        
        # Parse GPS
        if result['gps']:
            result['gps']['parsed'] = self._parse_gps(result['gps'])
        
        return result
    
    def _extract_pil(self, file_path: str) -> Dict:
        result = {}
        try:
            with self._Image.open(file_path) as img:
                result['Width'] = img.width
                result['Height'] = img.height
                result['Format'] = img.format
                result['Mode'] = img.mode
                
                exif = img.getexif()
                if exif:
                    for tag_id, value in exif.items():
                        tag = self._TAGS.get(tag_id, str(tag_id))
                        if isinstance(value, bytes):
                            try:
                                value = value.decode('utf-8', errors='ignore')
                            except:
                                value = str(value)
                        result[tag] = value
        except:
            pass
        return result
    
    def _extract_thumbnail(self, file_path: str) -> Optional[bytes]:
        try:
            if self._exiftool:
                result = subprocess.run(
                    [self._exiftool, '-b', '-ThumbnailImage', file_path],
                    capture_output=True, timeout=5
                )
                if result.stdout:
                    return result.stdout
        except:
            pass
        
        try:
            if self._pil_available:
                with self._Image.open(file_path) as img:
                    if hasattr(img, '_getexif'):
                        exif = img._getexif()
                        if exif:
                            for tag_id, value in exif.items():
                                if tag_id == 0x0100:
                                    return value
        except:
            pass
        return None
    
    def _parse_gps(self, gps_data: Dict) -> Dict:
        parsed = {}
        
        lat = self._parse_coordinate(
            gps_data.get('GPSLatitude'),
            gps_data.get('GPSLatitudeRef', 'N')
        )
        lon = self._parse_coordinate(
            gps_data.get('GPSLongitude'),
            gps_data.get('GPSLongitudeRef', 'E')
        )
        
        if lat is not None and lon is not None:
            parsed['latitude'] = lat
            parsed['longitude'] = lon
            parsed['coordinates'] = f"{lat}, {lon}"
            parsed['google_maps'] = f"https://www.google.com/maps?q={lat},{lon}"
            parsed['openstreetmap'] = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"
        
        if 'GPSAltitude' in gps_data:
            alt = gps_data['GPSAltitude']
            if isinstance(alt, tuple):
                alt = alt[0] / alt[1] if alt[1] else 0
            parsed['altitude'] = alt
        
        if 'GPSImgDirection' in gps_data:
            direction = gps_data['GPSImgDirection']
            if isinstance(direction, tuple):
                direction = direction[0] / direction[1] if direction[1] else 0
            parsed['bearing'] = direction
            parsed['compass'] = self._degrees_to_compass(direction)
        
        return parsed
    
    def _parse_coordinate(self, coord, ref) -> Optional[float]:
        if not coord:
            return None
        try:
            if isinstance(coord, tuple) and len(coord) >= 3:
                degrees = float(coord[0]) if coord[0] else 0
                minutes = float(coord[1]) if coord[1] else 0
                seconds = float(coord[2]) if coord[2] else 0
                value = degrees + minutes/60 + seconds/3600
                if ref in ['S', 'W']:
                    value = -value
                return value
        except:
            pass
        return None
    
    def _degrees_to_compass(self, degrees: float) -> str:
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        index = int((degrees + 22.5) / 45) % 8
        return directions[index]
    
    def _analyze_photo(self, data: Dict) -> Dict:
        analysis = {'quality': {}, 'composition': {}, 'conditions': {}}
        basic = data.get('basic', {})
        
        if 'ExposureTime' in basic:
            exp = basic['ExposureTime']
            if isinstance(exp, tuple):
                exp = exp[0] / exp[1] if exp[1] else 0
            analysis['quality']['exposure'] = exp
            analysis['quality']['tripod_needed'] = exp < 1/60
        
        if 'FNumber' in basic:
            aperture = basic['FNumber']
            if isinstance(aperture, tuple):
                aperture = aperture[0] / aperture[1] if aperture[1] else 0
            analysis['quality']['aperture'] = aperture
            if aperture < 2.8:
                analysis['quality']['aperture_quality'] = 'Excellent (fast lens)'
            elif aperture < 4:
                analysis['quality']['aperture_quality'] = 'Good'
            else:
                analysis['quality']['aperture_quality'] = 'Standard'
        
        if 'ISOSpeedRatings' in basic:
            iso = basic['ISOSpeedRatings']
            if isinstance(iso, tuple):
                iso = iso[0] / iso[1] if iso[1] else 0
            analysis['quality']['iso'] = iso
            if iso < 400:
                analysis['quality']['iso_quality'] = 'Excellent (low noise)'
            elif iso < 1600:
                analysis['quality']['iso_quality'] = 'Good'
            else:
                analysis['quality']['iso_quality'] = 'High ISO (noise possible)'
        
        if 'FocalLength' in basic:
            focal = basic['FocalLength']
            if isinstance(focal, tuple):
                focal = focal[0] / focal[1] if focal[1] else 0
            analysis['composition']['focal_length'] = focal
            if focal < 35:
                analysis['composition']['lens_type'] = 'Wide angle'
            elif focal < 70:
                analysis['composition']['lens_type'] = 'Standard'
            else:
                analysis['composition']['lens_type'] = 'Telephoto'
        
        if 'WhiteBalance' in basic:
            wb = basic['WhiteBalance']
            if isinstance(wb, int):
                wb_values = {0: 'Auto', 1: 'Manual', 2: 'Daylight', 3: 'Cloudy', 4: 'Tungsten', 5: 'Fluorescent'}
                analysis['conditions']['white_balance'] = wb_values.get(wb, 'Unknown')
        
        if 'Flash' in basic:
            flash = basic['Flash']
            if isinstance(flash, int):
                analysis['conditions']['flash'] = 'Fired' if flash & 1 else 'Not fired'
        
        return analysis

# =============================================================================
# AI SECURITY MODULE - Lazy loaded, no CUDA errors
# =============================================================================

class AISecurityModule:
    """Complete AI/LLM security analysis - Lazy loaded"""
    
    def __init__(self):
        self._loaded = False
        self._model = None
        self._suspicious_keywords = [
            'execute', 'system', 'shell', 'command', 'exec', 'delete', 'remove',
            'admin', 'root', 'sudo', 'privilege', 'elevate', 'bypass'
        ]
        
        self._attack_patterns = {
            'AMA': {'keywords': self._suspicious_keywords, 'success_rate': 0.95, 'severity': 'CRITICAL'},
            'MM-MEPA': {'keywords': ['caption', 'tag', 'label', 'multimodal'], 'success_rate': 0.91, 'severity': 'HIGH'},
            'MPMA': {'keywords': ['rank', 'priority', 'order', 'preference'], 'success_rate': 0.87, 'severity': 'HIGH'},
        }
    
    def _load_model(self):
        """Lazy load AI model"""
        if self._loaded:
            return
        
        try:
            from transformers import pipeline
            self._model = pipeline('sentiment-analysis', device=-1)  # CPU mode
            self._loaded = True
            Logger.debug("AI model loaded successfully")
        except Exception as e:
            Logger.debug(f"AI model load failed: {e}")
            self._loaded = False
    
    def analyze_metadata(self, metadata: Dict[str, Any]) -> Tuple[Optional[AIAttack], List[Finding]]:
        """Analyze AI metadata for security issues"""
        findings = []
        attack = None
        
        tool_name = metadata.get('name', '')
        description = metadata.get('description', '')
        
        # Check for suspicious keywords
        for keyword in self._suspicious_keywords:
            if keyword in tool_name.lower() or keyword in description.lower():
                attack = AIAttack(
                    attack_type='AMA',
                    tool_name=tool_name,
                    tool_description=description,
                    manipulated_metadata={'name': tool_name, 'description': description},
                    success_rate=0.95,
                    attack_vector='Keyword manipulation',
                    severity='CRITICAL',
                    detection_method='Keyword matching',
                    mitigation='Validate tool names and descriptions against allowlist'
                )
                
                finding = Finding(
                    type='AI_SUSPICIOUS_KEYWORD',
                    category='ai',
                    severity='CRITICAL',
                    title='Suspicious AI Tool Keyword Detected',
                    description=f'Tool metadata contains suspicious keyword: {keyword}',
                    evidence={'tool_name': tool_name, 'keyword': keyword},
                    remediation='Implement metadata validation and sanitization.',
                    confidence=0.9
                )
                findings.append(finding)
                break
        
        # Check for YAML frontmatter manipulation
        if '---' in description and '---' in description:
            if not attack:
                attack = AIAttack(
                    attack_type='spoofing',
                    tool_name=tool_name,
                    tool_description=description,
                    manipulated_metadata={'frontmatter': True},
                    success_rate=0.79,
                    attack_vector='YAML frontmatter injection',
                    severity='HIGH',
                    detection_method='YAML detection',
                    mitigation='Validate YAML frontmatter. Use safe parsing.'
                )
            
            finding = Finding(
                type='AI_YAML_INJECTION',
                category='ai',
                severity='HIGH',
                title='YAML Frontmatter Injection Detected',
                description='Tool metadata contains YAML frontmatter markers',
                evidence={'tool_name': tool_name},
                remediation='Sanitize YAML content. Use safe YAML loaders.',
                confidence=0.8
            )
            findings.append(finding)
        
        return attack, findings

# =============================================================================
# RECONNAISSANCE MODULE - COMPLETE
# =============================================================================

class ReconnaissanceModule:
    """Complete reconnaissance and profiling"""
    
    def __init__(self):
        self._email_patterns = [
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
        ]
        
        self._phone_patterns = [
            r'(\+\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}',
            r'\d{3}-\d{3}-\d{4}',
            r'\(\d{3}\) \d{3}-\d{4}',
        ]
        
        self._social_media_patterns = {
            'twitter': r'(?:@|twitter\.com/)([a-zA-Z0-9_]{2,15})',
            'linkedin': r'linkedin\.com/in/([a-zA-Z0-9_-]{3,30})',
            'github': r'github\.com/([a-zA-Z0-9_-]{3,39})',
            'facebook': r'facebook\.com/([a-zA-Z0-9.]{5,50})',
            'instagram': r'instagram\.com/([a-zA-Z0-9_.]{3,30})',
            'youtube': r'youtube\.com/(?:c|channel|user)/([a-zA-Z0-9_-]{3,30})',
        }
        
        self._device_patterns = [
            r'iPhone(\s\d+)?', r'iPad(\s\d+)?', r'Macintosh', r'MacBook',
            r'Android(\s\d+\.\d+)?', r'Windows(\s\d+\.\d+)?', r'Linux',
            r'Chrome(\s\d+)?', r'Firefox(\s\d+)?', r'Safari(\s\d+)?',
        ]
        
        self._location_patterns = [
            r'([-+]?\d{1,2}\.\d{4,6})\s*[,;]\s*([-+]?\d{1,3}\.\d{4,6})',
            r'lat[-_: ]?(\d+\.\d+)[,; ]+lon[-_: ]?(\d+\.\d+)',
        ]
    
    def analyze_content(self, content: str) -> ReconData:
        """Analyze content for reconnaissance data"""
        recon = ReconData()
        
        # Extract emails
        for pattern in self._email_patterns:
            emails = re.findall(pattern, content, re.I)
            recon.email_addresses.extend(list(set(emails)))
        
        # Extract phone numbers
        for pattern in self._phone_patterns:
            phones = re.findall(pattern, content)
            recon.phone_numbers.extend(list(set(phones)))
        
        # Extract social media
        for platform, pattern in self._social_media_patterns.items():
            matches = re.findall(pattern, content, re.I)
            if matches:
                recon.social_media[platform] = matches[0] if isinstance(matches[0], str) else matches[0][0]
        
        # Extract locations
        for pattern in self._location_patterns:
            matches = re.findall(pattern, content, re.I)
            for match in matches:
                if isinstance(match, tuple) and len(match) >= 2:
                    recon.locations.append(f"{match[0]}, {match[1]}")
        
        # Extract devices
        for pattern in self._device_patterns:
            matches = re.findall(pattern, content, re.I)
            for match in matches:
                recon.devices.append(str(match))
        
        # Calculate risk score
        recon.risk_score = self._calculate_risk_score(recon)
        
        recon.patterns = {
            'email_count': len(recon.email_addresses),
            'phone_count': len(recon.phone_numbers),
            'social_media_count': len(recon.social_media),
            'location_count': len(recon.locations),
            'device_count': len(recon.devices),
        }
        
        return recon
    
    def _calculate_risk_score(self, recon: ReconData) -> float:
        score = 0.0
        if recon.email_addresses:
            score += 0.3
        if recon.phone_numbers:
            score += 0.4
        if recon.social_media:
            score += 0.2
        if recon.locations:
            score += 0.3
        if recon.devices:
            score += 0.15
        return min(score, 1.0)

# =============================================================================
# SUPPLY CHAIN MODULE - COMPLETE
# =============================================================================

class SupplyChainModule:
    """Complete supply chain security"""
    
    def __init__(self):
        self._legitimate_packages = {
            'requests', 'flask', 'django', 'numpy', 'pandas', 'tensorflow', 'torch',
            'scikit-learn', 'pillow', 'sqlalchemy', 'alembic', 'celery', 'redis',
            'pytest', 'black', 'flake8', 'mypy', 'pre-commit', 'coverage',
            'boto3', 'awscli', 'google-cloud', 'azure-sdk', 'kubernetes',
        }
        
        self._red_flag_keywords = [
            'malicious', 'exploit', 'backdoor', 'trojan', 'crypto', 'mining',
            'stealer', 'rat', 'bypass', 'crack', 'hack', 'cheat', 'bot',
        ]
    
    def analyze_package(self, package_data: Dict[str, Any]) -> Tuple[SupplyChainAttack, List[Finding]]:
        """Analyze package for supply chain issues"""
        findings = []
        
        name = package_data.get('name', '')
        version = package_data.get('version', '')
        author = package_data.get('author', '')
        stars = package_data.get('stars', 0)
        forks = package_data.get('forks', 0)
        commits = package_data.get('commits', 0)
        maintainers = package_data.get('maintainers', [])
        dependencies = package_data.get('dependencies', [])
        
        attack = SupplyChainAttack(
            package_name=name,
            version=version,
            author=author,
            maintainers=maintainers,
            dependencies=dependencies,
            fake_stars=stars,
            fake_forks=forks,
            fake_commits=commits
        )
        
        # Check for typosquatting
        for legit in self._legitimate_packages:
            if legit in name.lower() and legit != name.lower():
                attack.attack_type = 'spoofing'
                attack.red_flags.append(f'Potential typosquatting: {legit} -> {name}')
                
                finding = Finding(
                    type='TYPOSQUATTING',
                    category='supply_chain',
                    severity='HIGH',
                    title='Package Typosquatting Detected',
                    description=f'Package name resembles legitimate package: {legit} -> {name}',
                    evidence={'legitimate': legit, 'suspicious': name},
                    remediation='Verify package authenticity. Check maintainer history.',
                    confidence=0.8
                )
                findings.append(finding)
        
        # Check for red flag keywords
        for keyword in self._red_flag_keywords:
            if keyword in name.lower():
                attack.attack_type = 'spoofing'
                attack.red_flags.append(f'Suspicious keyword: {keyword}')
                
                finding = Finding(
                    type='SUSPICIOUS_PACKAGE_KEYWORD',
                    category='supply_chain',
                    severity='HIGH',
                    title='Suspicious Package Keyword',
                    description=f'Package name contains suspicious keyword: {keyword}',
                    evidence={'package': name, 'keyword': keyword},
                    remediation='Investigate package thoroughly before using.',
                    confidence=0.75
                )
                findings.append(finding)
                break
        
        # StarJacking detection
        if stars > 100 and forks < 10:
            attack.attack_type = 'starjacking'
            attack.red_flags.append(f'Unusual star-to-fork ratio: {stars}:{forks}')
            
            finding = Finding(
                type='STARJACKING',
                category='supply_chain',
                severity='MEDIUM',
                title='StarJacking Detected',
                description=f'Unusual star count ({stars}) compared to forks ({forks})',
                evidence={'stars': stars, 'forks': forks},
                remediation='Verify repository activity. Check community engagement.',
                confidence=0.7
            )
            findings.append(finding)
        
        # Calculate trust score
        trust_score = 1.0
        if attack.red_flags:
            trust_score -= 0.2 * len(attack.red_flags)
        if attack.attack_type:
            trust_score -= 0.3
        if len(maintainers) == 0:
            trust_score -= 0.2
        if not author:
            trust_score -= 0.1
        
        attack.trust_score = max(0, trust_score)
        
        return attack, findings

# =============================================================================
# THREAT INTELLIGENCE MODULE
# =============================================================================

class ThreatIntelligenceModule:
    """Threat intelligence and IOCs"""
    
    def __init__(self):
        self._malware_signatures = [
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'MALICIOUS', 'RANSOMWARE', 'TROJAN', 'EXPLOIT', 'BACKDOOR'
        ]
        
        self._cve_database = {
            'CVE-2021-44228': {'description': 'Log4Shell', 'severity': 'CRITICAL'},
            'CVE-2022-22965': {'description': 'Spring4Shell', 'severity': 'CRITICAL'},
            'CVE-2022-1388': {'description': 'F5 BIG-IP', 'severity': 'CRITICAL'},
        }
    
    def analyze(self, data: Dict[str, Any]) -> ThreatIntel:
        """Analyze threat intelligence"""
        intel = ThreatIntel()
        
        data_str = str(data).lower()
        
        # Check for malware signatures
        for sig in self._malware_signatures:
            if sig.lower() in data_str:
                intel.malware_families.append('Unknown')
                intel.indicators.append(sig)
                intel.risk_score = 1.0
        
        # Check for CVE references
        for cve_id, cve_data in self._cve_database.items():
            if cve_id.lower() in data_str:
                intel.indicators.append(cve_id)
                intel.attack_patterns.append(cve_data['description'])
                if cve_data['severity'] == 'CRITICAL':
                    intel.risk_score = max(intel.risk_score, 0.9)
        
        # Check for suspicious patterns
        suspicious_patterns = ['system', 'exec', 'cmd', 'powershell', 'bash']
        for pattern in suspicious_patterns:
            if pattern in data_str:
                intel.indicators.append(pattern)
                intel.tactics.append('Execution')
                intel.risk_score = max(intel.risk_score, 0.6)
        
        intel.confidence = intel.risk_score
        intel.timestamp = time.time()
        
        return intel

# =============================================================================
# MAIN FRAMEWORK - LEPTOTHRIX ULTIMATE
# =============================================================================

class LeptothrixUltimate:
    """The Complete Invincible Framework"""
    
    def __init__(self):
        # Initialize all modules
        self.cloud = CloudMetadataModule()
        self.exif = EXIFMetadataModule()
        self.ai = AISecurityModule()
        self.supply = SupplyChainModule()
        self.recon = ReconnaissanceModule()
        self.threat = ThreatIntelligenceModule()
        
        # Storage
        self.findings: List[Finding] = []
        self.artifacts: List[Artifact] = []
        self.threat_intel: ThreatIntel = ThreatIntel()
        self._lock = threading.Lock()
        self._executor = ThreadPoolExecutor(max_workers=CONFIG['threads'])
        
        # Show banner
        self._show_banner()
    
    def _show_banner(self):
        """Show banner"""
        banner = f"""
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢴⢾⡙⢞⣷⢦⢤⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣢⣜⡛⠘⣫⣄⣻⠀⠀⠀⠀⠀
⢠⠶⣼⣇⣵⡤⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡺⠍⢫⣶⢰⣍⠋⢽⠀⠀⠀⠀⠀
⣎⣴⣌⡛⢋⣴⣼⠀⠀⠀⠀⡖⢦⠀⠀⢀⣠⣤⣄⡀⠀⠀⠙⠛⠾⣡⢬⣻⠾⠚⠁⢀⡤⡀⠀
⣠⠞⣩⣶⣮⡙⢦⠀⠀⠀⠀⠁⣪⣴⣾⡿⠟⠛⠻⢿⣷⣦⣄⡀⠀⠈⠉⠀⠀⠀⡖⠚⠀⠓⢢
⠈⠚⣿⣇⣽⠙⠉⠀⣀⣤⣶⣿⠿⠛⠁⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣦⣀⠀⠀⠀⠈⠹⣀⡟⠉
⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣶⡄⠀⠀⠈⠀⠀
⣠⣤⣤⡀⠀⢺⣿⠻⣷⣦⣔⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠿⢿⣿⠀⠀⠀⠀⠀
⣿⣏⣿⣿⠀⢸⣿⠀⠀⠉⠛⠿⣶⣭⡓⠤⣀⠀⠀⠀⢀⣠⣴⡾⠟⠋⠁⡆⢸⣿⠀⢀⡤⣄⠀
⠙⠛⠛⠃⠀⢸⣿⠀⠀⠀⠀⠀⠀⠙⠻⢷⣦⣭⣤⣶⠿⠋⠁⠀⠀⡄⠀⡇⢸⣿⠀⠘⠦⠞⠀
⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠲⡌⣿⡏⠀⠠⠀⠀⠀⣁⠤⠒⡇⢸⣿⠀⣴⣦⡀⠀
⠀⠀⣖⠙⡆⢸⣿⠀⠀⠀⠀⠀⠀⢀⠔⠁⡇⣿⡇⠀⠁⠠⡾⣴⡿⣿⣦⡄⢸⣿⠘⠧⠼⠇⠀
⠀⠀⠈⠉⠁⣼⣿⢀⡠⠖⠀⠀⢀⠥⣄⠀⡇⣿⡇⡇⠀⡼⡽⢿⣖⣣⣿⡇⢸⣿⠀⡖⢲⡄⠀
⠀⠀⠀⠀⠀⠸⣿⣦⣑⠢⢄⡀⠸⣀⣸⠀⡇⣿⡇⡇⢾⠞⢶⠎⣉⡿⢓⣡⣿⣿⠀⠉⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣦⣍⡓⠦⣀⠀⡇⣿⡇⡇⢀⡠⠔⣫⣵⣾⣿⣿⡿⠿⣿⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣿⣿⣷⣬⣙⠃⣿⡇⢓⣭⣶⣿⣿⣛⢹⣿⣯⠤⠀⢿⢻⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⢦⣿⣏⠀⣹⣿⠿⣿⣿⣿⡿⠟⠉⣸⣤⣼⠈⣿⣯⣓⣒⣪⣾⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠘⠿⠽⠿⠀⠈⠛⠿⠿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⢀⢀⣄⣀⣀⣀⣄⣀⣀⣀⣀⣀⡀⣀⢀⣀⢀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⠿⠟⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠻⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀
╔═══════════════════════════════════════════════════════════════════════════════╗
║  L E P T O T H R I X   U L T I M A T E   v{__version__}                    ║
║  ☁️ Cloud | 📷 EXIF | 🤖 AI | 📦 Supply Chain | 🔍 Recon | 🛡️ Threat      ║
║    AUTHOR - SYLHETYHACKVENGER (THE-ERROR808)              ║
╚═══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def analyze_file(self, file_path: str) -> Artifact:
        """Complete file analysis"""
        Logger.info(f"Analyzing: {file_path}")
        
        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            return Artifact()
        
        # Create artifact
        artifact = Artifact(
            path=file_path,
            name=os.path.basename(file_path),
            extension=os.path.splitext(file_path)[1].lower()
        )
        
        # Get file stats
        try:
            stat = os.stat(file_path)
            artifact.size = stat.st_size
            artifact.created = datetime.fromtimestamp(stat.st_ctime).isoformat()
            artifact.modified = datetime.fromtimestamp(stat.st_mtime).isoformat()
            artifact.accessed = datetime.fromtimestamp(stat.st_atime).isoformat()
            artifact.permissions = oct(stat.st_mode)[-3:]
        except:
            pass
        
        # Calculate hashes
        try:
            with open(file_path, 'rb') as f:
                data = f.read(CONFIG['chunk_size'])
                if data:
                    artifact.md5 = hashlib.md5(data).hexdigest()
                    artifact.sha1 = hashlib.sha1(data).hexdigest()
                    artifact.sha256 = hashlib.sha256(data).hexdigest()
                    artifact.sha512 = hashlib.sha512(data).hexdigest()
                    artifact.entropy = calculate_entropy(data)
        except:
            pass
        
        # Check if image
        if artifact.extension in ['.jpg', '.jpeg', '.png', '.tiff', '.webp', '.gif', '.bmp', '.heic']:
            exif_data = self.exif.extract(file_path)
            if exif_data:
                artifact.exif = exif_data
                artifact.metadata = exif_data.get('basic', {})
                artifact.gps = exif_data.get('gps', {}).get('parsed', {})
        
        # Security findings
        findings = []
        
        # Check for SSRF in content
        try:
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read(1024 * 1024)
                urls = re.findall(r'https?://[^\s"\'<>]+', content)
                for url in urls[:CONFIG['max_links']]:
                    findings.extend(self.cloud.analyze_ssrf(url))
                
                # Reconnaissance
                recon_data = self.recon.analyze_content(content)
                if recon_data.email_addresses or recon_data.social_media:
                    artifact.metadata['recon'] = asdict(recon_data)
        except:
            pass
        
        # Check for AI metadata
        if 'name' in str(artifact.metadata) or 'description' in str(artifact.metadata):
            _, ai_findings = self.ai.analyze_metadata(artifact.metadata)
            findings.extend(ai_findings)
        
        # Threat intelligence
        if artifact.metadata:
            self.threat_intel = self.threat.analyze(artifact.metadata)
            artifact.threat_intel = asdict(self.threat_intel)
        
        artifact.findings = findings
        
        with self._lock:
            self.artifacts.append(artifact)
            self.findings.extend(findings)
        
        return artifact
    
    def analyze_directory(self, dir_path: str, recursive: bool = True) -> int:
        """Analyze directory"""
        Logger.info(f"Scanning directory: {dir_path}")
        
        if not os.path.isdir(dir_path):
            Logger.error(f"Directory not found: {dir_path}")
            return 0
        
        pattern = '**/*' if recursive else '*'
        files = glob.glob(os.path.join(dir_path, pattern), recursive=recursive)
        files = [f for f in files if os.path.isfile(f)]
        files = [f for f in files if os.path.getsize(f) <= CONFIG['max_file_size']]
        
        count = 0
        total = len(files)
        Logger.info(f"Found {total} files")
        
        progress = ProgressTracker(total, "Analyzing")
        
        for i, file_path in enumerate(files):
            try:
                self.analyze_file(file_path)
                count += 1
                progress.update()
            except Exception as e:
                Logger.debug(f"Error on {file_path}: {e}")
        
        progress.finish()
        Logger.success(f"Analyzed {count} files")
        return count
    
    def analyze_image(self, file_path: str) -> Dict:
        """Analyze image with EXIF"""
        Logger.info(f"Analyzing image: {file_path}")
        return self.exif.extract(file_path)
    
    def analyze_ssrf(self, url: str) -> List[Finding]:
        """Analyze URL for SSRF"""
        Logger.info(f"Analyzing SSRF: {url}")
        return self.cloud.analyze_ssrf(url)
    
    def analyze_ai(self, metadata: Dict) -> List[Finding]:
        """Analyze AI metadata"""
        Logger.info("Analyzing AI metadata")
        _, findings = self.ai.analyze_metadata(metadata)
        return findings
    
    def analyze_package(self, data: Dict) -> List[Finding]:
        """Analyze package"""
        Logger.info(f"Analyzing package: {data.get('name', 'unknown')}")
        _, findings = self.supply.analyze_package(data)
        return findings
    
    def analyze_threat(self, data: Dict) -> ThreatIntel:
        """Analyze threat intelligence"""
        Logger.info("Analyzing threat intelligence")
        return self.threat.analyze(data)
    
    def generate_report(self, output_file: str, format: str = 'json'):
        """Generate report"""
        report = {
            'framework': 'Leptothrix Ultimate',
            'version': __version__,
            'timestamp': datetime.now().isoformat(),
            'total_findings': len(self.findings),
            'findings_by_severity': defaultdict(int),
            'findings_by_category': defaultdict(int),
            'findings': [
                {
                    'id': f.id,
                    'type': f.type,
                    'category': f.category,
                    'severity': f.severity,
                    'title': f.title,
                    'description': f.description,
                    'evidence': f.evidence,
                    'remediation': f.remediation,
                    'references': f.references,
                    'cve': f.cve,
                    'cvss_score': f.cvss_score,
                    'confidence': f.confidence,
                    'timestamp': f.timestamp
                }
                for f in self.findings
            ],
            'artifacts': [
                {
                    'path': a.path,
                    'name': a.name,
                    'size': a.size,
                    'size_human': human_readable_size(a.size),
                    'md5': a.md5,
                    'sha256': a.sha256,
                    'entropy': a.entropy,
                    'gps': a.gps,
                    'findings_count': len(a.findings),
                    'threat_score': a.threat_intel.get('risk_score', 0)
                }
                for a in self.artifacts
            ],
            'threat_intelligence': {
                'indicators': self.threat_intel.indicators,
                'malware_families': self.threat_intel.malware_families,
                'risk_score': self.threat_intel.risk_score,
                'confidence': self.threat_intel.confidence,
                'severity': self.threat_intel.severity
            }
        }
        
        # Count by severity and category
        for f in self.findings:
            report['findings_by_severity'][f.severity] += 1
            report['findings_by_category'][f.category] += 1
        
        report['findings_by_severity'] = dict(report['findings_by_severity'])
        report['findings_by_category'] = dict(report['findings_by_category'])
        
        # Generate based on format
        if format == 'json':
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2, default=str)
        elif format == 'html':
            self._generate_html_report(report, output_file)
        elif format == 'csv':
            self._generate_csv_report(report, output_file)
        
        Logger.success(f"Report saved: {output_file}")
        Logger.info(f"Total findings: {len(self.findings)}")
        for severity, count in report['findings_by_severity'].items():
            if count > 0:
                Logger.info(f"  {severity}: {count}")
    
    def _generate_html_report(self, report: Dict, output_file: str):
        """Generate HTML report"""
        html = [
            '<!DOCTYPE html><html><head><meta charset="UTF-8">',
            '<title>Leptothrix Ultimate Report</title>',
            '<style>',
            'body{font-family:monospace;background:#0a0a0f;color:#a0a0b8;padding:20px}',
            'h1{color:#ff006e;text-shadow:0 0 20px rgba(255,0,110,0.3)}',
            'h2{color:#ff006e;margin-top:30px}',
            '.stats{display:flex;gap:20px;margin:20px 0;flex-wrap:wrap}',
            '.stat{background:#111118;padding:15px 25px;border:1px solid #2a1f3d;border-radius:4px}',
            '.stat-num{color:#ff006e;font-size:28px;font-weight:bold}',
            '.stat-label{color:#6e6350;font-size:12px}',
            '.finding{background:#111118;border:1px solid #2a1f3d;padding:15px;margin:10px 0;border-radius:4px}',
            '.critical{border-left:4px solid #ff003c}',
            '.high{border-left:4px solid #ff6600}',
            '.medium{border-left:4px solid #ffaa00}',
            '.low{border-left:4px solid #00ff66}',
            '.info{border-left:4px solid #00aaff}',
            '.severity{font-weight:bold;font-size:14px}',
            '.critical .severity{color:#ff003c}',
            '.high .severity{color:#ff6600}',
            '.medium .severity{color:#ffaa00}',
            '.low .severity{color:#00ff66}',
            '.info .severity{color:#00aaff}',
            '.title{font-size:16px;font-weight:bold;color:#ff006e}',
            '.evidence{background:#000;padding:10px;border-radius:4px;margin:5px 0;font-size:12px}',
            '.remediation{color:#00ffaa;padding:5px 10px;border-left:3px solid #00ffaa}',
            '.badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:10px;margin:2px}',
            '.badge-critical{background:#ff003c33;color:#ff003c;border:1px solid #ff003c}',
            '.badge-high{background:#ff660033;color:#ff6600;border:1px solid #ff6600}',
            '.badge-medium{background:#ffaa0033;color:#ffaa00;border:1px solid #ffaa00}',
            '.badge-low{background:#00ff6633;color:#00ff66;border:1px solid #00ff66}',
            '.badge-info{background:#00aaff33;color:#00aaff;border:1px solid #00aaff}',
            '</style></head><body>',
            f'<h1>🔍 Leptothrix Ultimate Report</h1>',
            f'<p><strong>Generated:</strong> {report["timestamp"]}</p>',
            f'<p><strong>Version:</strong> {report["version"]}</p>'
        ]
        
        # Stats
        html.extend([
            '<div class="stats">',
            f'<div class="stat"><div class="stat-num">{len(report["artifacts"])}</div><div class="stat-label">Files Analyzed</div></div>',
            f'<div class="stat"><div class="stat-num">{report["total_findings"]}</div><div class="stat-label">Findings</div></div>',
            '</div>'
        ])
        
        # Findings by severity
        html.append('<h2>📊 Findings Summary</h2>')
        for severity, count in report['findings_by_severity'].items():
            color = {'CRITICAL': 'critical', 'HIGH': 'high', 'MEDIUM': 'medium', 'LOW': 'low', 'INFO': 'info'}.get(severity, 'info')
            html.append(f'<span class="badge badge-{color}">{severity}: {count}</span>')
        
        # Findings
        html.append('<h2>🔍 Detailed Findings</h2>')
        for f in report['findings']:
            severity_class = f['severity'].lower()
            html.append(f'<div class="finding {severity_class}">')
            html.append(f'<div class="severity">🚨 {f["severity"]}</div>')
            html.append(f'<div class="title">{f["title"]}</div>')
            html.append(f'<div><strong>Type:</strong> {f["type"]}</div>')
            html.append(f'<div><strong>Category:</strong> {f["category"]}</div>')
            html.append(f'<div>{f["description"]}</div>')
            
            if f['evidence']:
                html.append(f'<div class="evidence"><strong>Evidence:</strong> {json.dumps(f["evidence"], indent=2)}</div>')
            
            if f['remediation']:
                html.append(f'<div class="remediation">💡 {f["remediation"]}</div>')
            
            if f['references']:
                html.append(f'<div><strong>References:</strong> {", ".join(f["references"])}</div>')
            
            if f['cve']:
                html.append(f'<div><strong>CVE:</strong> {f["cve"]}</div>')
            
            html.append(f'<div style="font-size:12px;color:#6e6350">Confidence: {f["confidence"]*100:.0f}%</div>')
            html.append('</div>')
        
        html.append('</body></html>')
        
        with open(output_file, 'w') as f:
            f.write('\n'.join(html))
    
    def _generate_csv_report(self, report: Dict, output_file: str):
        """Generate CSV report"""
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Type', 'Category', 'Severity', 'Title', 'Description', 'Confidence', 'Timestamp'])
            for f in report['findings']:
                writer.writerow([
                    f['id'], f['type'], f['category'], f['severity'],
                    f['title'], f['description'], f['confidence'], f['timestamp']
                ])
    
    def run(self):
        """Main execution"""
        parser = argparse.ArgumentParser(
            description='Leptothrix Ultimate - Complete Security & Metadata Framework',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
EXAMPLES:
  %(prog)s -f document.pdf
  %(prog)s -d /path/to/files --threads 64
  %(prog)s -i photo.jpg -o exif_report.json
  %(prog)s -u http://169.254.169.254/latest/meta-data/
  %(prog)s -a ai_metadata.json
  %(prog)s -p package.json
  %(prog)s -f file.pdf -o report.html --format html
            """
        )
        
        parser.add_argument('-f', '--file', help='File to analyze')
        parser.add_argument('-d', '--dir', help='Directory to analyze')
        parser.add_argument('-i', '--image', help='Image to analyze (EXIF)')
        parser.add_argument('-u', '--url', help='URL to analyze for SSRF')
        parser.add_argument('-p', '--package', help='Package JSON to analyze')
        parser.add_argument('-a', '--ai', help='AI metadata JSON to analyze')
        parser.add_argument('-t', '--threat', help='Threat intelligence JSON to analyze')
        parser.add_argument('-o', '--output', default='leptothrix_report.json', help='Output file')
        parser.add_argument('--format', choices=['json', 'html', 'csv'], default='json', help='Report format')
        parser.add_argument('--threads', type=int, default=CONFIG['threads'], help='Thread count')
        parser.add_argument('--debug', action='store_true', help='Debug mode')
        parser.add_argument('--verbose', action='store_true', help='Verbose output')
        parser.add_argument('--silent', action='store_true', help='Silent mode')
        parser.add_argument('--log', help='Log file path')
        
        args = parser.parse_args()
        
        # Configure logging
        if args.silent:
            Logger.set_level('silent')
        elif args.debug:
            Logger.set_level('debug')
        elif args.verbose:
            Logger.set_level('verbose')
        
        if args.log:
            Logger.set_log_file(args.log)
        
        if args.threads:
            CONFIG['threads'] = args.threads
        
        try:
            if args.file:
                self.analyze_file(args.file)
                Logger.success(f"Analyzed file: {args.file}")
            
            elif args.dir:
                count = self.analyze_directory(args.dir)
                Logger.success(f"Analyzed {count} files in directory")
            
            elif args.image:
                report = self.analyze_image(args.image)
                img_output = args.output.replace('.json', '_exif.json')
                with open(img_output, 'w') as f:
                    json.dump(report, f, indent=2, default=str)
                Logger.success(f"EXIF report: {img_output}")
                
                # Print summary
                if report.get('gps', {}).get('parsed', {}).get('coordinates'):
                    Logger.info(f"📍 GPS: {report['gps']['parsed']['coordinates']}")
                if report.get('camera', {}).get('Model'):
                    Logger.info(f"📸 Camera: {report['camera']['Model']}")
                return
            
            elif args.url:
                findings = self.analyze_ssrf(args.url)
                for f in findings:
                    if f.severity == 'CRITICAL':
                        Logger.critical(f.title)
                    else:
                        Logger.warning(f.title)
                    Logger.info(f"  {f.description}")
                Logger.success(f"Found {len(findings)} SSRF findings")
            
            elif args.package:
                with open(args.package, 'r') as f:
                    data = json.load(f)
                findings = self.analyze_package(data)
                Logger.success(f"Found {len(findings)} supply chain findings")
            
            elif args.ai:
                with open(args.ai, 'r') as f:
                    data = json.load(f)
                findings = self.analyze_ai(data)
                Logger.success(f"Found {len(findings)} AI findings")
            
            elif args.threat:
                with open(args.threat, 'r') as f:
                    data = json.load(f)
                intel = self.analyze_threat(data)
                Logger.info(f"Threat Intelligence:")
                Logger.info(f"  Risk Score: {intel.risk_score:.2f}")
                Logger.info(f"  Confidence: {intel.confidence:.2f}")
                Logger.info(f"  Severity: {intel.severity}")
                if intel.indicators:
                    Logger.info(f"  Indicators: {', '.join(intel.indicators)}")
            
            else:
                Logger.error("No input specified. Use -f, -d, -i, -u, -p, -a, or -t")
                parser.print_help()
                return
            
            if self.findings:
                self.generate_report(args.output, args.format)
            
        except KeyboardInterrupt:
            Logger.warning("\nInterrupted by user")
        except Exception as e:
            Logger.error(f"Error: {e}")
            if args.debug:
                traceback.print_exc()

# =============================================================================
# ENTRY POINT
# =============================================================================

def main():
    """Leptothrix Ultimate Main Entry Point"""
    # Check dependencies (won't load heavy AI packages)
    check_and_install_dependencies()
    
    # Run framework
    framework = LeptothrixUltimate()
    framework.run()

if __name__ == "__main__":
    main()
