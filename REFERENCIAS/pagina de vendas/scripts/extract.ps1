Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$zipPath = "c:\Users\jeanc_pmc3uv0\Documents\curso - THIAGO\FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.zip"
$outputPath = "c:\Users\jeanc_pmc3uv0\Documents\curso - THIAGO\framework.md"

$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
$entry = $zip.Entries[0]
$stream = $entry.Open()
$fs = [System.IO.File]::Create($outputPath)
$stream.CopyTo($fs)
$fs.Dispose()
$stream.Dispose()
$zip.Dispose()

Write-Output "Successfully extracted entry $($entry.Name) to $outputPath"
