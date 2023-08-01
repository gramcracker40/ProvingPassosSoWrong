
$file_name = "application-event-log.txt"
$log_file = Get-Content -Path $file_name | Select-Object -Skip 1

$start = "01:34:00"
$end = "01:39:59"

$start_object = [DateTime]::ParseExact($start, "HH:mm:ss", $null)
$end_object = [DateTime]::ParseExact($end, "HH:mm:ss", $null)

$count = 0
foreach ($line in $log_file){
    $temp = $line -split "\t"
    $entry_time = [DateTime]::ParseExact($temp[2], "h:m:s tt", $null)
    if ($entry_time -gt $start_object -and $entry_time -lt $end_object){
        $count++
    }
}

Write-Host "Total count of log entries between $start and $end was --> $count"