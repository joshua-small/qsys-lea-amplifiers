"""Verify reviewed source bytes and product/release identity before packaging."""
import argparse
import hashlib
from pathlib import Path
from package_checks import check_identity

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--release-tag", help="Exact release tag; must equal v + source and project version")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = (root / "content/LeaAmplifierCustom.qplug").read_bytes()
if hashlib.sha256(source).hexdigest() != "084f58cddf487509b44ae889944c2a6b590e862093b36e25922635442f65d4f9":
    raise SystemExit("Update the reviewed source digest for an intentional plugin revision")
try:
    version = check_identity(source.decode("utf-8-sig"), (root / "LeaAmplifiers.csproj").read_text(),
        "JoshuaSmall.Qsys.LeaAmplifiers", args.release_tag)
except ValueError as error:
    raise SystemExit(str(error)) from error
if not (root / "icon.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
    raise SystemExit("Invalid package icon")
if "https://joshua-small.github.io/qsys-lea-amplifiers/registration/joshuasmall.qsys.leaamplifiers/index.json" not in (root / "README.md").read_text():
    raise SystemExit("README Library feed does not match package identity")
print("Verified", "LeaAmplifierCustom.qplug", version, hashlib.sha256(source).hexdigest())
