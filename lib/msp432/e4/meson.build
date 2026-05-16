msp432e4_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: msp432e4_vector_nvic,
)

libmsp432e4_sources = files(
	'gpio.c',
	'systemcontrol.c',
)

libmsp432e4_compile_args = [
	'-mfloat-abi=hard',
	'-mfpu=fpv4-sp-d16',
	'-mcpu=cortex-m4',
	'-mthumb',
	'-DMSP432E4',
]

libmsp432e4 = static_library(
	'opencm3_msp432e4',
	libmsp432e4_sources,
	c_args: libmsp432e4_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		msp432e4_cm3,
	],
	pic: false,
)

libopencm3_msp432e4 = declare_dependency(
	compile_args: libmsp432e4_compile_args,
	include_directories: common_includes,
	link_with: libmsp432e4,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_msp432e4', libopencm3_msp432e4)
