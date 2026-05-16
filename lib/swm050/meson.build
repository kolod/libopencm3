swm050_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: swm050_vector_nvic,
)

libswm050_sources = files(
	'clk.c',
	'flash.c',
	'gpio.c',
	'pwr.c',
	'syscon.c',
	'timer.c',
	'wdt.c',
)

libswm050_compile_args = [
	'-mcpu=cortex-m0',
	'-mthumb',
	'-DSWM050',
]

libswm050 = static_library(
	'opencm3_swm050',
	libswm050_sources,
	c_args: libswm050_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [swm050_cm3],
	pic: false,
)

libopencm3_swm050 = declare_dependency(
	compile_args: libswm050_compile_args,
	include_directories: common_includes,
	link_with: libswm050,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_swm050', libopencm3_swm050)
