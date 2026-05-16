lpc13xx_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: lpc13xx_vector_nvic,
)

liblpc13xx_sources = files(
	'gpio.c',
)

liblpc13xx_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DLPC13XX',
]

liblpc13xx = static_library(
	'opencm3_lpc13xx',
	liblpc13xx_sources,
	c_args: liblpc13xx_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		lpc13xx_cm3,
	],
	pic: false,
)

libopencm3_lpc13xx = declare_dependency(
	compile_args: liblpc13xx_compile_args,
	include_directories: common_includes,
	link_with: liblpc13xx,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_lpc13xx', libopencm3_lpc13xx)
