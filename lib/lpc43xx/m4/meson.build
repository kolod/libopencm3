lpc43xxm4_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: lpc43xxm4_vector_nvic,
)

liblpc43xxm4_compile_args = [
	'-mfloat-abi=hard',
	'-mfpu=fpv4-sp-d16',
	'-mcpu=cortex-m4',
	'-mthumb',
	'-DLPC43XX',
	'-DLPC43XX_M4',
]

liblpc43xxm4 = static_library(
	'opencm3_lpc43xxm4',
	[
		lpc43xx_common_sources,
		files('../ipc.c'),
	],
	c_args: liblpc43xxm4_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		lpc43xxm4_cm3,
	],
	pic: false,
)

libopencm3_lpc43xxm4 = declare_dependency(
	compile_args: liblpc43xxm4_compile_args,
	include_directories: common_includes,
	link_with: liblpc43xxm4,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_lpc43xxm4', libopencm3_lpc43xxm4)
