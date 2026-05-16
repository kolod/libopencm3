lpc17xx_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: lpc17xx_vector_nvic,
)

liblpc17xx_sources = files(
	'gpio.c',
	'pwr.c',
)

liblpc17xx_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DLPC17XX',
]

liblpc17xx = static_library(
	'opencm3_lpc17xx',
	liblpc17xx_sources,
	c_args: liblpc17xx_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		lpc17xx_cm3,
	],
	pic: false,
)

libopencm3_lpc17xx = declare_dependency(
	compile_args: liblpc17xx_compile_args,
	include_directories: common_includes,
	link_with: liblpc17xx,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_lpc17xx', libopencm3_lpc17xx)
