sam3a_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: sam3a_vector_nvic,
)

libsam3a_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DSAM3A',
]

libsam3a = static_library(
	'opencm3_sam3a',
	[
		libsam_gpio_common_all_sources,
		libsam_gpio_common_3a3u3x_sources,
		libsam_pmc_sources,
		libsam_usart_common_all_sources,
		libsam_usart_common_3_sources,
	],
	c_args: libsam3a_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [sam3a_cm3],
	pic: false,
)

libopencm3_sam3a = declare_dependency(
	compile_args: libsam3a_compile_args,
	include_directories: common_includes,
	link_with: libsam3a,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_sam3a', libopencm3_sam3a)
