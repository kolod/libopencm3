samd_cm3 = declare_dependency(
	sources: cm3_sources,
	include_directories: cm3_includes,
	dependencies: samd_vector_nvic,
)

libsamd_sources = files('port.c')

libsamd_compile_args = [
	'-mcpu=cortex-m0plus',
	'-mthumb',
	'-DSAMD',
]

libsamd = static_library(
	'opencm3_samd',
	libsamd_sources,
	c_args: libsamd_compile_args,
	include_directories: common_includes,
	implicit_include_directories: false,
	dependencies: [samd_cm3],
	pic: false,
)

libopencm3_samd = declare_dependency(
	compile_args: libsamd_compile_args,
	include_directories: common_includes,
	link_with: libsamd,
	link_args: [f'-L@locm3_ld_script_path@'],
)

meson.override_dependency('opencm3_samd', libopencm3_samd)
