nrf51_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: nrf51_vector_nvic,
)

libnrf51_sources = files(
	'clock.c',
	'radio.c',
	'../common/clock_common.c',
	'../common/gpio.c',
	'../common/i2c_common.c',
	'../common/ppi.c',
	'../common/radio_common.c',
	'../common/rtc.c',
	'../common/timer.c',
	'../common/uart.c',
)

libnrf51_compile_args = [
	'-msoft-float',
	'-mcpu=cortex-m0',
	'-mthumb',
	'-DNRF51',
]

libnrf51 = static_library(
	'opencm3_nrf51',
	libnrf51_sources,
	c_args: libnrf51_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		nrf51_cm3,
	],
	pic: false,
)

libopencm3_nrf51 = declare_dependency(
	compile_args: libnrf51_compile_args,
	include_directories: common_includes,
	link_with: libnrf51,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_nrf51', libopencm3_nrf51)
