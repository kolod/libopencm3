gd32f1x0_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: gd32f1x0_vector_nvic,
)

libgd32f1x0_sources = files(
	'flash.c',
	'rcc.c',
	'../../stm32/common/flash_common_all.c',
	'../../stm32/common/flash_common_f.c',
	'../../stm32/common/flash_common_f01.c',
	'../../stm32/common/gpio_common_all.c',
	'../../stm32/common/gpio_common_f0234.c',
	'../../stm32/common/rcc_common_all.c',
)

libgd32f1x0_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DGD32F1X0',
]

libgd32f1x0 = static_library(
	'opencm3_gd32f1x0',
	libgd32f1x0_sources,
	c_args: libgd32f1x0_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		gd32f1x0_cm3,
	],
	pic: false,
)

libopencm3_gd32f1x0 = declare_dependency(
	compile_args: libgd32f1x0_compile_args,
	include_directories: common_includes,
	link_with: libgd32f1x0,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_gd32f1x0', libopencm3_gd32f1x0)
