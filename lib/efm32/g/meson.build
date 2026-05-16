efm32g_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: efm32g_vector_nvic,
)

libefm32g_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DEFM32G',
]

libefm32g = static_library(
	'opencm3_efm32g',
	[],
	c_args: libefm32g_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		efm32g_cm3,
	],
	pic: false,
)

libopencm3_efm32g = declare_dependency(
	compile_args: libefm32g_compile_args,
	include_directories: common_includes,
	link_with: libefm32g,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_efm32g', libopencm3_efm32g)
