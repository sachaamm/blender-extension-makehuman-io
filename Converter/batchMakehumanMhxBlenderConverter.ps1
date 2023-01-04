$curDir = Get-Location

$curDirReplaced = $curDir.Path.Replace('\', '\\')
Write-Output "Current Directory"
Write-Output $curDirReplaced
$currentDate = Get-Date

$folderSeparator = "\\"

$underscore = "_"
$year = $currentDate.Year.ToString()
$month = $currentDate.Month.ToString()
$day = $currentDate.Day.ToString()
$hour = $currentDate.Hour.ToString()
$minute = $currentDate.Minute.ToString()
$seconds = $currentDate.Second.ToString()

$dateStr = $year + $underscore + $month + $underscore + $day + $underscore + $hour + $underscore + $minute + $underscore + $seconds

Write-Output "Date is "
Write-Output $dateStr

## Create the Export directory
$exportsFolderB = ".\Exports\"
$exportNewFolderPath = $exportsFolderB + $dateStr

Write-Output "Export new Folder"
Write-Output $exportNewFolderPath

New-Item -Path $exportNewFolderPath -ItemType Directory

Get-ChildItem "." -Filter *.mhx2 | 
Foreach-Object {
	$newfilename = $_.Name.substring(0, $_.Name.LastIndexOf('.'))

	$exportsFolder = "\\Exports\\"
	$fbxExtension = ".fbx"
	Write-Output "NewfileName"
	Write-Output $newfilename 

	$dateFolder = $dateStr + $folderSeparator
	
	$outputFilePath = $curDirReplaced + $exportsFolder + $dateFolder + $newfilename + $fbxExtension

	$inputFilePath = $_.FullName.Replace('\', '\\')
	Write-Output "InputFilePath"
	Write-Output $inputFilePath
	 
	Write-Output "OutputFilePath"
	Write-Output $outputFilePath

	blender --python ../importMhx2.py -- $inputFilePath $outputFilePath
}

Pause