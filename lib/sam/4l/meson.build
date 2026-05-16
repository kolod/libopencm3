sam4l_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: sam4l_vector_nvic,
)

libsam4l_sources = files(
	'adcife.c',
	'gpio.c',
	'pm.c',
	'scif.c',
	'usart.c',
)

libsam4l_compile_args = [
	'-msoft-float',
	'-mcpu=cortex-m4',
	'-mthumb',
	'-DSAM4L',
]

libsam4l = static_library(
	'opencm3_sam4l',
	[
		libsam4l_sources,
		libsam_usart_common_all_sources,
	],
	c_args: libsam4l_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [sam4l_cm3],
	pic: false,
)

libopencm3_sam4l = declare_dependency(
	compile_args: libsam4l_compile_args,
	include_directories: common_includes,
	link_with: libsam4l,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_sam4l', libopencm3_sam4l)
