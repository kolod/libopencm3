lm3s_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: lm3s_vector_nvic,
)

liblm3s_sources = files(
	'gpio.c',
	'rcc.c',
	'usart.c',
)

liblm3s_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DLM3S',
]

liblm3s = static_library(
	'opencm3_lm3s',
	liblm3s_sources,
	c_args: liblm3s_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		lm3s_cm3,
	],
	pic: false,
)

libopencm3_lm3s = declare_dependency(
	compile_args: liblm3s_compile_args,
	include_directories: common_includes,
	link_with: liblm3s,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_lm3s', libopencm3_lm3s)
