subdirs = {
	'gd32f1x0': 'f1x0',
}

foreach target_platform : target_platforms
	if target_platform in subdirs
		subdir(subdirs[target_platform])
	endif
endforeach
