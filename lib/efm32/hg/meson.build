efm32hg_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: efm32hg_vector_nvic,
)

libefm32hg_sources = files(
	'cmu.c',
	'../common/gpio_common.c',
	'../common/timer_common.c',
)

libefm32hg_compile_args = [
	'-mcpu=cortex-m0plus',
	'-mthumb',
	'-DEFM32HG',
]

libefm32hg = static_library(
	'opencm3_efm32hg',
	[
		libefm32hg_sources,
		usb_efm32hg_sources,
	],
	c_args: libefm32hg_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		efm32hg_cm3,
		usb_stm32_dwc,
	],
	pic: false,
)

libopencm3_efm32hg = declare_dependency(
	compile_args: libefm32hg_compile_args,
	include_directories: common_includes,
	link_with: libefm32hg,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_efm32hg', libopencm3_efm32hg)
