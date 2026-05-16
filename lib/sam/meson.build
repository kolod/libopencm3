libsam_gpio_common_all_sources = files('common/gpio_common_all.c')
libsam_gpio_common_3a3u3x_sources = files('common/gpio_common_3a3u3x.c')
libsam_gpio_common_3n3s_sources = files('common/gpio_common_3n3s.c')
libsam_pmc_sources = files('common/pmc.c')
libsam_usart_common_all_sources = files('common/usart_common_all.c')
libsam_usart_common_3_sources = files('common/usart_common_3.c')

if 'sam3a' in target_platforms
	subdir('3a')
endif
if 'sam3n' in target_platforms
	subdir('3n')
endif
if 'sam3s' in target_platforms
	subdir('3s')
endif
if 'sam3u' in target_platforms
	subdir('3u')
endif
if 'sam3x' in target_platforms
	subdir('3x')
endif
if 'sam4l' in target_platforms
	subdir('4l')
endif
if 'samd' in target_platforms
	subdir('d')
endif
