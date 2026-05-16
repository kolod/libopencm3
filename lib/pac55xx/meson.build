pac55xx_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: pac55xx_vector_nvic,
)

libpac55xx_sources = files(
	'can.c',
	'ccs.c',
	'gpio.c',
	'memctl.c',
	'usart.c',
)

libpac55xx_compile_args = [
	'-mfloat-abi=hard',
	'-mfpu=fpv4-sp-d16',
	'-mcpu=cortex-m4',
	'-mthumb',
	'-DPAC55XX',
]

libpac55xx = static_library(
	'opencm3_pac55xx',
	libpac55xx_sources,
	c_args: libpac55xx_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [pac55xx_cm3],
	pic: false,
)

libopencm3_pac55xx = declare_dependency(
	compile_args: libpac55xx_compile_args,
	include_directories: common_includes,
	link_with: libpac55xx,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_pac55xx', libopencm3_pac55xx)
