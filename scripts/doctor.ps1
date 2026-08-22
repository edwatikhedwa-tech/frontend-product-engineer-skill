param(
  [switch]$Quiet
)

$ErrorActionPreference = 'Stop'
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptRoot
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  Write-Error 'Python is required to run doctor.py.'
  exit 2
}

if ($Quiet) {
  & $python.Source (Join-Path $scriptRoot 'doctor.py') | Out-Null
} else {
  & $python.Source (Join-Path $scriptRoot 'doctor.py')
}
exit $LASTEXITCODE
