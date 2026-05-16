efm32lg_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: efm32lg_vector_nvic,
)

libefm32lg_common_sources = files(
	'../common/acmp_common.c',
	'../common/adc_common.c',
	'../common/burtc_common.c',
	'../common/cmu_common.c',
	'../common/dac_common.c',
	'../common/dma_common.c',
	'../common/emu_common.c',
	'../common/gpio_common.c',
	'../common/i2c_common.c',
	'../common/letimer_common.c',
	'../common/msc_common.c',
	'../common/prs_common.c',
	'../common/rmu_common.c',
	'../common/rtc_common.c',
	'../common/timer_common.c',
	'../common/usart_common.c',
	'../common/wdog_common.c',
)

libefm32lg_compile_args = [
	'-mcpu=cortex-m3',
	'-mthumb',
	'-DEFM32LG',
]

libefm32lg = static_library(
	'opencm3_efm32lg',
	[
		libefm32lg_common_sources,
		usb_efm32_sources,
	],
	c_args: libefm32lg_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		efm32lg_cm3,
		usb_common,
	],
	pic: false,
)

libopencm3_efm32lg = declare_dependency(
	compile_args: libefm32lg_compile_args,
	include_directories: common_includes,
	link_with: libefm32lg,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_efm32lg', libopencm3_efm32lg)
