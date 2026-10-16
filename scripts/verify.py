"""Verify package identity and source integrity before publishing."""
from pathlib import Path
import hashlib
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
source = (root / "content/LeaAmplifierCustom.qplug").read_bytes()
assert hashlib.sha256(source).hexdigest() == "084f58cddf487509b44ae889944c2a6b590e862093b36e25922635442f65d4f9", "Update the reviewed source digest for an intentional plugin revision"
info = re.search(r"PluginInfo\s*=\s*\{(.*?)\}", source.decode("utf-8-sig"), re.S)[1]
version = re.search(r'\bVersion\s*=\s*"([^"]+)"', info)[1]
project = ET.parse(root / "LeaAmplifiers.csproj").getroot()
assert version == project.findtext("PropertyGroup/Version"), "Plugin/package version mismatch"
assert project.findtext("PropertyGroup/PackageId") == "JoshuaSmall.Qsys.LeaAmplifiers"
assert (root / "icon.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
assert "https://joshua-small.github.io/qsys-lea-amplifiers/registration/joshuasmall.qsys.leaamplifiers/index.json" in (root / "README.md").read_text()
print("Verified", "LeaAmplifierCustom.qplug", version, hashlib.sha256(source).hexdigest())
