vf6xx_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: vf6xx_vector_nvic,
)

libvf6xx_sources = files(
	'ccm.c',
	'gpio.c',
	'iomuxc.c',
	'uart.c',
)

libvf6xx_compile_args = [
	'-mfloat-abi=hard',
	'-mfpu=fpv4-sp-d16',
	'-mcpu=cortex-m4',
	'-mthumb',
	'-DVF6XX',
]

libvf6xx = static_library(
	'opencm3_vf6xx',
	libvf6xx_sources,
	c_args: libvf6xx_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [vf6xx_cm3],
	pic: false,
)

libopencm3_vf6xx = declare_dependency(
	compile_args: libvf6xx_compile_args,
	include_directories: common_includes,
	link_with: libvf6xx,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_vf6xx', libopencm3_vf6xx)
