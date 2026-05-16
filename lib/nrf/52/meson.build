nrf52_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: nrf52_vector_nvic,
)

libnrf52_sources = files(
	'i2c.c',
	'../common/clock_common.c',
	'../common/gpio.c',
	'../common/i2c_common.c',
	'../common/ppi.c',
	'../common/radio_common.c',
	'../common/rtc.c',
	'../common/timer.c',
	'../common/uart.c',
)

libnrf52_compile_args = [
	'-mfloat-abi=hard',
	'-mfpu=fpv4-sp-d16',
	'-mcpu=cortex-m4',
	'-mthumb',
	'-DNRF52',
]

libnrf52 = static_library(
	'opencm3_nrf52',
	libnrf52_sources,
	c_args: libnrf52_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		nrf52_cm3,
	],
	pic: false,
)

libopencm3_nrf52 = declare_dependency(
	compile_args: libnrf52_compile_args,
	include_directories: common_includes,
	link_with: libnrf52,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_nrf52', libopencm3_nrf52)
