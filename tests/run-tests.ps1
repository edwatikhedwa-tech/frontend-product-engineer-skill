$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

Write-Output '== Python compile =='
python -m py_compile scripts\_common.py scripts\install.py scripts\sync.py scripts\doctor.py scripts\new_case.py

Write-Output '== Doctor =='
python scripts\doctor.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Output '== Installer plan =='
python scripts\install.py --agent all --scope global --plan | Out-Null
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Output '== New case dry-run =='
python scripts\new_case.py 'Verification case' --dry-run | Out-Null
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Output '== Sync check =='
python scripts\sync.py --check
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Output 'ALL LOCAL CHECKS PASSED'
