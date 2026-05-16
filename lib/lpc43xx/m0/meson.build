lpc43xxm0_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: lpc43xxm0_vector_nvic,
)

liblpc43xxm0_compile_args = [
	'-mcpu=cortex-m0',
	'-mthumb',
	'-DLPC43XX',
	'-DLPC43XX_M0',
]

liblpc43xxm0 = static_library(
	'opencm3_lpc43xxm0',
	lpc43xx_common_sources,
	c_args: liblpc43xxm0_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [
		lpc43xxm0_cm3,
	],
	pic: false,
)

libopencm3_lpc43xxm0 = declare_dependency(
	compile_args: liblpc43xxm0_compile_args,
	include_directories: common_includes,
	link_with: liblpc43xxm0,
	link_args: [
		f'-L@locm3_ld_script_path@',
	],
)

meson.override_dependency('opencm3_lpc43xxm0', libopencm3_lpc43xxm0)
