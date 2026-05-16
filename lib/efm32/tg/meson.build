efm32tg_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: efm32tg_vector_nvic,
)

libefm32tg_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DEFM32TG',
]

libefm32tg = static_library(
	'opencm3_efm32tg',
	[],
	c_args: libefm32tg_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		efm32tg_cm3,
	],
	pic: false,
)

libopencm3_efm32tg = declare_dependency(
	compile_args: libefm32tg_compile_args,
	include_directories: common_includes,
	link_with: libefm32tg,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_efm32tg', libopencm3_efm32tg)
