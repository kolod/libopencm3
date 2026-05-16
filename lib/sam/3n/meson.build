sam3n_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: sam3n_vector_nvic,
)

libsam3n_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DSAM3N',
]

libsam3n = static_library(
	'opencm3_sam3n',
	[
		libsam_gpio_common_all_sources,
		libsam_gpio_common_3n3s_sources,
		libsam_pmc_sources,
		libsam_usart_common_all_sources,
		libsam_usart_common_3_sources,
	],
	c_args: libsam3n_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [sam3n_cm3],
	pic: false,
)

libopencm3_sam3n = declare_dependency(
	compile_args: libsam3n_compile_args,
	include_directories: common_includes,
	link_with: libsam3n,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_sam3n', libopencm3_sam3n)
