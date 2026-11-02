# Pack pinecrest-knowledge.mcpb.
#
# An .mcpb is a zip with manifest.json at the ROOT (not inside a folder).
# Built with .NET rather than Compress-Archive because Compress-Archive writes
# Windows backslashes into entry paths ("server\index.js"), which is invalid per the
# ZIP spec and fails to extract cleanly on macOS.

$ErrorActionPreference = 'Stop'
$dir = $PSScriptRoot
$out = Join-Path $dir 'pinecrest-knowledge.mcpb'

$files = @(
    @{ Source = Join-Path $dir 'manifest.json';      Entry = 'manifest.json' }
    @{ Source = Join-Path $dir 'server\index.js';    Entry = 'server/index.js' }
)

foreach ($f in $files) {
    if (-not (Test-Path $f.Source)) { throw "missing: $($f.Source)" }
}

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

if (Test-Path $out) { Remove-Item $out -Force }

$zip = [System.IO.Compression.ZipFile]::Open($out, 'Create')
try {
    foreach ($f in $files) {
        $entry = $zip.CreateEntry($f.Entry, [System.IO.Compression.CompressionLevel]::Optimal)
        $in = [System.IO.File]::OpenRead($f.Source)
        try {
            $s = $entry.Open()
            try { $in.CopyTo($s) } finally { $s.Dispose() }
        } finally { $in.Dispose() }
    }
} finally { $zip.Dispose() }

Write-Host "built $out"
$check = [System.IO.Compression.ZipFile]::OpenRead($out)
$check.Entries | ForEach-Object { "  {0,7} bytes  {1}" -f $_.Length, $_.FullName }
$check.Dispose()
