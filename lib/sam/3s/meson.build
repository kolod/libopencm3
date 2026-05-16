sam3s_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: sam3s_vector_nvic,
)

libsam3s_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DSAM3S',
]

libsam3s = static_library(
	'opencm3_sam3s',
	[
		libsam_gpio_common_all_sources,
		libsam_gpio_common_3n3s_sources,
		libsam_pmc_sources,
		libsam_usart_common_all_sources,
		libsam_usart_common_3_sources,
	],
	c_args: libsam3s_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [sam3s_cm3],
	pic: false,
)

libopencm3_sam3s = declare_dependency(
	compile_args: libsam3s_compile_args,
	include_directories: common_includes,
	link_with: libsam3s,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_sam3s', libopencm3_sam3s)
