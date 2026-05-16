efm32gg_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: efm32gg_vector_nvic,
)

libefm32gg_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DEFM32GG',
]

libefm32gg = static_library(
	'opencm3_efm32gg',
	[],
	c_args: libefm32gg_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		efm32gg_cm3,
	],
	pic: false,
)

libopencm3_efm32gg = declare_dependency(
	compile_args: libefm32gg_compile_args,
	include_directories: common_includes,
	link_with: libefm32gg,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_efm32gg', libopencm3_efm32gg)
